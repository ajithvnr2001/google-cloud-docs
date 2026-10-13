---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/update-collector/
title: UpdateCollector parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:05.099800+00:00
---

# UpdateCollector parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/forwarder/update-collector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateCollector parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Ingestion Collector API (**`UpdateCollector`**) to the modern Chronicle API (**`UpdateCollector`**).

## Protocol and mapping overview

Feature | Legacy API (`UpdateCollector`) | Modern Chronicle API (`UpdateCollector`)  
---|---|---  
**HTTP method** | `PATCH` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/collectors.update`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `UpdateCollectorRequest` targets resources using Google Cloud resource name paths and enforces `PATCH` partial updates using a field mask.

Legacy field (`UpdateCollectorRequest` / `Collector`) | Modern field (`UpdateCollectorRequest` / `Collector`) | Field type | Parity and migration notes  
---|---|---|---  
`collector.name` | `collector.name` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** The legacy request used path format `forwarders/<forwarder_id>/collectors/<collector_id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder_id}/collectors/{collector_id}`.  
`collector.display_name` | `collector.display_name` | `string` | **Parity mapped:** Display name of the collector. Rename to `displayName` in JSON payloads.  
`collector.config` | `collector.config` | `CollectorConfig` | **Parity mapped:** Configuration settings mapping (sources, filters, networks).  
`collector.override_timezone` | `collector.override_timezone` | `bool` | **Parity mapped:** Toggles timezone overrides. Rename to `overrideTimezone` in JSON payloads.  
`collector.time_zone` | `collector.time_zone` | `string` | **Parity mapped:** Target timezone override. Rename to `timeZone` in JSON payloads.  
`update_mask` | `update_mask` | `FieldMask` | **Parity mapped:** Standard FieldMask selects which properties are modified in the `PATCH` request (must include the target fields, for example, `display_name`). Rename to `updateMask` in JSON.  
`collector.state` | — | — | **Ignored / output-only:** The state is set by the system and ignored during update requests.  
`collector.type` | — | — | **Ignored / output-only:** Collector types are immutable post-creation and cannot be modified using update `PATCH` calls.  
  
* * *

## Response payload field-by-field parity

Both responses return the modified `Collector` message representation.

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
