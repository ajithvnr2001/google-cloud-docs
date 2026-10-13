---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/archive-rule/
title: ArchiveRule (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:03.885722+00:00
---

# ArchiveRule (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/archive-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ArchiveRule (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`ArchiveRule`**) to the modern Chronicle API (**`UpdateRuleDeployment`**).

## Protocol and mapping overview

Feature | Legacy API (`ArchiveRule` V2) | Modern Chronicle API (`UpdateRuleDeployment`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/ruleDeployments.update`  
  
* * *

## Request payload field-by-field parity

The legacy backstory API implemented archiving as a dedicated `POST` RPC endpoint. The modern Chronicle API models archiving as a `PATCH` modification of the `archived` boolean attribute on `RuleDeployment`.

Legacy field (`ArchiveRuleRequest`) | Modern field (`UpdateRuleDeploymentRequest` / `RuleDeployment`) | Field type | Parity & migration notes  
---|---|---|---  
`version_id` | `rule_deployment.name` _(in HTTP path)_ | `string` | **Google Cloud scoping / resource unification:** Legacy passed `{rule_id}` (or `{rule_id}@{version_ts}`) in `version_id`. Modern archiving targets the Rule's deployment path (excluding revisions): `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `rule_deployment.archived` | `bool` | **Target attribute mapping:** To archive a rule, set `archived = true`. To unarchive a rule (migrating from `UnarchiveRule`), set `archived = false`.  
— | `update_mask` | `FieldMask` | **Required mask:** Include `archived` in JSON `updateMask`.  
  
> [!CAUTION] Ensure that `enabled = false` (rule deployment is disabled) before setting `archived = true`, as active rules cannot be archived.

* * *

## Response payload field-by-field parity

In legacy backstory, `ArchiveRule` returned an empty response. In the modern API, `UpdateRuleDeployment` returns the modified deployment state.

Legacy field (`Empty` response) | Modern field (`RuleDeployment` response) | Field type | Parity & migration notes  
---|---|---|---  
`google.protobuf.Empty` | `name` | `string` | **Canonical resource path name:** `projects/{project}/locations/{location}/instances/{instance}/rules/{rule_id}/deployment`.  
— | `archived` | `bool` | Returns true confirming rule archiving.  
— | `archive_time` | `Timestamp` | Populated timestamp indicating when archiving was applied. Rename to `archiveTime` in JSON.  
— | `enabled`, `alerting`, or `run_frequency` | `bool` or `enum` | Returns other deployment properties (where `enabled = false` and `alerting = false` are automatically applied upon successful archiving).  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`rule_deployment.name` path parameter).
  * **Stateful attributes (archived):**
    * Rather than launching custom `POST` endpoints `:archive` or `:unarchive`, archiving is parameterized as a boolean flag `archived = true` inside the sub-resource `RuleDeployment`.
  * **Execution dependencies:**
    * The modern API enforces validation rules: attempting to archive an active rule (`enabled = true`) fails. The client must disable rule execution before submitting the archiving request.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission check (`chronicle.googleapis.com/ruleDeployments.update`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
