---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-security-verify-saas-changelog/
title: Change log for IBM_SECURITY_VERIFY_SAAS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:40:20.079646+00:00
---

# Change log for IBM_SECURITY_VERIFY_SAAS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-security-verify-saas-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_SECURITY_VERIFY_SAAS

Date | Changes  
---|---  
2023-10-27 |  Enhancement:  
\- Mapped `data.ib_request_id` to `metadata.product_log_id`.  
\- Mapped `data.status_code`, `data.performedby_type`, `data.subject_type`, `data.target_type`, `data.templateid`, `data.subjectid`, `data.performedby`, `data.action`, and `data.performedby_clientname` to `additional.fields`.  
\- Mapped `data.cause` to `security_result.summary`.  
\- Mapped `data.json.Operations.path`, `data.json.Operations.op`, and `data.json.Operations.value` to `additional.fields`.   
2023-09-20 |  Bug-Fix:  
\- Mapped `event_type` to `metadata.product_event_type`.  
\- Mapped `geoip.as_org`, `geoip.country_iso_code` to `additional.fields`.  
\- Added conditional checks for date filter to support `UNIX` and `UNIX_MS` time format.   
2023-08-30 |  \- Mapped `data.account_name` to `target.user.user_display_name`.  
\- Mapped `data.targetid` to `target.resource.id`.  
\- Mapped `data.target` to `target.user.userid`.   
2023-07-05 |  Bug:  
\- Defined the `data.result`,`data.client_name`.   
2023-06-27 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
