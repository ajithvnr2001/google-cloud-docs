---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog/
title: Data Catalog roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:33.516857+00:00
---

# Data Catalog roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Catalog roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Catalog. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Catalog roles

Role | Permissions  
---|---  
  
#### Data Catalog Admin 

(`roles/datacatalog.admin`) Full access to all DataCatalog resources  |  `bigquery.connections.get` `bigquery.connections.updateTag` `bigquery.datasets.get` `bigquery.datasets.updateTag` `bigquery.models.getMetadata` `bigquery.models.updateTag` `bigquery.routines.get` `bigquery.routines.updateTag` `bigquery.tables.get` `bigquery.tables.updateTag` `datacatalog.catalogs.searchAll` `datacatalog.categories.getIamPolicy` `datacatalog.categories.setIamPolicy` `datacatalog.entries.*`

  * `datacatalog.entries.create`
  * `datacatalog.entries.createGlossary`
  * `datacatalog.entries.createGlossaryCategory`
  * `datacatalog.entries.createGlossaryTerm`
  * `datacatalog.entries.delete`
  * `datacatalog.entries.deleteGlossary`
  * `datacatalog.entries.deleteGlossaryCategory`
  * `datacatalog.entries.deleteGlossaryTerm`
  * `datacatalog.entries.get`
  * `datacatalog.entries.getIamPolicy`
  * `datacatalog.entries.list`
  * `datacatalog.entries.setIamPolicy`
  * `datacatalog.entries.update`
  * `datacatalog.entries.updateContacts`
  * `datacatalog.entries.updateGlossary`
  * `datacatalog.entries.updateGlossaryCategory`
  * `datacatalog.entries.updateGlossaryTerm`
  * `datacatalog.entries.updateOverview`
  * `datacatalog.entries.updateTag`

`datacatalog.entryGroups.*`

  * `datacatalog.entryGroups.create`
  * `datacatalog.entryGroups.delete`
  * `datacatalog.entryGroups.get`
  * `datacatalog.entryGroups.getIamPolicy`
  * `datacatalog.entryGroups.list`
  * `datacatalog.entryGroups.setIamPolicy`
  * `datacatalog.entryGroups.update`
  * `datacatalog.entryGroups.updateTag`

`datacatalog.migrationConfig.*`

  * `datacatalog.migrationConfig.get`
  * `datacatalog.migrationConfig.set`

`datacatalog.operations.list` `datacatalog.relationships.*`

  * `datacatalog.relationships.create`
  * `datacatalog.relationships.createBelongsTo`
  * `datacatalog.relationships.createIsDescribedBy`
  * `datacatalog.relationships.createIsRelatedTo`
  * `datacatalog.relationships.createIsSynonymousTo`
  * `datacatalog.relationships.delete`
  * `datacatalog.relationships.deleteBelongsTo`
  * `datacatalog.relationships.deleteIsDescribedBy`
  * `datacatalog.relationships.deleteIsRelatedTo`
  * `datacatalog.relationships.deleteIsSynonymousTo`
  * `datacatalog.relationships.list`

`datacatalog.tagTemplates.*`

  * `datacatalog.tagTemplates.create`
  * `datacatalog.tagTemplates.delete`
  * `datacatalog.tagTemplates.get`
  * `datacatalog.tagTemplates.getIamPolicy`
  * `datacatalog.tagTemplates.getTag`
  * `datacatalog.tagTemplates.setIamPolicy`
  * `datacatalog.tagTemplates.update`
  * `datacatalog.tagTemplates.use`

`datacatalog.taxonomies.*`

  * `datacatalog.taxonomies.create`
  * `datacatalog.taxonomies.delete`
  * `datacatalog.taxonomies.get`
  * `datacatalog.taxonomies.getIamPolicy`
  * `datacatalog.taxonomies.list`
  * `datacatalog.taxonomies.setIamPolicy`
  * `datacatalog.taxonomies.update`

`dataplex.aspectTypes.*`

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

`dataplex.operations.get` `dataplex.projects.search` `pubsub.topics.get` `pubsub.topics.updateTag` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Catalog Editor 

