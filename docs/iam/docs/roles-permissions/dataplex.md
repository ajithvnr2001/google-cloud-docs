---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex/
title: Knowledge Catalog roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:26.379548+00:00
---

# Knowledge Catalog roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Knowledge Catalog roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Knowledge Catalog. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Knowledge Catalog roles

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

  
  
## Knowledge Catalog permissions

Permission | Included in roles  
---|---  
  
#### `dataplex.agentTasks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.getData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.agentTasks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog TagTemplate Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateCreator) (`roles/datacatalog.tagTemplateCreator`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Data Catalog TagTemplate Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateCreator) (`roles/datacatalog.tagTemplateCreator`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Data Catalog TagTemplate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateViewer) (`roles/datacatalog.tagTemplateViewer`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Data Catalog TagTemplate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateViewer) (`roles/datacatalog.tagTemplateViewer`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.aspectTypes.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.assetActions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.assets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.assets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.assets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.assets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.assets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.assets.ownData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataOwner) (`roles/dataplex.dataOwner`)   
  
#### `dataplex.assets.readData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataOwner) (`roles/dataplex.dataOwner`)  [Dataplex Data Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataReader) (`roles/dataplex.dataReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.assets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.assets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.assets.writeData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataOwner) (`roles/dataplex.dataOwner`)  [Dataplex Data Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataWriter) (`roles/dataplex.dataWriter`)   
  
#### `dataplex.changeRequests.adminDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Workflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)   
  
#### `dataplex.changeRequests.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Change Request Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.changeRequestOwner) (`roles/dataplex.changeRequestOwner`)  [Dataplex Workflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)   
  
#### `dataplex.changeRequests.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Change Request Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.changeRequestOwner) (`roles/dataplex.changeRequestOwner`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Workflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)  [Dataplex Workflow Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.changeRequests.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.changeRequests.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Workflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)  [Dataplex Workflow Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.changeRequests.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.changeRequests.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Change Request Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.changeRequestOwner) (`roles/dataplex.changeRequestOwner`)   
  
#### `dataplex.changeRequests.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Workflow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)  [Dataplex Workflow Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`)   
  
#### `dataplex.content.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.content.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.content.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.content.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.content.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.content.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.content.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.dataAssets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataAssets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataAssets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsConsumer) (`roles/dataplex.dataProductsConsumer`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex Data Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAssets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsConsumer) (`roles/dataplex.dataProductsConsumer`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex Data Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAssets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataAttributeBindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)   
  
#### `dataplex.dataAttributeBindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)   
  
#### `dataplex.dataAttributeBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributeBindings.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributeBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributeBindings.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)   
  
#### `dataplex.dataAttributeBindings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Binding Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.bindingAdmin) (`roles/dataplex.bindingAdmin`)   
  
#### `dataplex.dataAttributes.bind`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataAttributes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataAttributes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataAttributes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataAttributes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataAttributes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataDomainBindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)   
  
#### `dataplex.dataDomainBindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)   
  
#### `dataplex.dataDomainBindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomainBindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomains.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)   
  
#### `dataplex.dataDomains.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)   
  
#### `dataplex.dataDomains.discover`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Entry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEntryReader) (`roles/dataplex.dataDomainEntryReader`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Link Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeUser) (`roles/dataplex.entryLinkTypeUser`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.dataDomains.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Entry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEntryReader) (`roles/dataplex.dataDomainEntryReader`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomains.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomains.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Entry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEntryReader) (`roles/dataplex.dataDomainEntryReader`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomains.lookupEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Domain Entry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEntryReader) (`roles/dataplex.dataDomainEntryReader`)  [Dataplex Data Domain Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataDomains.modifyEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)   
  
#### `dataplex.dataDomains.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)   
  
#### `dataplex.dataDomains.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)   
  
#### `dataplex.dataProducts.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataProducts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataProducts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataProducts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsConsumer) (`roles/dataplex.dataProductsConsumer`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex Data Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataProducts.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex Data Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataProducts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex Data Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataProducts.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)   
  
#### `dataplex.dataProducts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)   
  
#### `dataplex.dataTaxonomies.configureDataAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Security Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.securityAdmin) (`roles/dataplex.securityAdmin`)   
  
#### `dataplex.dataTaxonomies.configureResourceAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Security Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.securityAdmin) (`roles/dataplex.securityAdmin`)   
  
#### `dataplex.dataTaxonomies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataTaxonomies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataTaxonomies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataTaxonomies.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataTaxonomies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)  [Dataplex Taxonomy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyViewer) (`roles/dataplex.taxonomyViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.dataTaxonomies.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.dataTaxonomies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Taxonomy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.taxonomyAdmin) (`roles/dataplex.taxonomyAdmin`)   
  
#### `dataplex.datascans.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.getData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan DataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex DataScan Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.datascans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.encryptionConfig.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)   
  
#### `dataplex.encryptionConfig.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)   
  
#### `dataplex.encryptionConfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.encryptionConfig.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.encryptionConfig.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)   
  
#### `dataplex.entities.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.entities.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.entities.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entities.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entities.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.entries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.createContext`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.deleteContext`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.entries.getContext`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.getData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entries.link`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entries.listContext`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entries.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Data Catalog Tag Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagEditor) (`roles/datacatalog.tagEditor`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.entries.updateContext`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.createContextSet`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.entryGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.deleteContextSet`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.entryGroups.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Exporter](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupExporter) (`roles/dataplex.entryGroupExporter`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Exporter](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupExporter) (`roles/dataplex.entryGroupExporter`)  [Dataplex Entry Group Importer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.getContextSet`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Importer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.requestChanges`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryGroups.requestContextChanges`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.updateContextSet`

