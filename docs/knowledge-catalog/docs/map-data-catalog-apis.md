---
url: https://docs.cloud.google.com/knowledge-catalog/docs/map-data-catalog-apis/
title: Map Data Catalog API methods to Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:43.221749+00:00
---

# Map Data Catalog API methods to Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/map-data-catalog-apis/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Map Data Catalog API methods to Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Data Catalog is deprecated. If you are migrating programmatic workflows, scripts, client libraries, or Terraform configurations from Data Catalog to Knowledge Catalog, you must update your code to use the Dataplex API.

This document provides a comprehensive mapping of Data Catalog resources, features, and API methods to their equivalents in the Dataplex API.

For the step-by-step migration process, see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog). For API reference documentation, see the [Dataplex API REST documentation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest) and [Dataplex API RPC documentation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc).

## Resource mapping

The following table describes how resources in Data Catalog correspond to resources in Knowledge Catalog:

Data Catalog resource | Knowledge Catalog resource | Description  
---|---|---  
Public tag template | Aspect type (`global`) | Tag templates are regional resources in Data Catalog that can be used across regions. They correspond to `global` aspect types in Knowledge Catalog.  
Public tag | Optional aspect | Public tags correspond to optional aspects attached to an entry or column in Knowledge Catalog.  
Entry group | Entry group | Entry groups serve as organizational and security containers in both services. For Google Cloud sources, system entry groups such as `@bigquery` are established automatically per project.  
Custom entry | Custom entry (with required aspects) | Standard custom entry properties are modeled as required aspects defined by the custom entry's `EntryType`.  
System (Google Cloud) entry | System entry (with required aspects) | Metadata describing built-in entities (such as `Schema` for BigQuery tables) is captured in required aspects of system-defined aspect types.  
Business glossaries | Business glossaries | Taxonomies of business terms standardizing business context across the enterprise.  
  
## Feature comparison

The following table compares the metadata management capabilities of Knowledge Catalog and Data Catalog:

Feature | Knowledge Catalog | Data Catalog  
---|---|---  
Supported Google Cloud sources | All sources described in [Supported Google Cloud sources](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#supported-sources). | All sources described in Data Catalog documentation.  
Custom sources ingestion | Ingestion into custom entries with governed structure defined by entry types. Data Catalog custom entries and entry groups are made available in Knowledge Catalog under the `generic` entry type. | Ingestion into generic custom entries.  
Metadata enrichment | Captured using business glossaries, aspects, and aspect types. Entry links are supported. You can attach aspects directly to entry links. | Captured using business glossaries, tags, and tag templates. Entry links aren't supported.  
Entry links | Supported. Built-in types such as `synonym`, `definition`, `related`, and `schema-join` let you connect entries and columns. | Not available.  
Metadata change feeds | Near-real-time metadata change notifications streamed to Pub/Sub. | Not available.  
Search | Search is performed over all supported Google Cloud sources, custom entries, aspects, and migrated Data Catalog content within the same organization and VPC Service Controls perimeter. | Search is performed over supported sources, custom entries, and tags created in Data Catalog.  
Data lineage | Retrieves entry details for asset nodes using the Dataplex API. Displays attached aspects in the Google Cloud console. | Retrieves entry details using the Data Catalog API.  
Business glossaries | Lets you build taxonomies of business terms and associate them with both data assets (entries) and columns. | Lets you associate terms with columns.  
  
## Map Data Catalog API methods to Knowledge Catalog

The following tables provide a method-by-method mapping between the Data Catalog API (`google.cloud.datacatalog.v1`) and the Dataplex API (`google.cloud.dataplex.v1.CatalogService`).

### Entry groups

The concept of entry groups is consistent across both services:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.entryGroups.create`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create) (REST)  
[`CreateEntryGroup`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.CreateEntryGroup) (RPC) | [`projects.locations.entryGroups.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create) (REST)  
[`CreateEntryGroup`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.CreateEntryGroup) (RPC)  
[`projects.locations.entryGroups.get`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/get) (REST)  
[`GetEntryGroup`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.GetEntryGroup) (RPC) | [`projects.locations.entryGroups.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/get) (REST)  
[`GetEntryGroup`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.GetEntryGroup) (RPC)  
[`projects.locations.entryGroups.patch`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/patch) (REST)  
[`UpdateEntryGroup`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.UpdateEntryGroup) (RPC) | [`projects.locations.entryGroups.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/patch) (REST)  
[`UpdateEntryGroup`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntryGroup) (RPC)  
[`projects.locations.entryGroups.delete`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/delete) (REST)  
[`DeleteEntryGroup`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.DeleteEntryGroup) (RPC) | [`projects.locations.entryGroups.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/delete) (REST)  
[`DeleteEntryGroup`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.DeleteEntryGroup) (RPC)  
[`projects.locations.entryGroups.list`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/list) (REST)  
[`ListEntryGroups`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ListEntryGroups) (RPC) | [`projects.locations.entryGroups.list`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/list) (REST)  
[`ListEntryGroups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.ListEntryGroups) (RPC)  
  
