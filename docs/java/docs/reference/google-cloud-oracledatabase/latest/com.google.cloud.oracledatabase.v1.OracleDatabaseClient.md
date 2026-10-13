---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient
title: Class OracleDatabaseClient (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:37.232384+00:00
---

# Class OracleDatabaseClient (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OracleDatabaseClient (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-oracledatabase/google-cloud-oracledatabase/src/main/java/com/google/cloud/oracledatabase/v1/OracleDatabaseClient.java)| [Product Reference](https://cloud.google.com/oracle/database/docs)  
---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudExadataInfrastructureName name =
           CloudExadataInfrastructureName.of(
               "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]");
       CloudExadataInfrastructure response =
           oracleDatabaseClient.getCloudExadataInfrastructure(name);
     }
     

Note: close() needs to be called on the OracleDatabaseClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListCloudExadataInfrastructures |  Lists Exadata Infrastructures in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCloudExadataInfrastructures(LocationName parent) 
  * listCloudExadataInfrastructures(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCloudExadataInfrastructuresPagedCallable() 
  * listCloudExadataInfrastructuresCallable() 

  
GetCloudExadataInfrastructure |  Gets details of a single Exadata Infrastructure. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCloudExadataInfrastructure(CloudExadataInfrastructureName name) 
  * getCloudExadataInfrastructure(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCloudExadataInfrastructureCallable() 

  
CreateCloudExadataInfrastructure |  Creates a new Exadata Infrastructure in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCloudExadataInfrastructureAsync(LocationName parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId) 
  * createCloudExadataInfrastructureAsync(String parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCloudExadataInfrastructureOperationCallable() 
  * createCloudExadataInfrastructureCallable() 

  
DeleteCloudExadataInfrastructure |  Deletes a single Exadata Infrastructure. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCloudExadataInfrastructureAsync(CloudExadataInfrastructureName name) 
  * deleteCloudExadataInfrastructureAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCloudExadataInfrastructureOperationCallable() 
  * deleteCloudExadataInfrastructureCallable() 

  
ConfigureExascaleCloudExadataInfrastructure |  Configures Exascale for a single Exadata Infrastructure. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * configureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * configureExascaleCloudExadataInfrastructureAsync(CloudExadataInfrastructureName name, int totalStorageSizeGb) 
  * configureExascaleCloudExadataInfrastructureAsync(String name, int totalStorageSizeGb) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * configureExascaleCloudExadataInfrastructureOperationCallable() 
  * configureExascaleCloudExadataInfrastructureCallable() 

  
ListCloudVmClusters |  Lists the VM Clusters in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCloudVmClusters(ListCloudVmClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCloudVmClusters(LocationName parent) 
  * listCloudVmClusters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCloudVmClustersPagedCallable() 
  * listCloudVmClustersCallable() 

  
GetCloudVmCluster |  Gets details of a single VM Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCloudVmCluster(GetCloudVmClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCloudVmCluster(CloudVmClusterName name) 
  * getCloudVmCluster(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCloudVmClusterCallable() 

  
CreateCloudVmCluster |  Creates a new VM Cluster in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCloudVmClusterAsync(CreateCloudVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCloudVmClusterAsync(LocationName parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId) 
  * createCloudVmClusterAsync(String parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCloudVmClusterOperationCallable() 
  * createCloudVmClusterCallable() 

  
DeleteCloudVmCluster |  Deletes a single VM Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCloudVmClusterAsync(DeleteCloudVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCloudVmClusterAsync(CloudVmClusterName name) 
  * deleteCloudVmClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCloudVmClusterOperationCallable() 
  * deleteCloudVmClusterCallable() 

  
ListEntitlements |  Lists the entitlements in a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntitlements(ListEntitlementsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntitlements(LocationName parent) 
  * listEntitlements(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntitlementsPagedCallable() 
  * listEntitlementsCallable() 

  
ListDbServers |  Lists the database servers of an Exadata Infrastructure instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbServers(ListDbServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbServers(CloudExadataInfrastructureName parent) 
  * listDbServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbServersPagedCallable() 
  * listDbServersCallable() 

  
ListDbNodes |  Lists the database nodes of a VM Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbNodes(ListDbNodesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbNodes(CloudVmClusterName parent) 
  * listDbNodes(ExadbVmClusterName parent) 
  * listDbNodes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbNodesPagedCallable() 
  * listDbNodesCallable() 

  
ListGiVersions |  Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGiVersions(ListGiVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGiVersions(LocationName parent) 
  * listGiVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGiVersionsPagedCallable() 
  * listGiVersionsCallable() 

  
ListMinorVersions |  Lists all the valid minor versions for the given project, location, gi version and shape family. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMinorVersions(ListMinorVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMinorVersions(GiVersionName parent) 
  * listMinorVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMinorVersionsPagedCallable() 
  * listMinorVersionsCallable() 

  
ListDbSystemShapes |  Lists the database system shapes available for the project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbSystemShapes(ListDbSystemShapesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbSystemShapes(LocationName parent) 
  * listDbSystemShapes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbSystemShapesPagedCallable() 
  * listDbSystemShapesCallable() 

  
ListAutonomousDatabases |  Lists the Autonomous Databases in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAutonomousDatabases(ListAutonomousDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAutonomousDatabases(LocationName parent) 
  * listAutonomousDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAutonomousDatabasesPagedCallable() 
  * listAutonomousDatabasesCallable() 

  
GetAutonomousDatabase |  Gets the details of a single Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAutonomousDatabase(GetAutonomousDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAutonomousDatabase(AutonomousDatabaseName name) 
  * getAutonomousDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAutonomousDatabaseCallable() 

  
CreateAutonomousDatabase |  Creates a new Autonomous Database in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAutonomousDatabaseAsync(LocationName parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId) 
  * createAutonomousDatabaseAsync(String parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAutonomousDatabaseOperationCallable() 
  * createAutonomousDatabaseCallable() 

  
UpdateAutonomousDatabase |  Updates the parameters of a single Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAutonomousDatabaseAsync(AutonomousDatabase autonomousDatabase, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAutonomousDatabaseOperationCallable() 
  * updateAutonomousDatabaseCallable() 

  
DeleteAutonomousDatabase |  Deletes a single Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAutonomousDatabaseAsync(AutonomousDatabaseName name) 
  * deleteAutonomousDatabaseAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAutonomousDatabaseOperationCallable() 
  * deleteAutonomousDatabaseCallable() 

  
RestoreAutonomousDatabase |  Restores a single Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreAutonomousDatabaseAsync(AutonomousDatabaseName name, Timestamp restoreTime) 
  * restoreAutonomousDatabaseAsync(String name, Timestamp restoreTime) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreAutonomousDatabaseOperationCallable() 
  * restoreAutonomousDatabaseCallable() 

  
GenerateAutonomousDatabaseWallet |  Generates a wallet for an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateAutonomousDatabaseWallet(AutonomousDatabaseName name, GenerateType type, boolean isRegional, String password) 
  * generateAutonomousDatabaseWallet(String name, GenerateType type, boolean isRegional, String password) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateAutonomousDatabaseWalletCallable() 

  
ListAutonomousDbVersions |  Lists all the available Autonomous Database versions for a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAutonomousDbVersions(ListAutonomousDbVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAutonomousDbVersions(LocationName parent) 
  * listAutonomousDbVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAutonomousDbVersionsPagedCallable() 
  * listAutonomousDbVersionsCallable() 

  
ListAutonomousDatabaseCharacterSets |  Lists Autonomous Database Character Sets in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAutonomousDatabaseCharacterSets(LocationName parent) 
  * listAutonomousDatabaseCharacterSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAutonomousDatabaseCharacterSetsPagedCallable() 
  * listAutonomousDatabaseCharacterSetsCallable() 

  
ListAutonomousDatabaseBackups |  Lists the long-term and automatic backups of an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAutonomousDatabaseBackups(LocationName parent) 
  * listAutonomousDatabaseBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAutonomousDatabaseBackupsPagedCallable() 
  * listAutonomousDatabaseBackupsCallable() 

  
StopAutonomousDatabase |  Stops an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopAutonomousDatabaseAsync(AutonomousDatabaseName name) 
  * stopAutonomousDatabaseAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopAutonomousDatabaseOperationCallable() 
  * stopAutonomousDatabaseCallable() 

  
StartAutonomousDatabase |  Starts an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startAutonomousDatabaseAsync(StartAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startAutonomousDatabaseAsync(AutonomousDatabaseName name) 
  * startAutonomousDatabaseAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startAutonomousDatabaseOperationCallable() 
  * startAutonomousDatabaseCallable() 

  
RestartAutonomousDatabase |  Restarts an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restartAutonomousDatabaseAsync(AutonomousDatabaseName name) 
  * restartAutonomousDatabaseAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restartAutonomousDatabaseOperationCallable() 
  * restartAutonomousDatabaseCallable() 

  
SwitchoverAutonomousDatabase |  Initiates a switchover of specified autonomous database to the associated peer database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * switchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * switchoverAutonomousDatabaseAsync(AutonomousDatabaseName name, AutonomousDatabaseName peerAutonomousDatabase) 
  * switchoverAutonomousDatabaseAsync(AutonomousDatabaseName name, String peerAutonomousDatabase) 
  * switchoverAutonomousDatabaseAsync(String name, AutonomousDatabaseName peerAutonomousDatabase) 
  * switchoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * switchoverAutonomousDatabaseOperationCallable() 
  * switchoverAutonomousDatabaseCallable() 

  
FailoverAutonomousDatabase |  Initiates a failover to target autonomous database from the associated primary database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * failoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * failoverAutonomousDatabaseAsync(AutonomousDatabaseName name, AutonomousDatabaseName peerAutonomousDatabase) 
  * failoverAutonomousDatabaseAsync(AutonomousDatabaseName name, String peerAutonomousDatabase) 
  * failoverAutonomousDatabaseAsync(String name, AutonomousDatabaseName peerAutonomousDatabase) 
  * failoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * failoverAutonomousDatabaseOperationCallable() 
  * failoverAutonomousDatabaseCallable() 

  
RefreshAutonomousDatabase |  Refreshes the refreshable clone of an Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * refreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * refreshAutonomousDatabaseAsync(AutonomousDatabaseName name, Timestamp refreshCutoffTime) 
  * refreshAutonomousDatabaseAsync(String name, Timestamp refreshCutoffTime) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * refreshAutonomousDatabaseOperationCallable() 
  * refreshAutonomousDatabaseCallable() 

  
GetAutonomousDatabaseRefreshableClones |  Gets the refreshable clones for a given Autonomous Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAutonomousDatabaseRefreshableClones(AutonomousDatabaseName name) 
  * getAutonomousDatabaseRefreshableClones(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAutonomousDatabaseRefreshableClonesCallable() 

  
ListOdbNetworks |  Lists the ODB Networks in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOdbNetworks(ListOdbNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOdbNetworks(LocationName parent) 
  * listOdbNetworks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOdbNetworksPagedCallable() 
  * listOdbNetworksCallable() 

  
GetOdbNetwork |  Gets details of a single ODB Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOdbNetwork(GetOdbNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOdbNetwork(OdbNetworkName name) 
  * getOdbNetwork(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOdbNetworkCallable() 

  
CreateOdbNetwork |  Creates a new ODB Network in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createOdbNetworkAsync(CreateOdbNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createOdbNetworkAsync(LocationName parent, OdbNetwork odbNetwork, String odbNetworkId) 
  * createOdbNetworkAsync(String parent, OdbNetwork odbNetwork, String odbNetworkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createOdbNetworkOperationCallable() 
  * createOdbNetworkCallable() 

  
DeleteOdbNetwork |  Deletes a single ODB Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteOdbNetworkAsync(DeleteOdbNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteOdbNetworkAsync(OdbNetworkName name) 
  * deleteOdbNetworkAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOdbNetworkOperationCallable() 
  * deleteOdbNetworkCallable() 

  
ListOdbSubnets |  Lists all the ODB Subnets in a given ODB Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOdbSubnets(ListOdbSubnetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOdbSubnets(OdbNetworkName parent) 
  * listOdbSubnets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOdbSubnetsPagedCallable() 
  * listOdbSubnetsCallable() 

  
GetOdbSubnet |  Gets details of a single ODB Subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOdbSubnet(GetOdbSubnetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOdbSubnet(OdbSubnetName name) 
  * getOdbSubnet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOdbSubnetCallable() 

  
CreateOdbSubnet |  Creates a new ODB Subnet in a given ODB Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createOdbSubnetAsync(CreateOdbSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createOdbSubnetAsync(OdbNetworkName parent, OdbSubnet odbSubnet, String odbSubnetId) 
  * createOdbSubnetAsync(String parent, OdbSubnet odbSubnet, String odbSubnetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createOdbSubnetOperationCallable() 
  * createOdbSubnetCallable() 

  
DeleteOdbSubnet |  Deletes a single ODB Subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteOdbSubnetAsync(DeleteOdbSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteOdbSubnetAsync(OdbSubnetName name) 
  * deleteOdbSubnetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOdbSubnetOperationCallable() 
  * deleteOdbSubnetCallable() 

  
ListExadbVmClusters |  Lists all the Exadb (Exascale) VM Clusters for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExadbVmClusters(ListExadbVmClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExadbVmClusters(LocationName parent) 
  * listExadbVmClusters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExadbVmClustersPagedCallable() 
  * listExadbVmClustersCallable() 

  
GetExadbVmCluster |  Gets details of a single Exadb (Exascale) VM Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExadbVmCluster(GetExadbVmClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExadbVmCluster(ExadbVmClusterName name) 
  * getExadbVmCluster(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExadbVmClusterCallable() 

  
CreateExadbVmCluster |  Creates a new Exadb (Exascale) VM Cluster resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExadbVmClusterAsync(CreateExadbVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createExadbVmClusterAsync(LocationName parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId) 
  * createExadbVmClusterAsync(String parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExadbVmClusterOperationCallable() 
  * createExadbVmClusterCallable() 

  
DeleteExadbVmCluster |  Deletes a single Exadb (Exascale) VM Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExadbVmClusterAsync(DeleteExadbVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExadbVmClusterAsync(ExadbVmClusterName name) 
  * deleteExadbVmClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExadbVmClusterOperationCallable() 
  * deleteExadbVmClusterCallable() 

  
UpdateExadbVmCluster |  Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExadbVmClusterAsync(UpdateExadbVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateExadbVmClusterAsync(ExadbVmCluster exadbVmCluster, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExadbVmClusterOperationCallable() 
  * updateExadbVmClusterCallable() 

  
RemoveVirtualMachineExadbVmCluster |  Removes virtual machines from an existing exadb vm cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeVirtualMachineExadbVmClusterAsync(ExadbVmClusterName name, List<String> hostnames) 
  * removeVirtualMachineExadbVmClusterAsync(String name, List<String> hostnames) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeVirtualMachineExadbVmClusterOperationCallable() 
  * removeVirtualMachineExadbVmClusterCallable() 

  
ListExascaleDbStorageVaults |  Lists all the ExascaleDB Storage Vaults for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExascaleDbStorageVaults(LocationName parent) 
  * listExascaleDbStorageVaults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExascaleDbStorageVaultsPagedCallable() 
  * listExascaleDbStorageVaultsCallable() 

  
GetExascaleDbStorageVault |  Gets details of a single ExascaleDB Storage Vault. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExascaleDbStorageVault(GetExascaleDbStorageVaultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExascaleDbStorageVault(ExascaleDbStorageVaultName name) 
  * getExascaleDbStorageVault(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExascaleDbStorageVaultCallable() 

  
CreateExascaleDbStorageVault |  Creates a new ExascaleDB Storage Vault resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createExascaleDbStorageVaultAsync(LocationName parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId) 
  * createExascaleDbStorageVaultAsync(String parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExascaleDbStorageVaultOperationCallable() 
  * createExascaleDbStorageVaultCallable() 

  
DeleteExascaleDbStorageVault |  Deletes a single ExascaleDB Storage Vault. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExascaleDbStorageVaultAsync(ExascaleDbStorageVaultName name) 
  * deleteExascaleDbStorageVaultAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExascaleDbStorageVaultOperationCallable() 
  * deleteExascaleDbStorageVaultCallable() 

  
ListDbSystemInitialStorageSizes |  Lists all the DbSystemInitialStorageSizes for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbSystemInitialStorageSizes(LocationName parent) 
  * listDbSystemInitialStorageSizes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbSystemInitialStorageSizesPagedCallable() 
  * listDbSystemInitialStorageSizesCallable() 

  
ListDatabases |  Lists all the Databases for the given project, location and DbSystem. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatabases(ListDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatabases(LocationName parent) 
  * listDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatabasesPagedCallable() 
  * listDatabasesCallable() 

  
GetDatabase |  Gets details of a single Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDatabase(GetDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDatabase(DatabaseName name) 
  * getDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDatabaseCallable() 

  
ListPluggableDatabases |  Lists all the PluggableDatabases for the given project, location and Container Database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPluggableDatabases(ListPluggableDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPluggableDatabases(LocationName parent) 
  * listPluggableDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPluggableDatabasesPagedCallable() 
  * listPluggableDatabasesCallable() 

  
GetPluggableDatabase |  Gets details of a single PluggableDatabase. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPluggableDatabase(GetPluggableDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPluggableDatabase(PluggableDatabaseName name) 
  * getPluggableDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPluggableDatabaseCallable() 

  
ListDbSystems |  Lists all the DbSystems for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbSystems(ListDbSystemsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbSystems(LocationName parent) 
  * listDbSystems(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbSystemsPagedCallable() 
  * listDbSystemsCallable() 

  
GetDbSystem |  Gets details of a single DbSystem. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDbSystem(GetDbSystemRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDbSystem(DbSystemName name) 
  * getDbSystem(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDbSystemCallable() 

  
CreateDbSystem |  Creates a new DbSystem in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDbSystemAsync(CreateDbSystemRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDbSystemAsync(LocationName parent, DbSystem dbSystem, String dbSystemId) 
  * createDbSystemAsync(String parent, DbSystem dbSystem, String dbSystemId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDbSystemOperationCallable() 
  * createDbSystemCallable() 

  
DeleteDbSystem |  Deletes a single DbSystem. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDbSystemAsync(DeleteDbSystemRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDbSystemAsync(DbSystemName name) 
  * deleteDbSystemAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDbSystemOperationCallable() 
  * deleteDbSystemCallable() 

  
ListGoldengateDeployments |  Lists all the GoldengateDeployments for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateDeployments(ListGoldengateDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateDeployments(LocationName parent) 
  * listGoldengateDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateDeploymentsPagedCallable() 
  * listGoldengateDeploymentsCallable() 

  
GetGoldengateDeployment |  Gets details of a single GoldengateDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGoldengateDeployment(GetGoldengateDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGoldengateDeployment(GoldengateDeploymentName name) 
  * getGoldengateDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGoldengateDeploymentCallable() 

  
CreateGoldengateDeployment |  Creates a new GoldengateDeployment in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGoldengateDeploymentAsync(LocationName parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId) 
  * createGoldengateDeploymentAsync(String parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGoldengateDeploymentOperationCallable() 
  * createGoldengateDeploymentCallable() 

  
DeleteGoldengateDeployment |  Deletes a single GoldengateDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGoldengateDeploymentAsync(GoldengateDeploymentName name) 
  * deleteGoldengateDeploymentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGoldengateDeploymentOperationCallable() 
  * deleteGoldengateDeploymentCallable() 

  
StopGoldengateDeployment |  Stops a single GoldengateDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopGoldengateDeploymentAsync(GoldengateDeploymentName name) 
  * stopGoldengateDeploymentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopGoldengateDeploymentOperationCallable() 
  * stopGoldengateDeploymentCallable() 

  
StartGoldengateDeployment |  Starts a single GoldengateDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startGoldengateDeploymentAsync(StartGoldengateDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startGoldengateDeploymentAsync(GoldengateDeploymentName name) 
  * startGoldengateDeploymentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startGoldengateDeploymentOperationCallable() 
  * startGoldengateDeploymentCallable() 

  
ListGoldengateConnections |  Lists all the GoldengateConnections for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateConnections(ListGoldengateConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateConnections(LocationName parent) 
  * listGoldengateConnections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateConnectionsPagedCallable() 
  * listGoldengateConnectionsCallable() 

  
GetGoldengateConnection |  Gets details of a single GoldengateConnection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGoldengateConnection(GetGoldengateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGoldengateConnection(GoldengateConnectionName name) 
  * getGoldengateConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGoldengateConnectionCallable() 

  
CreateGoldengateConnection |  Creates a new GoldengateConnection in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGoldengateConnectionAsync(CreateGoldengateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGoldengateConnectionAsync(LocationName parent, GoldengateConnection goldengateConnection, String goldengateConnectionId) 
  * createGoldengateConnectionAsync(String parent, GoldengateConnection goldengateConnection, String goldengateConnectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGoldengateConnectionOperationCallable() 
  * createGoldengateConnectionCallable() 

  
DeleteGoldengateConnection |  Deletes a single GoldengateConnection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGoldengateConnectionAsync(GoldengateConnectionName name) 
  * deleteGoldengateConnectionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGoldengateConnectionOperationCallable() 
  * deleteGoldengateConnectionCallable() 

  
ListGoldengateDeploymentVersions |  Lists GoldengateDeploymentVersions in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateDeploymentVersions(LocationName parent) 
  * listGoldengateDeploymentVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateDeploymentVersionsPagedCallable() 
  * listGoldengateDeploymentVersionsCallable() 

  
ListGoldengateDeploymentTypes |  Lists GoldenGateDeploymentTypes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateDeploymentTypes(LocationName parent) 
  * listGoldengateDeploymentTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateDeploymentTypesPagedCallable() 
  * listGoldengateDeploymentTypesCallable() 

  
ListGoldengateDeploymentEnvironments |  Lists GoldengateDeploymentEnvironments in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateDeploymentEnvironments(LocationName parent) 
  * listGoldengateDeploymentEnvironments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateDeploymentEnvironmentsPagedCallable() 
  * listGoldengateDeploymentEnvironmentsCallable() 

  
ListGoldengateConnectionTypes |  Lists GoldengateConnectionTypes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateConnectionTypes(LocationName parent) 
  * listGoldengateConnectionTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateConnectionTypesPagedCallable() 
  * listGoldengateConnectionTypesCallable() 

  
ListDbVersions |  List DbVersions for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDbVersions(ListDbVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDbVersions(LocationName parent) 
  * listDbVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDbVersionsPagedCallable() 
  * listDbVersionsCallable() 

  
ListDatabaseCharacterSets |  List DatabaseCharacterSets for the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatabaseCharacterSets(ListDatabaseCharacterSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatabaseCharacterSets(LocationName parent) 
  * listDatabaseCharacterSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatabaseCharacterSetsPagedCallable() 
  * listDatabaseCharacterSetsCallable() 

  
ListGoldengateConnectionAssignments |  Lists GoldengateConnectionAssignments in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGoldengateConnectionAssignments(LocationName parent) 
  * listGoldengateConnectionAssignments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGoldengateConnectionAssignmentsPagedCallable() 
  * listGoldengateConnectionAssignmentsCallable() 

  
GetGoldengateConnectionAssignment |  Gets details of a single GoldengateConnectionAssignment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGoldengateConnectionAssignment(GoldengateConnectionAssignmentName name) 
  * getGoldengateConnectionAssignment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGoldengateConnectionAssignmentCallable() 

  
CreateGoldengateConnectionAssignment |  Creates a new GoldengateConnectionAssignment in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGoldengateConnectionAssignmentAsync(LocationName parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId) 
  * createGoldengateConnectionAssignmentAsync(String parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGoldengateConnectionAssignmentOperationCallable() 
  * createGoldengateConnectionAssignmentCallable() 

  
DeleteGoldengateConnectionAssignment |  Deletes a single GoldengateConnectionAssignment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGoldengateConnectionAssignmentAsync(GoldengateConnectionAssignmentName name) 
  * deleteGoldengateConnectionAssignmentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGoldengateConnectionAssignmentOperationCallable() 
  * deleteGoldengateConnectionAssignmentCallable() 

  
TestGoldengateConnectionAssignment |  Tests a single GoldengateConnectionAssignment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testGoldengateConnectionAssignment(GoldengateConnectionAssignmentName name) 
  * testGoldengateConnectionAssignment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testGoldengateConnectionAssignmentCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of OracleDatabaseSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OracleDatabaseSettings oracleDatabaseSettings =
         OracleDatabaseSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create(oracleDatabaseSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OracleDatabaseSettings oracleDatabaseSettings =
         OracleDatabaseSettings.newBuilder().setEndpoint(myEndpoint).build();
     OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create(oracleDatabaseSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OracleDatabaseSettings oracleDatabaseSettings =
         OracleDatabaseSettings.newHttpJsonBuilder().build();
     OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create(oracleDatabaseSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OracleDatabaseClient

## Static Methods 

### create()
    
    
    public static final OracleDatabaseClient create()

Constructs an instance of OracleDatabaseClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OracleDatabaseSettings settings)
    
    
    public static final OracleDatabaseClient create(OracleDatabaseSettings settings)

Constructs an instance of OracleDatabaseClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OracleDatabaseSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OracleDatabaseStub stub)
    
    
    public static final OracleDatabaseClient create(OracleDatabaseStub stub)

Constructs an instance of OracleDatabaseClient, using the given stub for making calls. This is for advanced usage - prefer using create(OracleDatabaseSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OracleDatabaseStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.stub.OracleDatabaseStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient)` |   
  
## Constructors 

### OracleDatabaseClient(OracleDatabaseSettings settings)
    
    
    protected OracleDatabaseClient(OracleDatabaseSettings settings)

Constructs an instance of OracleDatabaseClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OracleDatabaseSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings)`  
  
  
### OracleDatabaseClient(OracleDatabaseStub stub)
    
    
    protected OracleDatabaseClient(OracleDatabaseStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OracleDatabaseStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.stub.OracleDatabaseStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### configureExascaleCloudExadataInfrastructureAsync(@Nullable CloudExadataInfrastructureName name, int totalStorageSizeGb)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> configureExascaleCloudExadataInfrastructureAsync(@Nullable CloudExadataInfrastructureName name, int totalStorageSizeGb)

Configures Exascale for a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudExadataInfrastructureName name =
           CloudExadataInfrastructureName.of(
               "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]");
       int totalStorageSizeGb = 1493200154;
       CloudExadataInfrastructure response =
           oracleDatabaseClient
               .configureExascaleCloudExadataInfrastructureAsync(name, totalStorageSizeGb)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudExadataInfrastructureName`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
`totalStorageSizeGb` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Required. The total storage to be allocated to Exascale in GBs.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### configureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest request)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> configureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest request)

Configures Exascale for a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ConfigureExascaleCloudExadataInfrastructureRequest request =
           ConfigureExascaleCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setTotalStorageSizeGb(1493200154)
               .setTotalVmStorageSizeGb(-1791568024)
               .setRequestId("requestId693933066")
               .build();
       CloudExadataInfrastructure response =
           oracleDatabaseClient.configureExascaleCloudExadataInfrastructureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ConfigureExascaleCloudExadataInfrastructureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### configureExascaleCloudExadataInfrastructureAsync(String name, int totalStorageSizeGb)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> configureExascaleCloudExadataInfrastructureAsync(String name, int totalStorageSizeGb)

Configures Exascale for a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           CloudExadataInfrastructureName.of(
                   "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
               .toString();
       int totalStorageSizeGb = 1493200154;
       CloudExadataInfrastructure response =
           oracleDatabaseClient
               .configureExascaleCloudExadataInfrastructureAsync(name, totalStorageSizeGb)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
`totalStorageSizeGb` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Required. The total storage to be allocated to Exascale in GBs.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### configureExascaleCloudExadataInfrastructureCallable()
    
    
    public final UnaryCallable<ConfigureExascaleCloudExadataInfrastructureRequest,Operation> configureExascaleCloudExadataInfrastructureCallable()

Configures Exascale for a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ConfigureExascaleCloudExadataInfrastructureRequest request =
           ConfigureExascaleCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setTotalStorageSizeGb(1493200154)
               .setTotalVmStorageSizeGb(-1791568024)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient
               .configureExascaleCloudExadataInfrastructureCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ConfigureExascaleCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureExascaleCloudExadataInfrastructureOperationCallable()
    
    
    public final OperationCallable<ConfigureExascaleCloudExadataInfrastructureRequest,CloudExadataInfrastructure,OperationMetadata> configureExascaleCloudExadataInfrastructureOperationCallable()

Configures Exascale for a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ConfigureExascaleCloudExadataInfrastructureRequest request =
           ConfigureExascaleCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setTotalStorageSizeGb(1493200154)
               .setTotalVmStorageSizeGb(-1791568024)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<CloudExadataInfrastructure, OperationMetadata> future =
           oracleDatabaseClient
               .configureExascaleCloudExadataInfrastructureOperationCallable()
               .futureCall(request);
       // Do something.
       CloudExadataInfrastructure response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ConfigureExascaleCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createAutonomousDatabaseAsync(@Nullable LocationName parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> createAutonomousDatabaseAsync(@Nullable LocationName parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId)

Creates a new Autonomous Database in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AutonomousDatabase autonomousDatabase = AutonomousDatabase.newBuilder().build();
       String autonomousDatabaseId = "autonomousDatabaseId-1972693114";
       AutonomousDatabase response =
           oracleDatabaseClient
               .createAutonomousDatabaseAsync(parent, autonomousDatabase, autonomousDatabaseId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
`autonomousDatabase` | `[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)`  
Required. The Autonomous Database being created.  
`autonomousDatabaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Autonomous Database to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> createAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest request)

Creates a new Autonomous Database in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateAutonomousDatabaseRequest request =
           CreateAutonomousDatabaseRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAutonomousDatabaseId("autonomousDatabaseId-1972693114")
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.createAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createAutonomousDatabaseAsync(String parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> createAutonomousDatabaseAsync(String parent, AutonomousDatabase autonomousDatabase, String autonomousDatabaseId)

Creates a new Autonomous Database in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AutonomousDatabase autonomousDatabase = AutonomousDatabase.newBuilder().build();
       String autonomousDatabaseId = "autonomousDatabaseId-1972693114";
       AutonomousDatabase response =
           oracleDatabaseClient
               .createAutonomousDatabaseAsync(parent, autonomousDatabase, autonomousDatabaseId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
`autonomousDatabase` | `[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)`  
Required. The Autonomous Database being created.  
`autonomousDatabaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Autonomous Database to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<CreateAutonomousDatabaseRequest,Operation> createAutonomousDatabaseCallable()

Creates a new Autonomous Database in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateAutonomousDatabaseRequest request =
           CreateAutonomousDatabaseRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAutonomousDatabaseId("autonomousDatabaseId-1972693114")
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<CreateAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> createAutonomousDatabaseOperationCallable()

Creates a new Autonomous Database in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateAutonomousDatabaseRequest request =
           CreateAutonomousDatabaseRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAutonomousDatabaseId("autonomousDatabaseId-1972693114")
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.createAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudExadataInfrastructureAsync(@Nullable LocationName parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> createCloudExadataInfrastructureAsync(@Nullable LocationName parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId)

Creates a new Exadata Infrastructure in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CloudExadataInfrastructure cloudExadataInfrastructure =
           CloudExadataInfrastructure.newBuilder().build();
       String cloudExadataInfrastructureId = "cloudExadataInfrastructureId975345409";
       CloudExadataInfrastructure response =
           oracleDatabaseClient
               .createCloudExadataInfrastructureAsync(
                   parent, cloudExadataInfrastructure, cloudExadataInfrastructureId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for CloudExadataInfrastructure in the following format: projects/{project}/locations/{location}.  
`cloudExadataInfrastructure` | `[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)`  
Required. Details of the Exadata Infrastructure instance to create.  
`cloudExadataInfrastructureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Exadata Infrastructure to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest request)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> createCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest request)

Creates a new Exadata Infrastructure in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudExadataInfrastructureRequest request =
           CreateCloudExadataInfrastructureRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudExadataInfrastructureId("cloudExadataInfrastructureId975345409")
               .setCloudExadataInfrastructure(CloudExadataInfrastructure.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       CloudExadataInfrastructure response =
           oracleDatabaseClient.createCloudExadataInfrastructureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudExadataInfrastructureAsync(String parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId)
    
    
    public final OperationFuture<CloudExadataInfrastructure,OperationMetadata> createCloudExadataInfrastructureAsync(String parent, CloudExadataInfrastructure cloudExadataInfrastructure, String cloudExadataInfrastructureId)

Creates a new Exadata Infrastructure in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CloudExadataInfrastructure cloudExadataInfrastructure =
           CloudExadataInfrastructure.newBuilder().build();
       String cloudExadataInfrastructureId = "cloudExadataInfrastructureId975345409";
       CloudExadataInfrastructure response =
           oracleDatabaseClient
               .createCloudExadataInfrastructureAsync(
                   parent, cloudExadataInfrastructure, cloudExadataInfrastructureId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for CloudExadataInfrastructure in the following format: projects/{project}/locations/{location}.  
`cloudExadataInfrastructure` | `[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)`  
Required. Details of the Exadata Infrastructure instance to create.  
`cloudExadataInfrastructureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Exadata Infrastructure to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudExadataInfrastructureCallable()
    
    
    public final UnaryCallable<CreateCloudExadataInfrastructureRequest,Operation> createCloudExadataInfrastructureCallable()

Creates a new Exadata Infrastructure in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudExadataInfrastructureRequest request =
           CreateCloudExadataInfrastructureRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudExadataInfrastructureId("cloudExadataInfrastructureId975345409")
               .setCloudExadataInfrastructure(CloudExadataInfrastructure.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createCloudExadataInfrastructureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCloudExadataInfrastructureOperationCallable()
    
    
    public final OperationCallable<CreateCloudExadataInfrastructureRequest,CloudExadataInfrastructure,OperationMetadata> createCloudExadataInfrastructureOperationCallable()

Creates a new Exadata Infrastructure in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudExadataInfrastructureRequest request =
           CreateCloudExadataInfrastructureRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudExadataInfrastructureId("cloudExadataInfrastructureId975345409")
               .setCloudExadataInfrastructure(CloudExadataInfrastructure.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<CloudExadataInfrastructure, OperationMetadata> future =
           oracleDatabaseClient
               .createCloudExadataInfrastructureOperationCallable()
               .futureCall(request);
       // Do something.
       CloudExadataInfrastructure response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudVmClusterAsync(@Nullable LocationName parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId)
    
    
    public final OperationFuture<CloudVmCluster,OperationMetadata> createCloudVmClusterAsync(@Nullable LocationName parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId)

Creates a new VM Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CloudVmCluster cloudVmCluster = CloudVmCluster.newBuilder().build();
       String cloudVmClusterId = "cloudVmClusterId-1217103287";
       CloudVmCluster response =
           oracleDatabaseClient
               .createCloudVmClusterAsync(parent, cloudVmCluster, cloudVmClusterId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
`cloudVmCluster` | `[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)`  
Required. The resource being created  
`cloudVmClusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the VM Cluster to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudVmClusterAsync(CreateCloudVmClusterRequest request)
    
    
    public final OperationFuture<CloudVmCluster,OperationMetadata> createCloudVmClusterAsync(CreateCloudVmClusterRequest request)

Creates a new VM Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudVmClusterRequest request =
           CreateCloudVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudVmClusterId("cloudVmClusterId-1217103287")
               .setCloudVmCluster(CloudVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       CloudVmCluster response = oracleDatabaseClient.createCloudVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudVmClusterAsync(String parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId)
    
    
    public final OperationFuture<CloudVmCluster,OperationMetadata> createCloudVmClusterAsync(String parent, CloudVmCluster cloudVmCluster, String cloudVmClusterId)

Creates a new VM Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CloudVmCluster cloudVmCluster = CloudVmCluster.newBuilder().build();
       String cloudVmClusterId = "cloudVmClusterId-1217103287";
       CloudVmCluster response =
           oracleDatabaseClient
               .createCloudVmClusterAsync(parent, cloudVmCluster, cloudVmClusterId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
`cloudVmCluster` | `[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)`  
Required. The resource being created  
`cloudVmClusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the VM Cluster to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudVmClusterCallable()
    
    
    public final UnaryCallable<CreateCloudVmClusterRequest,Operation> createCloudVmClusterCallable()

Creates a new VM Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudVmClusterRequest request =
           CreateCloudVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudVmClusterId("cloudVmClusterId-1217103287")
               .setCloudVmCluster(CloudVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createCloudVmClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCloudVmClusterOperationCallable()
    
    
    public final OperationCallable<CreateCloudVmClusterRequest,CloudVmCluster,OperationMetadata> createCloudVmClusterOperationCallable()

Creates a new VM Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateCloudVmClusterRequest request =
           CreateCloudVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCloudVmClusterId("cloudVmClusterId-1217103287")
               .setCloudVmCluster(CloudVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<CloudVmCluster, OperationMetadata> future =
           oracleDatabaseClient.createCloudVmClusterOperationCallable().futureCall(request);
       // Do something.
       CloudVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudVmClusterRequest),[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createDbSystemAsync(@Nullable LocationName parent, DbSystem dbSystem, String dbSystemId)
    
    
    public final OperationFuture<DbSystem,OperationMetadata> createDbSystemAsync(@Nullable LocationName parent, DbSystem dbSystem, String dbSystemId)

Creates a new DbSystem in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DbSystem dbSystem = DbSystem.newBuilder().build();
       String dbSystemId = "dbSystemId-1467630008";
       DbSystem response =
           oracleDatabaseClient.createDbSystemAsync(parent, dbSystem, dbSystemId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The value for parent of the DbSystem in the following format: projects/{project}/locations/{location}.  
`dbSystem` | `[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)`  
Required. The resource being created.  
`dbSystemId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DbSystem to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createDbSystemAsync(CreateDbSystemRequest request)
    
    
    public final OperationFuture<DbSystem,OperationMetadata> createDbSystemAsync(CreateDbSystemRequest request)

Creates a new DbSystem in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateDbSystemRequest request =
           CreateDbSystemRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDbSystemId("dbSystemId-1467630008")
               .setDbSystem(DbSystem.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       DbSystem response = oracleDatabaseClient.createDbSystemAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateDbSystemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createDbSystemAsync(String parent, DbSystem dbSystem, String dbSystemId)
    
    
    public final OperationFuture<DbSystem,OperationMetadata> createDbSystemAsync(String parent, DbSystem dbSystem, String dbSystemId)

Creates a new DbSystem in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DbSystem dbSystem = DbSystem.newBuilder().build();
       String dbSystemId = "dbSystemId-1467630008";
       DbSystem response =
           oracleDatabaseClient.createDbSystemAsync(parent, dbSystem, dbSystemId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value for parent of the DbSystem in the following format: projects/{project}/locations/{location}.  
`dbSystem` | `[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)`  
Required. The resource being created.  
`dbSystemId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DbSystem to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createDbSystemCallable()
    
    
    public final UnaryCallable<CreateDbSystemRequest,Operation> createDbSystemCallable()

Creates a new DbSystem in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateDbSystemRequest request =
           CreateDbSystemRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDbSystemId("dbSystemId-1467630008")
               .setDbSystem(DbSystem.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createDbSystemCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateDbSystemRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDbSystemOperationCallable()
    
    
    public final OperationCallable<CreateDbSystemRequest,DbSystem,OperationMetadata> createDbSystemOperationCallable()

Creates a new DbSystem in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateDbSystemRequest request =
           CreateDbSystemRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDbSystemId("dbSystemId-1467630008")
               .setDbSystem(DbSystem.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<DbSystem, OperationMetadata> future =
           oracleDatabaseClient.createDbSystemOperationCallable().futureCall(request);
       // Do something.
       DbSystem response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateDbSystemRequest),[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExadbVmClusterAsync(@Nullable LocationName parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> createExadbVmClusterAsync(@Nullable LocationName parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId)

Creates a new Exadb (Exascale) VM Cluster resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ExadbVmCluster exadbVmCluster = ExadbVmCluster.newBuilder().build();
       String exadbVmClusterId = "exadbVmClusterId1890152722";
       ExadbVmCluster response =
           oracleDatabaseClient
               .createExadbVmClusterAsync(parent, exadbVmCluster, exadbVmClusterId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The value for parent of the ExadbVmCluster in the following format: projects/{project}/locations/{location}.  
`exadbVmCluster` | `[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)`  
Required. The resource being created.  
`exadbVmClusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the ExadbVmCluster to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExadbVmClusterAsync(CreateExadbVmClusterRequest request)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> createExadbVmClusterAsync(CreateExadbVmClusterRequest request)

Creates a new Exadb (Exascale) VM Cluster resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExadbVmClusterRequest request =
           CreateExadbVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExadbVmClusterId("exadbVmClusterId1890152722")
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ExadbVmCluster response = oracleDatabaseClient.createExadbVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExadbVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExadbVmClusterAsync(String parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> createExadbVmClusterAsync(String parent, ExadbVmCluster exadbVmCluster, String exadbVmClusterId)

Creates a new Exadb (Exascale) VM Cluster resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ExadbVmCluster exadbVmCluster = ExadbVmCluster.newBuilder().build();
       String exadbVmClusterId = "exadbVmClusterId1890152722";
       ExadbVmCluster response =
           oracleDatabaseClient
               .createExadbVmClusterAsync(parent, exadbVmCluster, exadbVmClusterId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value for parent of the ExadbVmCluster in the following format: projects/{project}/locations/{location}.  
`exadbVmCluster` | `[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)`  
Required. The resource being created.  
`exadbVmClusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the ExadbVmCluster to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExadbVmClusterCallable()
    
    
    public final UnaryCallable<CreateExadbVmClusterRequest,Operation> createExadbVmClusterCallable()

Creates a new Exadb (Exascale) VM Cluster resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExadbVmClusterRequest request =
           CreateExadbVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExadbVmClusterId("exadbVmClusterId1890152722")
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createExadbVmClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExadbVmClusterOperationCallable()
    
    
    public final OperationCallable<CreateExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> createExadbVmClusterOperationCallable()

Creates a new Exadb (Exascale) VM Cluster resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExadbVmClusterRequest request =
           CreateExadbVmClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExadbVmClusterId("exadbVmClusterId1890152722")
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExadbVmCluster, OperationMetadata> future =
           oracleDatabaseClient.createExadbVmClusterOperationCallable().futureCall(request);
       // Do something.
       ExadbVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExascaleDbStorageVaultAsync(@Nullable LocationName parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId)
    
    
    public final OperationFuture<ExascaleDbStorageVault,OperationMetadata> createExascaleDbStorageVaultAsync(@Nullable LocationName parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId)

Creates a new ExascaleDB Storage Vault resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ExascaleDbStorageVault exascaleDbStorageVault = ExascaleDbStorageVault.newBuilder().build();
       String exascaleDbStorageVaultId = "exascaleDbStorageVaultId-24370132";
       ExascaleDbStorageVault response =
           oracleDatabaseClient
               .createExascaleDbStorageVaultAsync(
                   parent, exascaleDbStorageVault, exascaleDbStorageVaultId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The value for parent of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.  
`exascaleDbStorageVault` | `[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)`  
Required. The resource being created.  
`exascaleDbStorageVaultId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the ExascaleDbStorageVault to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest request)
    
    
    public final OperationFuture<ExascaleDbStorageVault,OperationMetadata> createExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest request)

Creates a new ExascaleDB Storage Vault resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExascaleDbStorageVaultRequest request =
           CreateExascaleDbStorageVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExascaleDbStorageVaultId("exascaleDbStorageVaultId-24370132")
               .setExascaleDbStorageVault(ExascaleDbStorageVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ExascaleDbStorageVault response =
           oracleDatabaseClient.createExascaleDbStorageVaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExascaleDbStorageVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExascaleDbStorageVaultAsync(String parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId)
    
    
    public final OperationFuture<ExascaleDbStorageVault,OperationMetadata> createExascaleDbStorageVaultAsync(String parent, ExascaleDbStorageVault exascaleDbStorageVault, String exascaleDbStorageVaultId)

Creates a new ExascaleDB Storage Vault resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ExascaleDbStorageVault exascaleDbStorageVault = ExascaleDbStorageVault.newBuilder().build();
       String exascaleDbStorageVaultId = "exascaleDbStorageVaultId-24370132";
       ExascaleDbStorageVault response =
           oracleDatabaseClient
               .createExascaleDbStorageVaultAsync(
                   parent, exascaleDbStorageVault, exascaleDbStorageVaultId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value for parent of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.  
`exascaleDbStorageVault` | `[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)`  
Required. The resource being created.  
`exascaleDbStorageVaultId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the ExascaleDbStorageVault to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExascaleDbStorageVaultCallable()
    
    
    public final UnaryCallable<CreateExascaleDbStorageVaultRequest,Operation> createExascaleDbStorageVaultCallable()

Creates a new ExascaleDB Storage Vault resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExascaleDbStorageVaultRequest request =
           CreateExascaleDbStorageVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExascaleDbStorageVaultId("exascaleDbStorageVaultId-24370132")
               .setExascaleDbStorageVault(ExascaleDbStorageVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createExascaleDbStorageVaultCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExascaleDbStorageVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExascaleDbStorageVaultOperationCallable()
    
    
    public final OperationCallable<CreateExascaleDbStorageVaultRequest,ExascaleDbStorageVault,OperationMetadata> createExascaleDbStorageVaultOperationCallable()

Creates a new ExascaleDB Storage Vault resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateExascaleDbStorageVaultRequest request =
           CreateExascaleDbStorageVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExascaleDbStorageVaultId("exascaleDbStorageVaultId-24370132")
               .setExascaleDbStorageVault(ExascaleDbStorageVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExascaleDbStorageVault, OperationMetadata> future =
           oracleDatabaseClient.createExascaleDbStorageVaultOperationCallable().futureCall(request);
       // Do something.
       ExascaleDbStorageVault response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExascaleDbStorageVaultRequest),[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAssignmentAsync(@Nullable LocationName parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId)
    
    
    public final OperationFuture<GoldengateConnectionAssignment,OperationMetadata> createGoldengateConnectionAssignmentAsync(@Nullable LocationName parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId)

Creates a new GoldengateConnectionAssignment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       GoldengateConnectionAssignment goldengateConnectionAssignment =
           GoldengateConnectionAssignment.newBuilder().build();
       String goldengateConnectionAssignmentId = "goldengateConnectionAssignmentId-1362669254";
       GoldengateConnectionAssignment response =
           oracleDatabaseClient
               .createGoldengateConnectionAssignmentAsync(
                   parent, goldengateConnectionAssignment, goldengateConnectionAssignmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent resource where this GoldengateConnectionAssignment will be created. Format: projects/{project}/locations/{location}  
`goldengateConnectionAssignment` | `[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)`  
Required. The GoldengateConnectionAssignment to create.  
`goldengateConnectionAssignmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateConnectionAssignment to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest request)
    
    
    public final OperationFuture<GoldengateConnectionAssignment,OperationMetadata> createGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest request)

Creates a new GoldengateConnectionAssignment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionAssignmentRequest request =
           CreateGoldengateConnectionAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionAssignmentId("goldengateConnectionAssignmentId-1362669254")
               .setGoldengateConnectionAssignment(
                   GoldengateConnectionAssignment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       GoldengateConnectionAssignment response =
           oracleDatabaseClient.createGoldengateConnectionAssignmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAssignmentAsync(String parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId)
    
    
    public final OperationFuture<GoldengateConnectionAssignment,OperationMetadata> createGoldengateConnectionAssignmentAsync(String parent, GoldengateConnectionAssignment goldengateConnectionAssignment, String goldengateConnectionAssignmentId)

Creates a new GoldengateConnectionAssignment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       GoldengateConnectionAssignment goldengateConnectionAssignment =
           GoldengateConnectionAssignment.newBuilder().build();
       String goldengateConnectionAssignmentId = "goldengateConnectionAssignmentId-1362669254";
       GoldengateConnectionAssignment response =
           oracleDatabaseClient
               .createGoldengateConnectionAssignmentAsync(
                   parent, goldengateConnectionAssignment, goldengateConnectionAssignmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this GoldengateConnectionAssignment will be created. Format: projects/{project}/locations/{location}  
`goldengateConnectionAssignment` | `[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)`  
Required. The GoldengateConnectionAssignment to create.  
`goldengateConnectionAssignmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateConnectionAssignment to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAssignmentCallable()
    
    
    public final UnaryCallable<CreateGoldengateConnectionAssignmentRequest,Operation> createGoldengateConnectionAssignmentCallable()

Creates a new GoldengateConnectionAssignment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionAssignmentRequest request =
           CreateGoldengateConnectionAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionAssignmentId("goldengateConnectionAssignmentId-1362669254")
               .setGoldengateConnectionAssignment(
                   GoldengateConnectionAssignment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createGoldengateConnectionAssignmentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateConnectionAssignmentOperationCallable()
    
    
    public final OperationCallable<CreateGoldengateConnectionAssignmentRequest,GoldengateConnectionAssignment,OperationMetadata> createGoldengateConnectionAssignmentOperationCallable()

Creates a new GoldengateConnectionAssignment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionAssignmentRequest request =
           CreateGoldengateConnectionAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionAssignmentId("goldengateConnectionAssignmentId-1362669254")
               .setGoldengateConnectionAssignment(
                   GoldengateConnectionAssignment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<GoldengateConnectionAssignment, OperationMetadata> future =
           oracleDatabaseClient
               .createGoldengateConnectionAssignmentOperationCallable()
               .futureCall(request);
       // Do something.
       GoldengateConnectionAssignment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionAssignmentRequest),[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAsync(@Nullable LocationName parent, GoldengateConnection goldengateConnection, String goldengateConnectionId)
    
    
    public final OperationFuture<GoldengateConnection,OperationMetadata> createGoldengateConnectionAsync(@Nullable LocationName parent, GoldengateConnection goldengateConnection, String goldengateConnectionId)

Creates a new GoldengateConnection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       GoldengateConnection goldengateConnection = GoldengateConnection.newBuilder().build();
       String goldengateConnectionId = "goldengateConnectionId-1745824755";
       GoldengateConnection response =
           oracleDatabaseClient
               .createGoldengateConnectionAsync(parent, goldengateConnection, goldengateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The value for parent of the GoldengateConnection in the following format: projects/{project}/locations/{location}.  
`goldengateConnection` | `[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)`  
Required. The resource being created.  
`goldengateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateConnection to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAsync(CreateGoldengateConnectionRequest request)
    
    
    public final OperationFuture<GoldengateConnection,OperationMetadata> createGoldengateConnectionAsync(CreateGoldengateConnectionRequest request)

Creates a new GoldengateConnection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionRequest request =
           CreateGoldengateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionId("goldengateConnectionId-1745824755")
               .setGoldengateConnection(GoldengateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       GoldengateConnection response =
           oracleDatabaseClient.createGoldengateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAsync(String parent, GoldengateConnection goldengateConnection, String goldengateConnectionId)
    
    
    public final OperationFuture<GoldengateConnection,OperationMetadata> createGoldengateConnectionAsync(String parent, GoldengateConnection goldengateConnection, String goldengateConnectionId)

Creates a new GoldengateConnection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       GoldengateConnection goldengateConnection = GoldengateConnection.newBuilder().build();
       String goldengateConnectionId = "goldengateConnectionId-1745824755";
       GoldengateConnection response =
           oracleDatabaseClient
               .createGoldengateConnectionAsync(parent, goldengateConnection, goldengateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value for parent of the GoldengateConnection in the following format: projects/{project}/locations/{location}.  
`goldengateConnection` | `[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)`  
Required. The resource being created.  
`goldengateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateConnection to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionCallable()
    
    
    public final UnaryCallable<CreateGoldengateConnectionRequest,Operation> createGoldengateConnectionCallable()

Creates a new GoldengateConnection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionRequest request =
           CreateGoldengateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionId("goldengateConnectionId-1745824755")
               .setGoldengateConnection(GoldengateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createGoldengateConnectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateConnectionOperationCallable()
    
    
    public final OperationCallable<CreateGoldengateConnectionRequest,GoldengateConnection,OperationMetadata> createGoldengateConnectionOperationCallable()

Creates a new GoldengateConnection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateConnectionRequest request =
           CreateGoldengateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateConnectionId("goldengateConnectionId-1745824755")
               .setGoldengateConnection(GoldengateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<GoldengateConnection, OperationMetadata> future =
           oracleDatabaseClient.createGoldengateConnectionOperationCallable().futureCall(request);
       // Do something.
       GoldengateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionRequest),[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateDeploymentAsync(@Nullable LocationName parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> createGoldengateDeploymentAsync(@Nullable LocationName parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId)

Creates a new GoldengateDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       GoldengateDeployment goldengateDeployment = GoldengateDeployment.newBuilder().build();
       String goldengateDeploymentId = "goldengateDeploymentId489140788";
       GoldengateDeployment response =
           oracleDatabaseClient
               .createGoldengateDeploymentAsync(parent, goldengateDeployment, goldengateDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The value for parent of the GoldengateDeployment in the following format: projects/{project}/locations/{location}.  
`goldengateDeployment` | `[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)`  
Required. The resource being created.  
`goldengateDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateDeployment to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest request)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> createGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest request)

Creates a new GoldengateDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateDeploymentRequest request =
           CreateGoldengateDeploymentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateDeploymentId("goldengateDeploymentId489140788")
               .setGoldengateDeployment(GoldengateDeployment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       GoldengateDeployment response =
           oracleDatabaseClient.createGoldengateDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateDeploymentAsync(String parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> createGoldengateDeploymentAsync(String parent, GoldengateDeployment goldengateDeployment, String goldengateDeploymentId)

Creates a new GoldengateDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       GoldengateDeployment goldengateDeployment = GoldengateDeployment.newBuilder().build();
       String goldengateDeploymentId = "goldengateDeploymentId489140788";
       GoldengateDeployment response =
           oracleDatabaseClient
               .createGoldengateDeploymentAsync(parent, goldengateDeployment, goldengateDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value for parent of the GoldengateDeployment in the following format: projects/{project}/locations/{location}.  
`goldengateDeployment` | `[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)`  
Required. The resource being created.  
`goldengateDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the GoldengateDeployment to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateDeploymentCallable()
    
    
    public final UnaryCallable<CreateGoldengateDeploymentRequest,Operation> createGoldengateDeploymentCallable()

Creates a new GoldengateDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateDeploymentRequest request =
           CreateGoldengateDeploymentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateDeploymentId("goldengateDeploymentId489140788")
               .setGoldengateDeployment(GoldengateDeployment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createGoldengateDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateDeploymentOperationCallable()
    
    
    public final OperationCallable<CreateGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> createGoldengateDeploymentOperationCallable()

Creates a new GoldengateDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateGoldengateDeploymentRequest request =
           CreateGoldengateDeploymentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGoldengateDeploymentId("goldengateDeploymentId489140788")
               .setGoldengateDeployment(GoldengateDeployment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<GoldengateDeployment, OperationMetadata> future =
           oracleDatabaseClient.createGoldengateDeploymentOperationCallable().futureCall(request);
       // Do something.
       GoldengateDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbNetworkAsync(@Nullable LocationName parent, OdbNetwork odbNetwork, String odbNetworkId)
    
    
    public final OperationFuture<OdbNetwork,OperationMetadata> createOdbNetworkAsync(@Nullable LocationName parent, OdbNetwork odbNetwork, String odbNetworkId)

Creates a new ODB Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       OdbNetwork odbNetwork = OdbNetwork.newBuilder().build();
       String odbNetworkId = "odbNetworkId-169900740";
       OdbNetwork response =
           oracleDatabaseClient.createOdbNetworkAsync(parent, odbNetwork, odbNetworkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the OdbNetwork in the following format: projects/{project}/locations/{location}.  
`odbNetwork` | `[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)`  
Required. Details of the OdbNetwork instance to create.  
`odbNetworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the OdbNetwork to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbNetworkAsync(CreateOdbNetworkRequest request)
    
    
    public final OperationFuture<OdbNetwork,OperationMetadata> createOdbNetworkAsync(CreateOdbNetworkRequest request)

Creates a new ODB Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbNetworkRequest request =
           CreateOdbNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOdbNetworkId("odbNetworkId-169900740")
               .setOdbNetwork(OdbNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OdbNetwork response = oracleDatabaseClient.createOdbNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbNetworkAsync(String parent, OdbNetwork odbNetwork, String odbNetworkId)
    
    
    public final OperationFuture<OdbNetwork,OperationMetadata> createOdbNetworkAsync(String parent, OdbNetwork odbNetwork, String odbNetworkId)

Creates a new ODB Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       OdbNetwork odbNetwork = OdbNetwork.newBuilder().build();
       String odbNetworkId = "odbNetworkId-169900740";
       OdbNetwork response =
           oracleDatabaseClient.createOdbNetworkAsync(parent, odbNetwork, odbNetworkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the OdbNetwork in the following format: projects/{project}/locations/{location}.  
`odbNetwork` | `[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)`  
Required. Details of the OdbNetwork instance to create.  
`odbNetworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the OdbNetwork to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbNetworkCallable()
    
    
    public final UnaryCallable<CreateOdbNetworkRequest,Operation> createOdbNetworkCallable()

Creates a new ODB Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbNetworkRequest request =
           CreateOdbNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOdbNetworkId("odbNetworkId-169900740")
               .setOdbNetwork(OdbNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createOdbNetworkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOdbNetworkOperationCallable()
    
    
    public final OperationCallable<CreateOdbNetworkRequest,OdbNetwork,OperationMetadata> createOdbNetworkOperationCallable()

Creates a new ODB Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbNetworkRequest request =
           CreateOdbNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOdbNetworkId("odbNetworkId-169900740")
               .setOdbNetwork(OdbNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<OdbNetwork, OperationMetadata> future =
           oracleDatabaseClient.createOdbNetworkOperationCallable().futureCall(request);
       // Do something.
       OdbNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbNetworkRequest),[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbSubnetAsync(@Nullable OdbNetworkName parent, OdbSubnet odbSubnet, String odbSubnetId)
    
    
    public final OperationFuture<OdbSubnet,OperationMetadata> createOdbSubnetAsync(@Nullable OdbNetworkName parent, OdbSubnet odbSubnet, String odbSubnetId)

Creates a new ODB Subnet in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbNetworkName parent = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]");
       OdbSubnet odbSubnet = OdbSubnet.newBuilder().build();
       String odbSubnetId = "odbSubnetId1186954661";
       OdbSubnet response =
           oracleDatabaseClient.createOdbSubnetAsync(parent, odbSubnet, odbSubnetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbNetworkName`  
Required. The parent value for the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
`odbSubnet` | `[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)`  
Required. Details of the OdbSubnet instance to create.  
`odbSubnetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the OdbSubnet to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbSubnetAsync(CreateOdbSubnetRequest request)
    
    
    public final OperationFuture<OdbSubnet,OperationMetadata> createOdbSubnetAsync(CreateOdbSubnetRequest request)

Creates a new ODB Subnet in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbSubnetRequest request =
           CreateOdbSubnetRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setOdbSubnetId("odbSubnetId1186954661")
               .setOdbSubnet(OdbSubnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OdbSubnet response = oracleDatabaseClient.createOdbSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbSubnetAsync(String parent, OdbSubnet odbSubnet, String odbSubnetId)
    
    
    public final OperationFuture<OdbSubnet,OperationMetadata> createOdbSubnetAsync(String parent, OdbSubnet odbSubnet, String odbSubnetId)

Creates a new ODB Subnet in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString();
       OdbSubnet odbSubnet = OdbSubnet.newBuilder().build();
       String odbSubnetId = "odbSubnetId1186954661";
       OdbSubnet response =
           oracleDatabaseClient.createOdbSubnetAsync(parent, odbSubnet, odbSubnetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
`odbSubnet` | `[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)`  
Required. Details of the OdbSubnet instance to create.  
`odbSubnetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the OdbSubnet to create. This value is restricted to (^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$) and must be a maximum of 63 characters in length. The value must start with a letter and end with a letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbSubnetCallable()
    
    
    public final UnaryCallable<CreateOdbSubnetRequest,Operation> createOdbSubnetCallable()

Creates a new ODB Subnet in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbSubnetRequest request =
           CreateOdbSubnetRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setOdbSubnetId("odbSubnetId1186954661")
               .setOdbSubnet(OdbSubnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.createOdbSubnetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOdbSubnetOperationCallable()
    
    
    public final OperationCallable<CreateOdbSubnetRequest,OdbSubnet,OperationMetadata> createOdbSubnetOperationCallable()

Creates a new ODB Subnet in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CreateOdbSubnetRequest request =
           CreateOdbSubnetRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setOdbSubnetId("odbSubnetId1186954661")
               .setOdbSubnet(OdbSubnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<OdbSubnet, OperationMetadata> future =
           oracleDatabaseClient.createOdbSubnetOperationCallable().futureCall(request);
       // Do something.
       OdbSubnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbSubnetRequest),[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)

Deletes a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       oracleDatabaseClient.deleteAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the resource in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest request)

Deletes a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteAutonomousDatabaseRequest request =
           DeleteAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteAutonomousDatabaseAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAutonomousDatabaseAsync(String name)

Deletes a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       oracleDatabaseClient.deleteAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<DeleteAutonomousDatabaseRequest,Operation> deleteAutonomousDatabaseCallable()

Deletes a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteAutonomousDatabaseRequest request =
           DeleteAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<DeleteAutonomousDatabaseRequest,Empty,OperationMetadata> deleteAutonomousDatabaseOperationCallable()

Deletes a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteAutonomousDatabaseRequest request =
           DeleteAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteAutonomousDatabaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudExadataInfrastructureAsync(@Nullable CloudExadataInfrastructureName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudExadataInfrastructureAsync(@Nullable CloudExadataInfrastructureName name)

Deletes a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudExadataInfrastructureName name =
           CloudExadataInfrastructureName.of(
               "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]");
       oracleDatabaseClient.deleteCloudExadataInfrastructureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudExadataInfrastructureName`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest request)

Deletes a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudExadataInfrastructureRequest request =
           DeleteCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       oracleDatabaseClient.deleteCloudExadataInfrastructureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudExadataInfrastructureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudExadataInfrastructureAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudExadataInfrastructureAsync(String name)

Deletes a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           CloudExadataInfrastructureName.of(
                   "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
               .toString();
       oracleDatabaseClient.deleteCloudExadataInfrastructureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudExadataInfrastructureCallable()
    
    
    public final UnaryCallable<DeleteCloudExadataInfrastructureRequest,Operation> deleteCloudExadataInfrastructureCallable()

Deletes a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudExadataInfrastructureRequest request =
           DeleteCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteCloudExadataInfrastructureCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCloudExadataInfrastructureOperationCallable()
    
    
    public final OperationCallable<DeleteCloudExadataInfrastructureRequest,Empty,OperationMetadata> deleteCloudExadataInfrastructureOperationCallable()

Deletes a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudExadataInfrastructureRequest request =
           DeleteCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient
               .deleteCloudExadataInfrastructureOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudExadataInfrastructureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudVmClusterAsync(@Nullable CloudVmClusterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudVmClusterAsync(@Nullable CloudVmClusterName name)

Deletes a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudVmClusterName name =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]");
       oracleDatabaseClient.deleteCloudVmClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudVmClusterName`  
Required. The name of the Cloud VM Cluster in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudVmClusterAsync(DeleteCloudVmClusterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudVmClusterAsync(DeleteCloudVmClusterRequest request)

Deletes a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudVmClusterRequest request =
           DeleteCloudVmClusterRequest.newBuilder()
               .setName(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       oracleDatabaseClient.deleteCloudVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudVmClusterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCloudVmClusterAsync(String name)

Deletes a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString();
       oracleDatabaseClient.deleteCloudVmClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Cloud VM Cluster in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudVmClusterCallable()
    
    
    public final UnaryCallable<DeleteCloudVmClusterRequest,Operation> deleteCloudVmClusterCallable()

Deletes a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudVmClusterRequest request =
           DeleteCloudVmClusterRequest.newBuilder()
               .setName(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteCloudVmClusterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCloudVmClusterOperationCallable()
    
    
    public final OperationCallable<DeleteCloudVmClusterRequest,Empty,OperationMetadata> deleteCloudVmClusterOperationCallable()

Deletes a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteCloudVmClusterRequest request =
           DeleteCloudVmClusterRequest.newBuilder()
               .setName(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteCloudVmClusterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudVmClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteDbSystemAsync(@Nullable DbSystemName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDbSystemAsync(@Nullable DbSystemName name)

Deletes a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DbSystemName name = DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]");
       oracleDatabaseClient.deleteDbSystemAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.DbSystemName`  
Required. The name of the DbSystem in the following format: projects/{project}/locations/{location}/dbSystems/{db_system}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteDbSystemAsync(DeleteDbSystemRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDbSystemAsync(DeleteDbSystemRequest request)

Deletes a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteDbSystemRequest request =
           DeleteDbSystemRequest.newBuilder()
               .setName(DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteDbSystemAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteDbSystemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteDbSystemAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDbSystemAsync(String name)

Deletes a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name = DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString();
       oracleDatabaseClient.deleteDbSystemAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DbSystem in the following format: projects/{project}/locations/{location}/dbSystems/{db_system}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteDbSystemCallable()
    
    
    public final UnaryCallable<DeleteDbSystemRequest,Operation> deleteDbSystemCallable()

Deletes a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteDbSystemRequest request =
           DeleteDbSystemRequest.newBuilder()
               .setName(DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteDbSystemCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteDbSystemRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDbSystemOperationCallable()
    
    
    public final OperationCallable<DeleteDbSystemRequest,Empty,OperationMetadata> deleteDbSystemOperationCallable()

Deletes a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteDbSystemRequest request =
           DeleteDbSystemRequest.newBuilder()
               .setName(DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteDbSystemOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteDbSystemRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExadbVmClusterAsync(@Nullable ExadbVmClusterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExadbVmClusterAsync(@Nullable ExadbVmClusterName name)

Deletes a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExadbVmClusterName name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]");
       oracleDatabaseClient.deleteExadbVmClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExadbVmClusterName`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExadbVmClusterAsync(DeleteExadbVmClusterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExadbVmClusterAsync(DeleteExadbVmClusterRequest request)

Deletes a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExadbVmClusterRequest request =
           DeleteExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteExadbVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExadbVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExadbVmClusterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExadbVmClusterAsync(String name)

Deletes a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString();
       oracleDatabaseClient.deleteExadbVmClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExadbVmClusterCallable()
    
    
    public final UnaryCallable<DeleteExadbVmClusterRequest,Operation> deleteExadbVmClusterCallable()

Deletes a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExadbVmClusterRequest request =
           DeleteExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteExadbVmClusterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExadbVmClusterOperationCallable()
    
    
    public final OperationCallable<DeleteExadbVmClusterRequest,Empty,OperationMetadata> deleteExadbVmClusterOperationCallable()

Deletes a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExadbVmClusterRequest request =
           DeleteExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteExadbVmClusterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExadbVmClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExascaleDbStorageVaultAsync(@Nullable ExascaleDbStorageVaultName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExascaleDbStorageVaultAsync(@Nullable ExascaleDbStorageVaultName name)

Deletes a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExascaleDbStorageVaultName name =
           ExascaleDbStorageVaultName.of("[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]");
       oracleDatabaseClient.deleteExascaleDbStorageVaultAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExascaleDbStorageVaultName`  
Required. The name of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest request)

Deletes a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExascaleDbStorageVaultRequest request =
           DeleteExascaleDbStorageVaultRequest.newBuilder()
               .setName(
                   ExascaleDbStorageVaultName.of(
                           "[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteExascaleDbStorageVaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExascaleDbStorageVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExascaleDbStorageVaultAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExascaleDbStorageVaultAsync(String name)

Deletes a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           ExascaleDbStorageVaultName.of("[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
               .toString();
       oracleDatabaseClient.deleteExascaleDbStorageVaultAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExascaleDbStorageVaultCallable()
    
    
    public final UnaryCallable<DeleteExascaleDbStorageVaultRequest,Operation> deleteExascaleDbStorageVaultCallable()

Deletes a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExascaleDbStorageVaultRequest request =
           DeleteExascaleDbStorageVaultRequest.newBuilder()
               .setName(
                   ExascaleDbStorageVaultName.of(
                           "[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteExascaleDbStorageVaultCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExascaleDbStorageVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExascaleDbStorageVaultOperationCallable()
    
    
    public final OperationCallable<DeleteExascaleDbStorageVaultRequest,Empty,OperationMetadata> deleteExascaleDbStorageVaultOperationCallable()

Deletes a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteExascaleDbStorageVaultRequest request =
           DeleteExascaleDbStorageVaultRequest.newBuilder()
               .setName(
                   ExascaleDbStorageVaultName.of(
                           "[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteExascaleDbStorageVaultOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExascaleDbStorageVaultRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAssignmentAsync(@Nullable GoldengateConnectionAssignmentName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAssignmentAsync(@Nullable GoldengateConnectionAssignmentName name)

Deletes a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateConnectionAssignmentName name =
           GoldengateConnectionAssignmentName.of(
               "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]");
       oracleDatabaseClient.deleteGoldengateConnectionAssignmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignmentName`  
Required. The name of the GoldengateConnectionAssignment to delete. Format: projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest request)

Deletes a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionAssignmentRequest request =
           DeleteGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteGoldengateConnectionAssignmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAssignmentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAssignmentAsync(String name)

Deletes a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateConnectionAssignmentName.of(
                   "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
               .toString();
       oracleDatabaseClient.deleteGoldengateConnectionAssignmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateConnectionAssignment to delete. Format: projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAssignmentCallable()
    
    
    public final UnaryCallable<DeleteGoldengateConnectionAssignmentRequest,Operation> deleteGoldengateConnectionAssignmentCallable()

Deletes a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionAssignmentRequest request =
           DeleteGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteGoldengateConnectionAssignmentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateConnectionAssignmentOperationCallable()
    
    
    public final OperationCallable<DeleteGoldengateConnectionAssignmentRequest,Empty,OperationMetadata> deleteGoldengateConnectionAssignmentOperationCallable()

Deletes a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionAssignmentRequest request =
           DeleteGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient
               .deleteGoldengateConnectionAssignmentOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionAssignmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAsync(@Nullable GoldengateConnectionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAsync(@Nullable GoldengateConnectionName name)

Deletes a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateConnectionName name =
           GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]");
       oracleDatabaseClient.deleteGoldengateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateConnectionName`  
Required. The name of the GoldengateConnection in the following format: projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest request)

Deletes a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionRequest request =
           DeleteGoldengateConnectionRequest.newBuilder()
               .setName(
                   GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteGoldengateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateConnectionAsync(String name)

Deletes a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
               .toString();
       oracleDatabaseClient.deleteGoldengateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateConnection in the following format: projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionCallable()
    
    
    public final UnaryCallable<DeleteGoldengateConnectionRequest,Operation> deleteGoldengateConnectionCallable()

Deletes a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionRequest request =
           DeleteGoldengateConnectionRequest.newBuilder()
               .setName(
                   GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteGoldengateConnectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateConnectionOperationCallable()
    
    
    public final OperationCallable<DeleteGoldengateConnectionRequest,Empty,OperationMetadata> deleteGoldengateConnectionOperationCallable()

Deletes a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateConnectionRequest request =
           DeleteGoldengateConnectionRequest.newBuilder()
               .setName(
                   GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteGoldengateConnectionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)

Deletes a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateDeploymentName name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]");
       oracleDatabaseClient.deleteGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateDeploymentName`  
Required. The name of the GoldengateDeployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest request)

Deletes a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateDeploymentRequest request =
           DeleteGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteGoldengateDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateDeploymentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGoldengateDeploymentAsync(String name)

Deletes a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
               .toString();
       oracleDatabaseClient.deleteGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateDeployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateDeploymentCallable()
    
    
    public final UnaryCallable<DeleteGoldengateDeploymentRequest,Operation> deleteGoldengateDeploymentCallable()

Deletes a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateDeploymentRequest request =
           DeleteGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteGoldengateDeploymentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateDeploymentOperationCallable()
    
    
    public final OperationCallable<DeleteGoldengateDeploymentRequest,Empty,OperationMetadata> deleteGoldengateDeploymentOperationCallable()

Deletes a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteGoldengateDeploymentRequest request =
           DeleteGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteGoldengateDeploymentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbNetworkAsync(@Nullable OdbNetworkName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbNetworkAsync(@Nullable OdbNetworkName name)

Deletes a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbNetworkName name = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]");
       oracleDatabaseClient.deleteOdbNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbNetworkName`  
Required. The name of the resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbNetworkAsync(DeleteOdbNetworkRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbNetworkAsync(DeleteOdbNetworkRequest request)

Deletes a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbNetworkRequest request =
           DeleteOdbNetworkRequest.newBuilder()
               .setName(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteOdbNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbNetworkAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbNetworkAsync(String name)

Deletes a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString();
       oracleDatabaseClient.deleteOdbNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbNetworkCallable()
    
    
    public final UnaryCallable<DeleteOdbNetworkRequest,Operation> deleteOdbNetworkCallable()

Deletes a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbNetworkRequest request =
           DeleteOdbNetworkRequest.newBuilder()
               .setName(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteOdbNetworkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOdbNetworkOperationCallable()
    
    
    public final OperationCallable<DeleteOdbNetworkRequest,Empty,OperationMetadata> deleteOdbNetworkOperationCallable()

Deletes a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbNetworkRequest request =
           DeleteOdbNetworkRequest.newBuilder()
               .setName(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteOdbNetworkOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbSubnetAsync(@Nullable OdbSubnetName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbSubnetAsync(@Nullable OdbSubnetName name)

Deletes a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbSubnetName name =
           OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]");
       oracleDatabaseClient.deleteOdbSubnetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbSubnetName`  
Required. The name of the resource in the following format: projects/{project}/locations/{region}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbSubnetAsync(DeleteOdbSubnetRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbSubnetAsync(DeleteOdbSubnetRequest request)

Deletes a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbSubnetRequest request =
           DeleteOdbSubnetRequest.newBuilder()
               .setName(
                   OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       oracleDatabaseClient.deleteOdbSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbSubnetAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOdbSubnetAsync(String name)

Deletes a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]").toString();
       oracleDatabaseClient.deleteOdbSubnetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource in the following format: projects/{project}/locations/{region}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbSubnetCallable()
    
    
    public final UnaryCallable<DeleteOdbSubnetRequest,Operation> deleteOdbSubnetCallable()

Deletes a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbSubnetRequest request =
           DeleteOdbSubnetRequest.newBuilder()
               .setName(
                   OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.deleteOdbSubnetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOdbSubnetOperationCallable()
    
    
    public final OperationCallable<DeleteOdbSubnetRequest,Empty,OperationMetadata> deleteOdbSubnetOperationCallable()

Deletes a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DeleteOdbSubnetRequest request =
           DeleteOdbSubnetRequest.newBuilder()
               .setName(
                   OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           oracleDatabaseClient.deleteOdbSubnetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbSubnetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabaseName peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response =
           oracleDatabaseClient.failoverAutonomousDatabaseAsync(name, peerAutonomousDatabase).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Optional. The peer database name to fail over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, String peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, String peerAutonomousDatabase)

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       String peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response =
           oracleDatabaseClient.failoverAutonomousDatabaseAsync(name, peerAutonomousDatabase).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The peer database name to fail over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest request)

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       FailoverAutonomousDatabaseRequest request =
           FailoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.failoverAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.FailoverAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseAsync(String name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseAsync(String name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabaseName peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response =
           oracleDatabaseClient.failoverAutonomousDatabaseAsync(name, peerAutonomousDatabase).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Optional. The peer database name to fail over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase)

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       String peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response =
           oracleDatabaseClient.failoverAutonomousDatabaseAsync(name, peerAutonomousDatabase).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The peer database name to fail over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<FailoverAutonomousDatabaseRequest,Operation> failoverAutonomousDatabaseCallable()

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       FailoverAutonomousDatabaseRequest request =
           FailoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.failoverAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.FailoverAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### failoverAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<FailoverAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseOperationCallable()

Initiates a failover to target autonomous database from the associated primary database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       FailoverAutonomousDatabaseRequest request =
           FailoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.failoverAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.FailoverAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### generateAutonomousDatabaseWallet(@Nullable AutonomousDatabaseName name, GenerateType type, boolean isRegional, String password)
    
    
    public final GenerateAutonomousDatabaseWalletResponse generateAutonomousDatabaseWallet(@Nullable AutonomousDatabaseName name, GenerateType type, boolean isRegional, String password)

Generates a wallet for an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       GenerateType type = GenerateType.forNumber(0);
       boolean isRegional = true;
       String password = "password1216985755";
       GenerateAutonomousDatabaseWalletResponse response =
           oracleDatabaseClient.generateAutonomousDatabaseWallet(name, type, isRegional, password);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`type` | `[GenerateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateType)`  
Optional. The type of wallet generation for the Autonomous Database. The default value is SINGLE.  
`isRegional` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. True when requesting regional connection strings in PDB connect info, applicable to cross-region Data Guard only.  
`password` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The password used to encrypt the keys inside the wallet. The password must be a minimum of 8 characters.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletResponse)` |   
  
### generateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest request)
    
    
    public final GenerateAutonomousDatabaseWalletResponse generateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest request)

Generates a wallet for an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GenerateAutonomousDatabaseWalletRequest request =
           GenerateAutonomousDatabaseWalletRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setType(GenerateType.forNumber(0))
               .setIsRegional(true)
               .setPassword("password1216985755")
               .build();
       GenerateAutonomousDatabaseWalletResponse response =
           oracleDatabaseClient.generateAutonomousDatabaseWallet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletResponse)` |   
  
### generateAutonomousDatabaseWallet(String name, GenerateType type, boolean isRegional, String password)
    
    
    public final GenerateAutonomousDatabaseWalletResponse generateAutonomousDatabaseWallet(String name, GenerateType type, boolean isRegional, String password)

Generates a wallet for an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       GenerateType type = GenerateType.forNumber(0);
       boolean isRegional = true;
       String password = "password1216985755";
       GenerateAutonomousDatabaseWalletResponse response =
           oracleDatabaseClient.generateAutonomousDatabaseWallet(name, type, isRegional, password);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`type` | `[GenerateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateType)`  
Optional. The type of wallet generation for the Autonomous Database. The default value is SINGLE.  
`isRegional` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. True when requesting regional connection strings in PDB connect info, applicable to cross-region Data Guard only.  
`password` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The password used to encrypt the keys inside the wallet. The password must be a minimum of 8 characters.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletResponse)` |   
  
### generateAutonomousDatabaseWalletCallable()
    
    
    public final UnaryCallable<GenerateAutonomousDatabaseWalletRequest,GenerateAutonomousDatabaseWalletResponse> generateAutonomousDatabaseWalletCallable()

Generates a wallet for an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GenerateAutonomousDatabaseWalletRequest request =
           GenerateAutonomousDatabaseWalletRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setType(GenerateType.forNumber(0))
               .setIsRegional(true)
               .setPassword("password1216985755")
               .build();
       ApiFuture<GenerateAutonomousDatabaseWalletResponse> future =
           oracleDatabaseClient.generateAutonomousDatabaseWalletCallable().futureCall(request);
       // Do something.
       GenerateAutonomousDatabaseWalletResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletRequest),[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletResponse)>` |   
  
### getAutonomousDatabase(@Nullable AutonomousDatabaseName name)
    
    
    public final AutonomousDatabase getAutonomousDatabase(@Nullable AutonomousDatabaseName name)

Gets the details of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response = oracleDatabaseClient.getAutonomousDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)` |   
  
### getAutonomousDatabase(GetAutonomousDatabaseRequest request)
    
    
    public final AutonomousDatabase getAutonomousDatabase(GetAutonomousDatabaseRequest request)

Gets the details of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetAutonomousDatabaseRequest request =
           GetAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response = oracleDatabaseClient.getAutonomousDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)` |   
  
### getAutonomousDatabase(String name)
    
    
    public final AutonomousDatabase getAutonomousDatabase(String name)

Gets the details of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response = oracleDatabaseClient.getAutonomousDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)` |   
  
### getAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<GetAutonomousDatabaseRequest,AutonomousDatabase> getAutonomousDatabaseCallable()

Gets the details of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetAutonomousDatabaseRequest request =
           GetAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<AutonomousDatabase> future =
           oracleDatabaseClient.getAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)>` |   
  
### getAutonomousDatabaseRefreshableClones(@Nullable AutonomousDatabaseName name)
    
    
    public final AutonomousDatabaseRefreshableClones getAutonomousDatabaseRefreshableClones(@Nullable AutonomousDatabaseName name)

Gets the refreshable clones for a given Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabaseRefreshableClones response =
           oracleDatabaseClient.getAutonomousDatabaseRefreshableClones(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The Autonomous Database resource whose refreshable clones are to be listed. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseRefreshableClones)` |   
  
### getAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest request)
    
    
    public final AutonomousDatabaseRefreshableClones getAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest request)

Gets the refreshable clones for a given Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetAutonomousDatabaseRefreshableClonesRequest request =
           GetAutonomousDatabaseRefreshableClonesRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabaseRefreshableClones response =
           oracleDatabaseClient.getAutonomousDatabaseRefreshableClones(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRefreshableClonesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseRefreshableClones)` |   
  
### getAutonomousDatabaseRefreshableClones(String name)
    
    
    public final AutonomousDatabaseRefreshableClones getAutonomousDatabaseRefreshableClones(String name)

Gets the refreshable clones for a given Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabaseRefreshableClones response =
           oracleDatabaseClient.getAutonomousDatabaseRefreshableClones(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Autonomous Database resource whose refreshable clones are to be listed. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseRefreshableClones)` |   
  
### getAutonomousDatabaseRefreshableClonesCallable()
    
    
    public final UnaryCallable<GetAutonomousDatabaseRefreshableClonesRequest,AutonomousDatabaseRefreshableClones> getAutonomousDatabaseRefreshableClonesCallable()

Gets the refreshable clones for a given Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetAutonomousDatabaseRefreshableClonesRequest request =
           GetAutonomousDatabaseRefreshableClonesRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<AutonomousDatabaseRefreshableClones> future =
           oracleDatabaseClient.getAutonomousDatabaseRefreshableClonesCallable().futureCall(request);
       // Do something.
       AutonomousDatabaseRefreshableClones response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRefreshableClonesRequest),[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseRefreshableClones)>` |   
  
### getCloudExadataInfrastructure(@Nullable CloudExadataInfrastructureName name)
    
    
    public final CloudExadataInfrastructure getCloudExadataInfrastructure(@Nullable CloudExadataInfrastructureName name)

Gets details of a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudExadataInfrastructureName name =
           CloudExadataInfrastructureName.of(
               "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]");
       CloudExadataInfrastructure response =
           oracleDatabaseClient.getCloudExadataInfrastructure(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudExadataInfrastructureName`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)` |   
  
### getCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest request)
    
    
    public final CloudExadataInfrastructure getCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest request)

Gets details of a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetCloudExadataInfrastructureRequest request =
           GetCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .build();
       CloudExadataInfrastructure response =
           oracleDatabaseClient.getCloudExadataInfrastructure(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudExadataInfrastructureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)` |   
  
### getCloudExadataInfrastructure(String name)
    
    
    public final CloudExadataInfrastructure getCloudExadataInfrastructure(String name)

Gets details of a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           CloudExadataInfrastructureName.of(
                   "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
               .toString();
       CloudExadataInfrastructure response =
           oracleDatabaseClient.getCloudExadataInfrastructure(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)` |   
  
### getCloudExadataInfrastructureCallable()
    
    
    public final UnaryCallable<GetCloudExadataInfrastructureRequest,CloudExadataInfrastructure> getCloudExadataInfrastructureCallable()

Gets details of a single Exadata Infrastructure.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetCloudExadataInfrastructureRequest request =
           GetCloudExadataInfrastructureRequest.newBuilder()
               .setName(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .build();
       ApiFuture<CloudExadataInfrastructure> future =
           oracleDatabaseClient.getCloudExadataInfrastructureCallable().futureCall(request);
       // Do something.
       CloudExadataInfrastructure response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)>` |   
  
### getCloudVmCluster(@Nullable CloudVmClusterName name)
    
    
    public final CloudVmCluster getCloudVmCluster(@Nullable CloudVmClusterName name)

Gets details of a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudVmClusterName name =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]");
       CloudVmCluster response = oracleDatabaseClient.getCloudVmCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudVmClusterName`  
Required. The name of the Cloud VM Cluster in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)` |   
  
### getCloudVmCluster(GetCloudVmClusterRequest request)
    
    
    public final CloudVmCluster getCloudVmCluster(GetCloudVmClusterRequest request)

Gets details of a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetCloudVmClusterRequest request =
           GetCloudVmClusterRequest.newBuilder()
               .setName(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .build();
       CloudVmCluster response = oracleDatabaseClient.getCloudVmCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)` |   
  
### getCloudVmCluster(String name)
    
    
    public final CloudVmCluster getCloudVmCluster(String name)

Gets details of a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString();
       CloudVmCluster response = oracleDatabaseClient.getCloudVmCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Cloud VM Cluster in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)` |   
  
### getCloudVmClusterCallable()
    
    
    public final UnaryCallable<GetCloudVmClusterRequest,CloudVmCluster> getCloudVmClusterCallable()

Gets details of a single VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetCloudVmClusterRequest request =
           GetCloudVmClusterRequest.newBuilder()
               .setName(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .build();
       ApiFuture<CloudVmCluster> future =
           oracleDatabaseClient.getCloudVmClusterCallable().futureCall(request);
       // Do something.
       CloudVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudVmClusterRequest),[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)>` |   
  
### getDatabase(@Nullable DatabaseName name)
    
    
    public final Database getDatabase(@Nullable DatabaseName name)

Gets details of a single Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[LOCATION]", "[DATABASE]");
       Database response = oracleDatabaseClient.getDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.DatabaseName`  
Required. The name of the Database resource in the following format: projects/{project}/locations/{region}/databases/{database}  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.Database)` |   
  
### getDatabase(GetDatabaseRequest request)
    
    
    public final Database getDatabase(GetDatabaseRequest request)

Gets details of a single Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetDatabaseRequest request =
           GetDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[LOCATION]", "[DATABASE]").toString())
               .build();
       Database response = oracleDatabaseClient.getDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.Database)` |   
  
### getDatabase(String name)
    
    
    public final Database getDatabase(String name)

Gets details of a single Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[LOCATION]", "[DATABASE]").toString();
       Database response = oracleDatabaseClient.getDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Database resource in the following format: projects/{project}/locations/{region}/databases/{database}  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.Database)` |   
  
### getDatabaseCallable()
    
    
    public final UnaryCallable<GetDatabaseRequest,Database> getDatabaseCallable()

Gets details of a single Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetDatabaseRequest request =
           GetDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[LOCATION]", "[DATABASE]").toString())
               .build();
       ApiFuture<Database> future = oracleDatabaseClient.getDatabaseCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.Database)>` |   
  
### getDbSystem(@Nullable DbSystemName name)
    
    
    public final DbSystem getDbSystem(@Nullable DbSystemName name)

Gets details of a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       DbSystemName name = DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]");
       DbSystem response = oracleDatabaseClient.getDbSystem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.DbSystemName`  
Required. The name of the DbSystem in the following format: projects/{project}/locations/{location}/dbSystems/{db_system}.  
**Returns**  
---  
**Type** | **Description**  
`[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)` |   
  
### getDbSystem(GetDbSystemRequest request)
    
    
    public final DbSystem getDbSystem(GetDbSystemRequest request)

Gets details of a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetDbSystemRequest request =
           GetDbSystemRequest.newBuilder()
               .setName(DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString())
               .build();
       DbSystem response = oracleDatabaseClient.getDbSystem(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDbSystemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)` |   
  
### getDbSystem(String name)
    
    
    public final DbSystem getDbSystem(String name)

Gets details of a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name = DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString();
       DbSystem response = oracleDatabaseClient.getDbSystem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DbSystem in the following format: projects/{project}/locations/{location}/dbSystems/{db_system}.  
**Returns**  
---  
**Type** | **Description**  
`[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)` |   
  
### getDbSystemCallable()
    
    
    public final UnaryCallable<GetDbSystemRequest,DbSystem> getDbSystemCallable()

Gets details of a single DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetDbSystemRequest request =
           GetDbSystemRequest.newBuilder()
               .setName(DbSystemName.of("[PROJECT]", "[LOCATION]", "[DB_SYSTEM]").toString())
               .build();
       ApiFuture<DbSystem> future = oracleDatabaseClient.getDbSystemCallable().futureCall(request);
       // Do something.
       DbSystem response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDbSystemRequest),[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)>` |   
  
### getExadbVmCluster(@Nullable ExadbVmClusterName name)
    
    
    public final ExadbVmCluster getExadbVmCluster(@Nullable ExadbVmClusterName name)

Gets details of a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExadbVmClusterName name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]");
       ExadbVmCluster response = oracleDatabaseClient.getExadbVmCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExadbVmClusterName`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)` |   
  
### getExadbVmCluster(GetExadbVmClusterRequest request)
    
    
    public final ExadbVmCluster getExadbVmCluster(GetExadbVmClusterRequest request)

Gets details of a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetExadbVmClusterRequest request =
           GetExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .build();
       ExadbVmCluster response = oracleDatabaseClient.getExadbVmCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExadbVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)` |   
  
### getExadbVmCluster(String name)
    
    
    public final ExadbVmCluster getExadbVmCluster(String name)

Gets details of a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString();
       ExadbVmCluster response = oracleDatabaseClient.getExadbVmCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
**Returns**  
---  
**Type** | **Description**  
`[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)` |   
  
### getExadbVmClusterCallable()
    
    
    public final UnaryCallable<GetExadbVmClusterRequest,ExadbVmCluster> getExadbVmClusterCallable()

Gets details of a single Exadb (Exascale) VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetExadbVmClusterRequest request =
           GetExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .build();
       ApiFuture<ExadbVmCluster> future =
           oracleDatabaseClient.getExadbVmClusterCallable().futureCall(request);
       // Do something.
       ExadbVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)>` |   
  
### getExascaleDbStorageVault(@Nullable ExascaleDbStorageVaultName name)
    
    
    public final ExascaleDbStorageVault getExascaleDbStorageVault(@Nullable ExascaleDbStorageVaultName name)

Gets details of a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExascaleDbStorageVaultName name =
           ExascaleDbStorageVaultName.of("[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]");
       ExascaleDbStorageVault response = oracleDatabaseClient.getExascaleDbStorageVault(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExascaleDbStorageVaultName`  
Required. The name of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.  
**Returns**  
---  
**Type** | **Description**  
`[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)` |   
  
### getExascaleDbStorageVault(GetExascaleDbStorageVaultRequest request)
    
    
    public final ExascaleDbStorageVault getExascaleDbStorageVault(GetExascaleDbStorageVaultRequest request)

Gets details of a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetExascaleDbStorageVaultRequest request =
           GetExascaleDbStorageVaultRequest.newBuilder()
               .setName(
                   ExascaleDbStorageVaultName.of(
                           "[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
                       .toString())
               .build();
       ExascaleDbStorageVault response = oracleDatabaseClient.getExascaleDbStorageVault(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExascaleDbStorageVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)` |   
  
### getExascaleDbStorageVault(String name)
    
    
    public final ExascaleDbStorageVault getExascaleDbStorageVault(String name)

Gets details of a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           ExascaleDbStorageVaultName.of("[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
               .toString();
       ExascaleDbStorageVault response = oracleDatabaseClient.getExascaleDbStorageVault(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.  
**Returns**  
---  
**Type** | **Description**  
`[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)` |   
  
### getExascaleDbStorageVaultCallable()
    
    
    public final UnaryCallable<GetExascaleDbStorageVaultRequest,ExascaleDbStorageVault> getExascaleDbStorageVaultCallable()

Gets details of a single ExascaleDB Storage Vault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetExascaleDbStorageVaultRequest request =
           GetExascaleDbStorageVaultRequest.newBuilder()
               .setName(
                   ExascaleDbStorageVaultName.of(
                           "[PROJECT]", "[LOCATION]", "[EXASCALE_DB_STORAGE_VAULT]")
                       .toString())
               .build();
       ApiFuture<ExascaleDbStorageVault> future =
           oracleDatabaseClient.getExascaleDbStorageVaultCallable().futureCall(request);
       // Do something.
       ExascaleDbStorageVault response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExascaleDbStorageVaultRequest),[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)>` |   
  
### getGoldengateConnection(@Nullable GoldengateConnectionName name)
    
    
    public final GoldengateConnection getGoldengateConnection(@Nullable GoldengateConnectionName name)

Gets details of a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateConnectionName name =
           GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]");
       GoldengateConnection response = oracleDatabaseClient.getGoldengateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateConnectionName`  
Required. The name of the GoldengateConnection in the following format: projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)` |   
  
### getGoldengateConnection(GetGoldengateConnectionRequest request)
    
    
    public final GoldengateConnection getGoldengateConnection(GetGoldengateConnectionRequest request)

Gets details of a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateConnectionRequest request =
           GetGoldengateConnectionRequest.newBuilder()
               .setName(
                   GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
                       .toString())
               .build();
       GoldengateConnection response = oracleDatabaseClient.getGoldengateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)` |   
  
### getGoldengateConnection(String name)
    
    
    public final GoldengateConnection getGoldengateConnection(String name)

Gets details of a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
               .toString();
       GoldengateConnection response = oracleDatabaseClient.getGoldengateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateConnection in the following format: projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)` |   
  
### getGoldengateConnectionAssignment(@Nullable GoldengateConnectionAssignmentName name)
    
    
    public final GoldengateConnectionAssignment getGoldengateConnectionAssignment(@Nullable GoldengateConnectionAssignmentName name)

Gets details of a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateConnectionAssignmentName name =
           GoldengateConnectionAssignmentName.of(
               "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]");
       GoldengateConnectionAssignment response =
           oracleDatabaseClient.getGoldengateConnectionAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignmentName`  
Required. The name of the GoldengateConnectionAssignment to retrieve. Format: projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)` |   
  
### getGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest request)
    
    
    public final GoldengateConnectionAssignment getGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest request)

Gets details of a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateConnectionAssignmentRequest request =
           GetGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .build();
       GoldengateConnectionAssignment response =
           oracleDatabaseClient.getGoldengateConnectionAssignment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)` |   
  
### getGoldengateConnectionAssignment(String name)
    
    
    public final GoldengateConnectionAssignment getGoldengateConnectionAssignment(String name)

Gets details of a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateConnectionAssignmentName.of(
                   "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
               .toString();
       GoldengateConnectionAssignment response =
           oracleDatabaseClient.getGoldengateConnectionAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateConnectionAssignment to retrieve. Format: projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)` |   
  
### getGoldengateConnectionAssignmentCallable()
    
    
    public final UnaryCallable<GetGoldengateConnectionAssignmentRequest,GoldengateConnectionAssignment> getGoldengateConnectionAssignmentCallable()

Gets details of a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateConnectionAssignmentRequest request =
           GetGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .build();
       ApiFuture<GoldengateConnectionAssignment> future =
           oracleDatabaseClient.getGoldengateConnectionAssignmentCallable().futureCall(request);
       // Do something.
       GoldengateConnectionAssignment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionAssignmentRequest),[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)>` |   
  
### getGoldengateConnectionCallable()
    
    
    public final UnaryCallable<GetGoldengateConnectionRequest,GoldengateConnection> getGoldengateConnectionCallable()

Gets details of a single GoldengateConnection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateConnectionRequest request =
           GetGoldengateConnectionRequest.newBuilder()
               .setName(
                   GoldengateConnectionName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION]")
                       .toString())
               .build();
       ApiFuture<GoldengateConnection> future =
           oracleDatabaseClient.getGoldengateConnectionCallable().futureCall(request);
       // Do something.
       GoldengateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionRequest),[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)>` |   
  
### getGoldengateDeployment(@Nullable GoldengateDeploymentName name)
    
    
    public final GoldengateDeployment getGoldengateDeployment(@Nullable GoldengateDeploymentName name)

Gets details of a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateDeploymentName name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]");
       GoldengateDeployment response = oracleDatabaseClient.getGoldengateDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateDeploymentName`  
Required. The name of the GoldengateDeployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)` |   
  
### getGoldengateDeployment(GetGoldengateDeploymentRequest request)
    
    
    public final GoldengateDeployment getGoldengateDeployment(GetGoldengateDeploymentRequest request)

Gets details of a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateDeploymentRequest request =
           GetGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       GoldengateDeployment response = oracleDatabaseClient.getGoldengateDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)` |   
  
### getGoldengateDeployment(String name)
    
    
    public final GoldengateDeployment getGoldengateDeployment(String name)

Gets details of a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
               .toString();
       GoldengateDeployment response = oracleDatabaseClient.getGoldengateDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GoldengateDeployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)` |   
  
### getGoldengateDeploymentCallable()
    
    
    public final UnaryCallable<GetGoldengateDeploymentRequest,GoldengateDeployment> getGoldengateDeploymentCallable()

Gets details of a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetGoldengateDeploymentRequest request =
           GetGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<GoldengateDeployment> future =
           oracleDatabaseClient.getGoldengateDeploymentCallable().futureCall(request);
       // Do something.
       GoldengateDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = oracleDatabaseClient.getLocation(request);
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
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = oracleDatabaseClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOdbNetwork(@Nullable OdbNetworkName name)
    
    
    public final OdbNetwork getOdbNetwork(@Nullable OdbNetworkName name)

Gets details of a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbNetworkName name = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]");
       OdbNetwork response = oracleDatabaseClient.getOdbNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbNetworkName`  
Required. The name of the OdbNetwork in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)` |   
  
### getOdbNetwork(GetOdbNetworkRequest request)
    
    
    public final OdbNetwork getOdbNetwork(GetOdbNetworkRequest request)

Gets details of a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetOdbNetworkRequest request =
           GetOdbNetworkRequest.newBuilder()
               .setName(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .build();
       OdbNetwork response = oracleDatabaseClient.getOdbNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)` |   
  
### getOdbNetwork(String name)
    
    
    public final OdbNetwork getOdbNetwork(String name)

Gets details of a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString();
       OdbNetwork response = oracleDatabaseClient.getOdbNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the OdbNetwork in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)` |   
  
### getOdbNetworkCallable()
    
    
    public final UnaryCallable<GetOdbNetworkRequest,OdbNetwork> getOdbNetworkCallable()

Gets details of a single ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetOdbNetworkRequest request =
           GetOdbNetworkRequest.newBuilder()
               .setName(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .build();
       ApiFuture<OdbNetwork> future =
           oracleDatabaseClient.getOdbNetworkCallable().futureCall(request);
       // Do something.
       OdbNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbNetworkRequest),[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)>` |   
  
### getOdbSubnet(@Nullable OdbSubnetName name)
    
    
    public final OdbSubnet getOdbSubnet(@Nullable OdbSubnetName name)

Gets details of a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbSubnetName name =
           OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]");
       OdbSubnet response = oracleDatabaseClient.getOdbSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbSubnetName`  
Required. The name of the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.  
**Returns**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)` |   
  
### getOdbSubnet(GetOdbSubnetRequest request)
    
    
    public final OdbSubnet getOdbSubnet(GetOdbSubnetRequest request)

Gets details of a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetOdbSubnetRequest request =
           GetOdbSubnetRequest.newBuilder()
               .setName(
                   OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]")
                       .toString())
               .build();
       OdbSubnet response = oracleDatabaseClient.getOdbSubnet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)` |   
  
### getOdbSubnet(String name)
    
    
    public final OdbSubnet getOdbSubnet(String name)

Gets details of a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]").toString();
       OdbSubnet response = oracleDatabaseClient.getOdbSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.  
**Returns**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)` |   
  
### getOdbSubnetCallable()
    
    
    public final UnaryCallable<GetOdbSubnetRequest,OdbSubnet> getOdbSubnetCallable()

Gets details of a single ODB Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetOdbSubnetRequest request =
           GetOdbSubnetRequest.newBuilder()
               .setName(
                   OdbSubnetName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]", "[ODB_SUBNET]")
                       .toString())
               .build();
       ApiFuture<OdbSubnet> future = oracleDatabaseClient.getOdbSubnetCallable().futureCall(request);
       // Do something.
       OdbSubnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbSubnetRequest),[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getPluggableDatabase(@Nullable PluggableDatabaseName name)
    
    
    public final PluggableDatabase getPluggableDatabase(@Nullable PluggableDatabaseName name)

Gets details of a single PluggableDatabase.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       PluggableDatabaseName name =
           PluggableDatabaseName.of("[PROJECT]", "[LOCATION]", "[PLUGGABLE_DATABASE]");
       PluggableDatabase response = oracleDatabaseClient.getPluggableDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.PluggableDatabaseName`  
Required. The name of the PluggableDatabase resource in the following format: projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}  
**Returns**  
---  
**Type** | **Description**  
`[PluggableDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.PluggableDatabase)` |   
  
### getPluggableDatabase(GetPluggableDatabaseRequest request)
    
    
    public final PluggableDatabase getPluggableDatabase(GetPluggableDatabaseRequest request)

Gets details of a single PluggableDatabase.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetPluggableDatabaseRequest request =
           GetPluggableDatabaseRequest.newBuilder()
               .setName(
                   PluggableDatabaseName.of("[PROJECT]", "[LOCATION]", "[PLUGGABLE_DATABASE]")
                       .toString())
               .build();
       PluggableDatabase response = oracleDatabaseClient.getPluggableDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPluggableDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetPluggableDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PluggableDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.PluggableDatabase)` |   
  
### getPluggableDatabase(String name)
    
    
    public final PluggableDatabase getPluggableDatabase(String name)

Gets details of a single PluggableDatabase.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           PluggableDatabaseName.of("[PROJECT]", "[LOCATION]", "[PLUGGABLE_DATABASE]").toString();
       PluggableDatabase response = oracleDatabaseClient.getPluggableDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PluggableDatabase resource in the following format: projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}  
**Returns**  
---  
**Type** | **Description**  
`[PluggableDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.PluggableDatabase)` |   
  
### getPluggableDatabaseCallable()
    
    
    public final UnaryCallable<GetPluggableDatabaseRequest,PluggableDatabase> getPluggableDatabaseCallable()

Gets details of a single PluggableDatabase.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GetPluggableDatabaseRequest request =
           GetPluggableDatabaseRequest.newBuilder()
               .setName(
                   PluggableDatabaseName.of("[PROJECT]", "[LOCATION]", "[PLUGGABLE_DATABASE]")
                       .toString())
               .build();
       ApiFuture<PluggableDatabase> future =
           oracleDatabaseClient.getPluggableDatabaseCallable().futureCall(request);
       // Do something.
       PluggableDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPluggableDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetPluggableDatabaseRequest),[PluggableDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.PluggableDatabase)>` |   
  
### getSettings()
    
    
    public final @Nullable OracleDatabaseSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OracleDatabaseSettings` |   
  
### getStub()
    
    
    public OracleDatabaseStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.stub.OracleDatabaseStub)` |   
  
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
  
### listAutonomousDatabaseBackups(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse listAutonomousDatabaseBackups(@Nullable LocationName parent)

Lists the long-term and automatic backups of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AutonomousDatabaseBackup element :
           oracleDatabaseClient.listAutonomousDatabaseBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for ListAutonomousDatabaseBackups in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse)` |   
  
### listAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest request)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse listAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest request)

Lists the long-term and automatic backups of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseBackupsRequest request =
           ListAutonomousDatabaseBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AutonomousDatabaseBackup element :
           oracleDatabaseClient.listAutonomousDatabaseBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse)` |   
  
### listAutonomousDatabaseBackups(String parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse listAutonomousDatabaseBackups(String parent)

Lists the long-term and automatic backups of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AutonomousDatabaseBackup element :
           oracleDatabaseClient.listAutonomousDatabaseBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for ListAutonomousDatabaseBackups in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse)` |   
  
### listAutonomousDatabaseBackupsCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabaseBackupsRequest,ListAutonomousDatabaseBackupsResponse> listAutonomousDatabaseBackupsCallable()

Lists the long-term and automatic backups of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseBackupsRequest request =
           ListAutonomousDatabaseBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAutonomousDatabaseBackupsResponse response =
             oracleDatabaseClient.listAutonomousDatabaseBackupsCallable().call(request);
         for (AutonomousDatabaseBackup element : response.getAutonomousDatabaseBackupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest),[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsResponse)>` |   
  
### listAutonomousDatabaseBackupsPagedCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabaseBackupsRequest,OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse> listAutonomousDatabaseBackupsPagedCallable()

Lists the long-term and automatic backups of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseBackupsRequest request =
           ListAutonomousDatabaseBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AutonomousDatabaseBackup> future =
           oracleDatabaseClient.listAutonomousDatabaseBackupsPagedCallable().futureCall(request);
       // Do something.
       for (AutonomousDatabaseBackup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest),[ListAutonomousDatabaseBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse)>` |   
  
### listAutonomousDatabaseCharacterSets(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse listAutonomousDatabaseCharacterSets(@Nullable LocationName parent)

Lists Autonomous Database Character Sets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AutonomousDatabaseCharacterSet element :
           oracleDatabaseClient.listAutonomousDatabaseCharacterSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse)` |   
  
### listAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest request)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse listAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest request)

Lists Autonomous Database Character Sets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseCharacterSetsRequest request =
           ListAutonomousDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (AutonomousDatabaseCharacterSet element :
           oracleDatabaseClient.listAutonomousDatabaseCharacterSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse)` |   
  
### listAutonomousDatabaseCharacterSets(String parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse listAutonomousDatabaseCharacterSets(String parent)

Lists Autonomous Database Character Sets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AutonomousDatabaseCharacterSet element :
           oracleDatabaseClient.listAutonomousDatabaseCharacterSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse)` |   
  
### listAutonomousDatabaseCharacterSetsCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabaseCharacterSetsRequest,ListAutonomousDatabaseCharacterSetsResponse> listAutonomousDatabaseCharacterSetsCallable()

Lists Autonomous Database Character Sets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseCharacterSetsRequest request =
           ListAutonomousDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListAutonomousDatabaseCharacterSetsResponse response =
             oracleDatabaseClient.listAutonomousDatabaseCharacterSetsCallable().call(request);
         for (AutonomousDatabaseCharacterSet element :
             response.getAutonomousDatabaseCharacterSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsRequest),[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsResponse)>` |   
  
### listAutonomousDatabaseCharacterSetsPagedCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabaseCharacterSetsRequest,OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse> listAutonomousDatabaseCharacterSetsPagedCallable()

Lists Autonomous Database Character Sets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabaseCharacterSetsRequest request =
           ListAutonomousDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<AutonomousDatabaseCharacterSet> future =
           oracleDatabaseClient
               .listAutonomousDatabaseCharacterSetsPagedCallable()
               .futureCall(request);
       // Do something.
       for (AutonomousDatabaseCharacterSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsRequest),[ListAutonomousDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse)>` |   
  
### listAutonomousDatabases(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabasesPagedResponse listAutonomousDatabases(@Nullable LocationName parent)

Lists the Autonomous Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AutonomousDatabase element :
           oracleDatabaseClient.listAutonomousDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabasesPagedResponse)` |   
  
### listAutonomousDatabases(ListAutonomousDatabasesRequest request)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabasesPagedResponse listAutonomousDatabases(ListAutonomousDatabasesRequest request)

Lists the Autonomous Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabasesRequest request =
           ListAutonomousDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AutonomousDatabase element :
           oracleDatabaseClient.listAutonomousDatabases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabasesPagedResponse)` |   
  
### listAutonomousDatabases(String parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDatabasesPagedResponse listAutonomousDatabases(String parent)

Lists the Autonomous Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AutonomousDatabase element :
           oracleDatabaseClient.listAutonomousDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabasesPagedResponse)` |   
  
### listAutonomousDatabasesCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabasesRequest,ListAutonomousDatabasesResponse> listAutonomousDatabasesCallable()

Lists the Autonomous Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabasesRequest request =
           ListAutonomousDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAutonomousDatabasesResponse response =
             oracleDatabaseClient.listAutonomousDatabasesCallable().call(request);
         for (AutonomousDatabase element : response.getAutonomousDatabasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesRequest),[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesResponse)>` |   
  
### listAutonomousDatabasesPagedCallable()
    
    
    public final UnaryCallable<ListAutonomousDatabasesRequest,OracleDatabaseClient.ListAutonomousDatabasesPagedResponse> listAutonomousDatabasesPagedCallable()

Lists the Autonomous Databases in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDatabasesRequest request =
           ListAutonomousDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AutonomousDatabase> future =
           oracleDatabaseClient.listAutonomousDatabasesPagedCallable().futureCall(request);
       // Do something.
       for (AutonomousDatabase element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesRequest),[ListAutonomousDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabasesPagedResponse)>` |   
  
### listAutonomousDbVersions(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse listAutonomousDbVersions(@Nullable LocationName parent)

Lists all the available Autonomous Database versions for a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AutonomousDbVersion element :
           oracleDatabaseClient.listAutonomousDbVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse)` |   
  
### listAutonomousDbVersions(ListAutonomousDbVersionsRequest request)
    
    
    public final OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse listAutonomousDbVersions(ListAutonomousDbVersionsRequest request)

Lists all the available Autonomous Database versions for a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDbVersionsRequest request =
           ListAutonomousDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AutonomousDbVersion element :
           oracleDatabaseClient.listAutonomousDbVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse)` |   
  
### listAutonomousDbVersions(String parent)
    
    
    public final OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse listAutonomousDbVersions(String parent)

Lists all the available Autonomous Database versions for a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AutonomousDbVersion element :
           oracleDatabaseClient.listAutonomousDbVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse)` |   
  
### listAutonomousDbVersionsCallable()
    
    
    public final UnaryCallable<ListAutonomousDbVersionsRequest,ListAutonomousDbVersionsResponse> listAutonomousDbVersionsCallable()

Lists all the available Autonomous Database versions for a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDbVersionsRequest request =
           ListAutonomousDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAutonomousDbVersionsResponse response =
             oracleDatabaseClient.listAutonomousDbVersionsCallable().call(request);
         for (AutonomousDbVersion element : response.getAutonomousDbVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsRequest),[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsResponse)>` |   
  
### listAutonomousDbVersionsPagedCallable()
    
    
    public final UnaryCallable<ListAutonomousDbVersionsRequest,OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse> listAutonomousDbVersionsPagedCallable()

Lists all the available Autonomous Database versions for a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListAutonomousDbVersionsRequest request =
           ListAutonomousDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AutonomousDbVersion> future =
           oracleDatabaseClient.listAutonomousDbVersionsPagedCallable().futureCall(request);
       // Do something.
       for (AutonomousDbVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsRequest),[ListAutonomousDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse)>` |   
  
### listCloudExadataInfrastructures(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse listCloudExadataInfrastructures(@Nullable LocationName parent)

Lists Exadata Infrastructures in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CloudExadataInfrastructure element :
           oracleDatabaseClient.listCloudExadataInfrastructures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for CloudExadataInfrastructure in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse)` |   
  
### listCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest request)
    
    
    public final OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse listCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest request)

Lists Exadata Infrastructures in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudExadataInfrastructuresRequest request =
           ListCloudExadataInfrastructuresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (CloudExadataInfrastructure element :
           oracleDatabaseClient.listCloudExadataInfrastructures(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse)` |   
  
### listCloudExadataInfrastructures(String parent)
    
    
    public final OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse listCloudExadataInfrastructures(String parent)

Lists Exadata Infrastructures in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CloudExadataInfrastructure element :
           oracleDatabaseClient.listCloudExadataInfrastructures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for CloudExadataInfrastructure in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse)` |   
  
### listCloudExadataInfrastructuresCallable()
    
    
    public final UnaryCallable<ListCloudExadataInfrastructuresRequest,ListCloudExadataInfrastructuresResponse> listCloudExadataInfrastructuresCallable()

Lists Exadata Infrastructures in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudExadataInfrastructuresRequest request =
           ListCloudExadataInfrastructuresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListCloudExadataInfrastructuresResponse response =
             oracleDatabaseClient.listCloudExadataInfrastructuresCallable().call(request);
         for (CloudExadataInfrastructure element : response.getCloudExadataInfrastructuresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresRequest),[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresResponse)>` |   
  
### listCloudExadataInfrastructuresPagedCallable()
    
    
    public final UnaryCallable<ListCloudExadataInfrastructuresRequest,OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse> listCloudExadataInfrastructuresPagedCallable()

Lists Exadata Infrastructures in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudExadataInfrastructuresRequest request =
           ListCloudExadataInfrastructuresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<CloudExadataInfrastructure> future =
           oracleDatabaseClient.listCloudExadataInfrastructuresPagedCallable().futureCall(request);
       // Do something.
       for (CloudExadataInfrastructure element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresRequest),[ListCloudExadataInfrastructuresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse)>` |   
  
### listCloudVmClusters(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListCloudVmClustersPagedResponse listCloudVmClusters(@Nullable LocationName parent)

Lists the VM Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CloudVmCluster element : oracleDatabaseClient.listCloudVmClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudVmClustersPagedResponse)` |   
  
### listCloudVmClusters(ListCloudVmClustersRequest request)
    
    
    public final OracleDatabaseClient.ListCloudVmClustersPagedResponse listCloudVmClusters(ListCloudVmClustersRequest request)

Lists the VM Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudVmClustersRequest request =
           ListCloudVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (CloudVmCluster element :
           oracleDatabaseClient.listCloudVmClusters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCloudVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudVmClustersPagedResponse)` |   
  
### listCloudVmClusters(String parent)
    
    
    public final OracleDatabaseClient.ListCloudVmClustersPagedResponse listCloudVmClusters(String parent)

Lists the VM Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CloudVmCluster element : oracleDatabaseClient.listCloudVmClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListCloudVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudVmClustersPagedResponse)` |   
  
### listCloudVmClustersCallable()
    
    
    public final UnaryCallable<ListCloudVmClustersRequest,ListCloudVmClustersResponse> listCloudVmClustersCallable()

Lists the VM Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudVmClustersRequest request =
           ListCloudVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListCloudVmClustersResponse response =
             oracleDatabaseClient.listCloudVmClustersCallable().call(request);
         for (CloudVmCluster element : response.getCloudVmClustersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersRequest),[ListCloudVmClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersResponse)>` |   
  
### listCloudVmClustersPagedCallable()
    
    
    public final UnaryCallable<ListCloudVmClustersRequest,OracleDatabaseClient.ListCloudVmClustersPagedResponse> listCloudVmClustersPagedCallable()

Lists the VM Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListCloudVmClustersRequest request =
           ListCloudVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<CloudVmCluster> future =
           oracleDatabaseClient.listCloudVmClustersPagedCallable().futureCall(request);
       // Do something.
       for (CloudVmCluster element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersRequest),[ListCloudVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudVmClustersPagedResponse)>` |   
  
### listDatabaseCharacterSets(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse listDatabaseCharacterSets(@Nullable LocationName parent)

List DatabaseCharacterSets for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DatabaseCharacterSet element :
           oracleDatabaseClient.listDatabaseCharacterSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for DatabaseCharacterSets in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse)` |   
  
### listDatabaseCharacterSets(ListDatabaseCharacterSetsRequest request)
    
    
    public final OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse listDatabaseCharacterSets(ListDatabaseCharacterSetsRequest request)

List DatabaseCharacterSets for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabaseCharacterSetsRequest request =
           ListDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DatabaseCharacterSet element :
           oracleDatabaseClient.listDatabaseCharacterSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse)` |   
  
### listDatabaseCharacterSets(String parent)
    
    
    public final OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse listDatabaseCharacterSets(String parent)

List DatabaseCharacterSets for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DatabaseCharacterSet element :
           oracleDatabaseClient.listDatabaseCharacterSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for DatabaseCharacterSets in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse)` |   
  
### listDatabaseCharacterSetsCallable()
    
    
    public final UnaryCallable<ListDatabaseCharacterSetsRequest,ListDatabaseCharacterSetsResponse> listDatabaseCharacterSetsCallable()

List DatabaseCharacterSets for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabaseCharacterSetsRequest request =
           ListDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDatabaseCharacterSetsResponse response =
             oracleDatabaseClient.listDatabaseCharacterSetsCallable().call(request);
         for (DatabaseCharacterSet element : response.getDatabaseCharacterSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsRequest),[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsResponse)>` |   
  
### listDatabaseCharacterSetsPagedCallable()
    
    
    public final UnaryCallable<ListDatabaseCharacterSetsRequest,OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse> listDatabaseCharacterSetsPagedCallable()

List DatabaseCharacterSets for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabaseCharacterSetsRequest request =
           ListDatabaseCharacterSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DatabaseCharacterSet> future =
           oracleDatabaseClient.listDatabaseCharacterSetsPagedCallable().futureCall(request);
       // Do something.
       for (DatabaseCharacterSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsRequest),[ListDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse)>` |   
  
### listDatabases(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDatabasesPagedResponse listDatabases(@Nullable LocationName parent)

Lists all the Databases for the given project, location and DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Database element : oracleDatabaseClient.listDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent resource name in the following format: projects/{project}/locations/{region}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabasesPagedResponse)` |   
  
### listDatabases(ListDatabasesRequest request)
    
    
    public final OracleDatabaseClient.ListDatabasesPagedResponse listDatabases(ListDatabasesRequest request)

Lists all the Databases for the given project, location and DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Database element : oracleDatabaseClient.listDatabases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabasesPagedResponse)` |   
  
### listDatabases(String parent)
    
    
    public final OracleDatabaseClient.ListDatabasesPagedResponse listDatabases(String parent)

Lists all the Databases for the given project, location and DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Database element : oracleDatabaseClient.listDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name in the following format: projects/{project}/locations/{region}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabasesPagedResponse)` |   
  
### listDatabasesCallable()
    
    
    public final UnaryCallable<ListDatabasesRequest,ListDatabasesResponse> listDatabasesCallable()

Lists all the Databases for the given project, location and DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDatabasesResponse response = oracleDatabaseClient.listDatabasesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesRequest),[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesResponse)>` |   
  
### listDatabasesPagedCallable()
    
    
    public final UnaryCallable<ListDatabasesRequest,OracleDatabaseClient.ListDatabasesPagedResponse> listDatabasesPagedCallable()

Lists all the Databases for the given project, location and DbSystem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Database> future =
           oracleDatabaseClient.listDatabasesPagedCallable().futureCall(request);
       // Do something.
       for (Database element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesRequest),[ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabasesPagedResponse)>` |   
  
### listDbNodes(@Nullable CloudVmClusterName parent)
    
    
    public final OracleDatabaseClient.ListDbNodesPagedResponse listDbNodes(@Nullable CloudVmClusterName parent)

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudVmClusterName parent =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]");
       for (DbNode element : oracleDatabaseClient.listDbNodes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudVmClusterName`  
Required. The parent value for database node in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}. .  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)` |   
  
### listDbNodes(@Nullable ExadbVmClusterName parent)
    
    
    public final OracleDatabaseClient.ListDbNodesPagedResponse listDbNodes(@Nullable ExadbVmClusterName parent)

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExadbVmClusterName parent =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]");
       for (DbNode element : oracleDatabaseClient.listDbNodes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExadbVmClusterName`  
Required. The parent value for database node in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}. .  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)` |   
  
### listDbNodes(ListDbNodesRequest request)
    
    
    public final OracleDatabaseClient.ListDbNodesPagedResponse listDbNodes(ListDbNodesRequest request)

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbNodesRequest request =
           ListDbNodesRequest.newBuilder()
               .setParent(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DbNode element : oracleDatabaseClient.listDbNodes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)` |   
  
### listDbNodes(String parent)
    
    
    public final OracleDatabaseClient.ListDbNodesPagedResponse listDbNodes(String parent)

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent =
           CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString();
       for (DbNode element : oracleDatabaseClient.listDbNodes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for database node in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}. .  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)` |   
  
### listDbNodesCallable()
    
    
    public final UnaryCallable<ListDbNodesRequest,ListDbNodesResponse> listDbNodesCallable()

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbNodesRequest request =
           ListDbNodesRequest.newBuilder()
               .setParent(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDbNodesResponse response = oracleDatabaseClient.listDbNodesCallable().call(request);
         for (DbNode element : response.getDbNodesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesRequest),[ListDbNodesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesResponse)>` |   
  
### listDbNodesPagedCallable()
    
    
    public final UnaryCallable<ListDbNodesRequest,OracleDatabaseClient.ListDbNodesPagedResponse> listDbNodesPagedCallable()

Lists the database nodes of a VM Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbNodesRequest request =
           ListDbNodesRequest.newBuilder()
               .setParent(
                   CloudVmClusterName.of("[PROJECT]", "[LOCATION]", "[CLOUD_VM_CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DbNode> future =
           oracleDatabaseClient.listDbNodesPagedCallable().futureCall(request);
       // Do something.
       for (DbNode element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesRequest),[ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)>` |   
  
### listDbServers(@Nullable CloudExadataInfrastructureName parent)
    
    
    public final OracleDatabaseClient.ListDbServersPagedResponse listDbServers(@Nullable CloudExadataInfrastructureName parent)

Lists the database servers of an Exadata Infrastructure instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       CloudExadataInfrastructureName parent =
           CloudExadataInfrastructureName.of(
               "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]");
       for (DbServer element : oracleDatabaseClient.listDbServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.CloudExadataInfrastructureName`  
Required. The parent value for database server in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbServersPagedResponse)` |   
  
### listDbServers(ListDbServersRequest request)
    
    
    public final OracleDatabaseClient.ListDbServersPagedResponse listDbServers(ListDbServersRequest request)

Lists the database servers of an Exadata Infrastructure instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbServersRequest request =
           ListDbServersRequest.newBuilder()
               .setParent(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DbServer element : oracleDatabaseClient.listDbServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbServersPagedResponse)` |   
  
### listDbServers(String parent)
    
    
    public final OracleDatabaseClient.ListDbServersPagedResponse listDbServers(String parent)

Lists the database servers of an Exadata Infrastructure instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent =
           CloudExadataInfrastructureName.of(
                   "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
               .toString();
       for (DbServer element : oracleDatabaseClient.listDbServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for database server in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbServersPagedResponse)` |   
  
### listDbServersCallable()
    
    
    public final UnaryCallable<ListDbServersRequest,ListDbServersResponse> listDbServersCallable()

Lists the database servers of an Exadata Infrastructure instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbServersRequest request =
           ListDbServersRequest.newBuilder()
               .setParent(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDbServersResponse response = oracleDatabaseClient.listDbServersCallable().call(request);
         for (DbServer element : response.getDbServersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersRequest),[ListDbServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersResponse)>` |   
  
### listDbServersPagedCallable()
    
    
    public final UnaryCallable<ListDbServersRequest,OracleDatabaseClient.ListDbServersPagedResponse> listDbServersPagedCallable()

Lists the database servers of an Exadata Infrastructure instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbServersRequest request =
           ListDbServersRequest.newBuilder()
               .setParent(
                   CloudExadataInfrastructureName.of(
                           "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DbServer> future =
           oracleDatabaseClient.listDbServersPagedCallable().futureCall(request);
       // Do something.
       for (DbServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersRequest),[ListDbServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbServersPagedResponse)>` |   
  
### listDbSystemInitialStorageSizes(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse listDbSystemInitialStorageSizes(@Nullable LocationName parent)

Lists all the DbSystemInitialStorageSizes for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DbSystemInitialStorageSize element :
           oracleDatabaseClient.listDbSystemInitialStorageSizes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the DbSystemInitialStorageSize resource with the format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse)` |   
  
### listDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest request)
    
    
    public final OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse listDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest request)

Lists all the DbSystemInitialStorageSizes for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemInitialStorageSizesRequest request =
           ListDbSystemInitialStorageSizesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DbSystemInitialStorageSize element :
           oracleDatabaseClient.listDbSystemInitialStorageSizes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse)` |   
  
### listDbSystemInitialStorageSizes(String parent)
    
    
    public final OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse listDbSystemInitialStorageSizes(String parent)

Lists all the DbSystemInitialStorageSizes for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DbSystemInitialStorageSize element :
           oracleDatabaseClient.listDbSystemInitialStorageSizes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the DbSystemInitialStorageSize resource with the format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse)` |   
  
### listDbSystemInitialStorageSizesCallable()
    
    
    public final UnaryCallable<ListDbSystemInitialStorageSizesRequest,ListDbSystemInitialStorageSizesResponse> listDbSystemInitialStorageSizesCallable()

Lists all the DbSystemInitialStorageSizes for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemInitialStorageSizesRequest request =
           ListDbSystemInitialStorageSizesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDbSystemInitialStorageSizesResponse response =
             oracleDatabaseClient.listDbSystemInitialStorageSizesCallable().call(request);
         for (DbSystemInitialStorageSize element : response.getDbSystemInitialStorageSizesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesRequest),[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesResponse)>` |   
  
### listDbSystemInitialStorageSizesPagedCallable()
    
    
    public final UnaryCallable<ListDbSystemInitialStorageSizesRequest,OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse> listDbSystemInitialStorageSizesPagedCallable()

Lists all the DbSystemInitialStorageSizes for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemInitialStorageSizesRequest request =
           ListDbSystemInitialStorageSizesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DbSystemInitialStorageSize> future =
           oracleDatabaseClient.listDbSystemInitialStorageSizesPagedCallable().futureCall(request);
       // Do something.
       for (DbSystemInitialStorageSize element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesRequest),[ListDbSystemInitialStorageSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse)>` |   
  
### listDbSystemShapes(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDbSystemShapesPagedResponse listDbSystemShapes(@Nullable LocationName parent)

Lists the database system shapes available for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DbSystemShape element : oracleDatabaseClient.listDbSystemShapes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for Database System Shapes in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemShapesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemShapesPagedResponse)` |   
  
### listDbSystemShapes(ListDbSystemShapesRequest request)
    
    
    public final OracleDatabaseClient.ListDbSystemShapesPagedResponse listDbSystemShapes(ListDbSystemShapesRequest request)

Lists the database system shapes available for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemShapesRequest request =
           ListDbSystemShapesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DbSystemShape element : oracleDatabaseClient.listDbSystemShapes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemShapesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemShapesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemShapesPagedResponse)` |   
  
### listDbSystemShapes(String parent)
    
    
    public final OracleDatabaseClient.ListDbSystemShapesPagedResponse listDbSystemShapes(String parent)

Lists the database system shapes available for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DbSystemShape element : oracleDatabaseClient.listDbSystemShapes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for Database System Shapes in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemShapesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemShapesPagedResponse)` |   
  
### listDbSystemShapesCallable()
    
    
    public final UnaryCallable<ListDbSystemShapesRequest,ListDbSystemShapesResponse> listDbSystemShapesCallable()

Lists the database system shapes available for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemShapesRequest request =
           ListDbSystemShapesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDbSystemShapesResponse response =
             oracleDatabaseClient.listDbSystemShapesCallable().call(request);
         for (DbSystemShape element : response.getDbSystemShapesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemShapesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesRequest),[ListDbSystemShapesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesResponse)>` |   
  
### listDbSystemShapesPagedCallable()
    
    
    public final UnaryCallable<ListDbSystemShapesRequest,OracleDatabaseClient.ListDbSystemShapesPagedResponse> listDbSystemShapesPagedCallable()

Lists the database system shapes available for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemShapesRequest request =
           ListDbSystemShapesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DbSystemShape> future =
           oracleDatabaseClient.listDbSystemShapesPagedCallable().futureCall(request);
       // Do something.
       for (DbSystemShape element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemShapesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesRequest),[ListDbSystemShapesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemShapesPagedResponse)>` |   
  
### listDbSystems(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDbSystemsPagedResponse listDbSystems(@Nullable LocationName parent)

Lists all the DbSystems for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DbSystem element : oracleDatabaseClient.listDbSystems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for DbSystems in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemsPagedResponse)` |   
  
### listDbSystems(ListDbSystemsRequest request)
    
    
    public final OracleDatabaseClient.ListDbSystemsPagedResponse listDbSystems(ListDbSystemsRequest request)

Lists all the DbSystems for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemsRequest request =
           ListDbSystemsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DbSystem element : oracleDatabaseClient.listDbSystems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemsPagedResponse)` |   
  
### listDbSystems(String parent)
    
    
    public final OracleDatabaseClient.ListDbSystemsPagedResponse listDbSystems(String parent)

Lists all the DbSystems for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DbSystem element : oracleDatabaseClient.listDbSystems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for DbSystems in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemsPagedResponse)` |   
  
### listDbSystemsCallable()
    
    
    public final UnaryCallable<ListDbSystemsRequest,ListDbSystemsResponse> listDbSystemsCallable()

Lists all the DbSystems for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemsRequest request =
           ListDbSystemsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDbSystemsResponse response = oracleDatabaseClient.listDbSystemsCallable().call(request);
         for (DbSystem element : response.getDbSystemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsRequest),[ListDbSystemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsResponse)>` |   
  
### listDbSystemsPagedCallable()
    
    
    public final UnaryCallable<ListDbSystemsRequest,OracleDatabaseClient.ListDbSystemsPagedResponse> listDbSystemsPagedCallable()

Lists all the DbSystems for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbSystemsRequest request =
           ListDbSystemsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DbSystem> future =
           oracleDatabaseClient.listDbSystemsPagedCallable().futureCall(request);
       // Do something.
       for (DbSystem element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbSystemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsRequest),[ListDbSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemsPagedResponse)>` |   
  
### listDbVersions(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListDbVersionsPagedResponse listDbVersions(@Nullable LocationName parent)

List DbVersions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DbVersion element : oracleDatabaseClient.listDbVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the DbVersion resource with the format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbVersionsPagedResponse)` |   
  
### listDbVersions(ListDbVersionsRequest request)
    
    
    public final OracleDatabaseClient.ListDbVersionsPagedResponse listDbVersions(ListDbVersionsRequest request)

List DbVersions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbVersionsRequest request =
           ListDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DbVersion element : oracleDatabaseClient.listDbVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbVersionsPagedResponse)` |   
  
### listDbVersions(String parent)
    
    
    public final OracleDatabaseClient.ListDbVersionsPagedResponse listDbVersions(String parent)

List DbVersions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DbVersion element : oracleDatabaseClient.listDbVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the DbVersion resource with the format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbVersionsPagedResponse)` |   
  
### listDbVersionsCallable()
    
    
    public final UnaryCallable<ListDbVersionsRequest,ListDbVersionsResponse> listDbVersionsCallable()

List DbVersions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbVersionsRequest request =
           ListDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDbVersionsResponse response =
             oracleDatabaseClient.listDbVersionsCallable().call(request);
         for (DbVersion element : response.getDbVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsRequest),[ListDbVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsResponse)>` |   
  
### listDbVersionsPagedCallable()
    
    
    public final UnaryCallable<ListDbVersionsRequest,OracleDatabaseClient.ListDbVersionsPagedResponse> listDbVersionsPagedCallable()

List DbVersions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListDbVersionsRequest request =
           ListDbVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DbVersion> future =
           oracleDatabaseClient.listDbVersionsPagedCallable().futureCall(request);
       // Do something.
       for (DbVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsRequest),[ListDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbVersionsPagedResponse)>` |   
  
### listEntitlements(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListEntitlementsPagedResponse listEntitlements(@Nullable LocationName parent)

Lists the entitlements in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Entitlement element : oracleDatabaseClient.listEntitlements(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the entitlement in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListEntitlementsPagedResponse)` |   
  
### listEntitlements(ListEntitlementsRequest request)
    
    
    public final OracleDatabaseClient.ListEntitlementsPagedResponse listEntitlements(ListEntitlementsRequest request)

Lists the entitlements in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Entitlement element : oracleDatabaseClient.listEntitlements(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListEntitlementsPagedResponse)` |   
  
### listEntitlements(String parent)
    
    
    public final OracleDatabaseClient.ListEntitlementsPagedResponse listEntitlements(String parent)

Lists the entitlements in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Entitlement element : oracleDatabaseClient.listEntitlements(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the entitlement in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListEntitlementsPagedResponse)` |   
  
### listEntitlementsCallable()
    
    
    public final UnaryCallable<ListEntitlementsRequest,ListEntitlementsResponse> listEntitlementsCallable()

Lists the entitlements in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEntitlementsResponse response =
             oracleDatabaseClient.listEntitlementsCallable().call(request);
         for (Entitlement element : response.getEntitlementsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsRequest),[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsResponse)>` |   
  
### listEntitlementsPagedCallable()
    
    
    public final UnaryCallable<ListEntitlementsRequest,OracleDatabaseClient.ListEntitlementsPagedResponse> listEntitlementsPagedCallable()

Lists the entitlements in a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Entitlement> future =
           oracleDatabaseClient.listEntitlementsPagedCallable().futureCall(request);
       // Do something.
       for (Entitlement element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsRequest),[ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListEntitlementsPagedResponse)>` |   
  
### listExadbVmClusters(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListExadbVmClustersPagedResponse listExadbVmClusters(@Nullable LocationName parent)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ExadbVmCluster element : oracleDatabaseClient.listExadbVmClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for ExadbVmClusters in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExadbVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExadbVmClustersPagedResponse)` |   
  
### listExadbVmClusters(ListExadbVmClustersRequest request)
    
    
    public final OracleDatabaseClient.ListExadbVmClustersPagedResponse listExadbVmClusters(ListExadbVmClustersRequest request)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExadbVmClustersRequest request =
           ListExadbVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ExadbVmCluster element :
           oracleDatabaseClient.listExadbVmClusters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExadbVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExadbVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExadbVmClustersPagedResponse)` |   
  
### listExadbVmClusters(String parent)
    
    
    public final OracleDatabaseClient.ListExadbVmClustersPagedResponse listExadbVmClusters(String parent)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ExadbVmCluster element : oracleDatabaseClient.listExadbVmClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for ExadbVmClusters in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExadbVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExadbVmClustersPagedResponse)` |   
  
### listExadbVmClustersCallable()
    
    
    public final UnaryCallable<ListExadbVmClustersRequest,ListExadbVmClustersResponse> listExadbVmClustersCallable()

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExadbVmClustersRequest request =
           ListExadbVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExadbVmClustersResponse response =
             oracleDatabaseClient.listExadbVmClustersCallable().call(request);
         for (ExadbVmCluster element : response.getExadbVmClustersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExadbVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersRequest),[ListExadbVmClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersResponse)>` |   
  
### listExadbVmClustersPagedCallable()
    
    
    public final UnaryCallable<ListExadbVmClustersRequest,OracleDatabaseClient.ListExadbVmClustersPagedResponse> listExadbVmClustersPagedCallable()

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExadbVmClustersRequest request =
           ListExadbVmClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ExadbVmCluster> future =
           oracleDatabaseClient.listExadbVmClustersPagedCallable().futureCall(request);
       // Do something.
       for (ExadbVmCluster element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExadbVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersRequest),[ListExadbVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExadbVmClustersPagedResponse)>` |   
  
### listExascaleDbStorageVaults(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse listExascaleDbStorageVaults(@Nullable LocationName parent)

Lists all the ExascaleDB Storage Vaults for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ExascaleDbStorageVault element :
           oracleDatabaseClient.listExascaleDbStorageVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse)` |   
  
### listExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest request)
    
    
    public final OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse listExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest request)

Lists all the ExascaleDB Storage Vaults for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExascaleDbStorageVaultsRequest request =
           ListExascaleDbStorageVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ExascaleDbStorageVault element :
           oracleDatabaseClient.listExascaleDbStorageVaults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse)` |   
  
### listExascaleDbStorageVaults(String parent)
    
    
    public final OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse listExascaleDbStorageVaults(String parent)

Lists all the ExascaleDB Storage Vaults for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ExascaleDbStorageVault element :
           oracleDatabaseClient.listExascaleDbStorageVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse)` |   
  
### listExascaleDbStorageVaultsCallable()
    
    
    public final UnaryCallable<ListExascaleDbStorageVaultsRequest,ListExascaleDbStorageVaultsResponse> listExascaleDbStorageVaultsCallable()

Lists all the ExascaleDB Storage Vaults for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExascaleDbStorageVaultsRequest request =
           ListExascaleDbStorageVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExascaleDbStorageVaultsResponse response =
             oracleDatabaseClient.listExascaleDbStorageVaultsCallable().call(request);
         for (ExascaleDbStorageVault element : response.getExascaleDbStorageVaultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsRequest),[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsResponse)>` |   
  
### listExascaleDbStorageVaultsPagedCallable()
    
    
    public final UnaryCallable<ListExascaleDbStorageVaultsRequest,OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse> listExascaleDbStorageVaultsPagedCallable()

Lists all the ExascaleDB Storage Vaults for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListExascaleDbStorageVaultsRequest request =
           ListExascaleDbStorageVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ExascaleDbStorageVault> future =
           oracleDatabaseClient.listExascaleDbStorageVaultsPagedCallable().futureCall(request);
       // Do something.
       for (ExascaleDbStorageVault element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsRequest),[ListExascaleDbStorageVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse)>` |   
  
### listGiVersions(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGiVersionsPagedResponse listGiVersions(@Nullable LocationName parent)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GiVersion element : oracleDatabaseClient.listGiVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for Grid Infrastructure Version in the following format: Format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGiVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGiVersionsPagedResponse)` |   
  
### listGiVersions(ListGiVersionsRequest request)
    
    
    public final OracleDatabaseClient.ListGiVersionsPagedResponse listGiVersions(ListGiVersionsRequest request)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGiVersionsRequest request =
           ListGiVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (GiVersion element : oracleDatabaseClient.listGiVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGiVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGiVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGiVersionsPagedResponse)` |   
  
### listGiVersions(String parent)
    
    
    public final OracleDatabaseClient.ListGiVersionsPagedResponse listGiVersions(String parent)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GiVersion element : oracleDatabaseClient.listGiVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for Grid Infrastructure Version in the following format: Format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGiVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGiVersionsPagedResponse)` |   
  
### listGiVersionsCallable()
    
    
    public final UnaryCallable<ListGiVersionsRequest,ListGiVersionsResponse> listGiVersionsCallable()

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGiVersionsRequest request =
           ListGiVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListGiVersionsResponse response =
             oracleDatabaseClient.listGiVersionsCallable().call(request);
         for (GiVersion element : response.getGiVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGiVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsRequest),[ListGiVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsResponse)>` |   
  
### listGiVersionsPagedCallable()
    
    
    public final UnaryCallable<ListGiVersionsRequest,OracleDatabaseClient.ListGiVersionsPagedResponse> listGiVersionsPagedCallable()

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGiVersionsRequest request =
           ListGiVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<GiVersion> future =
           oracleDatabaseClient.listGiVersionsPagedCallable().futureCall(request);
       // Do something.
       for (GiVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGiVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsRequest),[ListGiVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGiVersionsPagedResponse)>` |   
  
### listGoldengateConnectionAssignments(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse listGoldengateConnectionAssignments(@Nullable LocationName parent)

Lists GoldengateConnectionAssignments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateConnectionAssignment element :
           oracleDatabaseClient.listGoldengateConnectionAssignments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the GoldengateConnectionAssignments. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse)` |   
  
### listGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse listGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest request)

Lists GoldengateConnectionAssignments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionAssignmentsRequest request =
           ListGoldengateConnectionAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GoldengateConnectionAssignment element :
           oracleDatabaseClient.listGoldengateConnectionAssignments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse)` |   
  
### listGoldengateConnectionAssignments(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse listGoldengateConnectionAssignments(String parent)

Lists GoldengateConnectionAssignments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateConnectionAssignment element :
           oracleDatabaseClient.listGoldengateConnectionAssignments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the GoldengateConnectionAssignments. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse)` |   
  
### listGoldengateConnectionAssignmentsCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionAssignmentsRequest,ListGoldengateConnectionAssignmentsResponse> listGoldengateConnectionAssignmentsCallable()

Lists GoldengateConnectionAssignments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionAssignmentsRequest request =
           ListGoldengateConnectionAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGoldengateConnectionAssignmentsResponse response =
             oracleDatabaseClient.listGoldengateConnectionAssignmentsCallable().call(request);
         for (GoldengateConnectionAssignment element :
             response.getGoldengateConnectionAssignmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsRequest),[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsResponse)>` |   
  
### listGoldengateConnectionAssignmentsPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionAssignmentsRequest,OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse> listGoldengateConnectionAssignmentsPagedCallable()

Lists GoldengateConnectionAssignments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionAssignmentsRequest request =
           ListGoldengateConnectionAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GoldengateConnectionAssignment> future =
           oracleDatabaseClient
               .listGoldengateConnectionAssignmentsPagedCallable()
               .futureCall(request);
       // Do something.
       for (GoldengateConnectionAssignment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsRequest),[ListGoldengateConnectionAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse)>` |   
  
### listGoldengateConnectionTypes(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse listGoldengateConnectionTypes(@Nullable LocationName parent)

Lists GoldengateConnectionTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateConnectionType element :
           oracleDatabaseClient.listGoldengateConnectionTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. Parent value for ListGoldengateConnectionTypesRequest Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse)` |   
  
### listGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse listGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest request)

Lists GoldengateConnectionTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionTypesRequest request =
           ListGoldengateConnectionTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (GoldengateConnectionType element :
           oracleDatabaseClient.listGoldengateConnectionTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse)` |   
  
### listGoldengateConnectionTypes(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse listGoldengateConnectionTypes(String parent)

Lists GoldengateConnectionTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateConnectionType element :
           oracleDatabaseClient.listGoldengateConnectionTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListGoldengateConnectionTypesRequest Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse)` |   
  
### listGoldengateConnectionTypesCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionTypesRequest,ListGoldengateConnectionTypesResponse> listGoldengateConnectionTypesCallable()

Lists GoldengateConnectionTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionTypesRequest request =
           ListGoldengateConnectionTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListGoldengateConnectionTypesResponse response =
             oracleDatabaseClient.listGoldengateConnectionTypesCallable().call(request);
         for (GoldengateConnectionType element : response.getGoldengateConnectionTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesRequest),[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesResponse)>` |   
  
### listGoldengateConnectionTypesPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionTypesRequest,OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse> listGoldengateConnectionTypesPagedCallable()

Lists GoldengateConnectionTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionTypesRequest request =
           ListGoldengateConnectionTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<GoldengateConnectionType> future =
           oracleDatabaseClient.listGoldengateConnectionTypesPagedCallable().futureCall(request);
       // Do something.
       for (GoldengateConnectionType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesRequest),[ListGoldengateConnectionTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse)>` |   
  
### listGoldengateConnections(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionsPagedResponse listGoldengateConnections(@Nullable LocationName parent)

Lists all the GoldengateConnections for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateConnection element :
           oracleDatabaseClient.listGoldengateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for GoldengateConnections in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionsPagedResponse)` |   
  
### listGoldengateConnections(ListGoldengateConnectionsRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionsPagedResponse listGoldengateConnections(ListGoldengateConnectionsRequest request)

Lists all the GoldengateConnections for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionsRequest request =
           ListGoldengateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GoldengateConnection element :
           oracleDatabaseClient.listGoldengateConnections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionsPagedResponse)` |   
  
### listGoldengateConnections(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateConnectionsPagedResponse listGoldengateConnections(String parent)

Lists all the GoldengateConnections for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateConnection element :
           oracleDatabaseClient.listGoldengateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for GoldengateConnections in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionsPagedResponse)` |   
  
### listGoldengateConnectionsCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionsRequest,ListGoldengateConnectionsResponse> listGoldengateConnectionsCallable()

Lists all the GoldengateConnections for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionsRequest request =
           ListGoldengateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGoldengateConnectionsResponse response =
             oracleDatabaseClient.listGoldengateConnectionsCallable().call(request);
         for (GoldengateConnection element : response.getGoldengateConnectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsRequest),[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsResponse)>` |   
  
### listGoldengateConnectionsPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateConnectionsRequest,OracleDatabaseClient.ListGoldengateConnectionsPagedResponse> listGoldengateConnectionsPagedCallable()

Lists all the GoldengateConnections for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateConnectionsRequest request =
           ListGoldengateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GoldengateConnection> future =
           oracleDatabaseClient.listGoldengateConnectionsPagedCallable().futureCall(request);
       // Do something.
       for (GoldengateConnection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsRequest),[ListGoldengateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionsPagedResponse)>` |   
  
### listGoldengateDeploymentEnvironments(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse listGoldengateDeploymentEnvironments(@Nullable LocationName parent)

Lists GoldengateDeploymentEnvironments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateDeploymentEnvironment element :
           oracleDatabaseClient.listGoldengateDeploymentEnvironments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent, which owns this collection of GoldengateDeploymentEnvironments. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse)` |   
  
### listGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse listGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest request)

Lists GoldengateDeploymentEnvironments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentEnvironmentsRequest request =
           ListGoldengateDeploymentEnvironmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (GoldengateDeploymentEnvironment element :
           oracleDatabaseClient.listGoldengateDeploymentEnvironments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse)` |   
  
### listGoldengateDeploymentEnvironments(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse listGoldengateDeploymentEnvironments(String parent)

Lists GoldengateDeploymentEnvironments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateDeploymentEnvironment element :
           oracleDatabaseClient.listGoldengateDeploymentEnvironments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of GoldengateDeploymentEnvironments. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse)` |   
  
### listGoldengateDeploymentEnvironmentsCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentEnvironmentsRequest,ListGoldengateDeploymentEnvironmentsResponse> listGoldengateDeploymentEnvironmentsCallable()

Lists GoldengateDeploymentEnvironments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentEnvironmentsRequest request =
           ListGoldengateDeploymentEnvironmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGoldengateDeploymentEnvironmentsResponse response =
             oracleDatabaseClient.listGoldengateDeploymentEnvironmentsCallable().call(request);
         for (GoldengateDeploymentEnvironment element :
             response.getGoldengateDeploymentEnvironmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsRequest),[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsResponse)>` |   
  
### listGoldengateDeploymentEnvironmentsPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentEnvironmentsRequest,OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse> listGoldengateDeploymentEnvironmentsPagedCallable()

Lists GoldengateDeploymentEnvironments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentEnvironmentsRequest request =
           ListGoldengateDeploymentEnvironmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<GoldengateDeploymentEnvironment> future =
           oracleDatabaseClient
               .listGoldengateDeploymentEnvironmentsPagedCallable()
               .futureCall(request);
       // Do something.
       for (GoldengateDeploymentEnvironment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsRequest),[ListGoldengateDeploymentEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse)>` |   
  
### listGoldengateDeploymentTypes(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse listGoldengateDeploymentTypes(@Nullable LocationName parent)

Lists GoldenGateDeploymentTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateDeploymentType element :
           oracleDatabaseClient.listGoldengateDeploymentTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent resource. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse)` |   
  
### listGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse listGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest request)

Lists GoldenGateDeploymentTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentTypesRequest request =
           ListGoldengateDeploymentTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GoldengateDeploymentType element :
           oracleDatabaseClient.listGoldengateDeploymentTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse)` |   
  
### listGoldengateDeploymentTypes(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse listGoldengateDeploymentTypes(String parent)

Lists GoldenGateDeploymentTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateDeploymentType element :
           oracleDatabaseClient.listGoldengateDeploymentTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse)` |   
  
### listGoldengateDeploymentTypesCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentTypesRequest,ListGoldengateDeploymentTypesResponse> listGoldengateDeploymentTypesCallable()

Lists GoldenGateDeploymentTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentTypesRequest request =
           ListGoldengateDeploymentTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGoldengateDeploymentTypesResponse response =
             oracleDatabaseClient.listGoldengateDeploymentTypesCallable().call(request);
         for (GoldengateDeploymentType element : response.getGoldengateDeploymentTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesRequest),[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesResponse)>` |   
  
### listGoldengateDeploymentTypesPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentTypesRequest,OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse> listGoldengateDeploymentTypesPagedCallable()

Lists GoldenGateDeploymentTypes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentTypesRequest request =
           ListGoldengateDeploymentTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GoldengateDeploymentType> future =
           oracleDatabaseClient.listGoldengateDeploymentTypesPagedCallable().futureCall(request);
       // Do something.
       for (GoldengateDeploymentType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesRequest),[ListGoldengateDeploymentTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse)>` |   
  
### listGoldengateDeploymentVersions(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse listGoldengateDeploymentVersions(@Nullable LocationName parent)

Lists GoldengateDeploymentVersions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateDeploymentVersion element :
           oracleDatabaseClient.listGoldengateDeploymentVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. Parent value for ListGoldengateDeploymentVersionsRequest Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse)` |   
  
### listGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse listGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest request)

Lists GoldengateDeploymentVersions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentVersionsRequest request =
           ListGoldengateDeploymentVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (GoldengateDeploymentVersion element :
           oracleDatabaseClient.listGoldengateDeploymentVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse)` |   
  
### listGoldengateDeploymentVersions(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse listGoldengateDeploymentVersions(String parent)

Lists GoldengateDeploymentVersions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateDeploymentVersion element :
           oracleDatabaseClient.listGoldengateDeploymentVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListGoldengateDeploymentVersionsRequest Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse)` |   
  
### listGoldengateDeploymentVersionsCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentVersionsRequest,ListGoldengateDeploymentVersionsResponse> listGoldengateDeploymentVersionsCallable()

Lists GoldengateDeploymentVersions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentVersionsRequest request =
           ListGoldengateDeploymentVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListGoldengateDeploymentVersionsResponse response =
             oracleDatabaseClient.listGoldengateDeploymentVersionsCallable().call(request);
         for (GoldengateDeploymentVersion element : response.getGoldengateDeploymentVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsRequest),[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsResponse)>` |   
  
### listGoldengateDeploymentVersionsPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentVersionsRequest,OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse> listGoldengateDeploymentVersionsPagedCallable()

Lists GoldengateDeploymentVersions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentVersionsRequest request =
           ListGoldengateDeploymentVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<GoldengateDeploymentVersion> future =
           oracleDatabaseClient.listGoldengateDeploymentVersionsPagedCallable().futureCall(request);
       // Do something.
       for (GoldengateDeploymentVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsRequest),[ListGoldengateDeploymentVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse)>` |   
  
### listGoldengateDeployments(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse listGoldengateDeployments(@Nullable LocationName parent)

Lists all the GoldengateDeployments for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GoldengateDeployment element :
           oracleDatabaseClient.listGoldengateDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for GoldengateDeployments in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse)` |   
  
### listGoldengateDeployments(ListGoldengateDeploymentsRequest request)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse listGoldengateDeployments(ListGoldengateDeploymentsRequest request)

Lists all the GoldengateDeployments for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentsRequest request =
           ListGoldengateDeploymentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GoldengateDeployment element :
           oracleDatabaseClient.listGoldengateDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse)` |   
  
### listGoldengateDeployments(String parent)
    
    
    public final OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse listGoldengateDeployments(String parent)

Lists all the GoldengateDeployments for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GoldengateDeployment element :
           oracleDatabaseClient.listGoldengateDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for GoldengateDeployments in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse)` |   
  
### listGoldengateDeploymentsCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentsRequest,ListGoldengateDeploymentsResponse> listGoldengateDeploymentsCallable()

Lists all the GoldengateDeployments for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentsRequest request =
           ListGoldengateDeploymentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGoldengateDeploymentsResponse response =
             oracleDatabaseClient.listGoldengateDeploymentsCallable().call(request);
         for (GoldengateDeployment element : response.getGoldengateDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsRequest),[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsResponse)>` |   
  
### listGoldengateDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListGoldengateDeploymentsRequest,OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse> listGoldengateDeploymentsPagedCallable()

Lists all the GoldengateDeployments for the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListGoldengateDeploymentsRequest request =
           ListGoldengateDeploymentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GoldengateDeployment> future =
           oracleDatabaseClient.listGoldengateDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (GoldengateDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsRequest),[ListGoldengateDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final OracleDatabaseClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : oracleDatabaseClient.listLocations(request).iterateAll()) {
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
`[OracleDatabaseClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = oracleDatabaseClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,OracleDatabaseClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           oracleDatabaseClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListLocationsPagedResponse)>` |   
  
### listMinorVersions(@Nullable GiVersionName parent)
    
    
    public final OracleDatabaseClient.ListMinorVersionsPagedResponse listMinorVersions(@Nullable GiVersionName parent)

Lists all the valid minor versions for the given project, location, gi version and shape family.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GiVersionName parent = GiVersionName.of("[PROJECT]", "[LOCATION]", "[GI_VERSION]");
       for (MinorVersion element : oracleDatabaseClient.listMinorVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GiVersionName`  
Required. The parent value for the MinorVersion resource with the format: projects/{project}/locations/{location}/giVersions/{gi_version}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListMinorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListMinorVersionsPagedResponse)` |   
  
### listMinorVersions(ListMinorVersionsRequest request)
    
    
    public final OracleDatabaseClient.ListMinorVersionsPagedResponse listMinorVersions(ListMinorVersionsRequest request)

Lists all the valid minor versions for the given project, location, gi version and shape family.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListMinorVersionsRequest request =
           ListMinorVersionsRequest.newBuilder()
               .setParent(GiVersionName.of("[PROJECT]", "[LOCATION]", "[GI_VERSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (MinorVersion element : oracleDatabaseClient.listMinorVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMinorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListMinorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListMinorVersionsPagedResponse)` |   
  
### listMinorVersions(String parent)
    
    
    public final OracleDatabaseClient.ListMinorVersionsPagedResponse listMinorVersions(String parent)

Lists all the valid minor versions for the given project, location, gi version and shape family.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = GiVersionName.of("[PROJECT]", "[LOCATION]", "[GI_VERSION]").toString();
       for (MinorVersion element : oracleDatabaseClient.listMinorVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the MinorVersion resource with the format: projects/{project}/locations/{location}/giVersions/{gi_version}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListMinorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListMinorVersionsPagedResponse)` |   
  
### listMinorVersionsCallable()
    
    
    public final UnaryCallable<ListMinorVersionsRequest,ListMinorVersionsResponse> listMinorVersionsCallable()

Lists all the valid minor versions for the given project, location, gi version and shape family.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListMinorVersionsRequest request =
           ListMinorVersionsRequest.newBuilder()
               .setParent(GiVersionName.of("[PROJECT]", "[LOCATION]", "[GI_VERSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListMinorVersionsResponse response =
             oracleDatabaseClient.listMinorVersionsCallable().call(request);
         for (MinorVersion element : response.getMinorVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMinorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsRequest),[ListMinorVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsResponse)>` |   
  
### listMinorVersionsPagedCallable()
    
    
    public final UnaryCallable<ListMinorVersionsRequest,OracleDatabaseClient.ListMinorVersionsPagedResponse> listMinorVersionsPagedCallable()

Lists all the valid minor versions for the given project, location, gi version and shape family.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListMinorVersionsRequest request =
           ListMinorVersionsRequest.newBuilder()
               .setParent(GiVersionName.of("[PROJECT]", "[LOCATION]", "[GI_VERSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<MinorVersion> future =
           oracleDatabaseClient.listMinorVersionsPagedCallable().futureCall(request);
       // Do something.
       for (MinorVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMinorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsRequest),[ListMinorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListMinorVersionsPagedResponse)>` |   
  
### listOdbNetworks(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListOdbNetworksPagedResponse listOdbNetworks(@Nullable LocationName parent)

Lists the ODB Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (OdbNetwork element : oracleDatabaseClient.listOdbNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent value for the ODB Network in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbNetworksPagedResponse)` |   
  
### listOdbNetworks(ListOdbNetworksRequest request)
    
    
    public final OracleDatabaseClient.ListOdbNetworksPagedResponse listOdbNetworks(ListOdbNetworksRequest request)

Lists the ODB Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbNetworksRequest request =
           ListOdbNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (OdbNetwork element : oracleDatabaseClient.listOdbNetworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOdbNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbNetworksPagedResponse)` |   
  
### listOdbNetworks(String parent)
    
    
    public final OracleDatabaseClient.ListOdbNetworksPagedResponse listOdbNetworks(String parent)

Lists the ODB Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (OdbNetwork element : oracleDatabaseClient.listOdbNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the ODB Network in the following format: projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbNetworksPagedResponse)` |   
  
### listOdbNetworksCallable()
    
    
    public final UnaryCallable<ListOdbNetworksRequest,ListOdbNetworksResponse> listOdbNetworksCallable()

Lists the ODB Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbNetworksRequest request =
           ListOdbNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListOdbNetworksResponse response =
             oracleDatabaseClient.listOdbNetworksCallable().call(request);
         for (OdbNetwork element : response.getOdbNetworksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOdbNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksRequest),[ListOdbNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksResponse)>` |   
  
### listOdbNetworksPagedCallable()
    
    
    public final UnaryCallable<ListOdbNetworksRequest,OracleDatabaseClient.ListOdbNetworksPagedResponse> listOdbNetworksPagedCallable()

Lists the ODB Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbNetworksRequest request =
           ListOdbNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<OdbNetwork> future =
           oracleDatabaseClient.listOdbNetworksPagedCallable().futureCall(request);
       // Do something.
       for (OdbNetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOdbNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksRequest),[ListOdbNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbNetworksPagedResponse)>` |   
  
### listOdbSubnets(@Nullable OdbNetworkName parent)
    
    
    public final OracleDatabaseClient.ListOdbSubnetsPagedResponse listOdbSubnets(@Nullable OdbNetworkName parent)

Lists all the ODB Subnets in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       OdbNetworkName parent = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]");
       for (OdbSubnet element : oracleDatabaseClient.listOdbSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.OdbNetworkName`  
Required. The parent value for the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbSubnetsPagedResponse)` |   
  
### listOdbSubnets(ListOdbSubnetsRequest request)
    
    
    public final OracleDatabaseClient.ListOdbSubnetsPagedResponse listOdbSubnets(ListOdbSubnetsRequest request)

Lists all the ODB Subnets in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbSubnetsRequest request =
           ListOdbSubnetsRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (OdbSubnet element : oracleDatabaseClient.listOdbSubnets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOdbSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbSubnetsPagedResponse)` |   
  
### listOdbSubnets(String parent)
    
    
    public final OracleDatabaseClient.ListOdbSubnetsPagedResponse listOdbSubnets(String parent)

Lists all the ODB Subnets in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString();
       for (OdbSubnet element : oracleDatabaseClient.listOdbSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent value for the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListOdbSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbSubnetsPagedResponse)` |   
  
### listOdbSubnetsCallable()
    
    
    public final UnaryCallable<ListOdbSubnetsRequest,ListOdbSubnetsResponse> listOdbSubnetsCallable()

Lists all the ODB Subnets in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbSubnetsRequest request =
           ListOdbSubnetsRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListOdbSubnetsResponse response =
             oracleDatabaseClient.listOdbSubnetsCallable().call(request);
         for (OdbSubnet element : response.getOdbSubnetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOdbSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsRequest),[ListOdbSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsResponse)>` |   
  
### listOdbSubnetsPagedCallable()
    
    
    public final UnaryCallable<ListOdbSubnetsRequest,OracleDatabaseClient.ListOdbSubnetsPagedResponse> listOdbSubnetsPagedCallable()

Lists all the ODB Subnets in a given ODB Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListOdbSubnetsRequest request =
           ListOdbSubnetsRequest.newBuilder()
               .setParent(OdbNetworkName.of("[PROJECT]", "[LOCATION]", "[ODB_NETWORK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<OdbSubnet> future =
           oracleDatabaseClient.listOdbSubnetsPagedCallable().futureCall(request);
       // Do something.
       for (OdbSubnet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOdbSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsRequest),[ListOdbSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbSubnetsPagedResponse)>` |   
  
### listPluggableDatabases(@Nullable LocationName parent)
    
    
    public final OracleDatabaseClient.ListPluggableDatabasesPagedResponse listPluggableDatabases(@Nullable LocationName parent)

Lists all the PluggableDatabases for the given project, location and Container Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PluggableDatabase element :
           oracleDatabaseClient.listPluggableDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.LocationName`  
Required. The parent, which owns this collection of PluggableDatabases. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListPluggableDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListPluggableDatabasesPagedResponse)` |   
  
### listPluggableDatabases(ListPluggableDatabasesRequest request)
    
    
    public final OracleDatabaseClient.ListPluggableDatabasesPagedResponse listPluggableDatabases(ListPluggableDatabasesRequest request)

Lists all the PluggableDatabases for the given project, location and Container Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListPluggableDatabasesRequest request =
           ListPluggableDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PluggableDatabase element :
           oracleDatabaseClient.listPluggableDatabases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPluggableDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListPluggableDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListPluggableDatabasesPagedResponse)` |   
  
### listPluggableDatabases(String parent)
    
    
    public final OracleDatabaseClient.ListPluggableDatabasesPagedResponse listPluggableDatabases(String parent)

Lists all the PluggableDatabases for the given project, location and Container Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PluggableDatabase element :
           oracleDatabaseClient.listPluggableDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of PluggableDatabases. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseClient.ListPluggableDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListPluggableDatabasesPagedResponse)` |   
  
### listPluggableDatabasesCallable()
    
    
    public final UnaryCallable<ListPluggableDatabasesRequest,ListPluggableDatabasesResponse> listPluggableDatabasesCallable()

Lists all the PluggableDatabases for the given project, location and Container Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListPluggableDatabasesRequest request =
           ListPluggableDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListPluggableDatabasesResponse response =
             oracleDatabaseClient.listPluggableDatabasesCallable().call(request);
         for (PluggableDatabase element : response.getPluggableDatabasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluggableDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesRequest),[ListPluggableDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesResponse)>` |   
  
### listPluggableDatabasesPagedCallable()
    
    
    public final UnaryCallable<ListPluggableDatabasesRequest,OracleDatabaseClient.ListPluggableDatabasesPagedResponse> listPluggableDatabasesPagedCallable()

Lists all the PluggableDatabases for the given project, location and Container Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ListPluggableDatabasesRequest request =
           ListPluggableDatabasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PluggableDatabase> future =
           oracleDatabaseClient.listPluggableDatabasesPagedCallable().futureCall(request);
       // Do something.
       for (PluggableDatabase element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluggableDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesRequest),[ListPluggableDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListPluggableDatabasesPagedResponse)>` |   
  
### refreshAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, Timestamp refreshCutoffTime)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> refreshAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, Timestamp refreshCutoffTime)

Refreshes the refreshable clone of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       Timestamp refreshCutoffTime = Timestamp.newBuilder().build();
       AutonomousDatabase response =
           oracleDatabaseClient.refreshAutonomousDatabaseAsync(name, refreshCutoffTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the AutonomousDatabase resource. Format: projects/{project}/location/{location}/autonomousDatabases/{autonomous_database}  
`refreshCutoffTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Required. The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are not part of the data refresh.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### refreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> refreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest request)

Refreshes the refreshable clone of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RefreshAutonomousDatabaseRequest request =
           RefreshAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRefreshCutoffTime(Timestamp.newBuilder().build())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.refreshAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RefreshAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### refreshAutonomousDatabaseAsync(String name, Timestamp refreshCutoffTime)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> refreshAutonomousDatabaseAsync(String name, Timestamp refreshCutoffTime)

Refreshes the refreshable clone of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       Timestamp refreshCutoffTime = Timestamp.newBuilder().build();
       AutonomousDatabase response =
           oracleDatabaseClient.refreshAutonomousDatabaseAsync(name, refreshCutoffTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the AutonomousDatabase resource. Format: projects/{project}/location/{location}/autonomousDatabases/{autonomous_database}  
`refreshCutoffTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Required. The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are not part of the data refresh.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### refreshAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<RefreshAutonomousDatabaseRequest,Operation> refreshAutonomousDatabaseCallable()

Refreshes the refreshable clone of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RefreshAutonomousDatabaseRequest request =
           RefreshAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRefreshCutoffTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.refreshAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RefreshAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### refreshAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<RefreshAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> refreshAutonomousDatabaseOperationCallable()

Refreshes the refreshable clone of an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RefreshAutonomousDatabaseRequest request =
           RefreshAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRefreshCutoffTime(Timestamp.newBuilder().build())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.refreshAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RefreshAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### removeVirtualMachineExadbVmClusterAsync(@Nullable ExadbVmClusterName name, List<String> hostnames)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> removeVirtualMachineExadbVmClusterAsync(@Nullable ExadbVmClusterName name, List<String> hostnames)

Removes virtual machines from an existing exadb vm cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExadbVmClusterName name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]");
       List<String> hostnames = new ArrayList<>();
       ExadbVmCluster response =
           oracleDatabaseClient.removeVirtualMachineExadbVmClusterAsync(name, hostnames).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.ExadbVmClusterName`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
`hostnames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The list of host names of db nodes to be removed from the ExadbVmCluster.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### removeVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest request)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> removeVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest request)

Removes virtual machines from an existing exadb vm cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RemoveVirtualMachineExadbVmClusterRequest request =
           RemoveVirtualMachineExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .addAllHostnames(new ArrayList<String>())
               .build();
       ExadbVmCluster response =
           oracleDatabaseClient.removeVirtualMachineExadbVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RemoveVirtualMachineExadbVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### removeVirtualMachineExadbVmClusterAsync(String name, List<String> hostnames)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> removeVirtualMachineExadbVmClusterAsync(String name, List<String> hostnames)

Removes virtual machines from an existing exadb vm cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString();
       List<String> hostnames = new ArrayList<>();
       ExadbVmCluster response =
           oracleDatabaseClient.removeVirtualMachineExadbVmClusterAsync(name, hostnames).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
`hostnames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The list of host names of db nodes to be removed from the ExadbVmCluster.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### removeVirtualMachineExadbVmClusterCallable()
    
    
    public final UnaryCallable<RemoveVirtualMachineExadbVmClusterRequest,Operation> removeVirtualMachineExadbVmClusterCallable()

Removes virtual machines from an existing exadb vm cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RemoveVirtualMachineExadbVmClusterRequest request =
           RemoveVirtualMachineExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .addAllHostnames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.removeVirtualMachineExadbVmClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RemoveVirtualMachineExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeVirtualMachineExadbVmClusterOperationCallable()
    
    
    public final OperationCallable<RemoveVirtualMachineExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> removeVirtualMachineExadbVmClusterOperationCallable()

Removes virtual machines from an existing exadb vm cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RemoveVirtualMachineExadbVmClusterRequest request =
           RemoveVirtualMachineExadbVmClusterRequest.newBuilder()
               .setName(
                   ExadbVmClusterName.of("[PROJECT]", "[LOCATION]", "[EXADB_VM_CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .addAllHostnames(new ArrayList<String>())
               .build();
       OperationFuture<ExadbVmCluster, OperationMetadata> future =
           oracleDatabaseClient
               .removeVirtualMachineExadbVmClusterOperationCallable()
               .futureCall(request);
       // Do something.
       ExadbVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RemoveVirtualMachineExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restartAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restartAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)

Restarts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response = oracleDatabaseClient.restartAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest request)

Restarts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestartAutonomousDatabaseRequest request =
           RestartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.restartAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestartAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restartAutonomousDatabaseAsync(String name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restartAutonomousDatabaseAsync(String name)

Restarts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response = oracleDatabaseClient.restartAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restartAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<RestartAutonomousDatabaseRequest,Operation> restartAutonomousDatabaseCallable()

Restarts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestartAutonomousDatabaseRequest request =
           RestartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.restartAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestartAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<RestartAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> restartAutonomousDatabaseOperationCallable()

Restarts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestartAutonomousDatabaseRequest request =
           RestartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.restartAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestartAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restoreAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, Timestamp restoreTime)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restoreAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, Timestamp restoreTime)

Restores a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       Timestamp restoreTime = Timestamp.newBuilder().build();
       AutonomousDatabase response =
           oracleDatabaseClient.restoreAutonomousDatabaseAsync(name, restoreTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`restoreTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Required. The time and date to restore the database to.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest request)

Restores a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestoreAutonomousDatabaseRequest request =
           RestoreAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRestoreTime(Timestamp.newBuilder().build())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.restoreAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestoreAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restoreAutonomousDatabaseAsync(String name, Timestamp restoreTime)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> restoreAutonomousDatabaseAsync(String name, Timestamp restoreTime)

Restores a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       Timestamp restoreTime = Timestamp.newBuilder().build();
       AutonomousDatabase response =
           oracleDatabaseClient.restoreAutonomousDatabaseAsync(name, restoreTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`restoreTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Required. The time and date to restore the database to.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restoreAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<RestoreAutonomousDatabaseRequest,Operation> restoreAutonomousDatabaseCallable()

Restores a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestoreAutonomousDatabaseRequest request =
           RestoreAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRestoreTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.restoreAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestoreAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<RestoreAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> restoreAutonomousDatabaseOperationCallable()

Restores a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       RestoreAutonomousDatabaseRequest request =
           RestoreAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setRestoreTime(Timestamp.newBuilder().build())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.restoreAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestoreAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> startAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)

Starts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response = oracleDatabaseClient.startAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startAutonomousDatabaseAsync(StartAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> startAutonomousDatabaseAsync(StartAutonomousDatabaseRequest request)

Starts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartAutonomousDatabaseRequest request =
           StartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.startAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startAutonomousDatabaseAsync(String name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> startAutonomousDatabaseAsync(String name)

Starts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response = oracleDatabaseClient.startAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<StartAutonomousDatabaseRequest,Operation> startAutonomousDatabaseCallable()

Starts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartAutonomousDatabaseRequest request =
           StartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.startAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<StartAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> startAutonomousDatabaseOperationCallable()

Starts an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartAutonomousDatabaseRequest request =
           StartAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.startAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> startGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)

Starts a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateDeploymentName name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]");
       GoldengateDeployment response =
           oracleDatabaseClient.startGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateDeploymentName`  
Required. The name of the Goldengate Deployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startGoldengateDeploymentAsync(StartGoldengateDeploymentRequest request)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> startGoldengateDeploymentAsync(StartGoldengateDeploymentRequest request)

Starts a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartGoldengateDeploymentRequest request =
           StartGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       GoldengateDeployment response =
           oracleDatabaseClient.startGoldengateDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartGoldengateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startGoldengateDeploymentAsync(String name)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> startGoldengateDeploymentAsync(String name)

Starts a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
               .toString();
       GoldengateDeployment response =
           oracleDatabaseClient.startGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Goldengate Deployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startGoldengateDeploymentCallable()
    
    
    public final UnaryCallable<StartGoldengateDeploymentRequest,Operation> startGoldengateDeploymentCallable()

Starts a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartGoldengateDeploymentRequest request =
           StartGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.startGoldengateDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startGoldengateDeploymentOperationCallable()
    
    
    public final OperationCallable<StartGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> startGoldengateDeploymentOperationCallable()

Starts a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StartGoldengateDeploymentRequest request =
           StartGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       OperationFuture<GoldengateDeployment, OperationMetadata> future =
           oracleDatabaseClient.startGoldengateDeploymentOperationCallable().futureCall(request);
       // Do something.
       GoldengateDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> stopAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name)

Stops an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response = oracleDatabaseClient.stopAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> stopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest request)

Stops an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopAutonomousDatabaseRequest request =
           StopAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response = oracleDatabaseClient.stopAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopAutonomousDatabaseAsync(String name)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> stopAutonomousDatabaseAsync(String name)

Stops an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response = oracleDatabaseClient.stopAutonomousDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<StopAutonomousDatabaseRequest,Operation> stopAutonomousDatabaseCallable()

Stops an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopAutonomousDatabaseRequest request =
           StopAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.stopAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<StopAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> stopAutonomousDatabaseOperationCallable()

Stops an Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopAutonomousDatabaseRequest request =
           StopAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.stopAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> stopGoldengateDeploymentAsync(@Nullable GoldengateDeploymentName name)

Stops a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateDeploymentName name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]");
       GoldengateDeployment response =
           oracleDatabaseClient.stopGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateDeploymentName`  
Required. The name of the Goldengate Deployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest request)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> stopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest request)

Stops a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopGoldengateDeploymentRequest request =
           StopGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       GoldengateDeployment response =
           oracleDatabaseClient.stopGoldengateDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopGoldengateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopGoldengateDeploymentAsync(String name)
    
    
    public final OperationFuture<GoldengateDeployment,OperationMetadata> stopGoldengateDeploymentAsync(String name)

Stops a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
               .toString();
       GoldengateDeployment response =
           oracleDatabaseClient.stopGoldengateDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Goldengate Deployment in the following format: projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopGoldengateDeploymentCallable()
    
    
    public final UnaryCallable<StopGoldengateDeploymentRequest,Operation> stopGoldengateDeploymentCallable()

Stops a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopGoldengateDeploymentRequest request =
           StopGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.stopGoldengateDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopGoldengateDeploymentOperationCallable()
    
    
    public final OperationCallable<StopGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> stopGoldengateDeploymentOperationCallable()

Stops a single GoldengateDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       StopGoldengateDeploymentRequest request =
           StopGoldengateDeploymentRequest.newBuilder()
               .setName(
                   GoldengateDeploymentName.of("[PROJECT]", "[LOCATION]", "[GOLDENGATE_DEPLOYMENT]")
                       .toString())
               .build();
       OperationFuture<GoldengateDeployment, OperationMetadata> future =
           oracleDatabaseClient.stopGoldengateDeploymentOperationCallable().futureCall(request);
       // Do something.
       GoldengateDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabaseName peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response =
           oracleDatabaseClient
               .switchoverAutonomousDatabaseAsync(name, peerAutonomousDatabase)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Optional. The peer database name to switch over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, String peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseAsync(@Nullable AutonomousDatabaseName name, String peerAutonomousDatabase)

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabaseName name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       String peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response =
           oracleDatabaseClient
               .switchoverAutonomousDatabaseAsync(name, peerAutonomousDatabase)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The peer database name to switch over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest request)

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       SwitchoverAutonomousDatabaseRequest request =
           SwitchoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.switchoverAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.SwitchoverAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseAsync(String name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseAsync(String name, @Nullable AutonomousDatabaseName peerAutonomousDatabase)

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabaseName peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]");
       AutonomousDatabase response =
           oracleDatabaseClient
               .switchoverAutonomousDatabaseAsync(name, peerAutonomousDatabase)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.AutonomousDatabaseName`  
Optional. The peer database name to switch over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseAsync(String name, String peerAutonomousDatabase)

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       String peerAutonomousDatabase =
           AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]").toString();
       AutonomousDatabase response =
           oracleDatabaseClient
               .switchoverAutonomousDatabaseAsync(name, peerAutonomousDatabase)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.  
`peerAutonomousDatabase` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The peer database name to switch over to. Required for cross-region standby, and must be omitted for in-region Data Guard.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<SwitchoverAutonomousDatabaseRequest,Operation> switchoverAutonomousDatabaseCallable()

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       SwitchoverAutonomousDatabaseRequest request =
           SwitchoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.switchoverAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.SwitchoverAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### switchoverAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<SwitchoverAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseOperationCallable()

Initiates a switchover of specified autonomous database to the associated peer database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       SwitchoverAutonomousDatabaseRequest request =
           SwitchoverAutonomousDatabaseRequest.newBuilder()
               .setName(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .setPeerAutonomousDatabase(
                   AutonomousDatabaseName.of("[PROJECT]", "[LOCATION]", "[AUTONOMOUS_DATABASE]")
                       .toString())
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.switchoverAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.SwitchoverAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### testGoldengateConnectionAssignment(@Nullable GoldengateConnectionAssignmentName name)
    
    
    public final TestGoldengateConnectionAssignmentResponse testGoldengateConnectionAssignment(@Nullable GoldengateConnectionAssignmentName name)

Tests a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       GoldengateConnectionAssignmentName name =
           GoldengateConnectionAssignmentName.of(
               "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]");
       TestGoldengateConnectionAssignmentResponse response =
           oracleDatabaseClient.testGoldengateConnectionAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignmentName`  
Required. Name of the connection assignment for which to test connection. projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentResponse)` |   
  
### testGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest request)
    
    
    public final TestGoldengateConnectionAssignmentResponse testGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest request)

Tests a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       TestGoldengateConnectionAssignmentRequest request =
           TestGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .build();
       TestGoldengateConnectionAssignmentResponse response =
           oracleDatabaseClient.testGoldengateConnectionAssignment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentResponse)` |   
  
### testGoldengateConnectionAssignment(String name)
    
    
    public final TestGoldengateConnectionAssignmentResponse testGoldengateConnectionAssignment(String name)

Tests a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       String name =
           GoldengateConnectionAssignmentName.of(
                   "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
               .toString();
       TestGoldengateConnectionAssignmentResponse response =
           oracleDatabaseClient.testGoldengateConnectionAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection assignment for which to test connection. projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengate_connection_assignment}  
**Returns**  
---  
**Type** | **Description**  
`[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentResponse)` |   
  
### testGoldengateConnectionAssignmentCallable()
    
    
    public final UnaryCallable<TestGoldengateConnectionAssignmentRequest,TestGoldengateConnectionAssignmentResponse> testGoldengateConnectionAssignmentCallable()

Tests a single GoldengateConnectionAssignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       TestGoldengateConnectionAssignmentRequest request =
           TestGoldengateConnectionAssignmentRequest.newBuilder()
               .setName(
                   GoldengateConnectionAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[GOLDENGATE_CONNECTION_ASSIGNMENT]")
                       .toString())
               .build();
       ApiFuture<TestGoldengateConnectionAssignmentResponse> future =
           oracleDatabaseClient.testGoldengateConnectionAssignmentCallable().futureCall(request);
       // Do something.
       TestGoldengateConnectionAssignmentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentRequest),[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentResponse)>` |   
  
### updateAutonomousDatabaseAsync(AutonomousDatabase autonomousDatabase, FieldMask updateMask)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> updateAutonomousDatabaseAsync(AutonomousDatabase autonomousDatabase, FieldMask updateMask)

Updates the parameters of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       AutonomousDatabase autonomousDatabase = AutonomousDatabase.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AutonomousDatabase response =
           oracleDatabaseClient.updateAutonomousDatabaseAsync(autonomousDatabase, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`autonomousDatabase` | `[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Exadata resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest request)
    
    
    public final OperationFuture<AutonomousDatabase,OperationMetadata> updateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest request)

Updates the parameters of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateAutonomousDatabaseRequest request =
           UpdateAutonomousDatabaseRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AutonomousDatabase response =
           oracleDatabaseClient.updateAutonomousDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateAutonomousDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateAutonomousDatabaseCallable()
    
    
    public final UnaryCallable<UpdateAutonomousDatabaseRequest,Operation> updateAutonomousDatabaseCallable()

Updates the parameters of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateAutonomousDatabaseRequest request =
           UpdateAutonomousDatabaseRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.updateAutonomousDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAutonomousDatabaseOperationCallable()
    
    
    public final OperationCallable<UpdateAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> updateAutonomousDatabaseOperationCallable()

Updates the parameters of a single Autonomous Database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateAutonomousDatabaseRequest request =
           UpdateAutonomousDatabaseRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutonomousDatabase(AutonomousDatabase.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AutonomousDatabase, OperationMetadata> future =
           oracleDatabaseClient.updateAutonomousDatabaseOperationCallable().futureCall(request);
       // Do something.
       AutonomousDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateExadbVmClusterAsync(ExadbVmCluster exadbVmCluster, FieldMask updateMask)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> updateExadbVmClusterAsync(ExadbVmCluster exadbVmCluster, FieldMask updateMask)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       ExadbVmCluster exadbVmCluster = ExadbVmCluster.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ExadbVmCluster response =
           oracleDatabaseClient.updateExadbVmClusterAsync(exadbVmCluster, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`exadbVmCluster` | `[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A mask specifying which fields in th VM Cluster should be updated. A field specified in the mask is overwritten. If a mask isn't provided then all the fields in the VM Cluster are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateExadbVmClusterAsync(UpdateExadbVmClusterRequest request)
    
    
    public final OperationFuture<ExadbVmCluster,OperationMetadata> updateExadbVmClusterAsync(UpdateExadbVmClusterRequest request)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateExadbVmClusterRequest request =
           UpdateExadbVmClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ExadbVmCluster response = oracleDatabaseClient.updateExadbVmClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateExadbVmClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateExadbVmClusterCallable()
    
    
    public final UnaryCallable<UpdateExadbVmClusterRequest,Operation> updateExadbVmClusterCallable()

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateExadbVmClusterRequest request =
           UpdateExadbVmClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           oracleDatabaseClient.updateExadbVmClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExadbVmClusterOperationCallable()
    
    
    public final OperationCallable<UpdateExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> updateExadbVmClusterOperationCallable()

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
       UpdateExadbVmClusterRequest request =
           UpdateExadbVmClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExadbVmCluster(ExadbVmCluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExadbVmCluster, OperationMetadata> future =
           oracleDatabaseClient.updateExadbVmClusterOperationCallable().futureCall(request);
       // Do something.
       ExadbVmCluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