(`roles/datacatalog.editor`) Editor role for Data Catalog  |  `bigquery.connections.get` `bigquery.datasets.get` `bigquery.models.getMetadata` `bigquery.routines.get` `bigquery.tables.get` `datacatalog.catalogs.searchAll` `datacatalog.categories.getIamPolicy` `datacatalog.entries.create` `datacatalog.entries.createGlossary` `datacatalog.entries.createGlossaryCategory` `datacatalog.entries.createGlossaryTerm` `datacatalog.entries.delete` `datacatalog.entries.deleteGlossary` `datacatalog.entries.deleteGlossaryCategory` `datacatalog.entries.deleteGlossaryTerm` `datacatalog.entries.get` `datacatalog.entries.getIamPolicy` `datacatalog.entries.list` `datacatalog.entries.update` `datacatalog.entries.updateContacts` `datacatalog.entries.updateGlossary` `datacatalog.entries.updateGlossaryCategory` `datacatalog.entries.updateGlossaryTerm` `datacatalog.entries.updateOverview` `datacatalog.entries.updateTag` `datacatalog.entryGroups.create` `datacatalog.entryGroups.delete` `datacatalog.entryGroups.get` `datacatalog.entryGroups.getIamPolicy` `datacatalog.entryGroups.list` `datacatalog.entryGroups.update` `datacatalog.entryGroups.updateTag` `datacatalog.migrationConfig.*`

  * `datacatalog.migrationConfig.get`
  * `datacatalog.migrationConfig.set`

`datacatalog.operations.list` `datacatalog.relationships.*`

  * `datacatalog.relationships.create`
  * `datacatalog.relationships.createBelongsTo`
  * `datacatalog.relationships.createIsDescribedBy`
  * `datacatalog.relationships.createIsRelatedTo`
  * `datacatalog.relationships.createIsSynonymousTo`
  * `datacatalog.relationships.delete`
  * `datacatalog.relationships.deleteBelongsTo`
  * `datacatalog.relationships.deleteIsDescribedBy`
  * `datacatalog.relationships.deleteIsRelatedTo`
  * `datacatalog.relationships.deleteIsSynonymousTo`
  * `datacatalog.relationships.list`

`datacatalog.tagTemplates.create` `datacatalog.tagTemplates.delete` `datacatalog.tagTemplates.get` `datacatalog.tagTemplates.getIamPolicy` `datacatalog.tagTemplates.getTag` `datacatalog.tagTemplates.update` `datacatalog.tagTemplates.use` `datacatalog.taxonomies.get` `datacatalog.taxonomies.getIamPolicy` `datacatalog.taxonomies.list` `dataplex.aspectTypes.get` `dataplex.aspectTypes.getIamPolicy` `dataplex.aspectTypes.list` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.get` `dataplex.entries.list` `dataplex.entryGroups.get` `dataplex.entryGroups.getIamPolicy` `dataplex.entryGroups.list` `dataplex.entryGroups.listEffectiveTags` `dataplex.entryGroups.listTagBindings` `dataplex.entryGroups.requestChanges` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.getIamPolicy` `dataplex.entryLinkTypes.list` `dataplex.entryLinks.get` `dataplex.entryTypes.get` `dataplex.entryTypes.getIamPolicy` `dataplex.entryTypes.list` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.glossaries.get` `dataplex.glossaries.getIamPolicy` `dataplex.glossaries.list` `dataplex.glossaries.requestChanges` `dataplex.glossaryCategories.get` `dataplex.glossaryCategories.list` `dataplex.glossaryTerms.get` `dataplex.glossaryTerms.list` `dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.projects.search` `pubsub.topics.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Catalog Viewer 

