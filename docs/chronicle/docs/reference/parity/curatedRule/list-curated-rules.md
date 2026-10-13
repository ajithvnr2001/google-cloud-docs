---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/list-curated-rules/
title: ListCuratedRules parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:45.531405+00:00
---

# ListCuratedRules parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/list-curated-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListCuratedRules parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine API (**`ListCuratedRules`**) to the modern Chronicle API ([**`ListCuratedRules`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.curatedRules/list)) defined under the `google.cloud.chronicle.v1main` package.

## Protocol and mapping overview

Feature | Legacy API (`ListCuratedRules`) | Modern API (`ListCuratedRules`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/curatedRules.list`  
  
* * *

## Request payload field-by-field parity

Paging parameters map directly, and the target is scoped under the parent Google Cloud instance directory path.

Legacy field (`ListCuratedRulesRequest`) | Modern field (`ListCuratedRulesRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `parent` (in HTTP path) | `string` | **Google Cloud Scoping Hierarchy:** Scopes the connection target using the standard resource path in the HTTP URL path. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`page_size` | `page_size` | `int32` | **Parity Mapped:** Pagination page size limits. Rename to `pageSize` in JSON payloads.  
`page_token` | `page_token` | `string` | **Parity Mapped:** Paging resumption token. Rename to `pageToken` in JSON payloads.  
  
* * *

## Response payload field-by-field parity

### Response roots mappings

The response returns arrays of curated rules and next page tokens.

Legacy field (`ListCuratedRulesResponse` message) | Modern field (`ListCuratedRulesResponse` message) | Field type | Parity & migration notes  
---|---|---|---  
`curated_rules` | `curated_rules` | `repeated CuratedRule` | **Parity Mapped:** Returns the repeated list of curated rules, with individual resource conversions mapped in the following table.  
`next_page_token` | `next_page_token` | `string` | **Parity Mapped:** Token to retrieve subsequent pages. Rename to `nextPageToken` in JSON payloads.  
  
### Nested CuratedRule field parity

The fields mapping inside the returned `CuratedRule` payloads is as follows:

Legacy field (`CuratedRule` message) | Modern field (`CuratedRule` message) | Target type | Parity & migration notes  
---|---|---|---  
`rule_id` | `name` | `string` | **Parity Mapped:** The ID is mapped inside the final segment of the canonical name resource path: `projects/{project}/locations/{location}/instances/{instance}/curatedRules/{rule_id}`.  
`rule_name` | `display_name` | `string` | **Parity Mapped:** Maps to `displayName`.  
`metadata` | `metadata` | `map<string, string>` | **Parity Mapped:** Custom key-value metadata.  
`severity` | `severity` | `enum` | **Type Alignment:** Legacy severity string maps to the strongly-typed `Severity` enum on the modern resource.  
`description` | `description` | `string` | **Parity Mapped:** Rule description.  
`rule_type` | `type` | `enum` | **Type Alignment / Renaming:** Rename to `type`. The legacy string value maps to the modern `RuleType` enum field.  
`precision` | `precision` | `enum` | **Type Alignment:** Legacy string maps to the modern `CuratedRulePrecision` enum.  
`tactics` | `tactics` | `repeated MitreTactic` | **Restructured:** Flat tactics string elements are mapped to the structured `MitreTactic` objects containing string `id` and `display_name`.  
`techniques` | `techniques` | `repeated MitreTechnique` | **Restructured:** Flat techniques string elements are mapped to the structured `MitreTechnique` objects containing string `id` and `display_name`.  
`update_time` | `update_time` | `Timestamp` | **Parity Mapped:** Timestamp of the last rule update.  
`rule_set` | `curated_rule_set` | `string` | **Parity Mapped / Restructured:** Mapped to the modern `curated_rule_set` resource path format: `projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{category}/curatedRuleSets/{rule_set_id}`.  
  
* * *

## Key differences analysis

  1. **Google Cloud Resource Scoping:**
     * Scoped natively under standard Google Cloud project/location layout path.
  2. **Type Safety Enhancements:**
     * Enums (`RuleType`, `CuratedRulePrecision`, `Severity`, and others) replace legacy unstructured strings (`rule_type`, `precision`, and others) to validate inputs securely.
  3. **MITRE ATT &CK Model Restructuring:**
     * Tactics and techniques are fully structured as objects containing tactile `id` and `displayName` definitions, rather than flat lists of strings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
