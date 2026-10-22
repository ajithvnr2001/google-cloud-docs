---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-dnac-changelog/
title: Change log for CISCO_DNAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:56.383439+00:00
---

# Change log for CISCO_DNAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-dnac-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_DNAC

Date | Changes  
---|---  
2025-08-14 |  Enhancement:  
\- Modified Grok pattern to correctly parse the src_ip field as either an IP address or a hostname.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `correlationId`, `isSimulated` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_start_time`: Newly mapped `startTime` raw log field(s) with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_start_time` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `details.wlcIp` raw log field(s) with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `details.detectingApName` raw log field(s) with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.location.name`: Newly mapped `details.detectingApLocation` raw log field(s) with `event.idm.read_only_udm.observer.location.name` UDM field.  
\- `event.idm.read_only_udm.observer.mac`: Newly mapped `details.detectingApMacAddress` raw log field(s) with `event.idm.read_only_udm.observer.mac` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `network.siteId` raw log field(s) with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `src_ip` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `details` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `details.threatType` raw log field(s) with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `tenantId` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added conditional logic to map `src_ip` to `event.idm.read_only_udm.principal.ip` if it is a valid IP address, otherwise it is mapped to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Added a fallback to map from the `efInstanceId` raw log field if `instanceId` is not present.   
2024-11-28 |  Enhancement:  
\- Added support for Syslog + KV format of logs.   
2023-12-29 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