(`roles/datacatalog.viewer`) Provides metadata read access to catalogued Google Cloud assets for BigQuery and Pub/Sub  |  `bigquery.connections.get` `bigquery.datasets.get` `bigquery.models.getMetadata` `bigquery.routines.get` `bigquery.tables.get` `datacatalog.catalogs.searchAll` `datacatalog.categories.getIamPolicy` `datacatalog.entries.get` `datacatalog.entries.getIamPolicy` `datacatalog.entries.list` `datacatalog.entryGroups.get` `datacatalog.entryGroups.getIamPolicy` `datacatalog.entryGroups.list` `datacatalog.migrationConfig.get` `datacatalog.operations.list` `datacatalog.relationships.list` `datacatalog.tagTemplates.get` `datacatalog.tagTemplates.getIamPolicy` `datacatalog.tagTemplates.getTag` `datacatalog.taxonomies.get` `datacatalog.taxonomies.getIamPolicy` `datacatalog.taxonomies.list` `dataplex.aspectTypes.get` `dataplex.aspectTypes.getIamPolicy` `dataplex.aspectTypes.list` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.get` `dataplex.entries.list` `dataplex.entryGroups.get` `dataplex.entryGroups.getIamPolicy` `dataplex.entryGroups.list` `dataplex.entryGroups.listEffectiveTags` `dataplex.entryGroups.listTagBindings` `dataplex.entryGroups.requestChanges` `dataplex.entryLinkTypes.get` `dataplex.entryLinkTypes.getIamPolicy` `dataplex.entryLinkTypes.list` `dataplex.entryLinks.get` `dataplex.entryTypes.get` `dataplex.entryTypes.getIamPolicy` `dataplex.entryTypes.list` `dataplex.entryTypes.listEffectiveTags` `dataplex.entryTypes.listTagBindings` `dataplex.glossaries.get` `dataplex.glossaries.getIamPolicy` `dataplex.glossaries.list` `dataplex.glossaries.requestChanges` `dataplex.glossaryCategories.get` `dataplex.glossaryCategories.list` `dataplex.glossaryTerms.get` `dataplex.glossaryTerms.list` `dataplex.locations.*`

  * `dataplex.locations.get`
  * `dataplex.locations.list`

`dataplex.projects.search` `pubsub.topics.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Policy Tag Admin 

(`roles/datacatalog.categoryAdmin`) Manage taxonomies  |  `datacatalog.categories.getIamPolicy` `datacatalog.categories.setIamPolicy` `datacatalog.taxonomies.*`

  * `datacatalog.taxonomies.create`
  * `datacatalog.taxonomies.delete`
  * `datacatalog.taxonomies.get`
  * `datacatalog.taxonomies.getIamPolicy`
  * `datacatalog.taxonomies.list`
  * `datacatalog.taxonomies.setIamPolicy`
  * `datacatalog.taxonomies.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Fine-Grained Reader 

(`roles/datacatalog.categoryFineGrainedReader`) Read access to sub-resources tagged by a policy tag, for example, BigQuery columns  |  `datacatalog.categories.fineGrainedGet`  
  
#### DataCatalog Data Steward Beta

(`roles/datacatalog.dataSteward`) Can update overview and data steward fields  |  `datacatalog.entries.get` `datacatalog.entries.list` `datacatalog.entries.updateContacts` `datacatalog.entries.updateOverview` `datacatalog.entryGroups.get` `datacatalog.migrationConfig.get` `datacatalog.relationships.list` `dataplex.entries.get` `dataplex.entries.list` `dataplex.entryGroups.get` `dataplex.entryGroups.useContactsAspect` `dataplex.entryGroups.useOverviewAspect` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DataCatalog EntryGroup Creator 

(`roles/datacatalog.entryGroupCreator`) Can create new entryGroups  |  `datacatalog.entryGroups.create` `datacatalog.entryGroups.get` `datacatalog.entryGroups.list` `dataplex.entryGroups.create` `dataplex.entryGroups.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DataCatalog EntryGroup Owner 

(`roles/datacatalog.entryGroupOwner`) Full access to entryGroups  |  `datacatalog.entries.*`

  * `datacatalog.entries.create`
  * `datacatalog.entries.createGlossary`
  * `datacatalog.entries.createGlossaryCategory`
  * `datacatalog.entries.createGlossaryTerm`
  * `datacatalog.entries.delete`
  * `datacatalog.entries.deleteGlossary`
  * `datacatalog.entries.deleteGlossaryCategory`
  * `datacatalog.entries.deleteGlossaryTerm`
  * `datacatalog.entries.get`
  * `datacatalog.entries.getIamPolicy`
  * `datacatalog.entries.list`
  * `datacatalog.entries.setIamPolicy`
  * `datacatalog.entries.update`
  * `datacatalog.entries.updateContacts`
  * `datacatalog.entries.updateGlossary`
  * `datacatalog.entries.updateGlossaryCategory`
  * `datacatalog.entries.updateGlossaryTerm`
  * `datacatalog.entries.updateOverview`
  * `datacatalog.entries.updateTag`

