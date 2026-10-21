---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-model-armor-changelog/
title: Change log for GCP_MODEL_ARMOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:27:13.284702+00:00
---

# Change log for GCP_MODEL_ARMOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-model-armor-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_MODEL_ARMOR

Date | Changes  
---|---  
2026-04-20 |  \- `event.idm.read_only_udm.security_result.description`: Newly mapped `jsonPayload.sanitizationResult.sanitizationVerdictReason` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `jsonPayload.sanitizationResult.sanitizationVerdict` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `labels.modelarmor.googleapis.com/client_correlation_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `labels.modelarmor.googleapis.com/client_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `labels.modelarmor.googleapis.com` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-19 |  \- Newly created Parser  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `jsonPayload.@type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `jsonPayload.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `resource.labels.location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.labels.resource_container` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `logName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.executionState` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped raw log field `jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.dangerous.matchState`,`jsonPayload.sanitizationResult.filterResults.sdp.sdpFilterResult.inspectResult.matchState`,`jsonPayload.sanitizationResult.filterResults.sdp.sdpFilterResult.inspectResult.executionState`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.sexually_explicit.matchState`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.sexually_explicit.confidenceLevel`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.hate_speech.matchState`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.hate_speech.confidenceLevel`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.harassment.matchState`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.raiFilterTypeResults.harassment.confidenceLevel`,`jsonPayload.sanitizationResult.filterResults.pi_and_jailbreak.piAndJailbreakFilterResult.confidenceLevel`,`jsonPayload.sanitizationResult.filterResults.malicious_uris.maliciousUriFilterResult.matchState`,`jsonPayload.sanitizationResult.filterResults.malicious_uris.maliciousUriFilterResult.executionState`,`jsonPayload.sanitizationResult.filterResults.csam.csamFilterFilterResult.matchState`,`jsonPayload.sanitizationResult.filterResults.csam.csamFilterFilterResult.executionState`,`jsonPayload.filterConfig.piAndJailbreakFilterSettings.confidenceLevel`,`raiFilter.filterType`,`raiFilter.confidenceLevel` with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped raw log field `resource.labels`,`template_id` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.sanitizationResult.invocationResult`,`jsonPayload.sanitizationResult.filterResults.rai.raiFilterResult.matchState`,`jsonPayload.sanitizationResult.filterResults.pi_and_jailbreak.piAndJailbreakFilterResult.matchState`,`jsonPayload.sanitizationResult.filterResults.pi_and_jailbreak.piAndJailbreakFilterResult.executionState`,`jsonPayload.sanitizationResult.filterMatchState`,`jsonPayload.sanitizationInput.text`,`operation_type`,`labels.modelarmor.googleapis.com/operation_type`,`jsonPayload.filterConfig.maliciousUriFilterSettings.filterEnforcement`, `jsonPayload.filterConfig.piAndJailbreakFilterSettings.filterEnforcement`, `jsonPayload.filterConfig.sdpSettings.basicConfig.filterEnforcement` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `GCP_MODEL_ARMOR`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `GCP_MODEL_ARMOR`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
