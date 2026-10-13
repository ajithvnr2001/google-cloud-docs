---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/get-collector/
title: GetCollector parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:22.487253+00:00
---

# GetCollector parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/get-collector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetCollector parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Ingestion Collector API (**`GetCollector`**) to the modern Chronicle API (**`GetCollector`**).

## Protocol and mapping overview

Feature | Legacy API (`GetCollector`) | Modern Chronicle API (`GetCollector`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/collectors.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetCollectorRequest` targets resources using Google Cloud resource name paths.

Legacy field (`GetCollectorRequest`) | Modern field (`GetCollectorRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the connection target using the standard resource path in the HTTP URL path. Pattern: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}/collectors/{collector_id}`.  
  
* * *

## Response payload field-by-field parity

Both APIs return the requested `Collector` representation.

Legacy field (`Collector` message) | Modern field (`Collector` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | **Parity mapped:** Contains the standard canonical resource path: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}/collectors/{collector_id}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`config` | `config` | `CollectorConfig` | Contains equivalent log source and network settings.  
`state` | `state` | `enum` | Maps directly to `State` enum (values: `ACTIVE`, `SUSPENDED`).  
`type` | `type` | `enum` | Maps directly to `Type` enum (values: `FILE`, `KAFKA`, `PCAP`, `SPLUNK`, `WEBPROXY`, `SYSLOG`).  
`override_timezone` | `override_timezone` | `bool` | Rename to `overrideTimezone` in JSON responses.  
`time_zone` | `time_zone` | `string` | Rename to `timeZone` in JSON responses.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Resource path renaming:**
    * Legacy path formats `forwarders/<forwarder_id>/collectors/<collector_id>` are migrated to standard Google Cloud path parameters `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}/collectors/{collector_id}`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
