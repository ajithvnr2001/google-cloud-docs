---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-instant-snapshots/
title: Troubleshooting instant snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:41:27.859645+00:00
---

# Troubleshooting instant snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-instant-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting instant snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page shows you how to resolve issues with [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

### Moving a disk that has instant snapshots

The following error might occur when you try to move a disk:
    
    
    Disks with instant snapshots can't be moved. To move this disk, delete the
    instant snapshots of the disk.
    

This error occurs because you still have instant snapshots of the disk.

To resolve this issue, [delete all instant snapshots](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#delete_an_instant_snapshot) of the disk.

## Instant snapshot creation errors

This section describes errors that might occur when you try to create an instant snapshot.

### Exceeding the number of instant snapshots for a single disk

The following error might occur when you create an instant snapshot of a disk:
    
    
    A disk can't have more than 32 instant snapshots. To create an instant snapshot
    of the disk, delete one first.
    

This error occurs because you can't create more than 32 instant snapshots of a single disk.

To resolve the error, [delete any instant snapshots](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#delete_an_instant_snapshot) that you no longer need.

### Exceeding minimum interval between subsequent snapshots

This error occurs when you attempt to create a new instant snapshot of a disk within 30 seconds of creating a instant snapshot:
    
    
    The previous instant snapshot is too recent. To create an instant snapshot,
    wait at least 30 seconds and try again.
    

To resolve this error, create a new instant snapshot at most once every 30 seconds.

## Instant snapshot restoration errors

This section describes errors that might occur when you try to create disks from instant snapshots.

### Restoring disks from a consistency group that contains instant snapshots in multiple locations

The following error might occur when you try to create disks from a consistency group of instant snapshots.

**Error message**
    
    
    All instant snapshots in the instant snapshot group must be in the same scope as the request.
    

This error occurs because the consistency group of instant snapshots contains snapshots of either a mix of zonal and regional disks, or of zonal disks that are in the same region but different zones.

**Resolution**

To resolve this issue and create disks from the group of instant snapshots, you must restore each instant snapshot to a new disk individually.

For instructions on how to restore an instant snapshot to a disk, see [Create a disk from an instant snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-instant-snapshot#create-disk-from-isp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
