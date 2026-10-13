---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/get-rule/
title: GetRule (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:31.474537+00:00
---

# GetRule (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/get-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetRule (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`GetRule`**) to the modern Chronicle API (**`GetRule`**).

## Protocol and mapping overview

Feature | Legacy API (`GetRule` V2) | Modern Chronicle API (`GetRule`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetRuleRequest` routes identification using Google Cloud canonical resource paths and introduces options for partial views.

Legacy field (`GetRuleRequest`) | Modern field (`GetRuleRequest`) | Field type | Parity & migration notes  
---|---|---|---  
`version_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping and consolidated ID:** Legacy passed `{rule_id}` (or `{rule_id}@{version_ts}`) in `version_id`. The modern API unifies these parameters into a single canonical Google Cloud resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}` (where `{rule}` takes either `{rule_uuid}` or `{rule_uuid}@{revision_id}`).  
— | `view` | `enum` | **New parameter:** Selects the rule view scope (`RuleView` enum: `RULE_VIEW_UNSPECIFIED`, `BASIC`, `REVISION_METADATA_ONLY`, `CONFIG_ONLY`, `FULL`). Defaults to `FULL`.  
  
* * *

## Response payload field-by-field parity

Both APIs return representing `Rule` objects, but the modern API decouples deployment states (alerts and live status) to `RuleDeployment` resources.

Legacy field (`Rule` response) | Modern field (`Rule` response) | Field type | Parity & migration notes  
---|---|---|---  
`rule_id` and `version_id` | `name` | `string` | **Consolidated:** Legacy separate identifier strings are unified into the canonical Google Cloud resource path name: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}`.  
`version_id` | `revision_id` | `string` | **Renamed:** Represents the unique version checksum string.  
`rule_name` | `display_name` | `string` | **Renamed:** The user-specified title display name of the rule.  
`rule_text` | `text` | `string` | **Renamed:** YARA-L rule content.  
`author` | `author` | `string` | **Direct map / extracted:** Author name metadata extracted from YARA-L comments.  
`metadata` | `metadata` | `map<string, string>` | **Direct map:** Structured user-defined YARA-L metadata headers.  
`version_create_time` | `revision_create_time` | `Timestamp` | **Renamed:** Timestamp when the rule revision was written.  
— | `create_time` | `Timestamp` | **New field:** Timestamp of when the rule was originally created.  
`compilation_state` | `compilation_state` | `enum` | **Direct map:** Compilation status enum (`COMPILATION_STATE_UNSPECIFIED`, `SUCCEEDED`, `FAILED`).  
`compilation_error` | — _(nested)_ | `string` | **Restructured:** Legacy compilation errors are mapped into structured warning lists inside `compilation_diagnostics` in the modern response.  
— | `compilation_diagnostics` | `repeated CompilationDiagnostic` | **New field:** Structured collection containing warnings and errors generated during compilation.  
`archived_time` | — | `Timestamp` | **Retired:** Rule archiving and deletion lifecycles are managed natively using standard delete and undelete actions and operations.  
`alerting_enabled` | — | `bool` | **Decoupled:** Alert enablement state is decoupled from the rule definition and managed under the `RuleDeployment` resource (`projects/*/rules/*/deployment`).  
`live_rule_enabled` | — | `bool` | **Decoupled:** Continuous live rule evaluation toggle is decoupled and managed under the `RuleDeployment` resource.  
`rule_type` | `type` | `enum` | **Renamed and type shift:** Renamed from string `rule_type` to `RuleType` enum (`RULE_TYPE_UNSPECIFIED`, `SINGLE_EVENT`, `MULTI_EVENT`).  
`last_alert_status_change_time` | — | `Timestamp` | **Decoupled:** Moved to the corresponding activation change history under `RuleDeployment`.  
`inputs_used` | `inputs_used` | `InputsUsed` | **Direct map:** Structured fields indicating if the rule reads UDM events, context entities, or system alerts.  
`labels` | — | — | **Retired / decoupled:** Event labeling rules are managed and resolved dynamically in the detection pipelines.  
— | `reference_lists` | `repeated string` | **New field:** Extracted list of resource names for Reference Lists referenced in the YARA-L rule.  
— | `allowed_run_frequencies` | `repeated RunFrequency` | **New field:** Execution frequencies allowed for the rule based on YARA-L complexity (for example, `LIVE`, `HOURLY`, `DAILY`).  
— | `etag` | `string` | **New field:** Concurrency control token used in updates.  
— | `scope` | `string` | **New field:** Data RBAC scope resource name associated with the rule.  
— | `near_real_time_live_rule_eligible` | `bool` | **New field:** Read-only flag indicating whether the rule is eligible for near-real-time streaming detection.  
— | `data_tables` | `repeated string` | **New field:** Resource names of Data Tables referenced by this rule.  
— | `has_nonexistence_checks` | `bool` | **New field:** Flag indicating whether the rule implements non-existence checks.  
  
* * *

## Key differences

  * **Google Cloud project scoping and ID unification:**
    * Scoped natively under parent project instance folder bindings. Separate rule identifiers, revision hashes, and instance qualifiers are unified into canonical Google Cloud resource names.
  * **Rule configuration versus rule deployment separation:**
    * Legacy YARA-L configurations and runtime deployment variables (alert states, live schedules) were combined inside a single Rule container.
    * Modern Chronicle API decouples these completely: `Rule` represents purely versioned config syntax (which is immutable upon revision creation), whereas mutable flags like alert states (`alerting_enabled`) and live status (`live_rule_enabled`) are structured under `RuleDeployment` resources (`projects/*/rules/*/deployment`).
  * **Compilation reporting and syntax resolution:**
    * Simple error strings are replaced by comprehensive diagnostic items (`compilation_diagnostics`), and modern YARA-L references to external tables (`data_tables`) and lookup keys (`reference_lists`) are automatically parsed and cataloged.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/rules.get`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
