---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-sandbox-changelog/
title: Change log for FORTINET_SANDBOX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:10:51.571216+00:00
---

# Change log for FORTINET_SANDBOX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-sandbox-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_SANDBOX

Date | Changes  
---|---  
2026-08-21 |  \- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` and `subtype` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `emailsndr` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `emailrcvr` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dstip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dstport` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `fname` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rsrc` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `rating` and `risk` raw log fields with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ftype`, `jobid`, `jstatus`, `scantime`, `subtime`, `scanstart`, `scanend`, `clientdev`, `clientname`, `clientvd`, and `stype` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.about.url` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `sha1` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `mname` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `mcate` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `date`, `time`, and `tz` raw log fields with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `rating` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2025-02-26 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
