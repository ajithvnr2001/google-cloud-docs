---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/
title: ManagedFolder \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:23.922529+00:00
---

# ManagedFolder  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ManagedFolder Stay organized with collections  Save and categorize content based on your preferences. 

The ManagedFolder resource represents a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) in Cloud Storage. You can apply IAM policies on a managed folder to control access to the resources within the managed folder. 

To try out the methods for this resource, see Methods.

## Resource representations
    
    
    {
      "kind": "storage#managedFolder"
      "id": string,
      "selfLink": string,
      "name": string,
      "bucket": string,
      "createTime": datetime,
      "updateTime": datetime,
      "metageneration": long
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For managed folders, this is always "`storage#managedFolder`". |   
`id` | `string` | The ID of the managed folder, which is composed of the bucket name and managed folder name, expressed as a path. For example, `example-bucket/example-dir/example-dir2/`. |   
`selfLink` | `string` | The canonical URL of the managed folder. For example, `https://www.googleapis.com/storage/v1/b/example-bucket/managedFolders/example-dir/example-dir2/`. |   
`name` | `string` | The name of the managed folder, expressed as a path. For example, `example_dir/example_dir2/`. |   
`bucket` | `string` | The name of the bucket that contains the managed folder. |   
`createTime` | `datetime` | The time at which the managed folder was created, in [RFC 3339 format](https://datatracker.ietf.org/doc/html/rfc3339). |   
`updateTime` | `datetime` | The time at which the managed folder's metadata or IAM policy was last updated, in [RFC 3339 format](https://datatracker.ietf.org/doc/html/rfc3339). |   
`metageneration` | `long`1 | The metadata generation of the managed folder. |   
  
## Methods

[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/insert)
    Create a managed folder.
[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/delete)
    Permanently delete a managed folder.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/get)
    View a managed folder.
[getIamPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/getIamPolicy)
    View the IAM policy for a managed folder.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/list)
    Retrieves a list of managed folders under a given bucket.
[setIamPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy)
    Update the IAM policy for a managed folder.
[testIamPermissions](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/testIamPermissions)
    Tests a set of permissions on a managed folder to see which, if any, are held by the caller.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
