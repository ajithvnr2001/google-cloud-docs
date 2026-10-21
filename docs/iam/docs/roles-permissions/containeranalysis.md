---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis/
title: Artifact Analysis roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:34.539738+00:00
---

# Artifact Analysis roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Artifact Analysis roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Artifact Analysis. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Artifact Analysis roles

Role | Permissions  
---|---  
  
#### Container Analysis Admin 

(`roles/containeranalysis.admin`) Access to all Container Analysis resources.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.notes.setIamPolicy` `containeranalysis.notes.update` `containeranalysis.occurrences.*`

  * `containeranalysis.occurrences.create`
  * `containeranalysis.occurrences.delete`
  * `containeranalysis.occurrences.get`
  * `containeranalysis.occurrences.getIamPolicy`
  * `containeranalysis.occurrences.list`
  * `containeranalysis.occurrences.setIamPolicy`
  * `containeranalysis.occurrences.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Editor 

(`roles/containeranalysis.editor`) Editor role for Container Analysis  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.notes.listOccurrences` `containeranalysis.notes.update` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.getIamPolicy` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Viewer 

(`roles/containeranalysis.viewer`) Viewer role for Container Analysis  |  `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.occurrences.get` `containeranalysis.occurrences.getIamPolicy` `containeranalysis.occurrences.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Notes Attacher 

(`roles/containeranalysis.notes.attacher`) Can attach Container Analysis Occurrences to Notes.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.get`  
  
#### Container Analysis Notes Editor 

(`roles/containeranalysis.notes.editor`) Can edit Container Analysis Notes.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.list` `containeranalysis.notes.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences for Notes Viewer 

(`roles/containeranalysis.notes.occurrences.viewer`) Can view all Container Analysis Occurrences attached to a Note.  |  `containeranalysis.notes.get` `containeranalysis.notes.listOccurrences`  
  
#### Container Analysis Notes Viewer 

(`roles/containeranalysis.notes.viewer`) Can view Container Analysis Notes.  |  `containeranalysis.notes.get` `containeranalysis.notes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences Editor 

(`roles/containeranalysis.occurrences.editor`) Can edit Container Analysis Occurrences.  |  `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences Viewer 

(`roles/containeranalysis.occurrences.viewer`) Can view Container Analysis Occurrences.  |  `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Container Analysis Service Agent 

(`roles/containeranalysis.ServiceAgent`) Gives Container Analysis API the access it needs to function  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `containeranalysis.notes.list` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `pubsub.messageTransforms.validate` `pubsub.schemas.attach` `pubsub.schemas.commit` `pubsub.schemas.create` `pubsub.schemas.delete` `pubsub.schemas.get` `pubsub.schemas.getIamPolicy` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.rollback` `pubsub.schemas.validate` `pubsub.snapshots.create` `pubsub.snapshots.delete` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.update` `pubsub.topics.updateTag` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.objects.get` `storage.objects.list`  
  
## Artifact Analysis permissions

Permission | Included in roles  
---|---  
  
#### `containeranalysis.notes.attachOccurrence`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Notes Attacher](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.attacher) (`roles/containeranalysis.notes.attacher`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.notes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.notes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.notes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Container Analysis Notes Attacher](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.attacher) (`roles/containeranalysis.notes.attacher`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  [Container Analysis Occurrences for Notes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.occurrences.viewer) (`roles/containeranalysis.notes.occurrences.viewer`)  [Container Analysis Notes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.viewer) (`roles/containeranalysis.notes.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.notes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `containeranalysis.notes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  [Container Analysis Notes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.viewer) (`roles/containeranalysis.notes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.notes.listOccurrences`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Occurrences for Notes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.occurrences.viewer) (`roles/containeranalysis.notes.occurrences.viewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 

  
  
#### `containeranalysis.notes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `containeranalysis.notes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Notes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.occurrences.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Container Analysis Occurrences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.editor) (`roles/containeranalysis.occurrences.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.occurrences.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Container Analysis Occurrences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.editor) (`roles/containeranalysis.occurrences.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.occurrences.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Container Analysis Occurrences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.editor) (`roles/containeranalysis.occurrences.editor`)  [Container Analysis Occurrences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)  [Developer Connect Insights Config Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.insightsAgent) (`roles/developerconnect.insightsAgent`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.occurrences.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `containeranalysis.occurrences.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Container Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.viewer) (`roles/containeranalysis.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Container Analysis Occurrences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.editor) (`roles/containeranalysis.occurrences.editor`)  [Container Analysis Occurrences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)  [Developer Connect Insights Config Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.insightsAgent) (`roles/developerconnect.insightsAgent`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
#### `containeranalysis.occurrences.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `containeranalysis.occurrences.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Container Analysis Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)  [Container Analysis Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.editor) (`roles/containeranalysis.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Container Analysis Occurrences Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.editor) (`roles/containeranalysis.occurrences.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Compliance Scanning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/compliancescanning#compliancescanning.serviceAgent) (`roles/compliancescanning.serviceAgent`) 
  * [Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent) (`roles/containeranalysis.ServiceAgent`) 
  * [Container Scanner Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`) 
  * [Cloud OS Config Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent) (`roles/osconfig.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
