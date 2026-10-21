---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines/
title: Data Pipelines roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:24.371790+00:00
---

# Data Pipelines roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Pipelines roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Pipelines. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Pipelines roles

Role | Permissions  
---|---  
  
#### Data pipelines Admin 

(`roles/datapipelines.admin`) Administrator of Data pipelines resources  |  `datapipelines.*`

  * `datapipelines.jobs.list`
  * `datapipelines.pipelines.create`
  * `datapipelines.pipelines.delete`
  * `datapipelines.pipelines.get`
  * `datapipelines.pipelines.list`
  * `datapipelines.pipelines.run`
  * `datapipelines.pipelines.stop`
  * `datapipelines.pipelines.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data pipelines Viewer 

(`roles/datapipelines.viewer`) Viewer of Data pipelines resources  |  `datapipelines.jobs.list` `datapipelines.pipelines.get` `datapipelines.pipelines.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data pipelines Invoker 

(`roles/datapipelines.invoker`) Invoker of Data pipelines jobs  |  `datapipelines.pipelines.run` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Datapipelines Service Agent 

(`roles/datapipelines.serviceAgent`) Gives Datapipelines service permissions to create Dataflow & Cloud Scheduler jobs in the user project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `bigquery.tables.get` `bigtable.tables.get` `cloudaicompanion.instances.completeTask` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudscheduler.*`

  * `cloudscheduler.jobs.create`
  * `cloudscheduler.jobs.delete`
  * `cloudscheduler.jobs.enable`
  * `cloudscheduler.jobs.fullView`
  * `cloudscheduler.jobs.get`
  * `cloudscheduler.jobs.list`
  * `cloudscheduler.jobs.pause`
  * `cloudscheduler.jobs.run`
  * `cloudscheduler.jobs.update`
  * `cloudscheduler.locations.get`
  * `cloudscheduler.locations.list`

`compute.machineTypes.get` `compute.projects.get` `compute.regions.list` `compute.zones.list` `dataflow.*`

  * `dataflow.jobs.cancel`
  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `dataflow.jobs.list`
  * `dataflow.jobs.snapshot`
  * `dataflow.jobs.updateContents`
  * `dataflow.messages.list`
  * `dataflow.metrics.get`
  * `dataflow.shuffle.read`
  * `dataflow.shuffle.write`
  * `dataflow.snapshots.delete`
  * `dataflow.snapshots.get`
  * `dataflow.snapshots.list`
  * `dataflow.streamingWorkItems.ImportState`
  * `dataflow.streamingWorkItems.commitWork`
  * `dataflow.streamingWorkItems.getData`
  * `dataflow.streamingWorkItems.getWork`
  * `dataflow.streamingWorkItems.getWorkerMetadata`
  * `dataflow.workItems.lease`
  * `dataflow.workItems.sendMessage`
  * `dataflow.workItems.update`

`firebase.projects.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`orgpolicy.policy.get` `pubsub.schemas.get` `pubsub.topics.get` `recommender.dataflowDiagnosticsInsights.*`

  * `recommender.dataflowDiagnosticsInsights.get`
  * `recommender.dataflowDiagnosticsInsights.list`
  * `recommender.dataflowDiagnosticsInsights.update`

`recommender.iamPolicyInsights.*`

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

`remotebuildexecution.blobs.get` `resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

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

  
  
## Data Pipelines permissions

Permission | Included in roles  
---|---  
  
#### `datapipelines.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)  [Data pipelines Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.viewer) (`roles/datapipelines.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datapipelines.pipelines.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)   
  
#### `datapipelines.pipelines.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)   
  
#### `datapipelines.pipelines.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)  [Data pipelines Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.viewer) (`roles/datapipelines.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datapipelines.pipelines.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)  [Data pipelines Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.viewer) (`roles/datapipelines.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datapipelines.pipelines.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)  [Data pipelines Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.invoker) (`roles/datapipelines.invoker`)   
  
#### `datapipelines.pipelines.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)   
  
#### `datapipelines.pipelines.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data pipelines Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.admin) (`roles/datapipelines.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