`datacatalog.entryGroups.*`

  * `datacatalog.entryGroups.create`
  * `datacatalog.entryGroups.delete`
  * `datacatalog.entryGroups.get`
  * `datacatalog.entryGroups.getIamPolicy`
  * `datacatalog.entryGroups.list`
  * `datacatalog.entryGroups.setIamPolicy`
  * `datacatalog.entryGroups.update`
  * `datacatalog.entryGroups.updateTag`

`datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.*`

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
  
#### DataCatalog Entry Owner 

(`roles/datacatalog.entryOwner`) Full access to entries  |  `datacatalog.entries.*`

  * `datacatalog.entries.create`
  * `datacatalog.entries.createGlossary`
  * `datacatalog.entries.createGlossaryCategory`
  * `datacatalog.entries.createGlossaryTerm`
  * `datacatalog.entries.delete`
  * `datacatalog.entries.deleteGlossary`
  * `datacatalog.entries.deleteGlossaryCategory`
  * `datacatalog.entries.deleteGlossaryTerm`
  * `datacatalog.entries.get`
  * `datacatalog.entries.getIamPolicy`
  * `datacatalog.entries.list`
  * `datacatalog.entries.setIamPolicy`
  * `datacatalog.entries.update`
  * `datacatalog.entries.updateContacts`
  * `datacatalog.entries.updateGlossary`
  * `datacatalog.entries.updateGlossaryCategory`
  * `datacatalog.entries.updateGlossaryTerm`
  * `datacatalog.entries.updateOverview`
  * `datacatalog.entries.updateTag`

`datacatalog.entryGroups.get` `datacatalog.migrationConfig.get` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.changeRequests.get` `dataplex.changeRequests.list` `dataplex.dataDomains.discover` `dataplex.entries.*`

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
  
#### DataCatalog Entry Viewer 

(`roles/datacatalog.entryViewer`) Read access to entries  |  `datacatalog.entries.get` `datacatalog.entries.list` `datacatalog.entryGroups.get` `datacatalog.migrationConfig.get` `datacatalog.relationships.list` `dataplex.entries.get` `dataplex.entries.list` `dataplex.entryGroups.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DataCatalog Glossary Owner Beta

(`roles/datacatalog.glossaryOwner`) Full access to glossaries  |  `datacatalog.entries.*`

  * `datacatalog.entries.create`
  * `datacatalog.entries.createGlossary`
  * `datacatalog.entries.createGlossaryCategory`
  * `datacatalog.entries.createGlossaryTerm`
  * `datacatalog.entries.delete`
  * `datacatalog.entries.deleteGlossary`
  * `datacatalog.entries.deleteGlossaryCategory`
  * `datacatalog.entries.deleteGlossaryTerm`
  * `datacatalog.entries.get`
  * `datacatalog.entries.getIamPolicy`
  * `datacatalog.entries.list`
  * `datacatalog.entries.setIamPolicy`
  * `datacatalog.entries.update`
  * `datacatalog.entries.updateContacts`
  * `datacatalog.entries.updateGlossary`
  * `datacatalog.entries.updateGlossaryCategory`
  * `datacatalog.entries.updateGlossaryTerm`
  * `datacatalog.entries.updateOverview`
  * `datacatalog.entries.updateTag`

`datacatalog.relationships.*`

  * `datacatalog.relationships.create`
  * `datacatalog.relationships.createBelongsTo`
  * `datacatalog.relationships.createIsDescribedBy`
  * `datacatalog.relationships.createIsRelatedTo`
  * `datacatalog.relationships.createIsSynonymousTo`
  * `datacatalog.relationships.delete`
  * `datacatalog.relationships.deleteBelongsTo`
  * `datacatalog.relationships.deleteIsDescribedBy`
  * `datacatalog.relationships.deleteIsRelatedTo`
  * `datacatalog.relationships.deleteIsSynonymousTo`
  * `datacatalog.relationships.list`

