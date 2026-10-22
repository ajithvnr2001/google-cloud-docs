---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/siteminder-sso-changelog/
title: Change log for SITEMINDER_SSO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:57.679278+00:00
---

# Change log for SITEMINDER_SSO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/siteminder-sso-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SITEMINDER_SSO

Date | Changes  
---|---  
2025-02-12 |  Enhancement:  
\- Added support for the new format of syslog logs.   
2024-08-15 |  Enhancement:  
\- Added support for the new format of SYSLOG logs.   
2024-08-01 |  Enhancement:  
\- Added support for the SYSLOG format logs.  
\- Added support for the new format of JSON logs.   
2022-08-30 |  Enhancement: Added Mapping for the failed/requested logs :  
\- Mapped `sm_hostname` to `principal.hostname`  
\- Mapped `sm_username` to `principal.user.user_display_name`  
\- Mapped `metadata.event_type` to `USER_UNCATEGORIZED`  
\- Mapped `sm_impersonatorname` to `target.user.user_display_name`  
\- Mapped `sm_realmname` to `observer.group.group_display_name`  
\- Mapped `sm_domainname` to `observer.domain.name`  
\- Mapped `sm_realmoid` to `observer.asset.product_object_id`  
\- Mapped `sm_domainoid` to `principal.asset.product_object_id`  
\- Mapped `sm_clientip` to `principal.ip`  
\- Mapped `sm_sessionid` to `network.session_id`  
\- Mapped `sm_agentname` to `network.http.user_agent`  
\- Mapped `sm_action` to `network.http.method`  
\- Mapped `sm_eventid` to `metadata.product_log_id`  
\- Mapped `sm_resource` to `principal.resource.name`  
\- Mapped `sm_authdirserver` to `additional.fields`  
\- Mapped `sm_impersonatordirname` to `additional.fields`  
\- Mapped `sm_authdirname` to `additional.fields`  
\- Mapped `sm_transactionid` to `additional.fields`  
2022-04-19 |  New: Updating and Converting Customer specific version to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
