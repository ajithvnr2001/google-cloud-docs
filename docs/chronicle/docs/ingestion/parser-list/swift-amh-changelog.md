---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/swift-amh-changelog/
title: Change log for SWIFT_AMH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:01:14.035530+00:00
---

# Change log for SWIFT_AMH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/swift-amh-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SWIFT_AMH

Date | Changes  
---|---  
2025-11-26 |  Enhancement:  
\- event.idm.read_only_udm.about.labels: Removed mapping of `target.traceId` raw log field from event.idm.read_only_udm.about.labels as it is a deprecacted UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `target.traceId` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.about.labels: Removed mapping of `target.parentSpanId` raw log field from event.idm.read_only_udm.about.labels as it is a deprecacted UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `target.parentSpanId` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.about.labels: Removed mapping of `sag` raw log field from event.idm.read_only_udm.about.labels as it is a deprecacted UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sag` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.about.labels: Removed mapping of `mr_id` raw log field from event.idm.read_only_udm.about.labels as it is a deprecacted UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mr_id` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `user_roles` raw log field to event.idm.read_only_udm.principal.user.attribute.roles UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `suffix` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `component` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `definition` raw log field to event.idm.read_only_udm.target.resource.name UDM field.  
\- event.idm.read_only_udm.security_result.summary: Mapped `event.idm.read_only_udm.security_result.summary` as `Rule execution error` when `sag` is `AMH-RUL-00010`.  
\- event.idm.read_only_udm.security_result.action: Mapped `event.idm.read_only_udm.security_result.action` as `BLOCK` when `sag` is `AMH-RUL-00010`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `exception`, `invalid_value`, `value_type`, `pattern`, `thread_info`, `logger`, `product_event_id` raw log fields to event.idm.read_only_udm.additional.fields UDM field.   
2025-09-23 |  Enhancement:  
\- Enhanced grok pattern to parse `operator` username to event.idm.read_only_udm.src.user.userid mapping to output `ADMIN` when operator is `administrator`.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `createdAt` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.intermediary.resource.attribute.labels: Newly mapped `data.properties._file_inode.str` raw log field to event.idm.read_only_udm.intermediary.resource.attribute.labels.  
\- event.idm.read_only_udm.intermediary.resource.attribute.labels: Newly mapped `data.properties._ecs_agent_version.str` raw log field to event.idm.read_only_udm.intermediary.resource.attribute.labels.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `parentSpanId`, `data.spanId`, `data.traceId` and `offset` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `data.level` raw log field to event.idm.read_only_udm.security_result.severity.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `uumid` raw log field to event.idm.read_only_udm.principal.user.product_object_id.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_object_id` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product_event_type` raw log field to event.idm.read_only_udm.metadata.product_event_type.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_id` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.principal.asset.creation_time: Newly mapped `data.creationDate` raw log field to event.idm.read_only_udm.principal.asset.creation_time.   
2024-03-14 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
