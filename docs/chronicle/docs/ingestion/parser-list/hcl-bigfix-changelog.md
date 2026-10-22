---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hcl-bigfix-changelog/
title: Change log for HCL_BIGFIX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:27.620446+00:00
---

# Change log for HCL_BIGFIX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hcl-bigfix-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HCL_BIGFIX

Date | Changes  
---|---  
2023-12-08 |  Bug-Fix:  
\- Added gsub function to remove double quotes.  
\- Mapped `CloudInfo` to `event.idm.entity.entity.labels`.   
2022-08-30 |  Enhancement:  
\- Removed mapping for field `CIDR_Subnet_String`.  
\- Mapped `metadata.entity_type` to `USER` when `SerialNumber` is empty.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `user_role` from `entity.user.role_name` to `entity.user.attribute.roles`.   
2022-06-07 |  Bug-Fix : Parser converted from UDM to ENTITY completely.   
2022-04-27 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
