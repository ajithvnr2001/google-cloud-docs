---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs
title: REST Resource: projects.locations.featureOnlineStores.featureViews.featureViewSyncs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:06:36.088183+00:00
---

# REST Resource: projects.locations.featureOnlineStores.featureViews.featureViewSyncs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.featureOnlineStores.featureViews.featureViewSyncs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: FeatureViewSync

FeatureViewSync is a representation of sync operation which copies data from data source to feature View in Online Store.

Fields  
  
`name` `string` Identifier. name of the FeatureViewSync. Format: `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}/featureViewSyncs/{featureViewSync}` | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when this FeatureViewSync is created. Creation of a FeatureViewSync means that the job is pending / waiting for sufficient resources but may not have started the actual data transfer yet.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `runTime` `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval)`)` Output only. time when this FeatureViewSync is finished. | `finalStatus` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Final status of the FeatureViewSync. | `syncSummary` `object (`[SyncSummary](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs#SyncSummary)`)` Output only. Summary of the sync job. | `satisfiesPzs` `boolean` Output only. reserved for future use. | `satisfiesPzi` `boolean` Output only. reserved for future use. | JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "runTime": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval))
      },
      "finalStatus": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "syncSummary": {
        object ([SyncSummary](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs#SyncSummary))
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
## SyncSummary

Summary from the Sync job. For continuous syncs, the summary is updated periodically. For batch syncs, it gets updated on completion of the sync.

Fields  
  
`rowSynced` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total number of rows synced. | `totalSlot` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. BigQuery slot milliseconds consumed for the sync job. | `systemWatermarkTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Lower bound of the system time watermark for the sync job. This is only set for continuously syncing feature views.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "rowSynced": string,
      "totalSlot": string,
      "systemWatermarkTime": string
    }  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/get)`

|  Gets details of a single FeatureViewSync.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list)`

|  Lists FeatureViewSyncs in a given FeatureView.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
