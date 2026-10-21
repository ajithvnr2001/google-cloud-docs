---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zero-networks-changelog/
title: Change log for ZERO_NETWORKS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:23:00.819062+00:00
---

# Change log for ZERO_NETWORKS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zero-networks-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZERO_NETWORKS

Date | Changes  
---|---  
2025-03-13 |  \- Mapped `rule.approvedAt` to `additional.fields`.  
\- Mapped `rule.createdAt` to `additional.fields`.  
\- Mapped `rule.created_by.id` to `target.user.userid` and set event_type to `USER_UNCATEGORIZED`.  
\- Mapped `rule.created_by.name` to `target.user.user_display_name` and set event_type to `USER_UNCATEGORIZED`.  
\- Mapped `rule.description` to `metadata.description`.  
\- Mapped `rule.expiration` to `additional.fields`.  
\- Mapped `rule.ipSecOpt` to `additional.fields`.  
\- Mapped `rule.isOccasionalMfa` to `additional.fields`.  
\- Mapped `rule.localEntityNames.id` to `additional.fields`.  
\- Mapped `rule.localEntityNames.name` to `additional.fields`.  
\- Mapped `rule.parent_switch_rule_id` to `additional.fields`.  
\- Mapped `rule.parent_switch_rule_type` to `additional.fields`.  
\- Mapped `rule.ruleClass` to `additional.fields`.  
\- Mapped `rule.state` to `additional.fields`.  
\- Mapped `rule.updatedAt` to `additional.fields`.  
\- Mapped `learningDuration` to `additional.fields`.  
\- Mapped `protectionDate` to `additional.fields`.  
\- Mapped `parentObjectId` to `additional.fields`.  
\- Mapped `reportedObjectId` to `additional.fields`.  
\- Mapped `reportedObjectGeneration` to `additional.fields`.  
\- Mapped `isoTimestamp` to `metadata.event_timestamp`.  
\- Mapped `auditType` to `metadata.product_event_type`.  
\- Mapped `enforcementSource` to `principal.application`.  
\- Mapped `userRole` to `target.user.role_name`.  
\- Mapped `destinationEntitiesList` to `additional.fields`.  
\- Mapped `rule.action` to `security_result.action_details`.  
\- Mapped `performedBy.id` to `target.user.userid` and set event_type to `USER_UNCATEGORIZED` if `rule.created_by.id` is not present.  
\- Mapped `performedBy.name` to `target.user.user_display_name` and set event_type to `USER_UNCATEGORIZED` if `rule.created_by.name` is not present.  
\- Mapped `connectServer` to `additional.fields`.  
\- Mapped `connectedSince` to `additional.fields`.  
\- Mapped `expiresAt` to `additional.fields`.  
\- Mapped `externalIP` to `target.ip`.  
\- Mapped `idp` to `additional.fields`.  
\- Mapped `sourceAsset` to `additional.fields`.  
\- Mapped `uacId` to `additional.fields`.  
\- Mapped `uacName` to `additional.fields`.  
\- Mapped `user` to `target.user.user_display_name` and set event_type to `USER_UNCATEGORIZED`.  
\- Mapped `prevInactiveReason` to `additional.fields`.  
\- Mapped `currInactiveReason` to `additional.fields`.  
\- Mapped `lastActiveDurationInMonths` to `additional.fields`.  
\- Mapped `lastActiveTime` to `additional.fields`.  
\- Mapped `security_result` to `security_result`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
