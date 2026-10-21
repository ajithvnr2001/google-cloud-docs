---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/splunk-changelog/
title: Change log for SPLUNK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:23:43.044401+00:00
---

# Change log for SPLUNK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/splunk-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SPLUNK

Date | Changes  
---|---  
2024-05-01 |  Update the mapping for deprecated UDM field.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.  
\- Modified logic to map `security_result.action_details` UDM field even if the values of `action` raw log field does not match the logic.   
2023-05-17 |  Added `auth.type` for login events.   
2023-01-04 |  \- Handled error and changed mapping for `Authentication` datamodel, if `user_id` variable is empty then `user` variable will be mapped to `principal.user.userid`. Also, event_type is now mapped to USER_LOGIN.  
\- Handled unparsed log for `Endpoint` datamodel.  
\- Modified mapping for `Change` datamodel. The `user` field is mapped to `target.user.user.userid`, the `user_name` field is mapped to principal.user.user_display_name for tag `change` and `account`, the `src_user` field is mapped to principal.user.userid. Also, event_type is mapped to `USER_UNCATEGORIZED`.  
\- Modified mapping for the fields `result` and `result_id` in the `Change` datamodel to metadata.description and metadata.product_event_type.  
\- Changed mapping for the `Network Traffic` datamodel. If `user_id` variable is empty then the `user` variable is mapped to `principal.user.userid`.   
2022-11-09 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
