---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-eyeinspect-changelog/
title: Change log for FORESCOUT_EYEINSPECT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:07:29.726012+00:00
---

# Change log for FORESCOUT_EYEINSPECT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-eyeinspect-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORESCOUT_EYEINSPECT

Date | Changes  
---|---  
2025-12-05 |  Enhancement:  
\- Added support for JSON format.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `deviceDnsDomain` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cnt` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `alertId` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `srcIp` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `srcMac` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `srcHostName` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.principal.port: Newly mapped `srcPort` raw log field to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.principal.file.sha1: Newly mapped `pcapSha1` raw log field to `event.idm.read_only_udm.principal.file.sha1`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dstIp` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.target.mac: Newly mapped `dstMac` raw log field to `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `dstHostName` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.port: Newly mapped `dstPort` raw log field to `event.idm.read_only_udm.target.port`.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `sensorName` raw log field to `event.idm.read_only_udm.observer.hostname`.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `l4Proto` raw log field to `event.idm.read_only_udm.network.ip_protocol`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `upDataLength` raw log field to `event.idm.read_only_udm.network.sent_bytes`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `downDataLength` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `typeId` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `name` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `alertCategory` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.security_result.attack_details.tactics.name: Newly mapped `mitreTacticsId` raw log field to `event.idm.read_only_udm.security_result.attack_details.tactics.name`.  
\- event.idm.read_only_udm.security_result.attack_details.techniques.name: Newly mapped `mitreTechniquesId` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques.name`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `l2Proto`, `l3Proto`, `srcMacVendor`, `dstMacVendor`, `status` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Moved the mapping for `event.idm.read_only_udm.intermediary` to apply to both CEF and JSON formats.   
2025-04-23 |  \- Map domain name to `network.dns.questions.name` when application protocol is DNS.  
\- Map answers to `network.dns.answers.data` when application protocol is DNS.   
2025-03-12 |  \- Newly created parser.  
\- Mapped `app_protocol_src` to `network.application_protocol`.  
\- Mapped `Source` to `principal.ip` if it is an IP address, otherwise to `principal.hostname`.  
\- Mapped `Target` to `target.ip` if it is an IP address, otherwise to `target.hostname`.  
\- Mapped `user_name` to `principal.user.userid`.  
\- Mapped `type` to `additional.fields`  
\- Mapped `session_id` to `network.session_id`.  
\- Mapped `product` to `metadata.product_name`.  
\- Mapped `pid` to `intermediary.process.pid`.  
\- Mapped `iporhost` to `intermediary.ip` if it is an IP address, otherwise to `intermediary.hostname`.  
\- Mapped `Rule` to `security_result.rule_id`.  
\- Mapped `Match` to `security_result.rule_name`.  
\- Mapped `Category` and `policy_details` to `security_result.description`.  
\- Mapped `Destination` to `target.ip` if it is an IP address, otherwise to `target.hostname`.  
\- Mapped `port` to `target.port`.  
\- Mapped `Host` to `principal.ip` if it is an IP address, otherwise to `principal.hostname`.  
\- Mapped `Target` to `target.ip` if it is an IP address, otherwise to `target.hostname`.  
\- Mapped `Service` to `target.port` and `network.ip_protocol`.  
\- Mapped `Reason` to `security_result.description`.  
\- Mapped `mail_from` to `network.email.from`.  
\- Mapped `mail_to` to `network.email.to`.  
\- Mapped `mail_subject` to `network.email.subject`.  
\- Mapped `event_type` to `security_result.summary`.  
\- Mapped `log_description` to `security_result.summary`.  
\- Mapped `details` to `security_result.description`.  
\- Mapped `CPU_usage`, `Available_memory`, `Used_memory`, `Available_swap`, `Used_swap` to `additional.fields`.  
\- Mapped `application_status`, `Connected_clients`, `EM_connection_status`, `Assigned_hosts`, `Engine_status`, `Installed_Plugins` to `additional.fields`.  
\- Mapped `User` to `principal.user.userid`.  
\- Mapped `Hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `MAC` to `principal.mac`.  
\- Mapped `src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `act` to `security_result.description`.  
\- Mapped `alart_id` to `security_result.rule_id`.  
\- Mapped `src_mac` to `principal.mac`.  
\- Mapped `dest_mac` to `target.mac`.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `dest_port` to `target.port`.  
\- Mapped `dest_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `severity` to `security_result.severity_details`.  
\- Mapped `threat` to `security_result.threat_name`.  
\- Mapped `protocol1` to `network.ip_protocol`.  
\- Mapped `protocol2` to `security_result.detection_fields`.  
\- Mapped `resource` to `security_result.about.resource.attribute.labels`.  
\- Mapped `desc` to `metadata.description`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
