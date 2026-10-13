---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/get-rule/
title: GetRule (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:30.755701+00:00
---

# GetRule (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/get-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetRule (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`GetRule`**) to the modern Chronicle API (**`GetRule`**).

## Protocol and mapping overview

Feature | Legacy API (`GetRule` V1) | Modern Chronicle API (`GetRule`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.get`  
  
* * *

## Request payload field-by-field parity

The modern request scopes retrieval parameters using Google Cloud canonical resource paths rather than separate UUIDs.

Legacy field (`GetRuleRequest` V1) | Modern field (`GetRuleRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping / consolidated ID:** Legacy passed the raw `{rule_id}` in the URL path. The modern API routes this using the standard Google Cloud resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}` (where you target the root YARA-L rule UUID).  
— | `view` | `enum` | **New parameter:** Selects the rule view scope (`RuleView` enum: `RULE_VIEW_UNSPECIFIED`, `BASIC`, `REVISION_METADATA_ONLY`, `CONFIG_ONLY`, `FULL`, `TRENDS`). Defaults to `FULL` for single rule fetches.  
  
* * *

## Response payload field-by-field parity

Both APIs return the retrieved `Rule` representation, with the modern API enriching return structures with compilation diagnostics and parsed metadata.

Legacy field (`Rule` response V1) | Modern field (`Rule` response) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | `name` | `string` | **Consolidated:** Legacy separate identifier strings are unified into the canonical Google Cloud resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}`.  
`rule` | `text` | `string` | **Renamed:** The YARA-L rule content. Rename to `text` in JSON.  
`etag` | `etag` | `string` | **Direct map:** Concurrency control token used in updates.  
— | `revision_id` | `string` | **New field:** Represents the unique version checksum string.  
— | `display_name` | `string` | **New field:** The user-specified title display name of the rule.  
— | `author` | `string` | **New field:** Author name metadata extracted from YARA-L comments.  
— | `metadata` | `map<string, string>` | **New field:** Structured user-defined YARA-L metadata headers.  
— | `create_time` | `Timestamp` | **New field:** Timestamp of when the rule was originally created.  
— | `revision_create_time` | `Timestamp` | **New field:** Timestamp when the rule revision was written.  
— | `compilation_state` / `compilation_diagnostics` | `enum` / `repeated Message` | **New fields:** Detailed compilation status and parse diagnostic warnings.  
— | `type` | `enum RuleType` | **New field:** Infers rule type (`SINGLE_EVENT` versus `MULTI_EVENT`).  
— | `reference_lists` | `repeated string` | **New field:** Extracted list of resource names for Reference Lists referenced in the Yara-L rule.  
— | `allowed_run_frequencies` | `repeated RunFrequency` | **New field:** Execution frequencies allowed for the rule based on Yara-L complexity (for example, `LIVE`, `HOURLY`, `DAILY`).  
— | `scope` | `string` | **New field:** Data RBAC scope resource name associated with the rule.  
— | `near_real_time_live_rule_eligible` | `bool` | **New field:** Flag indicating whether the rule is eligible for near-real-time streaming detection.  
— | `data_tables` | `repeated string` | **New field:** Resource names of Data Tables referenced by this rule.  
— | `has_nonexistence_checks` | `bool` | **New field:** Flag indicating whether the rule implements non-existence checks.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`projects/{project}/locations/{location}/instances/{instance}`).
  * **YARA-L field renaming:**
    * The rule content parameter is renamed from `rule` in V1 to `text` in the modern Chronicle API.
  * **Compilation reporting and syntax resolution:**
    * Modern APIs automatically run compilation validations and expose rich warning objects (`compilation_diagnostics`), while resolving YARA-L references to Reference Lists and Data Tables.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/rules.get`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
