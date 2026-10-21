---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/appengine/
title: App Engine roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:10.359572+00:00
---

# App Engine roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/appengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  App Engine roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for App Engine. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## App Engine roles

Role | Permissions  
---|---  
  
#### App Engine Service Admin 

(`roles/appengine.admin`) Full access to App Engine resources.  |  `appengine.*`

  * `appengine.applications.create`
  * `appengine.applications.get`
  * `appengine.applications.listRuntimes`
  * `appengine.applications.update`
  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`
  * `appengine.memcache.addKey`
  * `appengine.memcache.flush`
  * `appengine.memcache.get`
  * `appengine.memcache.getKey`
  * `appengine.memcache.list`
  * `appengine.memcache.update`
  * `appengine.operations.get`
  * `appengine.operations.list`
  * `appengine.runtimes.actAsAdmin`
  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`
  * `appengine.versions.create`
  * `appengine.versions.delete`
  * `appengine.versions.exportAppImage`
  * `appengine.versions.get`
  * `appengine.versions.getFileContents`
  * `appengine.versions.list`
  * `appengine.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Admin 

(`roles/appengine.appAdmin`) Read/Write/Modify access to all application configuration and settings. To deploy new versions, a principal must have the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) role on the assigned App Engine [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), and the Cloud Build Editor (`roles/cloudbuild.builds.editor`), and Cloud Storage Object Admin (`roles/storage.objectAdmin`) roles on the project. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Editor 

(`roles/appengine.editor`) Editor role for App Engine  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.*`

  * `appengine.memcache.addKey`
  * `appengine.memcache.flush`
  * `appengine.memcache.get`
  * `appengine.memcache.getKey`
  * `appengine.memcache.list`
  * `appengine.memcache.update`

`appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Viewer 

(`roles/appengine.viewer`) Viewer role for App Engine  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.memcache.get` `appengine.memcache.getKey` `appengine.memcache.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Creator 

(`roles/appengine.appCreator`) Ability to create the App Engine resource for the project.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.create` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Viewer 

(`roles/appengine.appViewer`) Read-only access to all application configuration and settings.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `artifactregistry.projectsettings.get` `recommender.appengineVersionCostInsights.get` `recommender.appengineVersionCostInsights.list` `recommender.appengineVersionCostRecommendations.get` `recommender.appengineVersionCostRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Code Viewer 

(`roles/appengine.codeViewer`) Read-only access to all application configuration, settings, and deployed source code.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.getFileContents` `appengine.versions.list` `artifactregistry.projectsettings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Managed VM Debug Access 

(`roles/appengine.debugger`) Ability to read or manage v2 instances.  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Deployer 

(`roles/appengine.deployer`) Read-only access to all application configuration and settings. To deploy new versions, you must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) role on the assigned App Engine [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), and the Cloud Build Editor (`roles/cloudbuild.builds.editor`), and Cloud Storage Object Admin (`roles/storage.objectAdmin`) roles on the project. Cannot modify existing versions other than deleting versions that are not receiving traffic. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `artifactregistry.projectsettings.get` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Memcache Data Admin 

(`roles/appengine.memcacheDataAdmin`) Can get, set, delete, and flush App Engine Memcache items.  |  `appengine.applications.get` `appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Service Admin 

(`roles/appengine.serviceAdmin`) Read-only access to all application configuration and settings. Write access to module-level and version-level settings. Cannot deploy a new version. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.delete` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.delete` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### App Engine Standard Environment Service Agent 

(`roles/appengine.serviceAgent`) Give App Engine Standard Envirnoment service account access to managed resources. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.versions.delete` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.aptartifacts.create` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.kfpartifacts.create` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.create` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.tags.update` `artifactregistry.versions.get` `artifactregistry.versions.list` `artifactregistry.yumartifacts.create` `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.globalOperations.get` `compute.networks.get` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.use` `compute.zoneOperations.get` `datastore.databases.get` `datastore.entities.create` `datastore.entities.delete` `datastore.entities.get` `datastore.entities.list` `datastore.entities.update` `datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.signBlob` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.get`  
  
## App Engine permissions

Permission | Included in roles  
---|---  
  
#### `appengine.applications.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appCreator) (`roles/appengine.appCreator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `appengine.applications.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Cloud Scheduler Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.admin) (`roles/cloudscheduler.admin`)  [Cloud Scheduler Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.viewer) (`roles/cloudscheduler.viewer`)  [Web Security Scanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecurityscanner#cloudsecurityscanner.admin) (`roles/cloudsecurityscanner.admin`)  [Web Security Scanner Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecurityscanner#cloudsecurityscanner.editor) (`roles/cloudsecurityscanner.editor`)  [Cloud Datastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.admin) (`roles/datastore.admin`)  [Cloud Datastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.editor) (`roles/datastore.editor`)  [Cloud Datastore Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.owner) (`roles/datastore.owner`)  [Cloud Datastore User](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.user) (`roles/datastore.user`)  [Cloud Datastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.viewer) (`roles/datastore.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Memcache Data Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.memcacheDataAdmin) (`roles/appengine.memcacheDataAdmin`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Cloud Scheduler Job Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.jobRunner) (`roles/cloudscheduler.jobRunner`)  [Cloud Datastore Import Export Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.importExportAdmin) (`roles/datastore.importExportAdmin`)  [Cloud Datastore Index Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore#datastore.indexAdmin) (`roles/datastore.indexAdmin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 
  * [Cloud Web Security Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecurityscanner#websecurityscanner.serviceAgent) (`roles/websecurityscanner.serviceAgent`) 

  
  
#### `appengine.applications.listRuntimes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.applications.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `appengine.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.instances.enableDebug`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.memcache.addKey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Memcache Data Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.memcacheDataAdmin) (`roles/appengine.memcacheDataAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.memcache.flush`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Memcache Data Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.memcacheDataAdmin) (`roles/appengine.memcacheDataAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.memcache.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Memcache Data Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.memcacheDataAdmin) (`roles/appengine.memcacheDataAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.memcache.getKey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `appengine.memcache.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `appengine.memcache.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Memcache Data Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.memcacheDataAdmin) (`roles/appengine.memcacheDataAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `appengine.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.runtimes.actAsAdmin`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.services.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.services.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.services.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `appengine.services.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.exportAppImage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.getFileContents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)   
  
#### `appengine.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.viewer) (`roles/appengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [App Engine Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appViewer) (`roles/appengine.appViewer`)  [App Engine Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.codeViewer) (`roles/appengine.codeViewer`)  [App Engine Managed VM Debug Access](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.debugger) (`roles/appengine.debugger`)  [App Engine Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
#### `appengine.versions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.admin) (`roles/appengine.admin`)  [App Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`)  [App Engine Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.editor) (`roles/appengine.editor`)  [App Engine Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAdmin) (`roles/appengine.serviceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine Standard Environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) (`roles/appengine.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
