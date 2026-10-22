---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs_edr_changelog/
title: Change log for CS_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:52.540289+00:00
---

# Change log for CS_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs_edr_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CS_EDR 

Date | Changes | 2022-04-27 | Bug - Fix: 1. Changed udm event_type from GENERIC_EVENT to USER_LOGIN for logs with ExternalApiType = Event_AuthActivityAuditEvent.   
2\. Changed mappings for target_user,actor_user, actor_user_uuid from additional.fields to target.user.email_addresses, target.user.user_display_name, target.user.userid respectively.   
  
---|---  
2022-04-25 | Enhancement - Mapped "RemoteAddressIP4" to principal.ip.   
  
2022-04-14 | Bug - Added Support for ScriptContent field for all type of logs   
  
2022-04-13 | Enhancement-Added mappings for new fields   
Added new event mappings - AuthenticationPackage mapped to target.resource.name   
  
2022-04-04 | Bug - Mapped "OriginatingURL" to principal.url for NetworkConnect events.   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
