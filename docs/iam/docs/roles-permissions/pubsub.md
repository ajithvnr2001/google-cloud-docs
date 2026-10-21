---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub/
title: Pub/Sub roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:41:57.094523+00:00
---

# Pub/Sub roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Pub/Sub roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Pub/Sub. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Pub/Sub roles

Role | Permissions  
---|---  
  
#### Pub/Sub Admin 

(`roles/pubsub.admin`) Provides full access to topics and subscriptions.  Lowest-level resources where you can grant this role:

  * Schema 
  * Snapshot 
  * Subscription 
  * Topic 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `pubsub.*`

  * `pubsub.messageTransforms.validate`
  * `pubsub.schemas.attach`
  * `pubsub.schemas.commit`
  * `pubsub.schemas.create`
  * `pubsub.schemas.delete`
  * `pubsub.schemas.get`
  * `pubsub.schemas.getIamPolicy`
  * `pubsub.schemas.list`
  * `pubsub.schemas.listRevisions`
  * `pubsub.schemas.rollback`
  * `pubsub.schemas.setIamPolicy`
  * `pubsub.schemas.validate`
  * `pubsub.snapshots.create`
  * `pubsub.snapshots.createTagBinding`
  * `pubsub.snapshots.delete`
  * `pubsub.snapshots.deleteTagBinding`
  * `pubsub.snapshots.get`
  * `pubsub.snapshots.getIamPolicy`
  * `pubsub.snapshots.list`
  * `pubsub.snapshots.listEffectiveTags`
  * `pubsub.snapshots.listTagBindings`
  * `pubsub.snapshots.seek`
  * `pubsub.snapshots.setIamPolicy`
  * `pubsub.snapshots.update`
  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.createTagBinding`
  * `pubsub.subscriptions.delete`
  * `pubsub.subscriptions.deleteTagBinding`
  * `pubsub.subscriptions.get`
  * `pubsub.subscriptions.getIamPolicy`
  * `pubsub.subscriptions.list`
  * `pubsub.subscriptions.listEffectiveTags`
  * `pubsub.subscriptions.listTagBindings`
  * `pubsub.subscriptions.setIamPolicy`
  * `pubsub.subscriptions.update`
  * `pubsub.topics.attachSubscription`
  * `pubsub.topics.create`
  * `pubsub.topics.createTagBinding`
  * `pubsub.topics.delete`
  * `pubsub.topics.deleteTagBinding`
  * `pubsub.topics.detachSubscription`
  * `pubsub.topics.get`
  * `pubsub.topics.getIamPolicy`
  * `pubsub.topics.list`
  * `pubsub.topics.listEffectiveTags`
  * `pubsub.topics.listTagBindings`
  * `pubsub.topics.publish`
  * `pubsub.topics.setIamPolicy`
  * `pubsub.topics.update`
  * `pubsub.topics.updateTag`

`resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Pub/Sub Editor 

(`roles/pubsub.editor`) Provides access to modify topics and subscriptions, and access to publish and consume messages.  Lowest-level resources where you can grant this role:

  * Schema 
  * Snapshot 
  * Subscription 
  * Topic 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `pubsub.messageTransforms.validate` `pubsub.schemas.attach` `pubsub.schemas.commit` `pubsub.schemas.create` `pubsub.schemas.delete` `pubsub.schemas.get` `pubsub.schemas.getIamPolicy` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.rollback` `pubsub.schemas.validate` `pubsub.snapshots.create` `pubsub.snapshots.createTagBinding` `pubsub.snapshots.delete` `pubsub.snapshots.deleteTagBinding` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.createTagBinding` `pubsub.subscriptions.delete` `pubsub.subscriptions.deleteTagBinding` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.createTagBinding` `pubsub.topics.delete` `pubsub.topics.deleteTagBinding` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.update` `pubsub.topics.updateTag` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Pub/Sub Publisher 

(`roles/pubsub.publisher`) Provides access to publish messages to a topic.  Lowest-level resources where you can grant this role:

  * Topic 

|  `pubsub.topics.publish`  
  
#### Pub/Sub Subscriber 

(`roles/pubsub.subscriber`) Provides access to consume messages from a subscription and to attach subscriptions to a topic.  Lowest-level resources where you can grant this role:

  * Snapshot 
  * Subscription 
  * Topic 

|  `pubsub.snapshots.seek` `pubsub.subscriptions.consume` `pubsub.topics.attachSubscription`  
  
#### Pub/Sub Viewer 

