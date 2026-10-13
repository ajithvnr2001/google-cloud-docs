---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient
title: Class AlloyDBAdminClient (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:50:11.055574+00:00
---

# Class AlloyDBAdminClient (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AlloyDBAdminClient (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-alloydb/google-cloud-alloydb/src/main/java/com/google/cloud/alloydb/v1/AlloyDBAdminClient.java)| [Product Reference](https://cloud.google.com/alloydb/)| [REST Documentation](https://cloud.google.com/alloydb/docs/reference/rest)  
---|---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = alloyDBAdminClient.getCluster(name);
     }
     

Note: close() needs to be called on the AlloyDBAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListClusters |  Lists Clusters in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClusters(ListClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClusters(LocationName parent) 
  * listClusters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClustersPagedCallable() 
  * listClustersCallable() 

  
GetCluster |  Gets details of a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCluster(GetClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCluster(ClusterName name) 
  * getCluster(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClusterCallable() 

  
CreateCluster |  Creates a new Cluster in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClusterAsync(CreateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createClusterAsync(LocationName parent, Cluster cluster, String clusterId) 
  * createClusterAsync(String parent, Cluster cluster, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClusterOperationCallable() 
  * createClusterCallable() 

  
UpdateCluster |  Updates the parameters of a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateClusterAsync(UpdateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateClusterAsync(Cluster cluster, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateClusterOperationCallable() 
  * updateClusterCallable() 

  
ExportCluster |  Exports data from the cluster. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportClusterAsync(ExportClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportClusterAsync(ClusterName name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions) 
  * exportClusterAsync(String name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportClusterOperationCallable() 
  * exportClusterCallable() 

  
ImportCluster |  Imports data to the cluster. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importClusterAsync(ImportClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importClusterAsync(ClusterName name, String gcsUri, String database, String user) 
  * importClusterAsync(String name, String gcsUri, String database, String user) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importClusterOperationCallable() 
  * importClusterCallable() 

  
UpgradeCluster |  Upgrades a single Cluster. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * upgradeClusterAsync(UpgradeClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * upgradeClusterAsync(ClusterName name, DatabaseVersion version) 
  * upgradeClusterAsync(String name, DatabaseVersion version) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * upgradeClusterOperationCallable() 
  * upgradeClusterCallable() 

  
DeleteCluster |  Deletes a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteClusterAsync(DeleteClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteClusterAsync(ClusterName name) 
  * deleteClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClusterOperationCallable() 
  * deleteClusterCallable() 

  
PromoteCluster |  Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * promoteClusterAsync(PromoteClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * promoteClusterAsync(ClusterName name) 
  * promoteClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * promoteClusterOperationCallable() 
  * promoteClusterCallable() 

  
SwitchoverCluster |  Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * switchoverClusterAsync(SwitchoverClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * switchoverClusterAsync(ClusterName name) 
  * switchoverClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * switchoverClusterOperationCallable() 
  * switchoverClusterCallable() 

  
RestoreCluster |  Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreClusterAsync(RestoreClusterRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreClusterOperationCallable() 
  * restoreClusterCallable() 

  
CreateSecondaryCluster |  Creates a cluster of type SECONDARY in the given location using the primary cluster as the source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSecondaryClusterAsync(CreateSecondaryClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSecondaryClusterAsync(LocationName parent, Cluster cluster, String clusterId) 
  * createSecondaryClusterAsync(String parent, Cluster cluster, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSecondaryClusterOperationCallable() 
  * createSecondaryClusterCallable() 

  
ListInstances |  Lists Instances in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInstances(ClusterName parent) 
  * listInstances(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
GetInstance |  Gets details of a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInstance(GetInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInstance(InstanceName name) 
  * getInstance(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInstanceCallable() 

  
CreateInstance |  Creates a new Instance in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstanceAsync(CreateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstanceAsync(ClusterName parent, Instance instance, String instanceId) 
  * createInstanceAsync(String parent, Instance instance, String instanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstanceOperationCallable() 
  * createInstanceCallable() 

  
CreateSecondaryInstance |  Creates a new SECONDARY Instance in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSecondaryInstanceAsync(CreateSecondaryInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSecondaryInstanceAsync(ClusterName parent, Instance instance, String instanceId) 
  * createSecondaryInstanceAsync(String parent, Instance instance, String instanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSecondaryInstanceOperationCallable() 
  * createSecondaryInstanceCallable() 

  
BatchCreateInstances |  Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateInstancesAsync(BatchCreateInstancesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateInstancesOperationCallable() 
  * batchCreateInstancesCallable() 

  
UpdateInstance |  Updates the parameters of a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInstanceAsync(UpdateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateInstanceAsync(Instance instance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInstanceOperationCallable() 
  * updateInstanceCallable() 

  
DeleteInstance |  Deletes a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstanceAsync(DeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstanceAsync(InstanceName name) 
  * deleteInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstanceOperationCallable() 
  * deleteInstanceCallable() 

  
FailoverInstance |  Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * failoverInstanceAsync(FailoverInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * failoverInstanceAsync(InstanceName name) 
  * failoverInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * failoverInstanceOperationCallable() 
  * failoverInstanceCallable() 

  
InjectFault |  Injects fault in an instance. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * injectFaultAsync(InjectFaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * injectFaultAsync(InjectFaultRequest.FaultType faultType, InstanceName name) 
  * injectFaultAsync(InjectFaultRequest.FaultType faultType, String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * injectFaultOperationCallable() 
  * injectFaultCallable() 

  
RestartInstance |  Restart an Instance in a cluster. Imperative only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restartInstanceAsync(RestartInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restartInstanceAsync(InstanceName name) 
  * restartInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restartInstanceOperationCallable() 
  * restartInstanceCallable() 

  
ExecuteSql |  Executes a SQL statement in a database inside an AlloyDB instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * executeSql(ExecuteSqlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * executeSql(InstanceName instance, String database, String user, String sqlStatement, String password) 
  * executeSql(String instance, String database, String user, String sqlStatement, String password) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * executeSqlCallable() 

  
ListBackups |  Lists Backups in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(LocationName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsPagedCallable() 
  * listBackupsCallable() 

  
GetBackup |  Gets details of a single Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
CreateBackup |  Creates a new Backup in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupAsync(CreateBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackupAsync(LocationName parent, Backup backup, String backupId) 
  * createBackupAsync(String parent, Backup backup, String backupId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupOperationCallable() 
  * createBackupCallable() 

  
UpdateBackup |  Updates the parameters of a single Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupAsync(UpdateBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackupAsync(Backup backup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupOperationCallable() 
  * updateBackupCallable() 

  
DeleteBackup |  Deletes a single Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupAsync(DeleteBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupAsync(BackupName name) 
  * deleteBackupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupOperationCallable() 
  * deleteBackupCallable() 

  
ListSupportedDatabaseFlags |  Lists SupportedDatabaseFlags for a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSupportedDatabaseFlags(ListSupportedDatabaseFlagsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSupportedDatabaseFlags(LocationName parent) 
  * listSupportedDatabaseFlags(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSupportedDatabaseFlagsPagedCallable() 
  * listSupportedDatabaseFlagsCallable() 

  
GenerateClientCertificate |  Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateClientCertificate(GenerateClientCertificateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateClientCertificate(ClusterName parent) 
  * generateClientCertificate(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateClientCertificateCallable() 

  
GetConnectionInfo |  Get instance metadata used for a connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnectionInfo(GetConnectionInfoRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConnectionInfo(InstanceName parent) 
  * getConnectionInfo(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectionInfoCallable() 

  
ListUsers |  Lists Users in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUsers(ListUsersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUsers(ClusterName parent) 
  * listUsers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUsersPagedCallable() 
  * listUsersCallable() 

  
GetUser |  Gets details of a single User. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUser(GetUserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUser(UserName name) 
  * getUser(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserCallable() 

  
CreateUser |  Creates a new User in a given project, location, and cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUser(CreateUserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUser(ClusterName parent, User user, String userId) 
  * createUser(String parent, User user, String userId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserCallable() 

  
UpdateUser |  Updates the parameters of a single User. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUser(UpdateUserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUser(User user, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserCallable() 

  
DeleteUser |  Deletes a single User. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUser(DeleteUserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUser(UserName name) 
  * deleteUser(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserCallable() 

  
ListDatabases |  Lists Databases in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatabases(ListDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatabases(ClusterName parent) 
  * listDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatabasesPagedCallable() 
  * listDatabasesCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AlloyDBAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBAdminSettings alloyDBAdminSettings =
         AlloyDBAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create(alloyDBAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBAdminSettings alloyDBAdminSettings =
         AlloyDBAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create(alloyDBAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBAdminSettings alloyDBAdminSettings = AlloyDBAdminSettings.newHttpJsonBuilder().build();
     AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create(alloyDBAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AlloyDBAdminClient

## Static Methods 

### create()
    
    
    public static final AlloyDBAdminClient create()

Constructs an instance of AlloyDBAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AlloyDBAdminSettings settings)
    
    
    public static final AlloyDBAdminClient create(AlloyDBAdminSettings settings)

Constructs an instance of AlloyDBAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AlloyDBAdminStub stub)
    
    
    public static final AlloyDBAdminClient create(AlloyDBAdminStub stub)

Constructs an instance of AlloyDBAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(AlloyDBAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AlloyDBAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.stub.AlloyDBAdminStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient)` |   
  
## Constructors 

### AlloyDBAdminClient(AlloyDBAdminSettings settings)
    
    
    protected AlloyDBAdminClient(AlloyDBAdminSettings settings)

Constructs an instance of AlloyDBAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings)`  
  
  
### AlloyDBAdminClient(AlloyDBAdminStub stub)
    
    
    protected AlloyDBAdminClient(AlloyDBAdminStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AlloyDBAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.stub.AlloyDBAdminStub)`  
  
  
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
  
### batchCreateInstancesAsync(BatchCreateInstancesRequest request)
    
    
    public final OperationFuture<BatchCreateInstancesResponse,OperationMetadata> batchCreateInstancesAsync(BatchCreateInstancesRequest request)

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       BatchCreateInstancesRequest request =
           BatchCreateInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequests(CreateInstanceRequests.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       BatchCreateInstancesResponse response =
           alloyDBAdminClient.batchCreateInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### batchCreateInstancesCallable()
    
    
    public final UnaryCallable<BatchCreateInstancesRequest,Operation> batchCreateInstancesCallable()

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       BatchCreateInstancesRequest request =
           BatchCreateInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequests(CreateInstanceRequests.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.batchCreateInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchCreateInstancesOperationCallable()
    
    
    public final OperationCallable<BatchCreateInstancesRequest,BatchCreateInstancesResponse,OperationMetadata> batchCreateInstancesOperationCallable()

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       BatchCreateInstancesRequest request =
           BatchCreateInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequests(CreateInstanceRequests.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BatchCreateInstancesResponse, OperationMetadata> future =
           alloyDBAdminClient.batchCreateInstancesOperationCallable().futureCall(request);
       // Do something.
       BatchCreateInstancesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest),[BatchCreateInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createBackupAsync(@Nullable LocationName parent, Backup backup, String backupId)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(@Nullable LocationName parent, Backup backup, String backupId)

Creates a new Backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Backup backup = Backup.newBuilder().build();
       String backupId = "backupId2121930365";
       Backup response = alloyDBAdminClient.createBackupAsync(parent, backup, backupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)`  
Required. The resource being created  
`backupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createBackupAsync(CreateBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(CreateBackupRequest request)

Creates a new Backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Backup response = alloyDBAdminClient.createBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createBackupAsync(String parent, Backup backup, String backupId)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(String parent, Backup backup, String backupId)

Creates a new Backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Backup backup = Backup.newBuilder().build();
       String backupId = "backupId2121930365";
       Backup response = alloyDBAdminClient.createBackupAsync(parent, backup, backupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)`  
Required. The resource being created  
`backupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createBackupCallable()
    
    
    public final UnaryCallable<CreateBackupRequest,Operation> createBackupCallable()

Creates a new Backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.createBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupOperationCallable()
    
    
    public final OperationCallable<CreateBackupRequest,Backup,OperationMetadata> createBackupOperationCallable()

Creates a new Backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           alloyDBAdminClient.createBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = alloyDBAdminClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)`  
Required. The resource being created  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createClusterAsync(CreateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(CreateClusterRequest request)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = alloyDBAdminClient.createClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createClusterAsync(String parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(String parent, Cluster cluster, String clusterId)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = alloyDBAdminClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)`  
Required. The resource being created  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createClusterCallable()
    
    
    public final UnaryCallable<CreateClusterRequest,Operation> createClusterCallable()

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.createClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClusterOperationCallable()
    
    
    public final OperationCallable<CreateClusterRequest,Cluster,OperationMetadata> createClusterOperationCallable()

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.createClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createInstanceAsync(@Nullable ClusterName parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(@Nullable ClusterName parent, Instance instance, String instanceId)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           alloyDBAdminClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)`  
Required. The resource being created  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createInstanceAsync(CreateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(CreateInstanceRequest request)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Instance response = alloyDBAdminClient.createInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createInstanceAsync(String parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(String parent, Instance instance, String instanceId)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           alloyDBAdminClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)`  
Required. The resource being created  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createInstanceCallable()
    
    
    public final UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.createInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public final OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.createInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createSecondaryClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response =
           alloyDBAdminClient.createSecondaryClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object (the secondary cluster).  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryClusterAsync(CreateSecondaryClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createSecondaryClusterAsync(CreateSecondaryClusterRequest request)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryClusterRequest request =
           CreateSecondaryClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = alloyDBAdminClient.createSecondaryClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryClusterAsync(String parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createSecondaryClusterAsync(String parent, Cluster cluster, String clusterId)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response =
           alloyDBAdminClient.createSecondaryClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object (the secondary cluster).  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryClusterCallable()
    
    
    public final UnaryCallable<CreateSecondaryClusterRequest,Operation> createSecondaryClusterCallable()

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryClusterRequest request =
           CreateSecondaryClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.createSecondaryClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSecondaryClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSecondaryClusterOperationCallable()
    
    
    public final OperationCallable<CreateSecondaryClusterRequest,Cluster,OperationMetadata> createSecondaryClusterOperationCallable()

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryClusterRequest request =
           CreateSecondaryClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.createSecondaryClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSecondaryClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryInstanceAsync(@Nullable ClusterName parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createSecondaryInstanceAsync(@Nullable ClusterName parent, Instance instance, String instanceId)

Creates a new SECONDARY Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           alloyDBAdminClient.createSecondaryInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)`  
Required. The resource being created  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryInstanceAsync(CreateSecondaryInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> createSecondaryInstanceAsync(CreateSecondaryInstanceRequest request)

Creates a new SECONDARY Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryInstanceRequest request =
           CreateSecondaryInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Instance response = alloyDBAdminClient.createSecondaryInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryInstanceAsync(String parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createSecondaryInstanceAsync(String parent, Instance instance, String instanceId)

Creates a new SECONDARY Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           alloyDBAdminClient.createSecondaryInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)`  
Required. The resource being created  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createSecondaryInstanceCallable()
    
    
    public final UnaryCallable<CreateSecondaryInstanceRequest,Operation> createSecondaryInstanceCallable()

Creates a new SECONDARY Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryInstanceRequest request =
           CreateSecondaryInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.createSecondaryInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSecondaryInstanceOperationCallable()
    
    
    public final OperationCallable<CreateSecondaryInstanceRequest,Instance,OperationMetadata> createSecondaryInstanceOperationCallable()

Creates a new SECONDARY Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateSecondaryInstanceRequest request =
           CreateSecondaryInstanceRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.createSecondaryInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateSecondaryInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### createUser(@Nullable ClusterName parent, User user, String userId)
    
    
    public final User createUser(@Nullable ClusterName parent, User user, String userId)

Creates a new User in a given project, location, and cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       User user = User.newBuilder().build();
       String userId = "userId-836030906";
       User response = alloyDBAdminClient.createUser(parent, user, userId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)`  
Required. The resource being created  
`userId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### createUser(CreateUserRequest request)
    
    
    public final User createUser(CreateUserRequest request)

Creates a new User in a given project, location, and cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateUserRequest request =
           CreateUserRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setUserId("userId-836030906")
               .setUser(User.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       User response = alloyDBAdminClient.createUser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### createUser(String parent, User user, String userId)
    
    
    public final User createUser(String parent, User user, String userId)

Creates a new User in a given project, location, and cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       User user = User.newBuilder().build();
       String userId = "userId-836030906";
       User response = alloyDBAdminClient.createUser(parent, user, userId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)`  
Required. The resource being created  
`userId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### createUserCallable()
    
    
    public final UnaryCallable<CreateUserRequest,User> createUserCallable()

Creates a new User in a given project, location, and cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       CreateUserRequest request =
           CreateUserRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setUserId("userId-836030906")
               .setUser(User.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<User> future = alloyDBAdminClient.createUserCallable().futureCall(request);
       // Do something.
       User response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)>` |   
  
### deleteBackupAsync(@Nullable BackupName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(@Nullable BackupName name)

Deletes a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]");
       alloyDBAdminClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.BackupName`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(DeleteBackupRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(DeleteBackupRequest request)

Deletes a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       alloyDBAdminClient.deleteBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(String name)

Deletes a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString();
       alloyDBAdminClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Operation> deleteBackupCallable()

Deletes a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.deleteBackupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupOperationCallable()
    
    
    public final OperationCallable<DeleteBackupRequest,Empty,OperationMetadata> deleteBackupOperationCallable()

Deletes a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           alloyDBAdminClient.deleteBackupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(@Nullable ClusterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(@Nullable ClusterName name)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       alloyDBAdminClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(DeleteClusterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(DeleteClusterRequest request)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       alloyDBAdminClient.deleteClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(String name)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       alloyDBAdminClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteClusterCallable()
    
    
    public final UnaryCallable<DeleteClusterRequest,Operation> deleteClusterCallable()

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.deleteClusterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClusterOperationCallable()
    
    
    public final OperationCallable<DeleteClusterRequest,Empty,OperationMetadata> deleteClusterOperationCallable()

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           alloyDBAdminClient.deleteClusterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(@Nullable InstanceName name)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       alloyDBAdminClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(DeleteInstanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(DeleteInstanceRequest request)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       alloyDBAdminClient.deleteInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(String name)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       alloyDBAdminClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public final UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.deleteInstanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           alloyDBAdminClient.deleteInstanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### deleteUser(@Nullable UserName name)
    
    
    public final void deleteUser(@Nullable UserName name)

Deletes a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UserName name = UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
       alloyDBAdminClient.deleteUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.UserName`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
  
### deleteUser(DeleteUserRequest request)
    
    
    public final void deleteUser(DeleteUserRequest request)

Deletes a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteUserRequest request =
           DeleteUserRequest.newBuilder()
               .setName(UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       alloyDBAdminClient.deleteUser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteUserRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUser(String name)
    
    
    public final void deleteUser(String name)

Deletes a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString();
       alloyDBAdminClient.deleteUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
  
### deleteUserCallable()
    
    
    public final UnaryCallable<DeleteUserRequest,Empty> deleteUserCallable()

Deletes a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       DeleteUserRequest request =
           DeleteUserRequest.newBuilder()
               .setName(UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Empty> future = alloyDBAdminClient.deleteUserCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DeleteUserRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeSql(@Nullable InstanceName instance, String database, String user, String sqlStatement, String password)
    
    
    public final ExecuteSqlResponse executeSql(@Nullable InstanceName instance, String database, String user, String sqlStatement, String password)

Executes a SQL statement in a database inside an AlloyDB instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName instance = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       String database = "database1789464955";
       String user = "user3599307";
       String sqlStatement = "sqlStatement937767745";
       String password = "password1216985755";
       ExecuteSqlResponse response =
           alloyDBAdminClient.executeSql(instance, database, user, sqlStatement, password);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The database native user’s password.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlResponse)` |   
  
### executeSql(ExecuteSqlRequest request)
    
    
    public final ExecuteSqlResponse executeSql(ExecuteSqlRequest request)

Executes a SQL statement in a database inside an AlloyDB instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ExecuteSqlRequest request =
           ExecuteSqlRequest.newBuilder()
               .setInstance(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setDatabase("database1789464955")
               .setUser("user3599307")
               .setSqlStatement("sqlStatement937767745")
               .setValidateOnly(true)
               .build();
       ExecuteSqlResponse response = alloyDBAdminClient.executeSql(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlResponse)` |   
  
### executeSql(String instance, String database, String user, String sqlStatement, String password)
    
    
    public final ExecuteSqlResponse executeSql(String instance, String database, String user, String sqlStatement, String password)

Executes a SQL statement in a database inside an AlloyDB instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String instance =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       String database = "database1789464955";
       String user = "user3599307";
       String sqlStatement = "sqlStatement937767745";
       String password = "password1216985755";
       ExecuteSqlResponse response =
           alloyDBAdminClient.executeSql(instance, database, user, sqlStatement, password);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The database native user’s password.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlResponse)` |   
  
### executeSqlCallable()
    
    
    public final UnaryCallable<ExecuteSqlRequest,ExecuteSqlResponse> executeSqlCallable()

Executes a SQL statement in a database inside an AlloyDB instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ExecuteSqlRequest request =
           ExecuteSqlRequest.newBuilder()
               .setInstance(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setDatabase("database1789464955")
               .setUser("user3599307")
               .setSqlStatement("sqlStatement937767745")
               .setValidateOnly(true)
               .build();
       ApiFuture<ExecuteSqlResponse> future =
           alloyDBAdminClient.executeSqlCallable().futureCall(request);
       // Do something.
       ExecuteSqlResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlRequest),[ExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExecuteSqlResponse)>` |   
  
### exportClusterAsync(@Nullable ClusterName name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions)
    
    
    public final OperationFuture<ExportClusterResponse,OperationMetadata> exportClusterAsync(@Nullable ClusterName name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions)

Exports data from the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       GcsDestination gcsDestination = GcsDestination.newBuilder().build();
       String database = "database1789464955";
       ExportClusterRequest.CsvExportOptions csvExportOptions =
           ExportClusterRequest.CsvExportOptions.newBuilder().build();
       ExportClusterRequest.SqlExportOptions sqlExportOptions =
           ExportClusterRequest.SqlExportOptions.newBuilder().build();
       ExportClusterResponse response =
           alloyDBAdminClient
               .exportClusterAsync(
                   name, gcsDestination, database, csvExportOptions, sqlExportOptions)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the database where the export command will be executed. Note

  * Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.

  
`csvExportOptions` | `[ExportClusterRequest.CsvExportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest.SqlExportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### exportClusterAsync(ExportClusterRequest request)
    
    
    public final OperationFuture<ExportClusterResponse,OperationMetadata> exportClusterAsync(ExportClusterRequest request)

Exports data from the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ExportClusterRequest request =
           ExportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setDatabase("database1789464955")
               .build();
       ExportClusterResponse response = alloyDBAdminClient.exportClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### exportClusterAsync(String name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions)
    
    
    public final OperationFuture<ExportClusterResponse,OperationMetadata> exportClusterAsync(String name, GcsDestination gcsDestination, String database, ExportClusterRequest.CsvExportOptions csvExportOptions, ExportClusterRequest.SqlExportOptions sqlExportOptions)

Exports data from the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       GcsDestination gcsDestination = GcsDestination.newBuilder().build();
       String database = "database1789464955";
       ExportClusterRequest.CsvExportOptions csvExportOptions =
           ExportClusterRequest.CsvExportOptions.newBuilder().build();
       ExportClusterRequest.SqlExportOptions sqlExportOptions =
           ExportClusterRequest.SqlExportOptions.newBuilder().build();
       ExportClusterResponse response =
           alloyDBAdminClient
               .exportClusterAsync(
                   name, gcsDestination, database, csvExportOptions, sqlExportOptions)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the database where the export command will be executed. Note

  * Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.

  
`csvExportOptions` | `[ExportClusterRequest.CsvExportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest.SqlExportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### exportClusterCallable()
    
    
    public final UnaryCallable<ExportClusterRequest,Operation> exportClusterCallable()

Exports data from the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ExportClusterRequest request =
           ExportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setDatabase("database1789464955")
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.exportClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportClusterOperationCallable()
    
    
    public final OperationCallable<ExportClusterRequest,ExportClusterResponse,OperationMetadata> exportClusterOperationCallable()

Exports data from the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ExportClusterRequest request =
           ExportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setDatabase("database1789464955")
               .build();
       OperationFuture<ExportClusterResponse, OperationMetadata> future =
           alloyDBAdminClient.exportClusterOperationCallable().futureCall(request);
       // Do something.
       ExportClusterResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterRequest),[ExportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ExportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### failoverInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Instance,OperationMetadata> failoverInstanceAsync(@Nullable InstanceName name)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       Instance response = alloyDBAdminClient.failoverInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### failoverInstanceAsync(FailoverInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> failoverInstanceAsync(FailoverInstanceRequest request)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       FailoverInstanceRequest request =
           FailoverInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Instance response = alloyDBAdminClient.failoverInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.FailoverInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### failoverInstanceAsync(String name)
    
    
    public final OperationFuture<Instance,OperationMetadata> failoverInstanceAsync(String name)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       Instance response = alloyDBAdminClient.failoverInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### failoverInstanceCallable()
    
    
    public final UnaryCallable<FailoverInstanceRequest,Operation> failoverInstanceCallable()

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       FailoverInstanceRequest request =
           FailoverInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.failoverInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FailoverInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.FailoverInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### failoverInstanceOperationCallable()
    
    
    public final OperationCallable<FailoverInstanceRequest,Instance,OperationMetadata> failoverInstanceOperationCallable()

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       FailoverInstanceRequest request =
           FailoverInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.failoverInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[FailoverInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.FailoverInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### generateClientCertificate(@Nullable ClusterName parent)
    
    
    public final GenerateClientCertificateResponse generateClientCertificate(@Nullable ClusterName parent)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       GenerateClientCertificateResponse response =
           alloyDBAdminClient.generateClientCertificate(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the parent resource. The required format is: * projects/{project}/locations/{location}/clusters/{cluster}  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateResponse)` |   
  
### generateClientCertificate(GenerateClientCertificateRequest request)
    
    
    public final GenerateClientCertificateResponse generateClientCertificate(GenerateClientCertificateRequest request)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GenerateClientCertificateRequest request =
           GenerateClientCertificateRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setCertDuration(Duration.newBuilder().build())
               .setPublicKey("publicKey1446899510")
               .setUseMetadataExchange(true)
               .build();
       GenerateClientCertificateResponse response =
           alloyDBAdminClient.generateClientCertificate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateClientCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateResponse)` |   
  
### generateClientCertificate(String parent)
    
    
    public final GenerateClientCertificateResponse generateClientCertificate(String parent)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       GenerateClientCertificateResponse response =
           alloyDBAdminClient.generateClientCertificate(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. The required format is: * projects/{project}/locations/{location}/clusters/{cluster}  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateResponse)` |   
  
### generateClientCertificateCallable()
    
    
    public final UnaryCallable<GenerateClientCertificateRequest,GenerateClientCertificateResponse> generateClientCertificateCallable()

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GenerateClientCertificateRequest request =
           GenerateClientCertificateRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setCertDuration(Duration.newBuilder().build())
               .setPublicKey("publicKey1446899510")
               .setUseMetadataExchange(true)
               .build();
       ApiFuture<GenerateClientCertificateResponse> future =
           alloyDBAdminClient.generateClientCertificateCallable().futureCall(request);
       // Do something.
       GenerateClientCertificateResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateClientCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateRequest),[GenerateClientCertificateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GenerateClientCertificateResponse)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Gets details of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]");
       Backup response = alloyDBAdminClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.BackupName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Gets details of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       Backup response = alloyDBAdminClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Gets details of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString();
       Backup response = alloyDBAdminClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Gets details of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       ApiFuture<Backup> future = alloyDBAdminClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)>` |   
  
### getCluster(@Nullable ClusterName name)
    
    
    public final Cluster getCluster(@Nullable ClusterName name)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = alloyDBAdminClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)` |   
  
### getCluster(GetClusterRequest request)
    
    
    public final Cluster getCluster(GetClusterRequest request)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setView(ClusterView.forNumber(0))
               .build();
       Cluster response = alloyDBAdminClient.getCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)` |   
  
### getCluster(String name)
    
    
    public final Cluster getCluster(String name)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Cluster response = alloyDBAdminClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)` |   
  
### getClusterCallable()
    
    
    public final UnaryCallable<GetClusterRequest,Cluster> getClusterCallable()

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setView(ClusterView.forNumber(0))
               .build();
       ApiFuture<Cluster> future = alloyDBAdminClient.getClusterCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)>` |   
  
### getConnectionInfo(@Nullable InstanceName parent)
    
    
    public final ConnectionInfo getConnectionInfo(@Nullable InstanceName parent)

Get instance metadata used for a connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       ConnectionInfo response = alloyDBAdminClient.getConnectionInfo(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ConnectionInfo)` |   
  
### getConnectionInfo(GetConnectionInfoRequest request)
    
    
    public final ConnectionInfo getConnectionInfo(GetConnectionInfoRequest request)

Get instance metadata used for a connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetConnectionInfoRequest request =
           GetConnectionInfoRequest.newBuilder()
               .setParent(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ConnectionInfo response = alloyDBAdminClient.getConnectionInfo(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetConnectionInfoRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ConnectionInfo)` |   
  
### getConnectionInfo(String parent)
    
    
    public final ConnectionInfo getConnectionInfo(String parent)

Get instance metadata used for a connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       ConnectionInfo response = alloyDBAdminClient.getConnectionInfo(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ConnectionInfo)` |   
  
### getConnectionInfoCallable()
    
    
    public final UnaryCallable<GetConnectionInfoRequest,ConnectionInfo> getConnectionInfoCallable()

Get instance metadata used for a connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetConnectionInfoRequest request =
           GetConnectionInfoRequest.newBuilder()
               .setParent(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<ConnectionInfo> future =
           alloyDBAdminClient.getConnectionInfoCallable().futureCall(request);
       // Do something.
       ConnectionInfo response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectionInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetConnectionInfoRequest),[ConnectionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ConnectionInfo)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInstance(@Nullable InstanceName name)
    
    
    public final Instance getInstance(@Nullable InstanceName name)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       Instance response = alloyDBAdminClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public final Instance getInstance(GetInstanceRequest request)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setView(InstanceView.forNumber(0))
               .build();
       Instance response = alloyDBAdminClient.getInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)` |   
  
### getInstance(String name)
    
    
    public final Instance getInstance(String name)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       Instance response = alloyDBAdminClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)` |   
  
### getInstanceCallable()
    
    
    public final UnaryCallable<GetInstanceRequest,Instance> getInstanceCallable()

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setView(InstanceView.forNumber(0))
               .build();
       ApiFuture<Instance> future = alloyDBAdminClient.getInstanceCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = alloyDBAdminClient.getLocation(request);
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
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = alloyDBAdminClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AlloyDBAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.AlloyDBAdminSettings` |   
  
### getStub()
    
    
    public AlloyDBAdminStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.stub.AlloyDBAdminStub)` |   
  
### getUser(@Nullable UserName name)
    
    
    public final User getUser(@Nullable UserName name)

Gets details of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UserName name = UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
       User response = alloyDBAdminClient.getUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.UserName`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### getUser(GetUserRequest request)
    
    
    public final User getUser(GetUserRequest request)

Gets details of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetUserRequest request =
           GetUserRequest.newBuilder()
               .setName(UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString())
               .build();
       User response = alloyDBAdminClient.getUser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### getUser(String name)
    
    
    public final User getUser(String name)

Gets details of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString();
       User response = alloyDBAdminClient.getUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### getUserCallable()
    
    
    public final UnaryCallable<GetUserRequest,User> getUserCallable()

Gets details of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       GetUserRequest request =
           GetUserRequest.newBuilder()
               .setName(UserName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]").toString())
               .build();
       ApiFuture<User> future = alloyDBAdminClient.getUserCallable().futureCall(request);
       // Do something.
       User response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.GetUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)>` |   
  
### importClusterAsync(@Nullable ClusterName name, String gcsUri, String database, String user)
    
    
    public final OperationFuture<ImportClusterResponse,OperationMetadata> importClusterAsync(@Nullable ClusterName name, String gcsUri, String database, String user)

Imports data to the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       String gcsUri = "gcsUri-1251224875";
       String database = "database1789464955";
       String user = "user3599307";
       ImportClusterResponse response =
           alloyDBAdminClient.importClusterAsync(name, gcsUri, database, user).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The resource name of the cluster.  
`gcsUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### importClusterAsync(ImportClusterRequest request)
    
    
    public final OperationFuture<ImportClusterResponse,OperationMetadata> importClusterAsync(ImportClusterRequest request)

Imports data to the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ImportClusterRequest request =
           ImportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setDatabase("database1789464955")
               .setUser("user3599307")
               .build();
       ImportClusterResponse response = alloyDBAdminClient.importClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### importClusterAsync(String name, String gcsUri, String database, String user)
    
    
    public final OperationFuture<ImportClusterResponse,OperationMetadata> importClusterAsync(String name, String gcsUri, String database, String user)

Imports data to the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       String gcsUri = "gcsUri-1251224875";
       String database = "database1789464955";
       String user = "user3599307";
       ImportClusterResponse response =
           alloyDBAdminClient.importClusterAsync(name, gcsUri, database, user).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the cluster.  
`gcsUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### importClusterCallable()
    
    
    public final UnaryCallable<ImportClusterRequest,Operation> importClusterCallable()

Imports data to the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ImportClusterRequest request =
           ImportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setDatabase("database1789464955")
               .setUser("user3599307")
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.importClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importClusterOperationCallable()
    
    
    public final OperationCallable<ImportClusterRequest,ImportClusterResponse,OperationMetadata> importClusterOperationCallable()

Imports data to the cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ImportClusterRequest request =
           ImportClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setDatabase("database1789464955")
               .setUser("user3599307")
               .build();
       OperationFuture<ImportClusterResponse, OperationMetadata> future =
           alloyDBAdminClient.importClusterOperationCallable().futureCall(request);
       // Do something.
       ImportClusterResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterRequest),[ImportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ImportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### injectFaultAsync(InjectFaultRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> injectFaultAsync(InjectFaultRequest request)

Injects fault in an instance. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InjectFaultRequest request =
           InjectFaultRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Instance response = alloyDBAdminClient.injectFaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InjectFaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InjectFaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### injectFaultAsync(InjectFaultRequest.FaultType faultType, @Nullable InstanceName name)
    
    
    public final OperationFuture<Instance,OperationMetadata> injectFaultAsync(InjectFaultRequest.FaultType faultType, @Nullable InstanceName name)

Injects fault in an instance. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InjectFaultRequest.FaultType faultType = InjectFaultRequest.FaultType.forNumber(0);
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       Instance response = alloyDBAdminClient.injectFaultAsync(faultType, name).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest.FaultType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InjectFaultRequest.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### injectFaultAsync(InjectFaultRequest.FaultType faultType, String name)
    
    
    public final OperationFuture<Instance,OperationMetadata> injectFaultAsync(InjectFaultRequest.FaultType faultType, String name)

Injects fault in an instance. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InjectFaultRequest.FaultType faultType = InjectFaultRequest.FaultType.forNumber(0);
       String name =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       Instance response = alloyDBAdminClient.injectFaultAsync(faultType, name).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest.FaultType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InjectFaultRequest.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### injectFaultCallable()
    
    
    public final UnaryCallable<InjectFaultRequest,Operation> injectFaultCallable()

Injects fault in an instance. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InjectFaultRequest request =
           InjectFaultRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.injectFaultCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InjectFaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InjectFaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### injectFaultOperationCallable()
    
    
    public final OperationCallable<InjectFaultRequest,Instance,OperationMetadata> injectFaultOperationCallable()

Injects fault in an instance. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InjectFaultRequest request =
           InjectFaultRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.injectFaultOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InjectFaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InjectFaultRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
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
  
### listBackups(@Nullable LocationName parent)
    
    
    public final AlloyDBAdminClient.ListBackupsPagedResponse listBackups(@Nullable LocationName parent)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Backup element : alloyDBAdminClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. Parent value for ListBackupsRequest  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListBackupsPagedResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final AlloyDBAdminClient.ListBackupsPagedResponse listBackups(ListBackupsRequest request)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Backup element : alloyDBAdminClient.listBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListBackupsPagedResponse)` |   
  
### listBackups(String parent)
    
    
    public final AlloyDBAdminClient.ListBackupsPagedResponse listBackups(String parent)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Backup element : alloyDBAdminClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListBackupsRequest  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListBackupsPagedResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListBackupsResponse response = alloyDBAdminClient.listBackupsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListBackupsResponse)>` |   
  
### listBackupsPagedCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,AlloyDBAdminClient.ListBackupsPagedResponse> listBackupsPagedCallable()

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Backup> future = alloyDBAdminClient.listBackupsPagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListBackupsRequest),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListBackupsPagedResponse)>` |   
  
### listClusters(@Nullable LocationName parent)
    
    
    public final AlloyDBAdminClient.ListClustersPagedResponse listClusters(@Nullable LocationName parent)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Cluster element : alloyDBAdminClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format: * projects/{project}/locations/-  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListClustersPagedResponse)` |   
  
### listClusters(ListClustersRequest request)
    
    
    public final AlloyDBAdminClient.ListClustersPagedResponse listClusters(ListClustersRequest request)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Cluster element : alloyDBAdminClient.listClusters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListClustersPagedResponse)` |   
  
### listClusters(String parent)
    
    
    public final AlloyDBAdminClient.ListClustersPagedResponse listClusters(String parent)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Cluster element : alloyDBAdminClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format: * projects/{project}/locations/-  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListClustersPagedResponse)` |   
  
### listClustersCallable()
    
    
    public final UnaryCallable<ListClustersRequest,ListClustersResponse> listClustersCallable()

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListClustersResponse response = alloyDBAdminClient.listClustersCallable().call(request);
         for (Cluster element : response.getClustersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListClustersResponse)>` |   
  
### listClustersPagedCallable()
    
    
    public final UnaryCallable<ListClustersRequest,AlloyDBAdminClient.ListClustersPagedResponse> listClustersPagedCallable()

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Cluster> future =
           alloyDBAdminClient.listClustersPagedCallable().futureCall(request);
       // Do something.
       for (Cluster element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListClustersRequest),[ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListClustersPagedResponse)>` |   
  
### listDatabases(@Nullable ClusterName parent)
    
    
    public final AlloyDBAdminClient.ListDatabasesPagedResponse listDatabases(@Nullable ClusterName parent)

Lists Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (Database element : alloyDBAdminClient.listDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. Parent value for ListDatabasesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListDatabasesPagedResponse)` |   
  
### listDatabases(ListDatabasesRequest request)
    
    
    public final AlloyDBAdminClient.ListDatabasesPagedResponse listDatabases(ListDatabasesRequest request)

Lists Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Database element : alloyDBAdminClient.listDatabases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListDatabasesPagedResponse)` |   
  
### listDatabases(String parent)
    
    
    public final AlloyDBAdminClient.ListDatabasesPagedResponse listDatabases(String parent)

Lists Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (Database element : alloyDBAdminClient.listDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListDatabasesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListDatabasesPagedResponse)` |   
  
### listDatabasesCallable()
    
    
    public final UnaryCallable<ListDatabasesRequest,ListDatabasesResponse> listDatabasesCallable()

Lists Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDatabasesResponse response = alloyDBAdminClient.listDatabasesCallable().call(request);
         for (Database element : response.getDatabasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListDatabasesRequest),[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListDatabasesResponse)>` |   
  
### listDatabasesPagedCallable()
    
    
    public final UnaryCallable<ListDatabasesRequest,AlloyDBAdminClient.ListDatabasesPagedResponse> listDatabasesPagedCallable()

Lists Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Database> future =
           alloyDBAdminClient.listDatabasesPagedCallable().futureCall(request);
       // Do something.
       for (Database element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListDatabasesRequest),[ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListDatabasesPagedResponse)>` |   
  
### listInstances(@Nullable ClusterName parent)
    
    
    public final AlloyDBAdminClient.ListInstancesPagedResponse listInstances(@Nullable ClusterName parent)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (Instance element : alloyDBAdminClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats: * projects/{project}/locations/-/clusters/- * projects/{project}/locations/{region}/clusters/-  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListInstancesPagedResponse)` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public final AlloyDBAdminClient.ListInstancesPagedResponse listInstances(ListInstancesRequest request)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Instance element : alloyDBAdminClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListInstancesPagedResponse)` |   
  
### listInstances(String parent)
    
    
    public final AlloyDBAdminClient.ListInstancesPagedResponse listInstances(String parent)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (Instance element : alloyDBAdminClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats: * projects/{project}/locations/-/clusters/- * projects/{project}/locations/{region}/clusters/-  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInstancesResponse response = alloyDBAdminClient.listInstancesCallable().call(request);
         for (Instance element : response.getInstancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,AlloyDBAdminClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Instance> future =
           alloyDBAdminClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (Instance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListInstancesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AlloyDBAdminClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : alloyDBAdminClient.listLocations(request).iterateAll()) {
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
`[AlloyDBAdminClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = alloyDBAdminClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AlloyDBAdminClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           alloyDBAdminClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListLocationsPagedResponse)>` |   
  
### listSupportedDatabaseFlags(@Nullable LocationName parent)
    
    
    public final AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse listSupportedDatabaseFlags(@Nullable LocationName parent)

Lists SupportedDatabaseFlags for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SupportedDatabaseFlag element :
           alloyDBAdminClient.listSupportedDatabaseFlags(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.LocationName`  
Required. The name of the parent resource. The required format is: * projects/{project}/locations/{location} Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse)` |   
  
### listSupportedDatabaseFlags(ListSupportedDatabaseFlagsRequest request)
    
    
    public final AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse listSupportedDatabaseFlags(ListSupportedDatabaseFlagsRequest request)

Lists SupportedDatabaseFlags for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListSupportedDatabaseFlagsRequest request =
           ListSupportedDatabaseFlagsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SupportedDatabaseFlag element :
           alloyDBAdminClient.listSupportedDatabaseFlags(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListSupportedDatabaseFlagsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse)` |   
  
### listSupportedDatabaseFlags(String parent)
    
    
    public final AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse listSupportedDatabaseFlags(String parent)

Lists SupportedDatabaseFlags for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SupportedDatabaseFlag element :
           alloyDBAdminClient.listSupportedDatabaseFlags(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource. The required format is: * projects/{project}/locations/{location} Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse)` |   
  
### listSupportedDatabaseFlagsCallable()
    
    
    public final UnaryCallable<ListSupportedDatabaseFlagsRequest,ListSupportedDatabaseFlagsResponse> listSupportedDatabaseFlagsCallable()

Lists SupportedDatabaseFlags for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListSupportedDatabaseFlagsRequest request =
           ListSupportedDatabaseFlagsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSupportedDatabaseFlagsResponse response =
             alloyDBAdminClient.listSupportedDatabaseFlagsCallable().call(request);
         for (SupportedDatabaseFlag element : response.getSupportedDatabaseFlagsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListSupportedDatabaseFlagsRequest),[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListSupportedDatabaseFlagsResponse)>` |   
  
### listSupportedDatabaseFlagsPagedCallable()
    
    
    public final UnaryCallable<ListSupportedDatabaseFlagsRequest,AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse> listSupportedDatabaseFlagsPagedCallable()

Lists SupportedDatabaseFlags for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListSupportedDatabaseFlagsRequest request =
           ListSupportedDatabaseFlagsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SupportedDatabaseFlag> future =
           alloyDBAdminClient.listSupportedDatabaseFlagsPagedCallable().futureCall(request);
       // Do something.
       for (SupportedDatabaseFlag element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListSupportedDatabaseFlagsRequest),[ListSupportedDatabaseFlagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse)>` |   
  
### listUsers(@Nullable ClusterName parent)
    
    
    public final AlloyDBAdminClient.ListUsersPagedResponse listUsers(@Nullable ClusterName parent)

Lists Users in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (User element : alloyDBAdminClient.listUsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. Parent value for ListUsersRequest  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListUsersPagedResponse)` |   
  
### listUsers(ListUsersRequest request)
    
    
    public final AlloyDBAdminClient.ListUsersPagedResponse listUsers(ListUsersRequest request)

Lists Users in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListUsersRequest request =
           ListUsersRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (User element : alloyDBAdminClient.listUsers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListUsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListUsersPagedResponse)` |   
  
### listUsers(String parent)
    
    
    public final AlloyDBAdminClient.ListUsersPagedResponse listUsers(String parent)

Lists Users in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (User element : alloyDBAdminClient.listUsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListUsersRequest  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient.ListUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListUsersPagedResponse)` |   
  
### listUsersCallable()
    
    
    public final UnaryCallable<ListUsersRequest,ListUsersResponse> listUsersCallable()

Lists Users in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListUsersRequest request =
           ListUsersRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListUsersResponse response = alloyDBAdminClient.listUsersCallable().call(request);
         for (User element : response.getUsersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListUsersRequest),[ListUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListUsersResponse)>` |   
  
### listUsersPagedCallable()
    
    
    public final UnaryCallable<ListUsersRequest,AlloyDBAdminClient.ListUsersPagedResponse> listUsersPagedCallable()

Lists Users in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ListUsersRequest request =
           ListUsersRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<User> future = alloyDBAdminClient.listUsersPagedCallable().futureCall(request);
       // Do something.
       for (User element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ListUsersRequest),[ListUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.ListUsersPagedResponse)>` |   
  
### promoteClusterAsync(@Nullable ClusterName name)
    
    
    public final OperationFuture<Cluster,OperationMetadata> promoteClusterAsync(@Nullable ClusterName name)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = alloyDBAdminClient.promoteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### promoteClusterAsync(PromoteClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> promoteClusterAsync(PromoteClusterRequest request)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       PromoteClusterRequest request =
           PromoteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       Cluster response = alloyDBAdminClient.promoteClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PromoteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.PromoteClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### promoteClusterAsync(String name)
    
    
    public final OperationFuture<Cluster,OperationMetadata> promoteClusterAsync(String name)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Cluster response = alloyDBAdminClient.promoteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### promoteClusterCallable()
    
    
    public final UnaryCallable<PromoteClusterRequest,Operation> promoteClusterCallable()

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       PromoteClusterRequest request =
           PromoteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.promoteClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PromoteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.PromoteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### promoteClusterOperationCallable()
    
    
    public final OperationCallable<PromoteClusterRequest,Cluster,OperationMetadata> promoteClusterOperationCallable()

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       PromoteClusterRequest request =
           PromoteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.promoteClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PromoteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.PromoteClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restartInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Instance,OperationMetadata> restartInstanceAsync(@Nullable InstanceName name)

Restart an Instance in a cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
       Instance response = alloyDBAdminClient.restartInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.InstanceName`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restartInstanceAsync(RestartInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> restartInstanceAsync(RestartInstanceRequest request)

Restart an Instance in a cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .addAllNodeIds(new ArrayList<String>())
               .build();
       Instance response = alloyDBAdminClient.restartInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restartInstanceAsync(String name)
    
    
    public final OperationFuture<Instance,OperationMetadata> restartInstanceAsync(String name)

Restart an Instance in a cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name =
           InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString();
       Instance response = alloyDBAdminClient.restartInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restartInstanceCallable()
    
    
    public final UnaryCallable<RestartInstanceRequest,Operation> restartInstanceCallable()

Restart an Instance in a cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .addAllNodeIds(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.restartInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartInstanceOperationCallable()
    
    
    public final OperationCallable<RestartInstanceRequest,Instance,OperationMetadata> restartInstanceOperationCallable()

Restart an Instance in a cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(
                   InstanceName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .addAllNodeIds(new ArrayList<String>())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.restartInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestartInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restoreClusterAsync(RestoreClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> restoreClusterAsync(RestoreClusterRequest request)

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestoreClusterRequest request =
           RestoreClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = alloyDBAdminClient.restoreClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### restoreClusterCallable()
    
    
    public final UnaryCallable<RestoreClusterRequest,Operation> restoreClusterCallable()

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestoreClusterRequest request =
           RestoreClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.restoreClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreClusterOperationCallable()
    
    
    public final OperationCallable<RestoreClusterRequest,Cluster,OperationMetadata> restoreClusterOperationCallable()

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       RestoreClusterRequest request =
           RestoreClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.restoreClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### switchoverClusterAsync(@Nullable ClusterName name)
    
    
    public final OperationFuture<Cluster,OperationMetadata> switchoverClusterAsync(@Nullable ClusterName name)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = alloyDBAdminClient.switchoverClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### switchoverClusterAsync(SwitchoverClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> switchoverClusterAsync(SwitchoverClusterRequest request)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       SwitchoverClusterRequest request =
           SwitchoverClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = alloyDBAdminClient.switchoverClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SwitchoverClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SwitchoverClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### switchoverClusterAsync(String name)
    
    
    public final OperationFuture<Cluster,OperationMetadata> switchoverClusterAsync(String name)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Cluster response = alloyDBAdminClient.switchoverClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### switchoverClusterCallable()
    
    
    public final UnaryCallable<SwitchoverClusterRequest,Operation> switchoverClusterCallable()

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       SwitchoverClusterRequest request =
           SwitchoverClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           alloyDBAdminClient.switchoverClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SwitchoverClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SwitchoverClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### switchoverClusterOperationCallable()
    
    
    public final OperationCallable<SwitchoverClusterRequest,Cluster,OperationMetadata> switchoverClusterOperationCallable()

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       SwitchoverClusterRequest request =
           SwitchoverClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.switchoverClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SwitchoverClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SwitchoverClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateBackupAsync(Backup backup, FieldMask updateMask)
    
    
    public final OperationFuture<Backup,OperationMetadata> updateBackupAsync(Backup backup, FieldMask updateMask)

Updates the parameters of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       Backup backup = Backup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Backup response = alloyDBAdminClient.updateBackupAsync(backup, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateBackupAsync(UpdateBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> updateBackupAsync(UpdateBackupRequest request)

Updates the parameters of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       Backup response = alloyDBAdminClient.updateBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateBackupCallable()
    
    
    public final UnaryCallable<UpdateBackupRequest,Operation> updateBackupCallable()

Updates the parameters of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.updateBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupOperationCallable()
    
    
    public final OperationCallable<UpdateBackupRequest,Backup,OperationMetadata> updateBackupOperationCallable()

Updates the parameters of a single Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           alloyDBAdminClient.updateBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateClusterAsync(Cluster cluster, FieldMask updateMask)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(Cluster cluster, FieldMask updateMask)

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       Cluster cluster = Cluster.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Cluster response = alloyDBAdminClient.updateClusterAsync(cluster, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateClusterAsync(UpdateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(UpdateClusterRequest request)

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       Cluster response = alloyDBAdminClient.updateClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateClusterCallable()
    
    
    public final UnaryCallable<UpdateClusterRequest,Operation> updateClusterCallable()

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.updateClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClusterOperationCallable()
    
    
    public final OperationCallable<UpdateClusterRequest,Cluster,OperationMetadata> updateClusterOperationCallable()

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBAdminClient.updateClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateInstanceAsync(Instance instance, FieldMask updateMask)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(Instance instance, FieldMask updateMask)

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       Instance instance = Instance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Instance response = alloyDBAdminClient.updateInstanceAsync(instance, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateInstanceAsync(UpdateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(UpdateInstanceRequest request)

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       Instance response = alloyDBAdminClient.updateInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateInstanceCallable()
    
    
    public final UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.updateInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public final OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           alloyDBAdminClient.updateInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### updateUser(UpdateUserRequest request)
    
    
    public final User updateUser(UpdateUserRequest request)

Updates the parameters of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateUserRequest request =
           UpdateUserRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUser(User.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       User response = alloyDBAdminClient.updateUser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### updateUser(User user, FieldMask updateMask)
    
    
    public final User updateUser(User user, FieldMask updateMask)

Updates the parameters of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       User user = User.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       User response = alloyDBAdminClient.updateUser(user, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`user` | `[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)` |   
  
### updateUserCallable()
    
    
    public final UnaryCallable<UpdateUserRequest,User> updateUserCallable()

Updates the parameters of a single User.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpdateUserRequest request =
           UpdateUserRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUser(User.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .build();
       ApiFuture<User> future = alloyDBAdminClient.updateUserCallable().futureCall(request);
       // Do something.
       User response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpdateUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.User)>` |   
  
### upgradeClusterAsync(@Nullable ClusterName name, DatabaseVersion version)
    
    
    public final OperationFuture<UpgradeClusterResponse,OperationMetadata> upgradeClusterAsync(@Nullable ClusterName name, DatabaseVersion version)

Upgrades a single Cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       DatabaseVersion version = DatabaseVersion.forNumber(0);
       UpgradeClusterResponse response = alloyDBAdminClient.upgradeClusterAsync(name, version).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1.ClusterName`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### upgradeClusterAsync(UpgradeClusterRequest request)
    
    
    public final OperationFuture<UpgradeClusterResponse,OperationMetadata> upgradeClusterAsync(UpgradeClusterRequest request)

Upgrades a single Cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpgradeClusterRequest request =
           UpgradeClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setVersion(DatabaseVersion.forNumber(0))
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       UpgradeClusterResponse response = alloyDBAdminClient.upgradeClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### upgradeClusterAsync(String name, DatabaseVersion version)
    
    
    public final OperationFuture<UpgradeClusterResponse,OperationMetadata> upgradeClusterAsync(String name, DatabaseVersion version)

Upgrades a single Cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       DatabaseVersion version = DatabaseVersion.forNumber(0);
       UpgradeClusterResponse response = alloyDBAdminClient.upgradeClusterAsync(name, version).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
### upgradeClusterCallable()
    
    
    public final UnaryCallable<UpgradeClusterRequest,Operation> upgradeClusterCallable()

Upgrades a single Cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpgradeClusterRequest request =
           UpgradeClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setVersion(DatabaseVersion.forNumber(0))
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = alloyDBAdminClient.upgradeClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### upgradeClusterOperationCallable()
    
    
    public final OperationCallable<UpgradeClusterRequest,UpgradeClusterResponse,OperationMetadata> upgradeClusterOperationCallable()

Upgrades a single Cluster. Imperative only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.create()) {
       UpgradeClusterRequest request =
           UpgradeClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setVersion(DatabaseVersion.forNumber(0))
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<UpgradeClusterResponse, OperationMetadata> future =
           alloyDBAdminClient.upgradeClusterOperationCallable().futureCall(request);
       // Do something.
       UpgradeClusterResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterRequest),[UpgradeClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.UpgradeClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
