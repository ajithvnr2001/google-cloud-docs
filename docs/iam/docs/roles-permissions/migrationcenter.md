---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter/
title: Google Cloud Migration Center roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:18.078483+00:00
---

# Google Cloud Migration Center roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Migration Center roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Migration Center. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Migration Center roles

Role | Permissions  
---|---  
  
#### Migration Center Admin Beta

(`roles/migrationcenter.admin`) Full access to Migration Center all resources.  |  `migrationcenter.*`

  * `migrationcenter.assets.delete`
  * `migrationcenter.assets.get`
  * `migrationcenter.assets.list`
  * `migrationcenter.assets.reportFrames`
  * `migrationcenter.assets.update`
  * `migrationcenter.assetsExportJobs.create`
  * `migrationcenter.assetsExportJobs.delete`
  * `migrationcenter.assetsExportJobs.get`
  * `migrationcenter.assetsExportJobs.list`
  * `migrationcenter.assetsExportJobs.run`
  * `migrationcenter.discoveryClients.create`
  * `migrationcenter.discoveryClients.delete`
  * `migrationcenter.discoveryClients.get`
  * `migrationcenter.discoveryClients.list`
  * `migrationcenter.discoveryClients.sendHeartbeat`
  * `migrationcenter.discoveryClients.update`
  * `migrationcenter.errorFrames.get`
  * `migrationcenter.errorFrames.list`
  * `migrationcenter.groups.create`
  * `migrationcenter.groups.delete`
  * `migrationcenter.groups.get`
  * `migrationcenter.groups.list`
  * `migrationcenter.groups.update`
  * `migrationcenter.importDataFiles.create`
  * `migrationcenter.importDataFiles.delete`
  * `migrationcenter.importDataFiles.get`
  * `migrationcenter.importDataFiles.list`
  * `migrationcenter.importJobs.create`
  * `migrationcenter.importJobs.delete`
  * `migrationcenter.importJobs.get`
  * `migrationcenter.importJobs.list`
  * `migrationcenter.importJobs.update`
  * `migrationcenter.locations.get`
  * `migrationcenter.locations.list`
  * `migrationcenter.operations.cancel`
  * `migrationcenter.operations.delete`
  * `migrationcenter.operations.get`
  * `migrationcenter.operations.list`
  * `migrationcenter.preferenceSets.create`
  * `migrationcenter.preferenceSets.delete`
  * `migrationcenter.preferenceSets.get`
  * `migrationcenter.preferenceSets.list`
  * `migrationcenter.preferenceSets.update`
  * `migrationcenter.relations.get`
  * `migrationcenter.relations.list`
  * `migrationcenter.reportConfigs.create`
  * `migrationcenter.reportConfigs.delete`
  * `migrationcenter.reportConfigs.get`
  * `migrationcenter.reportConfigs.list`
  * `migrationcenter.reports.create`
  * `migrationcenter.reports.delete`
  * `migrationcenter.reports.get`
  * `migrationcenter.reports.list`
  * `migrationcenter.settings.get`
  * `migrationcenter.settings.update`
  * `migrationcenter.sources.create`
  * `migrationcenter.sources.delete`
  * `migrationcenter.sources.get`
  * `migrationcenter.sources.list`
  * `migrationcenter.sources.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `rma.*`

  * `rma.annotations.create`
  * `rma.annotations.get`
  * `rma.collectors.create`
  * `rma.collectors.delete`
  * `rma.collectors.get`
  * `rma.collectors.list`
  * `rma.collectors.update`
  * `rma.locations.get`
  * `rma.locations.list`
  * `rma.operations.cancel`
  * `rma.operations.delete`
  * `rma.operations.get`
  * `rma.operations.list`

`serviceusage.quotas.get`  
  
#### Migration Center Viewer Beta

(`roles/migrationcenter.viewer`) Read-only access to Migration Center all resources.  |  `migrationcenter.assets.get` `migrationcenter.assets.list` `migrationcenter.assetsExportJobs.get` `migrationcenter.assetsExportJobs.list` `migrationcenter.discoveryClients.get` `migrationcenter.discoveryClients.list` `migrationcenter.errorFrames.*`

  * `migrationcenter.errorFrames.get`
  * `migrationcenter.errorFrames.list`

`migrationcenter.groups.get` `migrationcenter.groups.list` `migrationcenter.importDataFiles.get` `migrationcenter.importDataFiles.list` `migrationcenter.importJobs.get` `migrationcenter.importJobs.list` `migrationcenter.locations.*`

  * `migrationcenter.locations.get`
  * `migrationcenter.locations.list`

`migrationcenter.operations.get` `migrationcenter.operations.list` `migrationcenter.preferenceSets.get` `migrationcenter.preferenceSets.list` `migrationcenter.relations.*`

  * `migrationcenter.relations.get`
  * `migrationcenter.relations.list`

`migrationcenter.reportConfigs.get` `migrationcenter.reportConfigs.list` `migrationcenter.reports.get` `migrationcenter.reports.list` `migrationcenter.settings.get` `migrationcenter.sources.get` `migrationcenter.sources.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list` `serviceusage.quotas.get`  
  
#### Migration Center Discovery Client Beta

(`roles/migrationcenter.discoveryClient`) Migration Center Discover Client role  |  `migrationcenter.assets.reportFrames` `migrationcenter.discoveryClients.get` `migrationcenter.discoveryClients.sendHeartbeat`  
  
#### Migration Center Discovery Client Registrator Beta

(`roles/migrationcenter.discoveryClientRegistrator`) Registrator of Migration Center Discover Clients  |  `migrationcenter.discoveryClients.create` `migrationcenter.discoveryClients.delete` `migrationcenter.discoveryClients.update` `migrationcenter.operations.get` `migrationcenter.sources.create` `migrationcenter.sources.delete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Migration Center Service Agent 

(`roles/migrationcenter.serviceAgent`) Gives Migration Center Service Account access to objects storedin object store and Cloud Migration products.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.objects.get` `vmmigration.migratingVms.create`  
  
## Google Cloud Migration Center permissions

Permission | Included in roles  
---|---  
  
#### `migrationcenter.assets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.assets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.assets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.assets.reportFrames`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClient) (`roles/migrationcenter.discoveryClient`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.assets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.assetsExportJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.assetsExportJobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.assetsExportJobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.assetsExportJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.assetsExportJobs.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.discoveryClients.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)   
  
#### `migrationcenter.discoveryClients.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)   
  
#### `migrationcenter.discoveryClients.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Migration Center Discovery Client](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClient) (`roles/migrationcenter.discoveryClient`)   
  
#### `migrationcenter.discoveryClients.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.discoveryClients.sendHeartbeat`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClient) (`roles/migrationcenter.discoveryClient`)   
  
#### `migrationcenter.discoveryClients.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)   
  
#### `migrationcenter.errorFrames.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.errorFrames.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.groups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.groups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.groups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.groups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.groups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.importDataFiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.importDataFiles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.importDataFiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.importDataFiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.importJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.importJobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.importJobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.importJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.importJobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)   
  
#### `migrationcenter.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.preferenceSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.preferenceSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.preferenceSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.preferenceSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.preferenceSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.relations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.relations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.reportConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.reportConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.reportConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.reportConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.reports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.reports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.reports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.reports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `migrationcenter.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)   
  
#### `migrationcenter.sources.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.sources.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Discovery Client Registrator](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.discoveryClientRegistrator) (`roles/migrationcenter.discoveryClientRegistrator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.sources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.sources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `migrationcenter.sources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
