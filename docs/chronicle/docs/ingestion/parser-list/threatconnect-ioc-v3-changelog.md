---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatconnect-ioc-v3-changelog/
title: Change log for THREATCONNECT_IOC_V3 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:35.320271+00:00
---

# Change log for THREATCONNECT_IOC_V3  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatconnect-ioc-v3-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THREATCONNECT_IOC_V3

Date | Changes  
---|---  
2026-07-03 |  Enhancement  
\- `event.idm.entity.entity.labels`: Removed mapping of `rating`, `threatAssessRating`, `webLink`, `threatAssessConfidence`, `threatAssessScoreObserved`, `threatAssessScoreFalsePositive`, `calScore`, `observations`, `privateFlag`, `active`, `activeLocked`, `dnsActive`, `whoisActive` and `fileActions` from `event.idm.entity.entity.labels` UDM field since the UDM field is deprecated.  
\- `event.idm.entity.entity.resource.attribute.labels`: Mapped `type`, `summary`, `text`, `rating`, `threatAssessRating`, `webLink`, `threatAssessConfidence`, `threatAssessScoreObserved`, `threatAssessScoreFalsePositive`, `calScore`, `observations`, `privateFlag`, `active`, `activeLocked`, `dnsActive`, `whoisActive` and `fileActions` raw log fields with `event.idm.entity.entity.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.entity.metadata.entity_type`: Newly set `event.idm.read_only_udm.entity.metadata.entity_type` to `IP_ADDRESS` when ip-address is present.   
2026-03-02 |  Enhancement  
\- `event.idm.entity.entity.file.md5`: Newly mapped `file.md5` raw log field with `event.idm.entity.entity.file.md5` UDM field.  
\- `event.idm.entity.entity.file.sha1`: Newly mapped `file.sha1` raw log field with `event.idm.entity.entity.file.sha1` UDM field.  
\- `event.idm.entity.entity.file.sha256`: Newly mapped `file.sha256` raw log field with `event.idm.entity.entity.file.sha256` UDM field.  
\- `event.idm.read_only_udm.entity.relations.entity.labels`: Newly mapped `associatedindicators.dnsActive` (key: `associatedindicators_dnsActive`) and `associatedindicators.whoisActive` (key: `associatedindicators_whoisActive`) raw log fields with `event.idm.read_only_udm.entity.relations.entity.labels` UDM field.  
\- `event.idm.entity.entity.labels`: Newly mapped `dnsActive` (key: `dnsActive`) and `whoisActive` (key: `whoisActive`) raw log fields with `event.idm.entity.entity.labels` UDM field.  
\- `event.idm.entity.metadata.entity_type`: Setting `event.idm.entity.metadata.entity_type` to `FILE` when File data is present and `type` raw log field is `FILE`.  
\- Added a string conversion block for `rating` raw log field.  
\- Modified UDM field name from `event.idm.entity.metadata.security_result` to `event.idm.entity.entity.security_result`.   
2025-11-26 |  \- event.idm.read_only_udm.entity.entity.asset.product_object_id: Newly mapped `id` raw log field with event.idm.read_only_udm.entity.entity.asset.product_object_id UDM field.  
\- event.idm.read_only_udm.entity.metadata.threat.threat_feed_name: Newly mapped `ownerName` raw log field with event.idm.read_only_udm.entity.metadata.threat.threat_feed_name UDM field.  
\- event.idm.read_only_udm.entity.metadata.threat.threat_id: Newly mapped `ownerId` raw log field with event.idm.read_only_udm.entity.metadata.threat.threat_id UDM field.  
\- event.idm.read_only_udm.entity.metadata.threat.confidence_score: Newly mapped `confidence` raw log field with event.idm.read_only_udm.entity.metadata.threat.confidence_score UDM field.  
\- event.idm.read_only_udm.entity.metadata.interval.start_time: Newly mapped `dateAdded` raw log field with event.idm.read_only_udm.entity.metadata.interval.start_time UDM field.  
\- event.idm.read_only_udm.entity.metadata.interval.end_time: Newly mapped `lastModified` raw log field with event.idm.read_only_udm.entity.metadata.interval.end_time UDM field.  
\- event.idm.read_only_udm.entity.entity.url: Newly mapped `legacyLink` raw log field with event.idm.read_only_udm.entity.entity.url UDM field.  
\- event.idm.read_only_udm.entity.entity.user.email_addresses: Newly mapped `address` raw log field with event.idm.read_only_udm.entity.entity.user.email_addresses UDM field.  
\- event.idm.read_only_udm.entity.entity.hostname: Newly mapped `hostName` raw log field with event.idm.read_only_udm.entity.entity.hostname UDM field.  
\- event.idm.read_only_udm.entity.entity.ip: Newly mapped `ip` raw log field with event.idm.read_only_udm.entity.entity.ip UDM field.  
\- event.idm.read_only_udm.entity.entity.labels: Newly mapped `rating`, `threatAssessRating`, `webLink`, `threatAssessConfidence`, `threatAssessScoreObserved`, `threatAssessScoreFalsePositive`, `calScore`, `observations`, `privateFlag`, `active`, `activeLocked`, `fileActions.count` raw log fields with event.idm.read_only_udm.entity.entity.entity.labels UDM field.  
\- event.idm.read_only_udm.entity.metadata.threat.risk_score: Newly mapped `threatAssessScore` raw log field with event.idm.read_only_udm.entity.metadata.threat.risk_score UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.asset.product_object_id: Newly mapped `associatedGroups.data.id`, `associatedIndicators.data.id`, `tags.data.id`, `attributes.data.id` raw log field with event.idm.read_only_udm.entity.relations.entity.asset.product_object_id UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.asset.attribute.creation_time: Newly mapped `associatedGroups.data.dateAdded`, `associatedIndicators.data.dateAdded`, `attributes.data.dateAdded` raw log field with event.idm.read_only_udm.entity.relations.entity.asset.attribute.creation_time UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.asset.attribute.last_update_time: Newly mapped `associatedGroups.data.lastModified`, `associatedIndicators.data.lastModified`, `tags.data.lastUsed`, `attributes.data.lastModified` raw log field with event.idm.read_only_udm.entity.relations.entity.asset.attribute.last_update_time UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.url: Newly mapped `associatedGroups.data.legacyLink`, `associatedIndicators.data.legacyLink`, `attributes.data.value` raw log field with event.idm.read_only_udm.entity.relations.entity.url UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.labels: Newly mapped `associatedGroups.data.xid`, `associatedGroups.data.upVoteCount`, `associatedGroups.data.downVoteCount`, `associatedGroups.data.generatedReport`, `associatedGroups.data.webLink`, `associatedGroups.data.type`, `associatedGroups.data.fileName`, `associatedGroups.data.status`, `associatedGroups.data.documentType`, `associatedGroups.data.documentDateAdded`, `associatedGroups.data.publishDate`, `associatedIndicators.data.rating`, `associatedIndicators.data.privateFlag`, `associatedIndicators.data.active`, `associatedIndicators.data.activeLocked`, `tags.data.name`, `attributes.data.pinned`, `attributes.data.default` raw log field with event.idm.read_only_udm.entity.relations.entity.labels UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.user.role_description: Newly mapped `associatedGroups.data.name` raw log field with event.idm.read_only_udm.entity.relations.entity.user.role_description UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.user.user_display_name: Newly mapped `associatedGroups.data.createdBy.userName` raw log field with event.idm.read_only_udm.entity.relations.entity.user.user_display_name UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.user.first_name: Newly mapped `associatedGroups.data.createdBy.firstName` raw log field with event.idm.read_only_udm.entity.relations.entity.user.first_name UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.user.last_name: Newly mapped `associatedGroups.data.createdBy.lastName` raw log field with event.idm.read_only_udm.entity.relations.entity.user.last_name UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.ip: Newly mapped `associatedIndicators.data.ip` raw log field with event.idm.read_only_udm.entity.relations.entity.ip UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.file.sha1: Newly mapped `associatedIndicators.data.sha1` raw log field with event.idm.read_only_udm.entity.relations.entity.file.sha1 UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.file.sha256: Newly mapped `associatedIndicators.data.sha256` raw log field with event.idm.read_only_udm.entity.relations.entity.file.sha256 UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.file.md5: Newly mapped `associatedIndicators.data.md5` raw log field with event.idm.read_only_udm.entity.relations.entity.file.md5 UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.hostname: Newly mapped `associatedIndicators.data.hostName` raw log field with event.idm.read_only_udm.entity.relations.entity.hostname UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.security_result.confidence_score: Newly mapped `associatedIndicators.data.confidence` raw log field with event.idm.read_only_udm.entity.relations.entity.security_result.confidence_score UDM field.  
\- event.idm.read_only_udm.entity.relations.entity.security_result.description: Newly mapped `attributes.data.value` raw log field with event.idm.read_only_udm.entity.relations.entity.security_result.description UDM field.  
\- event.idm.read_only_udm.entity.metadata.entity_type: Newly mapped `type` raw log field with event.idm.read_only_udm.entity.metadata.entity_type UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
