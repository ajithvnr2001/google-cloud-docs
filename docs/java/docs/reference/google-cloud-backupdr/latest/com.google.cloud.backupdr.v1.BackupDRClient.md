---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient
title: Class BackupDRClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:55.312211+00:00
---

# Class BackupDRClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackupDRClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-backupdr/google-cloud-backupdr/src/main/java/com/google/cloud/backupdr/v1/BackupDRClient.java)| [Product Reference](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)  
---|---  
  
Service Description: The BackupDR Service

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ManagementServerName name =
           ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]");
       ManagementServer response = backupDRClient.getManagementServer(name);
     }
     

Note: close() needs to be called on the BackupDRClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListManagementServers |  Lists ManagementServers in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listManagementServers(ListManagementServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listManagementServers(LocationName parent) 
  * listManagementServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listManagementServersPagedCallable() 
  * listManagementServersCallable() 

  
GetManagementServer |  Gets details of a single ManagementServer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getManagementServer(GetManagementServerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getManagementServer(ManagementServerName name) 
  * getManagementServer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getManagementServerCallable() 

  
CreateManagementServer |  Creates a new ManagementServer in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createManagementServerAsync(CreateManagementServerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createManagementServerAsync(LocationName parent, ManagementServer managementServer, String managementServerId) 
  * createManagementServerAsync(String parent, ManagementServer managementServer, String managementServerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createManagementServerOperationCallable() 
  * createManagementServerCallable() 

  
DeleteManagementServer |  Deletes a single ManagementServer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteManagementServerAsync(DeleteManagementServerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteManagementServerAsync(ManagementServerName name) 
  * deleteManagementServerAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteManagementServerOperationCallable() 
  * deleteManagementServerCallable() 

  
CreateBackupVault |  Creates a new BackupVault in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupVaultAsync(CreateBackupVaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackupVaultAsync(LocationName parent, BackupVault backupVault, String backupVaultId) 
  * createBackupVaultAsync(String parent, BackupVault backupVault, String backupVaultId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupVaultOperationCallable() 
  * createBackupVaultCallable() 

  
ListBackupVaults |  Lists BackupVaults in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupVaults(ListBackupVaultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupVaults(LocationName parent) 
  * listBackupVaults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupVaultsPagedCallable() 
  * listBackupVaultsCallable() 

  
FetchUsableBackupVaults |  FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchUsableBackupVaults(LocationName parent) 
  * fetchUsableBackupVaults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchUsableBackupVaultsPagedCallable() 
  * fetchUsableBackupVaultsCallable() 

  
GetBackupVault |  Gets details of a BackupVault. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupVault(GetBackupVaultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupVault(BackupVaultName name) 
  * getBackupVault(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupVaultCallable() 

  
UpdateBackupVault |  Updates the settings of a BackupVault. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupVaultAsync(UpdateBackupVaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackupVaultAsync(BackupVault backupVault, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupVaultOperationCallable() 
  * updateBackupVaultCallable() 

  
DeleteBackupVault |  Deletes a BackupVault. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupVaultAsync(DeleteBackupVaultRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupVaultAsync(BackupVaultName name) 
  * deleteBackupVaultAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupVaultOperationCallable() 
  * deleteBackupVaultCallable() 

  
ListDataSources |  Lists DataSources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataSources(ListDataSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataSources(BackupVaultName parent) 
  * listDataSources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataSourcesPagedCallable() 
  * listDataSourcesCallable() 

  
GetDataSource |  Gets details of a DataSource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataSource(GetDataSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataSource(DataSourceName name) 
  * getDataSource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataSourceCallable() 

  
UpdateDataSource |  Updates the settings of a DataSource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataSourceAsync(UpdateDataSourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataSourceAsync(DataSource dataSource, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataSourceOperationCallable() 
  * updateDataSourceCallable() 

  
ListBackups |  Lists Backups in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(DataSourceName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsPagedCallable() 
  * listBackupsCallable() 

  
FetchBackupsForResourceType |  Fetch Backups for a given resource type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchBackupsForResourceType(DataSourceName parent, String resourceType) 
  * fetchBackupsForResourceType(String parent, String resourceType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchBackupsForResourceTypePagedCallable() 
  * fetchBackupsForResourceTypeCallable() 

  
GetBackup |  Gets details of a Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
UpdateBackup |  Updates the settings of a Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupAsync(UpdateBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackupAsync(Backup backup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupOperationCallable() 
  * updateBackupCallable() 

  
DeleteBackup |  Deletes a Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupAsync(DeleteBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupAsync(BackupName name) 
  * deleteBackupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupOperationCallable() 
  * deleteBackupCallable() 

  
RestoreBackup |  Restore from a Backup |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreBackupAsync(RestoreBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreBackupAsync(BackupName name) 
  * restoreBackupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreBackupOperationCallable() 
  * restoreBackupCallable() 

  
CreateBackupPlan |  Create a BackupPlan |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupPlanAsync(CreateBackupPlanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackupPlanAsync(LocationName parent, BackupPlan backupPlan, String backupPlanId) 
  * createBackupPlanAsync(String parent, BackupPlan backupPlan, String backupPlanId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupPlanOperationCallable() 
  * createBackupPlanCallable() 

  
UpdateBackupPlan |  Update a BackupPlan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupPlanAsync(UpdateBackupPlanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackupPlanAsync(BackupPlan backupPlan, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupPlanOperationCallable() 
  * updateBackupPlanCallable() 

  
GetBackupPlan |  Gets details of a single BackupPlan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupPlan(GetBackupPlanRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupPlan(BackupPlanName name) 
  * getBackupPlan(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupPlanCallable() 

  
ListBackupPlans |  Lists BackupPlans in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupPlans(ListBackupPlansRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupPlans(LocationName parent) 
  * listBackupPlans(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupPlansPagedCallable() 
  * listBackupPlansCallable() 

  
DeleteBackupPlan |  Deletes a single BackupPlan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupPlanAsync(DeleteBackupPlanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupPlanAsync(BackupPlanName name) 
  * deleteBackupPlanAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupPlanOperationCallable() 
  * deleteBackupPlanCallable() 

  
GetBackupPlanRevision |  Gets details of a single BackupPlanRevision. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupPlanRevision(GetBackupPlanRevisionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupPlanRevision(BackupPlanRevisionName name) 
  * getBackupPlanRevision(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupPlanRevisionCallable() 

  
ListBackupPlanRevisions |  Lists BackupPlanRevisions in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupPlanRevisions(ListBackupPlanRevisionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupPlanRevisions(BackupPlanName parent) 
  * listBackupPlanRevisions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupPlanRevisionsPagedCallable() 
  * listBackupPlanRevisionsCallable() 

  
CreateBackupPlanAssociation |  Create a BackupPlanAssociation |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupPlanAssociationAsync(CreateBackupPlanAssociationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackupPlanAssociationAsync(LocationName parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId) 
  * createBackupPlanAssociationAsync(String parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupPlanAssociationOperationCallable() 
  * createBackupPlanAssociationCallable() 

  
UpdateBackupPlanAssociation |  Update a BackupPlanAssociation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupPlanAssociationAsync(UpdateBackupPlanAssociationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackupPlanAssociationAsync(BackupPlanAssociation backupPlanAssociation, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupPlanAssociationOperationCallable() 
  * updateBackupPlanAssociationCallable() 

  
GetBackupPlanAssociation |  Gets details of a single BackupPlanAssociation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupPlanAssociation(GetBackupPlanAssociationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupPlanAssociation(BackupPlanAssociationName name) 
  * getBackupPlanAssociation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupPlanAssociationCallable() 

  
ListBackupPlanAssociations |  Lists BackupPlanAssociations in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupPlanAssociations(ListBackupPlanAssociationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupPlanAssociations(LocationName parent) 
  * listBackupPlanAssociations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupPlanAssociationsPagedCallable() 
  * listBackupPlanAssociationsCallable() 

  
FetchBackupPlanAssociationsForResourceType |  List BackupPlanAssociations for a given resource type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchBackupPlanAssociationsForResourceType(LocationName parent, String resourceType) 
  * fetchBackupPlanAssociationsForResourceType(String parent, String resourceType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchBackupPlanAssociationsForResourceTypePagedCallable() 
  * fetchBackupPlanAssociationsForResourceTypeCallable() 

  
DeleteBackupPlanAssociation |  Deletes a single BackupPlanAssociation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupPlanAssociationAsync(DeleteBackupPlanAssociationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupPlanAssociationAsync(BackupPlanAssociationName name) 
  * deleteBackupPlanAssociationAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupPlanAssociationOperationCallable() 
  * deleteBackupPlanAssociationCallable() 

  
TriggerBackup |  Triggers a new Backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * triggerBackupAsync(TriggerBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * triggerBackupAsync(BackupPlanAssociationName name, String ruleId) 
  * triggerBackupAsync(String name, String ruleId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * triggerBackupOperationCallable() 
  * triggerBackupCallable() 

  
GetDataSourceReference |  Gets details of a single DataSourceReference. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataSourceReference(GetDataSourceReferenceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataSourceReference(DataSourceReferenceName name) 
  * getDataSourceReference(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataSourceReferenceCallable() 

  
ListDataSourceReferences |  Lists DataSourceReferences for a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataSourceReferences(ListDataSourceReferencesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataSourceReferences(LocationName parent) 
  * listDataSourceReferences(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataSourceReferencesPagedCallable() 
  * listDataSourceReferencesCallable() 

  
FetchDataSourceReferencesForResourceType |  Fetch DataSourceReferences for a given project, location and resource type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchDataSourceReferencesForResourceType(LocationName parent, String resourceType) 
  * fetchDataSourceReferencesForResourceType(String parent, String resourceType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchDataSourceReferencesForResourceTypePagedCallable() 
  * fetchDataSourceReferencesForResourceTypeCallable() 

  
InitializeService |  Initializes the service related config for a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * initializeServiceAsync(InitializeServiceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * initializeServiceOperationCallable() 
  * initializeServiceCallable() 

  
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

This class can be customized by passing in a custom instance of BackupDRSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackupDRSettings backupDRSettings =
         BackupDRSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BackupDRClient backupDRClient = BackupDRClient.create(backupDRSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackupDRSettings backupDRSettings =
         BackupDRSettings.newBuilder().setEndpoint(myEndpoint).build();
     BackupDRClient backupDRClient = BackupDRClient.create(backupDRSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackupDRSettings backupDRSettings = BackupDRSettings.newHttpJsonBuilder().build();
     BackupDRClient backupDRClient = BackupDRClient.create(backupDRSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BackupDRClient

## Static Methods 

### create()
    
    
    public static final BackupDRClient create()

Constructs an instance of BackupDRClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackupDRSettings settings)
    
    
    public static final BackupDRClient create(BackupDRSettings settings)

Constructs an instance of BackupDRClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackupDRSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackupDRStub stub)
    
    
    public static final BackupDRClient create(BackupDRStub stub)

Constructs an instance of BackupDRClient, using the given stub for making calls. This is for advanced usage - prefer using create(BackupDRSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackupDRStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.stub.BackupDRStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient)` |   
  
## Constructors 

### BackupDRClient(BackupDRSettings settings)
    
    
    protected BackupDRClient(BackupDRSettings settings)

Constructs an instance of BackupDRClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackupDRSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRSettings)`  
  
  
### BackupDRClient(BackupDRStub stub)
    
    
    protected BackupDRClient(BackupDRStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackupDRStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.stub.BackupDRStub)`  
  
  
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

### createBackupPlanAssociationAsync(@Nullable LocationName parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> createBackupPlanAssociationAsync(@Nullable LocationName parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId)

Create a BackupPlanAssociation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BackupPlanAssociation backupPlanAssociation = BackupPlanAssociation.newBuilder().build();
       String backupPlanAssociationId = "backupPlanAssociationId567762737";
       BackupPlanAssociation response =
           backupDRClient
               .createBackupPlanAssociationAsync(
                   parent, backupPlanAssociation, backupPlanAssociationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The backup plan association project and location in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**.  
`backupPlanAssociation` | `[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)`  
Required. The resource being created  
`backupPlanAssociationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup plan association to create. The name must be unique for the specified project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAssociationAsync(CreateBackupPlanAssociationRequest request)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> createBackupPlanAssociationAsync(CreateBackupPlanAssociationRequest request)

Create a BackupPlanAssociation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanAssociationRequest request =
           CreateBackupPlanAssociationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanAssociationId("backupPlanAssociationId567762737")
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       BackupPlanAssociation response =
           backupDRClient.createBackupPlanAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanAssociationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAssociationAsync(String parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> createBackupPlanAssociationAsync(String parent, BackupPlanAssociation backupPlanAssociation, String backupPlanAssociationId)

Create a BackupPlanAssociation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BackupPlanAssociation backupPlanAssociation = BackupPlanAssociation.newBuilder().build();
       String backupPlanAssociationId = "backupPlanAssociationId567762737";
       BackupPlanAssociation response =
           backupDRClient
               .createBackupPlanAssociationAsync(
                   parent, backupPlanAssociation, backupPlanAssociationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The backup plan association project and location in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**.  
`backupPlanAssociation` | `[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)`  
Required. The resource being created  
`backupPlanAssociationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup plan association to create. The name must be unique for the specified project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAssociationCallable()
    
    
    public final UnaryCallable<CreateBackupPlanAssociationRequest,Operation> createBackupPlanAssociationCallable()

Create a BackupPlanAssociation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanAssociationRequest request =
           CreateBackupPlanAssociationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanAssociationId("backupPlanAssociationId567762737")
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backupDRClient.createBackupPlanAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanAssociationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupPlanAssociationOperationCallable()
    
    
    public final OperationCallable<CreateBackupPlanAssociationRequest,BackupPlanAssociation,OperationMetadata> createBackupPlanAssociationOperationCallable()

Create a BackupPlanAssociation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanAssociationRequest request =
           CreateBackupPlanAssociationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanAssociationId("backupPlanAssociationId567762737")
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BackupPlanAssociation, OperationMetadata> future =
           backupDRClient.createBackupPlanAssociationOperationCallable().futureCall(request);
       // Do something.
       BackupPlanAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanAssociationRequest),[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAsync(@Nullable LocationName parent, BackupPlan backupPlan, String backupPlanId)
    
    
    public final OperationFuture<BackupPlan,OperationMetadata> createBackupPlanAsync(@Nullable LocationName parent, BackupPlan backupPlan, String backupPlanId)

Create a BackupPlan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BackupPlan backupPlan = BackupPlan.newBuilder().build();
       String backupPlanId = "backupPlanId-84871546";
       BackupPlan response =
           backupDRClient.createBackupPlanAsync(parent, backupPlan, backupPlanId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The `BackupPlan` project and location in the format `projects/{project}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**.  
`backupPlan` | `[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)`  
Required. The `BackupPlan` resource object to create.  
`backupPlanId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `BackupPlan` to create. The name must be unique for the specified project and location.The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /a-z{,62}/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAsync(CreateBackupPlanRequest request)
    
    
    public final OperationFuture<BackupPlan,OperationMetadata> createBackupPlanAsync(CreateBackupPlanRequest request)

Create a BackupPlan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanRequest request =
           CreateBackupPlanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanId("backupPlanId-84871546")
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       BackupPlan response = backupDRClient.createBackupPlanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanAsync(String parent, BackupPlan backupPlan, String backupPlanId)
    
    
    public final OperationFuture<BackupPlan,OperationMetadata> createBackupPlanAsync(String parent, BackupPlan backupPlan, String backupPlanId)

Create a BackupPlan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BackupPlan backupPlan = BackupPlan.newBuilder().build();
       String backupPlanId = "backupPlanId-84871546";
       BackupPlan response =
           backupDRClient.createBackupPlanAsync(parent, backupPlan, backupPlanId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The `BackupPlan` project and location in the format `projects/{project}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**.  
`backupPlan` | `[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)`  
Required. The `BackupPlan` resource object to create.  
`backupPlanId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `BackupPlan` to create. The name must be unique for the specified project and location.The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /a-z{,62}/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupPlanCallable()
    
    
    public final UnaryCallable<CreateBackupPlanRequest,Operation> createBackupPlanCallable()

Create a BackupPlan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanRequest request =
           CreateBackupPlanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanId("backupPlanId-84871546")
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.createBackupPlanCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupPlanOperationCallable()
    
    
    public final OperationCallable<CreateBackupPlanRequest,BackupPlan,OperationMetadata> createBackupPlanOperationCallable()

Create a BackupPlan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupPlanRequest request =
           CreateBackupPlanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupPlanId("backupPlanId-84871546")
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BackupPlan, OperationMetadata> future =
           backupDRClient.createBackupPlanOperationCallable().futureCall(request);
       // Do something.
       BackupPlan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupVaultAsync(@Nullable LocationName parent, BackupVault backupVault, String backupVaultId)
    
    
    public final OperationFuture<BackupVault,OperationMetadata> createBackupVaultAsync(@Nullable LocationName parent, BackupVault backupVault, String backupVaultId)

Creates a new BackupVault in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BackupVault backupVault = BackupVault.newBuilder().build();
       String backupVaultId = "backupVaultId-1897432373";
       BackupVault response =
           backupDRClient.createBackupVaultAsync(parent, backupVault, backupVaultId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. Value for parent.  
`backupVault` | `[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)`  
Required. The resource being created  
`backupVaultId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object If auto-generating ID server-side, remove this field and backup_vault_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupVaultAsync(CreateBackupVaultRequest request)
    
    
    public final OperationFuture<BackupVault,OperationMetadata> createBackupVaultAsync(CreateBackupVaultRequest request)

Creates a new BackupVault in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupVaultRequest request =
           CreateBackupVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupVaultId("backupVaultId-1897432373")
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       BackupVault response = backupDRClient.createBackupVaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupVaultAsync(String parent, BackupVault backupVault, String backupVaultId)
    
    
    public final OperationFuture<BackupVault,OperationMetadata> createBackupVaultAsync(String parent, BackupVault backupVault, String backupVaultId)

Creates a new BackupVault in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BackupVault backupVault = BackupVault.newBuilder().build();
       String backupVaultId = "backupVaultId-1897432373";
       BackupVault response =
           backupDRClient.createBackupVaultAsync(parent, backupVault, backupVaultId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`backupVault` | `[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)`  
Required. The resource being created  
`backupVaultId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object If auto-generating ID server-side, remove this field and backup_vault_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createBackupVaultCallable()
    
    
    public final UnaryCallable<CreateBackupVaultRequest,Operation> createBackupVaultCallable()

Creates a new BackupVault in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupVaultRequest request =
           CreateBackupVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupVaultId("backupVaultId-1897432373")
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = backupDRClient.createBackupVaultCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupVaultOperationCallable()
    
    
    public final OperationCallable<CreateBackupVaultRequest,BackupVault,OperationMetadata> createBackupVaultOperationCallable()

Creates a new BackupVault in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateBackupVaultRequest request =
           CreateBackupVaultRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackupVaultId("backupVaultId-1897432373")
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<BackupVault, OperationMetadata> future =
           backupDRClient.createBackupVaultOperationCallable().futureCall(request);
       // Do something.
       BackupVault response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateBackupVaultRequest),[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createManagementServerAsync(@Nullable LocationName parent, ManagementServer managementServer, String managementServerId)
    
    
    public final OperationFuture<ManagementServer,OperationMetadata> createManagementServerAsync(@Nullable LocationName parent, ManagementServer managementServer, String managementServerId)

Creates a new ManagementServer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ManagementServer managementServer = ManagementServer.newBuilder().build();
       String managementServerId = "managementServerId-1229628127";
       ManagementServer response =
           backupDRClient
               .createManagementServerAsync(parent, managementServer, managementServerId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**.  
`managementServer` | `[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)`  
Required. A management server resource  
`managementServerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the management server to create. The name must be unique for the specified project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createManagementServerAsync(CreateManagementServerRequest request)
    
    
    public final OperationFuture<ManagementServer,OperationMetadata> createManagementServerAsync(CreateManagementServerRequest request)

Creates a new ManagementServer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateManagementServerRequest request =
           CreateManagementServerRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setManagementServerId("managementServerId-1229628127")
               .setManagementServer(ManagementServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ManagementServer response = backupDRClient.createManagementServerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateManagementServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createManagementServerAsync(String parent, ManagementServer managementServer, String managementServerId)
    
    
    public final OperationFuture<ManagementServer,OperationMetadata> createManagementServerAsync(String parent, ManagementServer managementServer, String managementServerId)

Creates a new ManagementServer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ManagementServer managementServer = ManagementServer.newBuilder().build();
       String managementServerId = "managementServerId-1229628127";
       ManagementServer response =
           backupDRClient
               .createManagementServerAsync(parent, managementServer, managementServerId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**.  
`managementServer` | `[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)`  
Required. A management server resource  
`managementServerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the management server to create. The name must be unique for the specified project and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### createManagementServerCallable()
    
    
    public final UnaryCallable<CreateManagementServerRequest,Operation> createManagementServerCallable()

Creates a new ManagementServer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateManagementServerRequest request =
           CreateManagementServerRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setManagementServerId("managementServerId-1229628127")
               .setManagementServer(ManagementServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backupDRClient.createManagementServerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateManagementServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createManagementServerOperationCallable()
    
    
    public final OperationCallable<CreateManagementServerRequest,ManagementServer,OperationMetadata> createManagementServerOperationCallable()

Creates a new ManagementServer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       CreateManagementServerRequest request =
           CreateManagementServerRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setManagementServerId("managementServerId-1229628127")
               .setManagementServer(ManagementServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ManagementServer, OperationMetadata> future =
           backupDRClient.createManagementServerOperationCallable().futureCall(request);
       // Do something.
       ManagementServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.CreateManagementServerRequest),[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(@Nullable BackupName name)
    
    
    public final OperationFuture<Backup,OperationMetadata> deleteBackupAsync(@Nullable BackupName name)

Deletes a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupName name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]");
       Backup response = backupDRClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(DeleteBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> deleteBackupAsync(DeleteBackupRequest request)

Deletes a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       Backup response = backupDRClient.deleteBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(String name)
    
    
    public final OperationFuture<Backup,OperationMetadata> deleteBackupAsync(String name)

Deletes a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
               .toString();
       Backup response = backupDRClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Operation> deleteBackupCallable()

Deletes a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.deleteBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupOperationCallable()
    
    
    public final OperationCallable<DeleteBackupRequest,Backup,OperationMetadata> deleteBackupOperationCallable()

Deletes a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           backupDRClient.deleteBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAssociationAsync(@Nullable BackupPlanAssociationName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAssociationAsync(@Nullable BackupPlanAssociationName name)

Deletes a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanAssociationName name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]");
       backupDRClient.deleteBackupPlanAssociationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanAssociationName`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAssociationAsync(DeleteBackupPlanAssociationRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAssociationAsync(DeleteBackupPlanAssociationRequest request)

Deletes a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanAssociationRequest request =
           DeleteBackupPlanAssociationRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       backupDRClient.deleteBackupPlanAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanAssociationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAssociationAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAssociationAsync(String name)

Deletes a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
               .toString();
       backupDRClient.deleteBackupPlanAssociationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAssociationCallable()
    
    
    public final UnaryCallable<DeleteBackupPlanAssociationRequest,Operation> deleteBackupPlanAssociationCallable()

Deletes a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanAssociationRequest request =
           DeleteBackupPlanAssociationRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backupDRClient.deleteBackupPlanAssociationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanAssociationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupPlanAssociationOperationCallable()
    
    
    public final OperationCallable<DeleteBackupPlanAssociationRequest,Empty,OperationMetadata> deleteBackupPlanAssociationOperationCallable()

Deletes a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanAssociationRequest request =
           DeleteBackupPlanAssociationRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           backupDRClient.deleteBackupPlanAssociationOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanAssociationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAsync(@Nullable BackupPlanName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAsync(@Nullable BackupPlanName name)

Deletes a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanName name = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]");
       backupDRClient.deleteBackupPlanAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanName`  
Required. The resource name of the `BackupPlan` to delete. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAsync(DeleteBackupPlanRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAsync(DeleteBackupPlanRequest request)

Deletes a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanRequest request =
           DeleteBackupPlanRequest.newBuilder()
               .setName(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setRequestId("requestId693933066")
               .build();
       backupDRClient.deleteBackupPlanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupPlanAsync(String name)

Deletes a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString();
       backupDRClient.deleteBackupPlanAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the `BackupPlan` to delete. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupPlanCallable()
    
    
    public final UnaryCallable<DeleteBackupPlanRequest,Operation> deleteBackupPlanCallable()

Deletes a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanRequest request =
           DeleteBackupPlanRequest.newBuilder()
               .setName(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.deleteBackupPlanCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupPlanOperationCallable()
    
    
    public final OperationCallable<DeleteBackupPlanRequest,Empty,OperationMetadata> deleteBackupPlanOperationCallable()

Deletes a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupPlanRequest request =
           DeleteBackupPlanRequest.newBuilder()
               .setName(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           backupDRClient.deleteBackupPlanOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupPlanRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupVaultAsync(@Nullable BackupVaultName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupVaultAsync(@Nullable BackupVaultName name)

Deletes a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupVaultName name = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]");
       backupDRClient.deleteBackupVaultAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupVaultName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupVaultAsync(DeleteBackupVaultRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupVaultAsync(DeleteBackupVaultRequest request)

Deletes a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupVaultRequest request =
           DeleteBackupVaultRequest.newBuilder()
               .setName(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setIgnoreBackupPlanReferences(true)
               .build();
       backupDRClient.deleteBackupVaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupVaultAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupVaultAsync(String name)

Deletes a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString();
       backupDRClient.deleteBackupVaultAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteBackupVaultCallable()
    
    
    public final UnaryCallable<DeleteBackupVaultRequest,Operation> deleteBackupVaultCallable()

Deletes a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupVaultRequest request =
           DeleteBackupVaultRequest.newBuilder()
               .setName(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setIgnoreBackupPlanReferences(true)
               .build();
       ApiFuture<Operation> future = backupDRClient.deleteBackupVaultCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupVaultOperationCallable()
    
    
    public final OperationCallable<DeleteBackupVaultRequest,Empty,OperationMetadata> deleteBackupVaultOperationCallable()

Deletes a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteBackupVaultRequest request =
           DeleteBackupVaultRequest.newBuilder()
               .setName(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setIgnoreBackupPlanReferences(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           backupDRClient.deleteBackupVaultOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteBackupVaultRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteManagementServerAsync(@Nullable ManagementServerName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementServerAsync(@Nullable ManagementServerName name)

Deletes a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ManagementServerName name =
           ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]");
       backupDRClient.deleteManagementServerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.ManagementServerName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteManagementServerAsync(DeleteManagementServerRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementServerAsync(DeleteManagementServerRequest request)

Deletes a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteManagementServerRequest request =
           DeleteManagementServerRequest.newBuilder()
               .setName(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       backupDRClient.deleteManagementServerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteManagementServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteManagementServerAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementServerAsync(String name)

Deletes a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]").toString();
       backupDRClient.deleteManagementServerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### deleteManagementServerCallable()
    
    
    public final UnaryCallable<DeleteManagementServerRequest,Operation> deleteManagementServerCallable()

Deletes a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteManagementServerRequest request =
           DeleteManagementServerRequest.newBuilder()
               .setName(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backupDRClient.deleteManagementServerCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteManagementServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteManagementServerOperationCallable()
    
    
    public final OperationCallable<DeleteManagementServerRequest,Empty,OperationMetadata> deleteManagementServerOperationCallable()

Deletes a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DeleteManagementServerRequest request =
           DeleteManagementServerRequest.newBuilder()
               .setName(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           backupDRClient.deleteManagementServerOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DeleteManagementServerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### fetchBackupPlanAssociationsForResourceType(@Nullable LocationName parent, String resourceType)
    
    
    public final BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse fetchBackupPlanAssociationsForResourceType(@Nullable LocationName parent, String resourceType)

List BackupPlanAssociations for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String resourceType = "resourceType-384364440";
       for (BackupPlanAssociation element :
           backupDRClient
               .fetchBackupPlanAssociationsForResourceType(parent, resourceType)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse)` |   
  
### fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request)
    
    
    public final BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request)

List BackupPlanAssociations for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupPlanAssociationsForResourceTypeRequest request =
           FetchBackupPlanAssociationsForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (BackupPlanAssociation element :
           backupDRClient.fetchBackupPlanAssociationsForResourceType(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse)` |   
  
### fetchBackupPlanAssociationsForResourceType(String parent, String resourceType)
    
    
    public final BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse fetchBackupPlanAssociationsForResourceType(String parent, String resourceType)

List BackupPlanAssociations for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String resourceType = "resourceType-384364440";
       for (BackupPlanAssociation element :
           backupDRClient
               .fetchBackupPlanAssociationsForResourceType(parent, resourceType)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse)` |   
  
### fetchBackupPlanAssociationsForResourceTypeCallable()
    
    
    public final UnaryCallable<FetchBackupPlanAssociationsForResourceTypeRequest,FetchBackupPlanAssociationsForResourceTypeResponse> fetchBackupPlanAssociationsForResourceTypeCallable()

List BackupPlanAssociations for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupPlanAssociationsForResourceTypeRequest request =
           FetchBackupPlanAssociationsForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         FetchBackupPlanAssociationsForResourceTypeResponse response =
             backupDRClient.fetchBackupPlanAssociationsForResourceTypeCallable().call(request);
         for (BackupPlanAssociation element : response.getBackupPlanAssociationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeRequest),[FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeResponse)>` |   
  
### fetchBackupPlanAssociationsForResourceTypePagedCallable()
    
    
    public final UnaryCallable<FetchBackupPlanAssociationsForResourceTypeRequest,BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse> fetchBackupPlanAssociationsForResourceTypePagedCallable()

List BackupPlanAssociations for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupPlanAssociationsForResourceTypeRequest request =
           FetchBackupPlanAssociationsForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<BackupPlanAssociation> future =
           backupDRClient
               .fetchBackupPlanAssociationsForResourceTypePagedCallable()
               .futureCall(request);
       // Do something.
       for (BackupPlanAssociation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeRequest),[FetchBackupPlanAssociationsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupPlanAssociationsForResourceTypePagedResponse)>` |   
  
### fetchBackupsForResourceType(@Nullable DataSourceName parent, String resourceType)
    
    
    public final BackupDRClient.FetchBackupsForResourceTypePagedResponse fetchBackupsForResourceType(@Nullable DataSourceName parent, String resourceType)

Fetch Backups for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DataSourceName parent =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]");
       String resourceType = "resourceType-384364440";
       for (Backup element :
           backupDRClient.fetchBackupsForResourceType(parent, resourceType).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.DataSourceName`  
Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupsForResourceTypePagedResponse)` |   
  
### fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request)
    
    
    public final BackupDRClient.FetchBackupsForResourceTypePagedResponse fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request)

Fetch Backups for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupsForResourceTypeRequest request =
           FetchBackupsForResourceTypeRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       for (Backup element : backupDRClient.fetchBackupsForResourceType(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupsForResourceTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupsForResourceTypePagedResponse)` |   
  
### fetchBackupsForResourceType(String parent, String resourceType)
    
    
    public final BackupDRClient.FetchBackupsForResourceTypePagedResponse fetchBackupsForResourceType(String parent, String resourceType)

Fetch Backups for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]").toString();
       String resourceType = "resourceType-384364440";
       for (Backup element :
           backupDRClient.fetchBackupsForResourceType(parent, resourceType).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchBackupsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupsForResourceTypePagedResponse)` |   
  
### fetchBackupsForResourceTypeCallable()
    
    
    public final UnaryCallable<FetchBackupsForResourceTypeRequest,FetchBackupsForResourceTypeResponse> fetchBackupsForResourceTypeCallable()

Fetch Backups for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupsForResourceTypeRequest request =
           FetchBackupsForResourceTypeRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       while (true) {
         FetchBackupsForResourceTypeResponse response =
             backupDRClient.fetchBackupsForResourceTypeCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupsForResourceTypeRequest),[FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupsForResourceTypeResponse)>` |   
  
### fetchBackupsForResourceTypePagedCallable()
    
    
    public final UnaryCallable<FetchBackupsForResourceTypeRequest,BackupDRClient.FetchBackupsForResourceTypePagedResponse> fetchBackupsForResourceTypePagedCallable()

Fetch Backups for a given resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchBackupsForResourceTypeRequest request =
           FetchBackupsForResourceTypeRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       ApiFuture<Backup> future =
           backupDRClient.fetchBackupsForResourceTypePagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchBackupsForResourceTypeRequest),[FetchBackupsForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchBackupsForResourceTypePagedResponse)>` |   
  
### fetchDataSourceReferencesForResourceType(@Nullable LocationName parent, String resourceType)
    
    
    public final BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse fetchDataSourceReferencesForResourceType(@Nullable LocationName parent, String resourceType)

Fetch DataSourceReferences for a given project, location and resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String resourceType = "resourceType-384364440";
       for (DataSourceReference element :
           backupDRClient
               .fetchDataSourceReferencesForResourceType(parent, resourceType)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse)` |   
  
### fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request)
    
    
    public final BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request)

Fetch DataSourceReferences for a given project, location and resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchDataSourceReferencesForResourceTypeRequest request =
           FetchDataSourceReferencesForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataSourceReference element :
           backupDRClient.fetchDataSourceReferencesForResourceType(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse)` |   
  
### fetchDataSourceReferencesForResourceType(String parent, String resourceType)
    
    
    public final BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse fetchDataSourceReferencesForResourceType(String parent, String resourceType)

Fetch DataSourceReferences for a given project, location and resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String resourceType = "resourceType-384364440";
       for (DataSourceReference element :
           backupDRClient
               .fetchDataSourceReferencesForResourceType(parent, resourceType)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
`resourceType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse)` |   
  
### fetchDataSourceReferencesForResourceTypeCallable()
    
    
    public final UnaryCallable<FetchDataSourceReferencesForResourceTypeRequest,FetchDataSourceReferencesForResourceTypeResponse> fetchDataSourceReferencesForResourceTypeCallable()

Fetch DataSourceReferences for a given project, location and resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchDataSourceReferencesForResourceTypeRequest request =
           FetchDataSourceReferencesForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         FetchDataSourceReferencesForResourceTypeResponse response =
             backupDRClient.fetchDataSourceReferencesForResourceTypeCallable().call(request);
         for (DataSourceReference element : response.getDataSourceReferencesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeRequest),[FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeResponse)>` |   
  
### fetchDataSourceReferencesForResourceTypePagedCallable()
    
    
    public final UnaryCallable<FetchDataSourceReferencesForResourceTypeRequest,BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse> fetchDataSourceReferencesForResourceTypePagedCallable()

Fetch DataSourceReferences for a given project, location and resource type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchDataSourceReferencesForResourceTypeRequest request =
           FetchDataSourceReferencesForResourceTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceType("resourceType-384364440")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataSourceReference> future =
           backupDRClient
               .fetchDataSourceReferencesForResourceTypePagedCallable()
               .futureCall(request);
       // Do something.
       for (DataSourceReference element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeRequest),[FetchDataSourceReferencesForResourceTypePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchDataSourceReferencesForResourceTypePagedResponse)>` |   
  
### fetchUsableBackupVaults(@Nullable LocationName parent)
    
    
    public final BackupDRClient.FetchUsableBackupVaultsPagedResponse fetchUsableBackupVaults(@Nullable LocationName parent)

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackupVault element : backupDRClient.fetchUsableBackupVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchUsableBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchUsableBackupVaultsPagedResponse)` |   
  
### fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request)
    
    
    public final BackupDRClient.FetchUsableBackupVaultsPagedResponse fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request)

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchUsableBackupVaultsRequest request =
           FetchUsableBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (BackupVault element : backupDRClient.fetchUsableBackupVaults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchUsableBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchUsableBackupVaultsPagedResponse)` |   
  
### fetchUsableBackupVaults(String parent)
    
    
    public final BackupDRClient.FetchUsableBackupVaultsPagedResponse fetchUsableBackupVaults(String parent)

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackupVault element : backupDRClient.fetchUsableBackupVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.FetchUsableBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchUsableBackupVaultsPagedResponse)` |   
  
### fetchUsableBackupVaultsCallable()
    
    
    public final UnaryCallable<FetchUsableBackupVaultsRequest,FetchUsableBackupVaultsResponse> fetchUsableBackupVaultsCallable()

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchUsableBackupVaultsRequest request =
           FetchUsableBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         FetchUsableBackupVaultsResponse response =
             backupDRClient.fetchUsableBackupVaultsCallable().call(request);
         for (BackupVault element : response.getBackupVaultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsRequest),[FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsResponse)>` |   
  
### fetchUsableBackupVaultsPagedCallable()
    
    
    public final UnaryCallable<FetchUsableBackupVaultsRequest,BackupDRClient.FetchUsableBackupVaultsPagedResponse> fetchUsableBackupVaultsPagedCallable()

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       FetchUsableBackupVaultsRequest request =
           FetchUsableBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<BackupVault> future =
           backupDRClient.fetchUsableBackupVaultsPagedCallable().futureCall(request);
       // Do something.
       for (BackupVault element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.FetchUsableBackupVaultsRequest),[FetchUsableBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.FetchUsableBackupVaultsPagedResponse)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Gets details of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupName name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]");
       Backup response = backupDRClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupName`  
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Gets details of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setView(BackupView.forNumber(0))
               .build();
       Backup response = backupDRClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Gets details of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
               .toString();
       Backup response = backupDRClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Gets details of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setView(BackupView.forNumber(0))
               .build();
       ApiFuture<Backup> future = backupDRClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup)>` |   
  
### getBackupPlan(@Nullable BackupPlanName name)
    
    
    public final BackupPlan getBackupPlan(@Nullable BackupPlanName name)

Gets details of a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanName name = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]");
       BackupPlan response = backupDRClient.getBackupPlan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanName`  
Required. The resource name of the `BackupPlan` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)` |   
  
### getBackupPlan(GetBackupPlanRequest request)
    
    
    public final BackupPlan getBackupPlan(GetBackupPlanRequest request)

Gets details of a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanRequest request =
           GetBackupPlanRequest.newBuilder()
               .setName(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .build();
       BackupPlan response = backupDRClient.getBackupPlan(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)` |   
  
### getBackupPlan(String name)
    
    
    public final BackupPlan getBackupPlan(String name)

Gets details of a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString();
       BackupPlan response = backupDRClient.getBackupPlan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the `BackupPlan` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)` |   
  
### getBackupPlanAssociation(@Nullable BackupPlanAssociationName name)
    
    
    public final BackupPlanAssociation getBackupPlanAssociation(@Nullable BackupPlanAssociationName name)

Gets details of a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanAssociationName name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]");
       BackupPlanAssociation response = backupDRClient.getBackupPlanAssociation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanAssociationName`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)` |   
  
### getBackupPlanAssociation(GetBackupPlanAssociationRequest request)
    
    
    public final BackupPlanAssociation getBackupPlanAssociation(GetBackupPlanAssociationRequest request)

Gets details of a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanAssociationRequest request =
           GetBackupPlanAssociationRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .build();
       BackupPlanAssociation response = backupDRClient.getBackupPlanAssociation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanAssociationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)` |   
  
### getBackupPlanAssociation(String name)
    
    
    public final BackupPlanAssociation getBackupPlanAssociation(String name)

Gets details of a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
               .toString();
       BackupPlanAssociation response = backupDRClient.getBackupPlanAssociation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)` |   
  
### getBackupPlanAssociationCallable()
    
    
    public final UnaryCallable<GetBackupPlanAssociationRequest,BackupPlanAssociation> getBackupPlanAssociationCallable()

Gets details of a single BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanAssociationRequest request =
           GetBackupPlanAssociationRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .build();
       ApiFuture<BackupPlanAssociation> future =
           backupDRClient.getBackupPlanAssociationCallable().futureCall(request);
       // Do something.
       BackupPlanAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanAssociationRequest),[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)>` |   
  
### getBackupPlanCallable()
    
    
    public final UnaryCallable<GetBackupPlanRequest,BackupPlan> getBackupPlanCallable()

Gets details of a single BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanRequest request =
           GetBackupPlanRequest.newBuilder()
               .setName(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .build();
       ApiFuture<BackupPlan> future = backupDRClient.getBackupPlanCallable().futureCall(request);
       // Do something.
       BackupPlan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)>` |   
  
### getBackupPlanRevision(@Nullable BackupPlanRevisionName name)
    
    
    public final BackupPlanRevision getBackupPlanRevision(@Nullable BackupPlanRevisionName name)

Gets details of a single BackupPlanRevision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanRevisionName name =
           BackupPlanRevisionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]", "[REVISION]");
       BackupPlanRevision response = backupDRClient.getBackupPlanRevision(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanRevisionName`  
Required. The resource name of the `BackupPlanRevision` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanRevision)` |   
  
### getBackupPlanRevision(GetBackupPlanRevisionRequest request)
    
    
    public final BackupPlanRevision getBackupPlanRevision(GetBackupPlanRevisionRequest request)

Gets details of a single BackupPlanRevision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanRevisionRequest request =
           GetBackupPlanRevisionRequest.newBuilder()
               .setName(
                   BackupPlanRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]", "[REVISION]")
                       .toString())
               .build();
       BackupPlanRevision response = backupDRClient.getBackupPlanRevision(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanRevisionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanRevision)` |   
  
### getBackupPlanRevision(String name)
    
    
    public final BackupPlanRevision getBackupPlanRevision(String name)

Gets details of a single BackupPlanRevision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupPlanRevisionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]", "[REVISION]")
               .toString();
       BackupPlanRevision response = backupDRClient.getBackupPlanRevision(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the `BackupPlanRevision` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanRevision)` |   
  
### getBackupPlanRevisionCallable()
    
    
    public final UnaryCallable<GetBackupPlanRevisionRequest,BackupPlanRevision> getBackupPlanRevisionCallable()

Gets details of a single BackupPlanRevision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupPlanRevisionRequest request =
           GetBackupPlanRevisionRequest.newBuilder()
               .setName(
                   BackupPlanRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]", "[REVISION]")
                       .toString())
               .build();
       ApiFuture<BackupPlanRevision> future =
           backupDRClient.getBackupPlanRevisionCallable().futureCall(request);
       // Do something.
       BackupPlanRevision response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupPlanRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupPlanRevisionRequest),[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanRevision)>` |   
  
### getBackupVault(@Nullable BackupVaultName name)
    
    
    public final BackupVault getBackupVault(@Nullable BackupVaultName name)

Gets details of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupVaultName name = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]");
       BackupVault response = backupDRClient.getBackupVault(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupVaultName`  
Required. Name of the backupvault store resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)` |   
  
### getBackupVault(GetBackupVaultRequest request)
    
    
    public final BackupVault getBackupVault(GetBackupVaultRequest request)

Gets details of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupVaultRequest request =
           GetBackupVaultRequest.newBuilder()
               .setName(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setView(BackupVaultView.forNumber(0))
               .build();
       BackupVault response = backupDRClient.getBackupVault(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)` |   
  
### getBackupVault(String name)
    
    
    public final BackupVault getBackupVault(String name)

Gets details of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString();
       BackupVault response = backupDRClient.getBackupVault(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backupvault store resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)` |   
  
### getBackupVaultCallable()
    
    
    public final UnaryCallable<GetBackupVaultRequest,BackupVault> getBackupVaultCallable()

Gets details of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetBackupVaultRequest request =
           GetBackupVaultRequest.newBuilder()
               .setName(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setView(BackupVaultView.forNumber(0))
               .build();
       ApiFuture<BackupVault> future = backupDRClient.getBackupVaultCallable().futureCall(request);
       // Do something.
       BackupVault response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetBackupVaultRequest),[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)>` |   
  
### getDataSource(@Nullable DataSourceName name)
    
    
    public final DataSource getDataSource(@Nullable DataSourceName name)

Gets details of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DataSourceName name =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]");
       DataSource response = backupDRClient.getDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.DataSourceName`  
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource)` |   
  
### getDataSource(GetDataSourceRequest request)
    
    
    public final DataSource getDataSource(GetDataSourceRequest request)

Gets details of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetDataSourceRequest request =
           GetDataSourceRequest.newBuilder()
               .setName(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .build();
       DataSource response = backupDRClient.getDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource)` |   
  
### getDataSource(String name)
    
    
    public final DataSource getDataSource(String name)

Gets details of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]").toString();
       DataSource response = backupDRClient.getDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource)` |   
  
### getDataSourceCallable()
    
    
    public final UnaryCallable<GetDataSourceRequest,DataSource> getDataSourceCallable()

Gets details of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetDataSourceRequest request =
           GetDataSourceRequest.newBuilder()
               .setName(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .build();
       ApiFuture<DataSource> future = backupDRClient.getDataSourceCallable().futureCall(request);
       // Do something.
       DataSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetDataSourceRequest),[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource)>` |   
  
### getDataSourceReference(@Nullable DataSourceReferenceName name)
    
    
    public final DataSourceReference getDataSourceReference(@Nullable DataSourceReferenceName name)

Gets details of a single DataSourceReference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DataSourceReferenceName name =
           DataSourceReferenceName.of("[PROJECT]", "[LOCATION]", "[DATA_SOURCE_REFERENCE]");
       DataSourceReference response = backupDRClient.getDataSourceReference(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.DataSourceReferenceName`  
Required. The name of the DataSourceReference to retrieve. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}  
**Returns**  
---  
**Type** | **Description**  
`[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceReference)` |   
  
### getDataSourceReference(GetDataSourceReferenceRequest request)
    
    
    public final DataSourceReference getDataSourceReference(GetDataSourceReferenceRequest request)

Gets details of a single DataSourceReference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetDataSourceReferenceRequest request =
           GetDataSourceReferenceRequest.newBuilder()
               .setName(
                   DataSourceReferenceName.of("[PROJECT]", "[LOCATION]", "[DATA_SOURCE_REFERENCE]")
                       .toString())
               .build();
       DataSourceReference response = backupDRClient.getDataSourceReference(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceReferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetDataSourceReferenceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceReference)` |   
  
### getDataSourceReference(String name)
    
    
    public final DataSourceReference getDataSourceReference(String name)

Gets details of a single DataSourceReference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           DataSourceReferenceName.of("[PROJECT]", "[LOCATION]", "[DATA_SOURCE_REFERENCE]")
               .toString();
       DataSourceReference response = backupDRClient.getDataSourceReference(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataSourceReference to retrieve. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}  
**Returns**  
---  
**Type** | **Description**  
`[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceReference)` |   
  
### getDataSourceReferenceCallable()
    
    
    public final UnaryCallable<GetDataSourceReferenceRequest,DataSourceReference> getDataSourceReferenceCallable()

Gets details of a single DataSourceReference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetDataSourceReferenceRequest request =
           GetDataSourceReferenceRequest.newBuilder()
               .setName(
                   DataSourceReferenceName.of("[PROJECT]", "[LOCATION]", "[DATA_SOURCE_REFERENCE]")
                       .toString())
               .build();
       ApiFuture<DataSourceReference> future =
           backupDRClient.getDataSourceReferenceCallable().futureCall(request);
       // Do something.
       DataSourceReference response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataSourceReferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetDataSourceReferenceRequest),[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSourceReference)>` |   
  
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = backupDRClient.getIamPolicy(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = backupDRClient.getIamPolicyCallable().futureCall(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = backupDRClient.getLocation(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = backupDRClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getManagementServer(@Nullable ManagementServerName name)
    
    
    public final ManagementServer getManagementServer(@Nullable ManagementServerName name)

Gets details of a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ManagementServerName name =
           ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]");
       ManagementServer response = backupDRClient.getManagementServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.ManagementServerName`  
Required. Name of the management server resource name, in the format 'projects/{project_id}/locations/{location}/managementServers/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)` |   
  
### getManagementServer(GetManagementServerRequest request)
    
    
    public final ManagementServer getManagementServer(GetManagementServerRequest request)

Gets details of a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetManagementServerRequest request =
           GetManagementServerRequest.newBuilder()
               .setName(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .build();
       ManagementServer response = backupDRClient.getManagementServer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetManagementServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)` |   
  
### getManagementServer(String name)
    
    
    public final ManagementServer getManagementServer(String name)

Gets details of a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]").toString();
       ManagementServer response = backupDRClient.getManagementServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the management server resource name, in the format 'projects/{project_id}/locations/{location}/managementServers/{resource_name}'  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)` |   
  
### getManagementServerCallable()
    
    
    public final UnaryCallable<GetManagementServerRequest,ManagementServer> getManagementServerCallable()

Gets details of a single ManagementServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       GetManagementServerRequest request =
           GetManagementServerRequest.newBuilder()
               .setName(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .build();
       ApiFuture<ManagementServer> future =
           backupDRClient.getManagementServerCallable().futureCall(request);
       // Do something.
       ManagementServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.GetManagementServerRequest),[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ManagementServer)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable BackupDRSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupDRSettings` |   
  
### getStub()
    
    
    public BackupDRStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BackupDRStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.stub.BackupDRStub)` |   
  
### initializeServiceAsync(InitializeServiceRequest request)
    
    
    public final OperationFuture<InitializeServiceResponse,OperationMetadata> initializeServiceAsync(InitializeServiceRequest request)

Initializes the service related config for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       InitializeServiceRequest request =
           InitializeServiceRequest.newBuilder()
               .setName("name3373707")
               .setResourceType("resourceType-384364440")
               .setRequestId("requestId693933066")
               .build();
       InitializeServiceResponse response = backupDRClient.initializeServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InitializeServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.InitializeServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InitializeServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.InitializeServiceResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### initializeServiceCallable()
    
    
    public final UnaryCallable<InitializeServiceRequest,Operation> initializeServiceCallable()

Initializes the service related config for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       InitializeServiceRequest request =
           InitializeServiceRequest.newBuilder()
               .setName("name3373707")
               .setResourceType("resourceType-384364440")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.initializeServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InitializeServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.InitializeServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### initializeServiceOperationCallable()
    
    
    public final OperationCallable<InitializeServiceRequest,InitializeServiceResponse,OperationMetadata> initializeServiceOperationCallable()

Initializes the service related config for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       InitializeServiceRequest request =
           InitializeServiceRequest.newBuilder()
               .setName("name3373707")
               .setResourceType("resourceType-384364440")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<InitializeServiceResponse, OperationMetadata> future =
           backupDRClient.initializeServiceOperationCallable().futureCall(request);
       // Do something.
       InitializeServiceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InitializeServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.InitializeServiceRequest),[InitializeServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.InitializeServiceResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
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
  
### listBackupPlanAssociations(@Nullable LocationName parent)
    
    
    public final BackupDRClient.ListBackupPlanAssociationsPagedResponse listBackupPlanAssociations(@Nullable LocationName parent)

Lists BackupPlanAssociations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackupPlanAssociation element :
           backupDRClient.listBackupPlanAssociations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The project and location for which to retrieve backup Plan Associations information, in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for example **us-central1**. To retrieve backup plan associations for all locations, use "-" for the `{location}` value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanAssociationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanAssociationsPagedResponse)` |   
  
### listBackupPlanAssociations(ListBackupPlanAssociationsRequest request)
    
    
    public final BackupDRClient.ListBackupPlanAssociationsPagedResponse listBackupPlanAssociations(ListBackupPlanAssociationsRequest request)

Lists BackupPlanAssociations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanAssociationsRequest request =
           ListBackupPlanAssociationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (BackupPlanAssociation element :
           backupDRClient.listBackupPlanAssociations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanAssociationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanAssociationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanAssociationsPagedResponse)` |   
  
### listBackupPlanAssociations(String parent)
    
    
    public final BackupDRClient.ListBackupPlanAssociationsPagedResponse listBackupPlanAssociations(String parent)

Lists BackupPlanAssociations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackupPlanAssociation element :
           backupDRClient.listBackupPlanAssociations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve backup Plan Associations information, in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for example **us-central1**. To retrieve backup plan associations for all locations, use "-" for the `{location}` value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanAssociationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanAssociationsPagedResponse)` |   
  
### listBackupPlanAssociationsCallable()
    
    
    public final UnaryCallable<ListBackupPlanAssociationsRequest,ListBackupPlanAssociationsResponse> listBackupPlanAssociationsCallable()

Lists BackupPlanAssociations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanAssociationsRequest request =
           ListBackupPlanAssociationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListBackupPlanAssociationsResponse response =
             backupDRClient.listBackupPlanAssociationsCallable().call(request);
         for (BackupPlanAssociation element : response.getBackupPlanAssociationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanAssociationsRequest),[ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanAssociationsResponse)>` |   
  
### listBackupPlanAssociationsPagedCallable()
    
    
    public final UnaryCallable<ListBackupPlanAssociationsRequest,BackupDRClient.ListBackupPlanAssociationsPagedResponse> listBackupPlanAssociationsPagedCallable()

Lists BackupPlanAssociations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanAssociationsRequest request =
           ListBackupPlanAssociationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<BackupPlanAssociation> future =
           backupDRClient.listBackupPlanAssociationsPagedCallable().futureCall(request);
       // Do something.
       for (BackupPlanAssociation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanAssociationsRequest),[ListBackupPlanAssociationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanAssociationsPagedResponse)>` |   
  
### listBackupPlanRevisions(@Nullable BackupPlanName parent)
    
    
    public final BackupDRClient.ListBackupPlanRevisionsPagedResponse listBackupPlanRevisions(@Nullable BackupPlanName parent)

Lists BackupPlanRevisions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanName parent = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]");
       for (BackupPlanRevision element :
           backupDRClient.listBackupPlanRevisions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanName`  
Required. The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanRevisionsPagedResponse)` |   
  
### listBackupPlanRevisions(ListBackupPlanRevisionsRequest request)
    
    
    public final BackupDRClient.ListBackupPlanRevisionsPagedResponse listBackupPlanRevisions(ListBackupPlanRevisionsRequest request)

Lists BackupPlanRevisions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanRevisionsRequest request =
           ListBackupPlanRevisionsRequest.newBuilder()
               .setParent(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BackupPlanRevision element :
           backupDRClient.listBackupPlanRevisions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanRevisionsPagedResponse)` |   
  
### listBackupPlanRevisions(String parent)
    
    
    public final BackupDRClient.ListBackupPlanRevisionsPagedResponse listBackupPlanRevisions(String parent)

Lists BackupPlanRevisions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString();
       for (BackupPlanRevision element :
           backupDRClient.listBackupPlanRevisions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlanRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanRevisionsPagedResponse)` |   
  
### listBackupPlanRevisionsCallable()
    
    
    public final UnaryCallable<ListBackupPlanRevisionsRequest,ListBackupPlanRevisionsResponse> listBackupPlanRevisionsCallable()

Lists BackupPlanRevisions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanRevisionsRequest request =
           ListBackupPlanRevisionsRequest.newBuilder()
               .setParent(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBackupPlanRevisionsResponse response =
             backupDRClient.listBackupPlanRevisionsCallable().call(request);
         for (BackupPlanRevision element : response.getBackupPlanRevisionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanRevisionsRequest),[ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanRevisionsResponse)>` |   
  
### listBackupPlanRevisionsPagedCallable()
    
    
    public final UnaryCallable<ListBackupPlanRevisionsRequest,BackupDRClient.ListBackupPlanRevisionsPagedResponse> listBackupPlanRevisionsPagedCallable()

Lists BackupPlanRevisions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlanRevisionsRequest request =
           ListBackupPlanRevisionsRequest.newBuilder()
               .setParent(BackupPlanName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BackupPlanRevision> future =
           backupDRClient.listBackupPlanRevisionsPagedCallable().futureCall(request);
       // Do something.
       for (BackupPlanRevision element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlanRevisionsRequest),[ListBackupPlanRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlanRevisionsPagedResponse)>` |   
  
### listBackupPlans(@Nullable LocationName parent)
    
    
    public final BackupDRClient.ListBackupPlansPagedResponse listBackupPlans(@Nullable LocationName parent)

Lists BackupPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackupPlan element : backupDRClient.listBackupPlans(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The project and location for which to retrieve `BackupPlans` information. Format: `projects/{project}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. To retrieve backup plans for all locations, use "-" for the `{location}` value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlansPagedResponse)` |   
  
### listBackupPlans(ListBackupPlansRequest request)
    
    
    public final BackupDRClient.ListBackupPlansPagedResponse listBackupPlans(ListBackupPlansRequest request)

Lists BackupPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlansRequest request =
           ListBackupPlansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (BackupPlan element : backupDRClient.listBackupPlans(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlansRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlansPagedResponse)` |   
  
### listBackupPlans(String parent)
    
    
    public final BackupDRClient.ListBackupPlansPagedResponse listBackupPlans(String parent)

Lists BackupPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackupPlan element : backupDRClient.listBackupPlans(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve `BackupPlans` information. Format: `projects/{project}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. To retrieve backup plans for all locations, use "-" for the `{location}` value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupPlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlansPagedResponse)` |   
  
### listBackupPlansCallable()
    
    
    public final UnaryCallable<ListBackupPlansRequest,ListBackupPlansResponse> listBackupPlansCallable()

Lists BackupPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlansRequest request =
           ListBackupPlansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListBackupPlansResponse response = backupDRClient.listBackupPlansCallable().call(request);
         for (BackupPlan element : response.getBackupPlansList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlansRequest),[ListBackupPlansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlansResponse)>` |   
  
### listBackupPlansPagedCallable()
    
    
    public final UnaryCallable<ListBackupPlansRequest,BackupDRClient.ListBackupPlansPagedResponse> listBackupPlansPagedCallable()

Lists BackupPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupPlansRequest request =
           ListBackupPlansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<BackupPlan> future =
           backupDRClient.listBackupPlansPagedCallable().futureCall(request);
       // Do something.
       for (BackupPlan element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupPlansRequest),[ListBackupPlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupPlansPagedResponse)>` |   
  
### listBackupVaults(@Nullable LocationName parent)
    
    
    public final BackupDRClient.ListBackupVaultsPagedResponse listBackupVaults(@Nullable LocationName parent)

Lists BackupVaults in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackupVault element : backupDRClient.listBackupVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupVaultsPagedResponse)` |   
  
### listBackupVaults(ListBackupVaultsRequest request)
    
    
    public final BackupDRClient.ListBackupVaultsPagedResponse listBackupVaults(ListBackupVaultsRequest request)

Lists BackupVaults in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupVaultsRequest request =
           ListBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupVaultView.forNumber(0))
               .build();
       for (BackupVault element : backupDRClient.listBackupVaults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupVaultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupVaultsPagedResponse)` |   
  
### listBackupVaults(String parent)
    
    
    public final BackupDRClient.ListBackupVaultsPagedResponse listBackupVaults(String parent)

Lists BackupVaults in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackupVault element : backupDRClient.listBackupVaults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupVaultsPagedResponse)` |   
  
### listBackupVaultsCallable()
    
    
    public final UnaryCallable<ListBackupVaultsRequest,ListBackupVaultsResponse> listBackupVaultsCallable()

Lists BackupVaults in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupVaultsRequest request =
           ListBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupVaultView.forNumber(0))
               .build();
       while (true) {
         ListBackupVaultsResponse response = backupDRClient.listBackupVaultsCallable().call(request);
         for (BackupVault element : response.getBackupVaultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupVaultsRequest),[ListBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupVaultsResponse)>` |   
  
### listBackupVaultsPagedCallable()
    
    
    public final UnaryCallable<ListBackupVaultsRequest,BackupDRClient.ListBackupVaultsPagedResponse> listBackupVaultsPagedCallable()

Lists BackupVaults in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupVaultsRequest request =
           ListBackupVaultsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupVaultView.forNumber(0))
               .build();
       ApiFuture<BackupVault> future =
           backupDRClient.listBackupVaultsPagedCallable().futureCall(request);
       // Do something.
       for (BackupVault element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupVaultsRequest),[ListBackupVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupVaultsPagedResponse)>` |   
  
### listBackups(@Nullable DataSourceName parent)
    
    
    public final BackupDRClient.ListBackupsPagedResponse listBackups(@Nullable DataSourceName parent)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DataSourceName parent =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]");
       for (Backup element : backupDRClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.DataSourceName`  
Required. The project and location for which to retrieve backup information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupsPagedResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final BackupDRClient.ListBackupsPagedResponse listBackups(ListBackupsRequest request)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       for (Backup element : backupDRClient.listBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupsPagedResponse)` |   
  
### listBackups(String parent)
    
    
    public final BackupDRClient.ListBackupsPagedResponse listBackups(String parent)

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent =
           DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]").toString();
       for (Backup element : backupDRClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve backup information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupsPagedResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       while (true) {
         ListBackupsResponse response = backupDRClient.listBackupsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupsResponse)>` |   
  
### listBackupsPagedCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,BackupDRClient.ListBackupsPagedResponse> listBackupsPagedCallable()

Lists Backups in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   DataSourceName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setView(BackupView.forNumber(0))
               .build();
       ApiFuture<Backup> future = backupDRClient.listBackupsPagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListBackupsRequest),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListBackupsPagedResponse)>` |   
  
### listDataSourceReferences(@Nullable LocationName parent)
    
    
    public final BackupDRClient.ListDataSourceReferencesPagedResponse listDataSourceReferences(@Nullable LocationName parent)

Lists DataSourceReferences for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataSourceReference element :
           backupDRClient.listDataSourceReferences(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourceReferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourceReferencesPagedResponse)` |   
  
### listDataSourceReferences(ListDataSourceReferencesRequest request)
    
    
    public final BackupDRClient.ListDataSourceReferencesPagedResponse listDataSourceReferences(ListDataSourceReferencesRequest request)

Lists DataSourceReferences for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourceReferencesRequest request =
           ListDataSourceReferencesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataSourceReference element :
           backupDRClient.listDataSourceReferences(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataSourceReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourceReferencesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourceReferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourceReferencesPagedResponse)` |   
  
### listDataSourceReferences(String parent)
    
    
    public final BackupDRClient.ListDataSourceReferencesPagedResponse listDataSourceReferences(String parent)

Lists DataSourceReferences for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataSourceReference element :
           backupDRClient.listDataSourceReferences(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourceReferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourceReferencesPagedResponse)` |   
  
### listDataSourceReferencesCallable()
    
    
    public final UnaryCallable<ListDataSourceReferencesRequest,ListDataSourceReferencesResponse> listDataSourceReferencesCallable()

Lists DataSourceReferences for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourceReferencesRequest request =
           ListDataSourceReferencesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataSourceReferencesResponse response =
             backupDRClient.listDataSourceReferencesCallable().call(request);
         for (DataSourceReference element : response.getDataSourceReferencesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourceReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourceReferencesRequest),[ListDataSourceReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourceReferencesResponse)>` |   
  
### listDataSourceReferencesPagedCallable()
    
    
    public final UnaryCallable<ListDataSourceReferencesRequest,BackupDRClient.ListDataSourceReferencesPagedResponse> listDataSourceReferencesPagedCallable()

Lists DataSourceReferences for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourceReferencesRequest request =
           ListDataSourceReferencesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataSourceReference> future =
           backupDRClient.listDataSourceReferencesPagedCallable().futureCall(request);
       // Do something.
       for (DataSourceReference element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourceReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourceReferencesRequest),[ListDataSourceReferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourceReferencesPagedResponse)>` |   
  
### listDataSources(@Nullable BackupVaultName parent)
    
    
    public final BackupDRClient.ListDataSourcesPagedResponse listDataSources(@Nullable BackupVaultName parent)

Lists DataSources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupVaultName parent = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]");
       for (DataSource element : backupDRClient.listDataSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupVaultName`  
Required. The project and location for which to retrieve data sources information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourcesPagedResponse)` |   
  
### listDataSources(ListDataSourcesRequest request)
    
    
    public final BackupDRClient.ListDataSourcesPagedResponse listDataSources(ListDataSourcesRequest request)

Lists DataSources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataSource element : backupDRClient.listDataSources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourcesPagedResponse)` |   
  
### listDataSources(String parent)
    
    
    public final BackupDRClient.ListDataSourcesPagedResponse listDataSources(String parent)

Lists DataSources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString();
       for (DataSource element : backupDRClient.listDataSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve data sources information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourcesPagedResponse)` |   
  
### listDataSourcesCallable()
    
    
    public final UnaryCallable<ListDataSourcesRequest,ListDataSourcesResponse> listDataSourcesCallable()

Lists DataSources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataSourcesResponse response = backupDRClient.listDataSourcesCallable().call(request);
         for (DataSource element : response.getDataSourcesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourcesRequest),[ListDataSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourcesResponse)>` |   
  
### listDataSourcesPagedCallable()
    
    
    public final UnaryCallable<ListDataSourcesRequest,BackupDRClient.ListDataSourcesPagedResponse> listDataSourcesPagedCallable()

Lists DataSources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(BackupVaultName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataSource> future =
           backupDRClient.listDataSourcesPagedCallable().futureCall(request);
       // Do something.
       for (DataSource element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListDataSourcesRequest),[ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListDataSourcesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final BackupDRClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : backupDRClient.listLocations(request).iterateAll()) {
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
`[BackupDRClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = backupDRClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,BackupDRClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = backupDRClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListLocationsPagedResponse)>` |   
  
### listManagementServers(@Nullable LocationName parent)
    
    
    public final BackupDRClient.ListManagementServersPagedResponse listManagementServers(@Nullable LocationName parent)

Lists ManagementServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ManagementServer element : backupDRClient.listManagementServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.LocationName`  
Required. The project and location for which to retrieve management servers information, in the format 'projects/{project_id}/locations/{location}'. In Cloud BackupDR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve management servers for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListManagementServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListManagementServersPagedResponse)` |   
  
### listManagementServers(ListManagementServersRequest request)
    
    
    public final BackupDRClient.ListManagementServersPagedResponse listManagementServers(ListManagementServersRequest request)

Lists ManagementServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListManagementServersRequest request =
           ListManagementServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ManagementServer element : backupDRClient.listManagementServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListManagementServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListManagementServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListManagementServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListManagementServersPagedResponse)` |   
  
### listManagementServers(String parent)
    
    
    public final BackupDRClient.ListManagementServersPagedResponse listManagementServers(String parent)

Lists ManagementServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ManagementServer element : backupDRClient.listManagementServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve management servers information, in the format 'projects/{project_id}/locations/{location}'. In Cloud BackupDR, locations map to Google Cloud regions, for example 

  * *us-central1**. To retrieve management servers for all locations, use "-" for the '{location}' value. 

  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRClient.ListManagementServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListManagementServersPagedResponse)` |   
  
### listManagementServersCallable()
    
    
    public final UnaryCallable<ListManagementServersRequest,ListManagementServersResponse> listManagementServersCallable()

Lists ManagementServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListManagementServersRequest request =
           ListManagementServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListManagementServersResponse response =
             backupDRClient.listManagementServersCallable().call(request);
         for (ManagementServer element : response.getManagementServersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagementServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListManagementServersRequest),[ListManagementServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListManagementServersResponse)>` |   
  
### listManagementServersPagedCallable()
    
    
    public final UnaryCallable<ListManagementServersRequest,BackupDRClient.ListManagementServersPagedResponse> listManagementServersPagedCallable()

Lists ManagementServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       ListManagementServersRequest request =
           ListManagementServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ManagementServer> future =
           backupDRClient.listManagementServersPagedCallable().futureCall(request);
       // Do something.
       for (ManagementServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagementServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ListManagementServersRequest),[ListManagementServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDRClient.ListManagementServersPagedResponse)>` |   
  
### restoreBackupAsync(@Nullable BackupName name)
    
    
    public final OperationFuture<RestoreBackupResponse,OperationMetadata> restoreBackupAsync(@Nullable BackupName name)

Restore from a Backup

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupName name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]");
       RestoreBackupResponse response = backupDRClient.restoreBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupName`  
Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreBackupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### restoreBackupAsync(RestoreBackupRequest request)
    
    
    public final OperationFuture<RestoreBackupResponse,OperationMetadata> restoreBackupAsync(RestoreBackupRequest request)

Restore from a Backup

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       RestoreBackupRequest request =
           RestoreBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setClearOverridesFieldMask(FieldMask.newBuilder().build())
               .build();
       RestoreBackupResponse response = backupDRClient.restoreBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreBackupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### restoreBackupAsync(String name)
    
    
    public final OperationFuture<RestoreBackupResponse,OperationMetadata> restoreBackupAsync(String name)

Restore from a Backup

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
               .toString();
       RestoreBackupResponse response = backupDRClient.restoreBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreBackupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### restoreBackupCallable()
    
    
    public final UnaryCallable<RestoreBackupRequest,Operation> restoreBackupCallable()

Restore from a Backup

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       RestoreBackupRequest request =
           RestoreBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setClearOverridesFieldMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = backupDRClient.restoreBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreBackupOperationCallable()
    
    
    public final OperationCallable<RestoreBackupRequest,RestoreBackupResponse,OperationMetadata> restoreBackupOperationCallable()

Restore from a Backup

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       RestoreBackupRequest request =
           RestoreBackupRequest.newBuilder()
               .setName(
                   BackupName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUPVAULT]", "[DATASOURCE]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setClearOverridesFieldMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<RestoreBackupResponse, OperationMetadata> future =
           backupDRClient.restoreBackupOperationCallable().futureCall(request);
       // Do something.
       RestoreBackupResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest),[RestoreBackupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = backupDRClient.setIamPolicy(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = backupDRClient.setIamPolicyCallable().futureCall(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = backupDRClient.testIamPermissions(request);
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
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ManagementServerName.of("[PROJECT]", "[LOCATION]", "[MANAGEMENTSERVER]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           backupDRClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### triggerBackupAsync(@Nullable BackupPlanAssociationName name, String ruleId)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> triggerBackupAsync(@Nullable BackupPlanAssociationName name, String ruleId)

Triggers a new Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanAssociationName name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]");
       String ruleId = "ruleId-919875273";
       BackupPlanAssociation response = backupDRClient.triggerBackupAsync(name, ruleId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.backupdr.v1.BackupPlanAssociationName`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
`ruleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. backup rule_id for which a backup needs to be triggered.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### triggerBackupAsync(TriggerBackupRequest request)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> triggerBackupAsync(TriggerBackupRequest request)

Triggers a new Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       TriggerBackupRequest request =
           TriggerBackupRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRuleId("ruleId-919875273")
               .setRequestId("requestId693933066")
               .build();
       BackupPlanAssociation response = backupDRClient.triggerBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TriggerBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.TriggerBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### triggerBackupAsync(String name, String ruleId)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> triggerBackupAsync(String name, String ruleId)

Triggers a new Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       String name =
           BackupPlanAssociationName.of("[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
               .toString();
       String ruleId = "ruleId-919875273";
       BackupPlanAssociation response = backupDRClient.triggerBackupAsync(name, ruleId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`  
`ruleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. backup rule_id for which a backup needs to be triggered.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### triggerBackupCallable()
    
    
    public final UnaryCallable<TriggerBackupRequest,Operation> triggerBackupCallable()

Triggers a new Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       TriggerBackupRequest request =
           TriggerBackupRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRuleId("ruleId-919875273")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.triggerBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TriggerBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.TriggerBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### triggerBackupOperationCallable()
    
    
    public final OperationCallable<TriggerBackupRequest,BackupPlanAssociation,OperationMetadata> triggerBackupOperationCallable()

Triggers a new Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       TriggerBackupRequest request =
           TriggerBackupRequest.newBuilder()
               .setName(
                   BackupPlanAssociationName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKUP_PLAN_ASSOCIATION]")
                       .toString())
               .setRuleId("ruleId-919875273")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BackupPlanAssociation, OperationMetadata> future =
           backupDRClient.triggerBackupOperationCallable().futureCall(request);
       // Do something.
       BackupPlanAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TriggerBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.TriggerBackupRequest),[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupAsync(Backup backup, FieldMask updateMask)
    
    
    public final OperationFuture<Backup,OperationMetadata> updateBackupAsync(Backup backup, FieldMask updateMask)

Updates the settings of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       Backup backup = Backup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Backup response = backupDRClient.updateBackupAsync(backup, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupAsync(UpdateBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> updateBackupAsync(UpdateBackupRequest request)

Updates the settings of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Backup response = backupDRClient.updateBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupCallable()
    
    
    public final UnaryCallable<UpdateBackupRequest,Operation> updateBackupCallable()

Updates the settings of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.updateBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupOperationCallable()
    
    
    public final OperationCallable<UpdateBackupRequest,Backup,OperationMetadata> updateBackupOperationCallable()

Updates the settings of a Backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           backupDRClient.updateBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanAssociationAsync(BackupPlanAssociation backupPlanAssociation, FieldMask updateMask)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> updateBackupPlanAssociationAsync(BackupPlanAssociation backupPlanAssociation, FieldMask updateMask)

Update a BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlanAssociation backupPlanAssociation = BackupPlanAssociation.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BackupPlanAssociation response =
           backupDRClient.updateBackupPlanAssociationAsync(backupPlanAssociation, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backupPlanAssociation` | `[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlanAssociation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently backup_plan_association.backup_plan is the only supported field.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanAssociationAsync(UpdateBackupPlanAssociationRequest request)
    
    
    public final OperationFuture<BackupPlanAssociation,OperationMetadata> updateBackupPlanAssociationAsync(UpdateBackupPlanAssociationRequest request)

Update a BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanAssociationRequest request =
           UpdateBackupPlanAssociationRequest.newBuilder()
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       BackupPlanAssociation response =
           backupDRClient.updateBackupPlanAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanAssociationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanAssociationCallable()
    
    
    public final UnaryCallable<UpdateBackupPlanAssociationRequest,Operation> updateBackupPlanAssociationCallable()

Update a BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanAssociationRequest request =
           UpdateBackupPlanAssociationRequest.newBuilder()
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backupDRClient.updateBackupPlanAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanAssociationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupPlanAssociationOperationCallable()
    
    
    public final OperationCallable<UpdateBackupPlanAssociationRequest,BackupPlanAssociation,OperationMetadata> updateBackupPlanAssociationOperationCallable()

Update a BackupPlanAssociation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanAssociationRequest request =
           UpdateBackupPlanAssociationRequest.newBuilder()
               .setBackupPlanAssociation(BackupPlanAssociation.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BackupPlanAssociation, OperationMetadata> future =
           backupDRClient.updateBackupPlanAssociationOperationCallable().futureCall(request);
       // Do something.
       BackupPlanAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanAssociationRequest),[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlanAssociation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanAsync(BackupPlan backupPlan, FieldMask updateMask)
    
    
    public final OperationFuture<BackupPlan,OperationMetadata> updateBackupPlanAsync(BackupPlan backupPlan, FieldMask updateMask)

Update a BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupPlan backupPlan = BackupPlan.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BackupPlan response = backupDRClient.updateBackupPlanAsync(backupPlan, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backupPlan` | `[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlan resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently, these fields are supported in update: description, schedules, retention period, adding and removing Backup Rules.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanAsync(UpdateBackupPlanRequest request)
    
    
    public final OperationFuture<BackupPlan,OperationMetadata> updateBackupPlanAsync(UpdateBackupPlanRequest request)

Update a BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanRequest request =
           UpdateBackupPlanRequest.newBuilder()
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       BackupPlan response = backupDRClient.updateBackupPlanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupPlanCallable()
    
    
    public final UnaryCallable<UpdateBackupPlanRequest,Operation> updateBackupPlanCallable()

Update a BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanRequest request =
           UpdateBackupPlanRequest.newBuilder()
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backupDRClient.updateBackupPlanCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupPlanOperationCallable()
    
    
    public final OperationCallable<UpdateBackupPlanRequest,BackupPlan,OperationMetadata> updateBackupPlanOperationCallable()

Update a BackupPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupPlanRequest request =
           UpdateBackupPlanRequest.newBuilder()
               .setBackupPlan(BackupPlan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<BackupPlan, OperationMetadata> future =
           backupDRClient.updateBackupPlanOperationCallable().futureCall(request);
       // Do something.
       BackupPlan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupVaultAsync(BackupVault backupVault, FieldMask updateMask)
    
    
    public final OperationFuture<BackupVault,OperationMetadata> updateBackupVaultAsync(BackupVault backupVault, FieldMask updateMask)

Updates the settings of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       BackupVault backupVault = BackupVault.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BackupVault response = backupDRClient.updateBackupVaultAsync(backupVault, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backupVault` | `[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the BackupVault resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupVaultAsync(UpdateBackupVaultRequest request)
    
    
    public final OperationFuture<BackupVault,OperationMetadata> updateBackupVaultAsync(UpdateBackupVaultRequest request)

Updates the settings of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupVaultRequest request =
           UpdateBackupVaultRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .setForceUpdateAccessRestriction(true)
               .build();
       BackupVault response = backupDRClient.updateBackupVaultAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupVaultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateBackupVaultCallable()
    
    
    public final UnaryCallable<UpdateBackupVaultRequest,Operation> updateBackupVaultCallable()

Updates the settings of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupVaultRequest request =
           UpdateBackupVaultRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .setForceUpdateAccessRestriction(true)
               .build();
       ApiFuture<Operation> future = backupDRClient.updateBackupVaultCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupVaultOperationCallable()
    
    
    public final OperationCallable<UpdateBackupVaultRequest,BackupVault,OperationMetadata> updateBackupVaultOperationCallable()

Updates the settings of a BackupVault.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateBackupVaultRequest request =
           UpdateBackupVaultRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackupVault(BackupVault.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .setForceUpdateAccessRestriction(true)
               .build();
       OperationFuture<BackupVault, OperationMetadata> future =
           backupDRClient.updateBackupVaultOperationCallable().futureCall(request);
       // Do something.
       BackupVault response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateBackupVaultRequest),[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateDataSourceAsync(DataSource dataSource, FieldMask updateMask)
    
    
    public final OperationFuture<DataSource,OperationMetadata> updateDataSourceAsync(DataSource dataSource, FieldMask updateMask)

Updates the settings of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       DataSource dataSource = DataSource.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataSource response = backupDRClient.updateDataSourceAsync(dataSource, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataSource` | `[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the DataSource resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateDataSourceAsync(UpdateDataSourceRequest request)
    
    
    public final OperationFuture<DataSource,OperationMetadata> updateDataSourceAsync(UpdateDataSourceRequest request)

Updates the settings of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateDataSourceRequest request =
           UpdateDataSourceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataSource(DataSource.newBuilder().build())
               .setRequestId("requestId693933066")
               .setAllowMissing(true)
               .build();
       DataSource response = backupDRClient.updateDataSourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
### updateDataSourceCallable()
    
    
    public final UnaryCallable<UpdateDataSourceRequest,Operation> updateDataSourceCallable()

Updates the settings of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateDataSourceRequest request =
           UpdateDataSourceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataSource(DataSource.newBuilder().build())
               .setRequestId("requestId693933066")
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future = backupDRClient.updateDataSourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateDataSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataSourceOperationCallable()
    
    
    public final OperationCallable<UpdateDataSourceRequest,DataSource,OperationMetadata> updateDataSourceOperationCallable()

Updates the settings of a DataSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackupDRClient backupDRClient = BackupDRClient.create()) {
       UpdateDataSourceRequest request =
           UpdateDataSourceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataSource(DataSource.newBuilder().build())
               .setRequestId("requestId693933066")
               .setAllowMissing(true)
               .build();
       OperationFuture<DataSource, OperationMetadata> future =
           backupDRClient.updateDataSourceOperationCallable().futureCall(request);
       // Do something.
       DataSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.UpdateDataSourceRequest),[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DataSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
