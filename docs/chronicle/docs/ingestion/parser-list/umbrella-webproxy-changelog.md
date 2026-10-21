---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-webproxy-changelog/
title: Change log for UMBRELLA_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:32:26.315102+00:00
---

# Change log for UMBRELLA_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UMBRELLA_WEBPROXY

Date | Changes  
---|---  
2026-06-01 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed the mapping of `column52` raw log field from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields as it represents intermediary IP value.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `column52` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field by adding grok pattern.  
\- `event.idm.read_only_udm.additional.fields`: Removed the mapping of `column25` raw log field from `event.idm.read_only_udm.additional.fields` UDM field for index value 0 as it represents resource type value.  
\- `event.idm.read_only_udm.intermediary.resource.type`: Mapped `column25` raw log field with `event.idm.read_only_udm.intermediary.resource.type` UDM field for index value 0.   
2026-05-25 |  Enhancement:  
\- `event.idm.read_only_udm.network.application_protocol`: If `appProto` is WSS, updated the value to HTTPS, and if `appProto` is WS, updated the value to HTTP.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `column55` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `egress_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM fields when `egress_ip` is a valid IP address.   
2025-11-11 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type : Newly mapped `type_of_log` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id : Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mdl` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `gdpr` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_seg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `_ses` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `pbc` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `fpa` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `fpan` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `uht` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `d` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `d` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2025-10-19 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `ihostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `ihostname` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.location.name: Newly mapped `ilocation` raw log field with `event.idm.read_only_udm.intermediary.location.name` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ai_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `egressip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `egressip` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field if `egressip` is a valid IP address.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `egressip` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `egressip` is not a valid IP address.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `identity` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.observer.asset.hostname: Newly mapped `identity` raw log field with `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `time_based_rule` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `policy_reasons` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `application_entity_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application_entity_category` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-06-11 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `verdict` field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `identityType` field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column38` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column41` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column42` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column43` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.domain.name: Newly mapped `column44` field with `event.idm.read_only_udm.target.domain.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column46` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column49` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identityTypeV8` field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-27 |  Enhancement:  
\- Added support for a new pattern of CSV logs with a different header.  
\- event.idm.read_only_udm.additional.fields: Mapped `column5`, `column7`, `column9`, `column11`, `column12`, `column13`, `column15`, `column20`, `column30`, `column33`, `column34`, `column36`, `column38`, `column39`, `column40`, `column43`, `column47`, `column48`, `column49`, `column51`, `column54`, `column55`, `column56`, `column57`, `column58`, `column59`, `column60`, `column63`, `column65`, `column66`, `column67`, ``column68``, ``column69`` and `column70` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Renamed fields: `column4` to `verdict`, `column6` to `rulesetID`, `column8` to `ruleID`, `column10` to `destinationListID`, `column16` to `identitiesV8`, `column17` to `identityTypeV8`, `column18` to `identity`, `column19` to `identityType`, `column21` to `internalIp`, `column22` to `externalIp`, `column24` to `destinationIp`, `column35` to `contentType`, `column37` to `fileName`, `column41` to `requestSize`, `column42` to `responseSize`, `column44` to `referer`, `column45` to `userAgent`, `column46` to `statusCode`, `column50` to `sha`,`column52` to `ampDisposition`,`column53` to `ampDisposition`,`column61` to `requestMethod` in order to map them to the respective UDM fields as per theexisting mappings present in the `umbrella_proxy_udm.include` and `umbrella_handle_identities.include` files.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `column1` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.network.tls.version_protocol: Newly mapped `column64` raw log field with `event.idm.read_only_udm.network.tls.version_protocol` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column23` and `column62` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column23` and `column62` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `column25` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `column26` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `column28` raw log field with `event.idm.read_only_udm.target.hostname` UDM field and set `has_target` to `true`.  
\- event.idm.read_only_udm.target.application: Newly mapped `column32` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column14` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Concatenated `column2` and `column3` raw log fields and mapped them to `ts`.  
\- Added null checks for several fields in `umbrella_proxy_udm.include` file.  
\- Added a drop statement to drop mistakenly ingested header text as a log entry.  
\- Added a gsub to make failing JSON logs with no valid information as GENERIC_EVENT logs.   
2025-03-25 |  Enhancement:  
\- Added gsubs in order to handle `principal.user.user_display_name` for new format of csv logs.   
2025-02-26 |  Enhancement:  
\- Added support to parse the unparsed logs.   
2025-01-15 |  Enhancement:  
\- Added a `gsub` to support new format of CSV logs.   
2025-01-08 |  Enhancement:  
\- If `identities` is an email address, then mapped `identities` to `principal.user.userid`.   
2024-09-05 |  Enhancement:  
\- Mapped `tld` to `security_result.detection_fields`.   
2023-10-17 |  Enhancement:  
\- Mapped `verdict` to `security_result.action`.   
2023-09-14 |  Enhancement:  
\- Added v8 support for proxy logs.  
\- Mapped `dlpstatus` to `security_result.detection_fields`.  
\- Mapped `certificateErrors` to `security_result.detection_fields`.  
\- Mapped `rulesetID` to `security_result.detection_fields`.  
\- Mapped `destinationListID` to `security_result.detection_fields`.  
\- Mapped `isolateAction` to `security_result.detection_fields`.  
\- Mapped `fileAction` to `security_result.detection_fields`.  
\- Mapped `warnstatus` to `security_result.detection_fields`.  
\- Mapped `avDetections` to `security_result.detection_fields`.  
\- Mapped `puas` to `security_result.detection_fields`.  
\- Mapped `ampDisposition` to `security_result.detection_fields`.  
\- Mapped `ampMalware` to `security_result.detection_fields`.  
\- Mapped `ampScore` to `security_result.detection_fields`.  
\- Mapped `responseBodySize` to `security_result.detection_fields`.  
\- Mapped `requestSize` to `network.sent_bytes`.  
\- Mapped `ruleID` to `security_result.rule_id`.  
\- Mapped `fileName` to `target.file.names`.  
\- Mapped `requestMethod` to `network.http.method`.   
2023-08-16 |  Bug-Fix-  
\- Modified the conditional check for `identity` field to support both `username with email` and `only email`  
\- Removed mapping of `identity` to `principal.user.product_object_id` for `AD Users`.   
2022-12-16 |  Enhancement-  
\- Modified the conditional check for the field `email` and mapped to `principal.user.email_addresses`.  
\- Modified the conditional check for the field `destinationIp` and mapped to `target.ip`.   
2022-09-02 |  Enhancement-  
Migrated the custom parsers into default parser.   
2022-08-19 |  Enhancement-Handled unparsed logs.  
Added on error condition for field `externalIp`.   
2022-08-17 |  Fix -  
\- Added new date type to parse dates of format `MM/dd/yy HH:mm`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
