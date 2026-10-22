---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/code42-incydr-changelog/
title: Change log for CODE42_INCYDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:54.965763+00:00
---

# Change log for CODE42_INCYDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/code42-incydr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CODE42_INCYDR

Date | Changes  
---|---  
2026-03-13 |  \- `event.idm.read_only_udm.security_result.detection_fields`: Changed key format for `filter.term` from `group_filter_term` to `group_filter_term_%{i}_%{j}`, changed key format for `filter.operator` from `group_filter_operator` to `group_filter_operator_%{i}_%{j}` and changed key format for `group.filterClause` from `group_filterclause` to `group_filterclause_%{i}`.  
\- `event.idm.read_only_udm.metadata.id`: Newly mapped `idme_evnt_id` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `audit_log` (key: type), `risk.score` (key: risk_score_parsed), `filter.value` (key: group_filter_value_%{i}_%{j}), `filter.display` (key: filter_display), `group.display` (key: group_display_%{i}) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW` and `BLOCK` based on conditional check.  
\- `event.idm.read_only_udm.principal.user.userid`: If `parsed_actorName` is extracted and differs from `actorId`, mapped `parsed_actorName` to `event.idm.read_only_udm.principal.user.userid` UDM field and modified parsing logic for `actorName` raw log field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the `event_type` to `FILE_DELETED` when there is target file and principal machine data.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `filter.value` from `event.idm.read_only_udm.metadata.product_log_id` UDM field when it contains a date format.  
\- Added a Grok pattern on `actorName` to extract `parsed_actorName`.  
\- Added a conditional check for `risk.score` values equal to 0 are mapped to `event.idm.read_only_udm.additional.fields` with key risk_score_parsed.   
2025-09-24 |  \- Added gsub for the `message` data field to parse the logs in the correct format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source.domains`, `destination.domains`, `source.domains`, `destination.domains`, `paste.mimeTypes`, `paste.visibleContentSize`, `origin`, `evnt.inserted` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `risk.activityTier`, `risk.activityTier` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels` : Newly mapped `source_tabs.title`, `source_tabs.url` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Corrected the mapping for the `file.archiveId` raw log field and mapped to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Corrected the mapping for the `source.email.from` raw log field and mapped to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2024-12-10 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
