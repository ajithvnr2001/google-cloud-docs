---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/legacy-search-curated-detections/
title: LegacySearchCuratedDetections parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:41.458483+00:00
---

# LegacySearchCuratedDetections parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/legacy-search-curated-detections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LegacySearchCuratedDetections parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine API (**`ListCuratedRuleDetections`**) to the modern Chronicle API ([**`LegacySearchCuratedDetections`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchCuratedDetections)) defined under the `google.cloud.chronicle.v1main` package.

## Protocol and mapping overview

Feature | Legacy API (`ListCuratedRuleDetections`) | Modern API (`LegacySearchCuratedDetections`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacySearchCuratedDetections`  
  
* * *

## Request payload field-by-field parity

The modern `LegacySearchCuratedDetectionsRequest` matches fields from the legacy request, with added controls for maximum response payload bytes, simulated data visibility, and nested configurations.

Legacy field (`ListCuratedRuleDetectionsRequest`) | Modern field (`LegacySearchCuratedDetectionsRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context:** Scopes the connection target using the standard resource path in the HTTP URL path. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`rule_id` | `rule_id` | `string` | **Direct Map:** Unique identifier of the curated rule.  
`alert_state` | `alert_state` | `enum` | **Direct Map:** Mapped directly to filter by `SecurityResult.AlertState` enum.  
`start_time` | `start_time` | `Timestamp` | **Direct Map:** Detections start time boundary.  
`end_time` | `end_time` | `Timestamp` | **Direct Map:** Detections end time boundary.  
`list_basis` | `list_basis` | `enum` | **Direct Map:** Maps to `ListBasis` enum to determine if bounds apply to detection or created times.  
`page_size` | `page_size` | `int32` | **Direct Map:** Pagination page size limits.  
`page_token` | `page_token` | `string` | **Direct Map:** Paging resumption token.  
`include_simulated_detections` | `include_simulated_detections` / `simulated_data_visibility` | `bool`/`enum` | **Modernized:** Legacy boolean `include_simulated_detections` is deprecated. Use the structured `simulated_data_visibility` enum setting.  
— | `max_resp_size_bytes` | `int32` | **New Option:** Toggles maximum response limit sizes in bytes.  
— | `include_nested_detections` | `bool` | **New Option:** Toggles whether nested rule detections are fetched.  
  
* * *

## Response payload field-by-field parity

The response payload maps the detection arrays directly, adding support for truncation reporting and nested detection structures.

Legacy field (`ListCuratedRuleDetectionsResponse` message) | Modern field (`LegacySearchCuratedDetectionsResponse` message) | Field type | Parity & migration notes  
---|---|---|---  
`curated_rule_detections` | `curated_detections` | `repeated Collection` | **Parity Mapped:** Array list of rule detections returned as backstory `Collection` elements.  
`next_page_token` | `next_page_token` | `string` | **Direct Map:** Paging resumption token.  
— | `nested_detection_samples` | `repeated DetectionWithSamples` | **New Parameter:** Nested detections returned if requested using `include_nested_detections`.  
— | `resp_too_large_detections_truncated` | `bool` | **New Parameter:** Set to `true` if the response exceeded requested `max_resp_size_bytes` and was truncated.  
  
* * *

## Key differences analysis

  1. **Google Cloud Instance Bounds:**
     * Legacy rule listings queried detections across tenant spaces globally.
     * The modern `LegacySearchCuratedDetections` API scopes query execution directly under the instance path (`projects/{project}/locations/{location}/instances/{instance}`) mapped as standard parent.
  2. **Advanced Response Handling:**
     * Adds the capability to configure maximum response payload sizes to prevent gateway timeout errors, and report truncation state explicitly using `resp_too_large_detections_truncated`.
  3. **Structured Nested Detections:**
     * Introduces options to resolve and fetch one level of nested child detections under the `nested_detection_samples` repeated array.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
