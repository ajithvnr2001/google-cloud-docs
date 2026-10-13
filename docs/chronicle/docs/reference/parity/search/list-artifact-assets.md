---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-artifact-assets/
title: ListArtifactAssets parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:43.088923+00:00
---

# ListArtifactAssets parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-artifact-assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListArtifactAssets parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`ListArtifactAssets`**) to the modern Chronicle API (**`FindRelatedEntities`**).

## Protocol and mapping overview

Feature | Legacy API (`ListArtifactAssets`) | Modern Chronicle API (`FindRelatedEntities`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/entities.findRelatedEntities`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `FindRelatedEntitiesRequest` generalizes graph traversal beyond assets and replaces standalone timestamp pairs with structured intervals.

Legacy field (`ListArtifactAssetsRequest`) | Modern field (`FindRelatedEntitiesRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes entity graph traversal under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`artifact` | `entity_id` / `field_and_value` | `oneof id` (`string` / `FieldAndValue`) | **Architectural shift:** Legacy accepted an `ArtifactIndicator` struct. The modern API generalizes graph traversal by taking either an exact `entity_id` string or a structured `field_and_value` locator (for example, matching a domain name or IP field). Rename to `entityId` or `fieldAndValue` in JSON.  
`start_time` / `end_time` | `time_range` | `Interval` | **Consolidated:** Legacy distinct start and end timestamps are mapped into a single required `google.type.Interval` object (`time_range.start_time` and `time_range.end_time`). Rename to `timeRange` in JSON.  
`page_size` | `limit` | `int32` | **Parity mapped and parameter renaming:** Sets the maximum number of entities returned (max 100). In Chronicle API, the `page_size` field is deprecated and replaced by `limit`.  
`page_token` | — _(deprecated)_ | `string` | **Retired:** Pagination is unsupported for `FindRelatedEntities`; legacy `page_token` is deprecated and ignored.  
— | `entity_types` / `domain_type` | `repeated enum` / `enum` | **New parameters:** Allows filtering returned graph relationships by target `entity_types` (for example, `ASSET`, `USER`) or specifying DNS relationship hierarchy (`domain_type`: `DOMAIN_TYPE_SIBLING`, `DOMAIN_TYPE_SUBDOMAIN`).  
— | `exclude_first_last_seen` / `include_all_udm_event_types_for_first_last_seen` | `bool` / `bool` | **New parameters:** Latency optimization toggles controlling whether to compute first/last seen observation metrics across UDM event stores.  
  
* * *

## Response payload field-by-field parity

While legacy backstory returned asset-specific info structures, the modern API returns generalized `Entity` messages and truncation indicators.

Legacy field (`ListArtifactAssetsResponse`) | Modern field (`FindRelatedEntitiesResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`assets` | `related_entities` | `repeated Entity` | **Parity mapped and generalized:** Legacy returned `AssetFirstLastSeenInfo` structures limited strictly to asset indicators. The modern API returns a repeated list of generalized `Entity` messages (`related_entities`) representing any linked entity graph node (assets, users, domains). Rename to `relatedEntities` in JSON.  
`next_page_token` | — _(deprecated)_ | `string` | **Retired:** Since pagination is disabled for related entity queries, `next_page_token` is deprecated.  
`uri` | — | `repeated string` | **Retired:** Backstory UI deep link URL arrays are removed from the API response payload.  
— | `has_more_entities` | `bool` | **New field:** Boolean indicator returning true if additional related entities exist in the graph but were truncated due to the `limit` threshold. Rename to `hasMoreEntities` in JSON.  
— | `result_time_range` | `Interval` | **New field:** Time window bounding the returned entity relationships. Rename to `resultTimeRange` in JSON.  
  
### Nested entity and asset info property mappings

The fields mapping inside individual `AssetFirstLastSeenInfo` and modern `Entity` returned properties are detailed in the following table:

Legacy field (`AssetFirstLastSeenInfo` message) | Modern field (`Entity` message) | Field type | Parity and migration notes  
---|---|---|---  
`asset` (`AssetIndicator`) | `metadata.entity_type` / `attributes` | `Message` | Mapped into standard Chronicle API `Entity` structures where `metadata.entity_type` is set to `ASSET` (or `USER`, `DOMAIN_NAME`).  
`first_seen_artifact_info` | `first_seen_time` | `Timestamp` | Mapped into first observed timestamps on the returned entity representation.  
`last_seen_artifact_info` | `last_seen_time` | `Timestamp` | Mapped into last observed timestamps on the returned entity representation.  
  
* * *

## Key differences

  * **Service decoupling and graph generalization:**
    * Legacy asset communication queries were housed under `SearchService` (`ListArtifactAssets`) and restricted strictly to asset indicators.
    * Modern Chronicle API generalizes graph traversal under `EntityService` (`FindRelatedEntities`), allowing clients to query any entity type (assets, users, domains, IPs) and filter results by relationship taxonomy (`entity_types`, `domain_type`).
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Pagination and truncation handling:**
    * Pagination (`page_size`, `page_token`, `next_page_token`) is retired and deprecated. Instead, clients control volume using `limit` (max 100) and check truncation status using `has_more_entities`.
  * **Time window consolidation (Interval):**
    * Standalone timestamp pairs are structured into standard `google.type.Interval` objects (`time_range`, `result_time_range`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/entities.findRelatedEntities`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