### Entries

The concept of entries, representing data assets, is consistent across both services:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.entryGroups.entries.create`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/create) (REST)  
[`CreateEntry`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.CreateEntry) (RPC) | [`projects.locations.entryGroups.entries.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/create) (REST)  
[`CreateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.CreateEntry) (RPC)  
[`projects.locations.entryGroups.entries.get`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) (REST)  
[`GetEntry`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.GetEntry) (RPC) | [`projects.locations.entryGroups.entries.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) (REST)  
[`GetEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.GetEntry) (RPC)  
[`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.UpdateEntry) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC) **Note:** You can also use the [`projects.locations.modifyEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/modifyEntry) (REST) and [`ModifyEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.ModifyEntry) (RPC) methods to update system entries using source-system permissions instead of catalog permissions.  
[`projects.locations.entryGroups.entries.delete`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/delete) (REST)  
[`DeleteEntry`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.DeleteEntry) (RPC) | [`projects.locations.entryGroups.entries.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/delete) (REST)  
[`DeleteEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.DeleteEntry) (RPC)  
[`projects.locations.entryGroups.entries.list`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/list) (REST)  
[`ListEntries`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ListEntries) (RPC) | [`projects.locations.entryGroups.entries.list`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/list) (REST)  
[`ListEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.ListEntries) (RPC)  
[`entries.lookup`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/entries/lookup) (REST)  
[`LookupEntry`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.LookupEntry) (RPC) | [`projects.locations.lookupEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntry) (REST)  
[`LookupEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.LookupEntry) (RPC) **Note:** To use `lookupEntry`, you must provide the entry name. To translate a BigQuery SQL name, fully qualified name, or linked resource name to an entry name, first call [`projects.locations.searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) (REST) or [`SearchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.SearchEntries) (RPC).  
[`projects.locations.entryGroups.entries.modifyEntryContacts`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/modifyEntryContacts) (REST)  
[`ModifyEntryContacts`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ModifyEntryContacts) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC) **Note:** Use `update_mask` to modify only the `contacts` aspect.  
[`projects.locations.entryGroups.entries.modifyEntryOverview`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/modifyEntryOverview) (REST)  
[`ModifyEntryOverview`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ModifyEntryOverview) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC) **Note:** Use `update_mask` to modify only the `overview` aspect.  
[`projects.locations.entryGroups.entries.tags.reconcile`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/reconcile) (REST)  
[`ReconcileTags`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ReconcileTags) (RPC) | [`projects.locations.metadataJobs.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) (REST)  
[`CreateMetadataJob`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.CreateMetadataJob) (RPC),  
[`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC) **Note:** Use `CreateMetadataJob` with the import job type to import metadata content for multiple entries in batch. To update all aspects for a single entry, use `UpdateEntry`.  
[`catalog.search`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/catalog/search) (REST)  
[`SearchCatalog`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.SearchCatalog) (RPC) | [`projects.locations.searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) (REST)  
[`SearchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.SearchEntries) (RPC) **Note:** `searchEntries` searches within the caller's organization. Cross-organization searches must be issued separately per organization.  
  
### Tag templates and aspect types

Aspect types are the successor to Data Catalog tag templates:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.tagTemplates.create`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create) (REST)  
[`CreateTagTemplate`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.CreateTagTemplate) (RPC) | [`projects.locations.aspectTypes.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/create) (REST)  
[`CreateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.CreateAspectType) (RPC)  
[`projects.locations.tagTemplates.get`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/get) (REST)  
[`GetTagTemplate`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.GetTagTemplate) (RPC) | [`projects.locations.aspectTypes.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/get) (REST)  
[`GetAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.GetAspectType) (RPC)  
[`projects.locations.tagTemplates.patch`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/patch) (REST)  
[`UpdateTagTemplate`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.UpdateTagTemplate) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
[`projects.locations.tagTemplates.delete`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/delete) (REST)  
[`DeleteTagTemplate`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.DeleteTagTemplate) (RPC) | [`projects.locations.aspectTypes.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/delete) (REST)  
[`DeleteAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.DeleteAspectType) (RPC)  
[`catalog.search`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/catalog/search) (REST) with `type=tag_template`  
[`SearchCatalog`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.SearchCatalog) (RPC) with `type=tag_template` | [`projects.locations.aspectTypes.list`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/list) (REST)  
[`ListAspectTypes`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.ListAspectTypes) (RPC)  
  
