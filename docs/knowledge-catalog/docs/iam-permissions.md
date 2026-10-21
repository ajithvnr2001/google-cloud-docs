---
url: https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions/
title: Knowledge Catalog IAM permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:05.179578+00:00
---

# Knowledge Catalog IAM permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Knowledge Catalog IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a reference of Identity and Access Management (IAM) permissions for Knowledge Catalog resources. Use these permissions to create custom roles or to verify the granular access required for metadata management, data scans, lake operations, tasks, and environments.

## Permissions and roles

You don't directly grant users permissions. Instead, you grant them roles, which have one or more permissions within them. This approach aligns with the principle of least privilege, encouraging you to grant only the necessary access required for a user or service account to perform its tasks.

IAM offers predefined roles for common use cases. If these predefined roles don't meet your specific needs, you can create your own custom roles containing only the specific permissions required.

For more information about predefined Knowledge Catalog roles and the permissions they contain, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

For a detailed description of IAM and its features, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

## IAM policy Set and Get permissions

The following table lists the permissions required to get and set IAM permissions:

Resource | API method | IAM permission  
---|---|---  
Aspect types | [`GetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/getIamPolicy) | dataplex.aspectTypes.getIamPolicy  
Aspect types | [`SetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/setIamPolicy) | dataplex.aspectTypes.setIamPolicy  
Entry groups | [`GetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/getIamPolicy) | dataplex.entryGroups.getIamPolicy  
Entry groups | [`SetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/setIamPolicy) | dataplex.entryGroups.setIamPolicy  
Entry types | [`GetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/getIamPolicy) | dataplex.entryTypes.getIamPolicy  
Entry types | [`SetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/setIamPolicy) | dataplex.entryTypes.setIamPolicy  
Lakes | [`GetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/getIamPolicy) | dataplex.lakes.getIamPolicy  
Lakes | [`SetIamPolicy`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/setIamPolicy) | dataplex.lakes.setIamPolicy  
  
## Metadata management permissions

The set of permissions that is required to perform operations on entry types, entry link types, aspect types, entry groups, entries, and entry links depends on whether the resources are system resources or custom resources. System resources are defined by Knowledge Catalog, and custom resources are defined by you or your organization.

**Note:** Only system entry link types are supported.

To enrich entries and entry links with additional information, you can attach aspects.

To perform operations that are related to multiple resources (for example, creating an entry of a particular entry type, or adding an aspect of a particular aspect type to an entry or entry link), you might need multiple permissions associated with the resources.

### Entry types

To create and manage entry types, you must be granted at least the standard `create`, `get`, `list`, `update`, and `delete` permissions.

When you create an entry type, you must be granted permissions to use each aspect type you want to mark as required for that entry type.

To use an entry type (for example, to create entries of an entry type), you must be granted the `use` permission on the entry type.

The following table lists the permissions required for operating on entry types:

Operation | IAM permission  
---|---  
[`Create entry types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/create) |  `dataplex.entryTypes.create` `dataplex.aspectTypes.use` (for every required aspect type in the entry type) `dataplex.entryGroups.useASPECT_TYPE` (for every required system aspect type in the entry type). See the permissions for system aspect types.  
[`Delete entry types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/delete) |  `dataplex.entryTypes.delete` `dataplex.aspectTypes.use` (for required aspect types in the entry types) `dataplex.entryGroups.useASPECT_TYPE` (for every required system aspect type in the entry type). See the permissions for system aspect types.  
[`Get entry types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/get) | `dataplex.entryTypes.get`  
[`List entry types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/list) | `dataplex.entryTypes.list`  
[`Update entry types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryTypes/patch) |  `dataplex.entryTypes.update` `dataplex.aspectTypes.use` (for every required aspect type in the entry type) `dataplex.entryGroups.useASPECT_TYPE` (for every required system aspect type in the entry type). See the permissions for system aspect types.  
Use entry types (when creating entries, updating top-level entry fields and required aspect type values) |  `dataplex.entryTypes.use` `dataplex.entries.create` or `dataplex.entries.update` `dataplex.aspectTypes.use` (for every aspect created or updated)  
  
### Aspect types

To create and manage aspect types, you must be granted the standard `create`, `get`, `list`, `update`, and `delete` permissions.

To use an aspect type (for example, to attach it as an optional aspect on an entry or update required aspect on the entry link), you must be granted the `use` permission on the aspect type.

