---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/change-volume-settings-volume-migration/
title: Change volume settings during volume migration \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:22.947783+00:00
---

# Change volume settings during volume migration  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/change-volume-settings-volume-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Change volume settings during volume migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to change volume settings during volume migration.

NetApp Volumes has access only to the SnapMirror protocol on your source cluster. While you authorized it to replicate the source volume content, it doesn't have read access to your source cluster or source volume configurations. Therefore, it can't read the following attributes of the source volume:

  * Volume size

  * Protocol settings

  * Export policies

  * Share name

  * Other cluster, vserver, or volume specific settings




Make sure you specify the correct settings when creating the destination volume. If source volume settings such as size, export policies, snapshot schedules, or protocol settings change, you must reflect the changes manually on the destination volume.

## What's next

[FlexGroups and large volumes](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/flexgroups-and-large-volumes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
