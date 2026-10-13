---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/list-detections/
title: ListDetections (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:50.110566+00:00
---

# ListDetections (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/list-detections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListDetections (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`ListDetections`**) to the modern Chronicle API (**`LegacySearchDetections`**).

## Protocol and mapping overview

Feature | Legacy API (`ListDetections` V2) | Modern Chronicle API (`LegacySearchDetections`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacySearchDetections`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacySearchDetectionsRequest` scopes search queries under parent project instances and renames bounding range timestamps.

Legacy field (`ListDetectionsRequest`) | Modern field (`LegacySearchDetectionsRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes structural queries under target instance environments: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`version_id` | `rule_id` | `string` | **Renamed:** Target rule identification path parameter segment name (can accept `{rule_id}`, `{rule_id}@{version_ts}`, `{rule_id}@*`, or `*`). Rename to `ruleId` in JSON. Note: Proto tag number changed from 1 to 2.  
`alert_state` | `alert_state` | `enum` | **Direct map / identical:** Alert state filter (`SecurityResult.AlertState` enum: `ALERTING`, `NOT_ALERTING`). Rename to `alertState` in JSON. Note: Proto tag number changed from 2 to 3.  
`start_time` / `detection_start_time` | `start_time` | `Timestamp` | **Consolidated / tag shift:** Legacy separate start time parameters are unified into `start_time`. Note: Proto tag number changed to 4. Rename to `startTime` in JSON.  
`end_time` / `detection_end_time` | `end_time` | `Timestamp` | **Consolidated / tag shift:** Legacy separate end time parameters are unified into `end_time`. Note: Proto tag number changed to 5. Rename to `endTime` in JSON.  
`list_basis` | `list_basis` | `enum` | **Direct map:** Selection metric used for filtering timestamps (`DETECTION_TIME` versus `CREATED_TIME`). Note: Proto tag number changed from 9 to 6. Rename to `listBasis` in JSON.  
`page_size` | `page_size` | `int32` | **Direct map:** Pagination window size limits. Note: Proto tag number changed from 5 to 7. Rename to `pageSize` in JSON.  
`page_token` | `page_token` | `string` | **Direct map:** Pagination resumption token. Note: Proto tag number changed from 6 to 8. Rename to `pageToken` in JSON.  
`include_simulated_detections` | `include_simulated_detections` or `simulated_data_visibility` | `bool` or `enum` | **Direct map / enriched:** Allows specifying simulated detection visibility. Note: Proto tag number changed from 10 to 11 and 12.  
— | `max_resp_size_bytes` | `int32` | **New field:** Restricts response size in bytes to prevent large message serialization heap overflows. Rename to `maxRespSizeBytes` in JSON.  
— | `include_nested_detections` | `bool` | **New field:** Toggles whether to recursively nest dependent children detections in output streams. Rename to `includeNestedDetections` in JSON.  
  
* * *

## Response payload field-by-field parity

The response returns repeated detections or nested detection structures depending on whether nesting query filters are enabled in requests.

Legacy field (`ListDetectionsResponse`) | Modern field (`LegacySearchDetectionsResponse`) | Field type | Parity & migration notes  
---|---|---|---  
`detections` | `detections` | `repeated Collection` | **Direct map:** Array list of matched detections (represented as `backstory.Collection` messages).  
`next_page_token` | `next_page_token` | `string` | **Direct map:** Token to retrieve subsequent pages of detections. Rename to `nextPageToken` in JSON.  
— | `nested_detection_samples` | `repeated DetectionWithSamples` | **New field:** Nested dependencies returned when `include_nested_detections` is set to true in requests.  
— | `resp_too_large_detections_truncated` | `bool` | **New field:** Truncation status indicator flagging whether matching detections were omitted to respect `max_resp_size_bytes` limits.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Proto tag rearrangements:**
    * Proto tags in requests shifted significantly to accommodate parent path integrations (for example, `rule_id` tag from 1 to 2, `start_time` renamed or moved to 4, `end_time` to 5).
  * **Response size protection:**
    * Adds `max_resp_size_bytes` and truncation indicators (`resp_too_large_detections_truncated`) to secure clients against large memory allocations when querying wide detection intervals.
  * **Nested detections support:**
    * Modern APIs introduce graph nesting capabilities (`include_nested_detections` and `nested_detection_samples`) to reconstruct rule inheritance and dependencies.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacySearchDetections`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
