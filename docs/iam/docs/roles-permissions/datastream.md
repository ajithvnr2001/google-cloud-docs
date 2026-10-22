---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datastream/
title: Datastream roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:07.182654+00:00
---

# Datastream roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datastream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Datastream roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Datastream. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Datastream roles

Role | Permissions  
---|---  
  
#### Datastream Admin 

(`roles/datastream.admin`) Full access to all Datastream resources.  |  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `compute.networkAttachments.use` `datastream.*`

  * `datastream.connectionProfiles.create`
  * `datastream.connectionProfiles.createTagBinding`
  * `datastream.connectionProfiles.delete`
  * `datastream.connectionProfiles.deleteTagBinding`
  * `datastream.connectionProfiles.deriveDestinationSchema`
  * `datastream.connectionProfiles.destinationTypes`
  * `datastream.connectionProfiles.discover`
  * `datastream.connectionProfiles.get`
  * `datastream.connectionProfiles.getIamPolicy`
  * `datastream.connectionProfiles.list`
  * `datastream.connectionProfiles.listEffectiveTags`
  * `datastream.connectionProfiles.listStaticServiceIps`
  * `datastream.connectionProfiles.listTagBindings`
  * `datastream.connectionProfiles.setIamPolicy`
  * `datastream.connectionProfiles.sourceTypes`
  * `datastream.connectionProfiles.update`
  * `datastream.locations.fetchStaticIps`
  * `datastream.locations.get`
  * `datastream.locations.list`
  * `datastream.objects.get`
  * `datastream.objects.list`
  * `datastream.objects.startBackfillJob`
  * `datastream.objects.stopBackfillJob`
  * `datastream.operations.cancel`
  * `datastream.operations.delete`
  * `datastream.operations.get`
  * `datastream.operations.list`
  * `datastream.privateConnections.create`
  * `datastream.privateConnections.createTagBinding`
  * `datastream.privateConnections.delete`
  * `datastream.privateConnections.deleteTagBinding`
  * `datastream.privateConnections.get`
  * `datastream.privateConnections.getIamPolicy`
  * `datastream.privateConnections.list`
  * `datastream.privateConnections.listEffectiveTags`
  * `datastream.privateConnections.listTagBindings`
  * `datastream.privateConnections.setIamPolicy`
  * `datastream.routes.create`
  * `datastream.routes.delete`
  * `datastream.routes.get`
  * `datastream.routes.getIamPolicy`
  * `datastream.routes.list`
  * `datastream.routes.setIamPolicy`
  * `datastream.streams.computeState`
  * `datastream.streams.create`
  * `datastream.streams.createTagBinding`
  * `datastream.streams.delete`
  * `datastream.streams.deleteTagBinding`
  * `datastream.streams.fetchErrors`
  * `datastream.streams.get`
  * `datastream.streams.getIamPolicy`
  * `datastream.streams.list`
  * `datastream.streams.listEffectiveTags`
  * `datastream.streams.listTagBindings`
  * `datastream.streams.pause`
  * `datastream.streams.resume`
  * `datastream.streams.setIamPolicy`
  * `datastream.streams.start`
  * `datastream.streams.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Datastream Viewer 

(`roles/datastream.viewer`) Read-only access to all Datastream resources.  |  `datastream.connectionProfiles.deriveDestinationSchema` `datastream.connectionProfiles.destinationTypes` `datastream.connectionProfiles.discover` `datastream.connectionProfiles.get` `datastream.connectionProfiles.getIamPolicy` `datastream.connectionProfiles.list` `datastream.connectionProfiles.listEffectiveTags` `datastream.connectionProfiles.listStaticServiceIps` `datastream.connectionProfiles.listTagBindings` `datastream.connectionProfiles.sourceTypes` `datastream.locations.*`

  * `datastream.locations.fetchStaticIps`
  * `datastream.locations.get`
  * `datastream.locations.list`

`datastream.objects.get` `datastream.objects.list` `datastream.operations.get` `datastream.operations.list` `datastream.privateConnections.get` `datastream.privateConnections.getIamPolicy` `datastream.privateConnections.list` `datastream.privateConnections.listEffectiveTags` `datastream.privateConnections.listTagBindings` `datastream.routes.get` `datastream.routes.getIamPolicy` `datastream.routes.list` `datastream.streams.fetchErrors` `datastream.streams.get` `datastream.streams.getIamPolicy` `datastream.streams.list` `datastream.streams.listEffectiveTags` `datastream.streams.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Datastream Bigquery Writer 

