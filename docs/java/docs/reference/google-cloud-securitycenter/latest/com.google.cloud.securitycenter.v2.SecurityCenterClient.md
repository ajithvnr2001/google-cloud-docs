---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient
title: Class SecurityCenterClient (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:05.354398+00:00
---

# Class SecurityCenterClient (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityCenterClient (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-securitycenter/google-cloud-securitycenter/src/main/java/com/google/cloud/securitycenter/v2/SecurityCenterClient.java)| [Product Reference](https://cloud.google.com/security-command-center)| [REST Documentation](https://cloud.google.com/security-command-center/docs/reference/rest)  
---|---|---  
  
Service Description: V2 APIs for Security Center service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       List<CreateResourceValueConfigRequest> requests = new ArrayList<>();
       BatchCreateResourceValueConfigsResponse response =
           securityCenterClient.batchCreateResourceValueConfigs(parent, requests);
     }
     

Note: close() needs to be called on the SecurityCenterClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
BatchCreateResourceValueConfigs |  Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateResourceValueConfigs(OrganizationLocationName parent, List<CreateResourceValueConfigRequest> requests) 
  * batchCreateResourceValueConfigs(OrganizationName parent, List<CreateResourceValueConfigRequest> requests) 
  * batchCreateResourceValueConfigs(String parent, List<CreateResourceValueConfigRequest> requests) 
  * batchCreateResourceValueConfigs(BatchCreateResourceValueConfigsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateResourceValueConfigsCallable() 

  
BulkMuteFindings |  Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * bulkMuteFindingsAsync(BulkMuteFindingsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * bulkMuteFindingsAsync(ResourceName parent) 
  * bulkMuteFindingsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bulkMuteFindingsOperationCallable() 
  * bulkMuteFindingsCallable() 

  
CreateBigQueryExport |  Creates a BigQuery export. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBigQueryExport(CreateBigQueryExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBigQueryExport(FolderLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId) 
  * createBigQueryExport(LocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId) 
  * createBigQueryExport(OrganizationLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId) 
  * createBigQueryExport(String parent, BigQueryExport bigQueryExport, String bigQueryExportId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBigQueryExportCallable() 

  
CreateFinding |  Creates a finding in a location. The corresponding source must exist for finding creation to succeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFinding(CreateFindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createFinding(SourceName parent, Finding finding, String findingId) 
  * createFinding(String parent, Finding finding, String findingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFindingCallable() 

  
CreateMuteConfig |  Creates a mute config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMuteConfig(CreateMuteConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMuteConfig(FolderLocationName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(FolderName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(LocationName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(OrganizationLocationName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(OrganizationName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(ProjectName parent, MuteConfig muteConfig, String muteConfigId) 
  * createMuteConfig(String parent, MuteConfig muteConfig, String muteConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMuteConfigCallable() 

  
CreateNotificationConfig |  Creates a notification config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNotificationConfig(CreateNotificationConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createNotificationConfig(FolderLocationName parent, NotificationConfig notificationConfig, String configId) 
  * createNotificationConfig(LocationName parent, NotificationConfig notificationConfig, String configId) 
  * createNotificationConfig(OrganizationLocationName parent, NotificationConfig notificationConfig, String configId) 
  * createNotificationConfig(String parent, NotificationConfig notificationConfig, String configId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNotificationConfigCallable() 

  
CreateSource |  Creates a source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSource(CreateSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSource(OrganizationName parent, Source source) 
  * createSource(String parent, Source source) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSourceCallable() 

  
DeleteBigQueryExport |  Deletes an existing BigQuery export. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBigQueryExport(DeleteBigQueryExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteBigQueryExport(BigQueryExportName name) 
  * deleteBigQueryExport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBigQueryExportCallable() 

  
DeleteMuteConfig |  Deletes an existing mute config. If no location is specified, default is global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMuteConfig(DeleteMuteConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteMuteConfig(MuteConfigName name) 
  * deleteMuteConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMuteConfigCallable() 

  
DeleteNotificationConfig |  Deletes a notification config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNotificationConfig(DeleteNotificationConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteNotificationConfig(NotificationConfigName name) 
  * deleteNotificationConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNotificationConfigCallable() 

  
DeleteResourceValueConfig |  Deletes a ResourceValueConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteResourceValueConfig(DeleteResourceValueConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteResourceValueConfig(ResourceValueConfigName name) 
  * deleteResourceValueConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteResourceValueConfigCallable() 

  
GetBigQueryExport |  Gets a BigQuery export. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBigQueryExport(GetBigQueryExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBigQueryExport(BigQueryExportName name) 
  * getBigQueryExport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBigQueryExportCallable() 

  
GetSimulation |  Get the simulation by name or the latest simulation for the given organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSimulation(GetSimulationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSimulation(SimulationName name) 
  * getSimulation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSimulationCallable() 

  
GetValuedResource |  Get the valued resource by name |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getValuedResource(GetValuedResourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getValuedResource(ValuedResourceName name) 
  * getValuedResource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getValuedResourceCallable() 

  
GetIamPolicy |  Gets the access control policy on the specified Source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(ResourceName resource) 
  * getIamPolicy(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetMuteConfig |  Gets a mute config. If no location is specified, default is global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMuteConfig(GetMuteConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMuteConfig(MuteConfigName name) 
  * getMuteConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMuteConfigCallable() 

  
GetNotificationConfig |  Gets a notification config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNotificationConfig(GetNotificationConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNotificationConfig(NotificationConfigName name) 
  * getNotificationConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNotificationConfigCallable() 

  
GetResourceValueConfig |  Gets a ResourceValueConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getResourceValueConfig(GetResourceValueConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getResourceValueConfig(ResourceValueConfigName name) 
  * getResourceValueConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getResourceValueConfigCallable() 

  
GetSource |  Gets a source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSource(GetSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSource(SourceName name) 
  * getSource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSourceCallable() 

  
GroupFindings |  Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global  To group across all sources provide a `-` as the source id. The following list shows some examples:  \+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * groupFindings(GroupFindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * groupFindings(SourceName parent, String groupBy) 
  * groupFindings(String parent, String groupBy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * groupFindingsPagedCallable() 
  * groupFindingsCallable() 

  
ListAttackPaths |  Lists the attack paths for a set of simulation results or valued resources and filter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAttackPaths(ListAttackPathsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAttackPaths(OrganizationValuedResourceName parent) 
  * listAttackPaths(ValuedResourceName parent) 
  * listAttackPaths(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAttackPathsPagedCallable() 
  * listAttackPathsCallable() 

  
ListBigQueryExports |  Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBigQueryExports(ListBigQueryExportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBigQueryExports(FolderLocationName parent) 
  * listBigQueryExports(LocationName parent) 
  * listBigQueryExports(OrganizationLocationName parent) 
  * listBigQueryExports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBigQueryExportsPagedCallable() 
  * listBigQueryExportsCallable() 

  
ListFindings |  Lists an organization or source's findings.  To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:  \+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFindings(ListFindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFindings(SourceName parent) 
  * listFindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFindingsPagedCallable() 
  * listFindingsCallable() 

  
ListMuteConfigs |  Lists mute configs. If no location is specified, default is global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMuteConfigs(ListMuteConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMuteConfigs(FolderLocationName parent) 
  * listMuteConfigs(FolderName parent) 
  * listMuteConfigs(LocationName parent) 
  * listMuteConfigs(OrganizationLocationName parent) 
  * listMuteConfigs(OrganizationName parent) 
  * listMuteConfigs(ProjectName parent) 
  * listMuteConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMuteConfigsPagedCallable() 
  * listMuteConfigsCallable() 

  
ListNotificationConfigs |  Lists notification configs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNotificationConfigs(ListNotificationConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNotificationConfigs(FolderLocationName parent) 
  * listNotificationConfigs(LocationName parent) 
  * listNotificationConfigs(OrganizationLocationName parent) 
  * listNotificationConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNotificationConfigsPagedCallable() 
  * listNotificationConfigsCallable() 

  
ListResourceValueConfigs |  Lists all ResourceValueConfigs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listResourceValueConfigs(ListResourceValueConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listResourceValueConfigs(OrganizationLocationName parent) 
  * listResourceValueConfigs(OrganizationName parent) 
  * listResourceValueConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listResourceValueConfigsPagedCallable() 
  * listResourceValueConfigsCallable() 

  
ListSources |  Lists all sources belonging to an organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSources(ListSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSources(FolderName parent) 
  * listSources(OrganizationName parent) 
  * listSources(ProjectName parent) 
  * listSources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSourcesPagedCallable() 
  * listSourcesCallable() 

  
ListValuedResources |  Lists the valued resources for a set of simulation results and filter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listValuedResources(ListValuedResourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listValuedResources(SimulationName parent) 
  * listValuedResources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listValuedResourcesPagedCallable() 
  * listValuedResourcesCallable() 

  
SetFindingState |  Updates the state of a finding. If no location is specified, finding is assumed to be in global |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setFindingState(SetFindingStateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setFindingState(FindingName name, Finding.State state) 
  * setFindingState(String name, Finding.State state) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setFindingStateCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified Source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(ResourceName resource, Policy policy) 
  * setIamPolicy(String resource, Policy policy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetMute |  Updates the mute state of a finding. If no location is specified, finding is assumed to be in global |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMute(SetMuteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setMute(FindingName name, Finding.Mute mute) 
  * setMute(String name, Finding.Mute mute) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMuteCallable() 

  
TestIamPermissions |  Returns the permissions that a caller has on the specified source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(ResourceName resource, List<String> permissions) 
  * testIamPermissions(String resource, List<String> permissions) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
UpdateBigQueryExport |  Updates a BigQuery export. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBigQueryExport(UpdateBigQueryExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateBigQueryExport(BigQueryExport bigQueryExport, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBigQueryExportCallable() 

  
UpdateExternalSystem |  Updates external system. This is for a given finding. If no location is specified, finding is assumed to be in global |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExternalSystem(UpdateExternalSystemRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateExternalSystem(ExternalSystem externalSystem, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExternalSystemCallable() 

  
UpdateFinding |  Creates or updates a finding. If no location is specified, finding is assumed to be in global. The corresponding source must exist for a finding creation to succeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFinding(UpdateFindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateFinding(Finding finding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFindingCallable() 

  
UpdateMuteConfig |  Updates a mute config. If no location is specified, default is global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMuteConfig(UpdateMuteConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateMuteConfig(MuteConfig muteConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMuteConfigCallable() 

  
UpdateNotificationConfig |  Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNotificationConfig(UpdateNotificationConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateNotificationConfig(NotificationConfig notificationConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNotificationConfigCallable() 

  
UpdateResourceValueConfig |  Updates an existing ResourceValueConfigs with new rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateResourceValueConfig(UpdateResourceValueConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateResourceValueConfig(ResourceValueConfig resourceValueConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateResourceValueConfigCallable() 

  
UpdateSecurityMarks |  Updates security marks. For Finding Security marks, if no location is specified, finding is assumed to be in global. Assets Security Marks can only be accessed through global endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSecurityMarks(UpdateSecurityMarksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSecurityMarks(SecurityMarks securityMarks, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSecurityMarksCallable() 

  
UpdateSource |  Updates a source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSource(UpdateSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSource(Source source, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSourceCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SecurityCenterSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterSettings securityCenterSettings =
         SecurityCenterSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SecurityCenterClient securityCenterClient = SecurityCenterClient.create(securityCenterSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterSettings securityCenterSettings =
         SecurityCenterSettings.newBuilder().setEndpoint(myEndpoint).build();
     SecurityCenterClient securityCenterClient = SecurityCenterClient.create(securityCenterSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterSettings securityCenterSettings =
         SecurityCenterSettings.newHttpJsonBuilder().build();
     SecurityCenterClient securityCenterClient = SecurityCenterClient.create(securityCenterSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SecurityCenterClient

## Static Methods 

### create()
    
    
    public static final SecurityCenterClient create()

Constructs an instance of SecurityCenterClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityCenterSettings settings)
    
    
    public static final SecurityCenterClient create(SecurityCenterSettings settings)

Constructs an instance of SecurityCenterClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityCenterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityCenterStub stub)
    
    
    public static final SecurityCenterClient create(SecurityCenterStub stub)

Constructs an instance of SecurityCenterClient, using the given stub for making calls. This is for advanced usage - prefer using create(SecurityCenterSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityCenterStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.stub.SecurityCenterStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient)` |   
  
## Constructors 

### SecurityCenterClient(SecurityCenterSettings settings)
    
    
    protected SecurityCenterClient(SecurityCenterSettings settings)

Constructs an instance of SecurityCenterClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityCenterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterSettings)`  
  
  
### SecurityCenterClient(SecurityCenterStub stub)
    
    
    protected SecurityCenterClient(SecurityCenterStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityCenterStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.stub.SecurityCenterStub)`  
  
  
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
  
### batchCreateResourceValueConfigs(@Nullable OrganizationLocationName parent, List<CreateResourceValueConfigRequest> requests)
    
    
    public final BatchCreateResourceValueConfigsResponse batchCreateResourceValueConfigs(@Nullable OrganizationLocationName parent, List<CreateResourceValueConfigRequest> requests)

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       List<CreateResourceValueConfigRequest> requests = new ArrayList<>();
       BatchCreateResourceValueConfigsResponse response =
           securityCenterClient.batchCreateResourceValueConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. Resource name of the new ResourceValueConfig's parent. The parent field in the CreateResourceValueConfigRequest messages must either be empty or match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateResourceValueConfigRequest)>`  
Required. The resource value configs to be created.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsResponse)` |   
  
### batchCreateResourceValueConfigs(@Nullable OrganizationName parent, List<CreateResourceValueConfigRequest> requests)
    
    
    public final BatchCreateResourceValueConfigsResponse batchCreateResourceValueConfigs(@Nullable OrganizationName parent, List<CreateResourceValueConfigRequest> requests)

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       List<CreateResourceValueConfigRequest> requests = new ArrayList<>();
       BatchCreateResourceValueConfigsResponse response =
           securityCenterClient.batchCreateResourceValueConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. Resource name of the new ResourceValueConfig's parent. The parent field in the CreateResourceValueConfigRequest messages must either be empty or match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateResourceValueConfigRequest)>`  
Required. The resource value configs to be created.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsResponse)` |   
  
### batchCreateResourceValueConfigs(BatchCreateResourceValueConfigsRequest request)
    
    
    public final BatchCreateResourceValueConfigsResponse batchCreateResourceValueConfigs(BatchCreateResourceValueConfigsRequest request)

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BatchCreateResourceValueConfigsRequest request =
           BatchCreateResourceValueConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .addAllRequests(new ArrayList<CreateResourceValueConfigRequest>())
               .build();
       BatchCreateResourceValueConfigsResponse response =
           securityCenterClient.batchCreateResourceValueConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateResourceValueConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsResponse)` |   
  
### batchCreateResourceValueConfigs(String parent, List<CreateResourceValueConfigRequest> requests)
    
    
    public final BatchCreateResourceValueConfigsResponse batchCreateResourceValueConfigs(String parent, List<CreateResourceValueConfigRequest> requests)

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       List<CreateResourceValueConfigRequest> requests = new ArrayList<>();
       BatchCreateResourceValueConfigsResponse response =
           securityCenterClient.batchCreateResourceValueConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the new ResourceValueConfig's parent. The parent field in the CreateResourceValueConfigRequest messages must either be empty or match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateResourceValueConfigRequest)>`  
Required. The resource value configs to be created.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsResponse)` |   
  
### batchCreateResourceValueConfigsCallable()
    
    
    public final UnaryCallable<BatchCreateResourceValueConfigsRequest,BatchCreateResourceValueConfigsResponse> batchCreateResourceValueConfigsCallable()

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BatchCreateResourceValueConfigsRequest request =
           BatchCreateResourceValueConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .addAllRequests(new ArrayList<CreateResourceValueConfigRequest>())
               .build();
       ApiFuture<BatchCreateResourceValueConfigsResponse> future =
           securityCenterClient.batchCreateResourceValueConfigsCallable().futureCall(request);
       // Do something.
       BatchCreateResourceValueConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateResourceValueConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsRequest),[BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BatchCreateResourceValueConfigsResponse)>` |   
  
### bulkMuteFindingsAsync(@Nullable ResourceName parent)
    
    
    public final OperationFuture<BulkMuteFindingsResponse,Empty> bulkMuteFindingsAsync(@Nullable ResourceName parent)

Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceName parent = FolderName.of("[FOLDER]");
       BulkMuteFindingsResponse response = securityCenterClient.bulkMuteFindingsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
Required. The parent, at which bulk action needs to be applied. If no location is specified, findings are updated in global. The following list shows some examples: \+ `organizations/[organization_id]` \+ `organizations/[organization_id]/locations/[location_id]` \+ `folders/[folder_id]` \+ `folders/[folder_id]/locations/[location_id]` \+ `projects/[project_id]` \+ `projects/[project_id]/locations/[location_id]`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsResponse),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### bulkMuteFindingsAsync(BulkMuteFindingsRequest request)
    
    
    public final OperationFuture<BulkMuteFindingsResponse,Empty> bulkMuteFindingsAsync(BulkMuteFindingsRequest request)

Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BulkMuteFindingsRequest request =
           BulkMuteFindingsRequest.newBuilder()
               .setParent(FolderName.of("[FOLDER]").toString())
               .setFilter("filter-1274492040")
               .build();
       BulkMuteFindingsResponse response = securityCenterClient.bulkMuteFindingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsResponse),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### bulkMuteFindingsAsync(String parent)
    
    
    public final OperationFuture<BulkMuteFindingsResponse,Empty> bulkMuteFindingsAsync(String parent)

Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = FolderName.of("[FOLDER]").toString();
       BulkMuteFindingsResponse response = securityCenterClient.bulkMuteFindingsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, at which bulk action needs to be applied. If no location is specified, findings are updated in global. The following list shows some examples: \+ `organizations/[organization_id]` \+ `organizations/[organization_id]/locations/[location_id]` \+ `folders/[folder_id]` \+ `folders/[folder_id]/locations/[location_id]` \+ `projects/[project_id]` \+ `projects/[project_id]/locations/[location_id]`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsResponse),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### bulkMuteFindingsCallable()
    
    
    public final UnaryCallable<BulkMuteFindingsRequest,Operation> bulkMuteFindingsCallable()

Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BulkMuteFindingsRequest request =
           BulkMuteFindingsRequest.newBuilder()
               .setParent(FolderName.of("[FOLDER]").toString())
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Operation> future =
           securityCenterClient.bulkMuteFindingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### bulkMuteFindingsOperationCallable()
    
    
    public final OperationCallable<BulkMuteFindingsRequest,BulkMuteFindingsResponse,Empty> bulkMuteFindingsOperationCallable()

Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BulkMuteFindingsRequest request =
           BulkMuteFindingsRequest.newBuilder()
               .setParent(FolderName.of("[FOLDER]").toString())
               .setFilter("filter-1274492040")
               .build();
       OperationFuture<BulkMuteFindingsResponse, Empty> future =
           securityCenterClient.bulkMuteFindingsOperationCallable().futureCall(request);
       // Do something.
       BulkMuteFindingsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsRequest),[BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BulkMuteFindingsResponse),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### createBigQueryExport(@Nullable FolderLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)
    
    
    public final BigQueryExport createBigQueryExport(@Nullable FolderLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       BigQueryExport bigQueryExport = BigQueryExport.newBuilder().build();
       String bigQueryExportId = "bigQueryExportId1024198583";
       BigQueryExport response =
           securityCenterClient.createBigQueryExport(parent, bigQueryExport, bigQueryExportId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. The name of the parent resource of the new BigQuery export. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)`  
Required. The BigQuery export being created.  
`bigQueryExportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### createBigQueryExport(@Nullable LocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)
    
    
    public final BigQueryExport createBigQueryExport(@Nullable LocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BigQueryExport bigQueryExport = BigQueryExport.newBuilder().build();
       String bigQueryExportId = "bigQueryExportId1024198583";
       BigQueryExport response =
           securityCenterClient.createBigQueryExport(parent, bigQueryExport, bigQueryExportId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. The name of the parent resource of the new BigQuery export. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)`  
Required. The BigQuery export being created.  
`bigQueryExportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### createBigQueryExport(@Nullable OrganizationLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)
    
    
    public final BigQueryExport createBigQueryExport(@Nullable OrganizationLocationName parent, BigQueryExport bigQueryExport, String bigQueryExportId)

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       BigQueryExport bigQueryExport = BigQueryExport.newBuilder().build();
       String bigQueryExportId = "bigQueryExportId1024198583";
       BigQueryExport response =
           securityCenterClient.createBigQueryExport(parent, bigQueryExport, bigQueryExportId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. The name of the parent resource of the new BigQuery export. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)`  
Required. The BigQuery export being created.  
`bigQueryExportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### createBigQueryExport(CreateBigQueryExportRequest request)
    
    
    public final BigQueryExport createBigQueryExport(CreateBigQueryExportRequest request)

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateBigQueryExportRequest request =
           CreateBigQueryExportRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setBigQueryExport(BigQueryExport.newBuilder().build())
               .setBigQueryExportId("bigQueryExportId1024198583")
               .build();
       BigQueryExport response = securityCenterClient.createBigQueryExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### createBigQueryExport(String parent, BigQueryExport bigQueryExport, String bigQueryExportId)
    
    
    public final BigQueryExport createBigQueryExport(String parent, BigQueryExport bigQueryExport, String bigQueryExportId)

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       BigQueryExport bigQueryExport = BigQueryExport.newBuilder().build();
       String bigQueryExportId = "bigQueryExportId1024198583";
       BigQueryExport response =
           securityCenterClient.createBigQueryExport(parent, bigQueryExport, bigQueryExportId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource of the new BigQuery export. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)`  
Required. The BigQuery export being created.  
`bigQueryExportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### createBigQueryExportCallable()
    
    
    public final UnaryCallable<CreateBigQueryExportRequest,BigQueryExport> createBigQueryExportCallable()

Creates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateBigQueryExportRequest request =
           CreateBigQueryExportRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setBigQueryExport(BigQueryExport.newBuilder().build())
               .setBigQueryExportId("bigQueryExportId1024198583")
               .build();
       ApiFuture<BigQueryExport> future =
           securityCenterClient.createBigQueryExportCallable().futureCall(request);
       // Do something.
       BigQueryExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateBigQueryExportRequest),[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)>` |   
  
### createFinding(@Nullable SourceName parent, Finding finding, String findingId)
    
    
    public final Finding createFinding(@Nullable SourceName parent, Finding finding, String findingId)

Creates a finding in a location. The corresponding source must exist for finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SourceName parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       Finding finding = Finding.newBuilder().build();
       String findingId = "findingId439150212";
       Finding response = securityCenterClient.createFinding(parent, finding, findingId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SourceName`  
Required. Resource name of the new finding's parent. The following list shows some examples of the format: + `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`  
`finding` | `[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)`  
Required. The Finding being created. The name and security_marks will be ignored as they are both output only fields on this resource.  
`findingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be alphanumeric and less than or equal to 32 characters and greater than 0 characters in length.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### createFinding(CreateFindingRequest request)
    
    
    public final Finding createFinding(CreateFindingRequest request)

Creates a finding in a location. The corresponding source must exist for finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateFindingRequest request =
           CreateFindingRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFindingId("findingId439150212")
               .setFinding(Finding.newBuilder().build())
               .build();
       Finding response = securityCenterClient.createFinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### createFinding(String parent, Finding finding, String findingId)
    
    
    public final Finding createFinding(String parent, Finding finding, String findingId)

Creates a finding in a location. The corresponding source must exist for finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString();
       Finding finding = Finding.newBuilder().build();
       String findingId = "findingId439150212";
       Finding response = securityCenterClient.createFinding(parent, finding, findingId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the new finding's parent. The following list shows some examples of the format: + `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`  
`finding` | `[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)`  
Required. The Finding being created. The name and security_marks will be ignored as they are both output only fields on this resource.  
`findingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be alphanumeric and less than or equal to 32 characters and greater than 0 characters in length.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### createFindingCallable()
    
    
    public final UnaryCallable<CreateFindingRequest,Finding> createFindingCallable()

Creates a finding in a location. The corresponding source must exist for finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateFindingRequest request =
           CreateFindingRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFindingId("findingId439150212")
               .setFinding(Finding.newBuilder().build())
               .build();
       ApiFuture<Finding> future = securityCenterClient.createFindingCallable().futureCall(request);
       // Do something.
       Finding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest),[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)>` |   
  
### createMuteConfig(@Nullable FolderLocationName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable FolderLocationName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(@Nullable FolderName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable FolderName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(@Nullable LocationName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable LocationName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(@Nullable OrganizationLocationName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable OrganizationLocationName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(@Nullable OrganizationName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable OrganizationName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(@Nullable ProjectName parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(@Nullable ProjectName parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ProjectName`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(CreateMuteConfigRequest request)
    
    
    public final MuteConfig createMuteConfig(CreateMuteConfigRequest request)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateMuteConfigRequest request =
           CreateMuteConfigRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setMuteConfig(MuteConfig.newBuilder().build())
               .setMuteConfigId("muteConfigId1689669942")
               .build();
       MuteConfig response = securityCenterClient.createMuteConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateMuteConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfig(String parent, MuteConfig muteConfig, String muteConfigId)
    
    
    public final MuteConfig createMuteConfig(String parent, MuteConfig muteConfig, String muteConfigId)

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       String muteConfigId = "muteConfigId1689669942";
       MuteConfig response = securityCenterClient.createMuteConfig(parent, muteConfig, muteConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being created.  
`muteConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### createMuteConfigCallable()
    
    
    public final UnaryCallable<CreateMuteConfigRequest,MuteConfig> createMuteConfigCallable()

Creates a mute config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateMuteConfigRequest request =
           CreateMuteConfigRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setMuteConfig(MuteConfig.newBuilder().build())
               .setMuteConfigId("muteConfigId1689669942")
               .build();
       ApiFuture<MuteConfig> future =
           securityCenterClient.createMuteConfigCallable().futureCall(request);
       // Do something.
       MuteConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateMuteConfigRequest),[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)>` |   
  
### createNotificationConfig(@Nullable FolderLocationName parent, NotificationConfig notificationConfig, String configId)
    
    
    public final NotificationConfig createNotificationConfig(@Nullable FolderLocationName parent, NotificationConfig notificationConfig, String configId)

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       NotificationConfig notificationConfig = NotificationConfig.newBuilder().build();
       String configId = "configId-580140035";
       NotificationConfig response =
           securityCenterClient.createNotificationConfig(parent, notificationConfig, configId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. Resource name of the new notification config's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`notificationConfig` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)`  
Required. The notification config being created. The name and the service account will be ignored as they are both output only fields on this resource.  
`configId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### createNotificationConfig(@Nullable LocationName parent, NotificationConfig notificationConfig, String configId)
    
    
    public final NotificationConfig createNotificationConfig(@Nullable LocationName parent, NotificationConfig notificationConfig, String configId)

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NotificationConfig notificationConfig = NotificationConfig.newBuilder().build();
       String configId = "configId-580140035";
       NotificationConfig response =
           securityCenterClient.createNotificationConfig(parent, notificationConfig, configId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. Resource name of the new notification config's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`notificationConfig` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)`  
Required. The notification config being created. The name and the service account will be ignored as they are both output only fields on this resource.  
`configId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### createNotificationConfig(@Nullable OrganizationLocationName parent, NotificationConfig notificationConfig, String configId)
    
    
    public final NotificationConfig createNotificationConfig(@Nullable OrganizationLocationName parent, NotificationConfig notificationConfig, String configId)

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       NotificationConfig notificationConfig = NotificationConfig.newBuilder().build();
       String configId = "configId-580140035";
       NotificationConfig response =
           securityCenterClient.createNotificationConfig(parent, notificationConfig, configId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. Resource name of the new notification config's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`notificationConfig` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)`  
Required. The notification config being created. The name and the service account will be ignored as they are both output only fields on this resource.  
`configId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### createNotificationConfig(CreateNotificationConfigRequest request)
    
    
    public final NotificationConfig createNotificationConfig(CreateNotificationConfigRequest request)

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateNotificationConfigRequest request =
           CreateNotificationConfigRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setConfigId("configId-580140035")
               .setNotificationConfig(NotificationConfig.newBuilder().build())
               .build();
       NotificationConfig response = securityCenterClient.createNotificationConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateNotificationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### createNotificationConfig(String parent, NotificationConfig notificationConfig, String configId)
    
    
    public final NotificationConfig createNotificationConfig(String parent, NotificationConfig notificationConfig, String configId)

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       NotificationConfig notificationConfig = NotificationConfig.newBuilder().build();
       String configId = "configId-580140035";
       NotificationConfig response =
           securityCenterClient.createNotificationConfig(parent, notificationConfig, configId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the new notification config's parent. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
`notificationConfig` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)`  
Required. The notification config being created. The name and the service account will be ignored as they are both output only fields on this resource.  
`configId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### createNotificationConfigCallable()
    
    
    public final UnaryCallable<CreateNotificationConfigRequest,NotificationConfig> createNotificationConfigCallable()

Creates a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateNotificationConfigRequest request =
           CreateNotificationConfigRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setConfigId("configId-580140035")
               .setNotificationConfig(NotificationConfig.newBuilder().build())
               .build();
       ApiFuture<NotificationConfig> future =
           securityCenterClient.createNotificationConfigCallable().futureCall(request);
       // Do something.
       NotificationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateNotificationConfigRequest),[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)>` |   
  
### createSource(@Nullable OrganizationName parent, Source source)
    
    
    public final Source createSource(@Nullable OrganizationName parent, Source source)

Creates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       Source source = Source.newBuilder().build();
       Source response = securityCenterClient.createSource(parent, source);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. Resource name of the new source's parent. Its format should be `organizations/[organization_id]`.  
`source` | `[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)`  
Required. The Source being created, only the display_name and description will be used. All other fields will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### createSource(CreateSourceRequest request)
    
    
    public final Source createSource(CreateSourceRequest request)

Creates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateSourceRequest request =
           CreateSourceRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setSource(Source.newBuilder().build())
               .build();
       Source response = securityCenterClient.createSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### createSource(String parent, Source source)
    
    
    public final Source createSource(String parent, Source source)

Creates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       Source source = Source.newBuilder().build();
       Source response = securityCenterClient.createSource(parent, source);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the new source's parent. Its format should be `organizations/[organization_id]`.  
`source` | `[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)`  
Required. The Source being created, only the display_name and description will be used. All other fields will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### createSourceCallable()
    
    
    public final UnaryCallable<CreateSourceRequest,Source> createSourceCallable()

Creates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       CreateSourceRequest request =
           CreateSourceRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setSource(Source.newBuilder().build())
               .build();
       ApiFuture<Source> future = securityCenterClient.createSourceCallable().futureCall(request);
       // Do something.
       Source response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)>` |   
  
### deleteBigQueryExport(@Nullable BigQueryExportName name)
    
    
    public final void deleteBigQueryExport(@Nullable BigQueryExportName name)

Deletes an existing BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BigQueryExportName name =
           BigQueryExportName.ofOrganizationLocationExportName(
               "[ORGANIZATION]", "[LOCATION]", "[EXPORT]");
       securityCenterClient.deleteBigQueryExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.BigQueryExportName`  
Required. The name of the BigQuery export to delete. The following list shows some examples of the format: \+ `organizations/{organization}/locations/{location}/bigQueryExports/{export_id}` \+ `folders/{folder}/locations/{location}/bigQueryExports/{export_id}` \+ `projects/{project}/locations/{location}/bigQueryExports/{export_id}`  
  
### deleteBigQueryExport(DeleteBigQueryExportRequest request)
    
    
    public final void deleteBigQueryExport(DeleteBigQueryExportRequest request)

Deletes an existing BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteBigQueryExportRequest request =
           DeleteBigQueryExportRequest.newBuilder()
               .setName(
                   BigQueryExportName.ofOrganizationLocationExportName(
                           "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
                       .toString())
               .build();
       securityCenterClient.deleteBigQueryExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteBigQueryExport(String name)
    
    
    public final void deleteBigQueryExport(String name)

Deletes an existing BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           BigQueryExportName.ofOrganizationLocationExportName(
                   "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
               .toString();
       securityCenterClient.deleteBigQueryExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the BigQuery export to delete. The following list shows some examples of the format: \+ `organizations/{organization}/locations/{location}/bigQueryExports/{export_id}` \+ `folders/{folder}/locations/{location}/bigQueryExports/{export_id}` \+ `projects/{project}/locations/{location}/bigQueryExports/{export_id}`  
  
### deleteBigQueryExportCallable()
    
    
    public final UnaryCallable<DeleteBigQueryExportRequest,Empty> deleteBigQueryExportCallable()

Deletes an existing BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteBigQueryExportRequest request =
           DeleteBigQueryExportRequest.newBuilder()
               .setName(
                   BigQueryExportName.ofOrganizationLocationExportName(
                           "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           securityCenterClient.deleteBigQueryExportCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteBigQueryExportRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMuteConfig(@Nullable MuteConfigName name)
    
    
    public final void deleteMuteConfig(@Nullable MuteConfigName name)

Deletes an existing mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       MuteConfigName name =
           MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]");
       securityCenterClient.deleteMuteConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.MuteConfigName`  
Required. Name of the mute config to delete. The following list shows some examples of the format: \+ `organizations/{organization}/muteConfigs/{config_id}` \+ `organizations/{organization}/locations/{location}/muteConfigs/{config_id}` \+ `folders/{folder}/muteConfigs/{config_id}` \+ `folders/{folder}/locations/{location}/muteConfigs/{config_id}` \+ `projects/{project}/muteConfigs/{config_id}` \+ `projects/{project}/locations/{location}/muteConfigs/{config_id}`  
  
### deleteMuteConfig(DeleteMuteConfigRequest request)
    
    
    public final void deleteMuteConfig(DeleteMuteConfigRequest request)

Deletes an existing mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteMuteConfigRequest request =
           DeleteMuteConfigRequest.newBuilder()
               .setName(
                   MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]")
                       .toString())
               .build();
       securityCenterClient.deleteMuteConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteMuteConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteMuteConfig(String name)
    
    
    public final void deleteMuteConfig(String name)

Deletes an existing mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]").toString();
       securityCenterClient.deleteMuteConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the mute config to delete. The following list shows some examples of the format: \+ `organizations/{organization}/muteConfigs/{config_id}` \+ `organizations/{organization}/locations/{location}/muteConfigs/{config_id}` \+ `folders/{folder}/muteConfigs/{config_id}` \+ `folders/{folder}/locations/{location}/muteConfigs/{config_id}` \+ `projects/{project}/muteConfigs/{config_id}` \+ `projects/{project}/locations/{location}/muteConfigs/{config_id}`  
  
### deleteMuteConfigCallable()
    
    
    public final UnaryCallable<DeleteMuteConfigRequest,Empty> deleteMuteConfigCallable()

Deletes an existing mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteMuteConfigRequest request =
           DeleteMuteConfigRequest.newBuilder()
               .setName(
                   MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future = securityCenterClient.deleteMuteConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteMuteConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteNotificationConfig(@Nullable NotificationConfigName name)
    
    
    public final void deleteNotificationConfig(@Nullable NotificationConfigName name)

Deletes a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       NotificationConfigName name =
           NotificationConfigName.ofOrganizationLocationNotificationConfigName(
               "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]");
       securityCenterClient.deleteNotificationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.NotificationConfigName`  
Required. Name of the notification config to delete. The following list shows some examples of the format: \+ `organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `folders/[folder_id]/locations/[location_id]notificationConfigs/[config_id]` \+ `projects/[project_id]/locations/[location_id]notificationConfigs/[config_id]`  
  
### deleteNotificationConfig(DeleteNotificationConfigRequest request)
    
    
    public final void deleteNotificationConfig(DeleteNotificationConfigRequest request)

Deletes a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteNotificationConfigRequest request =
           DeleteNotificationConfigRequest.newBuilder()
               .setName(
                   NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
                       .toString())
               .build();
       securityCenterClient.deleteNotificationConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteNotificationConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteNotificationConfig(String name)
    
    
    public final void deleteNotificationConfig(String name)

Deletes a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                   "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
               .toString();
       securityCenterClient.deleteNotificationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the notification config to delete. The following list shows some examples of the format: \+ `organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `folders/[folder_id]/locations/[location_id]notificationConfigs/[config_id]` \+ `projects/[project_id]/locations/[location_id]notificationConfigs/[config_id]`  
  
### deleteNotificationConfigCallable()
    
    
    public final UnaryCallable<DeleteNotificationConfigRequest,Empty> deleteNotificationConfigCallable()

Deletes a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteNotificationConfigRequest request =
           DeleteNotificationConfigRequest.newBuilder()
               .setName(
                   NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           securityCenterClient.deleteNotificationConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteNotificationConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteResourceValueConfig(@Nullable ResourceValueConfigName name)
    
    
    public final void deleteResourceValueConfig(@Nullable ResourceValueConfigName name)

Deletes a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceValueConfigName name =
           ResourceValueConfigName.ofOrganizationResourceValueConfigName(
               "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]");
       securityCenterClient.deleteResourceValueConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ResourceValueConfigName`  
Required. Name of the ResourceValueConfig to delete  
  
### deleteResourceValueConfig(DeleteResourceValueConfigRequest request)
    
    
    public final void deleteResourceValueConfig(DeleteResourceValueConfigRequest request)

Deletes a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteResourceValueConfigRequest request =
           DeleteResourceValueConfigRequest.newBuilder()
               .setName(
                   ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                           "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
                       .toString())
               .build();
       securityCenterClient.deleteResourceValueConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteResourceValueConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteResourceValueConfig(String name)
    
    
    public final void deleteResourceValueConfig(String name)

Deletes a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                   "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
               .toString();
       securityCenterClient.deleteResourceValueConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the ResourceValueConfig to delete  
  
### deleteResourceValueConfigCallable()
    
    
    public final UnaryCallable<DeleteResourceValueConfigRequest,Empty> deleteResourceValueConfigCallable()

Deletes a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       DeleteResourceValueConfigRequest request =
           DeleteResourceValueConfigRequest.newBuilder()
               .setName(
                   ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                           "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           securityCenterClient.deleteResourceValueConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.DeleteResourceValueConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getBigQueryExport(@Nullable BigQueryExportName name)
    
    
    public final BigQueryExport getBigQueryExport(@Nullable BigQueryExportName name)

Gets a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BigQueryExportName name =
           BigQueryExportName.ofOrganizationLocationExportName(
               "[ORGANIZATION]", "[LOCATION]", "[EXPORT]");
       BigQueryExport response = securityCenterClient.getBigQueryExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.BigQueryExportName`  
Required. Name of the BigQuery export to retrieve. The following list shows some examples of the format: \+ `organizations/{organization}/locations/{location}/bigQueryExports/{export_id}` \+ `folders/{folder}/locations/{location}/bigQueryExports/{export_id}` \+ `projects/{project}locations/{location}//bigQueryExports/{export_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### getBigQueryExport(GetBigQueryExportRequest request)
    
    
    public final BigQueryExport getBigQueryExport(GetBigQueryExportRequest request)

Gets a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetBigQueryExportRequest request =
           GetBigQueryExportRequest.newBuilder()
               .setName(
                   BigQueryExportName.ofOrganizationLocationExportName(
                           "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
                       .toString())
               .build();
       BigQueryExport response = securityCenterClient.getBigQueryExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### getBigQueryExport(String name)
    
    
    public final BigQueryExport getBigQueryExport(String name)

Gets a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           BigQueryExportName.ofOrganizationLocationExportName(
                   "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
               .toString();
       BigQueryExport response = securityCenterClient.getBigQueryExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the BigQuery export to retrieve. The following list shows some examples of the format: \+ `organizations/{organization}/locations/{location}/bigQueryExports/{export_id}` \+ `folders/{folder}/locations/{location}/bigQueryExports/{export_id}` \+ `projects/{project}locations/{location}//bigQueryExports/{export_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### getBigQueryExportCallable()
    
    
    public final UnaryCallable<GetBigQueryExportRequest,BigQueryExport> getBigQueryExportCallable()

Gets a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetBigQueryExportRequest request =
           GetBigQueryExportRequest.newBuilder()
               .setName(
                   BigQueryExportName.ofOrganizationLocationExportName(
                           "[ORGANIZATION]", "[LOCATION]", "[EXPORT]")
                       .toString())
               .build();
       ApiFuture<BigQueryExport> future =
           securityCenterClient.getBigQueryExportCallable().futureCall(request);
       // Do something.
       BigQueryExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetBigQueryExportRequest),[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(@Nullable ResourceName resource)
    
    
    public final Policy getIamPolicy(@Nullable ResourceName resource)

Gets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceName resource = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       Policy response = securityCenterClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = securityCenterClient.getIamPolicy(request);
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
  
### getIamPolicy(String resource)
    
    
    public final Policy getIamPolicy(String resource)

Gets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String resource = FolderName.of("[FOLDER]").toString();
       Policy response = securityCenterClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = securityCenterClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getMuteConfig(@Nullable MuteConfigName name)
    
    
    public final MuteConfig getMuteConfig(@Nullable MuteConfigName name)

Gets a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       MuteConfigName name =
           MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]");
       MuteConfig response = securityCenterClient.getMuteConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.MuteConfigName`  
Required. Name of the mute config to retrieve. The following list shows some examples of the format: \+ `organizations/{organization}/muteConfigs/{config_id}` \+ `organizations/{organization}/locations/{location}/muteConfigs/{config_id}` \+ `folders/{folder}/muteConfigs/{config_id}` \+ `folders/{folder}/locations/{location}/muteConfigs/{config_id}` \+ `projects/{project}/muteConfigs/{config_id}` \+ `projects/{project}/locations/{location}/muteConfigs/{config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### getMuteConfig(GetMuteConfigRequest request)
    
    
    public final MuteConfig getMuteConfig(GetMuteConfigRequest request)

Gets a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetMuteConfigRequest request =
           GetMuteConfigRequest.newBuilder()
               .setName(
                   MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]")
                       .toString())
               .build();
       MuteConfig response = securityCenterClient.getMuteConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetMuteConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### getMuteConfig(String name)
    
    
    public final MuteConfig getMuteConfig(String name)

Gets a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]").toString();
       MuteConfig response = securityCenterClient.getMuteConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the mute config to retrieve. The following list shows some examples of the format: \+ `organizations/{organization}/muteConfigs/{config_id}` \+ `organizations/{organization}/locations/{location}/muteConfigs/{config_id}` \+ `folders/{folder}/muteConfigs/{config_id}` \+ `folders/{folder}/locations/{location}/muteConfigs/{config_id}` \+ `projects/{project}/muteConfigs/{config_id}` \+ `projects/{project}/locations/{location}/muteConfigs/{config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### getMuteConfigCallable()
    
    
    public final UnaryCallable<GetMuteConfigRequest,MuteConfig> getMuteConfigCallable()

Gets a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetMuteConfigRequest request =
           GetMuteConfigRequest.newBuilder()
               .setName(
                   MuteConfigName.ofOrganizationMuteConfigName("[ORGANIZATION]", "[MUTE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<MuteConfig> future =
           securityCenterClient.getMuteConfigCallable().futureCall(request);
       // Do something.
       MuteConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetMuteConfigRequest),[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)>` |   
  
### getNotificationConfig(@Nullable NotificationConfigName name)
    
    
    public final NotificationConfig getNotificationConfig(@Nullable NotificationConfigName name)

Gets a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       NotificationConfigName name =
           NotificationConfigName.ofOrganizationLocationNotificationConfigName(
               "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]");
       NotificationConfig response = securityCenterClient.getNotificationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.NotificationConfigName`  
Required. Name of the notification config to get. The following list shows some examples of the format: \+ `organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `folders/[folder_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `projects/[project_id]/locations/[location_id]/notificationConfigs/[config_id]`  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### getNotificationConfig(GetNotificationConfigRequest request)
    
    
    public final NotificationConfig getNotificationConfig(GetNotificationConfigRequest request)

Gets a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetNotificationConfigRequest request =
           GetNotificationConfigRequest.newBuilder()
               .setName(
                   NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
                       .toString())
               .build();
       NotificationConfig response = securityCenterClient.getNotificationConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetNotificationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### getNotificationConfig(String name)
    
    
    public final NotificationConfig getNotificationConfig(String name)

Gets a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                   "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
               .toString();
       NotificationConfig response = securityCenterClient.getNotificationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the notification config to get. The following list shows some examples of the format: \+ `organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `folders/[folder_id]/locations/[location_id]/notificationConfigs/[config_id]` \+ `projects/[project_id]/locations/[location_id]/notificationConfigs/[config_id]`  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### getNotificationConfigCallable()
    
    
    public final UnaryCallable<GetNotificationConfigRequest,NotificationConfig> getNotificationConfigCallable()

Gets a notification config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetNotificationConfigRequest request =
           GetNotificationConfigRequest.newBuilder()
               .setName(
                   NotificationConfigName.ofOrganizationLocationNotificationConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[NOTIFICATION_CONFIG]")
                       .toString())
               .build();
       ApiFuture<NotificationConfig> future =
           securityCenterClient.getNotificationConfigCallable().futureCall(request);
       // Do something.
       NotificationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetNotificationConfigRequest),[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getResourceValueConfig(@Nullable ResourceValueConfigName name)
    
    
    public final ResourceValueConfig getResourceValueConfig(@Nullable ResourceValueConfigName name)

Gets a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceValueConfigName name =
           ResourceValueConfigName.ofOrganizationResourceValueConfigName(
               "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]");
       ResourceValueConfig response = securityCenterClient.getResourceValueConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ResourceValueConfigName`  
Required. Name of the resource value config to retrieve. Its format is organizations/{organization}/resourceValueConfigs/{config_id}.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)` |   
  
### getResourceValueConfig(GetResourceValueConfigRequest request)
    
    
    public final ResourceValueConfig getResourceValueConfig(GetResourceValueConfigRequest request)

Gets a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetResourceValueConfigRequest request =
           GetResourceValueConfigRequest.newBuilder()
               .setName(
                   ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                           "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
                       .toString())
               .build();
       ResourceValueConfig response = securityCenterClient.getResourceValueConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetResourceValueConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)` |   
  
### getResourceValueConfig(String name)
    
    
    public final ResourceValueConfig getResourceValueConfig(String name)

Gets a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                   "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
               .toString();
       ResourceValueConfig response = securityCenterClient.getResourceValueConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource value config to retrieve. Its format is organizations/{organization}/resourceValueConfigs/{config_id}.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)` |   
  
### getResourceValueConfigCallable()
    
    
    public final UnaryCallable<GetResourceValueConfigRequest,ResourceValueConfig> getResourceValueConfigCallable()

Gets a ResourceValueConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetResourceValueConfigRequest request =
           GetResourceValueConfigRequest.newBuilder()
               .setName(
                   ResourceValueConfigName.ofOrganizationResourceValueConfigName(
                           "[ORGANIZATION]", "[RESOURCE_VALUE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<ResourceValueConfig> future =
           securityCenterClient.getResourceValueConfigCallable().futureCall(request);
       // Do something.
       ResourceValueConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetResourceValueConfigRequest),[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable SecurityCenterSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SecurityCenterSettings` |   
  
### getSimulation(@Nullable SimulationName name)
    
    
    public final Simulation getSimulation(@Nullable SimulationName name)

Get the simulation by name or the latest simulation for the given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SimulationName name =
           SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]");
       Simulation response = securityCenterClient.getSimulation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SimulationName`  
Required. The organization name or simulation name of this simulation Valid format: `organizations/{organization}/simulations/latest` `organizations/{organization}/simulations/{simulation}`  
**Returns**  
---  
**Type** | **Description**  
`[Simulation](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Simulation)` |   
  
### getSimulation(GetSimulationRequest request)
    
    
    public final Simulation getSimulation(GetSimulationRequest request)

Get the simulation by name or the latest simulation for the given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetSimulationRequest request =
           GetSimulationRequest.newBuilder()
               .setName(
                   SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]")
                       .toString())
               .build();
       Simulation response = securityCenterClient.getSimulation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSimulationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSimulationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Simulation](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Simulation)` |   
  
### getSimulation(String name)
    
    
    public final Simulation getSimulation(String name)

Get the simulation by name or the latest simulation for the given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]").toString();
       Simulation response = securityCenterClient.getSimulation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The organization name or simulation name of this simulation Valid format: `organizations/{organization}/simulations/latest` `organizations/{organization}/simulations/{simulation}`  
**Returns**  
---  
**Type** | **Description**  
`[Simulation](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Simulation)` |   
  
### getSimulationCallable()
    
    
    public final UnaryCallable<GetSimulationRequest,Simulation> getSimulationCallable()

Get the simulation by name or the latest simulation for the given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetSimulationRequest request =
           GetSimulationRequest.newBuilder()
               .setName(
                   SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]")
                       .toString())
               .build();
       ApiFuture<Simulation> future =
           securityCenterClient.getSimulationCallable().futureCall(request);
       // Do something.
       Simulation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSimulationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSimulationRequest),[Simulation](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Simulation)>` |   
  
### getSource(@Nullable SourceName name)
    
    
    public final Source getSource(@Nullable SourceName name)

Gets a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SourceName name = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       Source response = securityCenterClient.getSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SourceName`  
Required. Relative resource name of the source. Its format is `organizations/[organization_id]/source/[source_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### getSource(GetSourceRequest request)
    
    
    public final Source getSource(GetSourceRequest request)

Gets a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetSourceRequest request =
           GetSourceRequest.newBuilder()
               .setName(SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .build();
       Source response = securityCenterClient.getSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### getSource(String name)
    
    
    public final Source getSource(String name)

Gets a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString();
       Source response = securityCenterClient.getSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Relative resource name of the source. Its format is `organizations/[organization_id]/source/[source_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### getSourceCallable()
    
    
    public final UnaryCallable<GetSourceRequest,Source> getSourceCallable()

Gets a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetSourceRequest request =
           GetSourceRequest.newBuilder()
               .setName(SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .build();
       ApiFuture<Source> future = securityCenterClient.getSourceCallable().futureCall(request);
       // Do something.
       Source response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)>` |   
  
### getStub()
    
    
    public SecurityCenterStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.stub.SecurityCenterStub)` |   
  
### getValuedResource(@Nullable ValuedResourceName name)
    
    
    public final ValuedResource getValuedResource(@Nullable ValuedResourceName name)

Get the valued resource by name

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ValuedResourceName name =
           ValuedResourceName.ofOrganizationSimulationValuedResourceName(
               "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]");
       ValuedResource response = securityCenterClient.getValuedResource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ValuedResourceName`  
Required. The name of this valued resource Valid format: `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[ValuedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ValuedResource)` |   
  
### getValuedResource(GetValuedResourceRequest request)
    
    
    public final ValuedResource getValuedResource(GetValuedResourceRequest request)

Get the valued resource by name

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetValuedResourceRequest request =
           GetValuedResourceRequest.newBuilder()
               .setName(
                   ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                           "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
                       .toString())
               .build();
       ValuedResource response = securityCenterClient.getValuedResource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetValuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetValuedResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ValuedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ValuedResource)` |   
  
### getValuedResource(String name)
    
    
    public final ValuedResource getValuedResource(String name)

Get the valued resource by name

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                   "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
               .toString();
       ValuedResource response = securityCenterClient.getValuedResource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of this valued resource Valid format: `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[ValuedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ValuedResource)` |   
  
### getValuedResourceCallable()
    
    
    public final UnaryCallable<GetValuedResourceRequest,ValuedResource> getValuedResourceCallable()

Get the valued resource by name

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GetValuedResourceRequest request =
           GetValuedResourceRequest.newBuilder()
               .setName(
                   ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                           "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
                       .toString())
               .build();
       ApiFuture<ValuedResource> future =
           securityCenterClient.getValuedResourceCallable().futureCall(request);
       // Do something.
       ValuedResource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetValuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetValuedResourceRequest),[ValuedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ValuedResource)>` |   
  
### groupFindings(@Nullable SourceName parent, String groupBy)
    
    
    public final SecurityCenterClient.GroupFindingsPagedResponse groupFindings(@Nullable SourceName parent, String groupBy)

Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global

To group across all sources provide a `-` as the source id. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SourceName parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       String groupBy = "groupBy293428022";
       for (GroupResult element : securityCenterClient.groupFindings(parent, groupBy).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SourceName`  
Required. Name of the source to groupBy. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]` \+ `folders/[folder_id]/sources/[source_id]` \+ `folders/[folder_id]/sources/[source_id]/locations/[location_id]` \+ `projects/[project_id]/sources/[source_id]` \+ `projects/[project_id]/sources/[source_id]/locations/[location_id]` To groupBy across all sources provide a source_id of `-`. The following list shows some examples: \+ `organizations/{organization_id}/sources/-` \+ `organizations/{organization_id}/sources/-/locations/[location_id]` \+ `folders/{folder_id}/sources/-` \+ `folders/{folder_id}/sources/-/locations/[location_id]` \+ `projects/{project_id}/sources/-` \+ `projects/{project_id}/sources/-/locations/[location_id]`  
`groupBy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Expression that defines what assets fields to use for grouping. The string value should follow SQL syntax: comma separated list of fields. For example: "parent,resource_name".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.GroupFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.GroupFindingsPagedResponse)` |   
  
### groupFindings(GroupFindingsRequest request)
    
    
    public final SecurityCenterClient.GroupFindingsPagedResponse groupFindings(GroupFindingsRequest request)

Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global

To group across all sources provide a `-` as the source id. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GroupFindingsRequest request =
           GroupFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setGroupBy("groupBy293428022")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (GroupResult element : securityCenterClient.groupFindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GroupFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GroupFindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.GroupFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.GroupFindingsPagedResponse)` |   
  
### groupFindings(String parent, String groupBy)
    
    
    public final SecurityCenterClient.GroupFindingsPagedResponse groupFindings(String parent, String groupBy)

Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global

To group across all sources provide a `-` as the source id. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString();
       String groupBy = "groupBy293428022";
       for (GroupResult element : securityCenterClient.groupFindings(parent, groupBy).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the source to groupBy. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]` \+ `folders/[folder_id]/sources/[source_id]` \+ `folders/[folder_id]/sources/[source_id]/locations/[location_id]` \+ `projects/[project_id]/sources/[source_id]` \+ `projects/[project_id]/sources/[source_id]/locations/[location_id]` To groupBy across all sources provide a source_id of `-`. The following list shows some examples: \+ `organizations/{organization_id}/sources/-` \+ `organizations/{organization_id}/sources/-/locations/[location_id]` \+ `folders/{folder_id}/sources/-` \+ `folders/{folder_id}/sources/-/locations/[location_id]` \+ `projects/{project_id}/sources/-` \+ `projects/{project_id}/sources/-/locations/[location_id]`  
`groupBy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Expression that defines what assets fields to use for grouping. The string value should follow SQL syntax: comma separated list of fields. For example: "parent,resource_name".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.GroupFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.GroupFindingsPagedResponse)` |   
  
### groupFindingsCallable()
    
    
    public final UnaryCallable<GroupFindingsRequest,GroupFindingsResponse> groupFindingsCallable()

Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global

To group across all sources provide a `-` as the source id. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GroupFindingsRequest request =
           GroupFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setGroupBy("groupBy293428022")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         GroupFindingsResponse response = securityCenterClient.groupFindingsCallable().call(request);
         for (GroupResult element : response.getGroupByResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GroupFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GroupFindingsRequest),[GroupFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GroupFindingsResponse)>` |   
  
### groupFindingsPagedCallable()
    
    
    public final UnaryCallable<GroupFindingsRequest,SecurityCenterClient.GroupFindingsPagedResponse> groupFindingsPagedCallable()

Filters an organization or source's findings and groups them by their specified properties in a location. If no location is specified, findings are assumed to be in global

To group across all sources provide a `-` as the source id. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings` \+ `/v2/folders/{folder_id}/sources/-/findings` \+ `/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings` \+ `/v2/projects/{project_id}/sources/-/findings` \+ `/v2/projects/{project_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       GroupFindingsRequest request =
           GroupFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setGroupBy("groupBy293428022")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<GroupResult> future =
           securityCenterClient.groupFindingsPagedCallable().futureCall(request);
       // Do something.
       for (GroupResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GroupFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GroupFindingsRequest),[GroupFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.GroupFindingsPagedResponse)>` |   
  
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
  
### listAttackPaths(@Nullable OrganizationValuedResourceName parent)
    
    
    public final SecurityCenterClient.ListAttackPathsPagedResponse listAttackPaths(@Nullable OrganizationValuedResourceName parent)

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationValuedResourceName parent =
           OrganizationValuedResourceName.of(
               "[ORGANIZATION]", "[LOCATION]", "[SIMULATION]", "[VALUED_RESOURCE]");
       for (AttackPath element : securityCenterClient.listAttackPaths(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationValuedResourceName`  
Required. Name of parent to list attack paths. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListAttackPathsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListAttackPathsPagedResponse)` |   
  
### listAttackPaths(@Nullable ValuedResourceName parent)
    
    
    public final SecurityCenterClient.ListAttackPathsPagedResponse listAttackPaths(@Nullable ValuedResourceName parent)

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ValuedResourceName parent =
           ValuedResourceName.ofOrganizationSimulationValuedResourceName(
               "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]");
       for (AttackPath element : securityCenterClient.listAttackPaths(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ValuedResourceName`  
Required. Name of parent to list attack paths. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListAttackPathsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListAttackPathsPagedResponse)` |   
  
### listAttackPaths(ListAttackPathsRequest request)
    
    
    public final SecurityCenterClient.ListAttackPathsPagedResponse listAttackPaths(ListAttackPathsRequest request)

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListAttackPathsRequest request =
           ListAttackPathsRequest.newBuilder()
               .setParent(
                   ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                           "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (AttackPath element : securityCenterClient.listAttackPaths(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAttackPathsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListAttackPathsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListAttackPathsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListAttackPathsPagedResponse)` |   
  
### listAttackPaths(String parent)
    
    
    public final SecurityCenterClient.ListAttackPathsPagedResponse listAttackPaths(String parent)

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent =
           ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                   "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
               .toString();
       for (AttackPath element : securityCenterClient.listAttackPaths(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list attack paths. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListAttackPathsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListAttackPathsPagedResponse)` |   
  
### listAttackPathsCallable()
    
    
    public final UnaryCallable<ListAttackPathsRequest,ListAttackPathsResponse> listAttackPathsCallable()

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListAttackPathsRequest request =
           ListAttackPathsRequest.newBuilder()
               .setParent(
                   ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                           "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListAttackPathsResponse response =
             securityCenterClient.listAttackPathsCallable().call(request);
         for (AttackPath element : response.getAttackPathsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAttackPathsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListAttackPathsRequest),[ListAttackPathsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListAttackPathsResponse)>` |   
  
### listAttackPathsPagedCallable()
    
    
    public final UnaryCallable<ListAttackPathsRequest,SecurityCenterClient.ListAttackPathsPagedResponse> listAttackPathsPagedCallable()

Lists the attack paths for a set of simulation results or valued resources and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListAttackPathsRequest request =
           ListAttackPathsRequest.newBuilder()
               .setParent(
                   ValuedResourceName.ofOrganizationSimulationValuedResourceName(
                           "[ORGANIZATION]", "[SIMULATION]", "[VALUED_RESOURCE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<AttackPath> future =
           securityCenterClient.listAttackPathsPagedCallable().futureCall(request);
       // Do something.
       for (AttackPath element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAttackPathsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListAttackPathsRequest),[ListAttackPathsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListAttackPathsPagedResponse)>` |   
  
### listBigQueryExports(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterClient.ListBigQueryExportsPagedResponse listBigQueryExports(@Nullable FolderLocationName parent)

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (BigQueryExport element : securityCenterClient.listBigQueryExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. The parent, which owns the collection of BigQuery exports. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)` |   
  
### listBigQueryExports(@Nullable LocationName parent)
    
    
    public final SecurityCenterClient.ListBigQueryExportsPagedResponse listBigQueryExports(@Nullable LocationName parent)

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BigQueryExport element : securityCenterClient.listBigQueryExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. The parent, which owns the collection of BigQuery exports. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)` |   
  
### listBigQueryExports(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterClient.ListBigQueryExportsPagedResponse listBigQueryExports(@Nullable OrganizationLocationName parent)

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (BigQueryExport element : securityCenterClient.listBigQueryExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. The parent, which owns the collection of BigQuery exports. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)` |   
  
### listBigQueryExports(ListBigQueryExportsRequest request)
    
    
    public final SecurityCenterClient.ListBigQueryExportsPagedResponse listBigQueryExports(ListBigQueryExportsRequest request)

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListBigQueryExportsRequest request =
           ListBigQueryExportsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BigQueryExport element :
           securityCenterClient.listBigQueryExports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListBigQueryExportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)` |   
  
### listBigQueryExports(String parent)
    
    
    public final SecurityCenterClient.ListBigQueryExportsPagedResponse listBigQueryExports(String parent)

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (BigQueryExport element : securityCenterClient.listBigQueryExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns the collection of BigQuery exports. Its format is `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, or `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)` |   
  
### listBigQueryExportsCallable()
    
    
    public final UnaryCallable<ListBigQueryExportsRequest,ListBigQueryExportsResponse> listBigQueryExportsCallable()

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListBigQueryExportsRequest request =
           ListBigQueryExportsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBigQueryExportsResponse response =
             securityCenterClient.listBigQueryExportsCallable().call(request);
         for (BigQueryExport element : response.getBigQueryExportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListBigQueryExportsRequest),[ListBigQueryExportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListBigQueryExportsResponse)>` |   
  
### listBigQueryExportsPagedCallable()
    
    
    public final UnaryCallable<ListBigQueryExportsRequest,SecurityCenterClient.ListBigQueryExportsPagedResponse> listBigQueryExportsPagedCallable()

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListBigQueryExportsRequest request =
           ListBigQueryExportsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BigQueryExport> future =
           securityCenterClient.listBigQueryExportsPagedCallable().futureCall(request);
       // Do something.
       for (BigQueryExport element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListBigQueryExportsRequest),[ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListBigQueryExportsPagedResponse)>` |   
  
### listFindings(@Nullable SourceName parent)
    
    
    public final SecurityCenterClient.ListFindingsPagedResponse listFindings(@Nullable SourceName parent)

Lists an organization or source's findings.

To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SourceName parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       for (ListFindingsResponse.ListFindingsResult element :
           securityCenterClient.listFindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SourceName`  
Required. Name of the source the findings belong to. If no location is specified, the default is global. The following list shows some examples: \+ `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]` \+ `folders/[folder_id]/sources/[source_id]` \+ `folders/[folder_id]/sources/[source_id]/locations/[location_id]` \+ `projects/[project_id]/sources/[source_id]` \+ `projects/[project_id]/sources/[source_id]/locations/[location_id]` To list across all sources provide a source_id of `-`. The following list shows some examples: \+ `organizations/{organization_id}/sources/-` \+ `organizations/{organization_id}/sources/-/locations/{location_id}` \+ `folders/{folder_id}/sources/-` \+ `folders/{folder_id}/sources/-locations/{location_id}` \+ `projects/{projects_id}/sources/-` \+ `projects/{projects_id}/sources/-/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListFindingsPagedResponse)` |   
  
### listFindings(ListFindingsRequest request)
    
    
    public final SecurityCenterClient.ListFindingsPagedResponse listFindings(ListFindingsRequest request)

Lists an organization or source's findings.

To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListFindingsRequest request =
           ListFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setFieldMask(FieldMask.newBuilder().build())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (ListFindingsResponse.ListFindingsResult element :
           securityCenterClient.listFindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListFindingsPagedResponse)` |   
  
### listFindings(String parent)
    
    
    public final SecurityCenterClient.ListFindingsPagedResponse listFindings(String parent)

Lists an organization or source's findings.

To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString();
       for (ListFindingsResponse.ListFindingsResult element :
           securityCenterClient.listFindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the source the findings belong to. If no location is specified, the default is global. The following list shows some examples: \+ `organizations/[organization_id]/sources/[source_id]` \+ `organizations/[organization_id]/sources/[source_id]/locations/[location_id]` \+ `folders/[folder_id]/sources/[source_id]` \+ `folders/[folder_id]/sources/[source_id]/locations/[location_id]` \+ `projects/[project_id]/sources/[source_id]` \+ `projects/[project_id]/sources/[source_id]/locations/[location_id]` To list across all sources provide a source_id of `-`. The following list shows some examples: \+ `organizations/{organization_id}/sources/-` \+ `organizations/{organization_id}/sources/-/locations/{location_id}` \+ `folders/{folder_id}/sources/-` \+ `folders/{folder_id}/sources/-locations/{location_id}` \+ `projects/{projects_id}/sources/-` \+ `projects/{projects_id}/sources/-/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListFindingsPagedResponse)` |   
  
### listFindingsCallable()
    
    
    public final UnaryCallable<ListFindingsRequest,ListFindingsResponse> listFindingsCallable()

Lists an organization or source's findings.

To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListFindingsRequest request =
           ListFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setFieldMask(FieldMask.newBuilder().build())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListFindingsResponse response = securityCenterClient.listFindingsCallable().call(request);
         for (ListFindingsResponse.ListFindingsResult element :
             response.getListFindingsResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest),[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse)>` |   
  
### listFindingsPagedCallable()
    
    
    public final UnaryCallable<ListFindingsRequest,SecurityCenterClient.ListFindingsPagedResponse> listFindingsPagedCallable()

Lists an organization or source's findings.

To list across all sources for a given location provide a `-` as the source id. If no location is specified, finding are assumed to be in global. The following list shows some examples:

\+ `/v2/organizations/{organization_id}/sources/-/findings` \+ `/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListFindingsRequest request =
           ListFindingsRequest.newBuilder()
               .setParent(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setFieldMask(FieldMask.newBuilder().build())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<ListFindingsResponse.ListFindingsResult> future =
           securityCenterClient.listFindingsPagedCallable().futureCall(request);
       // Do something.
       for (ListFindingsResponse.ListFindingsResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest),[ListFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListFindingsPagedResponse)>` |   
  
### listMuteConfigs(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable FolderLocationName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(@Nullable FolderName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable FolderName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(@Nullable LocationName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable LocationName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable OrganizationLocationName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(@Nullable OrganizationName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable OrganizationName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(@Nullable ProjectName parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(@Nullable ProjectName parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ProjectName`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(ListMuteConfigsRequest request)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(ListMuteConfigsRequest request)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListMuteConfigsRequest request =
           ListMuteConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MuteConfig element : securityCenterClient.listMuteConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigs(String parent)
    
    
    public final SecurityCenterClient.ListMuteConfigsPagedResponse listMuteConfigs(String parent)

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (MuteConfig element : securityCenterClient.listMuteConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]", "folders/[folder_id]`, `projects/[project_id]`, `organizations/[organization_id]/locations/[location_id]`, `folders/[folder_id]/locations/[location_id]`, `projects/[project_id]/locations/[location_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)` |   
  
### listMuteConfigsCallable()
    
    
    public final UnaryCallable<ListMuteConfigsRequest,ListMuteConfigsResponse> listMuteConfigsCallable()

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListMuteConfigsRequest request =
           ListMuteConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMuteConfigsResponse response =
             securityCenterClient.listMuteConfigsCallable().call(request);
         for (MuteConfig element : response.getMuteConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest),[ListMuteConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsResponse)>` |   
  
### listMuteConfigsPagedCallable()
    
    
    public final UnaryCallable<ListMuteConfigsRequest,SecurityCenterClient.ListMuteConfigsPagedResponse> listMuteConfigsPagedCallable()

Lists mute configs. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListMuteConfigsRequest request =
           ListMuteConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MuteConfig> future =
           securityCenterClient.listMuteConfigsPagedCallable().futureCall(request);
       // Do something.
       for (MuteConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest),[ListMuteConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListMuteConfigsPagedResponse)>` |   
  
### listNotificationConfigs(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterClient.ListNotificationConfigsPagedResponse listNotificationConfigs(@Nullable FolderLocationName parent)

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (NotificationConfig element :
           securityCenterClient.listNotificationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderLocationName`  
Required. The name of the parent in which to list the notification configurations. Its format is "organizations/[organization_id]/locations/[location_id]", "folders/[folder_id]/locations/[location_id]", or "projects/[project_id]/locations/[location_id]".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)` |   
  
### listNotificationConfigs(@Nullable LocationName parent)
    
    
    public final SecurityCenterClient.ListNotificationConfigsPagedResponse listNotificationConfigs(@Nullable LocationName parent)

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NotificationConfig element :
           securityCenterClient.listNotificationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.LocationName`  
Required. The name of the parent in which to list the notification configurations. Its format is "organizations/[organization_id]/locations/[location_id]", "folders/[folder_id]/locations/[location_id]", or "projects/[project_id]/locations/[location_id]".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)` |   
  
### listNotificationConfigs(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterClient.ListNotificationConfigsPagedResponse listNotificationConfigs(@Nullable OrganizationLocationName parent)

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (NotificationConfig element :
           securityCenterClient.listNotificationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. The name of the parent in which to list the notification configurations. Its format is "organizations/[organization_id]/locations/[location_id]", "folders/[folder_id]/locations/[location_id]", or "projects/[project_id]/locations/[location_id]".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)` |   
  
### listNotificationConfigs(ListNotificationConfigsRequest request)
    
    
    public final SecurityCenterClient.ListNotificationConfigsPagedResponse listNotificationConfigs(ListNotificationConfigsRequest request)

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListNotificationConfigsRequest request =
           ListNotificationConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (NotificationConfig element :
           securityCenterClient.listNotificationConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotificationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListNotificationConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)` |   
  
### listNotificationConfigs(String parent)
    
    
    public final SecurityCenterClient.ListNotificationConfigsPagedResponse listNotificationConfigs(String parent)

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (NotificationConfig element :
           securityCenterClient.listNotificationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent in which to list the notification configurations. Its format is "organizations/[organization_id]/locations/[location_id]", "folders/[folder_id]/locations/[location_id]", or "projects/[project_id]/locations/[location_id]".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)` |   
  
### listNotificationConfigsCallable()
    
    
    public final UnaryCallable<ListNotificationConfigsRequest,ListNotificationConfigsResponse> listNotificationConfigsCallable()

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListNotificationConfigsRequest request =
           ListNotificationConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListNotificationConfigsResponse response =
             securityCenterClient.listNotificationConfigsCallable().call(request);
         for (NotificationConfig element : response.getNotificationConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotificationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListNotificationConfigsRequest),[ListNotificationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListNotificationConfigsResponse)>` |   
  
### listNotificationConfigsPagedCallable()
    
    
    public final UnaryCallable<ListNotificationConfigsRequest,SecurityCenterClient.ListNotificationConfigsPagedResponse> listNotificationConfigsPagedCallable()

Lists notification configs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListNotificationConfigsRequest request =
           ListNotificationConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<NotificationConfig> future =
           securityCenterClient.listNotificationConfigsPagedCallable().futureCall(request);
       // Do something.
       for (NotificationConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotificationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListNotificationConfigsRequest),[ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListNotificationConfigsPagedResponse)>` |   
  
### listResourceValueConfigs(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterClient.ListResourceValueConfigsPagedResponse listResourceValueConfigs(@Nullable OrganizationLocationName parent)

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (ResourceValueConfig element :
           securityCenterClient.listResourceValueConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationLocationName`  
Required. The parent, which owns the collection of resource value configs. Its format is `organizations/[organization_id]`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListResourceValueConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListResourceValueConfigsPagedResponse)` |   
  
### listResourceValueConfigs(@Nullable OrganizationName parent)
    
    
    public final SecurityCenterClient.ListResourceValueConfigsPagedResponse listResourceValueConfigs(@Nullable OrganizationName parent)

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (ResourceValueConfig element :
           securityCenterClient.listResourceValueConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. The parent, which owns the collection of resource value configs. Its format is `organizations/[organization_id]`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListResourceValueConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListResourceValueConfigsPagedResponse)` |   
  
### listResourceValueConfigs(ListResourceValueConfigsRequest request)
    
    
    public final SecurityCenterClient.ListResourceValueConfigsPagedResponse listResourceValueConfigs(ListResourceValueConfigsRequest request)

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListResourceValueConfigsRequest request =
           ListResourceValueConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ResourceValueConfig element :
           securityCenterClient.listResourceValueConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListResourceValueConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListResourceValueConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListResourceValueConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListResourceValueConfigsPagedResponse)` |   
  
### listResourceValueConfigs(String parent)
    
    
    public final SecurityCenterClient.ListResourceValueConfigsPagedResponse listResourceValueConfigs(String parent)

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (ResourceValueConfig element :
           securityCenterClient.listResourceValueConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns the collection of resource value configs. Its format is `organizations/[organization_id]`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListResourceValueConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListResourceValueConfigsPagedResponse)` |   
  
### listResourceValueConfigsCallable()
    
    
    public final UnaryCallable<ListResourceValueConfigsRequest,ListResourceValueConfigsResponse> listResourceValueConfigsCallable()

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListResourceValueConfigsRequest request =
           ListResourceValueConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListResourceValueConfigsResponse response =
             securityCenterClient.listResourceValueConfigsCallable().call(request);
         for (ResourceValueConfig element : response.getResourceValueConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceValueConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListResourceValueConfigsRequest),[ListResourceValueConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListResourceValueConfigsResponse)>` |   
  
### listResourceValueConfigsPagedCallable()
    
    
    public final UnaryCallable<ListResourceValueConfigsRequest,SecurityCenterClient.ListResourceValueConfigsPagedResponse> listResourceValueConfigsPagedCallable()

Lists all ResourceValueConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListResourceValueConfigsRequest request =
           ListResourceValueConfigsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ResourceValueConfig> future =
           securityCenterClient.listResourceValueConfigsPagedCallable().futureCall(request);
       // Do something.
       for (ResourceValueConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceValueConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListResourceValueConfigsRequest),[ListResourceValueConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListResourceValueConfigsPagedResponse)>` |   
  
### listSources(@Nullable FolderName parent)
    
    
    public final SecurityCenterClient.ListSourcesPagedResponse listSources(@Nullable FolderName parent)

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (Source element : securityCenterClient.listSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FolderName`  
Required. Resource name of the parent of sources to list. Its format should be `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)` |   
  
### listSources(@Nullable OrganizationName parent)
    
    
    public final SecurityCenterClient.ListSourcesPagedResponse listSources(@Nullable OrganizationName parent)

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (Source element : securityCenterClient.listSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.OrganizationName`  
Required. Resource name of the parent of sources to list. Its format should be `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)` |   
  
### listSources(@Nullable ProjectName parent)
    
    
    public final SecurityCenterClient.ListSourcesPagedResponse listSources(@Nullable ProjectName parent)

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Source element : securityCenterClient.listSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.ProjectName`  
Required. Resource name of the parent of sources to list. Its format should be `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)` |   
  
### listSources(ListSourcesRequest request)
    
    
    public final SecurityCenterClient.ListSourcesPagedResponse listSources(ListSourcesRequest request)

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListSourcesRequest request =
           ListSourcesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (Source element : securityCenterClient.listSources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)` |   
  
### listSources(String parent)
    
    
    public final SecurityCenterClient.ListSourcesPagedResponse listSources(String parent)

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (Source element : securityCenterClient.listSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the parent of sources to list. Its format should be `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)` |   
  
### listSourcesCallable()
    
    
    public final UnaryCallable<ListSourcesRequest,ListSourcesResponse> listSourcesCallable()

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListSourcesRequest request =
           ListSourcesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListSourcesResponse response = securityCenterClient.listSourcesCallable().call(request);
         for (Source element : response.getSourcesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListSourcesRequest),[ListSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListSourcesResponse)>` |   
  
### listSourcesPagedCallable()
    
    
    public final UnaryCallable<ListSourcesRequest,SecurityCenterClient.ListSourcesPagedResponse> listSourcesPagedCallable()

Lists all sources belonging to an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListSourcesRequest request =
           ListSourcesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<Source> future =
           securityCenterClient.listSourcesPagedCallable().futureCall(request);
       // Do something.
       for (Source element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListSourcesRequest),[ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse)>` |   
  
### listValuedResources(@Nullable SimulationName parent)
    
    
    public final SecurityCenterClient.ListValuedResourcesPagedResponse listValuedResources(@Nullable SimulationName parent)

Lists the valued resources for a set of simulation results and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SimulationName parent =
           SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]");
       for (ValuedResource element : securityCenterClient.listValuedResources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.SimulationName`  
Required. Name of parent to list exposed resources. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListValuedResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListValuedResourcesPagedResponse)` |   
  
### listValuedResources(ListValuedResourcesRequest request)
    
    
    public final SecurityCenterClient.ListValuedResourcesPagedResponse listValuedResources(ListValuedResourcesRequest request)

Lists the valued resources for a set of simulation results and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListValuedResourcesRequest request =
           ListValuedResourcesRequest.newBuilder()
               .setParent(
                   SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ValuedResource element :
           securityCenterClient.listValuedResources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListValuedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListValuedResourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListValuedResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListValuedResourcesPagedResponse)` |   
  
### listValuedResources(String parent)
    
    
    public final SecurityCenterClient.ListValuedResourcesPagedResponse listValuedResources(String parent)

Lists the valued resources for a set of simulation results and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String parent =
           SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]").toString();
       for (ValuedResource element : securityCenterClient.listValuedResources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list exposed resources. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}`  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterClient.ListValuedResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListValuedResourcesPagedResponse)` |   
  
### listValuedResourcesCallable()
    
    
    public final UnaryCallable<ListValuedResourcesRequest,ListValuedResourcesResponse> listValuedResourcesCallable()

Lists the valued resources for a set of simulation results and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListValuedResourcesRequest request =
           ListValuedResourcesRequest.newBuilder()
               .setParent(
                   SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListValuedResourcesResponse response =
             securityCenterClient.listValuedResourcesCallable().call(request);
         for (ValuedResource element : response.getValuedResourcesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListValuedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListValuedResourcesRequest),[ListValuedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListValuedResourcesResponse)>` |   
  
### listValuedResourcesPagedCallable()
    
    
    public final UnaryCallable<ListValuedResourcesRequest,SecurityCenterClient.ListValuedResourcesPagedResponse> listValuedResourcesPagedCallable()

Lists the valued resources for a set of simulation results and filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ListValuedResourcesRequest request =
           ListValuedResourcesRequest.newBuilder()
               .setParent(
                   SimulationName.ofOrganizationSimulationName("[ORGANIZATION]", "[SIMULATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ValuedResource> future =
           securityCenterClient.listValuedResourcesPagedCallable().futureCall(request);
       // Do something.
       for (ValuedResource element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListValuedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListValuedResourcesRequest),[ListValuedResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListValuedResourcesPagedResponse)>` |   
  
### setFindingState(@Nullable FindingName name, Finding.State state)
    
    
    public final Finding setFindingState(@Nullable FindingName name, Finding.State state)

Updates the state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FindingName name =
           FindingName.ofOrganizationSourceFindingName("[ORGANIZATION]", "[SOURCE]", "[FINDING]");
       Finding.State state = Finding.State.forNumber(0);
       Finding response = securityCenterClient.setFindingState(name, state);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FindingName`  
Required. The [relative resource name](https://cloud.google.com/apis/design/resource_names#relative_resource_name) of the finding. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}` \+ `organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  * `folders/{folder_id}/sources/{source_id}/findings/{finding_id}` \+ `folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  
`state` | `[Finding.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.State)`  
Required. The desired State of the finding.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setFindingState(SetFindingStateRequest request)
    
    
    public final Finding setFindingState(SetFindingStateRequest request)

Updates the state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetFindingStateRequest request =
           SetFindingStateRequest.newBuilder()
               .setName(
                   FindingName.ofOrganizationSourceFindingName(
                           "[ORGANIZATION]", "[SOURCE]", "[FINDING]")
                       .toString())
               .build();
       Finding response = securityCenterClient.setFindingState(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetFindingStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setFindingState(String name, Finding.State state)
    
    
    public final Finding setFindingState(String name, Finding.State state)

Updates the state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           FindingName.ofOrganizationSourceFindingName("[ORGANIZATION]", "[SOURCE]", "[FINDING]")
               .toString();
       Finding.State state = Finding.State.forNumber(0);
       Finding response = securityCenterClient.setFindingState(name, state);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The [relative resource name](https://cloud.google.com/apis/design/resource_names#relative_resource_name) of the finding. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}` \+ `organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  * `folders/{folder_id}/sources/{source_id}/findings/{finding_id}` \+ `folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  
`state` | `[Finding.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.State)`  
Required. The desired State of the finding.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setFindingStateCallable()
    
    
    public final UnaryCallable<SetFindingStateRequest,Finding> setFindingStateCallable()

Updates the state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetFindingStateRequest request =
           SetFindingStateRequest.newBuilder()
               .setName(
                   FindingName.ofOrganizationSourceFindingName(
                           "[ORGANIZATION]", "[SOURCE]", "[FINDING]")
                       .toString())
               .build();
       ApiFuture<Finding> future =
           securityCenterClient.setFindingStateCallable().futureCall(request);
       // Do something.
       Finding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetFindingStateRequest),[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)>` |   
  
### setIamPolicy(@Nullable ResourceName resource, Policy policy)
    
    
    public final Policy setIamPolicy(@Nullable ResourceName resource, Policy policy)

Sets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceName resource = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       Policy policy = Policy.newBuilder().build();
       Policy response = securityCenterClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = securityCenterClient.setIamPolicy(request);
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
  
### setIamPolicy(String resource, Policy policy)
    
    
    public final Policy setIamPolicy(String resource, Policy policy)

Sets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String resource = FolderName.of("[FOLDER]").toString();
       Policy policy = Policy.newBuilder().build();
       Policy response = securityCenterClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified Source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = securityCenterClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### setMute(@Nullable FindingName name, Finding.Mute mute)
    
    
    public final Finding setMute(@Nullable FindingName name, Finding.Mute mute)

Updates the mute state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       FindingName name =
           FindingName.ofOrganizationSourceFindingName("[ORGANIZATION]", "[SOURCE]", "[FINDING]");
       Finding.Mute mute = Finding.Mute.forNumber(0);
       Finding response = securityCenterClient.setMute(name, mute);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v2.FindingName`  
Required. The [relative resource name](https://cloud.google.com/apis/design/resource_names#relative_resource_name) of the finding. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}` \+ `organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  * `folders/{folder_id}/sources/{source_id}/findings/{finding_id}` \+ `folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  
`mute` | `[Finding.Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute)`  
Required. The desired state of the Mute.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setMute(SetMuteRequest request)
    
    
    public final Finding setMute(SetMuteRequest request)

Updates the mute state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetMuteRequest request =
           SetMuteRequest.newBuilder()
               .setName(
                   FindingName.ofOrganizationSourceFindingName(
                           "[ORGANIZATION]", "[SOURCE]", "[FINDING]")
                       .toString())
               .build();
       Finding response = securityCenterClient.setMute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setMute(String name, Finding.Mute mute)
    
    
    public final Finding setMute(String name, Finding.Mute mute)

Updates the mute state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String name =
           FindingName.ofOrganizationSourceFindingName("[ORGANIZATION]", "[SOURCE]", "[FINDING]")
               .toString();
       Finding.Mute mute = Finding.Mute.forNumber(0);
       Finding response = securityCenterClient.setMute(name, mute);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The [relative resource name](https://cloud.google.com/apis/design/resource_names#relative_resource_name) of the finding. If no location is specified, finding is assumed to be in global. The following list shows some examples: \+ `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}` \+ `organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  * `folders/{folder_id}/sources/{source_id}/findings/{finding_id}` \+ `folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/findings/{finding_id}` \+ `projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}`

  
`mute` | `[Finding.Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute)`  
Required. The desired state of the Mute.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### setMuteCallable()
    
    
    public final UnaryCallable<SetMuteRequest,Finding> setMuteCallable()

Updates the mute state of a finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SetMuteRequest request =
           SetMuteRequest.newBuilder()
               .setName(
                   FindingName.ofOrganizationSourceFindingName(
                           "[ORGANIZATION]", "[SOURCE]", "[FINDING]")
                       .toString())
               .build();
       ApiFuture<Finding> future = securityCenterClient.setMuteCallable().futureCall(request);
       // Do something.
       Finding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest),[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(@Nullable ResourceName resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(@Nullable ResourceName resource, List<String> permissions)

Returns the permissions that a caller has on the specified source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceName resource = SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]");
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           securityCenterClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns the permissions that a caller has on the specified source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = securityCenterClient.testIamPermissions(request);
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
  
### testIamPermissions(String resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(String resource, List<String> permissions)

Returns the permissions that a caller has on the specified source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       String resource = FolderName.of("[FOLDER]").toString();
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           securityCenterClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns the permissions that a caller has on the specified source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   SourceName.ofOrganizationSourceName("[ORGANIZATION]", "[SOURCE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           securityCenterClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateBigQueryExport(BigQueryExport bigQueryExport, FieldMask updateMask)
    
    
    public final BigQueryExport updateBigQueryExport(BigQueryExport bigQueryExport, FieldMask updateMask)

Updates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       BigQueryExport bigQueryExport = BigQueryExport.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BigQueryExport response =
           securityCenterClient.updateBigQueryExport(bigQueryExport, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`bigQueryExport` | `[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)`  
Required. The BigQuery export being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated. If empty all mutable fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### updateBigQueryExport(UpdateBigQueryExportRequest request)
    
    
    public final BigQueryExport updateBigQueryExport(UpdateBigQueryExportRequest request)

Updates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateBigQueryExportRequest request =
           UpdateBigQueryExportRequest.newBuilder()
               .setBigQueryExport(BigQueryExport.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       BigQueryExport response = securityCenterClient.updateBigQueryExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateBigQueryExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)` |   
  
### updateBigQueryExportCallable()
    
    
    public final UnaryCallable<UpdateBigQueryExportRequest,BigQueryExport> updateBigQueryExportCallable()

Updates a BigQuery export.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateBigQueryExportRequest request =
           UpdateBigQueryExportRequest.newBuilder()
               .setBigQueryExport(BigQueryExport.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<BigQueryExport> future =
           securityCenterClient.updateBigQueryExportCallable().futureCall(request);
       // Do something.
       BigQueryExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateBigQueryExportRequest),[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.BigQueryExport)>` |   
  
### updateExternalSystem(ExternalSystem externalSystem, FieldMask updateMask)
    
    
    public final ExternalSystem updateExternalSystem(ExternalSystem externalSystem, FieldMask updateMask)

Updates external system. This is for a given finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ExternalSystem externalSystem = ExternalSystem.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ExternalSystem response =
           securityCenterClient.updateExternalSystem(externalSystem, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`externalSystem` | `[ExternalSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ExternalSystem)`  
Required. The external system resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask to use when updating the external system resource. If empty all mutable fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ExternalSystem)` |   
  
### updateExternalSystem(UpdateExternalSystemRequest request)
    
    
    public final ExternalSystem updateExternalSystem(UpdateExternalSystemRequest request)

Updates external system. This is for a given finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateExternalSystemRequest request =
           UpdateExternalSystemRequest.newBuilder()
               .setExternalSystem(ExternalSystem.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ExternalSystem response = securityCenterClient.updateExternalSystem(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExternalSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateExternalSystemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ExternalSystem)` |   
  
### updateExternalSystemCallable()
    
    
    public final UnaryCallable<UpdateExternalSystemRequest,ExternalSystem> updateExternalSystemCallable()

Updates external system. This is for a given finding. If no location is specified, finding is assumed to be in global

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateExternalSystemRequest request =
           UpdateExternalSystemRequest.newBuilder()
               .setExternalSystem(ExternalSystem.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ExternalSystem> future =
           securityCenterClient.updateExternalSystemCallable().futureCall(request);
       // Do something.
       ExternalSystem response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExternalSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateExternalSystemRequest),[ExternalSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ExternalSystem)>` |   
  
### updateFinding(Finding finding, FieldMask updateMask)
    
    
    public final Finding updateFinding(Finding finding, FieldMask updateMask)

Creates or updates a finding. If no location is specified, finding is assumed to be in global. The corresponding source must exist for a finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       Finding finding = Finding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Finding response = securityCenterClient.updateFinding(finding, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`finding` | `[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)`  
Required. The finding resource to update or create if it does not already exist. parent, security_marks, and update_time will be ignored. In the case of creation, the finding id portion of the name must be alphanumeric and less than or equal to 32 characters and greater than 0 characters in length.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask to use when updating the finding resource. This field should not be specified when creating a finding. When updating a finding, an empty mask is treated as updating all mutable fields and replacing source_properties. Individual source_properties can be added/updated by using "source_properties.<property key>" in the field mask.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### updateFinding(UpdateFindingRequest request)
    
    
    public final Finding updateFinding(UpdateFindingRequest request)

Creates or updates a finding. If no location is specified, finding is assumed to be in global. The corresponding source must exist for a finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateFindingRequest request =
           UpdateFindingRequest.newBuilder()
               .setFinding(Finding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Finding response = securityCenterClient.updateFinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateFindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)` |   
  
### updateFindingCallable()
    
    
    public final UnaryCallable<UpdateFindingRequest,Finding> updateFindingCallable()

Creates or updates a finding. If no location is specified, finding is assumed to be in global. The corresponding source must exist for a finding creation to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateFindingRequest request =
           UpdateFindingRequest.newBuilder()
               .setFinding(Finding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Finding> future = securityCenterClient.updateFindingCallable().futureCall(request);
       // Do something.
       Finding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateFindingRequest),[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding)>` |   
  
### updateMuteConfig(MuteConfig muteConfig, FieldMask updateMask)
    
    
    public final MuteConfig updateMuteConfig(MuteConfig muteConfig, FieldMask updateMask)

Updates a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       MuteConfig muteConfig = MuteConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MuteConfig response = securityCenterClient.updateMuteConfig(muteConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`muteConfig` | `[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)`  
Required. The mute config being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated. If empty all mutable fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### updateMuteConfig(UpdateMuteConfigRequest request)
    
    
    public final MuteConfig updateMuteConfig(UpdateMuteConfigRequest request)

Updates a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateMuteConfigRequest request =
           UpdateMuteConfigRequest.newBuilder()
               .setMuteConfig(MuteConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       MuteConfig response = securityCenterClient.updateMuteConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateMuteConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)` |   
  
### updateMuteConfigCallable()
    
    
    public final UnaryCallable<UpdateMuteConfigRequest,MuteConfig> updateMuteConfigCallable()

Updates a mute config. If no location is specified, default is global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateMuteConfigRequest request =
           UpdateMuteConfigRequest.newBuilder()
               .setMuteConfig(MuteConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<MuteConfig> future =
           securityCenterClient.updateMuteConfigCallable().futureCall(request);
       // Do something.
       MuteConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateMuteConfigRequest),[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig)>` |   
  
### updateNotificationConfig(NotificationConfig notificationConfig, FieldMask updateMask)
    
    
    public final NotificationConfig updateNotificationConfig(NotificationConfig notificationConfig, FieldMask updateMask)

Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       NotificationConfig notificationConfig = NotificationConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       NotificationConfig response =
           securityCenterClient.updateNotificationConfig(notificationConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`notificationConfig` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)`  
Required. The notification config to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask to use when updating the notification config. If empty all mutable fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### updateNotificationConfig(UpdateNotificationConfigRequest request)
    
    
    public final NotificationConfig updateNotificationConfig(UpdateNotificationConfigRequest request)

Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateNotificationConfigRequest request =
           UpdateNotificationConfigRequest.newBuilder()
               .setNotificationConfig(NotificationConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       NotificationConfig response = securityCenterClient.updateNotificationConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateNotificationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)` |   
  
### updateNotificationConfigCallable()
    
    
    public final UnaryCallable<UpdateNotificationConfigRequest,NotificationConfig> updateNotificationConfigCallable()

Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateNotificationConfigRequest request =
           UpdateNotificationConfigRequest.newBuilder()
               .setNotificationConfig(NotificationConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<NotificationConfig> future =
           securityCenterClient.updateNotificationConfigCallable().futureCall(request);
       // Do something.
       NotificationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateNotificationConfigRequest),[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig)>` |   
  
### updateResourceValueConfig(ResourceValueConfig resourceValueConfig, FieldMask updateMask)
    
    
    public final ResourceValueConfig updateResourceValueConfig(ResourceValueConfig resourceValueConfig, FieldMask updateMask)

Updates an existing ResourceValueConfigs with new rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       ResourceValueConfig resourceValueConfig = ResourceValueConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ResourceValueConfig response =
           securityCenterClient.updateResourceValueConfig(resourceValueConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resourceValueConfig` | `[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)`  
Required. The resource value config being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated. If empty all mutable fields will be updated. To update nested fields, include the top level field in the mask For example, to update gcp_metadata.resource_type, include the "gcp_metadata" field mask  
**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)` |   
  
### updateResourceValueConfig(UpdateResourceValueConfigRequest request)
    
    
    public final ResourceValueConfig updateResourceValueConfig(UpdateResourceValueConfigRequest request)

Updates an existing ResourceValueConfigs with new rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateResourceValueConfigRequest request =
           UpdateResourceValueConfigRequest.newBuilder()
               .setResourceValueConfig(ResourceValueConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ResourceValueConfig response = securityCenterClient.updateResourceValueConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateResourceValueConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)` |   
  
### updateResourceValueConfigCallable()
    
    
    public final UnaryCallable<UpdateResourceValueConfigRequest,ResourceValueConfig> updateResourceValueConfigCallable()

Updates an existing ResourceValueConfigs with new rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateResourceValueConfigRequest request =
           UpdateResourceValueConfigRequest.newBuilder()
               .setResourceValueConfig(ResourceValueConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ResourceValueConfig> future =
           securityCenterClient.updateResourceValueConfigCallable().futureCall(request);
       // Do something.
       ResourceValueConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateResourceValueConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateResourceValueConfigRequest),[ResourceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ResourceValueConfig)>` |   
  
### updateSecurityMarks(SecurityMarks securityMarks, FieldMask updateMask)
    
    
    public final SecurityMarks updateSecurityMarks(SecurityMarks securityMarks, FieldMask updateMask)

Updates security marks. For Finding Security marks, if no location is specified, finding is assumed to be in global. Assets Security Marks can only be accessed through global endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       SecurityMarks securityMarks = SecurityMarks.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SecurityMarks response = securityCenterClient.updateSecurityMarks(securityMarks, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityMarks` | `[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks)`  
Required. The security marks resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask to use when updating the security marks resource. The field mask must not contain duplicate fields. If empty or set to "marks", all marks will be replaced. Individual marks can be updated using "marks.<mark_key>".  
**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks)` |   
  
### updateSecurityMarks(UpdateSecurityMarksRequest request)
    
    
    public final SecurityMarks updateSecurityMarks(UpdateSecurityMarksRequest request)

Updates security marks. For Finding Security marks, if no location is specified, finding is assumed to be in global. Assets Security Marks can only be accessed through global endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateSecurityMarksRequest request =
           UpdateSecurityMarksRequest.newBuilder()
               .setSecurityMarks(SecurityMarks.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SecurityMarks response = securityCenterClient.updateSecurityMarks(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSecurityMarksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks)` |   
  
### updateSecurityMarksCallable()
    
    
    public final UnaryCallable<UpdateSecurityMarksRequest,SecurityMarks> updateSecurityMarksCallable()

Updates security marks. For Finding Security marks, if no location is specified, finding is assumed to be in global. Assets Security Marks can only be accessed through global endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateSecurityMarksRequest request =
           UpdateSecurityMarksRequest.newBuilder()
               .setSecurityMarks(SecurityMarks.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SecurityMarks> future =
           securityCenterClient.updateSecurityMarksCallable().futureCall(request);
       // Do something.
       SecurityMarks response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSecurityMarksRequest),[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks)>` |   
  
### updateSource(Source source, FieldMask updateMask)
    
    
    public final Source updateSource(Source source, FieldMask updateMask)

Updates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       Source source = Source.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Source response = securityCenterClient.updateSource(source, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`source` | `[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)`  
Required. The source resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask to use when updating the source resource. If empty all mutable fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### updateSource(UpdateSourceRequest request)
    
    
    public final Source updateSource(UpdateSourceRequest request)

Updates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateSourceRequest request =
           UpdateSourceRequest.newBuilder()
               .setSource(Source.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Source response = securityCenterClient.updateSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)` |   
  
### updateSourceCallable()
    
    
    public final UnaryCallable<UpdateSourceRequest,Source> updateSourceCallable()

Updates a source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterClient securityCenterClient = SecurityCenterClient.create()) {
       UpdateSourceRequest request =
           UpdateSourceRequest.newBuilder()
               .setSource(Source.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Source> future = securityCenterClient.updateSourceCallable().futureCall(request);
       // Do something.
       Source response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