(`roles/pubsub.viewer`) Provides access to view topics and subscriptions.  Lowest-level resources where you can grant this role:

  * Schema 
  * Snapshot 
  * Subscription 
  * Topic 

|  `pubsub.messageTransforms.validate` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.validate` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Pub/Sub Service Agent 

(`roles/pubsub.serviceAgent`) Grants Cloud Pub/Sub Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.implicitDelegation` `iam.serviceAccounts.list` `iam.serviceAccounts.signBlob` `iam.serviceAccounts.signJwt` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.services.use`  
  
## Pub/Sub permissions

Permission | Included in roles  
---|---  
  
#### `pubsub.messageTransforms.validate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.attach`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.commit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.schemas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.listRevisions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.rollback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.schemas.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.schemas.validate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.seek`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Healthcare Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.serviceAgent) (`roles/healthcare.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.snapshots.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.snapshots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.subscriptions.consume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Healthcare Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.serviceAgent) (`roles/healthcare.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Data Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsDataPlaneServiceAgent) (`roles/kuberun.eventsDataPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.subscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.subscriptions.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.subscriptions.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [KubeRun Events Data Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsDataPlaneServiceAgent) (`roles/kuberun.eventsDataPlaneServiceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.subscriptions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.subscriptions.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.subscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.attachSubscription`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Healthcare Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.serviceAgent) (`roles/healthcare.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.topics.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.topics.detachSubscription`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
#### `pubsub.topics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [KubeRun Events Data Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsDataPlaneServiceAgent) (`roles/kuberun.eventsDataPlaneServiceAgent`) 
  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 

  
  
#### `pubsub.topics.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.topics.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Assured OSS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.admin) (`roles/assuredoss.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Assured OSS Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.projectAdmin) (`roles/assuredoss.projectAdmin`)  [Assured OSS Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredoss#assuredoss.reader) (`roles/assuredoss.reader`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  [Security Center Admin Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)  [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `pubsub.topics.publish`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Firebase Rules System](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaserules#firebaserules.system) (`roles/firebaserules.system`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Artifact Registry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.serviceAgent) (`roles/artifactregistry.serviceAgent`) 
  * [Google Batch Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.serviceAgent) (`roles/batch.serviceAgent`) 
  * [Cloud Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent) (`roles/cloudasset.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud IoT Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudiot#cloudiot.serviceAgent) (`roles/cloudiot.serviceAgent`) 
  * [Cloud Scheduler Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.serviceAgent) (`roles/cloudscheduler.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Registry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerregistry#containerregistry.ServiceAgent) (`roles/containerregistry.ServiceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) (`roles/datastream.serviceAgent`) 
  * [Device Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.serviceAgent) (`roles/devicerun.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Firebase Realtime Database Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.serviceAgent) (`roles/firebasedatabase.serviceAgent`) 
  * [Genomics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#genomics.serviceAgent) (`roles/genomics.serviceAgent`) 
  * [Healthcare Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.serviceAgent) (`roles/healthcare.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [KubeRun Events Data Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsDataPlaneServiceAgent) (`roles/kuberun.eventsDataPlaneServiceAgent`) 
  * [Cloud Life Sciences Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/lifesciences#lifesciences.serviceAgent) (`roles/lifesciences.serviceAgent`) 
  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 
  * [Security Center Notification Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.notificationServiceAgent) (`roles/securitycenter.notificationServiceAgent`) 
  * [Google Cloud Security Response Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityResponseServiceAgent) (`roles/securitycenter.securityResponseServiceAgent`) 
  * [Cloud Source Repositories Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/source#sourcerepo.serviceAgent) (`roles/sourcerepo.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Transcoder Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent) (`roles/transcoder.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [KubeRun Events Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun#kuberun.eventsControlPlaneServiceAgent) (`roles/kuberun.eventsControlPlaneServiceAgent`) 
  * [Secured Landing Zone Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.serviceAgent) (`roles/securedlandingzone.serviceAgent`) 

  
  
#### `pubsub.topics.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [SLZ BQDW Blueprint Project Level Remediator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.bqdwProjectRemediator) (`roles/securedlandingzone.bqdwProjectRemediator`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 
  * [Storage Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.serviceAgent) (`roles/storagetransfer.serviceAgent`) 
  * [Cloud Vision AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visionai#visionai.serviceAgent) (`roles/visionai.serviceAgent`) 

  
  
#### `pubsub.topics.updateTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)  [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Catalog Tag Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagEditor) (`roles/datacatalog.tagEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 
  * [Spectrum SAS Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent) (`roles/spectrumsas.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
