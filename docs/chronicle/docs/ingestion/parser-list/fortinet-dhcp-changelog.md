---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-dhcp-changelog/
title: Change log for FORTINET_DHCP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:45.353021+00:00
---

# Change log for FORTINET_DHCP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-dhcp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_DHCP

Date | Changes  
---|---  
2022-11-21 |  Enhancement:  
\- Mapped the field `srcip` to `principal.ip`.  
\- Mapped the field `srcport` to `principal.port`.  
\- Mapped the field `srccountry` to `principal.location.country_or_region`.  
\- Mapped the field `interface` to `principal.hostname`.  
\- Mapped the field `user_name` to `principal.user.user_display_name`.  
\- Mapped the field `srcuuid` to `principal.user.product_object_id`.  
\- Mapped the field `host_name` to `intermediary.hostname`.  
\- Mapped the field `dstip` to `target.ip`.  
\- Mapped the field `dstport` to `target.port`.  
\- Mapped the field `dstcountry` to `target.location.country_or_region`.  
\- Mapped the field `application` to `target.application`.  
\- Mapped the field `dstuuid` to `target.user.product_object_id`.  
\- Mapped the field `url` to `target.url`.  
\- Mapped the field `profile` to `target.resource.name`.  
\- Mapped the field `sessionid` to `network.session_id`.  
\- Mapped the field `direction` to `network.direction`.  
\- Mapped the field `proto` to `network.ip_protocol`.  
\- Mapped the field `duration` to `network.session_duration.seconds`.  
\- Mapped the field `sentbyte` to `network.sent_bytes`.  
\- Mapped the field `rcvdbyte` to `network.received_bytes`.  
\- Mapped the field `level` to `security_result.severity_details`.  
\- Mapped the field `policyid` to `security_result.rule_id`.  
\- Mapped the field `policyname` to `security_result.rule_name`.  
\- Mapped the field `policytype` to `security_result.rule_type`.  
\- Mapped the field `catdesc` to `security_result.category_details`.  
\- Mapped the field `crlevel` to `security_result.severity`.  
\- Mapped the field `crscore` to `security_result.severity_details`.  
\- Mapped the field `srcintf`, `srcintfrole`, `dstintf`, `dstintfrole` and `craction` to `security_result.detection_fields`.  
\- Mapped the field `sentpkt`, `rcvdpkt` and `appcat` to `additional.fields`.  
\- Mapped the field `action` to `security_result.action` and `security_result.action_details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
