---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-create-soar-alert/
title: LegacyCreateSoarAlert APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:38.856992+00:00
---

# LegacyCreateSoarAlert APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-create-soar-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LegacyCreateSoarAlert APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory API (**`CreateSoarAlert`**) to the modern Chronicle API ([**`LegacyCreateSoarAlert`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyCreateSoarAlert)).

## Protocol and mapping overview

Feature | Legacy API (`CreateSoarAlert`) | Modern Chronicle API (`LegacyCreateSoarAlert`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Legacy partner permissions | `chronicle.googleapis.com/legacies.legacyCreateSoarAlert`  
  
* * *

## Request payload field-by-field parity

The legacy call ingested an alert from other SIEM systems using Chronicle SOAR. The modern Chronicle API targets a specific instance path and provides the same alert ingestion capabilities using `LegacyCreateSoarAlertRequest`.

Legacy field (`CreateSoarAlertRequest`) | Modern field (`LegacyCreateSoarAlertRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` (in HTTP path) | `string` | **Google Cloud scoped hierarchy:** In the legacy API, the target customer was authenticated globally without a resource hierarchy path. In the modern API, the request targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`soar_alert` | `soar_alert` | `LegacySoarAlert` | **Parity mapped:** Encapsulates the alert payload to be ingested. Maps directly between `SoarAlert` and `LegacySoarAlert`.  
`soar_alert.soar_alert_id` | `soar_alert.soar_alert_id` | `string` | **Parity mapped:** ID of the alert in the Chronicle SOAR product.  
`soar_alert.start_time` | `soar_alert.start_time` | `google.protobuf.Timestamp` | **Parity mapped:** Start time of the window for which the alert was generated.  
`soar_alert.end_time` | `soar_alert.end_time` | `google.protobuf.Timestamp` | **Parity mapped:** End time of the window for which the alert was generated.  
`soar_alert.detection_time` | `soar_alert.detection_time` | `google.protobuf.Timestamp` | **Parity mapped:** Timestamp when the alert was detected.  
`soar_alert.source_rule` | `soar_alert.source_rule` | `string` | **Parity mapped:** Name of the rule triggering the alert in the source SIEM.  
`soar_alert.source_system_uri` | `soar_alert.source_system_uri` | `string` | **Parity mapped:** URI to the source SIEM system.  
`soar_alert.vendor` | `soar_alert.vendor` | `string` | **Parity mapped:** Name of the vendor.  
`soar_alert.source_system` | `soar_alert.source_system` | `string` | **Parity mapped:** Name of the source SIEM system.  
`soar_alert.product` | `soar_alert.product` | `string` | **Parity mapped:** Name of the product generating the alert.  
`soar_alert.original_ticket_id` | `soar_alert.original_ticket_id` | `string` | **Parity mapped:** Ticket ID for the alert in the source SIEM system.  
`soar_alert.priority` | `soar_alert.priority` | `string` | **Parity mapped:** Priority of the alert.  
`soar_alert.severity` | `soar_alert.severity` | `string` | **Parity mapped:** Severity of the alert.  
`soar_alert.events` | `soar_alert.events` | `repeated SoarEvent` | **Parity mapped:** List of events associated with the alert.  
`soar_alert.description` | `soar_alert.description` | `string` | **Parity mapped:** Description of the alert.  
`soar_alert.summary` | `soar_alert.summary` | `string` | **Parity mapped:** Summary of the alert.  
`soar_alert.name` | `soar_alert.name` | `string` | **Parity mapped:** Name of the alert in the SecOps platform.  
`soar_alert.alert_group_id` | `soar_alert.alert_group_id` | `string` | **Parity mapped:** Alert identifier in SOAR unique per customer, used to enforce idempotency.  
`soar_alert.soar_create_time` | `soar_alert.soar_create_time` | `google.protobuf.Timestamp` | **Parity mapped:** Timestamp when the alert was created in SOAR.  
  
* * *

## Response payload field-by-field parity

The response returns the created SOAR alert resource.

Legacy field (`SoarAlert` response) | Modern field (`LegacySoarAlert` response) | Target type | Parity and migration notes  
---|---|---|---  
`soar_alert_id` | `soar_alert_id` | `string` | **Parity mapped:** ID of the alert in Chronicle SOAR.  
`start_time` | `start_time` | `google.protobuf.Timestamp` | **Parity mapped:** Start time of the window.  
`end_time` | `end_time` | `google.protobuf.Timestamp` | **Parity mapped:** End time of the window.  
`detection_time` | `detection_time` | `google.protobuf.Timestamp` | **Parity mapped:** Detection timestamp.  
`source_rule` | `source_rule` | `string` | **Parity mapped:** Rule name in the source SIEM.  
`source_system_uri` | `source_system_uri` | `string` | **Parity mapped:** Source SIEM system URI.  
`vendor` | `vendor` | `string` | **Parity mapped:** Vendor name.  
`source_system` | `source_system` | `string` | **Parity mapped:** Source SIEM system name.  
`product` | `product` | `string` | **Parity mapped:** Product name.  
`original_ticket_id` | `original_ticket_id` | `string` | **Parity mapped:** Source ticket ID.  
`priority` | `priority` | `string` | **Parity mapped:** Alert priority.  
`severity` | `severity` | `string` | **Parity mapped:** Alert severity.  
`events` | `events` | `repeated SoarEvent` | **Parity mapped:** Related events.  
`description` | `description` | `string` | **Parity mapped:** Alert description.  
`summary` | `summary` | `string` | **Parity mapped:** Alert summary.  
`name` | `name` | `string` | **Parity mapped:** SecOps alert resource name.  
`alert_group_id` | `alert_group_id` | `string` | **Parity mapped:** Idempotency group ID.  
`soar_create_time` | `soar_create_time` | `google.protobuf.Timestamp` | **Parity mapped:** SOAR creation timestamp.  
  
* * *

## Key differences

  * **Google Cloud scoped hierarchy:**
    * The modern Chronicle API targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.
  * **Full payload compatibility:**
    * All fields within `SoarAlert` and nested `SoarEvent` objects map directly to `LegacySoarAlert` and `SoarEvent` with identical types and field tags.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