Aspect types are categorized into system aspect types and custom aspect types. System aspect types are created by Knowledge Catalog and custom aspect types are created by you or your organization. System aspect types are further categorized into usable and read-only. For more information, see [Categories of aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#categories-aspect-types).

The following table lists the permissions required for operating on custom and system aspect types:

Operation | Permissions required for custom aspect types | Permissions required for usable system aspect types | Permissions required for read-only system aspect types  
---|---|---|---  
[`Create aspect types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/create) | `dataplex.aspectTypes.create` | Not applicable | Not applicable  
[`Delete aspect types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/delete) | `dataplex.aspectTypes.delete` | Not applicable | Not applicable  
[`Get aspect types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/get) | `dataplex.aspectTypes.get` | Granted to `allUsers` | Granted to `allUsers`  
[`List aspect types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/list) | `dataplex.aspectTypes.list` | Not applicable | Not applicable  
When creating or updating entries, set optional aspect type values |  `dataplex.aspectTypes.use` `dataplex.entries.create` or `dataplex.entries.update` |  `dataplex.entryGroups.useASPECT_TYPE`. See the permissions for system aspect types. `dataplex.entries.create` or `dataplex.entries.update` | Not applicable  
When creating or updating entries, set required aspect type values |  `dataplex.aspectTypes.use` `dataplex.entryTypes.use` `dataplex.entries.create` or `dataplex.entries.update` |  `dataplex.entryGroups.useASPECT_TYPE`. See the permissions for system aspect types. `dataplex.entryTypes.use` `dataplex.entries.create` or `dataplex.entries.update` | Not applicable  
[`Update aspect types`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) | `dataplex.aspectTypes.update` | N/A | N/A  
Set required aspect type values when creating or updating entry link | N/A |  `dataplex.entryGroups.useASPECT_TYPE`. See the permissions for system aspect types. `dataplex.entryLinkTypes.useENTRY_LINK_TYPE`. See the permissions for system entry link types. `dataplex.entries.link` Granted on entry group(s) containing linked entries. Only checked during entry link creation. `dataplex.entryLinks.create` or `dataplex.entryLinks.update` | N/A  
  
### Entry groups

To create and manage entry groups, you must be granted the standard `create`, `get`, `list`, `update`, and `delete` permissions.

**Note:** You can't modify or delete the system entry groups whose names start with the `@` symbol, such as `@bigquery`. You can only add optional aspects to the entries in such entry groups.

Entry groups are categorized into system entry groups, which are created by Knowledge Catalog, and custom entry groups, which are created by you or your organization. For more information, see [Categories of entry groups](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#categories-entry-groups).

The following table lists the permissions required for operating on entry groups:

Operation | Permissions required for custom entry groups | Permissions required for system entry groups (starting with @)  
---|---|---  
[`Create entry groups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create) | `dataplex.entryGroups.create` | Not applicable  
[`Delete entry groups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/delete) | `dataplex.entryGroups.delete` | Not applicable  
[`Get entry groups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/get) | `dataplex.entryGroups.get` | `dataplex.entryGroups.get`  
[`List entry groups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/list) | `dataplex.entryGroups.list` | `dataplex.entryGroups.list`  
[`Update entry groups`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups/patch) | `dataplex.entryGroups.update` | Not applicable  
  
### Entries

To create and manage entries, you must be granted the standard `create`, `get`, `list`, `update`, and `delete` permissions.

Note the following:

  * For lookup (`<code>LookupEntry</code>`) and search (`<code>SearchEntries</code>`) methods, the permission from the original source system is required on the entry. For example, if the source is a BigQuery table, you need `bigquery.tables.get` permission to view metadata, and `bigquery.tables.getData` to view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects).
  * If permission to view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects) is not present, entries are still visible, but the contents of data aspects are hidden.
  * When you create an entry or update the top-level fields of an entry, you must be granted the `use` permission on the entry type.
  * When you create or update a required aspect, you must be granted the `use` permission on the entry type of an entry, as well as on the underlying aspect type. This is because the required aspects are enforced by the entry type.
  * When you create, update, or delete an optional aspect, you must be granted the `use` permission on the aspect type of an aspect.
  * When you upsert an entry (`<code>UpdateEntry</code>` with `<code>allow_missing = True</code>`), you must be granted the `create` permission.



