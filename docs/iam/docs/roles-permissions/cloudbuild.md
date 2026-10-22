---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild/
title: Cloud Build roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:04.107734+00:00
---

# Cloud Build roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Build roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Build. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Build roles

Role | Permissions  
---|---  
  
#### Cloud Build Admin 

(`roles/cloudbuild.admin`) Admin role for Cloud Build  |  `cloudbuild.*`

  * `cloudbuild.builds.approve`
  * `cloudbuild.builds.create`
  * `cloudbuild.builds.get`
  * `cloudbuild.builds.list`
  * `cloudbuild.builds.update`
  * `cloudbuild.connections.create`
  * `cloudbuild.connections.delete`
  * `cloudbuild.connections.fetchLinkableRepositories`
  * `cloudbuild.connections.get`
  * `cloudbuild.connections.getIamPolicy`
  * `cloudbuild.connections.list`
  * `cloudbuild.connections.setIamPolicy`
  * `cloudbuild.connections.update`
  * `cloudbuild.integrations.create`
  * `cloudbuild.integrations.delete`
  * `cloudbuild.integrations.get`
  * `cloudbuild.integrations.list`
  * `cloudbuild.integrations.update`
  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`
  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`
  * `cloudbuild.repositories.accessReadToken`
  * `cloudbuild.repositories.accessReadWriteToken`
  * `cloudbuild.repositories.create`
  * `cloudbuild.repositories.delete`
  * `cloudbuild.repositories.fetchGitRefs`
  * `cloudbuild.repositories.get`
  * `cloudbuild.repositories.list`
  * `cloudbuild.workerpools.create`
  * `cloudbuild.workerpools.delete`
  * `cloudbuild.workerpools.get`
  * `cloudbuild.workerpools.list`
  * `cloudbuild.workerpools.update`
  * `cloudbuild.workerpools.use`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Service Account 

(`roles/cloudbuild.builds.builder`) Provides access to perform builds.  |  `artifactregistry.aptartifacts.create` `artifactregistry.attachments.*`

  * `artifactregistry.attachments.create`
  * `artifactregistry.attachments.delete`
  * `artifactregistry.attachments.get`
  * `artifactregistry.attachments.list`

`artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.files.update` `artifactregistry.files.upload` `artifactregistry.kfpartifacts.create` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.packages.update` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.createOnPush` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.create` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.tags.update` `artifactregistry.versions.get` `artifactregistry.versions.list` `artifactregistry.yumartifacts.create` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.workerpools.use` `compute.images.create` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `logging.logEntries.create` `logging.logEntries.list` `logging.views.access` `pubsub.topics.create` `pubsub.topics.publish` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `source.repos.get` `source.repos.list` `storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Cloud Build Editor 

(`roles/cloudbuild.editor`) Editor role for Cloud Build  |  `cloudbuild.builds.*`

  * `cloudbuild.builds.approve`
  * `cloudbuild.builds.create`
  * `cloudbuild.builds.get`
  * `cloudbuild.builds.list`
  * `cloudbuild.builds.update`

`cloudbuild.connections.create` `cloudbuild.connections.delete` `cloudbuild.connections.fetchLinkableRepositories` `cloudbuild.connections.get` `cloudbuild.connections.getIamPolicy` `cloudbuild.connections.list` `cloudbuild.connections.update` `cloudbuild.integrations.*`

  * `cloudbuild.integrations.create`
  * `cloudbuild.integrations.delete`
  * `cloudbuild.integrations.get`
  * `cloudbuild.integrations.list`
  * `cloudbuild.integrations.update`

`cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.repositories.create` `cloudbuild.repositories.delete` `cloudbuild.repositories.fetchGitRefs` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `cloudbuild.workerpools.*`

  * `cloudbuild.workerpools.create`
  * `cloudbuild.workerpools.delete`
  * `cloudbuild.workerpools.get`
  * `cloudbuild.workerpools.list`
  * `cloudbuild.workerpools.update`
  * `cloudbuild.workerpools.use`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Viewer 

(`roles/cloudbuild.viewer`) Viewer role for Cloud Build  |  `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.connections.fetchLinkableRepositories` `cloudbuild.connections.get` `cloudbuild.connections.getIamPolicy` `cloudbuild.connections.list` `cloudbuild.integrations.get` `cloudbuild.integrations.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.repositories.fetchGitRefs` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Approver 

(`roles/cloudbuild.builds.approver`) Can approve or reject pending builds.  |  `cloudbuild.builds.approve` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Editor 

(`roles/cloudbuild.builds.editor`) Provides access to create and cancel builds.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Viewer 

(`roles/cloudbuild.builds.viewer`) Provides access to view builds.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Connection Admin 

