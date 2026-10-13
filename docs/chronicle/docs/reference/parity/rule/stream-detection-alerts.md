---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/stream-detection-alerts/
title: StreamDetectionAlerts (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:03.908014+00:00
---

# StreamDetectionAlerts (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/stream-detection-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# StreamDetectionAlerts (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`StreamDetectionAlerts`**) to the modern Chronicle API (**`LegacyStreamDetectionAlerts`**).

## Protocol and mapping overview

Feature | Legacy API (`StreamDetectionAlerts` V2) | Modern Chronicle API (`LegacyStreamDetectionAlerts`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacyStreamDetectionAlerts`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacyStreamDetectionAlertsRequest` scopes search queries under parent project instances and renames segment path parameters.

Legacy field (`StreamDetectionAlertsRequest`) | Modern field (`LegacyStreamDetectionAlertsRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes the streaming connection under target instance environments: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`continuation_time` | `continuation_time` | `Timestamp` | **Direct map / tag shift:** Opaque timestamp where listing resumes. Note: Proto tag number changed from 1 to 2. Rename to `continuationTime` in JSON.  
`detection_batch_size` | `detection_batch_size` | `int32` | **Direct map / tag shift:** Page size batch limits. Note: Proto tag number changed from 2 to 3. Rename to `detectionBatchSize` in JSON.  
— | `max_detections` | `int32` | **New parameter:** Automatically closes the streaming connection after returning $N$ total detections (primarily used for parsing tests and probes). Rename to `maxDetections` in JSON.  
`page_token` | `page_token` | `string` | **Direct map / tag shift:** Resumption token. Note: Proto tag number changed from 3 to 6. Rename to `pageToken` in JSON.  
`page_start_time` | `page_start_time` | `Timestamp` | **Direct map / tag shift:** Timestamp where token-based pagination begins. Note: Proto tag number changed from 4 to 7. Rename to `pageStartTime` in JSON.  
`composite_alert_handling` | `composite_alert_handling` | `enum` | **Direct map / tag shift:** Enum handling rules (`FLATTEN_EVENTS_ENTITIES`). Note: Proto tag number changed from 5 to 8. Rename to `compositeAlertHandling` in JSON.  
`include_simulated_detections` | `include_simulated_detections` or `simulated_data_visibility` | `bool` or `enum` | **Direct map / tag shift:** Visibility toggle. Note: Proto tag number changed to 9 and 10.  
  
* * *

## Response payload field-by-field parity

Both streaming APIs return matching output blocks.

Legacy field (`StreamDetectionAlertsResponse`) | Modern field (`LegacyStreamDetectionAlertsResponse`) | Field type | Parity & migration notes  
---|---|---|---  
`detections` | `detections` | `repeated Collection` | **Direct map / identical:** Repeated list of detections in Collection format.  
`continuation_time` | `continuation_time` | `Timestamp` | **Direct map / identical:** continuation timestamp checkpoint. Rename to `continuationTime` in JSON.  
`heartbeat` | `heartbeat` | `bool` | **Direct map / identical:** Connection keepalive status indicator.  
`next_page_token` | `next_page_token` | `string` | **Direct map / identical:** Resume token. Rename to `nextPageToken` in JSON.  
`next_page_start_time` | `next_page_start_time` | `Timestamp` | **Direct map / identical:** Start time for next paging query. Rename to `nextPageStartTime` in JSON.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Proto tag rearrangements:**
    * Proto tags in requests shifted to accommodate parent path integrations (for example, `continuation_time` tag from 1 to 2, `detection_batch_size` from 2 to 3, `page_token` to 6, `page_start_time` to 7).
  * **Graceful connection closure:**
    * Introduces `max_detections` so integration probers can specify exactly when the stream should close automatically instead of keeping open-ended connections.
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacyStreamDetectionAlerts`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
