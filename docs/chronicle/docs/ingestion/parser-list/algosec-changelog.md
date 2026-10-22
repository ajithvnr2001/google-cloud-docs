---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/algosec-changelog/
title: Change log for ALGOSEC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:44.003827+00:00
---

# Change log for ALGOSEC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/algosec-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ALGOSEC

Date | Changes  
---|---  
2025-12-05 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields to respect UDM fields in correct manner.  
\- Added a conditional check before already existing mapping of `firewall_device`.  
\- Refactored parser logic to handle JSON data within `report_data_json` and map its key-value pairs to UDM fields.  
\- Added a drop tag `TAG_MALFORMED_MESSAGE` for the logs if `kv_data` was not null and `kv_fail` was true.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip` and `event.idm.read_only_udm.target.ip`: Newly mapped `report_data.Device IP` raw log field with `event.idm.read_only_udm.target.asset.ip` and `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `report_data.BSI Level` , `report_data.SWIFT Score`, `processnamevalue` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `report_data.NIST_800-53 Level`, `report_data.GLBA Level`, `report_data.NIST_800-41 Score`, `report_data.DORA Level`, `report_data.TRM Level`, `report_data.NCA Score`, `report_data.LGPD Score`, `report_data.Number of Duplicate Objects`, `report_data.GLBA Score`, `report_data.BASEL Level`, `report_data.Report Date`, `report_data.NIST_800-171 Level`, `report_data.Rule Count`, `report_data.NCA Level`, `report_data.changes.Total Deleted`, `report_data.changes.Number of Rules Changes`, `report_data.changes.Total Number of Changes`, `report_data.changes.Number of Topology Changes`, `report_data.changes.Total Edited`, `report_data.changes.Number of Risk Changes`, `report_data.changes.Total Added`, `report_data.changes.Total Change Operations`, `report_data.changes.Number of Network Object Changes`, `report_data.changes.Number of Audit Log Changes`, `report_data.changes.Number of Baseline Changes`, `report_data.changes.Number of Policy Object Changes`, `report_data.changes.Number of Service Object Changes`, `report_data.changes.Other Changes`, `report_data.changes.Number of Application Object Changes`, `report_data.NIST_800-41 Level`, `report_data.Number of Disabled Rules`, `report_data.BSI Score`, `report_data.Number of Low Risks`, `report_data.PCI Score`, `report_data.Number of Low Severity Risky Rules`, `report_data.ISO27001 Score`, `report_data.SOX Level`, `report_data.Number of High Severity Risky Rules`, `report_data.Domain Name`, `report_data.PCI Level`, `report_data.ASD_ISM Score`, `report_data.Number of Unused Rules`, `report_data.ASD_ISM Level`, `report_data.Device Groups`, `report_data.HIPAA Level`, `report_data.GDPR Level`, `report_data.HKMA Level`, `report_data.Number of Medium Severity Risky Rules`, `report_data.NIST_800-171 Score`, `report_data.GDPR Score`, `report_data.Number of Suspected High Risks`, `report_data.Number of High Risks`, `report_data.PCI4 Score`, `report_data.Change By`, `report_data.Device Id`, `report_data.Device Brand`, `report_data.NERC Score`, `report_data.ISO27001 Level`, `report_data.SOX Score`, `report_data.NERC Level`, `report_data.BASEL Score`, `report_data.PCI4 Level`, `report_data.HIPAA Score`, `report_data.Number of Special Case Rules`, `report_data.Number of Covered Rules`, `report_data.Number of Suspected High Severity Risky Rules`, `report_data.Number of Medium Risks`, `report_data.SWIFT Level`, `report_data.TRM Score`, `report_data.LGPD Level`, `report_data.HKMA Score`, `report_data.ECB Score`, `report_data.ECB Level`, `report_data.DORA Score`, `report_data.NIST_800-53 Score` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2022-11-27 |  Enhancement:  
\- Parsed CEF format and grok related unparsed logs by adding event specific conditional block to handle them.  
\- Also added a drop tag to drop malformed logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
