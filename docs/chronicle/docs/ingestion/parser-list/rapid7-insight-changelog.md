---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-insight-changelog/
title: Change log for RAPID7_INSIGHT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:09:23.541315+00:00
---

# Change log for RAPID7_INSIGHT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-insight-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RAPID7_INSIGHT

Date | Changes  
---|---  
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `risk_score` raw log field to `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity_score` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.asset.first_seen_time`: Newly mapped `added` raw log field to `event.idm.read_only_udm.principal.asset.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.last_seen_time`: Newly mapped `published` raw log field to `event.idm.read_only_udm.principal.process.file.last_seen_time` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `categories` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cve_id`: Newly mapped `cves` raw log field to `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cve_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score`: Newly mapped `cvss_v3_score` raw log field to `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector`: Newly mapped `cvss_v3_vector` raw log field to `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.description`: Newly mapped `description` raw log field to `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.description` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `title` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.last_updated_time`: Newly mapped `modified` raw log field to `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `links.id` , `links.href`, `links.source`, `cvss_v2_access_complexity`, `cvss_v2_access_vector`, `cvss_v2_authentication`, `cvss_v2_availability_impact`, `cvss_v2_confidentiality_impact`, `cvss_v2_exploit_score`, `cvss_v2_impact_score`, `cvss_v2_integrity_impact`, `cvss_v2_score`, `cvss_v2_vector`, `cvss_v3_attack_complexity`, `cvss_v3_attack_vector`, `cvss_v3_availability_impact`, `cvss_v3_confidentiality_impact`, `cvss_v3_exploit_score`, `cvss_v3_impact_score`, `denial_of_service`, `exploits`, `malware_kits`, `pci_cvss_score`, `pci_fail`, `pci_severity_score`, `pci_special_notes`, `pci_status`, `references`, `cvss_v3_integrity_impact`, `cvss_v3_privileges_required`, `cvss_v3_scope` and `cvss_v3_user_interaction` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `GENERIC_EVENT` value to `event.idm.read_only_udm.metadata.event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `Rapid7 Insight` value to `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `Rapid7 Insight` value to `event.idm.read_only_udm.metadata.vendor_name` UDM field.   
2024-05-13 |  Enhancement:  
\- Added support for the new format of SYSLOG+KV logs.   
2023-05-05 |  Enhancement  
\- Mapped `tags.type` to `asset.attribute.labels.key`.  
\- Mapped `tags.name` to `asset.attribute.labels.value`.   
2022-12-15 |  Enhancement  
\- Enhanced parser to parse application logs that are of Syslog format.  
\- Added Grok patterns for the logs with type `Session created`, `Session destroyed`, `Authentication attempt succeeded`, and `Authentication attempt failed`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
