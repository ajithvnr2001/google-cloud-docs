---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-webproxy-changelog/
title: Change log for FORTINET_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:21:38.952420+00:00
---

# Change log for FORTINET_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_WEBPROXY

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- Updated a conditional to prevent mapping the `dstport` raw log field with invalid values to the `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `logdesc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2026-04-14 |  Enhancement:  
\- Corrected the product `Category` from `Storage` to `Web Proxy` in the parser configuration.   
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventtime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `transid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `method` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern on `eventtime` to extract `eventtime_sec`, `eventtime_nano`.   
2025-06-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `subtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `catdesc` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sentbyte` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `rcvdbyte` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referralurl` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `httpmethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `reqtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ratemethod` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping for `vd` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.Because `event.idm.read_only_udm.principal.user.userid` UDM event is already mapped to `user` ,this caused the `vd` mapping to be overwritten.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `vd` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Updated the mapping for the `policyid` raw log field to merge it as a key-value pair with `PolicyID` as the key and the `policyid` value as the value, using the `policyid_label` variable.  
\- `event.idm.read_only_udm.network.direction`: Updated to include mapping for `outgoing` and `outbound` values to `OUTBOUND`, in existing raw log field `direction`.   
2025-01-07 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
