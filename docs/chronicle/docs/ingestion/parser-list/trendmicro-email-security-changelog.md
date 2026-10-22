---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-email-security-changelog/
title: Change log for TRENDMICRO_EMAIL_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:31.822252+00:00
---

# Change log for TRENDMICRO_EMAIL_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-email-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_EMAIL_SECURITY

Date | Changes  
---|---  
2026-10-01 |  \- event.idm.read_only_udm.principal.user.userid: Removed mapping of `suser` from `event.idm.read_only_udm.principal.user.userid` UDM field when `suser` raw log field contains username details.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `suser_name` log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `device_vendor` log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `device_product` log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `device_version` log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `device_event_class_id` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `event_name` log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_host` log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.observer.application: Newly mapped `observer_app` log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- event.idm.read_only_udm.observer.process.pid: Newly mapped `observer_pid` log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `suser_app` log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `euid` log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `eaid` log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.employee_id: Newly mapped `x_eaid` log field with `event.idm.read_only_udm.principal.user.employee_id` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `suser_email` log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.department: Newly mapped `suser_dept` log field with `event.idm.read_only_udm.principal.user.department` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `link_clicked`, `campaign_label`, `utm_source`, `utm_campaign`, `utm_medium`, and `email_sent` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `item.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `item.extractType` and `item.urlType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: When raw log contains user details updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_UNCATEGORIZED.  
\- Added a grok pattern on `suser` to extract `suser_name`, `suser_app`, `suser_dept`, and `suser_kv`.  
\- Added a grok pattern on `link_clicked` to extract `link_clicked_val` and `suser_email`.   
2025-02-20 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
