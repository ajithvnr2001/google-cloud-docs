---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/bigquery/provide-bigquery-access/
title: ProvideBigQueryAccess APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:02.523319+00:00
---

# ProvideBigQueryAccess APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/bigquery/provide-bigquery-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ProvideBigQueryAccess APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory API (**`UpdateBigQueryAccess`**) to the modern Chronicle API ([**`ProvideBigQueryAccess`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.bigQueryAccess/provide)).

## Protocol and mapping overview

Feature | Legacy API (`UpdateBigQueryAccess`) | Modern Chronicle API (`ProvideBigQueryAccess`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Legacy partner permissions | `chronicle.bigQueryAccess.provide`  
  
* * *

## Request payload field-by-field parity

The legacy call set BigQuery access permissions (read/write) for a customerID. The modern Chronicle API targets a specific instance path and standardizes dataset query permissions.

Legacy field (`UpdateBigQueryAccessRequest`) | Modern field (`ProvideBigQueryAccessRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_id` | `parent` (in HTTP path) | `string` | **Google Cloud scoped hierarchy:** In the legacy API, the target customer was identified globally by `customer_id`. In the modern API, the request targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`email` | `email` | `string` | **Parity mapped:** Identifies the user email obtaining access.  
`write_access` | — | `bool` | **Retired:** The modern Chronicle API standardizes user dataset queries as read-only, removing client-managed writes.  
  
* * *

## Response payload field-by-field parity

The response maps properties for user identifiers and roles.

Legacy field (`BigQueryAccess` response) | Modern field (`BigQueryAccess` response) | Target type | Parity and migration notes  
---|---|---|---  
— | `name` | `string` | **New field:** Standard resource name identifier of the BigQuery access resource. Format: `projects/{project}/locations/{location}/instances/{instance}/bigQueryAccess`.  
`email` | `email` | `string` | **Parity mapped:** User email address.  
`roles` | `roles` | `repeated BigQueryAccessRole` | **Parity mapped:** List of roles assigned. Members of `BigQueryAccessRole` contain a single `name` field that maps to legacy roles.  
`roles[].name` (Legacy `Role.name`) | `roles[].name` (Modern `BigQueryAccessRole.name`) | `string` | **Parity mapped:** Role string identifier.  
  
* * *

## Key differences

  * **Write access deprecated:**
    * Legacy clients could explicitly request write access using `write_access = true`.
    * The modern Chronicle API standardizes BigQuery access for user analysis as read-only table querying, removing the client-wide `write_access` parameter.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
