---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-ngfw-enterprise-changelog/
title: Change log for GCP_NGFW_ENTERPRISE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:51.656125+00:00
---

# Change log for GCP_NGFW_ENTERPRISE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-ngfw-enterprise-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_NGFW_ENTERPRISE

Date | Changes  
---|---  
2026-04-28 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `jsonPayload.interceptVpc.vpc`, `jsonPayload.interceptVpc.projectId`, `jsonPayload.threatDetails.repeatCount`, `jsonPayload.threatDetails.detectionTime` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `jsonPayload.threatDetails.type`, `jsonPayload.threatDetails.category` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `jsonPayload.threatDetails.application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `jsonPayload.threatDetails.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.threatDetails.cves`, `jsonPayload.interceptInstance.projectId`, `jsonPayload.interceptInstance.vm`, `jsonPayload.securityProfileGroupDetails.organizationId`, `jsonPayload.@type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.observer.location.name`: Newly mapped `resource.labels.location` raw log field with `event.idm.read_only_udm.observer.location.name` UDM field.  
\- `event.idm.read_only_udm.observer.resource.resource_subtype`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.observer.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.observer.resource.name`: Newly mapped `resource.labels.resource_container` raw log field with `event.idm.read_only_udm.observer.resource.name` UDM field.  
\- `event.idm.read_only_udm.observer.resource.product_object_id`: Newly mapped `resource.labels.id` raw log field with `event.idm.read_only_udm.observer.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: When `jsonPayload.action` is `DROP`, set the value of `event.idm.read_only_udm.security_result.action` to BLOCK.  
\- Modified the internal variable name from `action` to `action_var` for extracting the value mapped to `event.idm.read_only_udm.security_result.action`.   
2024-04-16 |  Enhancement:  
\- Changed mapping of `alert_severity` from `jsonPayload.alert_severity` to `jsonPayload.threatDetails.severity`.  
\- Changed mapping of `threat_id` from `jsonPayload.threat_id` to `jsonPayload.threatDetails.id`.  
\- Changed mapping of `rdspg` from `jsonPayload.security_profile_group` to `jsonPayload.securityProfileGroupDetails.securityProfileGroupId`.  
\- Changed mapping of `rduri` from `jsonPayload.uri_or_filename` to `jsonPayload.threatDetails.uriOrFilename`.  
\- Removed mapping of `jsonPayload.rule_details.priority`, `jsonPayload.rule_details.apply_security_profile_fallback_action`, `jsonPayload.rule_details.source_range`, and `jsonPayload.rule_details.target_secure_tag`.   
2024-03-26 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
