---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bomgar-changelog/
title: Change log for BOMGAR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:18:32.821612+00:00
---

# Change log for BOMGAR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bomgar-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BOMGAR

Date | Changes  
---|---  
2026-07-13 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` to include cases where `_userid` is present.   
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `exc` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `loggerHost` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `loggerHost` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `product`, `sequenceId`, and a combination of `site_id`, `segment`, and `total_segment` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.vendor_name: Updated mapping for event.idm.read_only_udm.metadata.vendor_name from `BeyondTrust` to `BeyondTrust Bomgar`.   
2024-04-15 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `who` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2024-01-12 |  Enhancement:  
\- Removed the drop statement with tag `TAG_NO_SECURITY_VALUE` when `status` is `challenge`.  
\- Added an email check for `temp_email` before mapping to `target.user.email_addresses`.   
2022-11-24 |  Bug-Fix:  
\- Modified a Grok pattern that parses `who` to correctly parse the fields `_user_display_name`, `_userid`, and `_method`.  
\- If `event.idm.read_only_udm.metadata.event_type` is `USER_LOGIN` then set `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.   
2022-10-13 |  Enhancement:  
\- Merged customer specific parser to default.   
2022-09-26 |  Enhancement:  
\- Merged customer specific parser to default.   
2022-08-19 |  Enhancement:  
\- Migrated the custom parsers into default parser and deleted the custom parsers.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
