---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway/
title: API Gateway roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:10.977683+00:00
---

# API Gateway roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  API Gateway roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for API Gateway. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## API Gateway roles

Role | Permissions  
---|---  
  
#### ApiGateway Admin 

(`roles/apigateway.admin`) Full access to ApiGateway and related resources.  |  `apigateway.*`

  * `apigateway.apiconfigs.create`
  * `apigateway.apiconfigs.delete`
  * `apigateway.apiconfigs.get`
  * `apigateway.apiconfigs.getIamPolicy`
  * `apigateway.apiconfigs.list`
  * `apigateway.apiconfigs.setIamPolicy`
  * `apigateway.apiconfigs.update`
  * `apigateway.apis.create`
  * `apigateway.apis.createTagBinding`
  * `apigateway.apis.delete`
  * `apigateway.apis.deleteTagBinding`
  * `apigateway.apis.get`
  * `apigateway.apis.getIamPolicy`
  * `apigateway.apis.list`
  * `apigateway.apis.listEffectiveTags`
  * `apigateway.apis.listTagBindings`
  * `apigateway.apis.setIamPolicy`
  * `apigateway.apis.update`
  * `apigateway.gateways.create`
  * `apigateway.gateways.createTagBinding`
  * `apigateway.gateways.delete`
  * `apigateway.gateways.deleteTagBinding`
  * `apigateway.gateways.get`
  * `apigateway.gateways.getIamPolicy`
  * `apigateway.gateways.list`
  * `apigateway.gateways.listEffectiveTags`
  * `apigateway.gateways.listTagBindings`
  * `apigateway.gateways.setIamPolicy`
  * `apigateway.gateways.update`
  * `apigateway.locations.get`
  * `apigateway.locations.list`
  * `apigateway.operations.cancel`
  * `apigateway.operations.delete`
  * `apigateway.operations.get`
  * `apigateway.operations.list`

`apihub.runTimeProjectAttachments.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.get` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### ApiGateway Editor 

(`roles/apigateway.editor`) Editor role for ApiGateway  |  `apigateway.apiconfigs.create` `apigateway.apiconfigs.delete` `apigateway.apiconfigs.get` `apigateway.apiconfigs.getIamPolicy` `apigateway.apiconfigs.list` `apigateway.apiconfigs.update` `apigateway.apis.create` `apigateway.apis.delete` `apigateway.apis.get` `apigateway.apis.getIamPolicy` `apigateway.apis.list` `apigateway.apis.listEffectiveTags` `apigateway.apis.listTagBindings` `apigateway.apis.update` `apigateway.gateways.create` `apigateway.gateways.delete` `apigateway.gateways.get` `apigateway.gateways.getIamPolicy` `apigateway.gateways.list` `apigateway.gateways.listEffectiveTags` `apigateway.gateways.listTagBindings` `apigateway.gateways.update` `apigateway.locations.*`

  * `apigateway.locations.get`
  * `apigateway.locations.list`

`apigateway.operations.*`

  * `apigateway.operations.cancel`
  * `apigateway.operations.delete`
  * `apigateway.operations.get`
  * `apigateway.operations.list`

`apihub.runTimeProjectAttachments.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.get` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### ApiGateway Viewer 

(`roles/apigateway.viewer`) Read-only access to ApiGateway and related resources.  |  `apigateway.apiconfigs.get` `apigateway.apiconfigs.getIamPolicy` `apigateway.apiconfigs.list` `apigateway.apis.get` `apigateway.apis.getIamPolicy` `apigateway.apis.list` `apigateway.apis.listEffectiveTags` `apigateway.apis.listTagBindings` `apigateway.gateways.get` `apigateway.gateways.getIamPolicy` `apigateway.gateways.list` `apigateway.gateways.listEffectiveTags` `apigateway.gateways.listTagBindings` `apigateway.locations.*`

  * `apigateway.locations.get`
  * `apigateway.locations.list`

`apigateway.operations.get` `apigateway.operations.list` `apihub.runTimeProjectAttachments.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.get` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud API Gateway Service Agent 

(`roles/apigateway.serviceAgent`) Gives Cloud API Gateway service account access to Service Management check and reports as well as impersonation on user-specified service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `servicemanagement.services.check` `servicemanagement.services.quota` `servicemanagement.services.report`  
  
#### Cloud API Gateway Management Service Agent 

(`roles/apigateway_management.serviceAgent`) Gives Cloud API Gateway service account access to retrieve a Service configuration.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.get` `servicemanagement.services.create` `servicemanagement.services.delete` `servicemanagement.services.get` `servicemanagement.services.list` `servicemanagement.services.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## API Gateway permissions

Permission | Included in roles  
---|---  
  
#### `apigateway.apiconfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.apiconfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.apiconfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Attack Surface Management Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackSurfaceManagementScannerServiceAgent) (`roles/securitycenter.attackSurfaceManagementScannerServiceAgent`) 

  
  
#### `apigateway.apiconfigs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apiconfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `apigateway.apiconfigs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigateway.apiconfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.apis.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.apis.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apigateway.apis.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.apis.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apigateway.apis.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apis.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apis.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apis.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apis.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.apis.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigateway.apis.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.gateways.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.gateways.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apigateway.gateways.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.gateways.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apigateway.gateways.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.gateways.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.gateways.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `apigateway.gateways.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.gateways.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.gateways.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigateway.gateways.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)   
  
#### `apigateway.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigateway.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
