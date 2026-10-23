---
url: https://docs.cloud.google.com/storage/docs/folders-overview/
title: About folders in buckets with hierarchical namespace enabled \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:30.193705+00:00
---

# About folders in buckets with hierarchical namespace enabled  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/folders-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  About folders in buckets with hierarchical namespace enabled Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about folders in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

## Overview

When you create a bucket with hierarchical namespace enabled, the bucket uses a true file system structure as opposed to a standard flat namespace. Folders exist as a resource in buckets with hierarchical namespace enabled. Using folders, you can organize your objects more effectively and gain access to true directory capabilities, such as atomic folder renames and efficient metadata operations.

Folders in buckets with hierarchical namespace enabled are different from simulated folders and managed folders. Simulated folders exist in flat namespace buckets and managed folders can be applied in both flat namespace buckets and buckets with hierarchical namespace enabled. Managed folders are primarily used to grant IAM permissions to groups of objects. For more information about these other folder types, see [Folder types](https://docs.cloud.google.com/storage/docs/folder-types).

You can manage folders by performing folder operations. To learn how to create, list, and delete folders, as well as get folder metadata, see [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders). To learn how to rename or move a folder, see [Rename a folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders).

## Folder metadata

A folder's metadata contains structured information about the folder. For detailed information about folder metadata, see the [`Folder` resource](https://docs.cloud.google.com/storage/docs/json_api/v1/folders#resource) in the Cloud Storage JSON API reference documentation.

The key components of a folder metadata are as follows:

  * `bucket`: The name of the bucket where the folder resides. For example, `my-bucket`.
  * `id`: A unique identifier for the folder within the bucket. For example, `hns-bucket/dir1/`.
  * `kind`: The resource type. For a folder, this value is always `storage#folder`.
  * `name`: The name of the folder. For example, `dir1/`.
  * `selfLink`: A URL that references the folder in the Cloud Storage API.
  * `timeCreated`: The timestamp when the folder was created. For example, `2023-05-05T16:32:08.878000+00:00`.
  * `updated`: The timestamp when the folder was last updated. For example, `2024-05-06T16:32:08.878000+00:00`.



## Folder operations

This section describes the operations you can perform on folders. Some operations initiate a [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) that you can monitor to keep track of the operation's progress and status.

### Create a folder

You can explicitly create folders by using the folder creation operation. Additionally, when you create an object and specify a non-existent folder in its path, the missing parent folder is automatically created for you. For example, creating an object named `dir1/foo.txt` automatically creates the folder `dir1/` if it doesn't already exist.

For information about folder naming, see Considerations.

### List folders

You can retrieve a list of folders in your bucket by using the list folders operation. Because folders are distinct resources in buckets with hierarchical namespace enabled, this operation evaluates the true folder structure instead of simulating folders from object paths.

When listing folders, you can filter the results using parameters such as `prefix`, `delimiter`, `lexicographicStart`, and `lexicographicEnd`. For example, setting the delimiter parameter to `/` lets you list folders in a directory-like mode, returning only the folders that match the prefix or exist one level below it.

The list folders operation returns paginated results. A single response page can contain a maximum of 1000 folders.

### Get the metadata of a folder

You can retrieve the properties of a folder by using the get folder metadata operation. This operation retrieves information about the folder resource itself, rather than the objects it contains.

This operation returns a folder's metadata, which provides structured information such as its creation timestamp, its unique identifier, and the bucket where it resides. For a detailed list of the properties returned by this operation, see Folder metadata.

### Rename or move a folder

Renaming a folder and moving a folder use the same underlying operation. The operation is an atomic, metadata-only change that updates the folder's path without physically copying or deleting the underlying objects. Renaming a folder also updates the folder's path for resources within the folder, such as child folders, objects, and managed folders. This makes the operation fast and avoids object copy costs.

The folder rename operation initiates a long-running operation.

During a folder rename operation, you can read and list the folders being renamed, but you can't run write operations on them.

In the JSON API and Google Cloud CLI, the renaming and moving operations use the same URL endpoint or command. In the Google Cloud console, **Rename folder** and **Move folder** are presented as two distinct options, but both options execute the same backend operation.

### Delete a folder

You can permanently delete a folder by using the delete folder operation. While folders can be created automatically during object operations, they are not automatically removed when they become empty. You must delete them explicitly.

## Interactions between folders and associated managed folders

[Associated managed folders](https://docs.cloud.google.com/storage/docs/hns-overview#managed-folder-operations) are used to control access for folders in buckets with hierarchical namespace enabled. Folders and associated managed folders interact in the following ways:

  * **Folder creation** : When you create a managed folder in a bucket with hierarchical namespace enabled, any missing folders in its path are created automatically, including parent folders and the actual target folder (also known as the **associated folder**).

For example, say you create a bucket with hierarchical namespace enabled called `my-bucket`. If you create a managed folder called `2025/training-data/` in the bucket, Cloud Storage automatically creates the parent folder `2025/` and the target associated folder `training-data/` in the bucket.

  * **Folder deletion** : When you delete a folder that has an associated managed folder, Cloud Storage deletes the associated managed folder as well. This is because when you delete a folder, you're deleting the path entirely. Because the path no longer exists, the associated managed folder and any IAM policies attached to it are deleted. In buckets with hierarchical namespace enabled, a managed folder can't exist without an associated folder.

If you don't have the required permissions to delete the folder's associated managed folder, the folder delete operation fails. To find the required permissions for deleting managed folders, see [Get required roles for managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#get-required-roles).

  * **Folder renaming** : When you rename a folder that has an associated managed folder, Cloud Storage renames the associated managed folder as well.




For information about naming requirements for folders that have an associated managed folder, see [Naming for folders](https://docs.cloud.google.com/storage/docs/hns-overview#naming).

## Considerations

When creating folders, consider the following:

  * **Object and folder names** : Buckets with hierarchical namespace enabled, support all valid [object names](https://docs.cloud.google.com/storage/docs/objects#naming), including those with leading, trailing slashes (`/`) or consecutive slashes. Each forward slash (`/`) in an object name represents a folder. The following table shows examples of the relationship between object names and their corresponding location in the folder hierarchy:

Object name | Location in the folder hierarchy  
---|---  
`foo.txt` | Every bucket includes a root folder. Object `foo.txt` resides under the root folder of the bucket.  
`dir1/foo.txt` | Object `foo.txt` resides within a top-level folder named `dir1/`. The top-level folder is distinct from the root folder.  
`dir1/` | The trailing slash in object names like `dir1/` indicates that the object resides within the folder. In this example, the object name `dir1/` is the same as the parent folder name `dir1/`.   
`dir1//foo.txt` | Object `foo.txt` resides in a second-level folder named `dir1//`, a child folder of `dir1/`.   
  * **Maximum folder depth** : Buckets with hierarchical namespace enabled support a maximum folder depth of 50. Folders can be created with up to 50 stacked child folders (for example, `folder1/folder2/folder3/.../folder50/my-data.txt`). However, if a folder has an associated managed folder, it can only have up to 15 stacked child folders.

  * **Maximum folder name size** : 512 bytes (UTF-8 encoded).

  * **Sensitive or personally identifiable information (PII)** : Folder names are more broadly visible than folder metadata. For example, folder names appear in URLs and when listing folders or objects in a bucket. Don't include sensitive information or PII in folder names.




## What's next

  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Rename a folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders).
  * [Optimize folder management](https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices#folder-management).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
