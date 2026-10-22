---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qnap-nas-changelog/
title: Change log for QNAP_NAS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:46.473330+00:00
---

# Change log for QNAP_NAS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qnap-nas-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for QNAP_NAS

Date | Changes  
---|---  
2025-12-11 |  Enhancement:  
\- Modified grok patterns to support additional log structures.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `sourceHost` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `productVersion` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `originator`, `policy_name`, `db_tag`, `loguid`, `originsicname`, `sequencenum`, `version`, `layer_name`, `context_num`, `hll_key`, `inzone`, `sig_id`, `outzone`, `service_id`, `match_id`, `layer_uuid`, `flags`, `conn_direction`, `analyzedBy`, `maxMatches`, `loginName`, `ifname`, `sub` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` when `src` is an IP address.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` when `src` is not an IP address.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` when `dst` is an IP address.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` when `dst` is not an IP address.  
\- event.idm.read_only_udm.principal.port: Newly mapped `s_port` raw log field to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `xlatesrc` raw log field to `event.idm.read_only_udm.principal.nat_ip`.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `xlatedst` raw log field to `event.idm.read_only_udm.target.nat_ip`.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `xlatesport` raw log field to `event.idm.read_only_udm.principal.nat_port`.  
\- event.idm.read_only_udm.target.nat_port: Newly mapped `xlatedport` raw log field to `event.idm.read_only_udm.target.nat_port`.  
\- event.idm.read_only_udm.network.direction: Newly mapped `ifdir` raw log field to `event.idm.read_only_udm.network.direction`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `logid` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `rule_action` raw log field to `event.idm.read_only_udm.security_result.action`.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `rule_uid` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `proto` raw log field to `event.idm.read_only_udm.network.ip_protocol`.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severityType` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `app_name` raw log field to `event.idm.read_only_udm.principal.application`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `parent_rule`, `nat_rulenum`, `nat_addtnl_rulenum` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Enhanced timestamp parsing to support `ISO8601`, `yyyy-MM-ddTHH:mm:ss.SSSZZ`, and `yyyy-MM-dd HH:mm:ss.SSS` formats, and utilize the `timeStamp` field from CEF logs.  
\- Included logic to determine IP protocol from the `proto` field.   
2025-12-02 |  Enhancement:  
\- Added support for Syslog format with key-value pairs in the message body.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip` and `origin` raw log fields to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `action_result` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `source` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `computer` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.application: Newly mapped `application` raw log field to `event.idm.read_only_udm.target.application`.  
\- event.idm.read_only_udm.principal.network.session_id: Newly mapped `client_id` raw log field to `event.idm.read_only_udm.principal.network.session_id`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `client_app` raw log field to `event.idm.read_only_udm.principal.application`.  
\- event.idm.read_only_udm.principal.network.http.user_agent: Newly mapped `client_agent` raw log field to `event.idm.read_only_udm.principal.network.http.user_agent`.  
\- event.idm.read_only_udm.target: Removed mapping of `intermediary` from `event.idm.read_only_udm.target`.  
\- event.idm.read_only_udm.intermediary: Mapped `intermediary` raw log field to `event.idm.read_only_udm.intermediary`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `desc` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `service` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Added support for timestamp format `yyyy-MM-ddTHH:mm:ss.SSSZZ`.  
\- Set `metadata.event_type` to `USER_UNCATEGORIZED` for events where the `user` field is present.  
\- Expanded grok patterns to handle additional syslog message structures and included CEF format extraction and UDM mapping to support dropped logs of different formats.   
2024-12-09 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
