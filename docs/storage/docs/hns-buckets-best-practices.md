---
url: https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices/
title: Optimize performance in buckets with hierarchical namespace enabled \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:16.261261+00:00
---

# Optimize performance in buckets with hierarchical namespace enabled  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Optimize performance in buckets with hierarchical namespace enabled Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on how you can optimize performance in buckets with hierarchical namespace enabled.

## Listing objects

The following are the performance considerations for listing objects:

  * In buckets with hierarchical namespace enabled, listing all objects for the entire bucket or with a prefix is resource-intensive as the operation must traverse each folder and subfolder, similar to the `ls -r` command in a file system. Consequently, if there are more folders in your bucket, the slower the object listing happens. A large number of empty folders can also negatively impact object listing performance. To avoid negatively impacting performance, we recommend that you maximize the number of objects in each folder and regularly delete empty folders.
  * Listing or retrieving objects and sub folders within a specific folder using a delimiter and a specific prefix is more efficient in buckets with hierarchical namespace enabled as the objects are organized within a folder structure. To optimize listing performance when using a delimiter and a specific prefix, set the `includeFoldersAsPrefixes` parameter. Otherwise, Cloud Storage performs additional checks to exclude empty folders, which can slow down the operation. For more information about using the `includeFoldersAsPrefixes` when listing objects, see [Listing objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list).



## Folder management

For efficient folder management, we recommend the following:

  * **Pre-create folder structure:** Instead of relying on automatic folder creation during object upload, rewrite, and compose operations, use the create folder operation to obtain your intended folder structure in advance. Pre-creating the folder structure improves the performance consistency and predictability.
  * **Maximize objects per folder ratio:** Aim for a high objects-to-folder ratio as it reduces the overhead associated with folder creation and management.
  * **Regularly delete empty folders:** Empty folders can accumulate, especially when using Object Lifecycle Management or deleting objects without explicitly deleting their parent folders. The accumulated folders can impact the performance of object listing operation and other folder related operations. The following are some of the methods that you can use to delete empty folders: 
    * When you use [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) or [Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) to interact with a bucket enabled with hierarchical namespace, deleting a directory deletes the corresponding folder in your bucket.
    * You can use a recursive delete to delete folders automatically when using the Google Cloud console or Google Cloud CLI.
    * You can use the [`delete_empty_folders.py`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/storagecontrol/hierarchical-namespace/delete_empty_folders.py) script to periodically delete empty folders using parallel processing. The script provides an option to target a specific folder path prefix, which allows the script to perform folder deletions on a subset of the bucket's directory structure. Additionally, the script deletes all empty folders (created implicitly or explicitly) including managed folders and their associated IAM policies. For details about how to use the script, see the [README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/storagecontrol/hierarchical-namespace/README.md).



## What's next

  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Rename a folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders).
  * [Listing objects](https://docs.cloud.google.com/storage/docs/listing-objects).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
