---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-aliases/
title: ListAliases parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:42.051994+00:00
---

# ListAliases parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-aliases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListAliases parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`ListAliases`**) to the modern Chronicle API (**`SummarizeEntity`**).

## Protocol and mapping overview

Feature | Legacy API (`ListAliases`) | Modern Chronicle API (`SummarizeEntity`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/entities.summarize`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `SummarizeEntityRequest` replaces single-day alias lookups with flexible time-range entity summary snapshots under a target instance.

Legacy field (`ListAliasesRequest`) | Modern field (`SummarizeEntityRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes entity summary retrieval under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`asset` | `entity_id` or `field_and_value` | `oneof id` (`string` or `FieldAndValue`) | **Architectural shift:** Legacy accepted an `AssetIndicator` struct. The modern API generalizes lookup by taking either an exact `entity_id` string or a structured `field_and_value` locator (for example, matching an IP, hostname, or MAC). Rename to `entityId` or `fieldAndValue` in JSON.  
`day` | `time_range` | `Timestamp` $\rightarrow$ `Interval` | **Consolidated and expanded:** Legacy restricted alias resolution to a specific 24-hour timestamp day (`day`). The modern API accepts a flexible time window bounding interval (`time_range.start_time` and `time_range.end_time`). Rename to `timeRange` in JSON.  
`page_size` and `page_token` | `page_size` and `page_token` | `int32` and `string` | **Deprecated and retired:** Token-based pagination on entity summaries is deprecated in Chronicle APIs; the backend returns up to 1000 snapshots sorted by time.  
— | `return_prevalence` or `return_alerts` or `include_all_udm_event_types_for_first_last_seen` | `bool` | **New parameters:** Toggles requesting additional intelligence like prevalence metrics (`return_prevalence`), associated alert counts (`return_alerts`), or comprehensive first/last seen calculations across UDM event stores.  
  
* * *

## Response payload field-by-field parity

In legacy backstory, `ListAliasesResponse` returned plain `AssetAlias` records containing raw IP or hostname strings. In Chronicle API workflows, `SummarizeEntityResponse` returns comprehensive `Entity` snapshot objects enriched with alerts, prevalence, and risk metadata.

Legacy field (`ListAliasesResponse`) | Modern field (`SummarizeEntityResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`asset_aliases` | `entities` | `repeated Entity` | **Parity mapped and enriched:** Legacy returned `AssetAlias` items. The modern API maps these to repeated `Entity` snapshots (`entities`). Each snapshot captures the full asset alias mapping (hostnames, IPs, MACs, product IDs) valid during a specific time slice. Rename to `entities` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Deprecated:** Token-based pagination is deprecated in Chronicle API entity summary responses. Rename to `nextPageToken` in JSON.  
`uri` | — | `repeated string` | **Retired:** Backstory UI deep link URL arrays are removed from the API response payload.  
— | `alert_counts` or `has_more_alerts` | `repeated AlertCountByRule` or `bool` | **New fields:** Array reporting rule display names and alert volumes associated with the entity during the time window, alongside truncation reporting.  
— | `timeline` | `Timeline` | **New field:** Bucketed timeline tracking alert volumes over time.  
— | `prevalence_result` or `tpd_prevalence_result` | `repeated PrevalenceSnapshot` | **New fields:** Historical prevalence statistics tracking observation counts over time for the entity and its top private domain. Rename to `prevalenceResult` and `tpdPrevalenceResult` in JSON.  
— | `asset_prevalence_times` | `repeated Timestamp` | **New field:** Array of specific timestamps when the asset was queried for prevalence analysis. Rename to `assetPrevalenceTimes` in JSON.  
— | `file_metadata_and_properties` or `widget_metadata` or `top_level_domain` | `Message` or `Entity` | **New fields:** Enriches responses with file hash properties, VirusTotal widget data, and top-level domain entity relationships.  
  
### Nested alias and entity attribute mappings

The fields mapping inside individual returned alias snapshots is as follows:

Legacy field (`AssetAlias` message) | Modern field (`Entity` snapshot message) | Field type | Parity and migration notes  
---|---|---|---  
`hostname` | `entity.metadata.vendor_name` or asset attributes | `string` | Mapped into standard asset properties inside the returned `Entity` snapshot.  
`ip_address` | `entity.metadata.vendor_name` or asset attributes | `string` | Mapped into IP address attributes inside the returned `Entity` snapshot.  
`mac` | `entity.metadata.vendor_name` or asset attributes | `string` | Mapped into MAC address attributes inside the returned `Entity` snapshot.  
`product_id` | `entity.metadata.product_specific_id` | `string` | Mapped into product-specific identifier fields on the entity metadata block.  
`start_time` | `entity.metadata.interval.start_time` | `Timestamp` | Mapped into the starting boundary of the snapshot validity window.  
`end_time` | `entity.metadata.interval.end_time` | `Timestamp` | Mapped into the ending boundary of the snapshot validity window.  
  
* * *

## Key differences

  * **Service decoupling and architectural unification:**
    * Legacy alias resolution was a standalone method (`ListAliases`) under `SearchService` restricted to returning basic hostname, IP or MAC strings for a single day.
    * Modern Chronicle API unifies aliasing, contextual entity histories, prevalence analysis, and alert correlation under `EntityService` (`SummarizeEntity`). A single call returns comprehensive time-sliced `Entity` snapshots covering any arbitrary time range.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Time window consolidation (Interval):**
    * Standalone single-day timestamps (`day`) and alias validity ranges (`start_time`, `end_time`) are structured into standard `google.type.Interval` objects on requests (`time_range`) and returned entity snapshots (`metadata.interval`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/entities.summarize`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
