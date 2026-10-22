---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-vm-changelog/
title: Change log for QUALYS_VM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:37.451862+00:00
---

# Change log for QUALYS_VM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-vm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for QUALYS_VM

Date | Changes  
---|---  
2025-07-03 |  Enhancement:  
\- Newly added a grok pattern to parse the new format of logs.  
\- Newly added kv filter to parse `kv_data` data field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` : Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field and set `has_principal` as `true`.  
\- `event.idm.read_only_udm.principal.asset.hostname` : Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field and set `has_principal` as `true`.  
\- `event.idm.read_only_udm.target.application` : Newly mapped `application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.process.pid` : Newly mapped `processid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` : Newly mapped `SLICEID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname` : Newly mapped `SCANNER` raw log field with `event.idm.read_only_udm.target.hostname` UDM field and set `has_target` as `true`.  
\- `event.idm.read_only_udm.target.asset.hostname` : Newly mapped `SCANNER` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field and set `has_target` as `true`.  
\- `event.idm.read_only_udm.security_result.category_details` : Newly mapped `CAT` raw log field with `event.idm.read_only_udm.security_result.category_details` raw log field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `EVENT` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `IPV4` raw log field with `event.idm.read_only_udm.principal.ip` UDM field and set `has_principal` as `true`.  
\- `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `IPV4` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field and set `has_principal` as `true`.  
\- `event.idm.read_only_udm.event_type` : Newly mapped `event.idm.read_only_udm.event_type` UDM field as `NETWORK_CONNECTION` when `has_principal` and `has_target` are `true` and as `STATUS_UPDATE` when `has_principal` is `true` and `has_target` is `false` and as `GENERIC_EVENT` when `has_principal` is `false` and `has_target` is `false`.   
2023-10-27 |  Enhancement:  
\- Added a `for` loop to split the events when there are multiple `QIDs`.   
2023-04-25 |  Enhancement:  
\- Mapped `DetectionList.FirstFoundTime` to `extensions.vulns.vulnerabilities.first_found`.  
\- Mapped `DetectionList.LastFoundTime` to `extensions.vulns.vulnerabilities.last_found`.  
\- Mapped `DetectionList.TimesFound` to `extensions.vulns.vulnerabilities.about.resource.attribute.labels`.  
\- Mapped `DetectionList.LastTestDateTime` to `extensions.vulns.vulnerabilities.about.resource.attribute.labels`.  
\- Mapped `DetectionList.LastUpdateDateTime` to `extensions.vulns.vulnerabilities.about.resource.attribute.labels`.  
\- Mapped `DetectionList.LastProcessedDatetime` to `extensions.vulns.vulnerabilities.about.resource.attribute.labels`.   
2023-01-23 |  Enhancement:  
\- Mapped `DetectionList` array details to `extensions.vulns.vulnerabilities`.  
\- Mapped `DetectionList.Qid` to `extensions.vulns.vulnerabilities.name`.  
\- Mapped `DetectionList.Severity` to `extensions.vulns.vulnerabilities.severity`.  
\- Mapped `DetectionList.Results` to `extensions.vulns.vulnerabilities.description`.  
\- Mapped `DetectionList.Status`, `DetectionList.DType` to `extensions.vulns.vulnerabilities.about.resource.attribute.labels`.   
2022-09-29 |  Enhancement:  
\- Mapped `ID` to `metadata.product_log_id`.  
\- Mapped `Netbios`,`TrackingMethod`,`NetworkID` to `additional.fields`.  
\- Mapped `QgHostID` to `principal.asset_id`.  
\- Mapped `Os` to `principal.platform_version`.  
\- Added conditional check for `_vulns`.   
2022-07-20 |  Enhancement: added mapping for following fields:  
\- `DETECTION.FIRST_FOUND_DATETIME` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.first_found`.  
\- `DETECTION.LAST_FOUND_DATETIME` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.last_found`.  
\- `HOST.LAST_VM_SCANNED_DATE` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_end_time`.  
\- `HOST.LAST_SCAN_DATETIME` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_start_time`.  
\- `DETECTION.QID` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.name`.  
\- `DETECTION.SEVERITY` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.severity`.  
\- `DETECTION.TYPE` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.about.labels`.  
\- `DETECTION.STATUS` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.labels`.  
\- `DETECTION.RESULTS` mapped to `event.idm.read_only_udm.extensions.vulns.vulnerabilities.description`.  
\- `HOST.DNS_DATA.DOMAIN` mapped to `event.idm.read_only_udm.principal.domain.name`.  
\- `HOST.ASSET_ID` mapped to `event.idm.read_only_udm.principal.asset_id`.  
\- `HOST.IP` mapped to `event.idm.read_only_udm.principal.ip`.  
\- `HOST.OS` mapped to `event.idm.read_only_udm.principal.platform_version`.  
\- `HOST.DNS` mapped to `event.idm.read_only_udm.principal.hostname`.  
\- `HOST.QG_HOSTID` mapped to `event.idm.read_only_udm.additional.fields`.  
\- `HOST.NETBIOS` mapped to `event.idm.read_only_udm.additional.fields`.  
\- `HOST.TRACKING_METHOD` mapped to `event.idm.read_only_udm.additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
