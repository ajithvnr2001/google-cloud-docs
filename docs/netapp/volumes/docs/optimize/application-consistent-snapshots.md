---
url: https://docs.cloud.google.com/netapp/volumes/docs/optimize/application-consistent-snapshots/
title: Create application-consistent snapshots \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:54.023941+00:00
---

# Create application-consistent snapshots  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/optimize/application-consistent-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create application-consistent snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about application-consistent snapshots.

## About application-consistent snapshots

Application-consistent snapshots are snapshots taken after the operating system and application write the current state of the data to storage. Application-consistent snapshots provide a clear recovery point for the application; you can use them to create consistent clones of the application.

## Application-consistent snapshots versus crash-consistent snapshots

Crash-consistent snapshots are outdated snapshots of your data due to client caching. Crash-consistent snapshots can help you recover data and work well for a majority of applications. However, some data in storage might be outdated at the time of recovery because it's kept in operating system and application caches for some time before it's written to storage.

## Create an application-consistent snapshot

We recommend that you synchronize snapshot creation with dedicated recovery points of your application. To use NetApp Volumes snapshots to create application-consistent snapshots, complete the following actions:

  1. Flush all unwritten data from the application caches to storage. Many applications, such as databases, provide built-in mechanisms for this procedure. Consult your application documentation for more information.

Alternatively, you can stop the application briefly.

  2. Take a snapshot of the volume. Snapshots take a few seconds to generate.

  3. Return your application to its normal state of operation.




This procedure lets you create consistent snapshots of large application datasets within a few seconds.

## What's next

[Manage your snapshots](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/manage-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
