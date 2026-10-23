---
url: https://docs.cloud.google.com/storage/docs/managed-folders/
title: Managed folders \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:57.315835+00:00
---

# Managed folders  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/managed-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Managed folders Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of managed folders in Cloud Storage. Managed folders are a type of folder on which you can grant IAM roles, so you have more fine-grained access control over specific groups of objects within a bucket. Managed folders exist as resources within Cloud Storage and are different from [simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders), which operate with a flat namespace.

## IAM for managed folders

When you apply an IAM policy on a managed folder, the access granted in the policy applies to any object within the bucket that uses the managed folder path as a prefix in the object name. For example, if you grant a principal the Storage Object Viewer (`roles/storage.objectViewer`) role on a managed folder named `example-managed-folder/`, the principal can view any object within the `example-managed-folder` path, such as `example-managed-folder/dog.png` or `example-managed-folder/cat.jpeg`. When you nest managed folders, the permissions granted through IAM policies are applied additively.

IAM deny policies can't be set on buckets or managed folders. Instead, they can only be set on project, folder, and organization resources. Additionally, managed folders cannot be specified as a resource in IAM deny policy conditions. Denial conditions only recognize resource tag functions, and tags can't be attached to managed folders.

Managed folders can only be created in buckets that have uniform bucket-level access enabled.

Read the following pages for more information about managed folders:

  * [Creating and managing managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders)

  * [Control access to managed folders](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders)

  * [ManagedFolder reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder) for the JSON API




## Managed folder names

The name you give to a managed folder must meet the following requirements:

  * Managed folder names can contain any sequence of valid Unicode characters, of length 1-1024 bytes when UTF-8 encoded.

  * Managed folder names cannot contain [Carriage Return or Line Feed characters](https://en.wikipedia.org/wiki/Newline#Unicode).

  * Managed folder names must end with `/`. At most, a managed folder name can have 15 `/`s. In other words, managed folders can be nested up to 15 levels deep.

  * Managed folder names cannot start with `.well-known/acme-challenge/`.

  * Managed folders cannot be named `.` or `..`.




It is strongly recommended that you avoid the following in your managed folder names:

  * [Control characters](http://www.w3.org/TR/xml/#charsets) that are illegal in XML 1.0 (#x7F–#x84 and #x86–#x9F): these characters cause XML listing issues when you try to list your managed folders.

  * The `[`, `]`, `*`, or `?` characters: the Google Cloud CLI interprets these characters as wildcards, so including them in managed folder names can make it difficult or impossible to perform [wildcard operations](https://docs.cloud.google.com/storage/docs/wildcards) with the tool. Additionally, `*` and `?` are not valid characters for file names in Windows.

  * Sensitive or personally identifiable information (PII): managed folder names are more broadly visible than object data. For example, managed folder names appear in URLs for the object and when listing objects in a bucket.




## Considerations

When working with managed folders, note the following considerations:

  * Managed folders can be created in place of [simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders), which means that you can create a managed folder and name it after an object's prefix, as long as there isn't already a managed folder using that name. For example, you can create a managed folder named `my-folder/`, even if you have an existing object named `my-folder/object.txt`. Note that the IAM policy on the managed folder `my-folder/` will then apply to all objects that has `my-folder/` as a name prefix.

  * You can create child managed folders before the parent managed folder is created. For example, you can create a managed folder named `my-folder-A/my-folder-B/` without first creating a managed folder named `my-folder-A/`.

  * By default, you can't delete a non-empty managed folder that contains objects or other child managed folders. You can bypass this rule when using the `allowNonEmpty` parameter in a [`Delete` ManagedFolder JSON API request](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/delete).

  * Managed folder names are visible in error messages and Cloud Audit Logs when a request to delete a [folder](https://docs.cloud.google.com/storage/docs/folders-overview) that has a managed folder at the same path fails, even without explicit `storage.managedFolders.get` or `storage.managedFolders.list` permissions.




## What's next

  * [Create and manage managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders).

  * Learn about [simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders).

  * [Upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to a Cloud Storage bucket.

  * Learn about the [best practices for using managed folders](https://docs.cloud.google.com/storage/docs/access-control#best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
