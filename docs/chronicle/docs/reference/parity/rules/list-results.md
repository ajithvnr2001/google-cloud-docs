---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/list-results/
title: ListResults (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:57.975370+00:00
---

# ListResults (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/list-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListResults (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`ListResults`**) to the modern Chronicle API (**`LegacySearchRuleResults`**).

## Protocol and mapping overview

Feature | Legacy API (`ListResults` V1) | Modern Chronicle API (`LegacySearchRuleResults`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacySearchRuleResults`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacySearchRuleResultsRequest` scopes queries under parent project instances and renames execution tracker segments.

Legacy field (`ListResultsRequest` V1) | Modern field (`LegacySearchRuleResultsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes the search queries under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`name` | `rule_id` / `version_timestamp` | `string` -> `string` / `Timestamp` | **Architectural realignment:** Legacy listed results by target job run identifier using `name` (LRO name). The modern API lists results by target rule UUID (`rule_id`) and optional version revision selector (`version_timestamp`). Rename to `ruleId` and `versionTimestamp` in JSON.  
— | `time_range` | `Interval` | **New parameter:** Bounds the search to target event start and end time windows (`Interval`). Rename to `timeRange` in JSON.  
`page_size` | `max_matches` | `int32` | **Renamed:** Sets the limit of returned matching detections (default 10000). Rename to `maxMatches` in JSON.  
`page_token` | — _(retired)_ | `string` | **Retired:** Token-based pagination is retired in favor of specifying bounding window filters (`time_range`).  
— | `rule_source` | `enum` | **New parameter:** Dictates whether rule queries evaluate client-authored rules (`CUSTOMER`) or Uppercase system-provided rules (`UPPERCASE`). Rename to `ruleSource` in JSON.  
— | `max_resp_size_bytes` | `int32` | **New field:** Restricts response size in bytes to prevent large message serialization overflows. Rename to `maxRespSizeBytes` in JSON.  
  
* * *

## Response payload field-by-field parity

While legacy backstory V1 returned a flat array of `RunResult` messages containing raw UDM event properties, the modern API returns compiled `YaraL2Detection` objects.

Legacy field (`ListResultsResponse` V1) | Modern field (`LegacySearchRuleResultsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`results` | `yara_l_2_detections` | `repeated RunResult` -> `repeated YaraL2Detection` | **Renamed / restructured:** Legacy returned `RunResult` items containing raw UDM events. The modern API returns structured `YaraL2Detection` lists capturing the full match details and custom bindings. Rename to `yaraL2Detections` in JSON.  
— | `yara_l_2_too_many_detections` | `bool` | **New field:** Flag indicating if more detections matched than allowed by `max_matches`. Rename to `yaraL2TooManyDetections` in JSON.  
— | `resp_too_large_detections_truncated` | `bool` | **New field:** Truncation status indicator flagging whether matching detections were omitted to respect `max_resp_size_bytes` limits.  
`next_page_token` | — _(retired)_ | `string` | **Retired:** Paging continuation tokens are retired in favor of window bounding filters.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Identification shift:**
    * Legacy indexed output lists using temporary job run identifiers (`name` operation paths).
    * Modern Chronicle API index queries target the rule UUID (`rule_id`) and timestamps directly, allowing history extraction without mapping back to operations.
  * **Detection representation:**
    * Decouples UDM event lists into structured compiled detection models (`yara_l_2_detections`), exposing matched keys and syntax contexts.
  * **Response size protection:**
    * Introduces `max_resp_size_bytes` and truncation indicators (`resp_too_large_detections_truncated`) to secure clients against large memory allocations.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacySearchRuleResults`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
