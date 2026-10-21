---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cylance-protect-changelog/
title: Change log for CYLANCE_PROTECT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:21:14.485416+00:00
---

# Change log for CYLANCE_PROTECT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cylance-protect-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYLANCE_PROTECT

Date | Changes  
---|---  
2025-05-16 |  Enhancement:  
\- event1.idm.read_only_udm.target.process.command_line: Newly mapped `Target Process Command Line` raw log field with `event1.idm.read_only_udm.target.process.command_line` UDM field  
\- event1.idm.read_only_udm.security_result.severity: Newly mapped `Severity` raw log field with `event1.idm.read_only_udm.security_result.severity` UDM field.   
2022-09-06 |  Bug-Fix: Fixed the flaky results from the mutate replace. Now the  
principal.process.file.sha256 should be consistently filled in when sha256  
exists in the logs.   
2022-08-11 |  Enhancement-  
Migrated customer specific parsers to default parser  
Converted all the mappings from sdm.proto to udm.proto   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
