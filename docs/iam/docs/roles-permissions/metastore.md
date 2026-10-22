---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/metastore/
title: Dataproc Metastore roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:11.896539+00:00
---

# Dataproc Metastore roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/metastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Dataproc Metastore roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Dataproc Metastore. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Dataproc Metastore roles

Role | Permissions  
---|---  
  
#### Dataproc Metastore Admin 

(`roles/metastore.admin`) Full access to all Dataproc Metastore resources.  |  `metastore.backups.*`

  * `metastore.backups.create`
  * `metastore.backups.delete`
  * `metastore.backups.get`
  * `metastore.backups.getIamPolicy`
  * `metastore.backups.list`
  * `metastore.backups.setIamPolicy`
  * `metastore.backups.use`

`metastore.federations.*`

  * `metastore.federations.create`
  * `metastore.federations.createTagBinding`
  * `metastore.federations.delete`
  * `metastore.federations.deleteTagBinding`
  * `metastore.federations.get`
  * `metastore.federations.getIamPolicy`
  * `metastore.federations.list`
  * `metastore.federations.listEffectiveTags`
  * `metastore.federations.listTagBindings`
  * `metastore.federations.setIamPolicy`
  * `metastore.federations.update`
  * `metastore.federations.use`

`metastore.imports.*`

  * `metastore.imports.create`
  * `metastore.imports.get`
  * `metastore.imports.list`
  * `metastore.imports.update`

`metastore.locations.*`

  * `metastore.locations.get`
  * `metastore.locations.list`

`metastore.migrations.*`

  * `metastore.migrations.cancel`
  * `metastore.migrations.complete`
  * `metastore.migrations.delete`
  * `metastore.migrations.get`
  * `metastore.migrations.list`
  * `metastore.migrations.start`

`metastore.operations.*`

  * `metastore.operations.cancel`
  * `metastore.operations.delete`
  * `metastore.operations.get`
  * `metastore.operations.list`

`metastore.services.create` `metastore.services.createTagBinding` `metastore.services.delete` `metastore.services.deleteTagBinding` `metastore.services.export` `metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `metastore.services.mutateMetadata` `metastore.services.queryMetadata` `metastore.services.restore` `metastore.services.setIamPolicy` `metastore.services.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Metastore Editor 

(`roles/metastore.editor`) Read and write access to all Dataproc Metastore resources.  |  `metastore.backups.create` `metastore.backups.delete` `metastore.backups.get` `metastore.backups.getIamPolicy` `metastore.backups.list` `metastore.backups.use` `metastore.federations.create` `metastore.federations.delete` `metastore.federations.get` `metastore.federations.getIamPolicy` `metastore.federations.list` `metastore.federations.listEffectiveTags` `metastore.federations.listTagBindings` `metastore.federations.update` `metastore.federations.use` `metastore.imports.*`

  * `metastore.imports.create`
  * `metastore.imports.get`
  * `metastore.imports.list`
  * `metastore.imports.update`

`metastore.locations.*`

  * `metastore.locations.get`
  * `metastore.locations.list`

`metastore.migrations.*`

  * `metastore.migrations.cancel`
  * `metastore.migrations.complete`
  * `metastore.migrations.delete`
  * `metastore.migrations.get`
  * `metastore.migrations.list`
  * `metastore.migrations.start`

`metastore.operations.*`

  * `metastore.operations.cancel`
  * `metastore.operations.delete`
  * `metastore.operations.get`
  * `metastore.operations.list`

`metastore.services.create` `metastore.services.createTagBinding` `metastore.services.delete` `metastore.services.deleteTagBinding` `metastore.services.export` `metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `metastore.services.restore` `metastore.services.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Metastore Viewer 

(`roles/metastore.viewer`) Viewer role for Dataproc Metastore  |  `metastore.backups.get` `metastore.backups.getIamPolicy` `metastore.backups.list` `metastore.backups.use` `metastore.databases.get` `metastore.databases.getIamPolicy` `metastore.databases.list` `metastore.federations.get` `metastore.federations.getIamPolicy` `metastore.federations.list` `metastore.federations.listEffectiveTags` `metastore.federations.listTagBindings` `metastore.imports.get` `metastore.imports.list` `metastore.locations.*`

  * `metastore.locations.get`
  * `metastore.locations.list`

`metastore.migrations.get` `metastore.migrations.list` `metastore.operations.get` `metastore.operations.list` `metastore.services.export` `metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `metastore.tables.get` `metastore.tables.getIamPolicy` `metastore.tables.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Metastore Federation Accessor 

