---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace_activity_changelog/
title: Change log for WORKSPACE_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:36:56.225788+00:00
---

# Change log for WORKSPACE_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace_activity_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKSPACE_ACTIVITY 

Date | Changes | 2022-04-27 | Device related fields mapped to asset entity as well   
Following fields were mapped:   
"DEVICE_TYPE", "DEVICE_NAME", "DEVICE_ID", "DEVICE_MODEL", "DEVICE_PLATFORM", "OS_VERSION", "DEVICE_USER", "COMPANY_DEVICE_ID"   
  
---|---  
2022-04-22 | Bug-fix -   
Modified mapping for 'id.customerId' from 'principal.user.userid' to 'about.labels'   
  
2022-04-13 | Enhancement- Added UDM events for logs where:   
\- applicationName is 'context_aware_access'   
\- applicationName is 'data_studio'   
\- events.name is 'email_as_attachment'   
\- applicationName is 'drive'.   
Mapped id.customerId to principal.user.userid.   
Corrected mapping for security_result[0].action[0] from "ALLOW" to "BLOCK" for one of the fields.   
Mapped fields "detector_id", "detector_type", "display_name" to "event.idm.read_only_udm.about.labels".   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