For more information about the entry types entries are based on, see [Categories of entry types](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#categories-entry-types).

The following table lists the permissions required for operating on entries:

Operation | Entry based on custom entry type | Entry based on usable system entry type | Entry based on read-only system entry type  
---|---|---|---  
[`Create entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/create) |  `dataplex.entries.create` `dataplex.entryTypes.use` `dataplex.aspectTypes.use` (for every custom aspect created) `dataplex.entryGroups.useASPECT_TYPE` (for every aspect of a usable system aspect type created). See the permissions for system aspect types. |  `dataplex.entries.create` `dataplex.entryGroups.useENTRY_TYPE`. See the permissions for system entry types. `dataplex.entryGroups.useASPECT_TYPE` (for every system aspect created). See the permissions for system aspect types. `dataplex.aspectTypes.use` (for every custom aspect created) | Not applicable  
[`Get entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) | `dataplex.entries.get` To view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects), `dataplex.entries.getData` is also required. | `dataplex.entries.get` To view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects), `dataplex.entries.getData` is also required. | `dataplex.entries.get` To view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects), `dataplex.entries.getData` is also required.  
[`List entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/list) | `dataplex.entries.list` | `dataplex.entries.list` | `dataplex.entries.list`  
[`Lookup entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntry) |  Requires metadata read permission of the source system. Permission to read data from the source system is required to view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects). For custom entries, where Knowledge Catalog is treated as the source system, these permissions are `dataplex.entries.get` and `dataplex.entries.getData`, respectively. |  Requires metadata read permission of the source system. Permission to read data from the source system is required to view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects). For custom entries, where Knowledge Catalog is treated as the source system, these permissions are `dataplex.entries.get` and `dataplex.entries.getData`, respectively. |  Requires metadata read permission of the source system. Permission to read data from the source system is required to view [data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects). For custom entries, where Knowledge Catalog is treated as the source system, these permissions are `dataplex.entries.get` and `dataplex.entries.getData`, respectively.  
[`Search entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) |  Read permission of the original source system. For custom entries, this is `dataplex.entries.get`, because Knowledge Catalog is treated as the original source system. |  Read permission of the original source system. For custom entries, this is `dataplex.entries.get`, because Knowledge Catalog is treated as the original source system. |  Read permission of the original source system. For custom entries, this is `dataplex.entries.get`, because Knowledge Catalog is treated as the original source system.  
[`Update entries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) |  `dataplex.entries.update` `dataplex.entryTypes.use` (for updating top-level fields or required aspects) `dataplex.aspectTypes.use` (for every aspect updated) `dataplex.entryGroups.useASPECT_TYPE` (for every system aspect updated). See the permissions for system aspect types. `dataplex.entries.create` (if `allow_missing` is `True`) |  `dataplex.entries.update` `dataplex.entryGroups.useENTRY_TYPE` (for updating top-level fields or required aspects). See the permissions for system entry types. `dataplex.aspectTypes.use` (for every custom aspect updated) `dataplex.entryGroups.useASPECT_TYPE` (for every aspect that belongs to system aspect types). See the permissions for system aspect types. `dataplex.entries.create` (if `allow_missing` is `True`) |  `dataplex.entries.update` `dataplex.aspectTypes.use` (for every custom aspect updated) `dataplex.entryGroups.useASPECT_TYPE` (for every aspect of a usable system aspect type updated). See the permissions for system aspect types. Top-level fields and required aspects can't be edited.  
  
### Entry Links

To create and manage entry links, you must be granted `create`, `get`, `list`, and `delete` permissions on `dataplex.entryLinks`.

Note the following:

  * Creating entry links (`CreateEntryLink`) also requires permissions on the entry link type and permissions to the link specific entries.
  * When creating an entry link with a _required_ aspect, you need the permissions to use the aspect type.
  * When upserting an entry link (`UpdateEntryLink` with `allow_missing = True`), you must also have the same permissions required for `CreateEntryLink`.



The following table lists the permissions required for operating on entry links:

Operation | IAM permission  
---|---  
[Create entry links](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/create) |  `dataplex.entryLinks.create` (on the entry group) Permissions required based on **Entry Link Type** :

  * **Synonym:** `dataplex.glossaryTerms.use` (on both term entries)
  * **Definition:** `dataplex.glossaryTerms.use` (on the term entry) and `dataplex.entries.link` (on the target entry)
  * **Other:** `dataplex.entries.link` (on both entries)

Permission to use the entry link type:

  * For system types: `dataplex.entryGroups.useENTRY_LINK_TYPE` (on the entry group). See the permissions for system entry link types.

Permissions for any required aspects specified by the entry link type:

  * For system types: `dataplex.entryGroups.useASPECT_TYPE` (on the entry group). See the permissions for system aspect types.

  