`dataplex.projects.search`  
  
#### DataCatalog Glossary User Beta

(`roles/datacatalog.glossaryUser`) Can view glossaries and associate terms to entries  |  `datacatalog.entries.get` `datacatalog.entries.list` `datacatalog.relationships.*`

  * `datacatalog.relationships.create`
  * `datacatalog.relationships.createBelongsTo`
  * `datacatalog.relationships.createIsDescribedBy`
  * `datacatalog.relationships.createIsRelatedTo`
  * `datacatalog.relationships.createIsSynonymousTo`
  * `datacatalog.relationships.delete`
  * `datacatalog.relationships.deleteBelongsTo`
  * `datacatalog.relationships.deleteIsDescribedBy`
  * `datacatalog.relationships.deleteIsRelatedTo`
  * `datacatalog.relationships.deleteIsSynonymousTo`
  * `datacatalog.relationships.list`

`dataplex.projects.search`  
  
#### DataCatalog Migration Config Admin 

(`roles/datacatalog.migrationConfigAdmin`) Full access to Migration Config  |  `datacatalog.migrationConfig.*`

  * `datacatalog.migrationConfig.get`
  * `datacatalog.migrationConfig.set`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### DataCatalog Search Admin 

(`roles/datacatalog.searchAdmin`) Can search all metadata for a project/org in DataCatalog  |  `datacatalog.catalogs.searchAll` `dataplex.projects.search` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Catalog Tag Editor 

(`roles/datacatalog.tagEditor`) Access to modify metadata tags for entries, as well as BigQuery and Pub/Sub data assets  |  `bigquery.connections.updateTag` `bigquery.datasets.updateTag` `bigquery.models.updateTag` `bigquery.routines.updateTag` `bigquery.tables.updateTag` `datacatalog.entries.updateTag` `datacatalog.entryGroups.updateTag` `dataplex.entries.update` `pubsub.topics.updateTag`  
  
#### Data Catalog TagTemplate Creator 

(`roles/datacatalog.tagTemplateCreator`) Access to create new tag templates  |  `datacatalog.tagTemplates.create` `datacatalog.tagTemplates.get` `dataplex.aspectTypes.create` `dataplex.aspectTypes.get` `dataplex.projects.search`  
  
#### Data Catalog TagTemplate Owner 

(`roles/datacatalog.tagTemplateOwner`) Full access to tag templates  |  `datacatalog.migrationConfig.get` `datacatalog.tagTemplates.*`

  * `datacatalog.tagTemplates.create`
  * `datacatalog.tagTemplates.delete`
  * `datacatalog.tagTemplates.get`
  * `datacatalog.tagTemplates.getIamPolicy`
  * `datacatalog.tagTemplates.getTag`
  * `datacatalog.tagTemplates.setIamPolicy`
  * `datacatalog.tagTemplates.update`
  * `datacatalog.tagTemplates.use`

`dataplex.aspectTypes.*`

  * `dataplex.aspectTypes.create`
  * `dataplex.aspectTypes.delete`
  * `dataplex.aspectTypes.get`
  * `dataplex.aspectTypes.getIamPolicy`
  * `dataplex.aspectTypes.list`
  * `dataplex.aspectTypes.setIamPolicy`
  * `dataplex.aspectTypes.update`
  * `dataplex.aspectTypes.use`

`dataplex.dataDomains.discover` `dataplex.operations.get` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Catalog TagTemplate User 

