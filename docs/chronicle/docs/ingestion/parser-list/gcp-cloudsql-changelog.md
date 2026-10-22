---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudsql-changelog/
title: Change log for GCP_CLOUDSQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:43.120028+00:00
---

# Change log for GCP_CLOUDSQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudsql-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_CLOUDSQL

Date | Changes  
---|---  
2026-03-19 |  The UDM mapping of `metadata.event_type` for `cloudsql_database` resource type has been updated to replace `GENERIC_EVENT` with more accurate `metadata.event_type` values:  
\- If textPayload` includes `select`, the event is categorized as `USER_RESOURCE_ACCESS".   
2026-02-27 |  The UDM mapping of `metadata.event_type` for `cloudsql_database` resource type has been updated to replace `GENERIC_EVENT` with more accurate `metadata.event_type` values:  
\- If `textPayload` includes INSERT, the event is categorized as `USER_RESOURCE_UPDATE_CONTENT`.  
\- If textPayload` includes SELECT, the event is categorized as `USER_RESOURCE_ACCESS".   
2025-12-05 |  Added a new grok pattern to parse PostgreSQL logs with `DETAIL:` in the textPayload.   
2025-11-20 |  Added a new grok pattern to parse PostgreSQL logs with `STATEMENT:` in the textPayload.   
2025-08-20 |  principal.namespace: Removed mapping of `protoPayload.request.metadata.namespace` from `principal.namespace` UDM field and mapped to `additional.fields` in order to prevent the feed namespace from being overwritten by the prebuilt parser.   
2025-08-11 |  \- `cloudsql.instances.query`: Added support for the event `cloudsql.instances.query` and its relevant corresponding raw log fields  
`protoPayload.request.auditClass`, `protoPayload.request.databaseSessionId`, `protoPayload.request.auditType`, `protoPayload.request.statementId`, `protoPayload.request.substatementId`, `protoPayload.request.command`, `protoPayload.request.object`, `protoPayload.request.objectType`, `protoPayload.request.chunkCount`, `protoPayload.request.chunkIndex`, `protoPayload.request.statement`, `protoPayload.request.parameter`, `protoPayload.request.priv_user`, `protoPayload.request.host`, `protoPayload.request.errCode`, `protoPayload.request.objects.object_type`.  
\- `target.process.command_line`: Removed mapping of `protoPayload.request.query` from `target.process.command_line` UDM field  
`target.resource.attribute.labels[query]`: Mapped `protoPayload.request.query` raw log field with `target.resource.attribute.labels[query]` UDM field  
\- `about.labels[database_name]`: Removed mapping of `protoPayload.request.objects.db` from `about.labels[database_name]` UDM field  
`target.resource.attribute.labels[database_name]`: Mapped `protoPayload.request.objects.db` raw log field with `target.resource.attribute.labels[database_name]` UDM field  
\- `about.labels[objects_name]`: Removed mapping of `protoPayload.request.objects.name` from `about.labels[objects_name]` UDM field  
`target.resource.attribute.labels[obj_name]`: Mapped `protoPayload.request.objects.name` raw log field with `target.resource.attribute.labels[obj_name]` UDM field   
2025-04-17 |  \- Modified the mapping of `metadata.event_type` to `USER_LOGIN` only when `resource_type` is `cloudsql_database` or `alloydb.googleapis.com/Instance`, and `textPayload` contains `Logon` or `connection authorized`.   
2024-09-27 |  \- Mapped `labels._HOSTNAME` to `principal.hostname` and `principl.asset.hostname` for the sqlserver.err logs  
\- Mapped `textPayload` log field to `metadata.description` for the sqlserver.err logs  
\- Extracted the user from the `textPayload` log field and mapped to `target.user.userid` for the sqlserver.err logs   
2024-09-05 |  Enhancement:  
\- Mapped `resource.labels.cluster_id` to `target.resource.id`.  
\- Mapped `labels.CONSUMER_PROJECT` to `target.asset.attribute.cloud.project.id`.  
\- Mapped `event_type` to `USER_LOGIN` when `resource_type` is either `cloudsql_database` or `alloydb.googleapis.com/Instance`.   
2024-07-19 |  Added additional mappings for deprecated noun.labels.   
2024-06-13 |  Enhancement:  
\- Added `gsub` to remove `\n` from the `textPayload` field.   
2024-05-15 |  Enhancement:  
\- Added new Grok patterns to parse `textPayload` field.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-11-01 |  \- Promoted the parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
