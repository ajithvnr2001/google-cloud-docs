---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-endpoint-vulnerabilities-changelog/
title: Change log for TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:15:00.011266+00:00
---

# Change log for TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-endpoint-vulnerabilities-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES

Date | Changes  
---|---  
2026-03-14 |  \- Newly created parser.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `deviceName`,`deviceName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_end_time`: Newly mapped `scanTime` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_end_time` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cve_id`: Newly mapped `cve.id` raw log field with event.idm.read_only_udm.extensions.vulns.vulnerabilities.cve_id` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.vendor`: Newly mapped `TREND VISION ONE` static value with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.vendor` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.description`: Newly mapped `cve.globalExploitActivityLevel` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.description` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score`: Newly mapped `cve.cvssScore` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.severity`: Newly mapped `cve.eventRiskLevel` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `discoveredBy`,`installedAgents`,`lastDetectDateTime`,`cve_affectedComponents_additional_data`,`lastScannedDateTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `osName`,`platformAssetTags.Assetgroup`,`customAssetTags.1` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cveCount`,`protectionRule.name`,`protectionRule.product`,`protectionRule.id`,`cve.mitigationStatus`, `cve.exploitAttemptCount` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `criticality` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `latestRiskScore` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `cve.id`,`cveCount` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `osPlatform` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `TREND VISION ONE VULNERABILITIES` static value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `TREND VISION ONE VULNERABILITIES` static value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `CVE Vulnerability Scan` static value with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `SCAN_VULN_HOST` to `event.idm.read_only_udm.metadata.event_type` UDM field when vulnerabilities details and principal machine data such as `deviceName` or `ip` are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `STATUS_UPDATE` to `event.idm.read_only_udm.metadata.event_type` UDM field when principal machine data such as `deviceName` or `ip` are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `GENERIC_EVENT` to `event.idm.read_only_udm.metadata.event_type` UDM field when vulnerabilities details and principal machine data such as `deviceName` or `ip` are not present.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