[Delete entry links](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/delete) | `dataplex.entryLinks.delete` (on the entry group)  
[Get entry links](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/get) |  `dataplex.entryLinks.get` (on the entry group)  
[Lookup entry links](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntryLinks) |  Requires metadata read permission of the source system on the entry for which entry links are looked up for. For linked custom entries, where Knowledge Catalog is treated as the source system, the permissions is `dataplex.entries.get`. For linked system entries, the permission is read permission of the source system of the linked entry.  
[Update entry link](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/patch) |  `dataplex.entryLinks.update` (on the entry group) Permission to use the entry link type:

  * For system types: `dataplex.entryGroups.useENTRY_LINK_TYPE` (on the entry group). See the permissions for system entry link types.

Permissions for any required aspects specified by the entry link type:

  * For system types: `dataplex.entryGroups.useASPECT_TYPE` (on the entry group). See the permissions for system aspect types.

If `allow_missing` is `True`, additionally, all permissions from `Create entry link` apply.  
  
#### Limitations for Aspects on Entry Links

The following [limitations](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#create-aspects-for-entry-links) apply to using aspects with entry links.

### Context sets

Context sets contain database-specific information, such as SQL query templates, [faceted search queries](https://en.wikipedia.org/wiki/Faceted_search), and value search queries. The context engineering agent uses context sets to build, evaluate, and optimize text-to-SQL translations. QueryData is a conversational query tool that uses context sets to translate natural language into database queries when you build [data agents](https://docs.cloud.google.com/gemini/data-agents).

For more information, see the context sets overview for [AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/querydata/alloydb/context-sets-overview), [Cloud SQL for MySQL](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/context-sets-overview), [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/context-sets-overview), or [Spanner](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/context-sets-overview).

To create and manage context sets for AI grounding, you must be granted the following IAM roles:

  * **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`): Read-only access to view, list, and download context sets, and to view locations.
  * **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`): Access to create, update, delete, upload, and download context sets.
  * **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`): Full administrative access to context sets.



For more information, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

### Metadata job permissions

The following table lists the permissions required for working with [metadata import jobs](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata) and [metadata export jobs](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata).

Operation | IAM permission  
---|---  
Access the exported results from metadata export jobs |  `storage.objects.get`  
[`Cancel metadata jobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/cancel) |  `dataplex.metadataJobs.cancel`  
[`Create metadata export jobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) |  `dataplex.metadataJobs.create` `dataplex.entryGroups.export` `dataplex.entryGroups.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
[`Create metadata import jobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) |  `dataplex.metadataJobs.create` `dataplex.entryTypes.use` (for custom entry types in the job's scope) `dataplex.entryTypes.useENTRY_TYPE` (for every system entry type in the job's scope). See the permissions for system entry types. However, this permission isn't needed to modify optional aspects when running an aspect-only metadata import job. `dataplex.aspectTypes.use` (for custom aspect types in the job's scope) `dataplex.aspectTypes.useASPECT_TYPE` (for every system aspect type in the job's scope). See the permissions for system aspect types. `dataplex.entryGroups.import` (for entry groups in the job's scope)  
[`Get metadata jobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get) |  `dataplex.metadataJobs.get`  
[`List metadata jobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/list) |  `dataplex.metadataJobs.list`  
  
### System aspect types, entry types, and entry link types

Each system-defined aspect type, system-defined entry type and system-defined entry link type has its own IAM permissions. These permissions use a format like `dataplex.entryGroups.useASPECT_TYPE`, `dataplex.entryGroups.useENTRY_TYPE` or `dataplex.entryGroups.useENTRY_LINK_TYPE`. For example, the permission for the `overview` system aspect type is `dataplex.entryGroups.useOverviewAspect`.

The following table lists the permissions that apply to system-defined aspect types, entry types and entry link types.

Resource | IAM permission  
---|---  
`contacts` (system aspect type) | `dataplex.entryGroups.useContactsAspect`  
`data-profile` (system aspect type) | `dataplex.entryGroups.useDataProfileAspect`  
`data-quality-rule-template` (system aspect type) | `dataplex.entryGroups.useDataQualityRuleTemplateAspect`  
`data-quality-scorecard` (system aspect type) | `dataplex.entryGroups.useDataQualityScorecardAspect`  
`data-rules` (system aspect type) | `dataplex.entryGroups.useDataRulesAspect`  
`generic` (system aspect type) | `dataplex.entryGroups.useGenericAspect`  
`guidelines` (system aspect type) | `dataplex.entryGroups.useGuidelinesAspect`  
`overview` (system aspect type) | `dataplex.entryGroups.useOverviewAspect`  
`schema` (system aspect type) | `dataplex.entryGroups.useSchemaAspect`  
`schema-join` (system aspect type) | `dataplex.entryGroups.useSchemaJoinAspect`  
`generic` (system entry type) | `dataplex.entryGroups.useGenericEntry`  
`definition` (system entry link type) | `dataplex.entryGroups.useDefinitionEntryLink`  
`related` (system entry link type) | `dataplex.entryGroups.useRelatedEntryLink`  
`synonym` (system entry link type) | `dataplex.entryGroups.useSynonymEntryLink`  
`schema-join` (system entry link type) | `dataplex.entryGroups.useSchemaJoinEntryLink`  
  
## Lake, zone, and asset permissions

The following table lists the permissions required for operating on lakes, zones, and assets:

API method | IAM permission  
---|---  
[`CreateAsset`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets/create) | dataplex.assets.create  
[`CreateLake`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/create) | dataplex.lakes.create  
[`CreateZone`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/create) | dataplex.zones.create  
[`DeleteAsset`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets/delete) | dataplex.assets.delete  
[`DeleteLake`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/delete) | dataplex.lakes.delete  
[`DeleteZone`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/delete) | dataplex.zones.delete  
[`GetAsset`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets/get) | dataplex.assets.get  
[`GetLake`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/get) | dataplex.lakes.get  
[`GetZone`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/get) | dataplex.zones.get  
[`ListAssetActions`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets.actions/list) | dataplex.assetActions.list  
[`ListAssets`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets/list) | dataplex.assets.list  
[`ListLakeActions`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.actions/list) | dataplex.lakeActions.list  
[`ListLakes`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/list) | dataplex.lakes.list  
[`ListZoneActions`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.actions/list) | dataplex.zoneActions.list  
[`ListZones`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/list) | dataplex.zones.list  
[`UpdateAsset`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets/patch) | dataplex.assets.update  
[`UpdateLake`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes/patch) | dataplex.lakes.update  
[`UpdateZone`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/patch) | dataplex.zones.update  
  
## Task permissions

The following table lists the permissions required for operating on tasks:

API method | IAM permission  
---|---  
[`CancelJob`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks.jobs/cancel) | dataplex.tasks.cancel  
[`CreateTask`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks/create) | dataplex.tasks.create  
[`DeleteTask`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks/delete) | dataplex.tasks.delete  
[`GetJob`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks.jobs/get) | dataplex.tasks.get  
[`GetTask`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks/get) | dataplex.tasks.get  
[`ListJobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks.jobs/list) | dataplex.tasks.get  
[`ListTasks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks/list) | dataplex.tasks.list  
[`UpdateTask`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.tasks/patch) | dataplex.tasks.update  
  
## Metadata permissions

The following table lists the permissions required for operating on entities and partitions:

API method | IAM permission  
---|---  
[`CreateEntity`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities/create) | dataplex.entities.create  
[`CreatePartition`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities.partitions/create) | dataplex.partitions.create  
[`DeleteEntity`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities/delete) | dataplex.entities.delete  
[`DeletePartition`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities.partitions/delete) | dataplex.partitions.delete  
[`GetEntity`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities/get) | dataplex.entities.get  
[`GetPartition`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities.partitions/get) | dataplex.partitions.get  
[`ListEntities`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities/list) | dataplex.entities.list  
[`ListPartitions`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.entities.partitions/list) | dataplex.partitions.list  
  
## Data scan permissions

The following table lists the permissions required for operating on data scans:

API method | IAM permission  
---|---  
[`CancelDataScanJob`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/cancel) | dataplex.datascans.cancel  
[`CreateDataScan`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/create) | dataplex.datascans.create  
[`DeleteDataScan`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/delete) | dataplex.datascans.delete  
[`GetDataScan` (basic view)](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/get) | dataplex.datascans.get  
[`GetDataScan` (full view)](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/get) | dataplex.datascans.getData  
[`GetDataScanJob` (basic view)](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/get) | dataplex.datascans.get  
[`GetDataScanJob` (full view)](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/get) | dataplex.datascans.getData  
[`ListDataScanJobs`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/list) | dataplex.datascans.get  
[`ListDataScans`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/list) | dataplex.datascans.list  
[`RunDataScan`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/run) | dataplex.datascans.run  
[`UpdateDataScan`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/patch) | dataplex.datascans.update  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
