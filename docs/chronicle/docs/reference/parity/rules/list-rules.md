---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/list-rules/
title: ListRules (V1) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:59.973760+00:00
---

# ListRules (V1) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rules/list-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListRules (V1) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V1 API (**`ListRules`**) to the modern Chronicle API (**`ListRules`**).

## Protocol and mapping overview

Feature | Legacy API (`ListRules` V1) | Modern Chronicle API (`ListRules`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListRulesRequest` scopes queries under standard Google Cloud parent folder instance resources and introduces options for filtering, sorting, and view limits.

Legacy Field (`ListRulesRequest` V1) | Modern Field (`ListRulesRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / New Field:** Scopes the listing under parent instance paths in the URL path: `projects/{project}/locations/{location}/instances/{instance}`.  
`page_size` | `page_size` | `int32` | **Parity Mapped:** Sets pagination limits (coerced down to 1000 max, or 5000 in `CONFIG_ONLY` view). Rename to `pageSize` in JSON.  
`page_token` | `page_token` | `string` | **Parity Mapped:** Paging resumption token. Rename to `pageToken` in JSON.  
— | `filter` | `string` | **New Parameter:** Enables filtering rule listings using standard AIP-160 filter strings (for example, `display_name = "test_rule"`).  
— | `view` | `enum` | **New Parameter:** Selects the rule view scope (`RuleView` enum: `RULE_VIEW_UNSPECIFIED`, `BASIC`, `REVISION_METADATA_ONLY`, `CONFIG_ONLY`, `FULL`, `TRENDS`). Defaults to `BASIC`.  
— | `order_by` | `string` | **New Parameter:** Sets sorting field and direction (for example, `display_name desc`). Rename to `orderBy` in JSON.  
— | `skip` | `int32` | **New Parameter:** Allows bypassing a page offset (only supported in `TRENDS` view).  
  
* * *

## Response payload field-by-field parity

Both APIs return rule arrays and nextPageTokens.

Legacy Field (`ListRulesResponse` V1) | Modern Field (`ListRulesResponse`) | Field type | Parity & Migration Notes  
---|---|---|---  
`rules` | `rules` | `repeated Rule` | **Parity Mapped:** Repeated list of compiled rule items (individual nested maps defined under `GetRule` guide).  
`next_page_token` | `next_page_token` | `string` | **Parity Mapped:** Token to retrieve subsequent pages of rules. Rename to `nextPageToken` in JSON.  
— | `total_size` | `int32` | **New Field:** Estimated total records matching query filters (only populated in `TRENDS` view). Rename to `totalSize` in JSON.  
  
* * *

## Key differences

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings (`parent` path parameter).
  * **Filtering Capabilities:**
    * Standardizes support for standard AIP-160 filter strings (`filter`) enabling users to query rules by reference lists, dates, owners, or alert status.
  * **Paging/View Optimization:**
    * Introduces `view` (to return only basic metadata or configs up to 5k entries per page) and `order_by` rules, improving performance.
  * **IAM Permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/rules.list`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
