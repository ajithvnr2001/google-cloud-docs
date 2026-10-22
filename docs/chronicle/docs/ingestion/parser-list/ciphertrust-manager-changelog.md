---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ciphertrust-manager-changelog/
title: Change log for CIPHERTRUST_MANAGER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:54.036924+00:00
---

# Change log for CIPHERTRUST_MANAGER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ciphertrust-manager-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CIPHERTRUST_MANAGER

Date | Changes  
---|---  
2026-08-19 |  \- Added a Grok pattern to parse the raw log fields.  
\- Added a grok pattern on `details_description` to extract `target_ip`, `target_port`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details.state`, `details.state_change_at`, and `subject` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `details.description` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `message` is Alarm, Update License Usage, Update CTE Client, Google Cloud EKM Unwrap, Terminating KMIP Connection, or SSL Handshake failed, updated the value of `event.idm.read_only_udm.metadata.event_type` to STATUS_UPDATE.  
\- `event.idm.read_only_udm.metadata.event_type`: If `message` is Use Key or Export Key, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_RESOURCE_UPDATE_CONTENT.   
2026-08-05 |  \- Updated the parser `Category`, `Supported Format` details.   
2025-11-20 |  \- Added a grok pattern to parse the new log format.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `details.host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details.messageFormat` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `details.transport` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `syslog_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is true and `has_target` is true, updated to `NETWORK_CONNECTION`.   
2025-10-13 |  \- Added a new grok pattern to support new format of SYSLOG logs.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `details.errorMessage` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `uid` field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `product_name` field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-09-16 |  \- event.idm.read_only_udm.additional.fields: Newly mapped details.format, details.requestIdentifier, details.requestIdentifierType, details.version, details.app_connector_type, details.meta, details.interfaceName, details.interfaceType, and service raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped details.port raw log field(s) with event.idm.read_only_udm.target.port UDM field.  
\- Added conditional check for cef_message field. Logic that populates event.idm.read_only_udm.principal.user.userid now also executes if cef_message contains `Export Key`.  
\- Added conditional check for message field. If message is `SSL Handshake failed`, `Terminating KMIP Connection`, `ADPReadClientProfile`, or `Update License Usage`, client_ip is mapped to event.idm.read_only_udm.principal.ip. Otherwise, client_ip is mapped to event.idm.read_only_udm.src.ip.  
\- event.idm.read_only_udm.metadata.event_type: If message is SSL Handshake failed or Terminating KMIP Connection, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.event_type: If message is ADPReadClientProfile or Reject access, updated to USER_RESOURCE_ACCESS.  
\- event.idm.read_only_udm.metadata.event_type: If message is Export Key, updated to USER_RESOURCE_UPDATE_CONTENT.  
\- Updated Grok patterns to support new log formats.   
2025-04-23 |  \- Added a Grok pattern to parse the unparsed logs.  
\- Added a gsub to parse the unparsed logs.  
\- `event.idm.read_only_udm.src.user.product_object_id`: Newly mapped `cust_client_id` raw log field with `event.idm.read_only_udm.src.user.product_object_id' UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid' UDM field.  
\- Added `has_user` flag as a conditional check for `user_id` raw log field to populate `USER_UNCATEGORIZED` event_type.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `service_name` raw log field with `event.idm.read_only_udm.target.application' UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record_type_id`, `details.aliases`, `details_algorithm`, `details_assignSelfAsOwner`, `details_emptyMaterial`, `details_feature`, `details_undeletable`, `details_unexportable`, `details_xts`, `details_padded`, `details_generateKeyId`, `details_id`, `details_objectType` and `details_ownerId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` \- Newly mapped `details_name`, `details_uri` and `details_usageMask` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.file.size` \- Newly mapped `details.size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- Added a gsub to map the `principal` raw log field to 'log_principal.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `details.label`, `details.domain`, `details.switch_domain_id`, `details.user_id`, `details.refresh_token_id`, `details.renew_refresh_token`, `details.user_metadata_current_persistedData`, `details.refresh_token_counts.labels`, `details_scope`, `details.refresh_token_counts.no_label`, `details.refresh_token_counts.total`, `details.user_metadata.current_domain.id`, `details.user_metadata.current_domain.name`, `details.meta.permissions`, `details.meta.ownerId`, `details.meta.customAttributes`, `details.errorMessage`, `details.zone_id`, `details.client_type`, `details.grant_type`, `details.client_name`, `details.username`, `details.idType`, `details.identifier`, `details.client_id`, `details.auth_domain`, `details.connection`, `details.userid`, `details.codeDesc`, `details.code` and `details.Internal` raw log fields with third variable to map to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `prev_msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `success` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `details.usage` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-06-24 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
