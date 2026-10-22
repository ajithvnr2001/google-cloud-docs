---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-cloudgen-firewall-changelog/
title: Change log for BARRACUDA_CLOUDGEN_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:33.844656+00:00
---

# Change log for BARRACUDA_CLOUDGEN_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-cloudgen-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BARRACUDA_CLOUDGEN_FIREWALL

Date | Changes  
---|---  
2026-04-16 |  \- `event.idm.read_only_udm.additional.fields`: Newly mapped `server`, `service`, `box`, `startport`, `endport`, `request_type`, `request_key`, `syslogpriority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `peer` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `cn_data` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- Added a Grok pattern on the `message` field to correctly parse the raw log fields.   
2026-04-02 |  \- `event.idm.read_only_udm.target.application`: Removed mapping of `action` from `event.idm.read_only_udm.target.application` UDM field, as it contains the `security action` details rather than `application` data.  
\- `event.idm.read_only_udm.security_result.action`: Mapped the `action` raw log field to `event.idm.read_only_udm.security_result.action` UDM field, mapped to `ALLOW` when `action` is `Allow` and to `BLOCK` when `action` is `Block`.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped the `action` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `column1` from `event.idm.read_only_udm.target.user.userid` UDM field, as it contains the `direction` data rather than `user id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column1` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Removed mapping of the `column6` raw log field from `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM field, when it contains the `principal MAC` address rather than the `target MAC` address.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Mapped `column6` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column3`, `column9` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added a Grok pattern on the `message` field to correctly parse the raw log fields.   
2025-02-10 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
