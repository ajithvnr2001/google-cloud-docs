---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume/
title: About volume reversion \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:32.511485+00:00
---

# About volume reversion  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  About volume reversion Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview on snapshot-based volume reversion.

## About volume reversion

Google Cloud NetApp Volumes lets you revert a volume to a previous state using the data captured in a snapshot. Volume reversion restores all the contents of a volume back to the point in time a snapshot was taken. During reversion, any snapshot created after the snapshot you're reverting to is lost. To maintain the data from those snapshots, we recommend that you [create a new volume from a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/new-volume-from-snapshot) or [restore specific data with snapshots](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/restore-specific-data-with-snapshots) instead.

## Common use cases for volume reversion

You can revert a volume to test and upgrade applications or to fend off ransomware attacks. Volume reversion is similar to overwriting the volume with a backup, but only takes a few seconds. You can revert a volume to a snapshot independent of the size of the volume.

### Considerations

Consider the following aspects of volume reversion:

  * Volume reversion takes a few seconds and happens while the volume is online and used by clients.

  * Reverting a volume to a prior state deletes any snapshot data taken after the snapshot you're using for reversion and the operation is irreversible.

  * If a volume has existing backups, you can't revert it to a previous snapshot in the Flex File service level.

**Caution:** Deleting backups is irreversible and can affect your data protection strategy.
    * To revert the existing volume to a snapshot, you must first delete all backups associated with that volume.

    * Alternatively, you can create a new volume from the selected snapshot. You don't need to delete any backups, but the new volume is separate from the original volume.

  * Volumes with replications should revert to the latest replication snapshot to maintain the replication. Reverting to an older snapshot breaks the replication process and requires you to start a new replication if necessary.

  * To avoid potential data corruption, we recommend that you stop applications using the volume before you perform volume reversion.




## What's next

Use the volume reversion instructions to [revert a volume from a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume-instructions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
