---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lookout-mobile-endpoint-security-changelog/
title: Change log for LOOKOUT_MOBILE_ENDPOINT_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:19:18.880633+00:00
---

# Change log for LOOKOUT_MOBILE_ENDPOINT_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lookout-mobile-endpoint-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LOOKOUT_MOBILE_ENDPOINT_SECURITY

Date | Changes  
---|---  
2026-07-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `outcome` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to `SCAN_UNCATEGORIZED` when `event_name` is `THREAT` and principal machine data is present.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `actor.type` (key: `actor_type`), `changeType` (key: `changeType`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `CustomerName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_target_user` is true, updated the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Added support for new format of JSON logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.principal.platform`  
\- `event.idm.read_only_udm.principal.resource.name`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.principal.application`  
\- `event.idm.read_only_udm.principal.asset.hardware.manufacturer`  
\- `event.idm.read_only_udm.principal.asset.hardware.model`  
\- `event.idm.read_only_udm.principal.file.full_path`  
\- `event.idm.read_only_udm.principal.platform_version`  
\- `event.idm.read_only_udm.principal.process.file.full_path`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.severity`  
2024-11-20 |  Enhancement:  
\- Mapped `details.type`, `details.packageSha`, `details.packageName`, `details.assessments`, `details.activationStatus`, `details.securityStatus`, and `details.protectionStatus` to `additional.fields`.  
\- Mapped `details.applicationName` to `principal.application`.  
\- Mapped `details.fileName` to `principal.process.file.full_path`.  
\- Mapped `details.path` to `principal.file.full_path`.  
\- Mapped `target.manufacturer` to `principal.asset.hardware.manufacturer`.  
\- Mapped `target.type` to `principal.resource.name`.   
2024-09-17 |  Enhancement:  
\- Added support for key-value pair log format.   
2024-03-07 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
