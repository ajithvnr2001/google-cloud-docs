---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-central-changelog/
title: Change log for ARUBA_CENTRAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:40.123199+00:00
---

# Change log for ARUBA_CENTRAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-central-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARUBA_CENTRAL

Date | Changes  
---|---  
2025-03-24 |  Enhancement:  
\- Added support to parse JSON log format.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `cid` to `principal.user.product_object_id`.  
\- Mapped `alert_type` to `metadata.product_event_type`.  
\- Mapped `device_id` to `principal.user.userid`.  
\- Mapped `details.user` to `principal.user.userid`.  
\- Mapped `details.group_name` to `principal.group.group_display_name`.  
\- Mapped `details.config_change` to `security_result.summary`.  
\- Mapped `description` to `security_result.description`.  
\- Mapped `target_userid` to `target.user.userid`.  
\- Mapped `target_mac` to `target.mac`.  
\- Mapped `princ_mac` to `principal.mac`.  
\- Mapped `network_ssid` to `network.session_id`.  
\- Mapped `cluster_hostname` to `principal.hostname`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `__base_url` to `metadata.url_back_to_product`.  
\- Mapped `state` to `security_result.detection_fields`.  
\- Mapped `nid` , `setting_id` , `details.dev_type` , `webhook` and `operation` to `additional.fields`.  
\- Mapped `details.group` to `principal.group.product_object_id`.  
\- Mapped `details.labels` to `security_result.about.labels`.  
\- If `severity` in `CRITICAL` , `MAJOR` then map `severity` as `CRITICAL` to `security_result.severity`.  
\- Added conditional check if `alert_type` is `DEVICE_CONFIG_CHANGE_DETECTED` then map `event_type` to `USER_RESOURCE_UPDATE_CONTENT`.  
\- Enhanced validation check for `datetime` , `host` , `app` , `pid` , `desc` , `userid` , `amm` and `event_data` before mapping them.   
2024-12-05 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
