---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/list-forwarders/
title: ListForwarders parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:51.824230+00:00
---

# ListForwarders parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/list-forwarders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListForwarders parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Ingestion Forwarder API (**`ListForwarders`**) to the modern Chronicle API (**`ListForwarders`**).

## Protocol and mapping overview

Feature | Legacy API (`ListForwarders`) | Modern Chronicle API (`ListForwarders`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/forwarders.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListForwardersRequest` requires parent scoping.

Legacy field (`ListForwardersRequest`) | Modern field (`ListForwardersRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the list target under parent projects using the standard resource name path in the URL. Pattern: `projects/{project}/locations/{location}/instances/{instance}`.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Pagination page size limits. Rename to `pageSize` in JSON payloads.  
`page_token` | `page_token` | `string` | **Parity mapped:** Paging resumption token. Rename to `pageToken` in JSON payloads.  
  
* * *

## Response payload field-by-field parity

Both APIs return pagination results with matching nested models.

Legacy field (`ListForwardersResponse` message) | Modern field (`ListForwardersResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`forwarders` | `forwarders` | `repeated Forwarder` | **Parity mapped:** Array list of forwarders (with nested field translations evaluated under `CreateForwarder` or `GetForwarder`). Rename to `forwarders` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Next page resumption token. Rename to `nextPageToken` in JSON.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Explicit paging token behavior:**
    * While the legacy backstory endpoint defined `next_page_token` and request pagers, pagination wasn't fully supported consistently in all backstory systems. The Chronicle API provides standard Google Cloud paging checkpoint logic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
