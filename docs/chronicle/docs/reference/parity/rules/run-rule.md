---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/run-rule/
title: RunRule (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:10.951752+00:00
---

# RunRule (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/run-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RunRule (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`RunRule`**) to the modern Chronicle API (**`CreateRetrohunt`**).

## Protocol and mapping overview

Feature | Legacy API (`RunRule` V1) | Modern Chronicle API (`CreateRetrohunt`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/retrohunts.create`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `CreateRetrohuntRequest` standardizes execution into standard REST sub-resource creation under parent rules and groups event times into interval fields.

Legacy field (`RunRuleRequest` V1) | Modern field (`CreateRetrohuntRequest` / `Retrohunt`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping / architectural shift:** Legacy identified rules using the raw parameter `rule_id` inside URL path. The modern API routes this using parent resource paths: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}` (where you target the rule UUID).  
`rule_id` | — | — | **Ignored:** Target rule ID is parsed directly from parent path segments.  
`event_start_time` | `retrohunt.process_interval.start_time` | `Timestamp` | **Consolidated into interval:** Legacy `event_start_time` is mapped inside the required `process_interval` interval object (`Interval.start_time`). Rename to `processInterval.startTime` in JSON.  
`event_end_time` | `retrohunt.process_interval.end_time` | `Timestamp` | **Consolidated into interval:** Legacy `event_end_time` is mapped inside the required `process_interval` interval object (`Interval.end_time`). Rename to `processInterval.endTime` in JSON.  
  
* * *

## Response payload field-by-field parity

Both APIs return a `google.longrunning.Operation` tracking the asynchronous execution job progress.

Legacy field (`google.longrunning.Operation` V1) | Modern field (`google.longrunning.Operation` response) | Field type | Parity and migration notes  
---|---|---|---  
`name` _(LRO name)_ | `name` | `string` | **Google Cloud scoping:** Standard canonical resource name of the LRO Operation.  
`metadata` _(RunRuleMetadata)_ | `metadata` _(RetrohuntMetadata / Retrohunt)_ | `Message` | **Restructured:** The modern LRO operation returns progress metadata that resolves to the modern Retrohunt execution resource object. Field mappings between `RunRuleMetadata` and modern properties are detailed in the following table.  
`response` _(RunRuleResponse)_ / empty | `response` _(Retrohunt)_ | `Message` | **Restructured:** Instead of returning an empty response block, the modern LRO resolves to the full Retrohunt resource showing final state.  
  
### Nested metadata / status field parity

The fields mapping inside individual `RunRuleMetadata` V1 and modern properties are detailed in the following table:

Legacy field (`RunRuleMetadata` V1) | Modern field (`Retrohunt` message) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | `name` | `string` | Consolidated into the modern canonical resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/retrohunts/{retrohunt_id}`.  
`event_start_time` | `process_interval.start_time` | `Timestamp` | Mapped inside the `process_interval` object (`Interval.start_time`).  
`event_end_time` | `process_interval.end_time` | `Timestamp` | Mapped inside the `process_interval` object (`Interval.end_time`).  
`run_started_time` | `execution_interval.start_time` | `Timestamp` | Mapped inside the `execution_interval` object (`Interval.start_time`).  
`run_completed_time` | `execution_interval.end_time` | `Timestamp` | Mapped inside the `execution_interval` object (`Interval.end_time`).  
— | `state` | `enum` | **New field:** Execution status enum (`RUNNING`, `DONE`, `CANCELLED`, `FAILED`).  
— | `progress_percentage` | `float` | **New field:** Percent progress towards completion.  
  
* * *

## Key differences

  * **Google Cloud project scoping and endpoint realignment:**
    * Scoped natively under parent project instance folder bindings (`parent` path parameter). Maps legacy `POST` custom actions `:run` under `RulesEngine` to standard REST sub-resource creations (`.../rules/{rule_id}/retrohunts`) under `RuleService`.
  * **Time window consolidation (Interval):**
    * Standalone timestamp pairs for event ranges and execution durations are structured into standard `google.type.Interval` objects (`process_interval` and `execution_interval`).
  * **Response enrichment:**
    * Rather than returning an empty response value on operation resolution, the modern operation returns the complete state of the finished Retrohunt execution details.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/retrohunts.create`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
