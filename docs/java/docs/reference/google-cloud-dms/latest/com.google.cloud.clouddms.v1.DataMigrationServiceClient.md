---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient
title: Class DataMigrationServiceClient (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:15.332240+00:00
---

# Class DataMigrationServiceClient (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataMigrationServiceClient (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.80.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.8  2.1.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dms/google-cloud-dms/src/main/java/com/google/cloud/clouddms/v1/DataMigrationServiceClient.java)| [Product Reference](https://cloud.google.com/database-migration/docs)| [REST Documentation](https://cloud.google.com/database-migration/docs/reference/rest)  
---|---|---  
  
Service Description: Database Migration service

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       MigrationJobName name = MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]");
       MigrationJob response = dataMigrationServiceClient.getMigrationJob(name);
     }
     

Note: close() needs to be called on the DataMigrationServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListMigrationJobs |  Lists migration jobs in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMigrationJobs(ListMigrationJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMigrationJobs(LocationName parent) 
  * listMigrationJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMigrationJobsPagedCallable() 
  * listMigrationJobsCallable() 

  
GetMigrationJob |  Gets details of a single migration job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMigrationJob(GetMigrationJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMigrationJob(MigrationJobName name) 
  * getMigrationJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMigrationJobCallable() 

  
CreateMigrationJob |  Creates a new migration job in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMigrationJobAsync(CreateMigrationJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMigrationJobAsync(LocationName parent, MigrationJob migrationJob, String migrationJobId) 
  * createMigrationJobAsync(String parent, MigrationJob migrationJob, String migrationJobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMigrationJobOperationCallable() 
  * createMigrationJobCallable() 

  
UpdateMigrationJob |  Updates the parameters of a single migration job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMigrationJobAsync(UpdateMigrationJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateMigrationJobAsync(MigrationJob migrationJob, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMigrationJobOperationCallable() 
  * updateMigrationJobCallable() 

  
DeleteMigrationJob |  Deletes a single migration job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMigrationJobAsync(DeleteMigrationJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteMigrationJobAsync(MigrationJobName name) 
  * deleteMigrationJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMigrationJobOperationCallable() 
  * deleteMigrationJobCallable() 

  
StartMigrationJob |  Start an already created migration job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startMigrationJobAsync(StartMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startMigrationJobOperationCallable() 
  * startMigrationJobCallable() 

  
StopMigrationJob |  Stops a running migration job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopMigrationJobAsync(StopMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopMigrationJobOperationCallable() 
  * stopMigrationJobCallable() 

  
ResumeMigrationJob |  Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeMigrationJobAsync(ResumeMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeMigrationJobOperationCallable() 
  * resumeMigrationJobCallable() 

  
PromoteMigrationJob |  Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * promoteMigrationJobAsync(PromoteMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * promoteMigrationJobOperationCallable() 
  * promoteMigrationJobCallable() 

  
VerifyMigrationJob |  Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * verifyMigrationJobAsync(VerifyMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * verifyMigrationJobOperationCallable() 
  * verifyMigrationJobCallable() 

  
RestartMigrationJob |  Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restartMigrationJobAsync(RestartMigrationJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restartMigrationJobOperationCallable() 
  * restartMigrationJobCallable() 

  
GenerateSshScript |  Generate a SSH configuration script to configure the reverse SSH connectivity. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateSshScript(GenerateSshScriptRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateSshScriptCallable() 

  
GenerateTcpProxyScript |  Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateTcpProxyScript(GenerateTcpProxyScriptRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateTcpProxyScriptCallable() 

  
ListConnectionProfiles |  Retrieves a list of all connection profiles in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConnectionProfiles(ListConnectionProfilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConnectionProfiles(LocationName parent) 
  * listConnectionProfiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConnectionProfilesPagedCallable() 
  * listConnectionProfilesCallable() 

  
GetConnectionProfile |  Gets details of a single connection profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnectionProfile(GetConnectionProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConnectionProfile(ConnectionProfileName name) 
  * getConnectionProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectionProfileCallable() 

  
CreateConnectionProfile |  Creates a new connection profile in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConnectionProfileAsync(CreateConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConnectionProfileAsync(LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId) 
  * createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConnectionProfileOperationCallable() 
  * createConnectionProfileCallable() 

  
UpdateConnectionProfile |  Update the configuration of a single connection profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConnectionProfileAsync(UpdateConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConnectionProfileOperationCallable() 
  * updateConnectionProfileCallable() 

  
DeleteConnectionProfile |  Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConnectionProfileAsync(DeleteConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteConnectionProfileAsync(ConnectionProfileName name) 
  * deleteConnectionProfileAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConnectionProfileOperationCallable() 
  * deleteConnectionProfileCallable() 

  
CreatePrivateConnection |  Creates a new private connection in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateConnectionAsync(CreatePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPrivateConnectionAsync(LocationName parent, PrivateConnection privateConnection, String privateConnectionId) 
  * createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateConnectionOperationCallable() 
  * createPrivateConnectionCallable() 

  
GetPrivateConnection |  Gets details of a single private connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateConnection(GetPrivateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateConnection(PrivateConnectionName name) 
  * getPrivateConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateConnectionCallable() 

  
ListPrivateConnections |  Retrieves a list of private connections in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateConnections(ListPrivateConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateConnections(LocationName parent) 
  * listPrivateConnections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateConnectionsPagedCallable() 
  * listPrivateConnectionsCallable() 

  
DeletePrivateConnection |  Deletes a single Database Migration Service private connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateConnectionAsync(DeletePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePrivateConnectionAsync(PrivateConnectionName name) 
  * deletePrivateConnectionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateConnectionOperationCallable() 
  * deletePrivateConnectionCallable() 

  
GetConversionWorkspace |  Gets details of a single conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversionWorkspace(GetConversionWorkspaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversionWorkspace(ConversionWorkspaceName name) 
  * getConversionWorkspace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversionWorkspaceCallable() 

  
ListConversionWorkspaces |  Lists conversion workspaces in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversionWorkspaces(ListConversionWorkspacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversionWorkspaces(LocationName parent) 
  * listConversionWorkspaces(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversionWorkspacesPagedCallable() 
  * listConversionWorkspacesCallable() 

  
CreateConversionWorkspace |  Creates a new conversion workspace in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversionWorkspaceAsync(CreateConversionWorkspaceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConversionWorkspaceAsync(LocationName parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId) 
  * createConversionWorkspaceAsync(String parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversionWorkspaceOperationCallable() 
  * createConversionWorkspaceCallable() 

  
UpdateConversionWorkspace |  Updates the parameters of a single conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConversionWorkspaceAsync(UpdateConversionWorkspaceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateConversionWorkspaceAsync(ConversionWorkspace conversionWorkspace, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConversionWorkspaceOperationCallable() 
  * updateConversionWorkspaceCallable() 

  
DeleteConversionWorkspace |  Deletes a single conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversionWorkspaceAsync(DeleteConversionWorkspaceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteConversionWorkspaceAsync(ConversionWorkspaceName name) 
  * deleteConversionWorkspaceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversionWorkspaceOperationCallable() 
  * deleteConversionWorkspaceCallable() 

  
CreateMappingRule |  Creates a new mapping rule for a given conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMappingRule(CreateMappingRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMappingRule(ConversionWorkspaceName parent, MappingRule mappingRule, String mappingRuleId) 
  * createMappingRule(String parent, MappingRule mappingRule, String mappingRuleId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMappingRuleCallable() 

  
DeleteMappingRule |  Deletes a single mapping rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMappingRule(DeleteMappingRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteMappingRule(ConversionWorkspaceName name) 
  * deleteMappingRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMappingRuleCallable() 

  
ListMappingRules |  Lists the mapping rules for a specific conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMappingRules(ListMappingRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMappingRules(ConversionWorkspaceName parent) 
  * listMappingRules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMappingRulesPagedCallable() 
  * listMappingRulesCallable() 

  
GetMappingRule |  Gets the details of a mapping rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMappingRule(GetMappingRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMappingRule(MappingRuleName name) 
  * getMappingRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMappingRuleCallable() 

  
SeedConversionWorkspace |  Imports a snapshot of the source database into the conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * seedConversionWorkspaceAsync(SeedConversionWorkspaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * seedConversionWorkspaceOperationCallable() 
  * seedConversionWorkspaceCallable() 

  
ImportMappingRules |  Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importMappingRulesAsync(ImportMappingRulesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importMappingRulesOperationCallable() 
  * importMappingRulesCallable() 

  
ConvertConversionWorkspace |  Creates a draft tree schema for the destination database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * convertConversionWorkspaceAsync(ConvertConversionWorkspaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * convertConversionWorkspaceOperationCallable() 
  * convertConversionWorkspaceCallable() 

  
CommitConversionWorkspace |  Marks all the data in the conversion workspace as committed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * commitConversionWorkspaceAsync(CommitConversionWorkspaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * commitConversionWorkspaceOperationCallable() 
  * commitConversionWorkspaceCallable() 

  
RollbackConversionWorkspace |  Rolls back a conversion workspace to the last committed snapshot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rollbackConversionWorkspaceAsync(RollbackConversionWorkspaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rollbackConversionWorkspaceOperationCallable() 
  * rollbackConversionWorkspaceCallable() 

  
ApplyConversionWorkspace |  Applies draft tree onto a specific destination database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * applyConversionWorkspaceAsync(ApplyConversionWorkspaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * applyConversionWorkspaceOperationCallable() 
  * applyConversionWorkspaceCallable() 

  
DescribeDatabaseEntities |  Describes the database entities tree for a specific conversion workspace and a specific tree type.  Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * describeDatabaseEntities(DescribeDatabaseEntitiesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * describeDatabaseEntitiesPagedCallable() 
  * describeDatabaseEntitiesCallable() 

  
SearchBackgroundJobs |  Searches/lists the background jobs for a specific conversion workspace.  The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchBackgroundJobs(SearchBackgroundJobsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchBackgroundJobsCallable() 

  
DescribeConversionWorkspaceRevisions |  Retrieves a list of committed revisions of a specific conversion workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * describeConversionWorkspaceRevisions(DescribeConversionWorkspaceRevisionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * describeConversionWorkspaceRevisionsCallable() 

  
FetchStaticIps |  Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchStaticIps(FetchStaticIpsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchStaticIps(LocationName name) 
  * fetchStaticIps(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchStaticIpsPagedCallable() 
  * fetchStaticIpsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataMigrationServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataMigrationServiceSettings dataMigrationServiceSettings =
         DataMigrationServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create(dataMigrationServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataMigrationServiceSettings dataMigrationServiceSettings =
         DataMigrationServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create(dataMigrationServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataMigrationServiceClient

## Static Methods 

### create()
    
    
    public static final DataMigrationServiceClient create()

Constructs an instance of DataMigrationServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataMigrationServiceSettings settings)
    
    
    public static final DataMigrationServiceClient create(DataMigrationServiceSettings settings)

Constructs an instance of DataMigrationServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataMigrationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataMigrationServiceStub stub)
    
    
    public static final DataMigrationServiceClient create(DataMigrationServiceStub stub)

Constructs an instance of DataMigrationServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataMigrationServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataMigrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.stub.DataMigrationServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient)` |   
  
## Constructors 

### DataMigrationServiceClient(DataMigrationServiceSettings settings)
    
    
    protected DataMigrationServiceClient(DataMigrationServiceSettings settings)

Constructs an instance of DataMigrationServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataMigrationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceSettings)`  
  
  
### DataMigrationServiceClient(DataMigrationServiceStub stub)
    
    
    protected DataMigrationServiceClient(DataMigrationServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataMigrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.stub.DataMigrationServiceStub)`  
  
  
## Methods 

### applyConversionWorkspaceAsync(ApplyConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> applyConversionWorkspaceAsync(ApplyConversionWorkspaceRequest request)

Applies draft tree onto a specific destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ApplyConversionWorkspaceRequest request =
           ApplyConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setDryRun(true)
               .setAutoCommit(true)
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.applyConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApplyConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ApplyConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### applyConversionWorkspaceCallable()
    
    
    public final UnaryCallable<ApplyConversionWorkspaceRequest,Operation> applyConversionWorkspaceCallable()

Applies draft tree onto a specific destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ApplyConversionWorkspaceRequest request =
           ApplyConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setDryRun(true)
               .setAutoCommit(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.applyConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApplyConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ApplyConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### applyConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<ApplyConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> applyConversionWorkspaceOperationCallable()

Applies draft tree onto a specific destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ApplyConversionWorkspaceRequest request =
           ApplyConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setDryRun(true)
               .setAutoCommit(true)
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .applyConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ApplyConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ApplyConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
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

### commitConversionWorkspaceAsync(CommitConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> commitConversionWorkspaceAsync(CommitConversionWorkspaceRequest request)

Marks all the data in the conversion workspace as committed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CommitConversionWorkspaceRequest request =
           CommitConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setCommitName("commitName1018078306")
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.commitConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CommitConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CommitConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### commitConversionWorkspaceCallable()
    
    
    public final UnaryCallable<CommitConversionWorkspaceRequest,Operation> commitConversionWorkspaceCallable()

Marks all the data in the conversion workspace as committed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CommitConversionWorkspaceRequest request =
           CommitConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setCommitName("commitName1018078306")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.commitConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CommitConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CommitConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### commitConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<CommitConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> commitConversionWorkspaceOperationCallable()

Marks all the data in the conversion workspace as committed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CommitConversionWorkspaceRequest request =
           CommitConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setCommitName("commitName1018078306")
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .commitConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CommitConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CommitConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### convertConversionWorkspaceAsync(ConvertConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> convertConversionWorkspaceAsync(ConvertConversionWorkspaceRequest request)

Creates a draft tree schema for the destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConvertConversionWorkspaceRequest request =
           ConvertConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .setFilter("filter-1274492040")
               .setConvertFullPath(true)
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.convertConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConvertConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### convertConversionWorkspaceCallable()
    
    
    public final UnaryCallable<ConvertConversionWorkspaceRequest,Operation> convertConversionWorkspaceCallable()

Creates a draft tree schema for the destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConvertConversionWorkspaceRequest request =
           ConvertConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .setFilter("filter-1274492040")
               .setConvertFullPath(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.convertConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConvertConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### convertConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<ConvertConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> convertConversionWorkspaceOperationCallable()

Creates a draft tree schema for the destination database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConvertConversionWorkspaceRequest request =
           ConvertConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .setFilter("filter-1274492040")
               .setConvertFullPath(true)
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .convertConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ConvertConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConvertConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConnectionProfileAsync(@Nullable LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(@Nullable LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId)

Creates a new connection profile in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       String connectionProfileId = "connectionProfileId597575526";
       ConnectionProfile response =
           dataMigrationServiceClient
               .createConnectionProfileAsync(parent, connectionProfile, connectionProfileId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of connection profiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)`  
Required. The create request body including the connection profile data  
`connectionProfileId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The connection profile identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConnectionProfileAsync(CreateConnectionProfileRequest request)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(CreateConnectionProfileRequest request)

Creates a new connection profile in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       ConnectionProfile response =
           dataMigrationServiceClient.createConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId)

Creates a new connection profile in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       String connectionProfileId = "connectionProfileId597575526";
       ConnectionProfile response =
           dataMigrationServiceClient
               .createConnectionProfileAsync(parent, connectionProfile, connectionProfileId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of connection profiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)`  
Required. The create request body including the connection profile data  
`connectionProfileId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The connection profile identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConnectionProfileCallable()
    
    
    public final UnaryCallable<CreateConnectionProfileRequest,Operation> createConnectionProfileCallable()

Creates a new connection profile in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.createConnectionProfileCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConnectionProfileOperationCallable()
    
    
    public final OperationCallable<CreateConnectionProfileRequest,ConnectionProfile,OperationMetadata> createConnectionProfileOperationCallable()

Creates a new connection profile in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       OperationFuture<ConnectionProfile, OperationMetadata> future =
           dataMigrationServiceClient.createConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConversionWorkspaceAsync(@Nullable LocationName parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> createConversionWorkspaceAsync(@Nullable LocationName parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId)

Creates a new conversion workspace in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ConversionWorkspace conversionWorkspace = ConversionWorkspace.newBuilder().build();
       String conversionWorkspaceId = "conversionWorkspaceId-928604774";
       ConversionWorkspace response =
           dataMigrationServiceClient
               .createConversionWorkspaceAsync(parent, conversionWorkspace, conversionWorkspaceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of conversion workspaces.  
`conversionWorkspace` | `[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)`  
Required. Represents a conversion workspace object.  
`conversionWorkspaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the conversion workspace to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConversionWorkspaceAsync(CreateConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> createConversionWorkspaceAsync(CreateConversionWorkspaceRequest request)

Creates a new conversion workspace in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConversionWorkspaceRequest request =
           CreateConversionWorkspaceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConversionWorkspaceId("conversionWorkspaceId-928604774")
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.createConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConversionWorkspaceAsync(String parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> createConversionWorkspaceAsync(String parent, ConversionWorkspace conversionWorkspace, String conversionWorkspaceId)

Creates a new conversion workspace in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ConversionWorkspace conversionWorkspace = ConversionWorkspace.newBuilder().build();
       String conversionWorkspaceId = "conversionWorkspaceId-928604774";
       ConversionWorkspace response =
           dataMigrationServiceClient
               .createConversionWorkspaceAsync(parent, conversionWorkspace, conversionWorkspaceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of conversion workspaces.  
`conversionWorkspace` | `[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)`  
Required. Represents a conversion workspace object.  
`conversionWorkspaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the conversion workspace to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createConversionWorkspaceCallable()
    
    
    public final UnaryCallable<CreateConversionWorkspaceRequest,Operation> createConversionWorkspaceCallable()

Creates a new conversion workspace in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConversionWorkspaceRequest request =
           CreateConversionWorkspaceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConversionWorkspaceId("conversionWorkspaceId-928604774")
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.createConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<CreateConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> createConversionWorkspaceOperationCallable()

Creates a new conversion workspace in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateConversionWorkspaceRequest request =
           CreateConversionWorkspaceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConversionWorkspaceId("conversionWorkspaceId-928604774")
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .createConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createMappingRule(@Nullable ConversionWorkspaceName parent, MappingRule mappingRule, String mappingRuleId)
    
    
    public final MappingRule createMappingRule(@Nullable ConversionWorkspaceName parent, MappingRule mappingRule, String mappingRuleId)

Creates a new mapping rule for a given conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspaceName parent =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]");
       MappingRule mappingRule = MappingRule.newBuilder().build();
       String mappingRuleId = "mappingRuleId-900824155";
       MappingRule response =
           dataMigrationServiceClient.createMappingRule(parent, mappingRule, mappingRuleId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConversionWorkspaceName`  
Required. The parent which owns this collection of mapping rules.  
`mappingRule` | `[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)`  
Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object.  
`mappingRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the rule to create.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### createMappingRule(CreateMappingRuleRequest request)
    
    
    public final MappingRule createMappingRule(CreateMappingRuleRequest request)

Creates a new mapping rule for a given conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateMappingRuleRequest request =
           CreateMappingRuleRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setMappingRuleId("mappingRuleId-900824155")
               .setMappingRule(MappingRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MappingRule response = dataMigrationServiceClient.createMappingRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateMappingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### createMappingRule(String parent, MappingRule mappingRule, String mappingRuleId)
    
    
    public final MappingRule createMappingRule(String parent, MappingRule mappingRule, String mappingRuleId)

Creates a new mapping rule for a given conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
               .toString();
       MappingRule mappingRule = MappingRule.newBuilder().build();
       String mappingRuleId = "mappingRuleId-900824155";
       MappingRule response =
           dataMigrationServiceClient.createMappingRule(parent, mappingRule, mappingRuleId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of mapping rules.  
`mappingRule` | `[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)`  
Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object.  
`mappingRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the rule to create.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### createMappingRuleCallable()
    
    
    public final UnaryCallable<CreateMappingRuleRequest,MappingRule> createMappingRuleCallable()

Creates a new mapping rule for a given conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateMappingRuleRequest request =
           CreateMappingRuleRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setMappingRuleId("mappingRuleId-900824155")
               .setMappingRule(MappingRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<MappingRule> future =
           dataMigrationServiceClient.createMappingRuleCallable().futureCall(request);
       // Do something.
       MappingRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateMappingRuleRequest),[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)>` |   
  
### createMigrationJobAsync(@Nullable LocationName parent, MigrationJob migrationJob, String migrationJobId)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> createMigrationJobAsync(@Nullable LocationName parent, MigrationJob migrationJob, String migrationJobId)

Creates a new migration job in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MigrationJob migrationJob = MigrationJob.newBuilder().build();
       String migrationJobId = "migrationJobId1870575242";
       MigrationJob response =
           dataMigrationServiceClient
               .createMigrationJobAsync(parent, migrationJob, migrationJobId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of migration jobs.  
`migrationJob` | `[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)`  
Required. Represents a [migration job](https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs) object.  
`migrationJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the instance to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createMigrationJobAsync(CreateMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> createMigrationJobAsync(CreateMigrationJobRequest request)

Creates a new migration job in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateMigrationJobRequest request =
           CreateMigrationJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMigrationJobId("migrationJobId1870575242")
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MigrationJob response = dataMigrationServiceClient.createMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createMigrationJobAsync(String parent, MigrationJob migrationJob, String migrationJobId)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> createMigrationJobAsync(String parent, MigrationJob migrationJob, String migrationJobId)

Creates a new migration job in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       MigrationJob migrationJob = MigrationJob.newBuilder().build();
       String migrationJobId = "migrationJobId1870575242";
       MigrationJob response =
           dataMigrationServiceClient
               .createMigrationJobAsync(parent, migrationJob, migrationJobId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of migration jobs.  
`migrationJob` | `[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)`  
Required. Represents a [migration job](https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs) object.  
`migrationJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the instance to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createMigrationJobCallable()
    
    
    public final UnaryCallable<CreateMigrationJobRequest,Operation> createMigrationJobCallable()

Creates a new migration job in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateMigrationJobRequest request =
           CreateMigrationJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMigrationJobId("migrationJobId1870575242")
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.createMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMigrationJobOperationCallable()
    
    
    public final OperationCallable<CreateMigrationJobRequest,MigrationJob,OperationMetadata> createMigrationJobOperationCallable()

Creates a new migration job in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreateMigrationJobRequest request =
           CreateMigrationJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMigrationJobId("migrationJobId1870575242")
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.createMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreateMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)

Creates a new private connection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           dataMigrationServiceClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)`  
Required. The private connection resource to create.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The private connection identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(CreatePrivateConnectionRequest request)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(CreatePrivateConnectionRequest request)

Creates a new private connection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSkipValidation(true)
               .build();
       PrivateConnection response =
           dataMigrationServiceClient.createPrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)

Creates a new private connection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           dataMigrationServiceClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)`  
Required. The private connection resource to create.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The private connection identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### createPrivateConnectionCallable()
    
    
    public final UnaryCallable<CreatePrivateConnectionRequest,Operation> createPrivateConnectionCallable()

Creates a new private connection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSkipValidation(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.createPrivateConnectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateConnectionOperationCallable()
    
    
    public final OperationCallable<CreatePrivateConnectionRequest,PrivateConnection,OperationMetadata> createPrivateConnectionOperationCallable()

Creates a new private connection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSkipValidation(true)
               .build();
       OperationFuture<PrivateConnection, OperationMetadata> future =
           dataMigrationServiceClient.createPrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.CreatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(@Nullable ConnectionProfileName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(@Nullable ConnectionProfileName name)

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConnectionProfileName name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
       dataMigrationServiceClient.deleteConnectionProfileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConnectionProfileName`  
Required. Name of the connection profile resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(DeleteConnectionProfileRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(DeleteConnectionProfileRequest request)

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       dataMigrationServiceClient.deleteConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(String name)

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]").toString();
       dataMigrationServiceClient.deleteConnectionProfileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection profile resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileCallable()
    
    
    public final UnaryCallable<DeleteConnectionProfileRequest,Operation> deleteConnectionProfileCallable()

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.deleteConnectionProfileCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConnectionProfileOperationCallable()
    
    
    public final OperationCallable<DeleteConnectionProfileRequest,Empty,OperationMetadata> deleteConnectionProfileOperationCallable()

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataMigrationServiceClient.deleteConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConnectionProfileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConversionWorkspaceAsync(@Nullable ConversionWorkspaceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConversionWorkspaceAsync(@Nullable ConversionWorkspaceName name)

Deletes a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspaceName name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]");
       dataMigrationServiceClient.deleteConversionWorkspaceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConversionWorkspaceName`  
Required. Name of the conversion workspace resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConversionWorkspaceAsync(DeleteConversionWorkspaceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConversionWorkspaceAsync(DeleteConversionWorkspaceRequest request)

Deletes a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConversionWorkspaceRequest request =
           DeleteConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       dataMigrationServiceClient.deleteConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConversionWorkspaceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConversionWorkspaceAsync(String name)

Deletes a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
               .toString();
       dataMigrationServiceClient.deleteConversionWorkspaceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the conversion workspace resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteConversionWorkspaceCallable()
    
    
    public final UnaryCallable<DeleteConversionWorkspaceRequest,Operation> deleteConversionWorkspaceCallable()

Deletes a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConversionWorkspaceRequest request =
           DeleteConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.deleteConversionWorkspaceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<DeleteConversionWorkspaceRequest,Empty,OperationMetadata> deleteConversionWorkspaceOperationCallable()

Deletes a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteConversionWorkspaceRequest request =
           DeleteConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataMigrationServiceClient
               .deleteConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteConversionWorkspaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteMappingRule(@Nullable ConversionWorkspaceName name)
    
    
    public final void deleteMappingRule(@Nullable ConversionWorkspaceName name)

Deletes a single mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspaceName name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]");
       dataMigrationServiceClient.deleteMappingRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConversionWorkspaceName`  
Required. Name of the mapping rule resource to delete.  
  
### deleteMappingRule(DeleteMappingRuleRequest request)
    
    
    public final void deleteMappingRule(DeleteMappingRuleRequest request)

Deletes a single mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteMappingRuleRequest request =
           DeleteMappingRuleRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       dataMigrationServiceClient.deleteMappingRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteMappingRuleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteMappingRule(String name)
    
    
    public final void deleteMappingRule(String name)

Deletes a single mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
               .toString();
       dataMigrationServiceClient.deleteMappingRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the mapping rule resource to delete.  
  
### deleteMappingRuleCallable()
    
    
    public final UnaryCallable<DeleteMappingRuleRequest,Empty> deleteMappingRuleCallable()

Deletes a single mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteMappingRuleRequest request =
           DeleteMappingRuleRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future =
           dataMigrationServiceClient.deleteMappingRuleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteMappingRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMigrationJobAsync(@Nullable MigrationJobName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMigrationJobAsync(@Nullable MigrationJobName name)

Deletes a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       MigrationJobName name = MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]");
       dataMigrationServiceClient.deleteMigrationJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.MigrationJobName`  
Required. Name of the migration job resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteMigrationJobAsync(DeleteMigrationJobRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMigrationJobAsync(DeleteMigrationJobRequest request)

Deletes a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteMigrationJobRequest request =
           DeleteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       dataMigrationServiceClient.deleteMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteMigrationJobAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMigrationJobAsync(String name)

Deletes a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name = MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString();
       dataMigrationServiceClient.deleteMigrationJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the migration job resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deleteMigrationJobCallable()
    
    
    public final UnaryCallable<DeleteMigrationJobRequest,Operation> deleteMigrationJobCallable()

Deletes a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteMigrationJobRequest request =
           DeleteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.deleteMigrationJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMigrationJobOperationCallable()
    
    
    public final OperationCallable<DeleteMigrationJobRequest,Empty,OperationMetadata> deleteMigrationJobOperationCallable()

Deletes a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeleteMigrationJobRequest request =
           DeleteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataMigrationServiceClient.deleteMigrationJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeleteMigrationJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)

Deletes a single Database Migration Service private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       dataMigrationServiceClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.PrivateConnectionName`  
Required. The name of the private connection to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)

Deletes a single Database Migration Service private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       dataMigrationServiceClient.deletePrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(String name)

Deletes a single Database Migration Service private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       dataMigrationServiceClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the private connection to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionCallable()
    
    
    public final UnaryCallable<DeletePrivateConnectionRequest,Operation> deletePrivateConnectionCallable()

Deletes a single Database Migration Service private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.deletePrivateConnectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeletePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateConnectionOperationCallable()
    
    
    public final OperationCallable<DeletePrivateConnectionRequest,Empty,OperationMetadata> deletePrivateConnectionOperationCallable()

Deletes a single Database Migration Service private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataMigrationServiceClient.deletePrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DeletePrivateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### describeConversionWorkspaceRevisions(DescribeConversionWorkspaceRevisionsRequest request)
    
    
    public final DescribeConversionWorkspaceRevisionsResponse describeConversionWorkspaceRevisions(DescribeConversionWorkspaceRevisionsRequest request)

Retrieves a list of committed revisions of a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DescribeConversionWorkspaceRevisionsRequest request =
           DescribeConversionWorkspaceRevisionsRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setCommitId("commitId-602292046")
               .build();
       DescribeConversionWorkspaceRevisionsResponse response =
           dataMigrationServiceClient.describeConversionWorkspaceRevisions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DescribeConversionWorkspaceRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DescribeConversionWorkspaceRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsResponse)` |   
  
### describeConversionWorkspaceRevisionsCallable()
    
    
    public final UnaryCallable<DescribeConversionWorkspaceRevisionsRequest,DescribeConversionWorkspaceRevisionsResponse> describeConversionWorkspaceRevisionsCallable()

Retrieves a list of committed revisions of a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DescribeConversionWorkspaceRevisionsRequest request =
           DescribeConversionWorkspaceRevisionsRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setCommitId("commitId-602292046")
               .build();
       ApiFuture<DescribeConversionWorkspaceRevisionsResponse> future =
           dataMigrationServiceClient
               .describeConversionWorkspaceRevisionsCallable()
               .futureCall(request);
       // Do something.
       DescribeConversionWorkspaceRevisionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DescribeConversionWorkspaceRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsRequest),[DescribeConversionWorkspaceRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsResponse)>` |   
  
### describeDatabaseEntities(DescribeDatabaseEntitiesRequest request)
    
    
    public final DataMigrationServiceClient.DescribeDatabaseEntitiesPagedResponse describeDatabaseEntities(DescribeDatabaseEntitiesRequest request)

Describes the database entities tree for a specific conversion workspace and a specific tree type.

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DescribeDatabaseEntitiesRequest request =
           DescribeDatabaseEntitiesRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setUncommitted(true)
               .setCommitId("commitId-602292046")
               .setFilter("filter-1274492040")
               .setView(DatabaseEntityView.forNumber(0))
               .build();
       for (DatabaseEntity element :
           dataMigrationServiceClient.describeDatabaseEntities(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DescribeDatabaseEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeDatabaseEntitiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.DescribeDatabaseEntitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.DescribeDatabaseEntitiesPagedResponse)` |   
  
### describeDatabaseEntitiesCallable()
    
    
    public final UnaryCallable<DescribeDatabaseEntitiesRequest,DescribeDatabaseEntitiesResponse> describeDatabaseEntitiesCallable()

Describes the database entities tree for a specific conversion workspace and a specific tree type.

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DescribeDatabaseEntitiesRequest request =
           DescribeDatabaseEntitiesRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setUncommitted(true)
               .setCommitId("commitId-602292046")
               .setFilter("filter-1274492040")
               .setView(DatabaseEntityView.forNumber(0))
               .build();
       while (true) {
         DescribeDatabaseEntitiesResponse response =
             dataMigrationServiceClient.describeDatabaseEntitiesCallable().call(request);
         for (DatabaseEntity element : response.getDatabaseEntitiesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DescribeDatabaseEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeDatabaseEntitiesRequest),[DescribeDatabaseEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeDatabaseEntitiesResponse)>` |   
  
### describeDatabaseEntitiesPagedCallable()
    
    
    public final UnaryCallable<DescribeDatabaseEntitiesRequest,DataMigrationServiceClient.DescribeDatabaseEntitiesPagedResponse> describeDatabaseEntitiesPagedCallable()

Describes the database entities tree for a specific conversion workspace and a specific tree type.

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       DescribeDatabaseEntitiesRequest request =
           DescribeDatabaseEntitiesRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setUncommitted(true)
               .setCommitId("commitId-602292046")
               .setFilter("filter-1274492040")
               .setView(DatabaseEntityView.forNumber(0))
               .build();
       ApiFuture<DatabaseEntity> future =
           dataMigrationServiceClient.describeDatabaseEntitiesPagedCallable().futureCall(request);
       // Do something.
       for (DatabaseEntity element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DescribeDatabaseEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DescribeDatabaseEntitiesRequest),[DescribeDatabaseEntitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.DescribeDatabaseEntitiesPagedResponse)>` |   
  
### fetchStaticIps(@Nullable LocationName name)
    
    
    public final DataMigrationServiceClient.FetchStaticIpsPagedResponse fetchStaticIps(@Nullable LocationName name)

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName name = LocationName.of("[PROJECT]", "[LOCATION]");
       for (String element : dataMigrationServiceClient.fetchStaticIps(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIps(FetchStaticIpsRequest request)
    
    
    public final DataMigrationServiceClient.FetchStaticIpsPagedResponse fetchStaticIps(FetchStaticIpsRequest request)

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : dataMigrationServiceClient.fetchStaticIps(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FetchStaticIpsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIps(String name)
    
    
    public final DataMigrationServiceClient.FetchStaticIpsPagedResponse fetchStaticIps(String name)

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (String element : dataMigrationServiceClient.fetchStaticIps(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIpsCallable()
    
    
    public final UnaryCallable<FetchStaticIpsRequest,FetchStaticIpsResponse> fetchStaticIpsCallable()

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchStaticIpsResponse response =
             dataMigrationServiceClient.fetchStaticIpsCallable().call(request);
         for (String element : response.getStaticIpsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FetchStaticIpsRequest),[FetchStaticIpsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FetchStaticIpsResponse)>` |   
  
### fetchStaticIpsPagedCallable()
    
    
    public final UnaryCallable<FetchStaticIpsRequest,DataMigrationServiceClient.FetchStaticIpsPagedResponse> fetchStaticIpsPagedCallable()

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future =
           dataMigrationServiceClient.fetchStaticIpsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.FetchStaticIpsRequest),[FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.FetchStaticIpsPagedResponse)>` |   
  
### generateSshScript(GenerateSshScriptRequest request)
    
    
    public final SshScript generateSshScript(GenerateSshScriptRequest request)

Generate a SSH configuration script to configure the reverse SSH connectivity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GenerateSshScriptRequest request =
           GenerateSshScriptRequest.newBuilder()
               .setMigrationJob(
                   MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setVm("vm3767")
               .setVmPort(563010825)
               .build();
       SshScript response = dataMigrationServiceClient.generateSshScript(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateSshScriptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GenerateSshScriptRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SshScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SshScript)` |   
  
### generateSshScriptCallable()
    
    
    public final UnaryCallable<GenerateSshScriptRequest,SshScript> generateSshScriptCallable()

Generate a SSH configuration script to configure the reverse SSH connectivity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GenerateSshScriptRequest request =
           GenerateSshScriptRequest.newBuilder()
               .setMigrationJob(
                   MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setVm("vm3767")
               .setVmPort(563010825)
               .build();
       ApiFuture<SshScript> future =
           dataMigrationServiceClient.generateSshScriptCallable().futureCall(request);
       // Do something.
       SshScript response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateSshScriptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GenerateSshScriptRequest),[SshScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SshScript)>` |   
  
### generateTcpProxyScript(GenerateTcpProxyScriptRequest request)
    
    
    public final TcpProxyScript generateTcpProxyScript(GenerateTcpProxyScriptRequest request)

Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GenerateTcpProxyScriptRequest request =
           GenerateTcpProxyScriptRequest.newBuilder()
               .setMigrationJob(
                   MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setVmName("vmName-813643294")
               .setVmMachineType("vmMachineType-1921917718")
               .setVmZone("vmZone-813272317")
               .setVmSubnet("vmSubnet-65857292")
               .build();
       TcpProxyScript response = dataMigrationServiceClient.generateTcpProxyScript(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateTcpProxyScriptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GenerateTcpProxyScriptRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TcpProxyScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.TcpProxyScript)` |   
  
### generateTcpProxyScriptCallable()
    
    
    public final UnaryCallable<GenerateTcpProxyScriptRequest,TcpProxyScript> generateTcpProxyScriptCallable()

Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GenerateTcpProxyScriptRequest request =
           GenerateTcpProxyScriptRequest.newBuilder()
               .setMigrationJob(
                   MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setVmName("vmName-813643294")
               .setVmMachineType("vmMachineType-1921917718")
               .setVmZone("vmZone-813272317")
               .setVmSubnet("vmSubnet-65857292")
               .build();
       ApiFuture<TcpProxyScript> future =
           dataMigrationServiceClient.generateTcpProxyScriptCallable().futureCall(request);
       // Do something.
       TcpProxyScript response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateTcpProxyScriptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GenerateTcpProxyScriptRequest),[TcpProxyScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.TcpProxyScript)>` |   
  
### getConnectionProfile(@Nullable ConnectionProfileName name)
    
    
    public final ConnectionProfile getConnectionProfile(@Nullable ConnectionProfileName name)

Gets details of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConnectionProfileName name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
       ConnectionProfile response = dataMigrationServiceClient.getConnectionProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConnectionProfileName`  
Required. Name of the connection profile resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)` |   
  
### getConnectionProfile(GetConnectionProfileRequest request)
    
    
    public final ConnectionProfile getConnectionProfile(GetConnectionProfileRequest request)

Gets details of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetConnectionProfileRequest request =
           GetConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .build();
       ConnectionProfile response = dataMigrationServiceClient.getConnectionProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)` |   
  
### getConnectionProfile(String name)
    
    
    public final ConnectionProfile getConnectionProfile(String name)

Gets details of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]").toString();
       ConnectionProfile response = dataMigrationServiceClient.getConnectionProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection profile resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)` |   
  
### getConnectionProfileCallable()
    
    
    public final UnaryCallable<GetConnectionProfileRequest,ConnectionProfile> getConnectionProfileCallable()

Gets details of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetConnectionProfileRequest request =
           GetConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .build();
       ApiFuture<ConnectionProfile> future =
           dataMigrationServiceClient.getConnectionProfileCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)>` |   
  
### getConversionWorkspace(@Nullable ConversionWorkspaceName name)
    
    
    public final ConversionWorkspace getConversionWorkspace(@Nullable ConversionWorkspaceName name)

Gets details of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspaceName name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]");
       ConversionWorkspace response = dataMigrationServiceClient.getConversionWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConversionWorkspaceName`  
Required. Name of the conversion workspace resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)` |   
  
### getConversionWorkspace(GetConversionWorkspaceRequest request)
    
    
    public final ConversionWorkspace getConversionWorkspace(GetConversionWorkspaceRequest request)

Gets details of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetConversionWorkspaceRequest request =
           GetConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .build();
       ConversionWorkspace response = dataMigrationServiceClient.getConversionWorkspace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)` |   
  
### getConversionWorkspace(String name)
    
    
    public final ConversionWorkspace getConversionWorkspace(String name)

Gets details of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
               .toString();
       ConversionWorkspace response = dataMigrationServiceClient.getConversionWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the conversion workspace resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)` |   
  
### getConversionWorkspaceCallable()
    
    
    public final UnaryCallable<GetConversionWorkspaceRequest,ConversionWorkspace> getConversionWorkspaceCallable()

Gets details of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetConversionWorkspaceRequest request =
           GetConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<ConversionWorkspace> future =
           dataMigrationServiceClient.getConversionWorkspaceCallable().futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)>` |   
  
### getMappingRule(@Nullable MappingRuleName name)
    
    
    public final MappingRule getMappingRule(@Nullable MappingRuleName name)

Gets the details of a mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       MappingRuleName name =
           MappingRuleName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]", "[MAPPING_RULE]");
       MappingRule response = dataMigrationServiceClient.getMappingRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.MappingRuleName`  
Required. Name of the mapping rule resource to get. Example: conversionWorkspaces/123/mappingRules/rule123 In order to retrieve a previous revision of the mapping rule, also provide the revision ID. Example: conversionWorkspace/123/mappingRules/rule123@c7cfa2a8c7cfa2a8c7cfa2a8c7cfa2a8  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### getMappingRule(GetMappingRuleRequest request)
    
    
    public final MappingRule getMappingRule(GetMappingRuleRequest request)

Gets the details of a mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetMappingRuleRequest request =
           GetMappingRuleRequest.newBuilder()
               .setName(
                   MappingRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]", "[MAPPING_RULE]")
                       .toString())
               .build();
       MappingRule response = dataMigrationServiceClient.getMappingRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetMappingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### getMappingRule(String name)
    
    
    public final MappingRule getMappingRule(String name)

Gets the details of a mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           MappingRuleName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]", "[MAPPING_RULE]")
               .toString();
       MappingRule response = dataMigrationServiceClient.getMappingRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the mapping rule resource to get. Example: conversionWorkspaces/123/mappingRules/rule123 In order to retrieve a previous revision of the mapping rule, also provide the revision ID. Example: conversionWorkspace/123/mappingRules/rule123@c7cfa2a8c7cfa2a8c7cfa2a8c7cfa2a8  
**Returns**  
---  
**Type** | **Description**  
`[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)` |   
  
### getMappingRuleCallable()
    
    
    public final UnaryCallable<GetMappingRuleRequest,MappingRule> getMappingRuleCallable()

Gets the details of a mapping rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetMappingRuleRequest request =
           GetMappingRuleRequest.newBuilder()
               .setName(
                   MappingRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]", "[MAPPING_RULE]")
                       .toString())
               .build();
       ApiFuture<MappingRule> future =
           dataMigrationServiceClient.getMappingRuleCallable().futureCall(request);
       // Do something.
       MappingRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMappingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetMappingRuleRequest),[MappingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MappingRule)>` |   
  
### getMigrationJob(@Nullable MigrationJobName name)
    
    
    public final MigrationJob getMigrationJob(@Nullable MigrationJobName name)

Gets details of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       MigrationJobName name = MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]");
       MigrationJob response = dataMigrationServiceClient.getMigrationJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.MigrationJobName`  
Required. Name of the migration job resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)` |   
  
### getMigrationJob(GetMigrationJobRequest request)
    
    
    public final MigrationJob getMigrationJob(GetMigrationJobRequest request)

Gets details of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetMigrationJobRequest request =
           GetMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       MigrationJob response = dataMigrationServiceClient.getMigrationJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)` |   
  
### getMigrationJob(String name)
    
    
    public final MigrationJob getMigrationJob(String name)

Gets details of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name = MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString();
       MigrationJob response = dataMigrationServiceClient.getMigrationJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the migration job resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)` |   
  
### getMigrationJobCallable()
    
    
    public final UnaryCallable<GetMigrationJobRequest,MigrationJob> getMigrationJobCallable()

Gets details of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetMigrationJobRequest request =
           GetMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       ApiFuture<MigrationJob> future =
           dataMigrationServiceClient.getMigrationJobCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getPrivateConnection(@Nullable PrivateConnectionName name)
    
    
    public final PrivateConnection getPrivateConnection(@Nullable PrivateConnectionName name)

Gets details of a single private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       PrivateConnection response = dataMigrationServiceClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.PrivateConnectionName`  
Required. The name of the private connection to get.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)` |   
  
### getPrivateConnection(GetPrivateConnectionRequest request)
    
    
    public final PrivateConnection getPrivateConnection(GetPrivateConnectionRequest request)

Gets details of a single private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       PrivateConnection response = dataMigrationServiceClient.getPrivateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)` |   
  
### getPrivateConnection(String name)
    
    
    public final PrivateConnection getPrivateConnection(String name)

Gets details of a single private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       PrivateConnection response = dataMigrationServiceClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the private connection to get.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)` |   
  
### getPrivateConnectionCallable()
    
    
    public final UnaryCallable<GetPrivateConnectionRequest,PrivateConnection> getPrivateConnectionCallable()

Gets details of a single private connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       ApiFuture<PrivateConnection> future =
           dataMigrationServiceClient.getPrivateConnectionCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.GetPrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PrivateConnection)>` |   
  
### getSettings()
    
    
    public final @Nullable DataMigrationServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.DataMigrationServiceSettings` |   
  
### getStub()
    
    
    public DataMigrationServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.stub.DataMigrationServiceStub)` |   
  
### importMappingRulesAsync(ImportMappingRulesRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> importMappingRulesAsync(ImportMappingRulesRequest request)

Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ImportMappingRulesRequest request =
           ImportMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRulesFormat(ImportRulesFileFormat.forNumber(0))
               .addAllRulesFiles(new ArrayList<ImportMappingRulesRequest.RulesFile>())
               .setAutoCommit(true)
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.importMappingRulesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ImportMappingRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### importMappingRulesCallable()
    
    
    public final UnaryCallable<ImportMappingRulesRequest,Operation> importMappingRulesCallable()

Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ImportMappingRulesRequest request =
           ImportMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRulesFormat(ImportRulesFileFormat.forNumber(0))
               .addAllRulesFiles(new ArrayList<ImportMappingRulesRequest.RulesFile>())
               .setAutoCommit(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.importMappingRulesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ImportMappingRulesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importMappingRulesOperationCallable()
    
    
    public final OperationCallable<ImportMappingRulesRequest,ConversionWorkspace,OperationMetadata> importMappingRulesOperationCallable()

Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ImportMappingRulesRequest request =
           ImportMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setRulesFormat(ImportRulesFileFormat.forNumber(0))
               .addAllRulesFiles(new ArrayList<ImportMappingRulesRequest.RulesFile>())
               .setAutoCommit(true)
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient.importMappingRulesOperationCallable().futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ImportMappingRulesRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
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
  
### listConnectionProfiles(@Nullable LocationName parent)
    
    
    public final DataMigrationServiceClient.ListConnectionProfilesPagedResponse listConnectionProfiles(@Nullable LocationName parent)

Retrieves a list of all connection profiles in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ConnectionProfile element :
           dataMigrationServiceClient.listConnectionProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of connection profiles.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfiles(ListConnectionProfilesRequest request)
    
    
    public final DataMigrationServiceClient.ListConnectionProfilesPagedResponse listConnectionProfiles(ListConnectionProfilesRequest request)

Retrieves a list of all connection profiles in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ConnectionProfile element :
           dataMigrationServiceClient.listConnectionProfiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConnectionProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfiles(String parent)
    
    
    public final DataMigrationServiceClient.ListConnectionProfilesPagedResponse listConnectionProfiles(String parent)

Retrieves a list of all connection profiles in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ConnectionProfile element :
           dataMigrationServiceClient.listConnectionProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of connection profiles.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfilesCallable()
    
    
    public final UnaryCallable<ListConnectionProfilesRequest,ListConnectionProfilesResponse> listConnectionProfilesCallable()

Retrieves a list of all connection profiles in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListConnectionProfilesResponse response =
             dataMigrationServiceClient.listConnectionProfilesCallable().call(request);
         for (ConnectionProfile element : response.getConnectionProfilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConnectionProfilesRequest),[ListConnectionProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConnectionProfilesResponse)>` |   
  
### listConnectionProfilesPagedCallable()
    
    
    public final UnaryCallable<ListConnectionProfilesRequest,DataMigrationServiceClient.ListConnectionProfilesPagedResponse> listConnectionProfilesPagedCallable()

Retrieves a list of all connection profiles in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ConnectionProfile> future =
           dataMigrationServiceClient.listConnectionProfilesPagedCallable().futureCall(request);
       // Do something.
       for (ConnectionProfile element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConnectionProfilesRequest),[ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConnectionProfilesPagedResponse)>` |   
  
### listConversionWorkspaces(@Nullable LocationName parent)
    
    
    public final DataMigrationServiceClient.ListConversionWorkspacesPagedResponse listConversionWorkspaces(@Nullable LocationName parent)

Lists conversion workspaces in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ConversionWorkspace element :
           dataMigrationServiceClient.listConversionWorkspaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of conversion workspaces.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConversionWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConversionWorkspacesPagedResponse)` |   
  
### listConversionWorkspaces(ListConversionWorkspacesRequest request)
    
    
    public final DataMigrationServiceClient.ListConversionWorkspacesPagedResponse listConversionWorkspaces(ListConversionWorkspacesRequest request)

Lists conversion workspaces in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConversionWorkspacesRequest request =
           ListConversionWorkspacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (ConversionWorkspace element :
           dataMigrationServiceClient.listConversionWorkspaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversionWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConversionWorkspacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConversionWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConversionWorkspacesPagedResponse)` |   
  
### listConversionWorkspaces(String parent)
    
    
    public final DataMigrationServiceClient.ListConversionWorkspacesPagedResponse listConversionWorkspaces(String parent)

Lists conversion workspaces in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ConversionWorkspace element :
           dataMigrationServiceClient.listConversionWorkspaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of conversion workspaces.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListConversionWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConversionWorkspacesPagedResponse)` |   
  
### listConversionWorkspacesCallable()
    
    
    public final UnaryCallable<ListConversionWorkspacesRequest,ListConversionWorkspacesResponse> listConversionWorkspacesCallable()

Lists conversion workspaces in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConversionWorkspacesRequest request =
           ListConversionWorkspacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListConversionWorkspacesResponse response =
             dataMigrationServiceClient.listConversionWorkspacesCallable().call(request);
         for (ConversionWorkspace element : response.getConversionWorkspacesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversionWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConversionWorkspacesRequest),[ListConversionWorkspacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConversionWorkspacesResponse)>` |   
  
### listConversionWorkspacesPagedCallable()
    
    
    public final UnaryCallable<ListConversionWorkspacesRequest,DataMigrationServiceClient.ListConversionWorkspacesPagedResponse> listConversionWorkspacesPagedCallable()

Lists conversion workspaces in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListConversionWorkspacesRequest request =
           ListConversionWorkspacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ConversionWorkspace> future =
           dataMigrationServiceClient.listConversionWorkspacesPagedCallable().futureCall(request);
       // Do something.
       for (ConversionWorkspace element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversionWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListConversionWorkspacesRequest),[ListConversionWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListConversionWorkspacesPagedResponse)>` |   
  
### listMappingRules(@Nullable ConversionWorkspaceName parent)
    
    
    public final DataMigrationServiceClient.ListMappingRulesPagedResponse listMappingRules(@Nullable ConversionWorkspaceName parent)

Lists the mapping rules for a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspaceName parent =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]");
       for (MappingRule element : dataMigrationServiceClient.listMappingRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.ConversionWorkspaceName`  
Required. Name of the conversion workspace resource whose mapping rules are listed in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMappingRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMappingRulesPagedResponse)` |   
  
### listMappingRules(ListMappingRulesRequest request)
    
    
    public final DataMigrationServiceClient.ListMappingRulesPagedResponse listMappingRules(ListMappingRulesRequest request)

Lists the mapping rules for a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMappingRulesRequest request =
           ListMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MappingRule element :
           dataMigrationServiceClient.listMappingRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMappingRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMappingRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMappingRulesPagedResponse)` |   
  
### listMappingRules(String parent)
    
    
    public final DataMigrationServiceClient.ListMappingRulesPagedResponse listMappingRules(String parent)

Lists the mapping rules for a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent =
           ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
               .toString();
       for (MappingRule element : dataMigrationServiceClient.listMappingRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the conversion workspace resource whose mapping rules are listed in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMappingRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMappingRulesPagedResponse)` |   
  
### listMappingRulesCallable()
    
    
    public final UnaryCallable<ListMappingRulesRequest,ListMappingRulesResponse> listMappingRulesCallable()

Lists the mapping rules for a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMappingRulesRequest request =
           ListMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMappingRulesResponse response =
             dataMigrationServiceClient.listMappingRulesCallable().call(request);
         for (MappingRule element : response.getMappingRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMappingRulesRequest),[ListMappingRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMappingRulesResponse)>` |   
  
### listMappingRulesPagedCallable()
    
    
    public final UnaryCallable<ListMappingRulesRequest,DataMigrationServiceClient.ListMappingRulesPagedResponse> listMappingRulesPagedCallable()

Lists the mapping rules for a specific conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMappingRulesRequest request =
           ListMappingRulesRequest.newBuilder()
               .setParent(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MappingRule> future =
           dataMigrationServiceClient.listMappingRulesPagedCallable().futureCall(request);
       // Do something.
       for (MappingRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMappingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMappingRulesRequest),[ListMappingRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMappingRulesPagedResponse)>` |   
  
### listMigrationJobs(@Nullable LocationName parent)
    
    
    public final DataMigrationServiceClient.ListMigrationJobsPagedResponse listMigrationJobs(@Nullable LocationName parent)

Lists migration jobs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MigrationJob element :
           dataMigrationServiceClient.listMigrationJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent which owns this collection of migrationJobs.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMigrationJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMigrationJobsPagedResponse)` |   
  
### listMigrationJobs(ListMigrationJobsRequest request)
    
    
    public final DataMigrationServiceClient.ListMigrationJobsPagedResponse listMigrationJobs(ListMigrationJobsRequest request)

Lists migration jobs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMigrationJobsRequest request =
           ListMigrationJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (MigrationJob element :
           dataMigrationServiceClient.listMigrationJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMigrationJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMigrationJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMigrationJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMigrationJobsPagedResponse)` |   
  
### listMigrationJobs(String parent)
    
    
    public final DataMigrationServiceClient.ListMigrationJobsPagedResponse listMigrationJobs(String parent)

Lists migration jobs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MigrationJob element :
           dataMigrationServiceClient.listMigrationJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent which owns this collection of migrationJobs.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListMigrationJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMigrationJobsPagedResponse)` |   
  
### listMigrationJobsCallable()
    
    
    public final UnaryCallable<ListMigrationJobsRequest,ListMigrationJobsResponse> listMigrationJobsCallable()

Lists migration jobs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMigrationJobsRequest request =
           ListMigrationJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMigrationJobsResponse response =
             dataMigrationServiceClient.listMigrationJobsCallable().call(request);
         for (MigrationJob element : response.getMigrationJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMigrationJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMigrationJobsRequest),[ListMigrationJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMigrationJobsResponse)>` |   
  
### listMigrationJobsPagedCallable()
    
    
    public final UnaryCallable<ListMigrationJobsRequest,DataMigrationServiceClient.ListMigrationJobsPagedResponse> listMigrationJobsPagedCallable()

Lists migration jobs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListMigrationJobsRequest request =
           ListMigrationJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<MigrationJob> future =
           dataMigrationServiceClient.listMigrationJobsPagedCallable().futureCall(request);
       // Do something.
       for (MigrationJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMigrationJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListMigrationJobsRequest),[ListMigrationJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListMigrationJobsPagedResponse)>` |   
  
### listPrivateConnections(@Nullable LocationName parent)
    
    
    public final DataMigrationServiceClient.ListPrivateConnectionsPagedResponse listPrivateConnections(@Nullable LocationName parent)

Retrieves a list of private connections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PrivateConnection element :
           dataMigrationServiceClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.clouddms.v1.LocationName`  
Required. The parent that owns the collection of private connections.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(ListPrivateConnectionsRequest request)
    
    
    public final DataMigrationServiceClient.ListPrivateConnectionsPagedResponse listPrivateConnections(ListPrivateConnectionsRequest request)

Retrieves a list of private connections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PrivateConnection element :
           dataMigrationServiceClient.listPrivateConnections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListPrivateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(String parent)
    
    
    public final DataMigrationServiceClient.ListPrivateConnectionsPagedResponse listPrivateConnections(String parent)

Retrieves a list of private connections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PrivateConnection element :
           dataMigrationServiceClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of private connections.  
**Returns**  
---  
**Type** | **Description**  
`[DataMigrationServiceClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnectionsCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,ListPrivateConnectionsResponse> listPrivateConnectionsCallable()

Retrieves a list of private connections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPrivateConnectionsResponse response =
             dataMigrationServiceClient.listPrivateConnectionsCallable().call(request);
         for (PrivateConnection element : response.getPrivateConnectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListPrivateConnectionsResponse)>` |   
  
### listPrivateConnectionsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,DataMigrationServiceClient.ListPrivateConnectionsPagedResponse> listPrivateConnectionsPagedCallable()

Retrieves a list of private connections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PrivateConnection> future =
           dataMigrationServiceClient.listPrivateConnectionsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateConnection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DataMigrationServiceClient.ListPrivateConnectionsPagedResponse)>` |   
  
### promoteMigrationJobAsync(PromoteMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> promoteMigrationJobAsync(PromoteMigrationJobRequest request)

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       PromoteMigrationJobRequest request =
           PromoteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       MigrationJob response = dataMigrationServiceClient.promoteMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PromoteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PromoteMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### promoteMigrationJobCallable()
    
    
    public final UnaryCallable<PromoteMigrationJobRequest,Operation> promoteMigrationJobCallable()

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       PromoteMigrationJobRequest request =
           PromoteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.promoteMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PromoteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PromoteMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### promoteMigrationJobOperationCallable()
    
    
    public final OperationCallable<PromoteMigrationJobRequest,MigrationJob,OperationMetadata> promoteMigrationJobOperationCallable()

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       PromoteMigrationJobRequest request =
           PromoteMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.promoteMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PromoteMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.PromoteMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### restartMigrationJobAsync(RestartMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> restartMigrationJobAsync(RestartMigrationJobRequest request)

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RestartMigrationJobRequest request =
           RestartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       MigrationJob response = dataMigrationServiceClient.restartMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RestartMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### restartMigrationJobCallable()
    
    
    public final UnaryCallable<RestartMigrationJobRequest,Operation> restartMigrationJobCallable()

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RestartMigrationJobRequest request =
           RestartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.restartMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RestartMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartMigrationJobOperationCallable()
    
    
    public final OperationCallable<RestartMigrationJobRequest,MigrationJob,OperationMetadata> restartMigrationJobOperationCallable()

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RestartMigrationJobRequest request =
           RestartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.restartMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RestartMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### resumeMigrationJobAsync(ResumeMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> resumeMigrationJobAsync(ResumeMigrationJobRequest request)

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ResumeMigrationJobRequest request =
           ResumeMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       MigrationJob response = dataMigrationServiceClient.resumeMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ResumeMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### resumeMigrationJobCallable()
    
    
    public final UnaryCallable<ResumeMigrationJobRequest,Operation> resumeMigrationJobCallable()

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ResumeMigrationJobRequest request =
           ResumeMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.resumeMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ResumeMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resumeMigrationJobOperationCallable()
    
    
    public final OperationCallable<ResumeMigrationJobRequest,MigrationJob,OperationMetadata> resumeMigrationJobOperationCallable()

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ResumeMigrationJobRequest request =
           ResumeMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.resumeMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResumeMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ResumeMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### rollbackConversionWorkspaceAsync(RollbackConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> rollbackConversionWorkspaceAsync(RollbackConversionWorkspaceRequest request)

Rolls back a conversion workspace to the last committed snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RollbackConversionWorkspaceRequest request =
           RollbackConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.rollbackConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RollbackConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RollbackConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### rollbackConversionWorkspaceCallable()
    
    
    public final UnaryCallable<RollbackConversionWorkspaceRequest,Operation> rollbackConversionWorkspaceCallable()

Rolls back a conversion workspace to the last committed snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RollbackConversionWorkspaceRequest request =
           RollbackConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.rollbackConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollbackConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RollbackConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rollbackConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<RollbackConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> rollbackConversionWorkspaceOperationCallable()

Rolls back a conversion workspace to the last committed snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       RollbackConversionWorkspaceRequest request =
           RollbackConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .rollbackConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RollbackConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RollbackConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### searchBackgroundJobs(SearchBackgroundJobsRequest request)
    
    
    public final SearchBackgroundJobsResponse searchBackgroundJobs(SearchBackgroundJobsRequest request)

Searches/lists the background jobs for a specific conversion workspace.

The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       SearchBackgroundJobsRequest request =
           SearchBackgroundJobsRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setReturnMostRecentPerJobType(true)
               .setMaxSize(408072700)
               .setCompletedUntilTime(Timestamp.newBuilder().build())
               .build();
       SearchBackgroundJobsResponse response =
           dataMigrationServiceClient.searchBackgroundJobs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchBackgroundJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SearchBackgroundJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchBackgroundJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SearchBackgroundJobsResponse)` |   
  
### searchBackgroundJobsCallable()
    
    
    public final UnaryCallable<SearchBackgroundJobsRequest,SearchBackgroundJobsResponse> searchBackgroundJobsCallable()

Searches/lists the background jobs for a specific conversion workspace.

The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       SearchBackgroundJobsRequest request =
           SearchBackgroundJobsRequest.newBuilder()
               .setConversionWorkspace(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setReturnMostRecentPerJobType(true)
               .setMaxSize(408072700)
               .setCompletedUntilTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<SearchBackgroundJobsResponse> future =
           dataMigrationServiceClient.searchBackgroundJobsCallable().futureCall(request);
       // Do something.
       SearchBackgroundJobsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchBackgroundJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SearchBackgroundJobsRequest),[SearchBackgroundJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SearchBackgroundJobsResponse)>` |   
  
### seedConversionWorkspaceAsync(SeedConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> seedConversionWorkspaceAsync(SeedConversionWorkspaceRequest request)

Imports a snapshot of the source database into the conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       SeedConversionWorkspaceRequest request =
           SeedConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.seedConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SeedConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SeedConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### seedConversionWorkspaceCallable()
    
    
    public final UnaryCallable<SeedConversionWorkspaceRequest,Operation> seedConversionWorkspaceCallable()

Imports a snapshot of the source database into the conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       SeedConversionWorkspaceRequest request =
           SeedConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.seedConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SeedConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SeedConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### seedConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<SeedConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> seedConversionWorkspaceOperationCallable()

Imports a snapshot of the source database into the conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       SeedConversionWorkspaceRequest request =
           SeedConversionWorkspaceRequest.newBuilder()
               .setName(
                   ConversionWorkspaceName.of("[PROJECT]", "[LOCATION]", "[CONVERSION_WORKSPACE]")
                       .toString())
               .setAutoCommit(true)
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient.seedConversionWorkspaceOperationCallable().futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SeedConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.SeedConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startMigrationJobAsync(StartMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> startMigrationJobAsync(StartMigrationJobRequest request)

Start an already created migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StartMigrationJobRequest request =
           StartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       MigrationJob response = dataMigrationServiceClient.startMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StartMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### startMigrationJobCallable()
    
    
    public final UnaryCallable<StartMigrationJobRequest,Operation> startMigrationJobCallable()

Start an already created migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StartMigrationJobRequest request =
           StartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.startMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StartMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startMigrationJobOperationCallable()
    
    
    public final OperationCallable<StartMigrationJobRequest,MigrationJob,OperationMetadata> startMigrationJobOperationCallable()

Start an already created migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StartMigrationJobRequest request =
           StartMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setSkipValidation(true)
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.startMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StartMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### stopMigrationJobAsync(StopMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> stopMigrationJobAsync(StopMigrationJobRequest request)

Stops a running migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StopMigrationJobRequest request =
           StopMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       MigrationJob response = dataMigrationServiceClient.stopMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StopMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### stopMigrationJobCallable()
    
    
    public final UnaryCallable<StopMigrationJobRequest,Operation> stopMigrationJobCallable()

Stops a running migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StopMigrationJobRequest request =
           StopMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.stopMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StopMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopMigrationJobOperationCallable()
    
    
    public final OperationCallable<StopMigrationJobRequest,MigrationJob,OperationMetadata> stopMigrationJobOperationCallable()

Stops a running migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       StopMigrationJobRequest request =
           StopMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.stopMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.StopMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask)

Update the configuration of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConnectionProfile response =
           dataMigrationServiceClient
               .updateConnectionProfileAsync(connectionProfile, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile)`  
Required. The connection profile parameters to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConnectionProfileAsync(UpdateConnectionProfileRequest request)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> updateConnectionProfileAsync(UpdateConnectionProfileRequest request)

Update the configuration of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       ConnectionProfile response =
           dataMigrationServiceClient.updateConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConnectionProfileCallable()
    
    
    public final UnaryCallable<UpdateConnectionProfileRequest,Operation> updateConnectionProfileCallable()

Update the configuration of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.updateConnectionProfileCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateConnectionProfileOperationCallable()
    
    
    public final OperationCallable<UpdateConnectionProfileRequest,ConnectionProfile,OperationMetadata> updateConnectionProfileOperationCallable()

Update the configuration of a single connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setSkipValidation(true)
               .build();
       OperationFuture<ConnectionProfile, OperationMetadata> future =
           dataMigrationServiceClient.updateConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConversionWorkspaceAsync(ConversionWorkspace conversionWorkspace, FieldMask updateMask)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> updateConversionWorkspaceAsync(ConversionWorkspace conversionWorkspace, FieldMask updateMask)

Updates the parameters of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       ConversionWorkspace conversionWorkspace = ConversionWorkspace.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConversionWorkspace response =
           dataMigrationServiceClient
               .updateConversionWorkspaceAsync(conversionWorkspace, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`conversionWorkspace` | `[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace)`  
Required. The conversion workspace parameters to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConversionWorkspaceAsync(UpdateConversionWorkspaceRequest request)
    
    
    public final OperationFuture<ConversionWorkspace,OperationMetadata> updateConversionWorkspaceAsync(UpdateConversionWorkspaceRequest request)

Updates the parameters of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConversionWorkspaceRequest request =
           UpdateConversionWorkspaceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ConversionWorkspace response =
           dataMigrationServiceClient.updateConversionWorkspaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConversionWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateConversionWorkspaceCallable()
    
    
    public final UnaryCallable<UpdateConversionWorkspaceRequest,Operation> updateConversionWorkspaceCallable()

Updates the parameters of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConversionWorkspaceRequest request =
           UpdateConversionWorkspaceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.updateConversionWorkspaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConversionWorkspaceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateConversionWorkspaceOperationCallable()
    
    
    public final OperationCallable<UpdateConversionWorkspaceRequest,ConversionWorkspace,OperationMetadata> updateConversionWorkspaceOperationCallable()

Updates the parameters of a single conversion workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateConversionWorkspaceRequest request =
           UpdateConversionWorkspaceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConversionWorkspace(ConversionWorkspace.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ConversionWorkspace, OperationMetadata> future =
           dataMigrationServiceClient
               .updateConversionWorkspaceOperationCallable()
               .futureCall(request);
       // Do something.
       ConversionWorkspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateConversionWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateConversionWorkspaceRequest),[ConversionWorkspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ConversionWorkspace),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateMigrationJobAsync(MigrationJob migrationJob, FieldMask updateMask)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> updateMigrationJobAsync(MigrationJob migrationJob, FieldMask updateMask)

Updates the parameters of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       MigrationJob migrationJob = MigrationJob.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MigrationJob response =
           dataMigrationServiceClient.updateMigrationJobAsync(migrationJob, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`migrationJob` | `[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob)`  
Required. The migration job parameters to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateMigrationJobAsync(UpdateMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> updateMigrationJobAsync(UpdateMigrationJobRequest request)

Updates the parameters of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateMigrationJobRequest request =
           UpdateMigrationJobRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MigrationJob response = dataMigrationServiceClient.updateMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### updateMigrationJobCallable()
    
    
    public final UnaryCallable<UpdateMigrationJobRequest,Operation> updateMigrationJobCallable()

Updates the parameters of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateMigrationJobRequest request =
           UpdateMigrationJobRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.updateMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMigrationJobOperationCallable()
    
    
    public final OperationCallable<UpdateMigrationJobRequest,MigrationJob,OperationMetadata> updateMigrationJobOperationCallable()

Updates the parameters of a single migration job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       UpdateMigrationJobRequest request =
           UpdateMigrationJobRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.updateMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.UpdateMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### verifyMigrationJobAsync(VerifyMigrationJobRequest request)
    
    
    public final OperationFuture<MigrationJob,OperationMetadata> verifyMigrationJobAsync(VerifyMigrationJobRequest request)

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       VerifyMigrationJobRequest request =
           VerifyMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .build();
       MigrationJob response = dataMigrationServiceClient.verifyMigrationJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[VerifyMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.VerifyMigrationJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
### verifyMigrationJobCallable()
    
    
    public final UnaryCallable<VerifyMigrationJobRequest,Operation> verifyMigrationJobCallable()

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       VerifyMigrationJobRequest request =
           VerifyMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           dataMigrationServiceClient.verifyMigrationJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[VerifyMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.VerifyMigrationJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### verifyMigrationJobOperationCallable()
    
    
    public final OperationCallable<VerifyMigrationJobRequest,MigrationJob,OperationMetadata> verifyMigrationJobOperationCallable()

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataMigrationServiceClient dataMigrationServiceClient =
         DataMigrationServiceClient.create()) {
       VerifyMigrationJobRequest request =
           VerifyMigrationJobRequest.newBuilder()
               .setName(MigrationJobName.of("[PROJECT]", "[LOCATION]", "[MIGRATION_JOB]").toString())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMigrationJob(MigrationJob.newBuilder().build())
               .build();
       OperationFuture<MigrationJob, OperationMetadata> future =
           dataMigrationServiceClient.verifyMigrationJobOperationCallable().futureCall(request);
       // Do something.
       MigrationJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[VerifyMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.VerifyMigrationJobRequest),[MigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
