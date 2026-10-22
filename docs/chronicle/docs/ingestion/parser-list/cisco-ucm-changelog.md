---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ucm-changelog/
title: Change log for CISCO_UCM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:48.640566+00:00
---

# Change log for CISCO_UCM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ucm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_UCM

Date | Changes  
---|---  
2026-07-15 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `ResourceAccessed` from `event.idm.read_only_udm.target.resource.id` UDM field since this UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `ResourceAccessed` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `AppID` from `event.idm.read_only_udm.target.resource.id` UDM field since this UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `AppID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `url`, `soap_ns`, `xml_encoding`, `xml_version`, `agreement_value`, `syslog_priority`, `method` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `syslog_seq` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message_type` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `axl_api_version` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `userid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `uniqueidentifier` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.first_name`: Newly mapped `firstname` raw log field with `event.idm.read_only_udm.target.user.first_name` UDM field.  
\- `event.idm.read_only_udm.target.user.last_name`: Newly mapped `lastname` raw log field with `event.idm.read_only_udm.target.user.last_name` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `mailid` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `displayname` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.title`: Newly mapped `title` raw log field with `event.idm.read_only_udm.target.user.title` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT` when `EventType` is `UserRoleMembershipUpdate` or `GeneralConfigurationUpdate`.   
2026-02-24 |  Enhancement:  
-`event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `AgreementId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.target.url`: Newly mapped `LDAPHost` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `ldap_host_protocol` from the `LDAPHost` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `ldap_host_ip` from the `LDAPHost` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
-`event.idm.read_only_udm.target.port`: Newly mapped `ldap_host_port` from the `LDAPHost` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
-`event.idm.read_only_udm.metadata.event_type`: If the raw field `EventType` is `UserAccess`, the UDM event type is updated to `USER_RESOURCE_ACCESS`.  
\- Modified the grok patterns in order to parse the logs and following UDM fields are now being mapped correctly:  
-`event.idm.read_only_udm.additional.fields`  
-`event.idm.read_only_udm.intermediary.ip`  
-`event.idm.read_only_udm.metadata.description`  
-`event.idm.read_only_udm.metadata.product_event_type`  
-`event.idm.read_only_udm.observer.application`  
-`event.idm.read_only_udm.principal.application`  
-`event.idm.read_only_udm.principal.asset.hostname`  
-`event.idm.read_only_udm.principal.asset.ip`  
-`event.idm.read_only_udm.principal.hostname`  
-`event.idm.read_only_udm.principal.ip`  
-`event.idm.read_only_udm.principal.process.pid`  
-`event.idm.read_only_udm.principal.user.userid`  
-`event.idm.read_only_udm.security_result.category_details`  
-`event.idm.read_only_udm.security_result.description`  
-`event.idm.read_only_udm.security_result.severity`  
-`event.idm.read_only_udm.security_result.severity_details`  
-`event.idm.read_only_udm.target.application`  
-`event.idm.read_only_udm.target.asset.ip`  
-`event.idm.read_only_udm.target.resource.id`  
2025-10-08 |  Enhancement:  
\- Added a grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserID` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ClientAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `ResourceAccessed` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `AuditDetails` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `ComponentID` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `CorrelationID`, `ClusterID`, `CompulsoryEvent`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `AppID` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `NodeID` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `EventType` is `UserLogging`, updated to `USER_UNCATEGORIZED`.  
\- Added conditional check for `EventStatus`: if the value is `Success`, the action is set to `ALLOW`; otherwise, it is set to `FAIL`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `AuditCategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.   
2024-10-15 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- Mapped `inter_hostname` to `intermediary.hostname`.  
\- Mapped `inter_ip` to `intermediary.ip` and `intermediary.asset.ip`.  
\- Mapped `ClusterId` to `additional.fields`.   
2022-08-18 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
