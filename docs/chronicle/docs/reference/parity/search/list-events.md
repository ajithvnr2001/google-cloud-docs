---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-events/
title: ListEvents parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:52.579448+00:00
---

# ListEvents parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/list-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListEvents parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`ListEvents`**) to the modern Chronicle API (**`LegacySearchAssetEvents`**).

## Protocol and mapping overview

Feature | Legacy API (`ListEvents`) | Modern Chronicle API (`LegacySearchAssetEvents`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacySearchAssetEvents`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacySearchAssetEventsRequest` scopes searches under target parent instances and replaces standalone timestamp pairs with structured intervals.

Legacy field (`ListEventsRequest`) | Modern field (`LegacySearchAssetEventsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the search query under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`asset` | `asset_indicator` | `AssetIndicator` | **Parity mapped:** Identifies the asset (hostname, IP, or MAC address). Rename to `assetIndicator` in JSON. Note: Proto tag number changed from 4 to 2.  
`start_time` / `end_time` | `time_range` | `Interval` | **Consolidated:** Legacy distinct start and end timestamps are mapped into a single required `google.type.Interval` object (`time_range.start_time` and `time_range.end_time`). Rename to `timeRange` in JSON.  
`reference_time` | `reference_time` | `Timestamp` | **Parity mapped:** Timestamp used to disambiguate dynamic asset indicators (DHCP IPs). Note: Proto tag number changed from 3 to 5. Rename to `referenceTime` in JSON.  
`page_size` | `max_results` | `int32` | **Parity mapped and parameter renaming:** Sets maximum returned events limit (default 10k, max 100k). Rename to `maxResults` in JSON.  
`page_token` | — _(retired)_ | `string` | **Retired:** Token-based pagination is retired in favor of specifying bounding window limits (`max_results`).  
  
* * *

## Response payload field-by-field parity

While the legacy Backstory API returned all events in a single, flat unsegmented array of raw UDM events (`events`), the modern Chronicle API partitions events across domain-specific arrays (`results`, `alerts`, `ip_network_events`, `edr_events`, and `typed_user_events`) and extracts observed hash digests. If your integration previously relied on consuming the combined `events` stream, you must now check and aggregate across these multiple domain fields.

Legacy field (`ListEventsResponse`) | Modern field (`LegacySearchAssetEventsResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`events` _(Flat UDM list)_ | `results` | `repeated SearchResult` | **Partitioned and categorized:** Network events with DNS domain context. Note that the legacy flat `events` list is now partitioned across domain-specific fields (`results`, `alerts`, `ip_network_events`, `edr_events`, and `typed_user_events`); users relying on the combined stream must check all relevant fields.  
`events` _(partitioned)_ | `alerts` | `repeated AssetAlertEvent` | **Partitioned event stream:** Stream of alert events correlated with the asset during the time range. Previously returned in the flat legacy `events` stream.  
`events` _(partitioned)_ | `ip_network_events` | `repeated IpNetworkEvent` | **Partitioned event stream:** Stream of raw IP-to-IP network events lacking DNS domain mappings. Previously returned in the flat legacy `events` stream. Rename to `ipNetworkEvents` in JSON.  
`events` _(partitioned)_ | `edr_events` | `repeated AssetEdrEvent` | **Partitioned event stream:** Stream of endpoint detection and response telemetry. Previously returned in the flat legacy `events` stream. Rename to `edrEvents` in JSON.  
`events` _(partitioned)_ | `typed_user_events` | `repeated UserEvent` | **Partitioned event stream:** Stream of user authentication and activity logs. Previously returned in the flat legacy `events` stream. Rename to `typedUserEvents` in JSON.  
— | `md5_file_hashes` / `sha1_file_hashes` / `sha256_file_hashes` | `repeated string` | **New fields:** Arrays extracting all unique MD5, SHA-1, and SHA256 file hash digests observed within the returned events.  
— | `total_records` | `int64` | **New field:** Total aggregate count of events matching the search query in storage before trimming limits. Rename to `totalRecords` in JSON.  
`more_data_available` | `too_many_results` | `bool` | **Parity mapped and renamed:** Boolean indicator returning true if more events matched than specified by `max_results`. Rename to `tooManyResults` in JSON.  
`uri` | — | `repeated string` | **Retired:** Backstory UI deep link URL arrays are removed from the API response payload.  
  
* * *

## Key differences

  * **Service consolidation and response stream partitioning:**
    * Legacy event listing was housed under `SearchService` (`ListEvents`) and returned a flat unsegmented array of raw UDM events (`events`).
    * Modern Chronicle API standardizes asset event searches under `LegacyEventService` (`LegacySearchAssetEvents`) and partitions the event stream across domain-specific fields: `results` (domain network events), `alerts` (correlated alert events), `ip_network_events` (raw IP-to-IP connections), `edr_events` (EDR telemetry), and `typed_user_events` (user activity).
    * **Action required:** If you previously relied on the single combined `events` array, update your client code to inspect and aggregate across each domain-specific field as needed.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Pagination and truncation handling:**
    * Token-based pagination (`page_token`, `next_page_token`) is retired. Instead, volume is constrained using `max_results` (up to 100k) and truncation is reported using `too_many_results` and `total_records`.
  * **Time window consolidation (Interval):**
    * Standalone timestamp pairs (`start_time`, `end_time`) are structured into standard `google.type.Interval` objects (`time_range`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacySearchAssetEvents`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
