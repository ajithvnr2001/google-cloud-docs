---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/stream-test-rule/
title: StreamTestRule (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:05.913559+00:00
---

# StreamTestRule (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/stream-test-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# StreamTestRule (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`StreamTestRule`**) to the modern Chronicle API (**`LegacyTestRuleStreaming`**).

## Protocol and mapping overview

Feature | Legacy API (`StreamTestRule` V2) | Modern Chronicle API (`LegacyTestRuleStreaming`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacyTestRuleStreaming`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacyTestRuleStreamingRequest` scopes queries under parent projects, flattens input text properties, and adds support for RBAC scoping parameters.

Legacy field (`StreamTestRuleRequest` / `Rule`) | Modern field (`LegacyTestRuleStreamingRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes the validation stream under target instance environments: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`rule.rule_text` | `rule_text` | `string` | **Renamed / restructured:** Legacy passed YARA-L content nested inside the rule object (`rule.rule_text`). The modern API flattens this, taking the raw YARA-L contents directly using the optional `rule_text` parameter. Rename to `ruleText` in JSON.  
— | `rule` | `string` | **New parameter:** Allows testing an existing Rule revision using its resource name path instead of passing raw rule text.  
`start_time` | `start_time` | `Timestamp` | **Direct map:** Start of query time range. Rename to `startTime` in JSON.  
`end_time` | `end_time` | `Timestamp` | **Direct map:** End of query time range. Rename to `endTime` in JSON.  
`max_results` | `max_detections` | `int32` | **Renamed:** Sets the limit of returned detections (default 1000, max 10000). Rename to `maxDetections` in JSON.  
— | `scope` | `string` | **New parameter:** Target Data RBAC scope resource name to run the rule validation check against.  
  
* * *

## Response payload field-by-field parity

Both streaming APIs return matching output blocks, with the modern API reporting granular execution details.

Legacy field (`StreamTestRuleResponse` / `Error`) | Modern field (`LegacyTestRuleStreamingResponse` / `ExecutionError`) | Field type | Parity & migration notes  
---|---|---|---  
`detection` | `detection` | `repeated Collection` | **Direct map:** A temporary, unpersisted detection Collection.  
`error` | `execution_error` | `ExecutionError` | **Restructured / renamed:** Execution errors are mapped into structured `ExecutionError` messages containing gRPC error status and bounding interval ranges (`time_range`). Rename to `executionError` in JSON.  
— | `rule_compilation_error` | `RuleCompilationError` | **New field:** Detailed diagnostic warnings when YARA-L parsing or compilation fails. Rename to `ruleCompilationError` in JSON.  
— | `too_many_detections` | `bool` | **New field:** Flag telling if more detections matched than allowed by `max_detections`. Rename to `tooManyDetections` in JSON.  
— | `progress_percent` | `float` | **New field:** Execution processing progress percent (0.0 to 100.0). Rename to `progressPercent` in JSON.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Request flattening & curated rule testing:**
    * Ephemeral test rules accept raw YARA-L text directly (`rule_text`), while the API adds a new `rule` parameter allowing clients to run temporary dry runs against stored, pre-existing rule revisions.
  * **Execution diagnostics:**
    * Modern responses enrich compile-time diagnostics (`rule_compilation_error`) and execution processing progress indicators (`progress_percent`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacyTestRuleStreaming`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
