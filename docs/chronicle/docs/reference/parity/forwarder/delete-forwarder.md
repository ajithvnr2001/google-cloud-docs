---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/delete-forwarder/
title: DeleteForwarder parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:13.628029+00:00
---

# DeleteForwarder parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/delete-forwarder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DeleteForwarder parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Ingestion Forwarder API (**`DeleteForwarder`**) to the modern Chronicle API (**`DeleteForwarder`**).

## Protocol and mapping overview

Feature | Legacy API (`DeleteForwarder`) | Modern Chronicle API (`DeleteForwarder`)  
---|---|---  
**HTTP method** | `DELETE` | `DELETE`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/forwarders.delete`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `DeleteForwarderRequest` targets resources using Google Cloud resource name paths.

Legacy field (`DeleteForwarderRequest`) | Modern field (`DeleteForwarderRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** The legacy request used path format `forwarders/<forwarder_id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}`.  
  
* * *

## Response payload field-by-field parity

Both APIs return an empty response message.

Legacy field | Modern field | Field type | Parity and migration notes  
---|---|---|---  
`google.protobuf.Empty` | `google.protobuf.Empty` | `Empty` | **Parity mapped:** Successful requests return HTTP 200 OK (mapping to an empty response object `{}`).  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Resource path renaming:**
    * Legacy path formats `forwarders/<forwarder_id>` are migrated to standard Google Cloud path parameters `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
