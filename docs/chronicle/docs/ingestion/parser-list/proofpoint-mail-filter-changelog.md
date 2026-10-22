---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-filter-changelog/
title: Change log for PROOFPOINT_MAIL_FILTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:40.457716+00:00
---

# Change log for PROOFPOINT_MAIL_FILTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-filter-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_MAIL_FILTER

Date | Changes  
---|---  
2025-12-02 |  Enhancement:  
\- event.idm.read_only_udm.network.session_id: Newly mapped `AppAccessContext.AADSessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `ClientAppName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AppAccessContext.CorrelationId` raw log field as key `AppAccessContext CorrelationId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AppAccessContext.UniqueTokenId` raw log field as key `AppAccessContext UniqueTokenId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `AppAccessContext.UserObjectId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `Id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `Operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `OrganizationId` raw log field as key `OrganizationId` `event.idm.read_only_udm.target.resource.attribute.labels` with UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `RecordType` raw log field as key `RecordType` with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `UserKey` raw log field as key `UserKey` with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `UserType` raw log field as key `UserType` with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Version` raw log field as key `Version` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `Workload` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `ClientIP` raw log field with `event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `UserId` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Newly mapped `AuthenticationType` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `BrowserName` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent.browser_version: Newly mapped `BrowserVersion` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent.browser_version` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `CorrelationId` raw log field as key `CorrelationId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EventSource` raw log field as key `EventSource` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `GeoLocation` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `IsManagedDevice` raw log field as key `IsManagedDevice` with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ItemType` raw log field as key `ItemType` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ListId` raw log field as key `ListId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ListItemUniqueId` raw log field as key `ListItemUniqueId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Platform` raw log field as key `Platform` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Site` raw log field as key `Site` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `UserAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `WebId` raw log field as key `WebId` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `HighPriorityMediaProcessing` raw log field as key `HighPriorityMediaProcessing` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ListBaseType` raw log field as key `ListBaseType` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ListServerTemplate` raw log field as key `ListServerTemplate` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `SourceRelativeUrl` raw log field with `event.idm.read_only_udm.principal.url` UDM field.   
2024-09-19 |  Enhancement:  
\- Added support for new log format.   
2024-06-03 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Added a conditonal check for `datetime`, `hfrom`.  
\- Mapped `net_mail_id` and `hdr_mid` to `network.email.mail_id`.   
2022-10-03 |  Enhancement  
\- Added grok pattern to parse newly ingested and unparsed logs.  
\- Added null check for field name `proc`.  
\- Mapped `process_id` to `principal.process.pid`.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.  
\- Mapped `version` to `network.tls.version`.  
\- Added error check for field name `status`.  
\- Mapped `proto` to `network.application_protocol` with newly added conditions.  
\- Added condition to check for valid email for the field name `from`.  
\- Added condition to check for valid email for the field name `to` and also handled multiple emails in the field. Mapped each valid email to `target.user.email_addresses`.  
\- Mapped `class` to `security_result.detection_fields`.  
\- MApped `msgid` to `network.email.mail_id`.  
\- Mapped `auth` to `extensions.auth.type`.  
\- Mapped `delay` to `about.resource.attribute.labels`.  
\- Set `security_result.action` to `ALLOW` if `verify` is `OK` and vice versa.  
\- Mapped `mailer` to `network.application_protocol` with newly added conditions.  
\- Added grok to parse `stat` and mapped the contents to `security_result.summary`.  
\- Mapped `received_byte` to `network.received_bytes`.  
\- Mapped `Hostname` to `target.hostname`.  
\- Mapped `H` to `target.hostname`.  
\- Added grok to map for ip, based on the check if it's domain then mapped `relay` to `intermediary.administrative_domain` else mapped `interm_ip` to `intermediary.ip`.  
\- Mapped `domain` to `intermediary.administrative_domain`.  
\- Remapped `device` from `intermediary.hostname` to `principal.hostname`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