(`roles/cloudbuild.connectionAdmin`) Can manage connections and repositories.  |  `cloudbuild.connections.*`

  * `cloudbuild.connections.create`
  * `cloudbuild.connections.delete`
  * `cloudbuild.connections.fetchLinkableRepositories`
  * `cloudbuild.connections.get`
  * `cloudbuild.connections.getIamPolicy`
  * `cloudbuild.connections.list`
  * `cloudbuild.connections.setIamPolicy`
  * `cloudbuild.connections.update`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.repositories.create` `cloudbuild.repositories.delete` `cloudbuild.repositories.fetchGitRefs` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Connection Viewer 

(`roles/cloudbuild.connectionViewer`) Can view and list connections and repositories.  |  `cloudbuild.connections.fetchLinkableRepositories` `cloudbuild.connections.get` `cloudbuild.connections.getIamPolicy` `cloudbuild.connections.list` `cloudbuild.repositories.fetchGitRefs` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Integrations Editor 

(`roles/cloudbuild.integrationsEditor`) Can update Integrations  |  `cloudbuild.integrations.get` `cloudbuild.integrations.list` `cloudbuild.integrations.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Integrations Owner 

(`roles/cloudbuild.integrationsOwner`) Can create/delete Integrations  |  `cloudbuild.integrations.*`

  * `cloudbuild.integrations.create`
  * `cloudbuild.integrations.delete`
  * `cloudbuild.integrations.get`
  * `cloudbuild.integrations.list`
  * `cloudbuild.integrations.update`

`compute.firewalls.create` `compute.firewalls.get` `compute.firewalls.list` `compute.networks.get` `compute.networks.updatePolicy` `compute.regions.get` `compute.subnetworks.get` `compute.subnetworks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Integrations Viewer 

(`roles/cloudbuild.integrationsViewer`) Can view Integrations  |  `cloudbuild.integrations.get` `cloudbuild.integrations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build Read Only Token Accessor 

(`roles/cloudbuild.readTokenAccessor`) Can view the connection and access its read-only token.  |  `cloudbuild.connections.get` `cloudbuild.repositories.accessReadToken` `cloudbuild.repositories.get`  
  
#### Cloud Build Token Accessor 

(`roles/cloudbuild.tokenAccessor`) Can view the connection and access its read/write and read-only tokens.  |  `cloudbuild.connections.get` `cloudbuild.repositories.accessReadToken` `cloudbuild.repositories.accessReadWriteToken` `cloudbuild.repositories.get` `cloudbuild.repositories.list`  
  
#### Cloud Build WorkerPool Editor 

(`roles/cloudbuild.workerPoolEditor`) Can update and view WorkerPools  |  `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `cloudbuild.workerpools.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build WorkerPool Owner 

(`roles/cloudbuild.workerPoolOwner`) Can create, delete, update, and view WorkerPools  |  `cloudbuild.workerpools.create` `cloudbuild.workerpools.delete` `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `cloudbuild.workerpools.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Build WorkerPool User 

(`roles/cloudbuild.workerPoolUser`) Can run builds in the WorkerPool  |  `cloudbuild.workerpools.use`  
  
#### Cloud Build WorkerPool Viewer 

(`roles/cloudbuild.workerPoolViewer`) Can view WorkerPools  |  `cloudbuild.workerpools.get` `cloudbuild.workerpools.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Build Logging Service Agent 

(`roles/cloudbuild.loggingServiceAgent`) Gives the Cloud Build logging-specific service account access to write logs.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `logging.buckets.write`  
  
#### Cloud Build Service Agent 

(`roles/cloudbuild.serviceAgent`) Gives Cloud Build service account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.aptartifacts.create` `artifactregistry.attachments.*`

  * `artifactregistry.attachments.create`
  * `artifactregistry.attachments.delete`
  * `artifactregistry.attachments.get`
  * `artifactregistry.attachments.list`

`artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.files.update` `artifactregistry.files.upload` `artifactregistry.kfpartifacts.create` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.packages.update` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.createOnPush` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.create` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.tags.update` `artifactregistry.versions.get` `artifactregistry.versions.list` `artifactregistry.yumartifacts.create` `binaryauthorization.attestors.create` `binaryauthorization.attestors.delete` `binaryauthorization.attestors.get` `binaryauthorization.attestors.list` `binaryauthorization.attestors.update` `binaryauthorization.attestors.verifyImageAttested` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.connections.get` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudbuild.repositories.accessReadToken` `cloudbuild.repositories.accessReadWriteToken` `cloudbuild.repositories.get` `cloudbuild.repositories.list` `cloudbuild.workerpools.use` `compute.firewalls.get` `compute.firewalls.list` `compute.images.create` `compute.networkAttachments.get` `compute.networkAttachments.update` `compute.networks.get` `compute.regionOperations.get` `compute.subnetworks.get` `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.list` `containeranalysis.notes.update` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `developerconnect.connections.get` `developerconnect.gitRepositoryLinks.fetchReadToken` `developerconnect.gitRepositoryLinks.fetchReadWriteToken` `developerconnect.gitRepositoryLinks.get` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.buckets.create` `logging.buckets.get` `logging.buckets.list` `logging.logEntries.create` `logging.logEntries.list` `logging.views.access` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.get` `pubsub.topics.publish` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.networks.access` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve` `serviceusage.services.use` `source.repos.get` `source.repos.list` `storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Cloud Build permissions

Permission | Included in roles  
---|---  
  
#### `cloudbuild.builds.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)   
  
