---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/remediant-secureone-changelog/
title: Change log for REMEDIANT_SECUREONE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:28.511252+00:00
---

# Change log for REMEDIANT_SECUREONE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/remediant-secureone-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for REMEDIANT_SECUREONE

Date | Changes  
---|---  
2025-07-09 |  Enhancement:  
\- Added new json filter for `message` and `json_message` data fields to parse the dropped the logs.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` : Newly mapped `targetSystem.cn` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field and set `has_principal` to `true`.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` : Newly mapped `req_headers_host` data field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.user.userid` : Newly mapped `user_user` data field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `req.query.page`, `user.distinguishedName`, `targetSystem.operatingSystem` and `req.query.limit` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `req.params.computerId`, `req.id`, and `targetSystem._id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly mapped `event_type` data field with `event.idm.read_only_udm.metadata.event_type` UDM field to `NETWORK_CONNECTION` when `principal_machine_id_present` is `true` and `has_target` is `true`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Newly mapped `user.domain_netbios`,`user.id`, and `user.objectSid` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.   
2025-06-11 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `persistent`, `access.type`, `access.tokenId`, `access.tokenType`, `targetSystem.cn`, `targetSystem.distinguishedName`, `targetSystem.policy.strict_secure`, `targetSystem.policy.secure`, `targetSystem.policy.scan`, `targetSystem.policy.manage_local_sids` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `user.domain`, `access.user.domain_netbios`, `access.user.objectSid` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `user.sid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user.user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.   
2024-12-12 |  \- When `strict_secure` is false & `secure` is false mapped key to a `Protect Mode` and set the value to `Disabled` to `security_result.detection_fields`.  
\- When `strict_secure` is false & `secure` is true mapped key to a `Protect Mode` and set the value to `JITA` to `security_result.detection_fields`.  
\- When `strict_secure` is false & `secure` is false mapped key to a `Protect Mode` and set the value to `DENY` to `security_result.detection_fields`.  
\- When `scan` is true mapped key to a `Scan Mode` and set the value to `Enabled` to `security_result.detection_fields`.  
\- When `scan` is false mapped key to a `Scan Mode` and set the value to `Disabled` to `security_result.detection_fields`.   
2024-11-27 |  \- Mapped `failover_dc`,`initial_dc`,`ldapName`,`sync_end_ts` ,and `sync_start_ts` to `additional.fields`.   
2023-12-08 |  New:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
