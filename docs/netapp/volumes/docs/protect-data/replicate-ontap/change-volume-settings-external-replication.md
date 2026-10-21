---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/change-volume-settings-external-replication/
title: Change volume settings during external replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:35.052126+00:00
---

# Change volume settings during external replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/change-volume-settings-external-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Change volume settings during external replication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to change volume settings during external replication.

NetApp Volumes has access only to the SnapMirror protocol on the ONTAP cluster. While you authorized it to perform SnapMirror transfers only, it doesn't have read access to your ONTAP cluster or ONTAP volume configurations. Therefore, NetApp Volumes can't read the following attributes of the ONTAP volume:

  * Volume size

  * Protocol settings

  * Export policies

  * Share name

  * Other cluster, vserver, or volume specific settings




Make sure you specify the correct settings when creating the NetApp Volumes volume. If you change any settings such as size, export policies, snapshot schedules, or protocol settings, you must reflect the changes manually on the replication partner volume.

## What's next

[FlexGroups and large volumes](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/flexgroups-and-large-volumes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
