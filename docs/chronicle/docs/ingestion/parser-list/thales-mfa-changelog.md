---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-mfa-changelog/
title: Change log for THALES_MFA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:27.772594+00:00
---

# Change log for THALES_MFA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-mfa-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THALES_MFA

Date | Changes  
---|---  
2025-11-07 |  Enhancement:  
\- Added new grok patterns to support `LoggedIn`,`AssignToken`,`AUTH_ATTEMPT` actcode formats.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `subtype` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.name`: Newly mapped `deviceProduct` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `deviceVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `msgId` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.   
2022-07-13 |  Enhancement -  
\- Added on_error for reason,sec_action,security_result field in mutate filter.  
\- Mapped `reason` to `security_result.description`.  
\- Mapped `act` field value to `security_result.action_details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
