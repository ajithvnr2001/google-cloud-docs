---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-user-aliases/
title: ListUserAliases parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:01.853218+00:00
---

# ListUserAliases parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-user-aliases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListUserAliases parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`ListUserAliases`**) to the modern Chronicle API (**`SummarizeEntity`**).

## Protocol and mapping overview

Feature | Legacy API (`ListUserAliases`) | Modern Chronicle API (`SummarizeEntity`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/entities.summarize`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `SummarizeEntityRequest` scopes queries under a target instance and returns time-range entity summary snapshots.

Legacy field (`ListUserAliasesRequest`) | Modern field (`SummarizeEntityRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes entity summary retrieval under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`user` | `entity_id` or `field_and_value` | `oneof id` (`string` or `FieldAndValue`) | **Architectural shift:** Legacy accepted a `UserIndicator` struct. The modern API generalizes lookup by taking either an exact `entity_id` string or a structured `field_and_value` locator (for example, matching an email, username, or employee ID field). Rename to `entityId` or `fieldAndValue` in JSON.  
`start_time` and `end_time` | `time_range` | `Interval` | **Consolidated:** Legacy distinct start and end timestamps map into a single required `google.type.Interval` object (`time_range.start_time` and `time_range.end_time`). Rename to `timeRange` in JSON.  
`page_size` and `page_token` | `page_size` and `page_token` | `int32` and `string` | **Deprecated and retired:** Token-based pagination on entity summaries is deprecated in Chronicle APIs; the backend returns up to 1000 snapshots sorted by time.  
— | `return_prevalence` or `return_alerts` or `include_all_udm_event_types_for_first_last_seen` | `bool` | **New parameters:** Toggles requesting additional intelligence like prevalence metrics (`return_prevalence`), associated alert counts (`return_alerts`), or comprehensive first/last seen calculations across UDM event stores.  
  
* * *

## Response payload field-by-field parity

Both APIs return lists of entity snapshot resources, with the modern Chronicle API enriching return payloads with alert counts, timelines, prevalence, and risk metadata.

Legacy field (`ListUserAliasesResponse`) | Modern field (`SummarizeEntityResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`user_aliases` | `entities` | `repeated Entity` | **Parity mapped and renamed:** Legacy returned repeated `.backstory.Entity` `user_aliases`. The modern API maps these to repeated `Entity` `entities`. Each snapshot captures the full user entity context and alias mapping valid during a specific time slice. Rename to `entities` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Deprecated:** Token-based pagination is deprecated in Chronicle API entity summary responses. Rename to `nextPageToken` in JSON.  
— | `alert_counts` or `has_more_alerts` | `repeated AlertCountByRule` or `bool` | **New fields:** Array reporting rule display names and alert volumes associated with the user entity during the time window, alongside truncation reporting.  
— | `timeline` | `Timeline` | **New field:** Bucketed timeline tracking alert volumes over time.  
— | `prevalence_result` or `tpd_prevalence_result` | `repeated PrevalenceSnapshot` | **New fields:** Historical prevalence statistics tracking observation counts over time for the entity and its top private domain. Rename to `prevalenceResult` and `tpdPrevalenceResult` in JSON.  
— | `asset_prevalence_times` | `repeated Timestamp` | **New field:** Array of specific timestamps when the entity was queried for prevalence analysis. Rename to `assetPrevalenceTimes` in JSON.  
— | `file_metadata_and_properties` or `widget_metadata` or `top_level_domain` | `Message` or `Entity` | **New fields:** Enriches responses with file hash properties, VirusTotal widget data, and top-level domain entity relationships.  
  
### Nested entity property mappings

The fields mapping inside individual returned entity snapshots is as follows:

Legacy field (`.backstory.Entity` item) | Modern field (`Entity` snapshot message) | Field type | Parity and migration notes  
---|---|---|---  
`.backstory.Entity` properties (metadata, attributes, relations) | `Entity` properties (metadata, asset or user attributes, relations) | `Entity` | **Parity mapped:** Identical structured representation of entity metadata and attribute snapshots across time windows. For user entities, `metadata.entity_type` is set to `USER`.  
  
* * *

## Key differences

  * **Service decoupling and architectural unification:**
    * Legacy user alias lookups were a standalone method (`ListUserAliases`) under `SearchService` restricted to user indicators.
    * Modern Chronicle API unifies aliasing, contextual entity histories, prevalence analysis, and alert correlation under `EntityService` (`SummarizeEntity`). A single call returns comprehensive time-sliced `Entity` snapshots covering any arbitrary time range and entity type.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Time window consolidation (Interval):**
    * Standalone timestamp pairs (`start_time`, `end_time`) are structured into standard `google.type.Interval` objects on requests (`time_range`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/entities.summarize`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
