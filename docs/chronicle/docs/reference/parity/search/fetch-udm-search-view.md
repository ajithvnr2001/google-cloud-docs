---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/fetch-udm-search-view/
title: FetchUdmSearchView parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:21.153058+00:00
---

# FetchUdmSearchView parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/fetch-udm-search-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FetchUdmSearchView parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`FetchUdmSearchView`**) to the modern Chronicle API (**`LegacyFetchUdmSearchView`**).

## Protocol and mapping overview

Feature | Legacy API (`FetchUdmSearchView`) | Modern Chronicle API (`LegacyFetchUdmSearchView`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacyFetchUdmSearchView`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacyFetchUdmSearchViewRequest` scopes searches under target parent instances and enriches query capabilities.

Legacy field (`FetchUdmSearchViewRequest`) | Modern field (`LegacyFetchUdmSearchViewRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the search query under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`baseline_query` | `baseline_query` | `string` | **Parity mapped:** Boolean structured query string (for example, `metadata.event_type = "NETWORK_CONNECTION"`). Note tag number changed from 1 to 2. Rename to `baselineQuery` in JSON.  
`snapshot_query` | `snapshot_query` | `string` | **Parity mapped:** Query applied to filter baseline events. Note tag number changed from 2 to 3. Rename to `snapshotQuery` in JSON.  
`baseline_time_range` | `baseline_time_range` | `Interval` | **Parity mapped:** Required time interval `[start_time, end_time)`. Note tag number changed from 3 to 4. Rename to `baselineTimeRange` in JSON.  
`snapshot_time_range` | `snapshot_time_range` | `Interval` | **Parity mapped:** Optional filtering interval within baseline bounds. Note tag number changed from 4 to 5. Rename to `snapshotTimeRange` in JSON.  
`event_list` | `event_list` | `UdmEventListOptions` | **Parity mapped:** Options controlling streamed events. Note tag number changed from 5 to 6. Rename to `eventList` in JSON.  
`timeline` | `timeline` | `EventCountTimelineOptions` | **Parity mapped:** Options controlling bucketed timelines. Note tag number changed from 6 to 7.  
`field_aggregations` | `field_aggregations` | `UdmFieldAggregationsOptions` | **Parity mapped:** Options controlling UDM field aggregations. Note tag number changed from 7 to 8. Rename to `fieldAggregations` in JSON.  
`case_insensitive` | `case_insensitive` | `bool` | **Parity mapped:** Case-insensitivity toggle. Note tag number changed from 10 to 13. Rename to `caseInsensitive` in JSON.  
`max_baseline_results` / `aggregations` | — | — | **Retired and shifted:** Legacy `max_baseline_results` and `aggregations` fields are retired from the request message in favor of new options like `detection_options`, `stats_function_parameter`, and `enable_poc_fast_path`.  
— | `detection_options` / `stats_function_parameter` / `user_sql` or others | `Message` / `string` | **New parameters:** Modern requests add support for detection correlation (`detection_options`), statistical functions (`stats_function_parameter`), prevalence options, and raw user SQL execution (`user_sql`).  
  
* * *

## Response payload field-by-field parity

Both APIs stream back query results, with the modern response adding operation tracking and rich entity and statistical aggregations.

Legacy field (`FetchUdmSearchViewResponse`) | Modern field (`LegacyFetchUdmSearchViewResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | `operation` | `string` | **New field:** Slice tracker token. Contains the canonical resource name of the underlying LRO operation: `projects/.../operations/{id}`. Can be passed to `StreamSearchOperation` to re-attach or resume streaming.  
`progress` | `progress` | `double` | **Parity mapped:** Query progress between 0.0 and 1.0.  
`too_many_events` | `too_many_events` | `bool` | **Parity mapped:** Flag indicating event omission due to volume. Rename to `tooManyEvents` in JSON.  
`complete` | `complete` | `bool` | **Parity mapped:** Flag indicating streaming completion.  
`valid_baseline_query` | `valid_baseline_query` | `bool` | **Parity mapped:** Baseline query syntax validity flag. Rename to `validBaselineQuery` in JSON.  
`baseline_events_count` | `baseline_events_count` | `int32` | **Parity mapped:** Count of matched baseline events. Rename to `baselineEventsCount` in JSON.  
`valid_snapshot_query` | `valid_snapshot_query` | `bool` | **Parity mapped:** Snapshot query syntax validity flag. Rename to `validSnapshotQuery` in JSON.  
`query_validation_errors` | `query_validation_errors` | `repeated ErrorMessage` | **Parity mapped:** Array of structured syntax or parse errors. Rename to `queryValidationErrors` in JSON.  
`runtime_errors` | `runtime_errors` | `repeated RuntimeError` | **Parity mapped:** Array of runtime query execution errors. Rename to `runtimeErrors` in JSON.  
`filtered_events_count` | `filtered_events_count` | `int32` | **Parity mapped:** Count of matched snapshot events. Rename to `filteredEventsCount` in JSON.  
`events` | `events` | `UdmEventList` | **Parity mapped:** Streamed list of matched UDM events.  
`timeline` | `timeline` | `EventCountTimeline` | **Parity mapped:** Streamed event count buckets.  
`field_aggregations` / `grouped_field_aggregations` | `field_aggregations` / `grouped_field_aggregations` | `UdmFieldAggregations` | **Parity mapped:** Aggregated UDM field statistics.  
`aggregation_results` | — | — | **Retired and replaced:** Replaced by richer specialized aggregation models (`udm_entity_field_aggregations`, `datatable_aggregations`, `join_aggregations`, and `prevalence`).  
— | `available_result_count` / `detections` / `prevalence` or others | `int32` / `Message` | **New fields:** Adds total un-paginated result counts (`available_result_count`), correlated detections (`detections`), statistical responses, and prevalence analysis.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Operation resource tracking:**
    * The modern response includes `operation` (`projects/.../operations/{id}`), allowing clients to reconnect to in-progress searches or fetch stored results using `StreamSearchOperation`.
  * **Proto tag shifts and parameter evolution:**
    * Within protobuf formatting, tag numbers for core query parameters shifted by +1 (for example, `baseline_query` shifted from tag 1 to 2; `baseline_time_range` from tag 3 to 4).
    * Legacy `max_baseline_results` and `aggregations` are retired, replaced by advanced entity aggregations, SQL query modes (`user_sql`), and statistical functions.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacyFetchUdmSearchView`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
