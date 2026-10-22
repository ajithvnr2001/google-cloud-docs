---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/slack-audit-changelog/
title: Change log for SLACK_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:57.191033+00:00
---

# Change log for SLACK_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/slack-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SLACK_AUDIT

Date | Changes  
---|---  
2026-09-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.labels`: Removed mappings of `actor.type`, `details.previous_ip_address`, and `details.previous_ua` raw log fields from `event.idm.read_only_udm.principal.labels` UDM field as the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `actor.type`, `details.previous_ip_address`, and `details.previous_ua` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.resource.id`: Removed mapping of `context.location.id` raw log field from `event.idm.read_only_udm.about.resource.id` UDM field as the field is deprecated.  
\- `event.idm.read_only_udm.about.resource.product_object_id`: Mapped `context.location.id` raw log field with `event.idm.read_only_udm.about.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details.action_timestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `details.ip_address_details` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.state` and `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `details.location` raw log field with `event.idm.read_only_udm.principal.location.state` and `event.idm.read_only_udm.principal.location.country_or_region` UDM fields.   
2025-03-28 |  Enhancement:  
\- The Gsub pattern was updated to `\\r\\n` from `\r\n` to fix the problem of `rn` being stripped from the generated output.  
\- A conversion block was added to explicitly convert the details.type field to a string.  
\- Mapped `actor.user.id` to `principal.user.userid`.  
\- Mapped `details.url_private` to `target.url`.  
\- Mapped `details.shared_with.channel_id` `target.labels`.  
\- Mapped `details.reason` to `security_result.description`.  
\- Mapped `details.previous_ip_address` to `principal.labels`.  
\- Mapped `details.previous_ua` to `principal.labels`.   
2023-10-27 |  Enhancement:  
\- Mapped `details.reason` to `security_result.description`.   
2022-08-03 |  Enhancement:  
\- Modified mapping for `prin_ip` from `principal.nat_ip` to `principal.ip`.   
2022-04-07 |  \- Corrected mapping for product_object_id.  
\- Corrected the user mappings for second log format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
