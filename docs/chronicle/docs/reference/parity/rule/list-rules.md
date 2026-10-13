---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/list-rules/
title: ListRules (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:01.240758+00:00
---

# ListRules (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/list-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListRules (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`ListRules`**) to the modern Chronicle API (**`ListRules`**).

## Protocol and mapping overview

Feature | Legacy API (`ListRules` V2) | Modern Chronicle API (`ListRules`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/rules.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListRulesRequest` scopes queries under standard Google Cloud instance resource name parent structures and replaces status enums with flexible filters.

Legacy field (`ListRulesRequest`) | Modern field (`ListRulesRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes the listing under parent instance paths in the URL path: `projects/{project}/locations/{location}/instances/{instance}`.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Sets pagination limits (coerced down to 1000 max, or 5000 in `CONFIG_ONLY` view). Rename to `pageSize` in JSON.  
`page_token` | `page_token` | `string` | **Parity mapped:** Paging resumption token. Rename to `pageToken` in JSON.  
`state` | `filter` | `enum` $\rightarrow$ `string` | **Syntax shift:** Legacy used `state` enum (to filter by archived versus active rules). The modern API handles this using flexible AIP-160 filter strings (for example, `filter = "archived = true"` or `filter = "alerting_enabled = true"`).  
— | `view` | `enum` | **New parameter:** Selects the rule view scope (`RuleView` enum: `RULE_VIEW_UNSPECIFIED`, `BASIC`, `REVISION_METADATA_ONLY`, `CONFIG_ONLY`, `FULL`, `TRENDS`). Defaults to `BASIC`.  
— | `order_by` | `string` | **New parameter:** Sets sorting field and direction (for example, `display_name desc, revision_create_time desc`). Rename to `orderBy` in JSON.  
— | `skip` | `int32` | **New parameter:** Allows bypassing a page offset (only supported in `TRENDS` view).  
  
* * *

## Response payload field-by-field parity

Both APIs return rule arrays and nextPageTokens.

Legacy field (`ListRulesResponse`) | Modern field (`ListRulesResponse`) | Field type | Parity & migration notes  
---|---|---|---  
`rules` | `rules` | `repeated Rule` | **Parity mapped:** Repeated list of compiled rule items (individual nested maps defined under `GetRule` guide).  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Token to retrieve subsequent pages of rules. Rename to `nextPageToken` in JSON.  
— | `total_size` | `int32` | **New field:** Estimated total records matching query filters (only populated in `TRENDS` view). Rename to `totalSize` in JSON.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`parent` path parameter).
  * **Flexible filter decoupling:**
    * The legacy request restricted filtering options to a dedicated enum state (active or archived). The modern API supports flexible AIP-160 query filters enabling users to subset rule listings based on reference lists, dates, owners, or alert status.
  * **Paging and view optimization:**
    * Introduces `view` (to return only basic metadata or configs up to 5k entries per page) and `order_by` rules, improving performance.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/rules.list`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
