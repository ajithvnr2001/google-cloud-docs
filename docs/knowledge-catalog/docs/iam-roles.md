---
url: https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles/
title: Knowledge Catalog IAM roles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:41:49.939606+00:00
---

# Knowledge Catalog IAM roles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Knowledge Catalog IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

Identity and access management (IAM) lets you control who can do what within Knowledge Catalog (formerly Dataplex Universal Catalog). You can adopt the security principle of least privilege, to protect private data, avoid unauthorized access, reduce the attack surface, or meet regulatory compliance.

Knowledge Catalog provides several predefined IAM roles, each with a specific set of permissions that let users perform actions. You can grant these roles using an IAM policy.

For more granular control, you can create a custom IAM role by choosing specific permissions and assigning that new role to users. Custom roles let you build an access model that matches your organization's needs.

This document describes the predefined and custom IAM roles that are relevant to Knowledge Catalog.

For a detailed description of IAM and its features, see the [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs).

**Note:** Some Knowledge Catalog features depend on other Google Cloud services. For example, Knowledge Catalog connectors use BigQuery Data Transfer Service to import metadata. To view and manage connector configurations, you need the following roles:

  * To view connector configurations and run history: 
    * BigQuery User (`roles/bigquery.user`)
    * Dataplex Viewer (`roles/dataplex.viewer`)
  * To create, edit, delete, or manually run connector configurations: 
    * BigQuery Admin (`roles/bigquery.admin`)
    * Dataplex Administrator (`roles/dataplex.admin`) or Dataplex Editor (`roles/dataplex.editor`)



