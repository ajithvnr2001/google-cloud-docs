---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/retrohunt/create-retrohunt/
title: CreateRetrohunt parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:08.698861+00:00
---

# CreateRetrohunt parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/retrohunt/create-retrohunt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CreateRetrohunt parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine API (**`RunRetrohunt`**) to the modern Chronicle API (**`CreateRetrohunt`**).

## Protocol and mapping overview

Feature | Legacy API (`RunRetrohunt`) | Modern Chronicle API (`CreateRetrohunt`)  
---|---|---  
**HTTP Method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/retrohunts.create`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `CreateRetrohuntRequest` standardizes retrohunt execution into standard REST sub-resource creation under a parent rule revision and consolidates time ranges into intervals.

Legacy Field (`RunRetrohuntRequest`) | Modern Field (`CreateRetrohuntRequest` / `Retrohunt`) | Field type | Parity & Migration Notes  
---|---|---|---  
`version_id` | `parent` _(in HTTP path)_ | `string` | **GCP Scoping / Architectural Shift:** Legacy passed `{rule_id}` or `{rule_id}@{version_ts}` in the URL path parameter `version_id`. The modern API routes this using the standard Google Cloud parent resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id@revision_id}`.  
`start_time` | `retrohunt.process_interval.start_time` | `Timestamp` | **Consolidated into Interval:** Legacy standalone `start_time` is mapped inside the required `process_interval` interval object (`Interval.start_time`). Rename to `processInterval.startTime` in JSON.  
`end_time` | `retrohunt.process_interval.end_time` | `Timestamp` | **Consolidated into Interval:** Legacy standalone `end_time` is mapped inside the required `process_interval` interval object (`Interval.end_time`). Rename to `processInterval.endTime` in JSON.  
  
* * *

## Response payload field-by-field parity

While legacy backstory returned the `Retrohunt` object directly (synchronously starting execution), the modern API returns a `google.longrunning.Operation` tracking the asynchronous job, where the final operation response resolves to `Retrohunt`.

Legacy Field (`Retrohunt` response) | Modern Field (`Retrohunt` in `Operation` response) | Field type | Parity & Migration Notes  
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
    * Legacy retrohunt execution was implemented as a custom `POST` action (`POST /v2/detect/rules/{version_id}:runRetrohunt`) under `RulesEngineService`.
    * Modern Chronicle API standardizes this as a REST sub-resource creation (`POST .../rules/{rule}/retrohunts`) under `RuleService` (`CreateRetrohunt`).
  * **Google Cloud Project Scoping and Canonical Names:**
    * Scoped natively under parent project instance rule bindings. Separate rule, version, and retrohunt IDs are consolidated into standard Google Cloud canonical resource names.
  * **Time Window Consolidation (Interval):**
    * Standalone timestamp pairs for event ranges and execution durations are structured into standard `google.type.Interval` objects (`process_interval` and `execution_interval`).
  * **Long-Running Operation Shift:**
    * Instead of returning the raw retrohunt object directly on initial request, the Chronicle API returns a `LongRunning.Operation` to reliably track asynchronous execution progress.
  * **IAM Permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/retrohunts.create`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
