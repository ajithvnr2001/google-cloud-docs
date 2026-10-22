---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cohesity-changelog/
title: Change log for COHESITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:54.519089+00:00
---

# Change log for COHESITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cohesity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for COHESITY

Date | Changes  
---|---  
2024-09-24 |  Enhancement:  
\- Removed `gsub` to format JSON logs.   
2024-09-10 |  Enhancement:  
\- Added `gsub` to remove unwanted character from log.  
\- Mapped `prin_ip` to `principal.ip`.   
2024-07-28 |  Enhancement:  
\- Mapped `EntityId` and `RegisteredSource.EntityId` to `principal.user.userid`.  
\- Mapped `Description` and `EventMessage` to `metadata.description`.  
\- Mapped `IP` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `User` to `principal.user.user_display_name`.  
\- Mapped `Action, `Domain, `ServiceContext, `AttributeMap.AttemptNum, `cluster_id, `cluster_name, `ClusterInfo.ClusterId, `ClusterInfo.ClusterName, `TaskId, `EntityName, `EntityType, `BackupJobId, `BackupJobName, `EnvironmentType, `RegisteredSource.EntityName, `RegisteredSource.EntityType, `AttributeMap.BridgeConstituent, `ReplicationTarget.ClusterName, and `ReplicationTarget.ClusterId to `additional.fields".   
2024-05-16 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
