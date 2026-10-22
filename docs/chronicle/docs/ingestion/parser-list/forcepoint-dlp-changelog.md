---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-dlp-changelog/
title: Change log for FORCEPOINT_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:46.027065+00:00
---

# Change log for FORCEPOINT_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORCEPOINT_DLP

Date | Changes  
---|---  
2026-09-16 |  Enhancement:  
\- Added Grok patterns to support new format of logs.  
\- Updated mapping for `timeStamp` raw log field to support new timestamp format.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `component` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `code` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `localTime`, `srcType` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event_type` to `EMAIL_TRANSACTION` when principal user email and target user email is present and `sourceServiceName` is `SMTP`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action` UDM field when `act` is `Permitted`.  
\- `event.idm.read_only_udm.metadata.product_version`: Updated conditional check to map `productVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field only when `device_version` is empty.   
2025-11-05 |  Enhancement:  
\- Added support for CEF log format prepended with timestamp and intermediary IP address.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_ts` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_ip` (extracted from `reason`) raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Corrected internal raw field typo from recevier_email to receiver_email.  
\- Modified grok pattern to handle extraction of `suser` when enclosed in curly braces.   
2025-10-23 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Changed mapping for `event.idm.read_only_udm.metadata.product_event_type` from `[%{device_event_class_id}] - %{event_name}` to `%{event_name}`.  
\- event.idm.read_only_udm.additional.fields[`IncidentID`]: Newly mapped `device_event_class_id` log field to `event.idm.read_only_udm.additional.fields[`IncidentID`]`.  
\- Added a Grok pattern to support new pattern of logs.   
2025-08-20 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `destinationDnsDomain` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `ahost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `agt` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.namespace: Newly mapped `agentZoneURI` raw log field to `event.idm.read_only_udm.intermediary.namespace` UDM field.  
\- event.idm.read_only_udm.intermediary.mac: Newly mapped `amac` raw log field to `event.idm.read_only_udm.intermediary.mac` UDM field.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `dvc` raw log field to `event.idm.read_only_udm.observer.ip` UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `dvchost` raw log field to `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.observer.mac: Newly mapped `dvcmac` raw log field to `event.idm.read_only_udm.observer.mac` UDM field.  
\- event.idm.read_only_udm.observer.namespace: Newly mapped `deviceZoneURI` raw log field to `event.idm.read_only_udm.observer.namespace` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cs2`, `start`, `end`, `mrt`, `art`, `rt`, `fileType`, `atz`, `dtz`, `geid`, `cefVer`, `aid`, `maxMatches` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `categorySignificance`, `categoryBehavior`, `categoryDeviceGroup`, `catdt`, `categoryOutcome`, `categoryObject` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `header_severity` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Modified Grok pattern to include `header_severity` extraction from the CEF header.  
\- Added gsub to pre-process kv_data to handle keys prefixed with `ad.`.  
\- Added logic to use `header_severity` from the CEF header as a fallback for `security_result.severity` and `security_result.severity_details`.  
\- Conditionally set `event.idm.read_only_udm.metadata.event_type` to `EMAIL_TRANSACTION` when `sourceServiceName` is `SMTP`.  
\- Adjusted conditional checks for `sourceHostname` and `sourceHost` to map them unless they are empty or exactly `N/A`.   
2025-03-06 |  Enhancement:  
\- Mapped `inter_host` to `intermediary.hostname`.   
2025-02-19 |  Enhancement:  
\- Mapped `violationTriggers.*` fields to `additional.fields`.   
2025-01-03 |  Enhancement:  
\- Mapped `violationTriggers.VZ CPNI` and `violationTriggers.Controlled Unclassified Information: Portion Marking` to `additional.fields`.   
2024-11-19 |  Enhancement:  
\- Added support for new CEF format logs.   
2024-08-05 |  Enhancement:  
\- When `act` is `Quarantined`, then mapped `act` to `security_result.action_details` and `security_result.action` to `ALLOW`.  
\- Mapped `caseDescription` to `metadata.description`.  
\- Mapped `eventIDs` to `metadata.product_event_type`.  
\- When `sourceServiceName` is a valid application_protocol, then mapped `sourceServiceName` to `network.application_protocol`.  
\- Mapped `productVersion` to `metadata.product_version`.  
\- Mapped `riskScore` to `additional.fields`.   
2024-05-20 |  Enhancement:  
\- Mapped `fname` to `target.file.full_path`.  
\- Mapped `destinationHosts` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `productVersion` and `analyzedBy` to `additional.fields`.   
2024-03-25 |  Bug-fix:  
\- Added support for new format logs.  
\- Mapped `timeStamp` to `metadata.event_timestamp`.  
\- Mapped `act` to `security_result.description`.  
\- Mapped `cat` to `security_result.category_details`.  
\- Mapped `severityType` to `security_result.severity`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `eventId` to `metadata.product_log_id`.  
\- Mapped `sourceServiceName` to `principal.application`.  
\- Mapped `sourceHost` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `sourceIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `suser` to `principal.user.userid`.  
\- Mapped `loginName` to `principal.user.user_display_name`.   
2022-11-07 |  \- Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