(`roles/datacatalog.tagTemplateUser`) Access to apply a tag template to an entry (to modify tags, see Data Catalog Tag Editor) |  `datacatalog.migrationConfig.get` `datacatalog.tagTemplates.get` `datacatalog.tagTemplates.getTag` `datacatalog.tagTemplates.use` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.aspectTypes.use` `dataplex.dataDomains.discover` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Catalog TagTemplate Viewer 

(`roles/datacatalog.tagTemplateViewer`) Read access to templates and tags created using the templates  |  `datacatalog.tagTemplates.get` `datacatalog.tagTemplates.getTag` `dataplex.aspectTypes.get` `dataplex.aspectTypes.list` `dataplex.projects.search` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Data Catalog permissions

Permission | Included in roles  
---|---  
  
#### `datacatalog.catalogs.searchAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.searchAdmin) (`roles/datacatalog.searchAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.categories.fineGrainedGet`

|  [Fine-Grained Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryFineGrainedReader) (`roles/datacatalog.categoryFineGrainedReader`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.categories.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.categories.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.entries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.createGlossary`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.createGlossaryCategory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.createGlossaryTerm`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.deleteGlossary`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.deleteGlossaryCategory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.deleteGlossaryTerm`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.entries.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.entries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.entries.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateContacts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateGlossary`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateGlossaryCategory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateGlossaryTerm`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateOverview`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)   
  
#### `datacatalog.entries.updateTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [Data Catalog Tag Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagEditor) (`roles/datacatalog.tagEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datacatalog.entryGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)   
  
#### `datacatalog.entryGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)   
  
#### `datacatalog.entryGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.entryGroups.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.entryGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog EntryGroup Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupCreator) (`roles/datacatalog.entryGroupCreator`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.entryGroups.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)   
  
#### `datacatalog.entryGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)   
  
#### `datacatalog.entryGroups.updateTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [Data Catalog Tag Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagEditor) (`roles/datacatalog.tagEditor`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `datacatalog.migrationConfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog EntryGroup Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryGroupOwner) (`roles/datacatalog.entryGroupOwner`)  [DataCatalog Entry Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryOwner) (`roles/datacatalog.entryOwner`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [DataCatalog Migration Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.migrationConfigAdmin) (`roles/datacatalog.migrationConfigAdmin`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Dataplex Aspect Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`)  [Dataplex Aspect Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`)  [Dataplex Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)  [Dataplex Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)  [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)  [Dataplex Entry Group Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`)  [Dataplex Entry and EntryLink Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`)  [Dataplex Entry Type Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeOwner) (`roles/dataplex.entryTypeOwner`)  [Dataplex Entry Type User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.migrationConfig.set`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Migration Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.migrationConfigAdmin) (`roles/datacatalog.migrationConfigAdmin`)   
  
#### `datacatalog.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.relationships.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.createBelongsTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.createIsDescribedBy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.createIsRelatedTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.createIsSynonymousTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.deleteBelongsTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.deleteIsDescribedBy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.deleteIsRelatedTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.deleteIsSynonymousTo`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)   
  
#### `datacatalog.relationships.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [DataCatalog Data Steward](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.dataSteward) (`roles/datacatalog.dataSteward`)  [DataCatalog Entry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.entryViewer) (`roles/datacatalog.entryViewer`)  [DataCatalog Glossary Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryOwner) (`roles/datacatalog.glossaryOwner`)  [DataCatalog Glossary User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.glossaryUser) (`roles/datacatalog.glossaryUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.tagTemplates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog TagTemplate Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateCreator) (`roles/datacatalog.tagTemplateCreator`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Data Catalog TagTemplate Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateCreator) (`roles/datacatalog.tagTemplateCreator`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Data Catalog TagTemplate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateViewer) (`roles/datacatalog.tagTemplateViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.getTag`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [Data Catalog TagTemplate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateViewer) (`roles/datacatalog.tagTemplateViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.tagTemplates.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog TagTemplate Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateOwner) (`roles/datacatalog.tagTemplateOwner`)  [Data Catalog TagTemplate User](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.tagTemplateUser) (`roles/datacatalog.tagTemplateUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 

  
  
#### `datacatalog.taxonomies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.taxonomies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.taxonomies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.taxonomies.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datacatalog.taxonomies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Data Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.editor) (`roles/datacatalog.editor`)  [Data Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer) (`roles/datacatalog.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `datacatalog.taxonomies.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)   
  
#### `datacatalog.taxonomies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin) (`roles/datacatalog.admin`)  [Policy Tag Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryAdmin) (`roles/datacatalog.categoryAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