#### `cloudbuild.builds.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 

  
  
#### `cloudbuild.builds.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent) (`roles/appengineflex.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 

  
  
#### `cloudbuild.builds.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Application Design Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Application Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationAdmin) (`roles/designcenter.applicationAdmin`)  [Application Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.applicationEditor) (`roles/designcenter.applicationEditor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DesignCenter Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent) (`roles/designcenter.serviceAgent`) 

  
  
#### `cloudbuild.builds.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 

  
  
#### `cloudbuild.connections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.connections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.connections.fetchLinkableRepositories`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.connections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Cloud Build Read Only Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.readTokenAccessor) (`roles/cloudbuild.readTokenAccessor`)  [Cloud Build Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.tokenAccessor) (`roles/cloudbuild.tokenAccessor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Gemini for Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent) (`roles/cloudaicompanion.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 

  
  
#### `cloudbuild.connections.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.connections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `cloudbuild.connections.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.connections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.integrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Integrations Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsOwner) (`roles/cloudbuild.integrationsOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.integrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Integrations Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsOwner) (`roles/cloudbuild.integrationsOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.integrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build Integrations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsEditor) (`roles/cloudbuild.integrationsEditor`)  [Cloud Build Integrations Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsOwner) (`roles/cloudbuild.integrationsOwner`)  [Cloud Build Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsViewer) (`roles/cloudbuild.integrationsViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.integrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Integrations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsEditor) (`roles/cloudbuild.integrationsEditor`)  [Cloud Build Integrations Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsOwner) (`roles/cloudbuild.integrationsOwner`)  [Cloud Build Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsViewer) (`roles/cloudbuild.integrationsViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.integrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Integrations Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsEditor) (`roles/cloudbuild.integrationsEditor`)  [Cloud Build Integrations Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.integrationsOwner) (`roles/cloudbuild.integrationsOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 

  
  
#### `cloudbuild.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 

  
  
#### `cloudbuild.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 

  
  
#### `cloudbuild.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Functions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.admin) (`roles/cloudfunctions.admin`)  [Cloud Functions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.editor) (`roles/cloudfunctions.editor`)  [Cloud Functions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.viewer) (`roles/cloudfunctions.viewer`)  [Dataflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin) (`roles/dataflow.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.approver) (`roles/cloudbuild.builds.approver`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Functions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dataflow Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)  [Cloud Run Source Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceViewer) (`roles/run.sourceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 

  
  
#### `cloudbuild.repositories.accessReadToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Read Only Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.readTokenAccessor) (`roles/cloudbuild.readTokenAccessor`)  [Cloud Build Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.tokenAccessor) (`roles/cloudbuild.tokenAccessor`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Gemini for Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent) (`roles/cloudaicompanion.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `cloudbuild.repositories.accessReadWriteToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.tokenAccessor) (`roles/cloudbuild.tokenAccessor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 

  
  
#### `cloudbuild.repositories.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.repositories.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.repositories.fetchGitRefs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Gemini for Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent) (`roles/cloudaicompanion.serviceAgent`) 

  
  
#### `cloudbuild.repositories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Cloud Build Read Only Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.readTokenAccessor) (`roles/cloudbuild.readTokenAccessor`)  [Cloud Build Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.tokenAccessor) (`roles/cloudbuild.tokenAccessor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Gemini for Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent) (`roles/cloudaicompanion.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Firebase App Hosting Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent) (`roles/firebaseapphosting.serviceAgent`) 

  
  
#### `cloudbuild.repositories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`)  [Cloud Build Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionViewer) (`roles/cloudbuild.connectionViewer`)  [Cloud Build Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.tokenAccessor) (`roles/cloudbuild.tokenAccessor`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Gemini for Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent) (`roles/cloudaicompanion.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `cloudbuild.workerpools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build WorkerPool Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.workerpools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build WorkerPool Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.workerpools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Cloud Build WorkerPool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolEditor) (`roles/cloudbuild.workerPoolEditor`)  [Cloud Build WorkerPool Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`)  [Cloud Build WorkerPool Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolViewer) (`roles/cloudbuild.workerPoolViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.workerpools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.viewer) (`roles/cloudbuild.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Build WorkerPool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolEditor) (`roles/cloudbuild.workerPoolEditor`)  [Cloud Build WorkerPool Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`)  [Cloud Build WorkerPool Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolViewer) (`roles/cloudbuild.workerPoolViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudbuild.workerpools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build WorkerPool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolEditor) (`roles/cloudbuild.workerPoolEditor`)  [Cloud Build WorkerPool Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `cloudbuild.workerpools.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Build Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.admin) (`roles/cloudbuild.admin`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.editor) (`roles/cloudbuild.editor`)  [Cloud Build WorkerPool User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolUser) (`roles/cloudbuild.workerPoolUser`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Infrastructure Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent) (`roles/cloudconfig.serviceAgent`) 
  * [Cloud Deploy Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent) (`roles/clouddeploy.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
