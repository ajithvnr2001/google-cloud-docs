---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-create-or-update-case/
title: LegacyCreateOrUpdateCase parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:38.259320+00:00
---

# LegacyCreateOrUpdateCase parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-create-or-update-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LegacyCreateOrUpdateCase parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory API (**`CreateOrUpdateCase`**) to the modern Chronicle API ([**`LegacyCreateOrUpdateCase`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyCreateOrUpdateCase)).

## Protocol and mapping overview

Feature | Legacy API (`CreateOrUpdateCase`) | Modern Chronicle API (`LegacyCreateOrUpdateCase`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Legacy partner permissions | `chronicle.googleapis.com/legacies.legacyCreateOrUpdateCase`  
  
* * *

## Request payload field-by-field parity

The legacy call created or updated a case. The modern Chronicle API targets a specific instance path and provides case creation and update capabilities with backward compatibility for integrations.

Legacy field (`CreateOrUpdateCaseRequest`) | Modern field (`LegacyCreateOrUpdateCaseRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` (in HTTP path) | `string` | **Google Cloud scoped hierarchy:** In the legacy API, the target instance was not specified in the resource path. In the modern API, the request targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`case_resource` | `case_resource` | `LegacyCase` | **Parity mapped:** Encapsulates the case payload to create or update.  
`case_resource.name` | `case_resource.id` | `string` | **Field name change:** In the legacy Backstory API, the case identifier was specified in the `name` field (format: `cases/{case}`). In the modern API, the identifier is provided using the `id` field.  
`case_resource.response_platform_info` | `case_resource.soar_platform_info` | `SoarPlatformInfo` | **Field name change:** Renamed from `response_platform_info` to `soar_platform_info`. Contains case metadata in the customer's SOAR platform.  
`case_resource.response_platform_info.case_id` | `case_resource.soar_platform_info.case_id` | `string` | **Parity mapped:** Identifier of the case in the SOAR platform.  
`case_resource.response_platform_info.response_platform_type` | `case_resource.soar_platform_info.response_platform_type` | `ResponsePlatformType` | **Parity mapped:** Type of SOAR platform. Supported values: `RESPONSE_PLATFORM_TYPE_UNSPECIFIED` (0), `RESPONSE_PLATFORM_TYPE_SIEMPLIFY` (1).  
`case_resource.display_name` | `case_resource.display_name` | `string` | **Parity mapped:** Display name of the case.  
`case_resource.stage` | `case_resource.stage` | `string` | **Parity mapped:** Stage of the case (for example, "Triage", "Assessment", "Investigation", "Incident", "Improvement", "Research", or custom user-defined values).  
`case_resource.priority` | `case_resource.priority` | `Priority` | **Parity mapped:** Case priority (`PRIORITY_UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`).  
`case_resource.status` | `case_resource.status` | `Status` | **Parity mapped:** Case status (`STATUS_UNSPECIFIED`, `OPEN`, `CLOSED`).  
`case_resource.alert_ids` | `case_resource.alert_ids` | `repeated string` | **Parity mapped:** List of alert IDs associated with this case.  
  
* * *

## Response payload field-by-field parity

The response returns the created or updated case resource.

Legacy field (`Case` response) | Modern field (`LegacyCase` response) | Target type | Parity and migration notes  
---|---|---|---  
`name` | `id` | `string` | **Field name change:** In the legacy Backstory API, the case identifier was returned in `name` (format: `cases/{case}`). In the modern API, the identifier is returned in `id`.  
`response_platform_info` | `soar_platform_info` | `SoarPlatformInfo` | **Field name change:** Renamed from `response_platform_info` to `soar_platform_info`.  
`response_platform_info.case_id` | `soar_platform_info.case_id` | `string` | **Parity mapped:** Case ID in the customer's SOAR platform.  
`response_platform_info.response_platform_type` | `soar_platform_info.response_platform_type` | `ResponsePlatformType` | **Parity mapped:** Response platform type enum identifier.  
`display_name` | `display_name` | `string` | **Parity mapped:** Display name of the case.  
`stage` | `stage` | `string` | **Parity mapped:** Case stage identifier.  
`priority` | `priority` | `Priority` | **Parity mapped:** Priority level of the case.  
`status` | `status` | `Status` | **Parity mapped:** Status of the case.  
`alert_ids` | `alert_ids` | `repeated string` | **Parity mapped:** Associated alert IDs.  
  
* * *

## Key differences

  * **Google Cloud scoped hierarchy:**
    * The modern Chronicle API targets a specific instance path: `projects/{project}/locations/{location}/instances/{instance}`.
  * **Identifier field naming:**
    * The legacy Backstory API represented the case identifier using `name` (`cases/{case}`), while the modern API accepts and returns the identifier in the `id` field.
  * **SOAR platform field naming:**
    * The legacy Backstory API uses `response_platform_info` (`ResponsePlatformInfo`), whereas the modern API uses `soar_platform_info` (`SoarPlatformInfo`), preserving the same nested field structure (`case_id` and `response_platform_type`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
