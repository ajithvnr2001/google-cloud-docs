---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/disable-alerting/
title: DisableAlerting (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:17.377257+00:00
---

# DisableAlerting (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/disable-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DisableAlerting (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`DisableAlerting`**) to the modern Chronicle API (**`UpdateRuleDeployment`**).

## Protocol and mapping overview

Feature | Legacy API (`DisableAlerting` V2) | Modern Chronicle API (`UpdateRuleDeployment`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/ruleDeployments.update`  
  
* * *

## Request payload field-by-field parity

The legacy backstory API implemented disabling alerting as a dedicated `POST` RPC endpoint. The modern Chronicle API models alerting configuration as a `PATCH` modification of the `alerting` boolean attribute (setting to false) on the sub-resource `RuleDeployment`.

Legacy field (`DisableAlertingRequest`) | Modern field (`UpdateRuleDeploymentRequest` / `RuleDeployment`) | Field type | Parity & migration notes  
---|---|---|---  
`rule_id` | `rule_deployment.name` _(in HTTP path)_ | `string` | **Google Cloud scoping / resource unification:** Legacy passed the raw rules engine parameter `rule_id`. The modern API routes this using parent resource paths: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `rule_deployment.alerting` | `bool` | **Target attribute mapping:** Set `alerting = false` to disable rule alerting status.  
— | `update_mask` | `FieldMask` | **Required mask:** Include `alerting` in JSON `updateMask`.  
  
* * *

## Response payload field-by-field parity

In legacy backstory, `DisableAlerting` returned an empty response. In the modern API, `UpdateRuleDeployment` returns the modified deployment state.

Legacy field (`Empty` response) | Modern field (`RuleDeployment` response) | Field type | Parity & migration notes  
---|---|---|---  
`google.protobuf.Empty` | `name` | `string` | **Canonical resource path name:** `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `alerting` | `bool` | Returns false confirming alerting is disabled.  
— | `enabled`, `archived`, or `run_frequency` | `bool` or `enum` | Returns other deployment properties.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`rule_deployment.name` path parameter).
  * **Stateful attributes (alerting):**
    * Rather than launching custom `POST` endpoints `:disableAlerting`, alerting configuration is parameterized by setting `alerting = false` inside the sub-resource `RuleDeployment`.
  * **Execution dependency on archive states:**
    * Alert status cannot be modified on archived rules; if `archived = true`, the update request fails.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/ruleDeployments.update`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
