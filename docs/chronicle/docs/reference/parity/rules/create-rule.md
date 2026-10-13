---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/create-rule/
title: CreateRule (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:09.911091+00:00
---

# CreateRule (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/create-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CreateRule (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`CreateRule`**) to the modern Chronicle API (**`CreateRule`**).

## Protocol and mapping overview

Feature | Legacy API (`CreateRule` V1) | Modern Chronicle API (`CreateRule`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.create`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `CreateRuleRequest` scopes rule creation under parent project instances instead of utilizing global scopes.

Legacy field (`CreateRuleRequest` V1) | Modern field (`CreateRuleRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes rule creation under parent project instance folder bindings in the URL path: `projects/{project}/locations/{location}/instances/{instance}`.  
`rule` | `rule` | `Rule` | **Parity mapped:** The rule representation structure. Details inside nested mappings in the following table.  
  
### Nested Rule request fields mapped

The fields mapping inside the `Rule` request is as follows:

Legacy field (`Rule` request V1) | Modern field (`Rule` request) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | — | `string` | **Retired / server-assigned:** In the modern API, rule identifiers are assigned by the server upon creation and cannot be predefined by the client.  
`rule` | `text` | `string` | **Renamed:** The YARA-L rule content string block itself.  
`etag` | `etag` | `string` | **Direct map:** Optional concurrency token (typically empty or ignored on initial creations).  
  
* * *

## Response payload field-by-field parity

The response of modern `CreateRule` enriches outputs significantly, compiling diagnostics and parsing metadata.

Legacy field (`Rule` response V1) | Modern field (`Rule` response) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | `name` | `string` | **Consolidated:** Unified into the canonical resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}`.  
`rule` | `text` | `string` | **Renamed:** Original YARA-L rule content string.  
`etag` | `etag` | `string` | **Direct map:** Version concurrency control token.  
— | `revision_id` | `string` | **New field:** Server-generated unique revision identifier checksum.  
— | `display_name` | `string` | **New field:** Title extracted automatically from YARA-L rules metadata headers.  
— | `author` | `string` | **New field:** Author parsed automatically from YARA-L comments metadata.  
— | `severity` | `Severity` | **New field:** Severity rating extracted from YARA-L details.  
— | `metadata` | `map<string, string>` | **New field:** Raw map of YARA-L header attributes.  
— | `create_time` | `Timestamp` | **New field:** Initial rule creation timestamp.  
— | `revision_create_time` | `Timestamp` | **New field:** Rule version modification timestamp.  
— | `compilation_state` | `enum` | **New field:** Compilation status (for example, `SUCCEEDED`, `FAILED`).  
— | `compilation_diagnostics` | `repeated Diagnostic` | **New field:** Compiler diagnostic logs listing error and warning blocks.  
— | `type` | `enum RuleType` | **New field:** Infers rule type (`SINGLE_EVENT` versus `MULTI_EVENT`).  
— | `reference_lists` | `repeated string` | **New field:** External Reference List bindings compiled dynamically.  
— | `allowed_run_frequencies` | `repeated RunFrequency` | **New field:** Allowed schedules matching compilation complexities.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`projects/{project}/locations/{location}/instances/{instance}`).
  * **Server-assigned unique resource identifiers:**
    * Legacy API allowed client-specified `rule_id` properties inside the payload request. The modern API ignores client-submitted IDs, assigning secure UUID components directly in resource paths.
  * **Comprehensive compilation warnings:**
    * Legacy responses failed to return detailed diagnostics when compilation succeeded with warnings or non-blocking syntax errors. The modern API introduces structured `compilation_diagnostics` items to help debug compilation complexities.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/rules.create`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
