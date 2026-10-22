---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/ml/
title: AI Platform roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:09.532698+00:00
---

# AI Platform roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  AI Platform roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for AI Platform. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## AI Platform roles

Role | Permissions  
---|---  
  
#### AI Platform Admin 

(`roles/ml.admin`) Provides full access to AI Platform resources, and its jobs, operations, models, and versions.  Lowest-level resources where you can grant this role:

  * Project 

|  `ml.*`

  * `ml.jobs.cancel`
  * `ml.jobs.create`
  * `ml.jobs.get`
  * `ml.jobs.getIamPolicy`
  * `ml.jobs.list`
  * `ml.jobs.setIamPolicy`
  * `ml.jobs.update`
  * `ml.locations.get`
  * `ml.locations.list`
  * `ml.models.create`
  * `ml.models.delete`
  * `ml.models.get`
  * `ml.models.getIamPolicy`
  * `ml.models.list`
  * `ml.models.predict`
  * `ml.models.setIamPolicy`
  * `ml.models.update`
  * `ml.operations.cancel`
  * `ml.operations.get`
  * `ml.operations.list`
  * `ml.projects.getConfig`
  * `ml.studies.create`
  * `ml.studies.delete`
  * `ml.studies.get`
  * `ml.studies.getIamPolicy`
  * `ml.studies.list`
  * `ml.studies.setIamPolicy`
  * `ml.trials.create`
  * `ml.trials.delete`
  * `ml.trials.get`
  * `ml.trials.list`
  * `ml.trials.update`
  * `ml.versions.create`
  * `ml.versions.delete`
  * `ml.versions.get`
  * `ml.versions.list`
  * `ml.versions.predict`
  * `ml.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### AI Platform Editor 

(`roles/ml.editor`) Editor role for AI Platform  |  `ml.jobs.cancel` `ml.jobs.create` `ml.jobs.get` `ml.jobs.getIamPolicy` `ml.jobs.list` `ml.jobs.update` `ml.locations.*`

  * `ml.locations.get`
  * `ml.locations.list`

`ml.models.create` `ml.models.delete` `ml.models.get` `ml.models.getIamPolicy` `ml.models.list` `ml.models.predict` `ml.models.update` `ml.operations.*`

  * `ml.operations.cancel`
  * `ml.operations.get`
  * `ml.operations.list`

`ml.projects.getConfig` `ml.studies.create` `ml.studies.delete` `ml.studies.get` `ml.studies.getIamPolicy` `ml.studies.list` `ml.trials.*`

  * `ml.trials.create`
  * `ml.trials.delete`
  * `ml.trials.get`
  * `ml.trials.list`
  * `ml.trials.update`

`ml.versions.*`

  * `ml.versions.create`
  * `ml.versions.delete`
  * `ml.versions.get`
  * `ml.versions.list`
  * `ml.versions.predict`
  * `ml.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### AI Platform Viewer 

(`roles/ml.viewer`) Provides read-only access to AI Platform resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `ml.jobs.get` `ml.jobs.getIamPolicy` `ml.jobs.list` `ml.locations.*`

  * `ml.locations.get`
  * `ml.locations.list`

`ml.models.get` `ml.models.getIamPolicy` `ml.models.list` `ml.operations.get` `ml.operations.list` `ml.projects.getConfig` `ml.studies.get` `ml.studies.getIamPolicy` `ml.studies.list` `ml.trials.get` `ml.trials.list` `ml.versions.get` `ml.versions.list` `resourcemanager.projects.get`  
  
#### AI Platform Developer 

(`roles/ml.developer`) Provides ability to use AI Platform resources for creating models, versions, jobs for training and prediction, and sending online prediction requests.  Lowest-level resources where you can grant this role:

  * Project 

|  `ml.jobs.create` `ml.jobs.get` `ml.jobs.getIamPolicy` `ml.jobs.list` `ml.locations.*`

  * `ml.locations.get`
  * `ml.locations.list`

`ml.models.create` `ml.models.get` `ml.models.getIamPolicy` `ml.models.list` `ml.models.predict` `ml.operations.get` `ml.operations.list` `ml.projects.getConfig` `ml.studies.*`

  * `ml.studies.create`
  * `ml.studies.delete`
  * `ml.studies.get`
  * `ml.studies.getIamPolicy`
  * `ml.studies.list`
  * `ml.studies.setIamPolicy`