Additionally, you must grant the BigQuery Data Transfer Service service agent (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`) the `dataplex.entryGroups.import` permission or the Dataplex Entry Group Importer (`roles/dataplex.entryGroupImporter`) role. This can be granted either at the project level or at the entry group level.

See [About Knowledge Catalog Connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors).

Make sure you granted access to the Knowledge Catalog entries before using them.

## About Knowledge Catalog roles

Knowledge Catalog IAM roles are a bundle of one or more permissions. You grant roles to principals to let them perform actions on the Knowledge Catalog resources in your project. For example, the Dataplex Viewer role contains the `dataplex.*.get` and `dataplex.*.list` permissions, which let users get and list Knowledge Catalog resources in a project. For more information, see [Knowledge Catalog permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions).

You can apply Knowledge Catalog roles to any resources in the service hierarchy, including the following:

  * Projects
  * Lakes, data zones, and assets
  * Data scans, tasks, and environments
  * Entry groups, entry types, entry link types, aspect types, and glossaries
  * Data taxonomies, data attributes, and data attribute bindings



## Predefined roles for Knowledge Catalog

Predefined roles contain the permissions that are needed to perform a task or a group of related tasks.

The following roles provide broad access to BigQuery resources:

Role | Description  
---|---  
**Dataplex Administrator**  
(`roles/dataplex.admin`) | Full access to BigQuery resources.  
**Dataplex Editor**  
(`roles/dataplex.editor`) | Edit access to BigQuery resources.  
**Dataplex Viewer**  
(`roles/dataplex.viewer`) | Read-only access to BigQuery resources.  
**Dataplex Developer**  
(`roles/dataplex.developer`) | Lets you run data analytics workloads.  
  
The **Dataplex Administrator** (`roles/dataplex.admin`), **Dataplex Editor** (`roles/dataplex.editor`), and **Dataplex Viewer** (`roles/dataplex.viewer`) roles don't provide access to metadata resources such as entry groups, entries, entry links, entry types, entry link types, and aspect types.

The following table lists the Knowledge Catalog predefined roles and the permissions associated with each role:

Role | Permissions  
---|---  
  
#### Dataplex Administrator 

(`roles/dataplex.admin`) Full access to Dataplex Universal Catalog resources, except for catalog resources like entries and entry groups.  |  `cloudasset.assets.analyzeIamPolicy` `cloudasset.assets.searchAllIamPolicies` `cloudasset.assets.searchAllResources` `dataplex.agentTasks.*`

  * `dataplex.agentTasks.create`
  * `dataplex.agentTasks.delete`
  * `dataplex.agentTasks.get`
  * `dataplex.agentTasks.getData`
  * `dataplex.agentTasks.getIamPolicy`
  * `dataplex.agentTasks.list`
  * `dataplex.agentTasks.run`
  * `dataplex.agentTasks.setIamPolicy`
  * `dataplex.agentTasks.update`

`dataplex.assetActions.list` `dataplex.assets.create` `dataplex.assets.delete` `dataplex.assets.get` `dataplex.assets.getIamPolicy` `dataplex.assets.list` `dataplex.assets.setIamPolicy` `dataplex.assets.update` `dataplex.changeRequests.*`

  * `dataplex.changeRequests.adminDelete`
  * `dataplex.changeRequests.delete`
  * `dataplex.changeRequests.get`
  * `dataplex.changeRequests.getIamPolicy`
  * `dataplex.changeRequests.list`
  * `dataplex.changeRequests.setIamPolicy`
  * `dataplex.changeRequests.update`
  * `dataplex.changeRequests.use`

`dataplex.content.*`

  * `dataplex.content.create`
  * `dataplex.content.delete`
  * `dataplex.content.get`
  * `dataplex.content.getIamPolicy`
  * `dataplex.content.list`
  * `dataplex.content.setIamPolicy`
  * `dataplex.content.update`

`dataplex.dataAssets.*`

  * `dataplex.dataAssets.create`
  * `dataplex.dataAssets.delete`
  * `dataplex.dataAssets.get`
  * `dataplex.dataAssets.list`
  * `dataplex.dataAssets.update`

`dataplex.dataAttributeBindings.*`

  * `dataplex.dataAttributeBindings.create`
  * `dataplex.dataAttributeBindings.delete`
  * `dataplex.dataAttributeBindings.get`
  * `dataplex.dataAttributeBindings.getIamPolicy`
  * `dataplex.dataAttributeBindings.list`
  * `dataplex.dataAttributeBindings.setIamPolicy`
  * `dataplex.dataAttributeBindings.update`

`dataplex.dataAttributes.*`

  * `dataplex.dataAttributes.bind`
  * `dataplex.dataAttributes.create`
  * `dataplex.dataAttributes.delete`
  * `dataplex.dataAttributes.get`
  * `dataplex.dataAttributes.getIamPolicy`
  * `dataplex.dataAttributes.list`
  * `dataplex.dataAttributes.setIamPolicy`
  * `dataplex.dataAttributes.update`

`dataplex.dataDomainBindings.*`

  * `dataplex.dataDomainBindings.create`
  * `dataplex.dataDomainBindings.delete`
  * `dataplex.dataDomainBindings.get`
  * `dataplex.dataDomainBindings.list`

`dataplex.dataDomains.*`

  * `dataplex.dataDomains.create`
  * `dataplex.dataDomains.delete`
  * `dataplex.dataDomains.discover`
  * `dataplex.dataDomains.get`
  * `dataplex.dataDomains.getIamPolicy`
  * `dataplex.dataDomains.list`
  * `dataplex.dataDomains.lookupEntry`
  * `dataplex.dataDomains.modifyEntry`
  * `dataplex.dataDomains.setIamPolicy`
  * `dataplex.dataDomains.update`

`dataplex.dataProducts.*`

  * `dataplex.dataProducts.approve`
  * `dataplex.dataProducts.create`
  * `dataplex.dataProducts.delete`
  * `dataplex.dataProducts.get`
  * `dataplex.dataProducts.getIamPolicy`
  * `dataplex.dataProducts.list`
  * `dataplex.dataProducts.setIamPolicy`
  * `dataplex.dataProducts.update`

`dataplex.dataTaxonomies.*`

  * `dataplex.dataTaxonomies.configureDataAccess`
  * `dataplex.dataTaxonomies.configureResourceAccess`
  * `dataplex.dataTaxonomies.create`
  * `dataplex.dataTaxonomies.delete`
  * `dataplex.dataTaxonomies.get`
  * `dataplex.dataTaxonomies.getIamPolicy`
  * `dataplex.dataTaxonomies.list`
  * `dataplex.dataTaxonomies.setIamPolicy`
  * `dataplex.dataTaxonomies.update`

`dataplex.datascans.*`

  * `dataplex.datascans.cancel`
  * `dataplex.datascans.create`
  * `dataplex.datascans.delete`
  * `dataplex.datascans.get`
  * `dataplex.datascans.getData`
  * `dataplex.datascans.getIamPolicy`
  * `dataplex.datascans.list`
  * `dataplex.datascans.run`
  * `dataplex.datascans.setIamPolicy`
  * `dataplex.datascans.update`

`dataplex.entities.*`

  * `dataplex.entities.create`
  * `dataplex.entities.delete`
  * `dataplex.entities.get`
  * `dataplex.entities.list`
  * `dataplex.entities.update`

`dataplex.entries.link` `dataplex.entryGroups.createTagBinding` `dataplex.entryGroups.deleteTagBinding` `dataplex.entryGroups.export` `dataplex.entryGroups.import` `dataplex.entryGroups.listEffectiveTags` `dataplex.entryGroups.listTagBindings` `dataplex.entryGroups.requestChanges` `dataplex.entryGroups.useContextEntryLink` `dataplex.entryGroups.useDefinitionEntryLink` `dataplex.entryGroups.useRelatedEntryLink` `dataplex.entryGroups.useSchemaJoinEntryLink` `dataplex.entryGroups.useSynonymEntryLink` `dataplex.entryLinks.*`

  * `dataplex.entryLinks.create`
  * `dataplex.entryLinks.delete`
  * `dataplex.entryLinks.get`
  * `dataplex.entryLinks.reference`
  * `dataplex.entryLinks.update`

`dataplex.entryTypes.createTagBinding` `dataplex.entryTypes.deleteTagBinding` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.environments.*`

  * `dataplex.environments.create`
  * `dataplex.environments.delete`
  * `dataplex.environments.execute`
  * `dataplex.environments.get`
  * `dataplex.environments.getIamPolicy`
  * `dataplex.environments.list`
  * `dataplex.environments.setIamPolicy`
  * `dataplex.environments.update`

`dataplex.glossaries.*`

  * `dataplex.glossaries.create`
  * `dataplex.glossaries.delete`
  * `dataplex.glossaries.get`
  * `dataplex.glossaries.getIamPolicy`
  * `dataplex.glossaries.import`
  * `dataplex.glossaries.list`
  * `dataplex.glossaries.requestChanges`
  * `dataplex.glossaries.setIamPolicy`
  * `dataplex.glossaries.update`

`dataplex.glossaryCategories.*`

  * `dataplex.glossaryCategories.create`
  * `dataplex.glossaryCategories.delete`
  * `dataplex.glossaryCategories.get`
  * `dataplex.glossaryCategories.list`
  * `dataplex.glossaryCategories.update`

`dataplex.glossaryTerms.*`

  * `dataplex.glossaryTerms.create`
  * `dataplex.glossaryTerms.delete`
  * `dataplex.glossaryTerms.get`
  * `dataplex.glossaryTerms.list`
  * `dataplex.glossaryTerms.update`
  * `dataplex.glossaryTerms.use`

`dataplex.governanceRules.*`

  * `dataplex.governanceRules.createTagBinding`
  * `dataplex.governanceRules.deleteTagBinding`
  * `dataplex.governanceRules.listEffectiveTags`
  * `dataplex.governanceRules.listTagBindings`

`dataplex.lakeActions.list` `dataplex.lakes.*`

  * `dataplex.lakes.create`
  * `dataplex.lakes.delete`
  * `dataplex.lakes.get`
  * `dataplex.lakes.getIamPolicy`
  * `dataplex.lakes.list`
  * `dataplex.lakes.setIamPolicy`
  * `dataplex.lakes.update`

`dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.metadataFeeds.*`

  * `dataplex.metadataFeeds.create`
  * `dataplex.metadataFeeds.delete`
  * `dataplex.metadataFeeds.get`
  * `dataplex.metadataFeeds.list`
  * `dataplex.metadataFeeds.update`

`dataplex.metadataJobs.*`

  * `dataplex.metadataJobs.cancel`
  * `dataplex.metadataJobs.create`
  * `dataplex.metadataJobs.get`
  * `dataplex.metadataJobs.list`

`dataplex.operations.*`

  * `dataplex.operations.cancel`
  * `dataplex.operations.delete`
  * `dataplex.operations.get`
  * `dataplex.operations.list`

`dataplex.partitions.*`

  * `dataplex.partitions.create`
  * `dataplex.partitions.delete`
  * `dataplex.partitions.get`
  * `dataplex.partitions.list`
  * `dataplex.partitions.update`

`dataplex.tasks.*`

  * `dataplex.tasks.cancel`
  * `dataplex.tasks.create`
  * `dataplex.tasks.delete`
  * `dataplex.tasks.get`
  * `dataplex.tasks.getIamPolicy`
  * `dataplex.tasks.list`
  * `dataplex.tasks.run`
  * `dataplex.tasks.setIamPolicy`
  * `dataplex.tasks.update`

`dataplex.zoneActions.list` `dataplex.zones.*`

  * `dataplex.zones.create`
  * `dataplex.zones.delete`
  * `dataplex.zones.get`
  * `dataplex.zones.getIamPolicy`
  * `dataplex.zones.list`
  * `dataplex.zones.setIamPolicy`
  * `dataplex.zones.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex DataScan Administrator 

(`roles/dataplex.dataScanAdmin`) Full access to DataScan resources.  |  `dataplex.agentTasks.*`

  * `dataplex.agentTasks.create`
  * `dataplex.agentTasks.delete`
  * `dataplex.agentTasks.get`
  * `dataplex.agentTasks.getData`
  * `dataplex.agentTasks.getIamPolicy`
  * `dataplex.agentTasks.list`
  * `dataplex.agentTasks.run`
  * `dataplex.agentTasks.setIamPolicy`
  * `dataplex.agentTasks.update`

`dataplex.datascans.*`

  * `dataplex.datascans.cancel`
  * `dataplex.datascans.create`
  * `dataplex.datascans.delete`
  * `dataplex.datascans.get`
  * `dataplex.datascans.getData`
  * `dataplex.datascans.getIamPolicy`
  * `dataplex.datascans.list`
  * `dataplex.datascans.run`
  * `dataplex.datascans.setIamPolicy`
  * `dataplex.datascans.update`

`dataplex.operations.get` `dataplex.operations.list`  
  
#### Dataplex Editor 

(`roles/dataplex.editor`) Write access to Dataplex Universal Catalog resources, except for catalog resources like entries, entry groups, and glossaries.  |  `cloudasset.assets.analyzeIamPolicy` `dataplex.agentTasks.create` `dataplex.agentTasks.delete` `dataplex.agentTasks.get` `dataplex.agentTasks.getIamPolicy` `dataplex.agentTasks.list` `dataplex.agentTasks.run` `dataplex.agentTasks.update` `dataplex.assetActions.list` `dataplex.assets.create` `dataplex.assets.delete` `dataplex.assets.get` `dataplex.assets.getIamPolicy` `dataplex.assets.list` `dataplex.assets.update` `dataplex.content.delete` `dataplex.content.get` `dataplex.content.getIamPolicy` `dataplex.content.list` `dataplex.dataAssets.*`

  * `dataplex.dataAssets.create`
  * `dataplex.dataAssets.delete`
  * `dataplex.dataAssets.get`
  * `dataplex.dataAssets.list`
  * `dataplex.dataAssets.update`

`dataplex.dataAttributeBindings.create` `dataplex.dataAttributeBindings.delete` `dataplex.dataAttributeBindings.get` `dataplex.dataAttributeBindings.getIamPolicy` `dataplex.dataAttributeBindings.list` `dataplex.dataAttributeBindings.update` `dataplex.dataAttributes.bind` `dataplex.dataAttributes.create` `dataplex.dataAttributes.delete` `dataplex.dataAttributes.get` `dataplex.dataAttributes.getIamPolicy` `dataplex.dataAttributes.list` `dataplex.dataAttributes.update` `dataplex.dataProducts.approve` `dataplex.dataProducts.create` `dataplex.dataProducts.delete` `dataplex.dataProducts.get` `dataplex.dataProducts.getIamPolicy` `dataplex.dataProducts.list` `dataplex.dataProducts.update` `dataplex.dataTaxonomies.configureDataAccess` `dataplex.dataTaxonomies.configureResourceAccess` `dataplex.dataTaxonomies.create` `dataplex.dataTaxonomies.delete` `dataplex.dataTaxonomies.get` `dataplex.dataTaxonomies.getIamPolicy` `dataplex.dataTaxonomies.list` `dataplex.dataTaxonomies.update` `dataplex.datascans.cancel` `dataplex.datascans.create` `dataplex.datascans.delete` `dataplex.datascans.get` `dataplex.datascans.getIamPolicy` `dataplex.datascans.list` `dataplex.datascans.run` `dataplex.datascans.update` `dataplex.environments.create` `dataplex.environments.delete` `dataplex.environments.get` `dataplex.environments.getIamPolicy` `dataplex.environments.list` `dataplex.environments.update` `dataplex.lakeActions.list` `dataplex.lakes.create` `dataplex.lakes.delete` `dataplex.lakes.get` `dataplex.lakes.getIamPolicy` `dataplex.lakes.list` `dataplex.lakes.update` `dataplex.operations.*`

  * `dataplex.operations.cancel`
  * `dataplex.operations.delete`
  * `dataplex.operations.get`
  * `dataplex.operations.list`

`dataplex.tasks.cancel` `dataplex.tasks.create` `dataplex.tasks.delete` `dataplex.tasks.get` `dataplex.tasks.getIamPolicy` `dataplex.tasks.list` `dataplex.tasks.run` `dataplex.tasks.update` `dataplex.zoneActions.list` `dataplex.zones.create` `dataplex.zones.delete` `dataplex.zones.get` `dataplex.zones.getIamPolicy` `dataplex.zones.list` `dataplex.zones.update`  
  
#### Dataplex Viewer 

(`roles/dataplex.viewer`) Read access to Dataplex Universal Catalog resources, except for catalog resources like entries, entry groups, and glossaries.  |  `cloudasset.assets.analyzeIamPolicy` `dataplex.agentTasks.get` `dataplex.agentTasks.getIamPolicy` `dataplex.agentTasks.list` `dataplex.assetActions.list` `dataplex.assets.get` `dataplex.assets.getIamPolicy` `dataplex.assets.list` `dataplex.content.get` `dataplex.content.getIamPolicy` `dataplex.content.list` `dataplex.dataAssets.get` `dataplex.dataAssets.list` `dataplex.dataAttributeBindings.get` `dataplex.dataAttributeBindings.getIamPolicy` `dataplex.dataAttributeBindings.list` `dataplex.dataAttributes.get` `dataplex.dataAttributes.getIamPolicy` `dataplex.dataAttributes.list` `dataplex.dataProducts.get` `dataplex.dataProducts.getIamPolicy` `dataplex.dataProducts.list` `dataplex.dataTaxonomies.get` `dataplex.dataTaxonomies.getIamPolicy` `dataplex.dataTaxonomies.list` `dataplex.datascans.get` `dataplex.datascans.getIamPolicy` `dataplex.datascans.list` `dataplex.environments.get` `dataplex.environments.getIamPolicy` `dataplex.environments.list` `dataplex.lakeActions.list` `dataplex.lakes.get` `dataplex.lakes.getIamPolicy` `dataplex.lakes.list` `dataplex.operations.get` `dataplex.operations.list` `dataplex.tasks.get` `dataplex.tasks.getIamPolicy` `dataplex.tasks.list` `dataplex.zoneActions.list` `dataplex.zones.get` `dataplex.zones.getIamPolicy` `dataplex.zones.list`  
  
#### Dataplex Aspect Type Owner 

(`roles/dataplex.aspectTypeOwner`) Grants access to creating and managing Aspect Types. Does not give the right to create/modify Entries.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.*`

  * `dataplex.aspectTypes.create`
  * `dataplex.aspectTypes.delete`
  * `dataplex.aspectTypes.get`
  * `dataplex.aspectTypes.getIamPolicy`
  * `dataplex.aspectTypes.list`
  * `dataplex.aspectTypes.setIamPolicy`
  * `dataplex.aspectTypes.update`
  * `dataplex.aspectTypes.use`

`dataplex.dataDomains.discover` `dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Aspect Type User 

(`roles/dataplex.aspectTypeUser`) Grants access to use Aspect Types to create/modify Entries with the corresponding aspects.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.dataDomains.discover` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Binding Administrator 

(`roles/dataplex.bindingAdmin`) Full access on DataAttribute Binding resources.  |  `dataplex.dataAttributeBindings.*`

  * `dataplex.dataAttributeBindings.create`
  * `dataplex.dataAttributeBindings.delete`
  * `dataplex.dataAttributeBindings.get`
  * `dataplex.dataAttributeBindings.getIamPolicy`
  * `dataplex.dataAttributeBindings.list`
  * `dataplex.dataAttributeBindings.setIamPolicy`
  * `dataplex.dataAttributeBindings.update`

  
  
#### Dataplex Catalog Admin 

(`roles/dataplex.catalogAdmin`) Full access to catalog resources, including entries, entry groups, and glossaries.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.*`

  * `dataplex.aspectTypes.create`
  * `dataplex.aspectTypes.delete`
  * `dataplex.aspectTypes.get`
  * `dataplex.aspectTypes.getIamPolicy`
  * `dataplex.aspectTypes.list`
  * `dataplex.aspectTypes.setIamPolicy`
  * `dataplex.aspectTypes.update`
  * `dataplex.aspectTypes.use`

`dataplex.changeRequests.adminDelete` `dataplex.changeRequests.delete` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.changeRequests.use` `dataplex.dataDomains.discover` `dataplex.entries.*`

  * `dataplex.entries.create`
  * `dataplex.entries.createContext`
  * `dataplex.entries.delete`
  * `dataplex.entries.deleteContext`
  * `dataplex.entries.get`
  * `dataplex.entries.getContext`
  * `dataplex.entries.getData`
  * `dataplex.entries.link`
  * `dataplex.entries.list`
  * `dataplex.entries.listContext`
  * `dataplex.entries.update`
  * `dataplex.entries.updateContext`

`dataplex.entryGroups.*`

  * `dataplex.entryGroups.create`
  * `dataplex.entryGroups.createContextSet`
  * `dataplex.entryGroups.createTagBinding`
  * `dataplex.entryGroups.delete`
  * `dataplex.entryGroups.deleteContextSet`
  * `dataplex.entryGroups.deleteTagBinding`
  * `dataplex.entryGroups.export`
  * `dataplex.entryGroups.get`
  * `dataplex.entryGroups.getContextSet`
  * `dataplex.entryGroups.getIamPolicy`
  * `dataplex.entryGroups.import`
  * `dataplex.entryGroups.list`
  * `dataplex.entryGroups.listEffectiveTags`
  * `dataplex.entryGroups.listTagBindings`
  * `dataplex.entryGroups.requestChanges`
  * `dataplex.entryGroups.requestContextChanges`
  * `dataplex.entryGroups.setIamPolicy`
  * `dataplex.entryGroups.update`
  * `dataplex.entryGroups.updateContextSet`
  * `dataplex.entryGroups.useCertificationAspect`
  * `dataplex.entryGroups.useContactsAspect`
  * `dataplex.entryGroups.useContextAspect`
  * `dataplex.entryGroups.useContextEntry`
  * `dataplex.entryGroups.useContextEntryLink`
  * `dataplex.entryGroups.useDataProfileAspect`
  * `dataplex.entryGroups.useDataQualityRuleTemplateAspect`
  * `dataplex.entryGroups.useDataQualityRuleTemplateEntry`
  * `dataplex.entryGroups.useDataQualityScorecardAspect`
  * `dataplex.entryGroups.useDataRulesAspect`
  * `dataplex.entryGroups.useDatabaseDataPolicyAspect`
  * `dataplex.entryGroups.useDefinitionEntryLink`
  * `dataplex.entryGroups.useDescriptionsAspect`
  * `dataplex.entryGroups.useDocumentAspect`
  * `dataplex.entryGroups.useDocumentEntry`
  * `dataplex.entryGroups.useGenericAspect`
  * `dataplex.entryGroups.useGenericEntry`
  * `dataplex.entryGroups.useGraphProfileAspect`
  * `dataplex.entryGroups.useManagedConnectorTypes`
  * `dataplex.entryGroups.useMySQLConnectorTypes`
  * `dataplex.entryGroups.useOracleConnectorTypes`
  * `dataplex.entryGroups.useOverviewAspect`
  * `dataplex.entryGroups.usePostgreSQLConnectorTypes`
  * `dataplex.entryGroups.useQueriesAspect`
  * `dataplex.entryGroups.useQueryTemplateAspect`
  * `dataplex.entryGroups.useQueryTemplateEntry`
  * `dataplex.entryGroups.useReferenceEntryLink`
  * `dataplex.entryGroups.useRefreshCadenceAspect`
  * `dataplex.entryGroups.useRelatedEntryLink`
  * `dataplex.entryGroups.useSQLAccessAspect`
  * `dataplex.entryGroups.useSQLServerConnectorTypes`
  * `dataplex.entryGroups.useSQLTriggersAspect`
  * `dataplex.entryGroups.useSchemaAspect`
  * `dataplex.entryGroups.useSchemaJoinAspect`
  * `dataplex.entryGroups.useSchemaJoinEntryLink`
  * `dataplex.entryGroups.useSecondaryIndexesAspect`
  * `dataplex.entryGroups.useStorageAspect`
  * `dataplex.entryGroups.useSynonymEntryLink`
  * `dataplex.entryGroups.useUsageAspect`

`dataplex.entryLinkTypes.*`

  * `dataplex.entryLinkTypes.create`
  * `dataplex.entryLinkTypes.delete`
  * `dataplex.entryLinkTypes.get`
  * `dataplex.entryLinkTypes.getIamPolicy`
  * `dataplex.entryLinkTypes.list`
  * `dataplex.entryLinkTypes.setIamPolicy`
  * `dataplex.entryLinkTypes.update`
  * `dataplex.entryLinkTypes.use`

`dataplex.entryLinks.*`

  * `dataplex.entryLinks.create`
  * `dataplex.entryLinks.delete`
  * `dataplex.entryLinks.get`
  * `dataplex.entryLinks.reference`
  * `dataplex.entryLinks.update`

`dataplex.entryTypes.*`

  * `dataplex.entryTypes.create`
  * `dataplex.entryTypes.createTagBinding`
  * `dataplex.entryTypes.delete`
  * `dataplex.entryTypes.deleteTagBinding`
  * `dataplex.entryTypes.get`
  * `dataplex.entryTypes.getIamPolicy`
  * `dataplex.entryTypes.list`
  * `dataplex.entryTypes.listEffectiveTags`
  * `dataplex.entryTypes.listTagBindings`
  * `dataplex.entryTypes.setIamPolicy`
  * `dataplex.entryTypes.update`
  * `dataplex.entryTypes.use`

`dataplex.glossaries.*`

  * `dataplex.glossaries.create`
  * `dataplex.glossaries.delete`
  * `dataplex.glossaries.get`
  * `dataplex.glossaries.getIamPolicy`
  * `dataplex.glossaries.import`
  * `dataplex.glossaries.list`
  * `dataplex.glossaries.requestChanges`
  * `dataplex.glossaries.setIamPolicy`
  * `dataplex.glossaries.update`

`dataplex.glossaryCategories.*`

  * `dataplex.glossaryCategories.create`
  * `dataplex.glossaryCategories.delete`
  * `dataplex.glossaryCategories.get`
  * `dataplex.glossaryCategories.list`
  * `dataplex.glossaryCategories.update`

`dataplex.glossaryTerms.*`

  * `dataplex.glossaryTerms.create`
  * `dataplex.glossaryTerms.delete`
  * `dataplex.glossaryTerms.get`
  * `dataplex.glossaryTerms.list`
  * `dataplex.glossaryTerms.update`
  * `dataplex.glossaryTerms.use`

`dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Catalog Editor 

(`roles/dataplex.catalogEditor`) Write access to catalog resources, including entries, entry groups, and glossaries. Cannot set IAM policies on resources.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.create` `dataplex.aspectTypes.delete` `dataplex.aspectTypes.get` `dataplex.aspectTypes.getIamPolicy` `dataplex.aspectTypes.list` `dataplex.aspectTypes.update` `dataplex.aspectTypes.use` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.create` `dataplex.entries.delete` `dataplex.entries.get` `dataplex.entries.getData` `dataplex.entries.link` `dataplex.entries.list` `dataplex.entries.update` `dataplex.entryGroups.create` `dataplex.entryGroups.delete` `dataplex.entryGroups.get` `dataplex.entryGroups.getIamPolicy` `dataplex.entryGroups.list` `dataplex.entryGroups.listEffectiveTags` `dataplex.entryGroups.listTagBindings` `dataplex.entryGroups.update` `dataplex.entryGroups.useCertificationAspect` `dataplex.entryGroups.useContactsAspect` `dataplex.entryGroups.useContextAspect` `dataplex.entryGroups.useContextEntry` `dataplex.entryGroups.useContextEntryLink` `dataplex.entryGroups.useDataProfileAspect` `dataplex.entryGroups.useDataQualityRuleTemplateAspect` `dataplex.entryGroups.useDataQualityRuleTemplateEntry` `dataplex.entryGroups.useDataQualityScorecardAspect` `dataplex.entryGroups.useDataRulesAspect` `dataplex.entryGroups.useDatabaseDataPolicyAspect` `dataplex.entryGroups.useDefinitionEntryLink` `dataplex.entryGroups.useDescriptionsAspect` `dataplex.entryGroups.useDocumentAspect` `dataplex.entryGroups.useDocumentEntry` `dataplex.entryGroups.useGenericAspect` `dataplex.entryGroups.useGenericEntry` `dataplex.entryGroups.useGraphProfileAspect` `dataplex.entryGroups.useManagedConnectorTypes` `dataplex.entryGroups.useMySQLConnectorTypes` `dataplex.entryGroups.useOracleConnectorTypes` `dataplex.entryGroups.useOverviewAspect` `dataplex.entryGroups.usePostgreSQLConnectorTypes` `dataplex.entryGroups.useQueriesAspect` `dataplex.entryGroups.useQueryTemplateAspect` `dataplex.entryGroups.useQueryTemplateEntry` `dataplex.entryGroups.useReferenceEntryLink` `dataplex.entryGroups.useRefreshCadenceAspect` `dataplex.entryGroups.useRelatedEntryLink` `dataplex.entryGroups.useSQLAccessAspect` `dataplex.entryGroups.useSQLServerConnectorTypes` `dataplex.entryGroups.useSQLTriggersAspect` `dataplex.entryGroups.useSchemaAspect` `dataplex.entryGroups.useSchemaJoinAspect` `dataplex.entryGroups.useSchemaJoinEntryLink` `dataplex.entryGroups.useSecondaryIndexesAspect` `dataplex.entryGroups.useStorageAspect` `dataplex.entryGroups.useSynonymEntryLink` `dataplex.entryGroups.useUsageAspect` `dataplex.entryLinkTypes.create` `dataplex.entryLinkTypes.delete` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.getIamPolicy` `dataplex.entryLinkTypes.list` `dataplex.entryLinkTypes.update` `dataplex.entryLinkTypes.use` `dataplex.entryLinks.create` `dataplex.entryLinks.delete` `dataplex.entryLinks.get` `dataplex.entryLinks.update` `dataplex.entryTypes.create` `dataplex.entryTypes.delete` `dataplex.entryTypes.get` `dataplex.entryTypes.getIamPolicy` `dataplex.entryTypes.list` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.entryTypes.update` `dataplex.entryTypes.use` `dataplex.glossaries.create` `dataplex.glossaries.delete` `dataplex.glossaries.get` `dataplex.glossaries.getIamPolicy` `dataplex.glossaries.list` `dataplex.glossaries.update` `dataplex.glossaryCategories.*`

  * `dataplex.glossaryCategories.create`
  * `dataplex.glossaryCategories.delete`
  * `dataplex.glossaryCategories.get`
  * `dataplex.glossaryCategories.list`
  * `dataplex.glossaryCategories.update`

`dataplex.glossaryTerms.*`

  * `dataplex.glossaryTerms.create`
  * `dataplex.glossaryTerms.delete`
  * `dataplex.glossaryTerms.get`
  * `dataplex.glossaryTerms.list`
  * `dataplex.glossaryTerms.update`
  * `dataplex.glossaryTerms.use`

`dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Catalog Viewer 

(`roles/dataplex.catalogViewer`) Read access to catalog resources, including entries, entry groups, and glossaries. Can view IAM policies on catalog resources.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.getIamPolicy` `dataplex.aspectTypes.list` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.get` `dataplex.entries.list` `dataplex.entryGroups.get` `dataplex.entryGroups.getIamPolicy` `dataplex.entryGroups.list` `dataplex.entryGroups.listEffectiveTags` `dataplex.entryGroups.listTagBindings` `dataplex.entryGroups.requestChanges` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.getIamPolicy` `dataplex.entryLinkTypes.list` `dataplex.entryLinks.get` `dataplex.entryTypes.get` `dataplex.entryTypes.getIamPolicy` `dataplex.entryTypes.list` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.glossaries.get` `dataplex.glossaries.getIamPolicy` `dataplex.glossaries.list` `dataplex.glossaries.requestChanges` `dataplex.glossaryCategories.get` `dataplex.glossaryCategories.list` `dataplex.glossaryTerms.get` `dataplex.glossaryTerms.list` `dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Change Request Owner Beta

(`roles/dataplex.changeRequestOwner`) Grants Change Request creator necessary permissions on a created ChangeRequest instance.  |  `dataplex.changeRequests.delete` `dataplex.changeRequests.get` `dataplex.changeRequests.update`  
  
#### Dataplex Data Domain Admin Beta

(`roles/dataplex.dataDomainAdmin`) Allows full management of the Data Domain and its bindings.  |  `dataplex.dataDomainBindings.*`

  * `dataplex.dataDomainBindings.create`
  * `dataplex.dataDomainBindings.delete`
  * `dataplex.dataDomainBindings.get`
  * `dataplex.dataDomainBindings.list`

`dataplex.dataDomains.create` `dataplex.dataDomains.delete` `dataplex.dataDomains.discover` `dataplex.dataDomains.get` `dataplex.dataDomains.getIamPolicy` `dataplex.dataDomains.list` `dataplex.dataDomains.lookupEntry` `dataplex.dataDomains.setIamPolicy` `dataplex.dataDomains.update` `dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Domain Configuration Editor Beta

(`roles/dataplex.dataDomainEditor`) Allows updating the Data Domain as well as full management of its bindings.  |  `dataplex.dataDomainBindings.*`

  * `dataplex.dataDomainBindings.create`
  * `dataplex.dataDomainBindings.delete`
  * `dataplex.dataDomainBindings.get`
  * `dataplex.dataDomainBindings.list`

`dataplex.dataDomains.discover` `dataplex.dataDomains.get` `dataplex.dataDomains.getIamPolicy` `dataplex.dataDomains.list` `dataplex.dataDomains.lookupEntry` `dataplex.dataDomains.update` `dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Domain Entry Reader Beta

(`roles/dataplex.dataDomainEntryReader`) Allows discovering and viewing the Data Domain, its subdomains, and metadata of all its resources.  |  `dataplex.dataDomains.discover` `dataplex.dataDomains.get` `dataplex.dataDomains.list` `dataplex.dataDomains.lookupEntry`  
  
#### Dataplex Data Domain Configuration Viewer Beta

(`roles/dataplex.dataDomainViewer`) Allows viewing the configuration of the Data Domain and its bindings.  |  `dataplex.dataDomainBindings.get` `dataplex.dataDomainBindings.list` `dataplex.dataDomains.discover` `dataplex.dataDomains.get` `dataplex.dataDomains.getIamPolicy` `dataplex.dataDomains.list` `dataplex.dataDomains.lookupEntry` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Owner 

(`roles/dataplex.dataOwner`) Owner access to data. To be granted to Dataplex Universal Catalog resources Lake, Zone or Asset only.  |  `dataplex.assets.ownData` `dataplex.assets.readData` `dataplex.assets.writeData`  
  
#### Dataplex Data Products Admin 

(`roles/dataplex.dataProductsAdmin`) Full access to Data Products.  |  `dataplex.dataAssets.*`

  * `dataplex.dataAssets.create`
  * `dataplex.dataAssets.delete`
  * `dataplex.dataAssets.get`
  * `dataplex.dataAssets.list`
  * `dataplex.dataAssets.update`

`dataplex.dataProducts.*`

  * `dataplex.dataProducts.approve`
  * `dataplex.dataProducts.create`
  * `dataplex.dataProducts.delete`
  * `dataplex.dataProducts.get`
  * `dataplex.dataProducts.getIamPolicy`
  * `dataplex.dataProducts.list`
  * `dataplex.dataProducts.setIamPolicy`
  * `dataplex.dataProducts.update`

`dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Products Consumer 

(`roles/dataplex.dataProductsConsumer`) Restricted read access, intended for consumers of Data Products.  |  `dataplex.dataAssets.get` `dataplex.dataAssets.list` `dataplex.dataProducts.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Products Editor 

(`roles/dataplex.dataProductsEditor`) Write access to Data Products.  |  `dataplex.dataAssets.*`

  * `dataplex.dataAssets.create`
  * `dataplex.dataAssets.delete`
  * `dataplex.dataAssets.get`
  * `dataplex.dataAssets.list`
  * `dataplex.dataAssets.update`

`dataplex.dataProducts.approve` `dataplex.dataProducts.create` `dataplex.dataProducts.delete` `dataplex.dataProducts.get` `dataplex.dataProducts.getIamPolicy` `dataplex.dataProducts.list` `dataplex.dataProducts.update` `dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Products Viewer 

(`roles/dataplex.dataProductsViewer`) Read access to Data Products.  |  `dataplex.dataAssets.get` `dataplex.dataAssets.list` `dataplex.dataProducts.get` `dataplex.dataProducts.getIamPolicy` `dataplex.dataProducts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Data Reader 

(`roles/dataplex.dataReader`) Read only access to data. To be granted to Dataplex Universal Catalog resources Lake, Zone or Asset only.  |  `dataplex.assets.readData`  
  
#### Dataplex DataScan Creator 

(`roles/dataplex.dataScanCreator`) Access to create new DataScan resources.  |  `dataplex.agentTasks.create` `dataplex.agentTasks.get` `dataplex.agentTasks.list` `dataplex.datascans.create` `dataplex.datascans.get` `dataplex.datascans.list` `dataplex.operations.get`  
  
#### Dataplex DataScan DataViewer 

(`roles/dataplex.dataScanDataViewer`) Read access to DataScan resources, including the results.  |  `dataplex.agentTasks.get` `dataplex.agentTasks.getData` `dataplex.agentTasks.getIamPolicy` `dataplex.agentTasks.list` `dataplex.datascans.get` `dataplex.datascans.getData` `dataplex.datascans.getIamPolicy` `dataplex.datascans.list`  
  
#### Dataplex DataScan Editor 

(`roles/dataplex.dataScanEditor`) Write access to DataScan resources.  |  `dataplex.agentTasks.create` `dataplex.agentTasks.delete` `dataplex.agentTasks.get` `dataplex.agentTasks.getData` `dataplex.agentTasks.getIamPolicy` `dataplex.agentTasks.list` `dataplex.agentTasks.run` `dataplex.agentTasks.update` `dataplex.datascans.cancel` `dataplex.datascans.create` `dataplex.datascans.delete` `dataplex.datascans.get` `dataplex.datascans.getData` `dataplex.datascans.getIamPolicy` `dataplex.datascans.list` `dataplex.datascans.run` `dataplex.datascans.update` `dataplex.operations.get` `dataplex.operations.list`  
  
#### Dataplex DataScan Viewer 

(`roles/dataplex.dataScanViewer`) Read access to DataScan resources, excluding the results.  |  `dataplex.agentTasks.get` `dataplex.agentTasks.getIamPolicy` `dataplex.agentTasks.list` `dataplex.datascans.get` `dataplex.datascans.getIamPolicy` `dataplex.datascans.list`  
  
#### Dataplex Data Writer 

(`roles/dataplex.dataWriter`) Write access to data. To be granted to Dataplex Universal Catalog resources Lake, Zone or Asset only.  |  `dataplex.assets.writeData`  
  
#### Dataplex Developer 

(`roles/dataplex.developer`) Allows running data analytics workloads in a lake.  |  `dataplex.content.*`

  * `dataplex.content.create`
  * `dataplex.content.delete`
  * `dataplex.content.get`
  * `dataplex.content.getIamPolicy`
  * `dataplex.content.list`
  * `dataplex.content.setIamPolicy`
  * `dataplex.content.update`

`dataplex.environments.execute` `dataplex.environments.get` `dataplex.environments.list` `dataplex.tasks.cancel` `dataplex.tasks.create` `dataplex.tasks.delete` `dataplex.tasks.get` `dataplex.tasks.list` `dataplex.tasks.run` `dataplex.tasks.update`  
  
#### Dataplex Encryption Admin 

(`roles/dataplex.encryptionAdmin`) Gives user permissions to manage encryption configurations.  |  `dataplex.encryptionConfig.*`

  * `dataplex.encryptionConfig.create`
  * `dataplex.encryptionConfig.delete`
  * `dataplex.encryptionConfig.get`
  * `dataplex.encryptionConfig.list`
  * `dataplex.encryptionConfig.update`

`dataplex.operations.get` `dataplex.operations.list`  
  
#### Dataplex Entry Group Exporter 

(`roles/dataplex.entryGroupExporter`) Grants access to export this entry group for Metadata Job processing.  |  `dataplex.entryGroups.export` `dataplex.entryGroups.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Group Importer 

(`roles/dataplex.entryGroupImporter`) Grants access to import this entry group for Metadata Job processing.  |  `dataplex.entryGroups.get` `dataplex.entryGroups.import` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Group Owner 

(`roles/dataplex.entryGroupOwner`) Owns Entry Groups and Entries inside of them.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.*`

  * `dataplex.entries.create`
  * `dataplex.entries.createContext`
  * `dataplex.entries.delete`
  * `dataplex.entries.deleteContext`
  * `dataplex.entries.get`
  * `dataplex.entries.getContext`
  * `dataplex.entries.getData`
  * `dataplex.entries.link`
  * `dataplex.entries.list`
  * `dataplex.entries.listContext`
  * `dataplex.entries.update`
  * `dataplex.entries.updateContext`

`dataplex.entryGroups.*`

  * `dataplex.entryGroups.create`
  * `dataplex.entryGroups.createContextSet`
  * `dataplex.entryGroups.createTagBinding`
  * `dataplex.entryGroups.delete`
  * `dataplex.entryGroups.deleteContextSet`
  * `dataplex.entryGroups.deleteTagBinding`
  * `dataplex.entryGroups.export`
  * `dataplex.entryGroups.get`
  * `dataplex.entryGroups.getContextSet`
  * `dataplex.entryGroups.getIamPolicy`
  * `dataplex.entryGroups.import`
  * `dataplex.entryGroups.list`
  * `dataplex.entryGroups.listEffectiveTags`
  * `dataplex.entryGroups.listTagBindings`
  * `dataplex.entryGroups.requestChanges`
  * `dataplex.entryGroups.requestContextChanges`
  * `dataplex.entryGroups.setIamPolicy`
  * `dataplex.entryGroups.update`
  * `dataplex.entryGroups.updateContextSet`
  * `dataplex.entryGroups.useCertificationAspect`
  * `dataplex.entryGroups.useContactsAspect`
  * `dataplex.entryGroups.useContextAspect`
  * `dataplex.entryGroups.useContextEntry`
  * `dataplex.entryGroups.useContextEntryLink`
  * `dataplex.entryGroups.useDataProfileAspect`
  * `dataplex.entryGroups.useDataQualityRuleTemplateAspect`
  * `dataplex.entryGroups.useDataQualityRuleTemplateEntry`
  * `dataplex.entryGroups.useDataQualityScorecardAspect`
  * `dataplex.entryGroups.useDataRulesAspect`
  * `dataplex.entryGroups.useDatabaseDataPolicyAspect`
  * `dataplex.entryGroups.useDefinitionEntryLink`
  * `dataplex.entryGroups.useDescriptionsAspect`
  * `dataplex.entryGroups.useDocumentAspect`
  * `dataplex.entryGroups.useDocumentEntry`
  * `dataplex.entryGroups.useGenericAspect`
  * `dataplex.entryGroups.useGenericEntry`
  * `dataplex.entryGroups.useGraphProfileAspect`
  * `dataplex.entryGroups.useManagedConnectorTypes`
  * `dataplex.entryGroups.useMySQLConnectorTypes`
  * `dataplex.entryGroups.useOracleConnectorTypes`
  * `dataplex.entryGroups.useOverviewAspect`
  * `dataplex.entryGroups.usePostgreSQLConnectorTypes`
  * `dataplex.entryGroups.useQueriesAspect`
  * `dataplex.entryGroups.useQueryTemplateAspect`
  * `dataplex.entryGroups.useQueryTemplateEntry`
  * `dataplex.entryGroups.useReferenceEntryLink`
  * `dataplex.entryGroups.useRefreshCadenceAspect`
  * `dataplex.entryGroups.useRelatedEntryLink`
  * `dataplex.entryGroups.useSQLAccessAspect`
  * `dataplex.entryGroups.useSQLServerConnectorTypes`
  * `dataplex.entryGroups.useSQLTriggersAspect`
  * `dataplex.entryGroups.useSchemaAspect`
  * `dataplex.entryGroups.useSchemaJoinAspect`
  * `dataplex.entryGroups.useSchemaJoinEntryLink`
  * `dataplex.entryGroups.useSecondaryIndexesAspect`
  * `dataplex.entryGroups.useStorageAspect`
  * `dataplex.entryGroups.useSynonymEntryLink`
  * `dataplex.entryGroups.useUsageAspect`

`dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.list` `dataplex.entryLinkTypes.use` `dataplex.entryLinks.*`

  * `dataplex.entryLinks.create`
  * `dataplex.entryLinks.delete`
  * `dataplex.entryLinks.get`
  * `dataplex.entryLinks.reference`
  * `dataplex.entryLinks.update`

`dataplex.entryTypes.get` `dataplex.entryTypes.list` `dataplex.entryTypes.use` `dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Link Type Owner 

(`roles/dataplex.entryLinkTypeOwner`) Grants access to creating and managing Entry Link Types. Does not give the right to create/modify Entry Links.  |  `dataplex.dataDomains.discover` `dataplex.entryLinkTypes.*`

  * `dataplex.entryLinkTypes.create`
  * `dataplex.entryLinkTypes.delete`
  * `dataplex.entryLinkTypes.get`
  * `dataplex.entryLinkTypes.getIamPolicy`
  * `dataplex.entryLinkTypes.list`
  * `dataplex.entryLinkTypes.setIamPolicy`
  * `dataplex.entryLinkTypes.update`
  * `dataplex.entryLinkTypes.use`

`dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Link Type User 

(`roles/dataplex.entryLinkTypeUser`) Grants access to use Entry Link Types to create EntryLinks of those types.  |  `dataplex.dataDomains.discover` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.list` `dataplex.entryLinkTypes.use` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry and EntryLink Owner 

(`roles/dataplex.entryOwner`) Owns Metadata Entries and EntryLinks.  |  `datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.*`

  * `dataplex.entries.create`
  * `dataplex.entries.createContext`
  * `dataplex.entries.delete`
  * `dataplex.entries.deleteContext`
  * `dataplex.entries.get`
  * `dataplex.entries.getContext`
  * `dataplex.entries.getData`
  * `dataplex.entries.link`
  * `dataplex.entries.list`
  * `dataplex.entries.listContext`
  * `dataplex.entries.update`
  * `dataplex.entries.updateContext`

`dataplex.entryGroups.get` `dataplex.entryGroups.useCertificationAspect` `dataplex.entryGroups.useContactsAspect` `dataplex.entryGroups.useContextAspect` `dataplex.entryGroups.useContextEntry` `dataplex.entryGroups.useContextEntryLink` `dataplex.entryGroups.useDataProfileAspect` `dataplex.entryGroups.useDataQualityRuleTemplateAspect` `dataplex.entryGroups.useDataQualityRuleTemplateEntry` `dataplex.entryGroups.useDataQualityScorecardAspect` `dataplex.entryGroups.useDataRulesAspect` `dataplex.entryGroups.useDatabaseDataPolicyAspect` `dataplex.entryGroups.useDefinitionEntryLink` `dataplex.entryGroups.useDescriptionsAspect` `dataplex.entryGroups.useDocumentAspect` `dataplex.entryGroups.useDocumentEntry` `dataplex.entryGroups.useGenericAspect` `dataplex.entryGroups.useGenericEntry` `dataplex.entryGroups.useGraphProfileAspect` `dataplex.entryGroups.useManagedConnectorTypes` `dataplex.entryGroups.useMySQLConnectorTypes` `dataplex.entryGroups.useOracleConnectorTypes` `dataplex.entryGroups.useOverviewAspect` `dataplex.entryGroups.usePostgreSQLConnectorTypes` `dataplex.entryGroups.useQueriesAspect` `dataplex.entryGroups.useQueryTemplateAspect` `dataplex.entryGroups.useQueryTemplateEntry` `dataplex.entryGroups.useReferenceEntryLink` `dataplex.entryGroups.useRefreshCadenceAspect` `dataplex.entryGroups.useRelatedEntryLink` `dataplex.entryGroups.useSQLAccessAspect` `dataplex.entryGroups.useSQLServerConnectorTypes` `dataplex.entryGroups.useSQLTriggersAspect` `dataplex.entryGroups.useSchemaAspect` `dataplex.entryGroups.useSchemaJoinAspect` `dataplex.entryGroups.useSchemaJoinEntryLink` `dataplex.entryGroups.useSecondaryIndexesAspect` `dataplex.entryGroups.useStorageAspect` `dataplex.entryGroups.useSynonymEntryLink` `dataplex.entryGroups.useUsageAspect` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.list` `dataplex.entryLinkTypes.use` `dataplex.entryLinks.*`

  * `dataplex.entryLinks.create`
  * `dataplex.entryLinks.delete`
  * `dataplex.entryLinks.get`
  * `dataplex.entryLinks.reference`
  * `dataplex.entryLinks.update`

`dataplex.entryTypes.get` `dataplex.entryTypes.list` `dataplex.entryTypes.use` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Type Owner 

(`roles/dataplex.entryTypeOwner`) Grants access to creating and managing Entry Types. Does not give the right to create/modify Entries.  |  `datacatalog.migrationConfig.get` `dataplex.dataDomains.discover` `dataplex.entryTypes.*`

  * `dataplex.entryTypes.create`
  * `dataplex.entryTypes.createTagBinding`
  * `dataplex.entryTypes.delete`
  * `dataplex.entryTypes.deleteTagBinding`
  * `dataplex.entryTypes.get`
  * `dataplex.entryTypes.getIamPolicy`
  * `dataplex.entryTypes.list`
  * `dataplex.entryTypes.listEffectiveTags`
  * `dataplex.entryTypes.listTagBindings`
  * `dataplex.entryTypes.setIamPolicy`
  * `dataplex.entryTypes.update`
  * `dataplex.entryTypes.use`

`dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Entry Type User 

(`roles/dataplex.entryTypeUser`) Grants access to use Entry Types to create/modify Entries of those types.  |  `datacatalog.migrationConfig.get` `dataplex.dataDomains.discover` `dataplex.entryTypes.get` `dataplex.entryTypes.list` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.entryTypes.use` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Feed Owner 

(`roles/dataplex.metadataFeedOwner`) Grants access to creating and managing Metadata Feeds. Does not give the right to create/modify Entry Groups.  |  `dataplex.metadataFeeds.*`

  * `dataplex.metadataFeeds.create`
  * `dataplex.metadataFeeds.delete`
  * `dataplex.metadataFeeds.get`
  * `dataplex.metadataFeeds.list`
  * `dataplex.metadataFeeds.update`

`dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Feed Viewer 

(`roles/dataplex.metadataFeedViewer`) Read access to Metadata Feed resources.  |  `dataplex.metadataFeeds.get` `dataplex.metadataFeeds.list` `dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Job Owner 

(`roles/dataplex.metadataJobOwner`) Grants access to creating and managing Metadata Jobs. Does not give the right to create/modify Entry Groups.  |  `dataplex.metadataJobs.*`

  * `dataplex.metadataJobs.cancel`
  * `dataplex.metadataJobs.create`
  * `dataplex.metadataJobs.get`
  * `dataplex.metadataJobs.list`

`dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Job Viewer 

(`roles/dataplex.metadataJobViewer`) Read access to Metadata Job resources.  |  `dataplex.metadataJobs.get` `dataplex.metadataJobs.list` `dataplex.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Reader 

(`roles/dataplex.metadataReader`) Read only access to metadata within table and fileset entities and partitions.  |  `dataplex.assets.get` `dataplex.assets.list` `dataplex.entities.get` `dataplex.entities.list` `dataplex.partitions.get` `dataplex.partitions.list` `dataplex.zones.get` `dataplex.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Metadata Writer 

(`roles/dataplex.metadataWriter`) Write and read access to metadata within table and fileset entities and partitions.  |  `dataplex.assets.get` `dataplex.assets.list` `dataplex.entities.*`

  * `dataplex.entities.create`
  * `dataplex.entities.delete`
  * `dataplex.entities.get`
  * `dataplex.entities.list`
  * `dataplex.entities.update`

`dataplex.partitions.*`

  * `dataplex.partitions.create`
  * `dataplex.partitions.delete`
  * `dataplex.partitions.get`
  * `dataplex.partitions.list`
  * `dataplex.partitions.update`

`dataplex.zones.get` `dataplex.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataplex Security Administrator 

(`roles/dataplex.securityAdmin`) Permissions configure ResourceAccess and DataAccess Specs on Data Attributes.  |  `dataplex.dataTaxonomies.configureDataAccess` `dataplex.dataTaxonomies.configureResourceAccess`  
  
#### Dataplex Storage Data Owner 

(`roles/dataplex.storageDataOwner`) Owner access to data. Should not be used directly. This role is granted by Dataplex to managed resources like Cloud Storage buckets, BigQuery datasets etc.  |  `bigquery.datasets.get` `bigquery.models.create` `bigquery.models.delete` `bigquery.models.export` `bigquery.models.getData` `bigquery.models.getMetadata` `bigquery.models.list` `bigquery.models.updateData` `bigquery.models.updateMetadata` `bigquery.routines.create` `bigquery.routines.delete` `bigquery.routines.get` `bigquery.routines.list` `bigquery.routines.update` `bigquery.tables.create` `bigquery.tables.createSnapshot` `bigquery.tables.delete` `bigquery.tables.deleteSnapshot` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.restoreSnapshot` `bigquery.tables.update` `bigquery.tables.updateData` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
#### Dataplex Storage Data Reader 

(`roles/dataplex.storageDataReader`) Read only access to data. Should not be used directly. This role is granted by Dataplex to managed resources like Cloud Storage buckets, BigQuery datasets etc.  |  `bigquery.datasets.get` `bigquery.models.export` `bigquery.models.getData` `bigquery.models.getMetadata` `bigquery.models.list` `bigquery.routines.get` `bigquery.routines.list` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `storage.buckets.get` `storage.objects.get` `storage.objects.list`  
  
#### Dataplex Storage Data Writer 

(`roles/dataplex.storageDataWriter`) Write access to data. Should not be used directly. This role is granted by Dataplex to managed resources like Cloud Storage buckets, BigQuery datasets etc.  |  `bigquery.tables.updateData` `storage.objects.create` `storage.objects.delete` `storage.objects.update`  
  
#### Dataplex Taxonomy Administrator 

(`roles/dataplex.taxonomyAdmin`) Full access to DataTaxonomy, DataAttribute resources.  |  `dataplex.dataAttributes.*`

  * `dataplex.dataAttributes.bind`
  * `dataplex.dataAttributes.create`
  * `dataplex.dataAttributes.delete`
  * `dataplex.dataAttributes.get`
  * `dataplex.dataAttributes.getIamPolicy`
  * `dataplex.dataAttributes.list`
  * `dataplex.dataAttributes.setIamPolicy`
  * `dataplex.dataAttributes.update`

`dataplex.dataTaxonomies.create` `dataplex.dataTaxonomies.delete` `dataplex.dataTaxonomies.get` `dataplex.dataTaxonomies.getIamPolicy` `dataplex.dataTaxonomies.list` `dataplex.dataTaxonomies.setIamPolicy` `dataplex.dataTaxonomies.update`  
  
#### Dataplex Taxonomy Viewer 

(`roles/dataplex.taxonomyViewer`) Read access on DataTaxonomy, DataAttribute resources.  |  `dataplex.dataAttributes.get` `dataplex.dataAttributes.getIamPolicy` `dataplex.dataAttributes.list` `dataplex.dataTaxonomies.get` `dataplex.dataTaxonomies.getIamPolicy` `dataplex.dataTaxonomies.list`  
  
#### Dataplex Workflow Admin Beta

(`roles/dataplex.workflowAdmin`) Full access to Change Requests in Approval Workflows.  |  `dataplex.changeRequests.adminDelete` `dataplex.changeRequests.delete` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.changeRequests.use`  
  
#### Dataplex Workflow Approver Beta

(`roles/dataplex.workflowApprover`) Access to approve, reject, or revoke Change Requests in Approval Workflows.  |  `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.changeRequests.use`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Dataplex Discovery BigLake Publishing Service Agent 

(`roles/dataplex.discoveryBigLakePublishingServiceAgent`) Gives the Dataplex Discovery Service Agent permissions to use bigquery connection.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.connections.delegate` `bigquery.connections.use`  
  
#### Dataplex Discovery Publishing Service Agent 

(`roles/dataplex.discoveryPublishingServiceAgent`) Gives the Dataplex Discovery Service Agent dataset create and get permissions.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get`  
  
#### Dataplex Discovery Service Agent 

(`roles/dataplex.discoveryServiceAgent`) Gives the Dataplex Discovery Service Agent bucket read permissions.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.buckets.get` `storage.objects.get` `storage.objects.list`  
  
#### Cloud Dataplex Service Agent 

(`roles/dataplex.serviceAgent`) Gives the Dataplex service account access to project resources. This access will be used in data discovery, data management and data workload management.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `biglake.catalogs.get` `biglake.namespaces.get` `biglake.tables.get` `biglake.tables.getData` `biglake.tables.list` `bigquery.bireservations.*`

  * `bigquery.bireservations.get`
  * `bigquery.bireservations.update`

`bigquery.capacityCommitments.*`

  * `bigquery.capacityCommitments.create`
  * `bigquery.capacityCommitments.delete`
  * `bigquery.capacityCommitments.get`
  * `bigquery.capacityCommitments.list`
  * `bigquery.capacityCommitments.update`

`bigquery.config.*`

  * `bigquery.config.get`
  * `bigquery.config.update`

`bigquery.connections.*`

  * `bigquery.connections.create`
  * `bigquery.connections.delegate`
  * `bigquery.connections.delete`
  * `bigquery.connections.get`
  * `bigquery.connections.getIamPolicy`
  * `bigquery.connections.list`
  * `bigquery.connections.setIamPolicy`
  * `bigquery.connections.update`
  * `bigquery.connections.updateTag`
  * `bigquery.connections.use`

`bigquery.dataPolicies.attach` `bigquery.dataPolicies.create` `bigquery.dataPolicies.delete` `bigquery.dataPolicies.get` `bigquery.dataPolicies.getIamPolicy` `bigquery.dataPolicies.list` `bigquery.dataPolicies.setIamPolicy` `bigquery.dataPolicies.update` `bigquery.datasets.*`

  * `bigquery.datasets.create`
  * `bigquery.datasets.createTagBinding`
  * `bigquery.datasets.delete`
  * `bigquery.datasets.deleteTagBinding`
  * `bigquery.datasets.get`
  * `bigquery.datasets.getIamPolicy`
  * `bigquery.datasets.link`
  * `bigquery.datasets.listEffectiveTags`
  * `bigquery.datasets.listSharedDatasetUsage`
  * `bigquery.datasets.listTagBindings`
  * `bigquery.datasets.setIamPolicy`
  * `bigquery.datasets.update`
  * `bigquery.datasets.updateTag`

`bigquery.jobs.*`

  * `bigquery.jobs.create`
  * `bigquery.jobs.createGlobalQuery`
  * `bigquery.jobs.delete`
  * `bigquery.jobs.get`
  * `bigquery.jobs.list`
  * `bigquery.jobs.listAll`
  * `bigquery.jobs.listExecutionMetadata`
  * `bigquery.jobs.update`

`bigquery.models.*`

  * `bigquery.models.create`
  * `bigquery.models.delete`
  * `bigquery.models.export`
  * `bigquery.models.getData`
  * `bigquery.models.getMetadata`
  * `bigquery.models.list`
  * `bigquery.models.updateData`
  * `bigquery.models.updateMetadata`
  * `bigquery.models.updateTag`

`bigquery.objectRefs.*`

  * `bigquery.objectRefs.read`
  * `bigquery.objectRefs.write`

`bigquery.propertyGraphs.*`

  * `bigquery.propertyGraphs.create`
  * `bigquery.propertyGraphs.delete`
  * `bigquery.propertyGraphs.get`
  * `bigquery.propertyGraphs.list`
  * `bigquery.propertyGraphs.update`

`bigquery.readsessions.*`

  * `bigquery.readsessions.create`
  * `bigquery.readsessions.getData`
  * `bigquery.readsessions.update`

`bigquery.reservationAssignments.*`

  * `bigquery.reservationAssignments.create`
  * `bigquery.reservationAssignments.delete`
  * `bigquery.reservationAssignments.list`
  * `bigquery.reservationAssignments.search`

`bigquery.reservationGroups.*`

  * `bigquery.reservationGroups.create`
  * `bigquery.reservationGroups.delete`
  * `bigquery.reservationGroups.get`
  * `bigquery.reservationGroups.list`
  * `bigquery.reservationGroups.update`

`bigquery.reservations.*`

  * `bigquery.reservations.create`
  * `bigquery.reservations.delete`
  * `bigquery.reservations.get`
  * `bigquery.reservations.getIamPolicy`
  * `bigquery.reservations.list`
  * `bigquery.reservations.listFailoverDatasets`
  * `bigquery.reservations.setIamPolicy`
  * `bigquery.reservations.update`
  * `bigquery.reservations.use`

`bigquery.routines.*`

  * `bigquery.routines.create`
  * `bigquery.routines.delete`
  * `bigquery.routines.get`
  * `bigquery.routines.list`
  * `bigquery.routines.update`
  * `bigquery.routines.updateTag`

`bigquery.rowAccessPolicies.create` `bigquery.rowAccessPolicies.delete` `bigquery.rowAccessPolicies.get` `bigquery.rowAccessPolicies.getIamPolicy` `bigquery.rowAccessPolicies.list` `bigquery.rowAccessPolicies.overrideTimeTravelRestrictions` `bigquery.rowAccessPolicies.setIamPolicy` `bigquery.rowAccessPolicies.update` `bigquery.savedqueries.*`

  * `bigquery.savedqueries.create`
  * `bigquery.savedqueries.delete`
  * `bigquery.savedqueries.get`
  * `bigquery.savedqueries.list`
  * `bigquery.savedqueries.update`

`bigquery.tables.*`

  * `bigquery.tables.create`
  * `bigquery.tables.createIndex`
  * `bigquery.tables.createSnapshot`
  * `bigquery.tables.createTagBinding`
  * `bigquery.tables.delete`
  * `bigquery.tables.deleteIndex`
  * `bigquery.tables.deleteSnapshot`
  * `bigquery.tables.deleteTagBinding`
  * `bigquery.tables.export`
  * `bigquery.tables.get`
  * `bigquery.tables.getData`
  * `bigquery.tables.getIamPolicy`
  * `bigquery.tables.list`
  * `bigquery.tables.listEffectiveTags`
  * `bigquery.tables.listTagBindings`
  * `bigquery.tables.replicateData`
  * `bigquery.tables.restoreSnapshot`
  * `bigquery.tables.setCategory`
  * `bigquery.tables.setColumnDataPolicy`
  * `bigquery.tables.setIamPolicy`
  * `bigquery.tables.update`
  * `bigquery.tables.updateData`
  * `bigquery.tables.updateIndex`
  * `bigquery.tables.updateTag`

`bigquery.transfers.*`

  * `bigquery.transfers.get`
  * `bigquery.transfers.update`

`bigquerymigration.translation.translate` `cloudaicompanion.instances.completeTask` `datacatalog.catalogs.searchAll` `datacatalog.categories.getIamPolicy` `datacatalog.categories.setIamPolicy` `datacatalog.entries.get` `datacatalog.taxonomies.create` `datacatalog.taxonomies.delete` `datacatalog.taxonomies.get` `datacatalog.taxonomies.list` `datacatalog.taxonomies.update` `dataform.*`

  * `dataform.commentThreads.create`
  * `dataform.commentThreads.delete`
  * `dataform.commentThreads.get`
  * `dataform.commentThreads.list`
  * `dataform.commentThreads.update`
  * `dataform.comments.create`
  * `dataform.comments.delete`
  * `dataform.comments.get`
  * `dataform.comments.list`
  * `dataform.comments.update`
  * `dataform.compilationResults.create`
  * `dataform.compilationResults.get`
  * `dataform.compilationResults.list`
  * `dataform.compilationResults.query`
  * `dataform.config.get`
  * `dataform.config.update`
  * `dataform.folders.addContents`
  * `dataform.folders.create`
  * `dataform.folders.delete`
  * `dataform.folders.deleteTree`
  * `dataform.folders.get`
  * `dataform.folders.getIamPolicy`
  * `dataform.folders.move`
  * `dataform.folders.queryContents`
  * `dataform.folders.setIamPolicy`
  * `dataform.folders.update`
  * `dataform.locations.get`
  * `dataform.locations.list`
  * `dataform.operations.cancel`
  * `dataform.operations.delete`
  * `dataform.operations.get`
  * `dataform.operations.list`
  * `dataform.releaseConfigs.create`
  * `dataform.releaseConfigs.delete`
  * `dataform.releaseConfigs.get`
  * `dataform.releaseConfigs.list`
  * `dataform.releaseConfigs.update`
  * `dataform.repositories.commit`
  * `dataform.repositories.computeAccessTokenStatus`
  * `dataform.repositories.create`
  * `dataform.repositories.createTagBinding`
  * `dataform.repositories.delete`
  * `dataform.repositories.deleteTagBinding`
  * `dataform.repositories.fetchHistory`
  * `dataform.repositories.fetchRemoteBranches`
  * `dataform.repositories.get`
  * `dataform.repositories.getIamPolicy`
  * `dataform.repositories.list`
  * `dataform.repositories.listEffectiveTags`
  * `dataform.repositories.listTagBindings`
  * `dataform.repositories.move`
  * `dataform.repositories.queryDirectoryContents`
  * `dataform.repositories.readFile`
  * `dataform.repositories.scheduleRelease`
  * `dataform.repositories.scheduleWorkflow`
  * `dataform.repositories.setIamPolicy`
  * `dataform.repositories.update`
  * `dataform.teamFolders.create`
  * `dataform.teamFolders.delete`
  * `dataform.teamFolders.deleteTree`
  * `dataform.teamFolders.get`
  * `dataform.teamFolders.getIamPolicy`
  * `dataform.teamFolders.setIamPolicy`
  * `dataform.teamFolders.update`
  * `dataform.workflowConfigs.create`
  * `dataform.workflowConfigs.delete`
  * `dataform.workflowConfigs.get`
  * `dataform.workflowConfigs.list`
  * `dataform.workflowConfigs.update`
  * `dataform.workflowInvocations.cancel`
  * `dataform.workflowInvocations.create`
  * `dataform.workflowInvocations.delete`
  * `dataform.workflowInvocations.get`
  * `dataform.workflowInvocations.list`
  * `dataform.workflowInvocations.query`
  * `dataform.workspaces.commit`
  * `dataform.workspaces.create`
  * `dataform.workspaces.delete`
  * `dataform.workspaces.fetchFileDiff`
  * `dataform.workspaces.fetchFileGitStatuses`
  * `dataform.workspaces.fetchGitAheadBehind`
  * `dataform.workspaces.get`
  * `dataform.workspaces.getIamPolicy`
  * `dataform.workspaces.installNpmPackages`
  * `dataform.workspaces.list`
  * `dataform.workspaces.makeDirectory`
  * `dataform.workspaces.moveDirectory`
  * `dataform.workspaces.moveFile`
  * `dataform.workspaces.pull`
  * `dataform.workspaces.push`
  * `dataform.workspaces.queryDirectoryContents`
  * `dataform.workspaces.readFile`
  * `dataform.workspaces.removeDirectory`
  * `dataform.workspaces.removeFile`
  * `dataform.workspaces.reset`
  * `dataform.workspaces.searchFiles`
  * `dataform.workspaces.setIamPolicy`
  * `dataform.workspaces.writeFile`

`dataplex.agentTasks.*`

  * `dataplex.agentTasks.create`
  * `dataplex.agentTasks.delete`
  * `dataplex.agentTasks.get`
  * `dataplex.agentTasks.getData`
  * `dataplex.agentTasks.getIamPolicy`
  * `dataplex.agentTasks.list`
  * `dataplex.agentTasks.run`
  * `dataplex.agentTasks.setIamPolicy`
  * `dataplex.agentTasks.update`

`dataplex.assets.getIamPolicy` `dataplex.datascans.*`

  * `dataplex.datascans.cancel`
  * `dataplex.datascans.create`
  * `dataplex.datascans.delete`
  * `dataplex.datascans.get`
  * `dataplex.datascans.getData`
  * `dataplex.datascans.getIamPolicy`
  * `dataplex.datascans.list`
  * `dataplex.datascans.run`
  * `dataplex.datascans.setIamPolicy`
  * `dataplex.datascans.update`

`dataplex.environments.execute` `dataplex.environments.get` `dataplex.environments.list` `dataplex.lakes.get` `dataplex.lakes.getIamPolicy` `dataplex.operations.get` `dataplex.operations.list` `dataplex.projects.search` `dataplex.zones.getIamPolicy` `dataproc.batches.cancel` `dataproc.batches.create` `dataproc.batches.get` `dataproc.operations.cancel` `dataproc.operations.get` `dataproc.operations.list` `developerconnect.accountConnectors.*`

  * `developerconnect.accountConnectors.create`
  * `developerconnect.accountConnectors.delete`
  * `developerconnect.accountConnectors.fetchUserRepositories`
  * `developerconnect.accountConnectors.get`
  * `developerconnect.accountConnectors.gitProxyRead`
  * `developerconnect.accountConnectors.gitProxyWrite`
  * `developerconnect.accountConnectors.httpProxyRead`
  * `developerconnect.accountConnectors.httpProxyWrite`
  * `developerconnect.accountConnectors.list`
  * `developerconnect.accountConnectors.update`

`developerconnect.connections.constructGitHubAppManifest` `developerconnect.connections.create` `developerconnect.connections.delete` `developerconnect.connections.fetchGitHubInstallations` `developerconnect.connections.fetchLinkableGitRepositories` `developerconnect.connections.generateGitHubStateToken` `developerconnect.connections.get` `developerconnect.connections.list` `developerconnect.connections.processGitHubAppCreationCallback` `developerconnect.connections.processGitHubOAuthCallback` `developerconnect.connections.update` `developerconnect.gitRepositoryLinks.*`

  * `developerconnect.gitRepositoryLinks.create`
  * `developerconnect.gitRepositoryLinks.delete`
  * `developerconnect.gitRepositoryLinks.fetchGitRefs`
  * `developerconnect.gitRepositoryLinks.fetchReadToken`
  * `developerconnect.gitRepositoryLinks.fetchReadWriteToken`
  * `developerconnect.gitRepositoryLinks.get`
  * `developerconnect.gitRepositoryLinks.gitProxyRead`
  * `developerconnect.gitRepositoryLinks.gitProxyWrite`
  * `developerconnect.gitRepositoryLinks.list`

`developerconnect.locations.*`

  * `developerconnect.locations.get`
  * `developerconnect.locations.list`

`developerconnect.operations.*`

  * `developerconnect.operations.cancel`
  * `developerconnect.operations.delete`
  * `developerconnect.operations.get`
  * `developerconnect.operations.list`

`developerconnect.providers.list` `developerconnect.users.*`

  * `developerconnect.users.delete`
  * `developerconnect.users.deleteSelf`
  * `developerconnect.users.fetchAccessToken`
  * `developerconnect.users.finishOAuth`
  * `developerconnect.users.getSelf`
  * `developerconnect.users.list`
  * `developerconnect.users.startOAuth`

`firebase.projects.get` `iam.serviceAccounts.actAs` `logging.logEntries.create` `logging.logEntries.route` `metastore.services.get` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

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

`resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicemanagement.services.report` `serviceusage.services.use` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

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

  
  
### Dataplex Entry and EntryLink Owner role

The **Dataplex Entry and EntryLink Owner** (`roles/dataplex.entryOwner`) role includes the following features:

  * Grants full access to entry-related operations.
  * Grants full access to entry-link-related operations.
  * Grants permissions to add aspects to entries of some of the system aspect types, such as `Schema`, `Generic`, `Overview`, and `Contacts`.
  * Grants permissions to add aspects to entry links of some of the system aspect types, such as `SchemaJoin`.
  * Grants permissions to create entries of the `GenericEntry` type.
  * Grants permissions to create entry links of the `schema-join` type.
  * This role lets you create an entry with an entry type and aspect type, where the entry type and aspect type are defined in the same project as the entry. Otherwise, you must also grant the **Dataplex Entry Type User** (`roles/dataplex.entryTypeUser`) and **Dataplex Aspect Type User** (`roles/dataplex.aspectTypeUser`) roles on the projects where the entry and aspect types are defined.
  * This role lets you create all available entry links with their required aspects.
  * This role doesn't grant permissions to read entries that are created from Google Cloud resources outside of Knowledge Catalog, such as BigQuery entries, when using the [`LookupEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntry), [`SearchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries), or [`ModifyEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/modifyEntry) methods. To read or modify these entries, you must have the respective metadata read or update permissions on the source system resources. Alternatively, you can read the entries with only the **Dataplex Entry and EntryLink Owner** (`roles/dataplex.entryOwner`) role by using the [`GetEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) method, or modify the entry using the [`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.



### Role considerations

  * No role grants permissions to add or delete Knowledge Catalog entries from system-defined entry groups, such as `@bigquery` and `@dataplex`.

  * To view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects) attached to an entry, you need permissions to read data from the source asset that the entry represents, in addition to permissions to view the entry. If you have permission to view an entry but lack data-read permissions for the source asset, you can still view all other metadata on the entry. However, Knowledge Catalog hides the content of any attached data aspects.

  * The **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) and **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) roles grant permissions to view custom entries.

  * The **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) role grants permissions to get and list context sets and locations (`dataplex.contextSets.get`, `dataplex.contextSets.list`, `dataplex.locations.get`, and `dataplex.locations.list`). The **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) roles grant full creation, modification, deletion, and file upload or download permissions for context sets.

  * To search for entries using the [`SearchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) method, you must have at least one of the following IAM roles on the project used in the API request: **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`), **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`), or **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`). Permissions on search results are checked independently of the selected project.




