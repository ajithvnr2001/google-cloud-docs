---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/retrohunt/get-retrohunt/
title: GetRetrohunt parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:29.500919+00:00
---

# GetRetrohunt parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/retrohunt/get-retrohunt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetRetrohunt parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine API (**`GetRetrohunt`**) to the modern Chronicle API (**`GetRetrohunt`**).

## Protocol and mapping overview

Feature | Legacy API (`GetRetrohunt`) | Modern Chronicle API (`GetRetrohunt`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/retrohunts.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetRetrohuntRequest` identifies target execution resources using canonical Google Cloud resource paths rather than separate version and execution IDs.

Legacy Field (`GetRetrohuntRequest`) | Modern Field (`GetRetrohuntRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`version_id` / `retrohunt_id` | `name` _(in HTTP path)_ | `string` | **GCP Scoping / Consolidated ID:** Legacy passed `{rule_id}` (or `{rule_id}@{version_ts}`) in `version_id` and the execution ID in `retrohunt_id`. The modern API unifies these parameters into a single canonical Google Cloud resource path under name: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id@revision_id}/retrohunts/{retrohunt_id}`.  
  
* * *

## Response payload field-by-field parity

Both APIs return the retrieved `Retrohunt` execution resource.

Legacy Field (`Retrohunt` response) | Modern Field (`Retrohunt` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`retrohunt_id` / `rule_id` / `version_id` | `name` | `string` | **Consolidated:** Legacy separate identifier strings are unified into the canonical Google Cloud resource path under name: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id@revision_id}/retrohunts/{retrohunt_id}`.  
`event_start_time` | `process_interval.start_time` | `Timestamp` | Mapped inside the `process_interval` object (`Interval.start_time`).  
`event_end_time` | `process_interval.end_time` | `Timestamp` | Mapped inside the `process_interval` object (`Interval.end_time`).  
`retrohunt_start_time` | `execution_interval.start_time` | `Timestamp` | Mapped inside the `execution_interval` object (`Interval.start_time`).  
`retrohunt_end_time` | `execution_interval.end_time` | `Timestamp` | Mapped inside the `execution_interval` object (`Interval.end_time`).  
`state` | `state` | `enum` | **Parity Mapped / Value Enrichment:** Maps directly to `State` enum (`RUNNING`, `DONE`, `CANCELLED`). The modern API adds support for `FAILED` (value 4) when execution fails.  
`progress_percentage` | `progress_percentage` | `float` | **Parity Mapped:** Percent progress towards completion (0.00 to 100.00). Rename to `progressPercentage` in JSON.  
  
* * *

## Key differences

  * **Service Consolidation and Renaming:**
    * Legacy retrohunt retrieval was housed under `RulesEngineService` with URL pattern `/v2/detect/rules/{version_id}/retrohunts/{retrohunt_id}`.
    * Modern Chronicle API consolidates this under `RuleService` (`GetRetrohunt`), using standard Google Cloud parent paths (`projects/.../rules/{rule}/retrohunts/{retrohunt}`).
  * **Google Cloud Project Scoping and Canonical Names:**
    * Scoped natively under parent project instance rule bindings. Separate rule, version, and retrohunt IDs are consolidated into standard Google Cloud canonical resource names.
  * **Time Window Consolidation (Interval):**
    * Standalone timestamp pairs for event ranges and execution durations on returned objects are structured into standard `google.type.Interval` objects (`process_interval` and `execution_interval`).
  * **IAM Permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/retrohunts.get`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
