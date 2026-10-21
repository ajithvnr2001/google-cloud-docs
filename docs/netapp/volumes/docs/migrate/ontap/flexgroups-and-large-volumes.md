---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/flexgroups-and-large-volumes/
title: FlexGroups and large volumes \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:41.465165+00:00
---

# FlexGroups and large volumes  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/flexgroups-and-large-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  FlexGroups and large volumes Stay organized with collections  Save and categorize content based on your preferences. 

Both volume migration and external replication support ONTAP [FlexGroups](https://docs.netapp.com/us-en/ontap/flexgroup/definition-concept.html) as source volumes.

A FlexGroups volume is a large volume internally built out of multiple FlexVols, known as member volumes or constituents. NetApp Volumes uses FlexGroups internally to provide its [large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes) or large volume feature.

When replicating a FlexGroup volume to NetApp Volumes, the destination volume must also be a large volume. For the Flex Unified, you can only create large volumes on large capacity storage pools. The number of constituents on the destination large volume must match with the number of constituents on the source FlexGroup. As external replication can't read this number from the source volume, you must specify it during replication creation using the `large-volume-constituent-count` parameter within the `hybrid-replication-parameters` parameter block.

The `large-volume-constituent-count` you provide must meet the following criteria:

  * It must be between 2 and 36.

  * No odd numbers are allowed, with the exceptions of 3 and 5.




If your source FlexGroup's constituent count doesn't meet these requirements, you must change the source FlexGroup constituent count to a correct value before establishing an external replication. Once the replication is enabled, you can't change the constituent count on NetApp Volumes. Therefore, don't add constituents to an ONTAP FlexGroup that is already in replication with NetApp Volumes.

External replications between FlexGroups and large volumes don't support the `EVERY_10_MINUTES` replication schedule. However, volume migration uses a fixed `HOURLY` replication schedule.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
