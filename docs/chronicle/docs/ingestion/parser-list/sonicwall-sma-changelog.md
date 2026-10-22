---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonicwall-sma-changelog/
title: Change log for SONICWALL_SMA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:54.736752+00:00
---

# Change log for SONICWALL_SMA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonicwall-sma-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SONICWALL_SMA

Date | Changes  
---|---  
2025-03-27 |  Enhancement:  
-`event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `connection_status` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `fd` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `server` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `time_reopen` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attributes.net.transport` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attributes.chronicle_ingestion_label.Environment` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attributes.chronicle_ingestion_label.ingestion_source` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attributes.log_type` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attributes.chronicle_log_type` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.principal.hostname`: Newly mapped `attributes.net.host.name` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
-`event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `attributes.net.host.name` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
-`event.idm.read_only_udm.principal.port`: Newly mapped `attributes.net.host.port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
-`event.idm.read_only_udm.principal.ip`: Newly mapped `attributes.net.host.ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
-`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `attributes.net.host.ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
-`event.idm.read_only_udm.target.hostname`: Newly mapped `attributes.net.peer.name` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
-`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `attributes.net.peer.name` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
-`event.idm.read_only_udm.target.port`: Newly mapped `attributes.net.peer.port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `attributes.net.peer.ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
-`event.idm.read_only_udm.target.asset.ip`: Newly mapped `attributes.net.peer.ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
-`event.idm.read_only_udm.intermediary.hostname`: Newly mapped `resource_attributes.host.name` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
-`event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `resource_attributes.host.name` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
-`event.idm.read_only_udm.intermediary.platform_version`: Newly mapped `resource_attributes.os.type` raw log field to `event.idm.read_only_udm.intermediary.platform_version` UDM field.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `VirtualHost` raw log field to `event.idm.read_only_udm.target.ip` UDM field if it is a valid IP address.  
-`event.idm.read_only_udm.target.asset.ip`: Newly mapped `VirtualHost` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field if it is a valid IP address.  
-`event.idm.read_only_udm.target.hostname`: Newly mapped `VirtualHost` raw log field to `event.idm.read_only_udm.target.hostname` UDM field if it is not a valid IP address.  
-`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `VirtualHost` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field if it is not a valid IP address.  
-`event.idm.read_only_udm.principal.ip`: Newly mapped `Src` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
-`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Src` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
-`event.idm.read_only_udm.network.http.method`: Newly mapped `Method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
-`event.idm.read_only_udm.target.url`: Newly mapped `Request` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
-`event.idm.read_only_udm.network.http.response_code`: Newly mapped `Status` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
-`event.idm.read_only_udm.network.received_bytes`: Newly mapped `Bytes` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
-`event.idm.read_only_udm.principal.process.pid`: Newly mapped `EquipmentId` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
-`event.idm.read_only_udm.target.application`: Newly mapped `ApplicationName` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
-`event.idm.read_only_udm.network.session_id`: Newly mapped `SessionKey` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `server_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
-`event.idm.read_only_udm.target.asset.ip`: Newly mapped `server_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
-`event.idm.read_only_udm.target.port`: Newly mapped `server_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
-`event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field to `event.idm.read_only_udm.metadata.description` UDM field if `desc_invalid` is `true` UDM field.  
-`event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `pam_type` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `session_type` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `status` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `level` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.security_result.action_details`: Newly mapped `subsystem` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
-`event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
-`event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `User` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
-`event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
-`event.idm.read_only_udm.target.user.userid`: Newly mapped `by_user_id` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
-`event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Command` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `Dest` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
-`event.idm.read_only_udm.target.asset.ip`: Newly mapped `Dest` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
-`event.idm.read_only_udm.network.received_bytes`: Newly mapped `SrcBytes` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
-`event.idm.read_only_udm.network.sent_bytes`: Newly mapped `DestBytes` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
-`event.idm.read_only_udm.metadata.event_type`: Newly mapped `metadata.event_type` raw log field to `event.idm.read_only_udm.metadata.event_type` if `target_user_present` or `principal_user_present` is `true`.  
\- `json`: Added support for `json` format.  
\- `syslog`: Added support for `syslog` format.   
2024-03-28 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
