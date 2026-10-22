---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel471-watcher-alerts-changelog/
title: Change log for INTEL471_WATCHER_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:41.556872+00:00
---

# Change log for INTEL471_WATCHER_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel471-watcher-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for INTEL471_WATCHER_ALERTS

Date | Changes  
---|---  
2025-04-03 |  \- `event.idm.read_only_udm.metadata.additional.fields`: Newly mapped `report.uid` and `report.admiraltyCode` raw log field with `event.idm.read_only_udm.metadata.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `report.subject` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `report.portalReportUrl` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `report.released` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-11 |  \- Mapped `post.links.forum.description` and `actor.links.reports.subject` to `metadata.description`.  
\- Mapped `post.links.authorActor.uid`, `data_leak_post.uid` and `actor.uid` to `principal.user.userid`.  
\- Mapped `post.links.authorActor.handle` and `actor.links.reports.actorHandle` to `principal.user.attribute.labels`.  
\- Mapped `data_leak_post.file_listing.download_url` and `actor.links.reports.portalReportUrl` to `principal.url`.  
\- Mapped `post.links.forum.uid`, `post.links.forum.name`, `post.links.thread.uid`, `post.links.thread.topic`, `post.links.thread.count`, `post.uid`, `post.message`, `highlights.field`, `highlights.chunks.text`, `highlights.chunks.hl`, `actor.links.forumTotalCount`, `actor.links.forumPrivateMessageTotalCount`, `actor.links.instantMessageChannelTotalCount`, `actor.links.reportTotalCount`, `actor.links.instantMessageTotalCount`, `actor.links.instantMessageServerTotalCount`, `actor.links.forumPostTotalCount`, `actor.lastUpdated`, `actor.activeFrom`, `actor.activeUntil`, `data_leak_post.chunk_number`, `data_leak_post.links.blog.uid`, `data_leak_post.links.blog.name`, `data_leak_post.links.thread.uid`, `data_leak_post.links.thread.topic`, `data_leak_post.links.thread.count`, `data_leak_post.message`, `actor.links.reports.uid`, `actor.links.reports.admiraltyCode`, `actor.links.reports.dateOfInformation` to `additional.fields`.   
2024-10-17 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
