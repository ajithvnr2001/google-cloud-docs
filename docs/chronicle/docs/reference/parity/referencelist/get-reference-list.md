---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/referencelist/get-reference-list/
title: GetReferenceList parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:30.165770+00:00
---

# GetReferenceList parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/referencelist/get-reference-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetReferenceList parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Reference List API (**`GetReferenceList`**) to the modern Chronicle API (**`GetReferenceList`**).

## Protocol and mapping overview

Feature | Legacy API (`GetReferenceList`) | Modern Chronicle API (`GetReferenceList`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/referenceLists.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetReferenceListRequest` identifies target resources using canonical Google Cloud resource paths.

Legacy Field (`GetReferenceListRequest`) | Modern Field (`GetReferenceListRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Renaming:** The legacy request used path format `lists/{list}`. The modern API routes this using canonical Google Cloud resource paths: `projects/{project}/locations/{location}/instances/{instance}/referenceLists/{reference_list}`.  
`view` | `view` | `enum` | **Renamed / Value Alignment:** Selects partial versus full response views. Enum value translations:  
• `REFERENCE_LIST_VIEW_UNSPECIFIED` $\rightarrow$ `REFERENCE_LIST_VIEW_UNSPECIFIED`  
• `BASIC` $\rightarrow$ `REFERENCE_LIST_VIEW_BASIC`  
• `FULL` $\rightarrow$ `REFERENCE_LIST_VIEW_FULL`.  
  
* * *

## Response payload field-by-field parity

Both responses return the retrieved reference list representation, with the modern API enriching return payloads with rule associations and RBAC scopes.

Legacy Field (`ReferenceList` response) | Modern Field (`ReferenceList` response) | Field type | Parity & Migration Notes  
---|---|---|---  
`name` | `name` | `string` | **Parity Mapped:** Contains standard Google Cloud canonical resource path: `projects/{pr}/locations/{loc}/instances/{in}/referenceLists/{id}`.  
— | `display_name` | `string` | **New Field:** The unique display title of the reference list. Rename to `displayName` in JSON responses.  
`description` | `description` | `string` | User-provided description text.  
`lines` | `entries` | `repeated ReferenceListEntry` | **Restructured:** Each item is returned as a `ReferenceListEntry` message containing string `value = 1;` (omitted if view is set to `REFERENCE_LIST_VIEW_BASIC`).  
`content_type` | `syntax_type` | `enum` | **Renamed:** Returns `ReferenceListSyntaxType` enum representing list validation rules (`PLAIN_TEXT_STRING`, `REGEX`, `CIDR`). Rename to `syntaxType` in JSON.  
`create_time` | `revision_create_time` | `Timestamp` | **Renamed:** Timestamp recording when the revision was created. Rename to `revisionCreateTime` in JSON.  
— | `rules` | `repeated string` | **New Field:** Array of self-authored detection rule names associating with this list (omitted in `BASIC` view).  
— | `rule_associations_count` | `int32` | **New Field:** Total count of active self-authored rules referencing this list. Rename to `ruleAssociationsCount` in JSON.  
— | `scope_info` | `ScopeInfo` | **New Field:** Data RBAC scoping boundaries assigned to the list. Rename to `scopeInfo` in JSON.  
  
* * *

## Key differences

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings (`name` path parameter).
  * **Enum Naming Shifts:**
    * The `ReferenceListView` values shift from short prefixes (`BASIC`, `FULL`) to fully qualified names (`REFERENCE_LIST_VIEW_BASIC`, `REFERENCE_LIST_VIEW_FULL`).
    * Legacy `content_type` is renamed to `syntax_type` with clearer enum prefixing (`REFERENCE_LIST_SYNTAX_TYPE_*`).
  * **Payload Restructuring:**
    * Plain string line arrays in legacy `lines` are wrapped inside structured `ReferenceListEntry` messages under `entries` (for example, `lines` $\rightarrow$ `entries`).
  * **Rule Tracking and Scoping Enrichment:**
    * The modern response enriches return payloads with RBAC scoping (`scope_info`) and rule association analytics (`rules` array and `rule_associations_count`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
