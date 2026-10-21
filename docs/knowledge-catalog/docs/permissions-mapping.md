---
url: https://docs.cloud.google.com/knowledge-catalog/docs/permissions-mapping/
title: Map IAM permissions between Data Catalog and Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:43.279249+00:00
---

# Map IAM permissions between Data Catalog and Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/permissions-mapping/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Map IAM permissions between Data Catalog and Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

When transitioning from Data Catalog to Knowledge Catalog (formerly Dataplex Universal Catalog), you must update your Identity and Access Management (IAM) policies to ensure consistent access. This document provides a detailed comparison of legacy Data Catalog permissions and their equivalent permissions in Knowledge Catalog. Use these mappings to audit your existing roles or to create new custom roles for metadata management.

For more information, see [Data Catalog permissions](https://docs.cloud.google.com/data-catalog/docs/concepts/iam#predefined_roles) and [Knowledge Catalog permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#catalog-permissions).

## Entry groups

The following table provides a detailed mapping between Data Catalog permissions and Knowledge Catalog permissions for common operations on entry groups:

Operation | Required permissions in Data Catalog | Required permissions in Knowledge Catalog  
---|---|---  
Create entry groups | `datacatalog.entryGroups.create` | `dataplex.entryGroups.create`  
Update entry groups | `datacatalog.entryGroups.update` | `dataplex.entryGroups.update`  
View details of an entry group | `datacatalog.entryGroups.get` | `dataplex.entryGroups.get`  
Delete entry groups | `datacatalog.entryGroups.delete` | `dataplex.entryGroups.delete`  
  
For more information about entry groups, see [entry groups in Data Catalog](https://docs.cloud.google.com/data-catalog/docs/entries-and-entry-groups#entry_groups) and [entry groups in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups).

## Entries

The following table provides a detailed mapping between Data Catalog permissions and Knowledge Catalog permissions for common operations on entries:

Operation | Required permissions in Data Catalog | Required permissions in Knowledge Catalog | Notes  
---|---|---|---  
Create custom entries | `datacatalog.entries.create` | `dataplex.entries.create` `dataplex.entryTypes.use` (to use entry type to create entries of that type) `dataplex.aspectTypes.use` (to use aspect types to create entries with the corresponding aspects) | Data Catalog doesn't have the notion of entry types. In Data Catalog, you can create tags for an entry only after you create the entry. In Knowledge Catalog, you can create aspects for an entry when you create the entry.  
Use reusable system entry types to create entries | Not applicable | Specified permission on the entry group—for example, `dataplex.entryGroups.useENTRY_TYPE` | For more information, see [System aspect types, entry types and entry link types](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#system-aspect-types-entry-types-entry-link-types).  
View details of a custom entry | `datacatalog.entries.get` | `dataplex.entries.get` | -  
View details of a system entry | System-specific permission—for example, `bigquery.tables.get` | `dataplex.entries.get` (for [entries.get](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) method)   
or  
system-specific permission—for example, `bigquery.tables.get` (for [lookupEntry](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntry) method) | In Knowledge Catalog, you can retrieve an entry using the `entries.get` method or `lookupEntry` method. The difference between these methods is the permissions that are required. The Google Cloud console uses the `lookupEntry` method.  
List entries | `datacatalog.entries.list` (for custom entries) | `dataplex.entries.list` (for both system and custom entries) | Data Catalog doesn't support listing system entries. In Knowledge Catalog, system entry groups are valid resources that you can set permissions on.  
Perform a search | No permission required for the search action itself | `dataplex.projects.search` | In Data Catalog, you can perform the search without needing special permissions. To perform the search in Knowledge Catalog, you need the `dataplex.projects.search` permission on the project used to perform the search. This project is set using the `name` parameter in the [searchEntries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) method, while the `scope` parameter defines which projects you're searching within. In both Data Catalog and Knowledge Catalog, the search results are subject to system-specific permission checks. You only see the resources that you're authorized to access. For more information about the permissions required to search for entries in Knowledge Catalog, see [Entries](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#entries).   
Update fields (other than tags and aspects) in custom entries | `datacatalog.entries.update` | `dataplex.entries.update` `dataplex.entryTypes.use` | The `entryTypes.use` permission in Knowledge Catalog protects the non-aspect fields, such as [`entrySource`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#EntrySource). For example, you can use this permission to prevent your users from modifying the fields that are set by a [managed connectivity pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview).   
Set permission on a specific entry instead of an entry group | Generally not supported. However, you can set permission on a specific entry when updating tags for a system entry. This requires permissions on the source system. | Not supported | IAM policies are created only for entry groups. In Data Catalog, when you update tags for a system entry, you need permissions on the source system. For example, when you update tags for a BigQuery table, you need the `bigquery.tables.updateTag` permission. You can set this permission on a specific entry. In Knowledge Catalog, to update aspects for an entry, you need `dataplex.entries.update`, which can't be set on a specific entry.  
Delete entries | `datacatalog.entries.delete` | `dataplex.entries.delete` | -  
  
For more information about entries, see [entries in Data Catalog](https://docs.cloud.google.com/data-catalog/docs/entries-and-entry-groups#entries) and [entries in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries).

## Tag templates and aspect types

The following table provides a detailed mapping between Data Catalog permissions and Knowledge Catalog permissions for common operations on [tag templates](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates#tag-templates) (in Data Catalog) and [aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types) (in Knowledge Catalog).

Operation | Required permissions in Data Catalog | Required permissions in Knowledge Catalog | Notes  
---|---|---|---  
Create tag templates or aspect types | `datacatalog.tagTemplates.create` | `dataplex.aspectTypes.create` | -  
Update tag templates or aspect types | `datacatalog.tagTemplates.update` | `dataplex.aspectTypes.update` | -  
View details of a tag template or an aspect type | `datacatalog.tagTemplates.get` | `dataplex.aspectTypes.get` | -  
List all tag templates or aspect types | Not supported | `dataplex.aspectTypes.list` | Data Catalog doesn't support listing tag templates.  
Use reusable system aspect types | Not applicable | Specified permission on the entry group instead of `dataplex.aspectTypes.use`. For example, `dataplex.entryGroups.useASPECT_TYPE`.  | For more information, see [System aspect types, entry types and entry link types](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#system-aspect-types-entry-types-entry-link-types).   
Delete tag templates or aspect types | `datacatalog.tagTemplates.delete` | `dataplex.aspectTypes.delete` | -  
  
## Tags and aspects

The following table provides a detailed mapping between Data Catalog permissions and Knowledge Catalog permissions for common operations on [tags](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates#tags) (in Data Catalog) and [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) (in Knowledge Catalog).

Operation | Required permissions in Data Catalog | Required permissions in Knowledge Catalog | Notes  
---|---|---|---  
Create, update, and delete tags or aspects | `datacatalog.entries.updateTag`  
or  
service-dependent equivalent—for example, `bigquery.tables.updateTag` `datacatalog.tagTemplates.use` | `dataplex.entries.update` `dataplex.aspectTypes.use` | In Data Catalog, tags are standalone resources from entries. You update tags and entries by using separate methods, and the respective permissions that are required are also separate. In Knowledge Catalog, aspects are stored within entries, not as standalone resources. You update aspects for an entry by updating the entry. This applies to both system and custom entries.  
List tags or aspects | `datacatalog.entries.get` (for both public tags and private tags) `datacatalog.tagTemplates.get` (for each private tag. If you don't have access to a tag, it is omitted in the search results.) | `dataplex.entries.get` |  In Knowledge Catalog, when you retrieve an entry, its aspects are listed too.  
  
## What's next

  * Learn more about [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles) and [permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions).
  * Learn more about [metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
