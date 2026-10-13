---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/delete-data-tap/
title: DeleteDataTap parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:14.904925+00:00
---

# DeleteDataTap parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/delete-data-tap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DeleteDataTap parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Data Tap API (**`DeleteDataTap`**) to the modern Chronicle API (**`DeleteDataTap`**).

## Protocol and mapping overview

Feature | Legacy API (`DeleteDataTap`) | Modern Chronicle API (`DeleteDataTap`)  
---|---|---  
**HTTP Method** | `DELETE` | `DELETE`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/dataTaps.delete`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `DeleteDataTapRequest` targets resources using Google Cloud resource name paths.

Legacy Field (`DeleteDataTapRequest`) | Modern Field (`DeleteDataTapRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context:** The legacy request used path format `dataTaps/<tap_id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/dataTaps/{id}`.  
  
* * *

## Response payload field-by-field parity

Both APIs return an empty response message.

Legacy Field | Modern Field | Field type | Parity & Migration Notes  
---|---|---|---  
`google.protobuf.Empty` | `google.protobuf.Empty` | `Empty` | **Parity Mapped:** Successful requests return HTTP 200 OK (mapping to an empty response object `{}`).  
  
* * *

## Key differences

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Resource Path Renaming:**
    * Legacy path formats `dataTaps/<id>` are migrated to standard Google Cloud path parameters `projects/*/locations/*/instances/*/dataTaps/<id>`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
