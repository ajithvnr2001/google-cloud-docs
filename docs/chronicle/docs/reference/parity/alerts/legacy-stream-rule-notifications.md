---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/alerts/legacy-stream-rule-notifications/
title: StreamRuleNotifications parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:39.883127+00:00
---

# StreamRuleNotifications parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/alerts/legacy-stream-rule-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# StreamRuleNotifications parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine API (**`StreamRuleNotifications`**) to the modern Chronicle API ([**`LegacyStreamDetectionAlerts`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyStreamDetectionAlerts)) defined under the `google.cloud.chronicle.v1main` package.

## Protocol and mapping overview

Feature | Legacy API (`StreamRuleNotifications`) | Modern API (`LegacyStreamDetectionAlerts`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacyStreamDetectionAlerts`  
  
* * *

## Request payload field-by-field parity

The modern `LegacyStreamDetectionAlertsRequest` extends query options by adding standard instance parents, simulated data visibility scopes, connection controls, and composite alert models.

Legacy field (`StreamRuleNotificationsRequest`) | Modern field (`LegacyStreamDetectionAlertsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** Scopes the connection target using the standard resource path model in the URL path. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`continuation_time` | `continuation_time` | `Timestamp` | **Parity mapped (deprecated):** Start timestamp checkpoint. Omit if launching a new stream using page tokens.  
`max_size` | `detection_batch_size` | `int32` | **Parity mapped / renamed:** The maximum number of detections returned in a single batch. Maps directly to `detectionBatchSize`.  
— | `page_token` | `string` | **New parameter:** Page resumption token parsed on reconnection.  
— | `page_start_time` | `Timestamp` | **New parameter:** Start timestamp of the first page-token-based stream.  
— | `max_detections` | `int32` | **New parameter:** Limit on the total number of streamed detections returned before the server automatically closes the connection.  
— | `composite_alert_handling` | `enum` | **New parameter:** Configures compilation of composite alerts (for example, `FLATTEN_EVENTS_ENTITIES`).  
— | `include_simulated_detections` | `bool` | **New parameter (deprecated):** Toggles whether simulated indicators are returned. Prefer `simulated_data_visibility`.  
— | `simulated_data_visibility` | `enum` | **New parameter:** Configures visibility filtering on simulated test rules results.  
  
* * *

## Response payload field-by-field parity

The response stream returns batches of detection alert records.

Legacy field (`StreamRuleNotificationsResponse` message) | Modern field (`LegacyStreamDetectionAlertsResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`notifications` | `detections` | `repeated Collection` | **Parity mapped / restructured:** Mapped from the legacy list of rule notifications to a repeated list of backstory `Collection` resources representing rule detection alerts containing UDM events and metadata.  
`continuation_time` | `continuation_time` | `Timestamp` | **Deprecated:** Reconnection timestamp. Note: Only populated if the stream request was initialized using legacy `continuation_time`.  
— | `heartbeat` | `bool` | **New parameter:** A boolean indicating if the stream message is a keep-alive heartbeat ping during periods of zero alerts.  
— | `next_page_token` | `string` | **New parameter:** The token value to pass back as `page_token` on reconnection.  
— | `next_page_start_time` | `Timestamp` | **New parameter:** Start timestamp for paging returned when no page token is pending.  
  
* * *

## Key differences analysis

  1. **Rule change events vs. live detection alerts:**
     * Legacy `StreamRuleNotifications` streamed operations and error statuses alongside standard match configurations.
     * The modern `LegacyStreamDetectionAlerts` API focuses exclusively on streaming live parsed threat detection outcomes represented as standard collections.
  2. **Google Cloud instance bounds:**
     * Legacy rule streams retrieved detections using global connection tokens.
     * The modern `LegacyStreamDetectionAlerts` API scopes rules execution directly under the instance path (`projects/{project}/locations/{location}/instances/{instance}`) mapped as standard parent.
  3. **Standard pagination:**
     * Continuation timestamps are replaced by built-in `page_token` paging limits, preventing sync gaps.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
