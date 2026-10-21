---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/anomali-ioc-changelog/
title: Change log for ANOMALI_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:47:19.415854+00:00
---

# Change log for ANOMALI_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/anomali-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ANOMALI_IOC

Date | Changes  
---|---  
2026-08-04 |  Bug-Fix:  
\- Only populate `event.ioc` when IOC type is `ip` or `domain`.   
2024-02-09 |  Enhancement:  
\- Mapped `can_add_public_tags_label`, `owner_organization_id_label`, `created_by_label`, `is_public_label`, `is_editable_label`, `rdns_label`, `source_created_label`, `source_modified_label`, `subtype_label`, `uuid_label` and `update_id_label` to `entity.additional.fields`.  
\- Mapped `is_anonymous_label`, `source_reported_confidence_label`, `feed_id_label` and `threat_type_label` to `entity.metadata.threat.detection_fields`.  
\- Mapped `obj.source` to `entity.metadata.threat.threat_feed_name`.  
\- Mapped `obj.itype` to `entity.metadata.threat.threat_name`.  
\- Mapped `obj.meta.severity` to `entity.metadata.threat.severity_details`.  
\- Initialized `id_label` and `name_label` to null inside the `for loop`.  
\- Mapped `obj.threatscore` to `entity.metadata.threat.risk_score`.  
\- If `obj.type` is `md5` or `obj.itype` is `mal_md5`, then map `obj.value` to `entity.entity.file.md5` and set `metadata.entity_type` as `FILE`.  
\- If `obj.type` is `url`, then map `obj.value` to `entity.entity.url`.  
\- Mapped `obj.meta.severity` to `entity.metadata.threat.severity_details`.  
\- Mapped `obj.retina_confidence` to `metadata.threat.confidence_score`.  
\- Changed mapping of `obj.resource_uri` from `entity.entity.url` to `metadata.threat.url_back_to_product`.   
2024-01-25 |  Enhancement:  
\- Mapped `obj.status` to `entity.metadata.source_labels`.   
2024-01-19 |  Bug-Fix:  
\- Added support for the new format of unparsed JSON logs by converting them into an array.  
\- If `event_name` is `domain` and `shost` is not null then set `entity.metadata.entity_type` as `DMOMAIN_NAME`.   
2023-12-28 |  Enhancement:  
\- Mapped `obj.created.ts` to `entity.metadata.creation_timestamp` and `entity.metadata.threat.first_discovered_time`.  
\- Mapped `obj.modified_ts` to `entity.metadata.threat.last_updated_time`.  
\- Mapped `obj.confidence` to `entity.metadata.threat.confidence`.  
\- Mapped `obj.tags` to `entity.metadata.source_labels`.  
\- Mapped `obj.status` to `entity.metadata.threat.threat_status`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
