---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalarts-ifilter-changelog/
title: Change log for DIGITALARTS_IFILTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:42:41.806622+00:00
---

# Change log for DIGITALARTS_IFILTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalarts-ifilter-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DIGITALARTS_IFILTER

Date | Changes  
---|---  
2025-10-16 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `content_type` and `trailing_id` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `group_name` raw log field(s) with event.idm.read_only_udm.principal.user.group_identifiers UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `webservice_id` raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_host` raw log field(s) with event.idm.read_only_udm.intermediary.ip UDM field if its a valid IP address.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field(s) with event.idm.read_only_udm.intermediary.hostname UDM field if its not a valid IP address.  
\- event.idm.read_only_udm.network.tls.version_protocol: Newly mapped `request_version` raw log field(s) with event.idm.read_only_udm.network.tls.version_protocol UDM field if its a valid IP address.   
2024-06-24 |  Enhancement:  
\- Modified the date format to add timezone.   
2023-04-17 |  Enhancement -  
\- Generalization of the drop logs processing.  
\- Handle logs without a target IP address and hostname.  
\- Improved the precision of the URL Grok pattern.  
\- Added security action patterns.  
\- Mapped `user_agent` to `network.http.parsed_user_agent`.   
2023-02-09 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