(`roles/metastore.federationAccessor`) Access to the Metastore Federation resource.  |  `metastore.federations.use`  
  
#### Dataproc Metastore Metadata Editor 

(`roles/metastore.metadataEditor`) Access to read and modify the metadata of databases and tables under those databases.  |  `metastore.databases.create` `metastore.databases.delete` `metastore.databases.get` `metastore.databases.getIamPolicy` `metastore.databases.list` `metastore.databases.update` `metastore.services.get` `metastore.services.use` `metastore.tables.create` `metastore.tables.delete` `metastore.tables.get` `metastore.tables.getIamPolicy` `metastore.tables.list` `metastore.tables.update`  
  
#### Dataproc Metastore Metadata Mutate Admin 

(`roles/metastore.metadataMutateAdmin`) Access to mutate metadata from a Dataproc Metastore service's underlying metadata store.  |  `metastore.services.mutateMetadata`  
  
#### Dataproc Metastore Metadata Operator 

(`roles/metastore.metadataOperator`) Read-only access to Dataproc Metastore resources with additional metadata operations permission.  |  `metastore.backups.create` `metastore.backups.delete` `metastore.backups.get` `metastore.backups.list` `metastore.backups.use` `metastore.imports.*`

  * `metastore.imports.create`
  * `metastore.imports.get`
  * `metastore.imports.list`
  * `metastore.imports.update`

`metastore.locations.*`

  * `metastore.locations.get`
  * `metastore.locations.list`

`metastore.operations.get` `metastore.operations.list` `metastore.services.export` `metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `metastore.services.restore` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Metastore Data Owner 

(`roles/metastore.metadataOwner`) Full access to the metadata of databases and tables under those databases.  |  `metastore.databases.*`

  * `metastore.databases.create`
  * `metastore.databases.delete`
  * `metastore.databases.get`
  * `metastore.databases.getIamPolicy`
  * `metastore.databases.list`
  * `metastore.databases.setIamPolicy`
  * `metastore.databases.update`

`metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `metastore.services.use` `metastore.tables.*`

  * `metastore.tables.create`
  * `metastore.tables.delete`
  * `metastore.tables.get`
  * `metastore.tables.getIamPolicy`
  * `metastore.tables.list`
  * `metastore.tables.setIamPolicy`
  * `metastore.tables.update`

  
  
#### Dataproc Metastore Metadata Query Admin 

(`roles/metastore.metadataQueryAdmin`) Access to query metadata from a Dataproc Metastore service's underlying metadata store.  |  `metastore.services.queryMetadata`  
  
#### Dataproc Metastore Metadata User 

(`roles/metastore.metadataUser`) Access to the Dataproc Metastore gRPC endpoint  |  `metastore.databases.get` `metastore.databases.list` `metastore.services.get` `metastore.services.use`  
  
#### Dataproc Metastore Metadata Viewer 

(`roles/metastore.metadataViewer`) Access to read the metadata of databases and tables under those databases  |  `metastore.databases.get` `metastore.databases.getIamPolicy` `metastore.databases.list` `metastore.services.get` `metastore.services.use` `metastore.tables.get` `metastore.tables.getIamPolicy` `metastore.tables.list`  
  
#### Dataproc Metastore Managed Migration Admin 

(`roles/metastore.migrationAdmin`) Access to Dataproc Metastore Managed Migration resources and workflow.  |  `cloudsql.instances.connect` `cloudsql.instances.get` `cloudsql.instances.login` `compute.autoscalers.create` `compute.autoscalers.delete` `compute.disks.create` `compute.disks.delete` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.use` `compute.instanceGroupManagers.create` `compute.instanceGroupManagers.delete` `compute.instanceGroupManagers.use` `compute.instanceGroups.delete` `compute.instanceGroups.use` `compute.instanceTemplates.create` `compute.instanceTemplates.delete` `compute.instanceTemplates.get` `compute.instanceTemplates.useReadOnly` `compute.instances.create` `compute.instances.delete` `compute.instances.get` `compute.instances.setMetadata` `compute.machineTypes.list` `compute.regionBackendServices.create` `compute.regionBackendServices.delete` `compute.regionBackendServices.use` `compute.regionHealthChecks.create` `compute.regionHealthChecks.delete` `compute.regionHealthChecks.use` `compute.regionHealthChecks.useReadOnly` `compute.serviceAttachments.create` `compute.serviceAttachments.delete` `compute.subnetworks.get` `compute.subnetworks.use` `compute.zones.list` `datastream.connectionProfiles.create` `datastream.connectionProfiles.delete` `datastream.objects.*`

  * `datastream.objects.get`
  * `datastream.objects.list`
  * `datastream.objects.startBackfillJob`
  * `datastream.objects.stopBackfillJob`

`datastream.operations.get` `datastream.privateConnections.create` `datastream.privateConnections.delete` `datastream.streams.create` `datastream.streams.delete` `datastream.streams.get` `datastream.streams.update`  
  
#### Dataproc Metastore Viewer 

(`roles/metastore.user`) Read-only access to all Dataproc Metastore resources.  |  `metastore.backups.get` `metastore.backups.list` `metastore.federations.get` `metastore.federations.getIamPolicy` `metastore.federations.list` `metastore.federations.listEffectiveTags` `metastore.federations.listTagBindings` `metastore.imports.get` `metastore.imports.list` `metastore.locations.*`

  * `metastore.locations.get`
  * `metastore.locations.list`

`metastore.operations.get` `metastore.operations.list` `metastore.services.export` `metastore.services.get` `metastore.services.getIamPolicy` `metastore.services.list` `metastore.services.listEffectiveTags` `metastore.services.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Dataproc Metastore Service Agent 