## Predefined roles for data lineage

To access the lineage for any Knowledge Catalog entry, you need a viewer role on the corresponding [system resource](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets#required-roles) or the [Dataplex Catalog Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project that stores the Knowledge Catalog entry. This section describes the roles required to work with lineage.

Role | Permissions  
---|---  
  
#### Data Lineage Administrator 

(`roles/datalineage.admin`) Grants full access to all resources in Data Lineage API  |  `datalineage.*`

  * `datalineage.configs.get`
  * `datalineage.configs.update`
  * `datalineage.events.create`
  * `datalineage.events.delete`
  * `datalineage.events.get`
  * `datalineage.events.getFields`
  * `datalineage.events.list`
  * `datalineage.locations.processOpenLineageMessage`
  * `datalineage.locations.searchLinks`
  * `datalineage.operations.get`
  * `datalineage.processRevisions.delete`
  * `datalineage.processRevisions.get`
  * `datalineage.processRevisions.insert`
  * `datalineage.processRevisions.list`
  * `datalineage.processes.create`
  * `datalineage.processes.delete`
  * `datalineage.processes.get`
  * `datalineage.processes.list`
  * `datalineage.processes.markAsDeleted`
  * `datalineage.processes.update`
  * `datalineage.runs.create`
  * `datalineage.runs.delete`
  * `datalineage.runs.get`
  * `datalineage.runs.list`
  * `datalineage.runs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Editor 

(`roles/datalineage.editor`) Grants edit access to all resources in Data Lineage API  |  `datalineage.events.*`

  * `datalineage.events.create`
  * `datalineage.events.delete`
  * `datalineage.events.get`
  * `datalineage.events.getFields`
  * `datalineage.events.list`

`datalineage.locations.*`

  * `datalineage.locations.processOpenLineageMessage`
  * `datalineage.locations.searchLinks`

`datalineage.operations.get` `datalineage.processRevisions.*`

  * `datalineage.processRevisions.delete`
  * `datalineage.processRevisions.get`
  * `datalineage.processRevisions.insert`
  * `datalineage.processRevisions.list`

`datalineage.processes.*`

  * `datalineage.processes.create`
  * `datalineage.processes.delete`
  * `datalineage.processes.get`
  * `datalineage.processes.list`
  * `datalineage.processes.markAsDeleted`
  * `datalineage.processes.update`

`datalineage.runs.*`

  * `datalineage.runs.create`
  * `datalineage.runs.delete`
  * `datalineage.runs.get`
  * `datalineage.runs.list`
  * `datalineage.runs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Viewer 

(`roles/datalineage.viewer`) Grants read access to all resources in Data Lineage API  |  `datalineage.events.get` `datalineage.events.getFields` `datalineage.events.list` `datalineage.locations.searchLinks` `datalineage.processRevisions.get` `datalineage.processRevisions.list` `datalineage.processes.get` `datalineage.processes.list` `datalineage.runs.get` `datalineage.runs.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Events Producer 

(`roles/datalineage.producer`) Grants access to creating all resources in Data Lineage API  |  `datalineage.events.create` `datalineage.locations.processOpenLineageMessage` `datalineage.processRevisions.insert` `datalineage.processes.create` `datalineage.processes.get` `datalineage.processes.markAsDeleted` `datalineage.processes.update` `datalineage.runs.create` `datalineage.runs.get` `datalineage.runs.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Lineage viewer role

The [Data Lineage Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#data-lineage-roles) (`roles/datalineage.viewer`) lets you view Knowledge Catalog lineage in the Google Cloud console and read lineage information using the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest). The runs and events for a given process are all stored in the same project as the process. In the case of [automated lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage), the process, runs, and events are stored in the project in which the job that generated the lineage was running. For example, this could be the project in which a BigQuery job was running.

To view lineage between assets, you need the [Data Lineage Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#data-lineage-roles) (`roles/datalineage.viewer`) on both the project in which you're viewing lineage and the projects in which lineage is recorded. Specifically, you need the role on the following projects:

  * The **project in which you're viewing lineage** (known as [active project](https://docs.cloud.google.com/knowledge-catalog/docs/troubleshooting-lineage#active-project)), that is, the project in the drop-down at the top of the Google Cloud console or the project from which API calls are made. This is typically the project containing the resources you create in Knowledge Catalog or access in other Google Cloud systems with the API.
  * The **projects in which lineage is recorded** (known as [compute project](https://docs.cloud.google.com/knowledge-catalog/docs/troubleshooting-lineage#compute-project)). Lineage is stored in the project where the corresponding process executed, as described earlier. This project can be different from the project storing the asset that you're viewing lineage for.



To view asset metadata, you need the same roles used for accessing metadata entries in Knowledge Catalog.

Depending on the use case, grant the [Data Lineage Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#data-lineage-roles) (`roles/datalineage.viewer`) on the folder or organization level to ensure access to the lineage (see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role)).

**Note:** To see the SQL statement for a BigQuery process, you must have the `bigquery.jobs.get` permission for the corresponding job. To see the SQL statement for a BigQuery view definition, you must have the `bigquery.tables.get` permission for the corresponding view.

### Roles to view asset metadata when viewing lineage

To view metadata about an asset stored in Knowledge Catalog, you must have a viewer role on the corresponding [system resource](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets#required-roles) or the [Dataplex Catalog Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project storing the Knowledge Catalog entry. You might have access to assets on the lineage graph or list through appropriate viewer roles but no access to the lineage between them. This occurs if you don't have the [Data Lineage Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#data-lineage-roles) (`roles/datalineage.viewer`) on the project where the lineage was recorded. In this case, the Data Lineage API and Google Cloud console don't show the lineage or return an error. This prevents leaking information about the existence of lineage. Therefore, the absence of lineage for an asset doesn't mean that no lineage exists, but rather that you might not have permissions to view it.

**Note:** If an asset is located in an organization that you're not a member of, data lineage might not be able to retrieve the metadata for that asset.

## Metadata roles

Metadata roles grant permissions to view and update metadata, such as table schemas.

Role | Description  
---|---  
**Dataplex Metadata Writer**  
(`roles/dataplex.metadataWriter`) | Lets you update a resource's metadata.  
**Dataplex Metadata Reader**  
(`roles/dataplex.metadataReader`) | Lets you read metadata, for example, to query a table.  
**Note:** The **Dataplex Metadata Reader** (`roles/dataplex.metadataReader`) role grants permissions to read-only metadata. The **Dataplex Data Reader** (`roles/dataplex.dataReader`) role, described in the Data roles section, includes all the permissions of `roles/dataplex.metadataReader` plus permissions to read the actual data.

## Data roles

Knowledge Catalog defines the following IAM roles that apply to any resource managed by Knowledge Catalog. For more information about the permissions associated with each role, see the [Predefined roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#predefined-roles) section of this document.

Role | Description  
---|---  
**Dataplex Data Owner**  
(`roles/dataplex.dataOwner`) | Full access to the managed resource and its children. Permissions include updating metadata, creating child resources, and granting granular permissions.  
**Dataplex Data Reader**  
(`roles/dataplex.dataReader`) | Read access to data and metadata in the managed resource and its children.  
**Dataplex Data Writer**  
(`roles/dataplex.dataWriter`) | Write access to data in the managed resource. This includes creating, updating, and deleting data, but not metadata.  
  
## What's next

  * Learn how to [create custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).
  * Learn how to [grant and manage roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * See the [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