(`roles/datastream.bigqueryWriter`) Permissions needed for datastream to write to BigQuery.  |  `bigquery.connections.delegate` `bigquery.connections.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.delete` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.update` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `datastream.connectionProfiles.create` `datastream.connectionProfiles.delete` `datastream.connectionProfiles.deriveDestinationSchema` `datastream.connectionProfiles.destinationTypes` `datastream.connectionProfiles.discover` `datastream.connectionProfiles.get` `datastream.connectionProfiles.getIamPolicy` `datastream.connectionProfiles.list` `datastream.connectionProfiles.listEffectiveTags` `datastream.connectionProfiles.listStaticServiceIps` `datastream.connectionProfiles.listTagBindings` `datastream.connectionProfiles.sourceTypes` `datastream.connectionProfiles.update` `datastream.locations.*`

  * `datastream.locations.fetchStaticIps`
  * `datastream.locations.get`
  * `datastream.locations.list`

`datastream.objects.*`

  * `datastream.objects.get`
  * `datastream.objects.list`
  * `datastream.objects.startBackfillJob`
  * `datastream.objects.stopBackfillJob`

`datastream.operations.*`

  * `datastream.operations.cancel`
  * `datastream.operations.delete`
  * `datastream.operations.get`
  * `datastream.operations.list`

`datastream.privateConnections.create` `datastream.privateConnections.delete` `datastream.privateConnections.get` `datastream.privateConnections.getIamPolicy` `datastream.privateConnections.list` `datastream.privateConnections.listEffectiveTags` `datastream.privateConnections.listTagBindings` `datastream.routes.create` `datastream.routes.delete` `datastream.routes.get` `datastream.routes.getIamPolicy` `datastream.routes.list` `datastream.streams.computeState` `datastream.streams.create` `datastream.streams.delete` `datastream.streams.fetchErrors` `datastream.streams.get` `datastream.streams.getIamPolicy` `datastream.streams.list` `datastream.streams.listEffectiveTags` `datastream.streams.listTagBindings` `datastream.streams.pause` `datastream.streams.resume` `datastream.streams.start` `datastream.streams.update`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Datastream Service Agent 

(`roles/datastream.serviceAgent`) Grants Cloud Datastream permissions to write data in the user project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.connections.delegate` `bigquery.connections.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.delete` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.update` `bigquery.routines.get` `bigquery.routines.list` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `compute.globalAddresses.create` `compute.globalAddresses.createInternal` `compute.globalAddresses.delete` `compute.globalAddresses.deleteInternal` `compute.globalAddresses.get` `compute.globalOperations.get` `compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networks.addPeering` `compute.networks.get` `compute.networks.listPeeringRoutes` `compute.networks.removePeering` `compute.networks.use` `compute.routes.get` `compute.routes.list` `compute.subnetworks.get` `compute.subnetworks.list` `monitoring.timeSeries.list` `pubsub.topics.publish` `spanner.databases.beginReadOnlyTransaction` `spanner.databases.getDdl` `spanner.databases.partitionQuery` `spanner.databases.partitionRead` `spanner.databases.read` `spanner.databases.select` `spanner.databases.useDataBoost` `spanner.databases.useRoleBasedAccess` `spanner.sessions.create` `spanner.sessions.delete` `spanner.sessions.get` `storage.buckets.get` `storage.objects.create` `storage.objects.get` `storage.objects.list`  
  
## Datastream permissions

Permission | Included in roles  
---|---  
  
#### `datastream.connectionProfiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.connectionProfiles.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.connectionProfiles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.connectionProfiles.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.connectionProfiles.deriveDestinationSchema`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.destinationTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.discover`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datastream.connectionProfiles.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.listStaticServiceIps`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datastream.connectionProfiles.sourceTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.connectionProfiles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.locations.fetchStaticIps`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datastream.objects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.objects.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.objects.startBackfillJob`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.objects.stopBackfillJob`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.privateConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.privateConnections.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.privateConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.privateConnections.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.privateConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.privateConnections.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.privateConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datastream.privateConnections.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.privateConnections.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.privateConnections.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datastream.routes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.routes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.routes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.routes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.routes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.routes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datastream.streams.computeState`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.streams.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.streams.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.streams.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.streams.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datastream.streams.fetchErrors`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.streams.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
#### `datastream.streams.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.streams.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `datastream.streams.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.streams.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.viewer) (`roles/datastream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datastream.streams.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.streams.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.streams.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `datastream.streams.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)   
  
#### `datastream.streams.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`)  [Datastream Bigquery Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.bigqueryWriter) (`roles/datastream.bigqueryWriter`)  [Dataproc Metastore Managed Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.migrationAdmin) (`roles/metastore.migrationAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
