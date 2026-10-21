---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/venafi-ztpki-changelog/
title: Change log for VENAFI_ZTPKI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:05:27.652903+00:00
---

# Change log for VENAFI_ZTPKI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/venafi-ztpki-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VENAFI_ZTPKI

Date | Changes  
---|---  
2026-09-23 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `column13` (`created_at`) raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `column2` (`common_name`) raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column17` (`user_id`) raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `column18` (`user_email`) raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `column4` (`subject_dn`), `column21` (`organization_id`) raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `column19` (`account_id`) raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `column20` (`account_name`) raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.network.organization_name`: Newly mapped `column22` (`organization_name`) raw log field with `event.idm.read_only_udm.network.organization_name` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.serial`: Newly mapped `column3` (`serial`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.serial` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.issuer`: Newly mapped `column5` (`issuer_dn`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.issuer` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.not_before`: Newly mapped `column6` (`not_before`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.not_before` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.not_after`: Newly mapped `column7` (`not_after`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.not_after` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.sha1`: Newly mapped `column25` (`fingerprint`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.sha1` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.certificate.sha256`: Newly mapped `column26` (`fingerprint_sha256`) raw log field with `event.idm.read_only_udm.network.tls.client.certificate.sha256` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `column23` (`policy_id`) raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `column24` (`policy_name`) raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column1` (`certificate_id`), `column8` (`signature_algorithm`), `column9` (`revocation_status`), `column10` (`revocation_reason`), `column11` (`revocation_date`), `column12` (`imported`), `column14` (`updated_at`), `column15` (`deleted_at`), `column16` (`certificate_request_id`), `column27` (`key_size`), `column28` (`key_algorithm`), `column29` (`discovered`), `column30` (`private_key_at_rest`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-08-21 |  \- Added a grok pattern to parse new log formats.  
-`event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `api_type`, `transaction_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `deployment_id` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
-`event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.   
2025-10-14 |  Enhancement:  
\- Added a grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `dvc_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `object` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `object_subsystem` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `object_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target_port`: Newly mapped `value1.value` raw log field with `event.idm.read_only_udm.target_port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `value1.name`, `text2.value`, `data.name`, `data.value`, `grouping.name`, `grouping.value`, `value2.name`, `value2.value`, `text1.name`, `text2.name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `text1.value` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is true and `has_target` is true, updated to NETWORK_CONNECTION.   
2025-03-03 |  Enhancement:  
\- Add support for new pattern of csv logs.  
\- Changed mapping for `policy_id` from `security_result.detection_fields` to `security_result.rule_id`.  
\- Changed mapping `common_name` from `principal.resource.attribute.labels` to `principal.user.user_display_name`.  
\- Changed mapping for `not_before` from `security_result.detection_fields` to `network.tls.client.certificate.not_before`.  
\- Changed mapping for `not_after` from `security_result.detection_fields` to `network.tls.client.certificate.not_after`.  
\- Changed mapping for `serial` from `security_result.default_fields` to `network.tls.client.certificate.serial`.  
\- Mapped `key_size` and `key_algorithm` to `security_result.detection_fields`.  
\- Mapped `fingerprint_sha256` to `network.tls.client.certificate.sha256`.  
\- Mapped `fringerprint_sha1` to `network.tls.client.certificate.sha1`.  
\- Mapped `policy_name` to `security_result.rule_name`.  
\- Mapped `issuer_dn` to `network.tls.client.certificate.issuer`.  
\- Changed mapping for `organization_name` from `principal.resource.attribute.labels` to `network.organization_name`.   
2024-12-20 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
