---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-utm-changelog/
title: Change log for SOPHOS_UTM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:24:43.903662+00:00
---

# Change log for SOPHOS_UTM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-utm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOPHOS_UTM

Date | Changes  
---|---  
2025-07-25 |  Enhancement -  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `content-type`, `reason` , and `referer` raw log fields with `event.idm.read_only_udm.additional.fields` UDM fields.  
\- Added a new grok for the `url` raw log field to parse the `HOSTNAME` from the `url` raw log field and map it to the `target.hostname` and `target.asset.hostname` UDM field.   
2024-12-18 |  Enhancement -  
\- Mapped `size` to `target.file.size`.  
\- Mapped `subject` to `network.email.subject`  
\- Mapped `from` to `network.email.from`.  
\- Mapped `to` to `network.email.to`.   
2024-10-10 |  Enhancement -  
\- Mapped `virus` to `security_result.detection_fields`.  
\- Mapped `filename` to `target.file.names`.  
\- Mapped `severity` to `security_result.severity_details`.  
\- Added `gsub` to parse unparsed logs.  
\- Parsed `Authentication` logs to `USER_LOGIN` event type.   
2024-05-29 |  Enhancement -  
\- Mapped `url` to `target.hostname` and `target.asset.hostname`.   
2022-06-30 |  Enhancement -  
\- Mapped `size` to `additional.fields`.  
\- Mapped `fullreqtime` to `additional.fields`.  
\- Mapped `category` to `security_result.detection_fields`.  
\- Mapped `device` to `additional.fields`.  
\- Mapped `exceptions` to `additional.fields`.  
\- When `action` is equal to `DROP` then Mapped `security_result.action` to `BLOCK`.  
\- Mapped `inter_host` to `intermediary.hostname`.   
2022-04-13 |  Enhancement - Added mappings for following fields:  
\- `categoryname` to `security_result.category_details`.  
\- `user` to `target.user.userid`  
\- `ad_domain` to `target.administrative_domain`  
\- `group` to `target.group.group_display_name`  
\- `sys` to `metadata.product_event_type`  
\- `application` to `principal.application`  
\- `auth` to `extensions.auth.auth_details`  
\- `profile` to `security_result1.rule_name`  
\- `app-id`, `reputation`, `request`, `authtime`, `dnstime`, `aptptime`, `cattime`, `avscantime` to `additional.fields`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