|  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)   
  
#### `dataplex.entryGroups.useCertificationAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useContactsAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useContextAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useContextEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useContextEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDataProfileAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useDataQualityRuleTemplateAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDataQualityRuleTemplateEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDataQualityScorecardAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDataRulesAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDatabaseDataPolicyAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useDefinitionEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDescriptionsAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDocumentAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useDocumentEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useGenericAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useGenericEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useGraphProfileAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useManagedConnectorTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useMySQLConnectorTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useOracleConnectorTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useOverviewAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.usePostgreSQLConnectorTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useQueriesAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useQueryTemplateAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useQueryTemplateEntry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useReferenceEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useRefreshCadenceAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useRelatedEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useSQLAccessAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useSQLServerConnectorTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useSQLTriggersAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useSchemaAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useSchemaJoinAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useSchemaJoinEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useSecondaryIndexesAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useStorageAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.entryGroups.useSynonymEntryLink`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryGroups.useUsageAspect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryLinkTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)   
  
#### `dataplex.entryLinkTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)   
  
#### `dataplex.entryLinkTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Link Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeUser) (`roles/dataplex.entryLinkTypeUser`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryLinkTypes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryLinkTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Link Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeUser) (`roles/dataplex.entryLinkTypeUser`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryLinkTypes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)   
  
#### `dataplex.entryLinkTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)   
  
#### `dataplex.entryLinkTypes.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Link Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeUser) (`roles/dataplex.entryLinkTypeUser`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryLinks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryLinks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryLinks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryLinks.reference`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryLinks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)   
  
#### `dataplex.entryTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)   
  
#### `dataplex.entryTypes.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.entryTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)   
  
#### `dataplex.entryTypes.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.entryTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryTypes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryTypes.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryTypes.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.entryTypes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)   
  
#### `dataplex.entryTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)   
  
#### `dataplex.entryTypes.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)   
  
#### `dataplex.environments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.environments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.environments.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.environments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.environments.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.environments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.environments.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.environments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.glossaries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaries.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaries.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)   
  
#### `dataplex.glossaries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaries.requestChanges`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaries.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)   
  
#### `dataplex.glossaries.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryCategories.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryCategories.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryCategories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaryCategories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaryCategories.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryTerms.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryTerms.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryTerms.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaryTerms.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.glossaryTerms.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.glossaryTerms.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)   
  
#### `dataplex.governanceRules.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.governanceRules.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `dataplex.governanceRules.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.governanceRules.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.lakeActions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.lakes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.lakes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.lakes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.lakes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.lakes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.lakes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.lakes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.metadataFeeds.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)   
  
#### `dataplex.metadataFeeds.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)   
  
#### `dataplex.metadataFeeds.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)  [Dataplex Metadata Feed Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedViewer) (`roles/dataplex.metadataFeedViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.metadataFeeds.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)  [Dataplex Metadata Feed Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedViewer) (`roles/dataplex.metadataFeedViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.metadataFeeds.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)   
  
#### `dataplex.metadataJobs.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`)   
  
#### `dataplex.metadataJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.metadataJobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`)  [Dataplex Metadata Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobViewer) (`roles/dataplex.metadataJobViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.metadataJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`)  [Dataplex Metadata Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobViewer) (`roles/dataplex.metadataJobViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [BigQuery Data Transfer Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent) (`roles/bigquerydatatransfer.serviceAgent`) 

  
  
#### `dataplex.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Data Domain Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`)  [Dataplex Data Domain Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`)  [Dataplex Data Products Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)  [Dataplex Data Products Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)  [Dataplex DataScan Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Metadata Feed Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedOwner) (`roles/dataplex.metadataFeedOwner`)  [Dataplex Metadata Feed Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataFeedViewer) (`roles/dataplex.metadataFeedViewer`)  [Dataplex Metadata Job Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`)  [Dataplex Metadata Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobViewer) (`roles/dataplex.metadataJobViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)  [BigQuery Data Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex DataScan Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`)  [Dataplex Encryption Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.encryptionAdmin) (`roles/dataplex.encryptionAdmin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.partitions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.partitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.partitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.partitions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.partitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)   
  
#### `dataplex.projects.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [BigQuery User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [BigQuery Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.securityAdmin) (`roles/bigquery.securityAdmin`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)  [DataCatalog Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.searchAdmin) (`roles/datacatalog.searchAdmin`)  [Data Catalog TagTemplate Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateCreator) (`roles/datacatalog.tagTemplateCreator`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Data Catalog TagTemplate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateViewer) (`roles/datacatalog.tagTemplateViewer`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry Link Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeOwner) (`roles/dataplex.entryLinkTypeOwner`)  [Dataplex Entry Link Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryLinkTypeUser) (`roles/dataplex.entryLinkTypeUser`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `dataplex.tasks.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.tasks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.tasks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.tasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.tasks.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.tasks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.tasks.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.tasks.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.tasks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.developer) (`roles/dataplex.developer`)   
  
#### `dataplex.zoneActions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.zones.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.zones.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
#### `dataplex.zones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.zones.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `dataplex.zones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)  [Dataplex Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataplex Metadata Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`)  [Dataplex Metadata Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataWriter) (`roles/dataplex.metadataWriter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataplex.zones.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `dataplex.zones.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataplex Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`)  [Dataplex Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.editor) (`roles/dataplex.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
