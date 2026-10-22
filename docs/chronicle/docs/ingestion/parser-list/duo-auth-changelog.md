---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-auth-changelog/
title: Change log for DUO_AUTH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:13.689986+00:00
---

# Change log for DUO_AUTH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-auth-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DUO_AUTH

Date | Changes  
---|---  
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Added a conditional check before mapping the rawlog field `host` to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` only if `host` is not empty and does not start with `api`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `access_device.key` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2026-01-06 |  Enhancement:  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.browser_version` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `access_device.device_info_source` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.epkey` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.flash_version` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.is_encryption_enabled` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.is_firewall_enabled` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `trusted_endpoint_status` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.is_password_set` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `access_device.java_version` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `application.name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `is_supported` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `trusted_session_uuid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `passport_assessment_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `remembered_factor` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `passport_assessment.is_potential` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `access_device.os` raw log field with `event.idm.read_only_udm.principal.platform` UDM field when the value of `access_device.os` is `iOS` or `Android`.  
\- Updated the values for `factor` in else if condition, for example `verified_duo_push`.   
2025-02-26 |  Enhancement:  
\- Mapped `adaptive_trust_assessments.more_secure_auth.detected_attack_detectors` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.features_version` to `security_result.detection_fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.model_version` to `security_result.detection_fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.policy_enabled` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.preview_mode_enabled` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.reason` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.more_secure_auth.trust_level` to `security_result.detection_fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.features_version` to `security_result.detection_fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.model_version` to `security_result.detection_fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.policy_enabled` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.preview_mode_enabled` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.reason` to `additional.fields`.  
\- Mapped `adaptive_trust_assessments.remember_me.trust_level` to `security_result.detection_fields`.  
\- Mapped changed for `access_device.browser` from `target.resource.attribute.labels` to `principal.resource.attribute.labels`.   
2024-11-26 |  Enhancement:  
\- Mapped `application.destination_name` to `target.application`.   
2024-07-24 |  Enhancement:  
\- Added `duo_mobile_passcode_hotp` in conditional check to map `authMechanism` to `OTP`.   
2024-06-07 |  Enhancement:  
\- Mapped `access_device.ip` to `principal.hostname` when the value of the field is a hostname.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.   
2024-06-05 |  Enhancement:  
\- Mapped `access_device.ip` to `additional.fields` when the value of the field is in a non-IP format.   
2023-10-23 |  Enhancement:  
\- Mapped `msg` to `security_result.summary`.  
\- Mapped `auth_stage` to `metadata.product_event_type`.  
\- Mapped `status` to `security_result.action` and `security_result.action_details`.  
\- Mapped `hostname` to `principal.hostname`.  
\- Mapped `username` to `target.user.userid`.  
\- Mapped `client_ip` to `target.ip`.  
\- Mapped `server_section`, `server_section_ikey`, `client_section`, `log_logger.unpersistable`,  
`log_level.name`, `log_level.__class_uuid__`, `log_namespace`, and `log_source`, and `log_format` to `target.resource.attribute.labels`.   
2023-08-03 |  Enhancement:  
\- As `auth_device.name` sometimes contains a phone number, mapped the same to `target.user.phone_numbers`.  
\- Mapped `user.groups` to `target.user.group_identifiers`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
