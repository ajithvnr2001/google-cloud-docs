---
url: https://docs.cloud.google.com/dataproc-metastore/docs/release-channel/
title: Release channels \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:37.822724+00:00
---

# Release channels  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/release-channel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Release channels Stay organized with collections  Save and categorize content based on your preferences. 

Dataproc Metastore uses release channels to bundle features of varying levels of stability. Release channels allow you to select between stable features and newer experimental features. You can select the release channel when you create a Dataproc Metastore service.

## Types of release channels

There are two types of release channels:

  * **Canary** : The `Canary` release channel contains the newest features, which may be unstable and subject to unresolved issues with no known workarounds. Services using `Canary` are not subject to any SLAs.

  * **Stable** : The `Stable` release channel contains features that are considered stable and have been validated for production use.




If you don't specify a channel, new Dataproc Metastore services are created with the `Stable` value. If you select the `Canary` release channel, then you automatically receive the newer features.

## Release notes

To learn what's new in a release channel, review the following release notes:

Release Channel | Notes  
---|---  
`Canary` | Contains the feature to [run the asynchronous background tasks like ACID compaction](https://docs.cloud.google.com/dataproc-metastore/docs/transactional-tables) separately from the Hive metastore. This frees up resources to run more Hive metastore tasks. This preview feature is only available for Hive version 3.1.2 `Enterprise` tier.  
  
## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Release notes](https://docs.cloud.google.com/dataproc-metastore/docs/release-notes)
  * [Version policy](https://docs.cloud.google.com/dataproc-metastore/docs/version-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