### Tag template fields

Tag template fields correspond to the contents of the `metadata_template` field in an aspect type. Use `UpdateAspectType` with the modified `metadata_template` to create, update, rename, or delete fields:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.tagTemplates.fields.create`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/create) (REST)  
[`CreateTagTemplateField`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.CreateTagTemplateField) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
[`projects.locations.tagTemplates.fields.patch`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/patch) (REST)  
[`UpdateTagTemplateField`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.UpdateTagTemplateField) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
[`projects.locations.tagTemplates.fields.rename`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/rename) (REST)  
[`RenameTagTemplateField`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.RenameTagTemplateField) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
[`projects.locations.tagTemplates.fields.delete`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/delete) (REST)  
[`DeleteTagTemplateField`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.DeleteTagTemplateField) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
  
### Tag template field enum values

Modify enum values by updating the `metadata_template` field in the corresponding aspect type:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.tagTemplates.fields.enumValues.rename`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields.enumValues/rename) (REST)  
[`RenameTagTemplateFieldEnumValue`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.RenameTagTemplateFieldEnumValue) (RPC) | [`projects.locations.aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) (REST)  
[`UpdateAspectType`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateAspectType) (RPC)  
  
### Tags and aspects

Aspects are the successor to Data Catalog tags. Aspects are encapsulated directly in their parent entries or entry links, and are managed using the `UpdateEntry` method with `update_mask`:

Data Catalog API method | Dataplex API method  
---|---  
[`projects.locations.entryGroups.entries.tags.create`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create) (REST)  
[`CreateTag`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.CreateTag) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC)  
[`projects.locations.entryGroups.entries.tags.list`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/list) (REST)  
[`ListTags`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.ListTags) (RPC) | [`projects.locations.entryGroups.entries.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) (REST)  
[`GetEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.GetEntry) (RPC) **Note:** To filter aspects in the response, use the `views`, `aspect_types`, and `paths` parameters.  
[`projects.locations.entryGroups.entries.tags.patch`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/patch) (REST)  
[`UpdateTag`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.UpdateTag) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC)  
[`projects.locations.entryGroups.entries.tags.delete`](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/delete) (REST)  
[`DeleteTag`](https://docs.cloud.google.com/data-catalog/docs/reference/rpc/google.cloud.datacatalog.v1#google.cloud.datacatalog.v1.DataCatalog.DeleteTag) (RPC) | [`projects.locations.entryGroups.entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) (REST)  
[`UpdateEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.CatalogService.UpdateEntry) (RPC)  
  
### Policy tags and taxonomies

The APIs for policy tags and taxonomies aren't changing and don't require migration. They continue to be served under the `datacatalog.googleapis.com` endpoint (Policy Tag Manager service). The Data Catalog API (`datacatalog.googleapis.com`) must remain enabled in projects that use BigQuery column-level access control or dynamic data masking.

## Features not supported in Knowledge Catalog

The following Data Catalog behaviors and features aren't supported or operate differently in Knowledge Catalog:

  * **Private aspect types** : The concept of private aspects and private aspect types (the counterparts to private tags and private tag templates in Data Catalog) doesn't exist. All custom aspect types are governed by project and entry group Identity and Access Management permissions.
  * **Policy tag search** : Searching for policy tags using the `policytag` or `policytagid` predicates isn't supported in catalog search.
  * **Permissions transfer** : When you import Data Catalog custom entry groups, custom entries, tag templates, and tags into Knowledge Catalog, their original permissions don't carry over. You must [configure IAM permissions](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog#configure-permissions) for the imported resources. For a detailed comparison of legacy and replacement permissions, see [Map IAM permissions between Data Catalog and Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/permissions-mapping).
  * **Sensitive Data Protection inspection results** : Sending Sensitive Data Protection inspection results directly to Knowledge Catalog isn't supported. Instead, send inspection results to Data Catalog and transition the results to Knowledge Catalog.
  * **Cross-project type listing** : Listing entry types, entry link types, and aspect types across projects in a single API call isn't supported; requests must be scoped to a single project.
  * **Administrator search** : Administrator search (full recall) isn't supported. Instead, [export metadata](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata) to Cloud Storage and query it using BigQuery.



## What's next

Guide 

###  [ Transition from Data Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/transition-to-dataplex-catalog)

Step-by-step guide to migrate tag templates, custom entries, and workflows. 

Concept 

###  [ About metadata in Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)

Learn about the Knowledge Catalog flexible metamodel and Active Context Graph. 

Reference 

###  [ Dataplex REST API reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest)

Browse the REST API reference documentation for the Dataplex Catalog service. 

Reference 

###  [ Dataplex RPC API reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc)

Browse the gRPC API reference documentation for the Dataplex Catalog service. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
