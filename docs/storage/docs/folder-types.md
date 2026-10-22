---
url: https://docs.cloud.google.com/storage/docs/folder-types/
title: Folder types in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:05.471074+00:00
---

# Folder types in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/folder-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Folder types in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage buckets have either a flat namespace or a true file system structure. In buckets with a flat namespace, [objects are stored as a flat list](https://docs.cloud.google.com/storage/docs/objects#flat-namespace). In buckets with a file system structure, objects are indexed by actual directories.

Cloud Storage offers different folder types for flat namespace buckets and file system structured buckets. These folders have different interfaces, characteristics, and semantics. This page describes the three types of folders available in Cloud Storage.

## Simulated folders

[Simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders) provide a simulated directory structure in flat namespace buckets. Simulated folders don't exist as actual resources in Cloud Storage. Instead, these folders are merely simulated by object name prefixes, delimited by a forward slash `/` in the object's name. Simulated folders create a visual hierarchy of your objects in the Google Cloud console and the Google Cloud CLI.

## Folders in buckets with hierarchical namespace enabled

In buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled, you can create real folders that exist as actual resources within Cloud Storage. These folders can contain objects or child folders, and they can be managed by operations such as renaming or listing. The hierarchical structure and folder management operations improve performance, consistency, navigation, and management for file-oriented and data-intensive workloads.

For more information about folders, see [About folders in buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/folders-overview).

## Managed folders

[Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) let you apply Identity and Access Management (IAM) roles to groups of objects at once, providing more granular security and control over your data. Managed folders are an actual resource within Cloud Storage.

You can use managed folders in flat namespace buckets or buckets with hierarchical namespace enabled. In buckets with hierarchical namespace enabled, a managed folder acts as a specialized access control layer that must be explicitly created with the same name as the corresponding folder to apply IAM permissions. For more detail, see [Access control for folders](https://docs.cloud.google.com/storage/docs/hns-overview#managed-folder-operations).

To get started using managed folders, see [Create managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders).

## What's next

  * Learn how to [create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