(`roles/metastore.serviceAgent`) Gives the Dataproc Metastore service account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.use` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.get` `compute.forwardingRules.pscCreate` `compute.forwardingRules.pscDelete` `compute.globalAddresses.createInternal` `compute.globalAddresses.deleteInternal` `compute.globalAddresses.get` `compute.globalAddresses.list` `compute.globalOperations.get` `compute.globalOperations.list` `compute.networks.addPeering` `compute.networks.get` `compute.networks.removePeering` `compute.networks.updatePeering` `compute.networks.use` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.use` `dns.changes.create` `dns.changes.get` `dns.managedZones.create` `dns.managedZones.delete` `dns.managedZones.get` `dns.managedZones.list` `dns.networks.bindPrivateDNSZone` `dns.networks.targetWithPeeringZone` `dns.resourceRecordSets.*`

  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.get`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

`metastore.databases.get` `metastore.databases.setIamPolicy` `metastore.databases.update` `metastore.federations.use` `metastore.services.get` `metastore.tables.get` `metastore.tables.setIamPolicy` `metastore.tables.update` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.services.create` `servicedirectory.services.delete` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Dataproc Metastore permissions

Permission | Included in roles  
---|---  
  
#### `metastore.backups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.backups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.backups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.backups.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `metastore.backups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.backups.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)   
  
#### `metastore.backups.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.databases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)   
  
#### `metastore.databases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)   
  
#### `metastore.databases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata User](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataUser) (`roles/metastore.metadataUser`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.databases.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)   
  
#### `metastore.databases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata User](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataUser) (`roles/metastore.metadataUser`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)   
  
#### `metastore.databases.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.databases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.federations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.federations.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `metastore.federations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.federations.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `metastore.federations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.federations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.federations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.federations.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.federations.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.federations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)   
  
#### `metastore.federations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.federations.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Metastore Federation Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.federationAccessor) (`roles/metastore.federationAccessor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.imports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.imports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.imports.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.imports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.migrations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.migrations.complete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.migrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.migrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `metastore.migrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `metastore.migrations.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.services.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.services.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `metastore.services.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.services.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `metastore.services.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.services.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata User](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataUser) (`roles/metastore.metadataUser`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.services.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.services.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `metastore.services.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.services.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.user) (`roles/metastore.user`)   
  
#### `metastore.services.mutateMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Metadata Mutate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataMutateAdmin) (`roles/metastore.metadataMutateAdmin`)   
  
#### `metastore.services.queryMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Metadata Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataQueryAdmin) (`roles/metastore.metadataQueryAdmin`)   
  
#### `metastore.services.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)  [Dataproc Metastore Metadata Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`)   
  
#### `metastore.services.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)   
  
#### `metastore.services.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)  [Dataproc Metastore Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)   
  
#### `metastore.services.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata User](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataUser) (`roles/metastore.metadataUser`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)   
  
#### `metastore.tables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)   
  
#### `metastore.tables.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)   
  
#### `metastore.tables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.tables.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)   
  
#### `metastore.tables.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Metastore Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.viewer) (`roles/metastore.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  [Dataproc Metastore Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`)   
  
#### `metastore.tables.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
#### `metastore.tables.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Metastore Metadata Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataEditor) (`roles/metastore.metadataEditor`)  [Dataproc Metastore Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOwner) (`roles/metastore.metadataOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
