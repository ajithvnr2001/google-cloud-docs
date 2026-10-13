---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/delete-rule/
title: DeleteRule (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:14.222010+00:00
---

# DeleteRule (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/delete-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DeleteRule (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`DeleteRule`**) to the modern Chronicle API (**`DeleteRule`**).

## Protocol and mapping overview

Feature | Legacy API (`DeleteRule` V1) | Modern Chronicle API (`DeleteRule`)  
---|---|---  
**HTTP method** | `DELETE` | `DELETE`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.delete`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `DeleteRuleRequest` routes target paths using Google Cloud resource formats and introduces controls for cascading deletion.

Legacy field (`DeleteRuleRequest` V1) | Modern field (`DeleteRuleRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`rule_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping / consolidated ID:** Legacy passed the raw `{rule_id}` in the URL path. The modern API routes this using the standard Google Cloud resource path: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}` (deleting specific revisions is unsupported; target the root rule UUID).  
— | `force` | `bool` | **New parameter:** Cascade deletion toggle. If true, deletes all associated retrohunts and legacy alerts. If false, the call will only succeed if the rule has no associated retrohunts or alerts. Rename to `force` in JSON.  
  
* * *

## Response payload field-by-field parity

Both APIs return empty responses upon successful deletion.

Legacy field | Modern field | Field type | Parity and migration notes  
---|---|---|---  
`google.protobuf.Empty` | `google.protobuf.Empty` | `Empty` | **Parity mapped:** Successful requests return HTTP 200 OK (mapping to an empty response object `{}`).  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`name` path parameter).
  * **Cascade safety checks (force):**
    * Introduces a `force` boolean control parameter. Clients must explicitly verify if they want to cascade-delete associated retrohunts and historical alerts, preventing unintended loss of audit artifacts.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/rules.delete`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
