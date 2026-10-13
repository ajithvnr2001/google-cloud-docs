---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/list-data-taps/
title: ListDataTaps parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:45.091278+00:00
---

# ListDataTaps parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/list-data-taps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListDataTaps parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Data Tap API (**`ListDataTaps`**) to the modern Chronicle API (**`ListDataTaps`**).

## Protocol and mapping overview

Feature | Legacy API (`ListDataTaps`) | Modern Chronicle API (`ListDataTaps`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/dataTaps.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListDataTapsRequest` requires scoping under a parent Google Cloud instance path.

Legacy Field (`ListDataTapsRequest`) | Modern Field (`ListDataTapsRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context:** Scopes the list target under parent projects using the standard resource name path in the URL. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`page_size` | `page_size` | `int32` | **Parity Mapped:** Pagination page size limits. Rename to `pageSize` in JSON payloads.  
`page_token` | `page_token` | `string` | **Parity Mapped:** Paging resumption token. Rename to `pageToken` in JSON payloads.  
  
* * *

## Response payload field-by-field parity

Both APIs return pagination results with matching nested models.

Legacy Field (`ListDataTapsResponse` message) | Modern Field (`ListDataTapsResponse` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`data_taps` | `data_taps` | `repeated DataTap` | **Parity Mapped:** Array list of data taps (with nested field translations evaluated under `CreateDataTap` or `GetDataTap`). Rename to `dataTaps` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Parity Mapped:** Next page resumption token. Rename to `nextPageToken` in JSON.  
  
* * *

## Key differences

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Explicit Paging Token Behavior:**
    * The modern Chronicle API follows standard Google Cloud paging checkpoint logic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