`ml.trials.*`

  * `ml.trials.create`
  * `ml.trials.delete`
  * `ml.trials.get`
  * `ml.trials.list`
  * `ml.trials.update`

`ml.versions.get` `ml.versions.list` `ml.versions.predict` `resourcemanager.projects.get`  
  
#### AI Platform Job Owner 

(`roles/ml.jobOwner`) Provides full access to all permissions for a particular job resource. This role is automatically granted to the user who creates the job.  Lowest-level resources where you can grant this role:

  * Job 

|  `ml.jobs.*`

  * `ml.jobs.cancel`
  * `ml.jobs.create`
  * `ml.jobs.get`
  * `ml.jobs.getIamPolicy`
  * `ml.jobs.list`
  * `ml.jobs.setIamPolicy`
  * `ml.jobs.update`

  
  
#### AI Platform Model Owner 

(`roles/ml.modelOwner`) Provides full access to the model and its versions. This role is automatically granted to the user who creates the model.  Lowest-level resources where you can grant this role:

  * Model 

|  `ml.models.*`

  * `ml.models.create`
  * `ml.models.delete`
  * `ml.models.get`
  * `ml.models.getIamPolicy`
  * `ml.models.list`
  * `ml.models.predict`
  * `ml.models.setIamPolicy`
  * `ml.models.update`

`ml.versions.*`

  * `ml.versions.create`
  * `ml.versions.delete`
  * `ml.versions.get`
  * `ml.versions.list`
  * `ml.versions.predict`
  * `ml.versions.update`

  
  
#### AI Platform Model User 

(`roles/ml.modelUser`) Provides permissions to read the model and its versions, and use them for prediction.  Lowest-level resources where you can grant this role:

  * Model 

|  `ml.models.get` `ml.models.predict` `ml.versions.get` `ml.versions.list` `ml.versions.predict`  
  
#### AI Platform Operation Owner 

(`roles/ml.operationOwner`) Provides full access to all permissions for a particular operation resource.  Lowest-level resources where you can grant this role:

  * Operation 

|  `ml.operations.*`

  * `ml.operations.cancel`
  * `ml.operations.get`
  * `ml.operations.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### AI Platform Service Agent 

(`roles/ml.serviceAgent`) AI Platform service agent can act as log writer, Cloud Storage admin, Artifact Registry Reader, BigQuery writer, and service account access token creator.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.update` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.updateData` `cloudaicompanion.instances.completeTask` `firebase.projects.get` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.implicitDelegation` `iam.serviceAccounts.list` `iam.serviceAccounts.signBlob` `iam.serviceAccounts.signJwt` `logging.logEntries.create` `logging.logEntries.route` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
## AI Platform permissions

Permission | Included in roles  
---|---  
  
#### `ml.jobs.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)   
  
#### `ml.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `ml.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `ml.jobs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 
  * [AI Platform Notebooks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent) (`roles/notebooks.serviceAgent`) 

  
  
#### `ml.jobs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)   
  
#### `ml.jobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.jobOwner) (`roles/ml.jobOwner`)   
  
#### `ml.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  [AI Platform Model User](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelUser) (`roles/ml.modelUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  [AI Platform Model User](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelUser) (`roles/ml.modelUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.models.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Operation Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.operationOwner) (`roles/ml.operationOwner`)   
  
#### `ml.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Operation Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.operationOwner) (`roles/ml.operationOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Operation Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.operationOwner) (`roles/ml.operationOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.projects.getConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.studies.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.trials.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.trials.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.trials.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.trials.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.trials.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  [AI Platform Model User](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelUser) (`roles/ml.modelUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.viewer) (`roles/ml.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  [AI Platform Model User](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelUser) (`roles/ml.modelUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.predict`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [AI Platform Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.developer) (`roles/ml.developer`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  [AI Platform Model User](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelUser) (`roles/ml.modelUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
#### `ml.versions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.admin) (`roles/ml.admin`)  [AI Platform Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.editor) (`roles/ml.editor`)  [AI Platform Model Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.modelOwner) (`roles/ml.modelOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Data Labeling Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent) (`roles/datalabeling.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
