---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/disable-live-rule/
title: DisableLiveRule (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:16.122243+00:00
---

# DisableLiveRule (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/disable-live-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DisableLiveRule (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`DisableLiveRule`**) to the modern Chronicle API (**`UpdateRuleDeployment`**).

## Protocol and mapping overview

Feature | Legacy API (`DisableLiveRule` V2) | Modern Chronicle API (`UpdateRuleDeployment`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/ruleDeployments.update`  
  
* * *

## Request payload field-by-field parity

The legacy backstory API implemented disabling live rules as a dedicated `POST` RPC endpoint. The modern Chronicle API models disabling live evaluation as a `PATCH` modification of `enabled` (setting to false) on the sub-resource `RuleDeployment`.

Legacy field (`DisableLiveRuleRequest`) | Modern field (`UpdateRuleDeploymentRequest` / `RuleDeployment`) | Field type | Parity & migration notes  
---|---|---|---  
`rule_id` | `rule_deployment.name` _(in HTTP path)_ | `string` | **Google Cloud scoping / resource unification:** Legacy passed the raw rules engine parameter `rule_id`. The modern API routes this using parent resource paths: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `rule_deployment.enabled` | `bool` | **Target attribute mapping:** Set `enabled = false` to deactivate continuous rule execution.  
— | `update_mask` | `FieldMask` | **Required mask:** Include `enabled` in JSON `updateMask`.  
  
* * *

## Response payload field-by-field parity

In legacy backstory, `DisableLiveRule` returned an empty response. In the modern API, `UpdateRuleDeployment` returns the modified deployment state.

Legacy field (`Empty` response) | Modern field (`RuleDeployment` response) | Field type | Parity & migration notes  
---|---|---|---  
`google.protobuf.Empty` | `name` | `string` | **Canonical resource path name:** `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `enabled` | `bool` | Returns false confirming rule execution is disabled.  
— | `run_frequency` | `enum` | Returns current configured frequency (for example, `LIVE`).  
— | `alerting` and `archived` | `bool` | Returns other deployment properties.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`rule_deployment.name` path parameter).
  * **Stateful attributes (enabled):**
    * Rather than launching custom `POST` endpoints `:disableLiveRule`, disabling continuous execution is parameterized by setting `enabled = false` inside the sub-resource `RuleDeployment`.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/ruleDeployments.update`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
