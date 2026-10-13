---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-update-alert/
title: LegacyUpdateAlert APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:40.735243+00:00
---

# LegacyUpdateAlert APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/dai/legacy-update-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LegacyUpdateAlert APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the Legacy Backstory API (**`UpdateAlert`**) to the modern Chronicle API ([**`LegacyUpdateAlert`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyUpdateAlert)).

## Protocol and mapping overview

Feature | Legacy API (`UpdateAlert`) | Modern Chronicle API (`LegacyUpdateAlert`)  
---|---|---  
**HTTP method** | `PATCH` | `POST`  
**Permissions** | Legacy partner permissions | `chronicle.googleapis.com/legacies.legacyUpdateAlert`  
  
* * *

## Request payload field-by-field parity

The legacy call updated an alert with analyst-supplied feedback and metadata. The modern Chronicle API targets a specific instance path and updates the alert using the `LegacyUpdateAlertRequest` payload.

Legacy field (`UpdateAlertRequest`) | Modern field (`LegacyUpdateAlertRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` (in HTTP path) | `string` | **Google Cloud scoped hierarchy:** In the legacy API, the target customer was authenticated globally without a resource hierarchy path. In the modern API, the request targets a specific instance resource path: `projects/{project}/locations/{location}/instances/{instance}`.  
`id` | `alert_id` | `string` | **Field name change:** In the legacy API, the alert identifier was passed in the `id` field. In the modern API, the identifier is provided using `alert_id`.  
`case_name` | `case_name` | `string` | **Parity mapped:** The resource name of the case that the alert is associated with.  
`response_platform_info` | `response_platform_info` | `ResponsePlatformInfo` | **Parity mapped:** Response platform info associated with the alert.  
`response_platform_info.case_id` | `response_platform_info.case_id` | `string` | **Parity mapped:** Identifier of the case in the SOAR platform.  
`response_platform_info.response_platform_type` | `response_platform_info.response_platform_type` | `ResponsePlatformType` | **Parity mapped:** Type of SOAR platform. Supported values: `RESPONSE_PLATFORM_TYPE_UNSPECIFIED` (0), `RESPONSE_PLATFORM_TYPE_SIEMPLIFY` (1).  
`feedback` | `feedback` | `LegacyFeedback` | **Parity mapped:** Analyst-supplied feedback on the alert. Maps to `LegacyFeedback` in the modern API.  
`feedback.idp_user_id` | `feedback.idp_user_id` | `string` | **Parity mapped:** Unique identifier supplied by the customer's identity provider (IDP) for the user who provided feedback.  
`feedback.created_time` | `feedback.create_time` | `google.protobuf.Timestamp` | **Field name change:** Renamed from `created_time` in legacy to AIP-compliant `create_time` in the modern API.  
`feedback.verdict` | `feedback.verdict` | `Verdict` | **Parity mapped:** Verdict on whether the finding reflects a security incident.  
`feedback.reputation` | `feedback.reputation` | `Reputation` | **Parity mapped:** Categorization of the finding as useful or not useful.  
`feedback.confidence_score` | `feedback.confidence_score` | `int32` | **Parity mapped:** Confidence score (0-100) of the finding.  
`feedback.risk_score` | `feedback.risk_score` | `int32` | **Parity mapped:** Risk score (0-100) of the finding.  
`feedback.disregarded` | `feedback.disregarded` | `bool` | **Parity mapped:** Indicates whether the analyst disregarded the event.  
`feedback.severity` | `feedback.severity` | `int32` | **Parity mapped:** Severity score (1-100) of the finding.  
`feedback.comment` | `feedback.comment` | `string` | **Parity mapped:** Analyst comment.  
`feedback.status` | `feedback.status` | `Status` | **Parity mapped:** Alert status.  
`feedback.priority` | `feedback.priority` | `Priority` | **Parity mapped:** Alert priority.  
`feedback.root_cause` | `feedback.root_cause` | `string` | **Parity mapped:** Root cause of the alert.  
`feedback.reason` | `feedback.reason` | `Reason` | **Parity mapped:** Reason for closing the alert.  
`feedback.severity_display` | `feedback.severity_display` | `string` | **Parity mapped:** Severity display name for UI and filtering.  
`feedback.priority_display` | — | `string` | **Retired:** Display string for priority is omitted from `LegacyFeedback`.  
`feedback.triage_agent_investigation_id` | `feedback.triage_agent_investigation_id` | `string` | **Parity mapped:** Investigation ID of the latest investigation performed by the Triage Agent.  
`feedback.user_type` | `feedback.user_type` | `UserType` | **Parity mapped:** Type of user that submitted or updated the feedback (`USER_TYPE_UNSPECIFIED`, `ANALYST`, `TRIAGE_AGENT`).  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory API and the modern Chronicle API return the `Collection` resource containing the updated alert data and associated feedback.

Legacy field (`Collection` response) | Modern field (`Collection` response) | Target type | Parity and migration notes  
---|---|---|---  
`id` | `id` | `string` | **Parity mapped:** Unique identifier for the collection.  
`type` | `type` | `CollectionType` | **Parity mapped:** Collection type (for example, `ALERT`).  
`alert_details` | `alert_details` | `AlertDetails` | **Parity mapped:** Alert-specific details and investigation state.  
`feedback` | `feedback` | `repeated Feedback` | **Parity mapped:** List of user and agent feedback entries recorded on the alert.  
  
* * *

## Key differences

  * **HTTP method and endpoint path:**
    * The legacy Backstory API used HTTP `PATCH` with `/v1/alert/updatealert`.
    * The modern Chronicle API uses HTTP `POST` with the resource hierarchy path: `projects/{project}/locations/{location}/instances/{instance}/legacy:legacyUpdateAlert`.
  * **Alert identifier field:**
    * The alert identifier parameter was renamed from `id` in the legacy request to `alert_id` in the modern request.
  * **Feedback field refinements:**
    * The timestamp field `created_time` was renamed to `create_time` to align with AIP standards.
    * The deprecated `priority_display` string field was retired.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
