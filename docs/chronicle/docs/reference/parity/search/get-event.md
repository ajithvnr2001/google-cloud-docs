---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/get-event/
title: GetEvent parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:24.804311+00:00
---

# GetEvent parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/get-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetEvent parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`GetEvent`**) to the modern Chronicle API (**`GetEvent`**).

## Protocol and mapping overview

Feature | Legacy API (`GetEvent`) | Modern Chronicle API (`GetEvent`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/events.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetEventRequest` targets resources using Google Cloud canonical resource paths with Base64 encoding rules.

Legacy field (`GetEventRequest`) | Modern field (`GetEventRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `bytes` $\rightarrow$ `string` | **Google Cloud scoping, type, and encoding shift:** Legacy accepted a 256-bit raw byte string prefix (`bytes name`). The modern API takes a standard canonical Google Cloud string resource path: `projects/{project}/locations/{location}/instances/{instance}/events/{event_id}`, where `{event_id}` must be URL-encoded Base64 (matching the unencoded binary in `udm.metadata.id`).  
  
* * *

## Response payload field-by-field parity

Both endpoints return the retrieved `Event` representation containing parsed UDM data.

Legacy field (`Event` message) | Modern field (`Event` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | **Parity mapped and format shift:** Legacy returned the raw string event ID. The modern API encapsulates this inside canonical resource names: `projects/{project}/locations/{location}/instances/{instance}/events/{event_id}`, where `{event_id}` is URL-encoded Base64.  
`udm` | `udm` | `backstory.UDM` | **Parity mapped:** Identical structured representation of Unified Data Model (UDM) telemetry event properties.  
  
* * *

## Key differences

  * **Service decoupling:**
    * Legacy event retrieval was housed under the general-purpose `SearchService` alongside searches and log queries.
    * Modern Chronicle API decouples event operations into a dedicated `EventService` resource hierarchy.
  * **Google Cloud project scoping and Base64 encoding:**
    * Scoped natively under parent project instance folder bindings.
    * Rather than transmitting raw 256-bit binary byte identifiers, the modern API requires that event identifiers in resource paths be URL-encoded Base64 strings.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/events.get`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
