---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/get-detection/
title: GetDetection (V2) parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:24.146161+00:00
---

# GetDetection (V2) parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/rule/get-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetDetection (V2) parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Rules Engine V2 API (**`GetDetection`**) to the modern Chronicle API (**`LegacyGetDetection`**).

## Protocol and mapping overview

Feature | Legacy API (`GetDetection` V2) | Modern Chronicle API (`LegacyGetDetection`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/legacies.legacyGetDetection`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `LegacyGetDetectionRequest` scopes queries under parent project instances and renames segment path parameters.

Legacy field (`GetDetectionRequest`) | Modern field (`LegacyGetDetectionRequest`) | Field type | Parity & migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context / new field:** Scopes extraction under target instance environments: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`version_id` | `rule_id` | `string` | **Renamed:** Target rule identification segment name (can accept `{rule_id}` or `{rule_id}@{revision_id}`). Rename to `ruleId` in JSON. Note: Proto tag number changed from 1 to 2.  
`detection_id` | `detection_id` | `string` | **Direct map / identical:** Opaque detection identifier string. Rename to `detectionId` in JSON. Note: Proto tag number changed from 2 to 3.  
  
* * *

## Response payload field-by-field parity

Both endpoints return the identical parsed telemetry detection Collection output.

Legacy field (`.backstory.Collection` response) | Modern field (`.backstory.Collection` response) | Field type | Parity & notes  
---|---|---|---  
`.backstory.Collection` | `.backstory.Collection` | `Collection` | **Parity mapped:** Returns the matching detection resource representation under identical structures.  
  
* * *

## Key differences

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Proto tag rearrangements:**
    * Proto tags in requests shifted to accommodate parent path integrations (`rule_id` tag from 1 to 2, `detection_id` from 2 to 3).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/legacies.legacyGetDetection`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
