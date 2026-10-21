---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-azure-changelog/
title: Change log for KUBERNETES_AUDIT_AZURE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:15:01.858987+00:00
---

# Change log for KUBERNETES_AUDIT_AZURE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-azure-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KUBERNETES_AUDIT_AZURE

Date | Changes  
---|---  
2024-12-11 |  Enhancement:  
\- Mapped `record.properties.log`, `record.properties.stream`, `record.properties.containerID`, and `record.serviceBuild` to `additional.fields`.   
2024-10-28 |  Enhancement:  
\- Mapped `verb` to `sec_result.action_details`.  
\- Mapped `record.properties.log.responseObject.spec.nonResourceAttributes.path` to `principal.process.file.full_path`.  
\- Mapped `record.properties.log.requestObject.spec.nonResourceAttributes.path` to `target.process.file.full_path`.   
2024-10-22 |  Enhancement:  
\- Mapped `record.properties.log.responseStatus.reason` and `record.properties.pod` to `additional.fields`.  
\- Mapped `record.properties.log.responseStatus.code` to `network.http.response_code`.   
2024-01-11 |  Enhancement:  
\- Added support for the new format of unparsed logs by converting them into an array.   
2023-06-20 |  \- Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
