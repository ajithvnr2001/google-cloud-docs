---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zywall-changelog/
title: Change log for ZYWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:20.517173+00:00
---

# Change log for ZYWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zywall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZYWALL

Date | Changes  
---|---  
2025-12-08 |  \- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.  
\- Updated conditional logic for the `action` field to include `pass` alongside `ACCEPT` to map to `ALLOW`.  
\- The intermediate field `security_result_action` has been replaced with `security_action` before mapping to the final UDM field.  
\- Removed logic that directly extracted the `action` field from the `msg` field.  
\- Removed a condition that set the `action` field to `ACCEPT` based on a pattern match in the `msg` field.   
2025-11-18 |  \- `event.idm.read_only_udm.additional.fields`: Newly mapped `app`, `cef_event_class_id`, `cef_spec_version`, and `proto` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `cef_name` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `cef_device_version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `ob` raw log field(s) with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `cef_severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `ZYlevel` raw log field(s) with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dvchost` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `dvchost` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `cef_product` with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `cef_vendor` with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `spt` with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dpt` with `event.idm.read_only_udm.target.port` UDM field.  
\- Renamed from ZYnote to note.  
\- Renamed from act to action.  
\- Renamed from ZYclass to class.  
\- Renamed from ZYruleId to rule_name.  
\- Added conditional check for message to support CEF formatted logs.   
2024-08-29 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
