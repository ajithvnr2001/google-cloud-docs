---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netscout-oci-changelog/
title: Change log for NETSCOUT_OCI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:44.721114+00:00
---

# Change log for NETSCOUT_OCI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netscout-oci-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETSCOUT_OCI

Date | Changes  
---|---  
2024-02-21 |  Enhancement:  
\- Added support for new version of Syslog CEF logs.  
\- Mapped `url` to `target.url`.  
\- Mapped `app` to `target.application`.  
\- When `src_iporhost` is a valid IP, then mapped it to `principal.ip` or else mapped it to `principal.hostname`.  
\- Mapped `mitreTactic`, `mitreTechnique`, `srcCount`, `dstCount`, `srcHostGroupCount`, `dstHostGroupCount`, `interfaceCount`, `violationCount`, `dstHostGroup`, and `srcHostGroup` to `security_result.detection_fields`.  
\- Removed `desc` mapping to `security_result.description` as it is already being mapped to `metadata.description`.  
\- Mapped `iocDescription` to `security_result.description`.  
\- Mapped `Category` to `security_result.category_details`.  
\- Mapped `Policy` and `Classification` to `additional.fields`.   
2023-09-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
