---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-nexpose-changelog/
title: Change log for RAPID7_NEXPOSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:29.302925+00:00
---

# Change log for RAPID7_NEXPOSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-nexpose-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RAPID7_NEXPOSE

Date | Changes  
---|---  
2024-05-14 |  Enhancement:  
\- Added support to handle new JSON logs.  
\- Mapped `description.text` to `metadata.description`.  
\- Mapped `categories`, `pci.adjustedCVSSScore`, `pci.adjustedSeverityScore`, `pci.fail`, and `pci.status` to `additional.fields`.  
\- Mapped `cvss.v2.accessComplexity`, `cvss.v2.accessVector`, `cvss.v2.authentication`, `cvss.v2.availabilityImpact`, `cvss.v2.confidentialityImpact`, `cvss.v2.integrityImpact`, `cvss.v2.vector`, `cvss.v3.attackComplexity`, `cvss.v3.attackVector`, `cvss.v3.availabilityImpact`, `cvss.v3.confidentialityImpact`, `cvss.v3.privilegeRequired`, `cvss.v3.integrityImpact`, `cvss.v3.scope`, `cvss.v3.userInteraction`, and `cvss.v3.vector` to `security_result.detection_fields`.   
2022-09-27 |  Enhancement:  
\- Added support for syslog pattern to parse the unparsed logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
