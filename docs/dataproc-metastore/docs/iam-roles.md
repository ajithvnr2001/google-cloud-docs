---
url: https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles/
title: Dataproc Metastore IAM roles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:59.147477+00:00
---

# Dataproc Metastore IAM roles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

Dataproc Metastore defines several [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles. Each predefined role contains a set of IAM permissions that allow principals to perform certain actions. You can use an IAM policy to give a principal one or more IAM roles.

Identity and Access Management (IAM) also offers the ability to create customized IAM roles. You can create custom IAM roles and assign the role one or more permissions. Then, you can grant the new role to your principals. Use custom roles to create an access control model that maps directly to your needs, alongside the available predefined roles.

This page focuses on the IAM roles relevant to Dataproc Metastore.

## Before you begin

  * Read the [IAM](https://docs.cloud.google.com/iam) documentation.



## Dataproc Metastore roles

IAM Dataproc Metastore roles are a bundle of one or more permissions. You grant roles to principals to allow them to perform actions on the Dataproc Metastore resources in your project. For example, the **Dataproc Metastore User** role contains the `metastore.*.get` and `metastore.*.list` permissions, which allow a user to get and list Dataproc Metastore services, metadata imports, backups, and operations in a project.

The following table lists all Dataproc Metastore roles and the permissions associated with each role:

**Note:** The database and table permissions are used with gRPC-enabled Dataproc Metastore services. They have no effect when used with services using Thrift endpoints.

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
  
## What's next

  * Learn how to [create custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).
  * Learn how to [grant and manage roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * See the [Dataproc Metastore IAM permissions mapping](https://docs.cloud.google.com/dataproc-metastore/docs/iam-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
