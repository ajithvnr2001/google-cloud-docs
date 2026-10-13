---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/
title: Folder \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:14.026339+00:00
---

# Folder  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Folder Stay organized with collections  Save and categorize content based on your preferences. 

The Folder resource represents a [folder](https://docs.cloud.google.com/storage/docs/folders-overview) in a Cloud Storage bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. 

To try out the methods for this resource, see Methods.

## Resource representations
    
    
    {
      "kind": "storage#folder"
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
`kind` | `string` | The kind of item this is. For folders, this is always `storage#folder`. |   
`id` | `string` | The ID of the folder, which is composed of the bucket name and folder name, expressed as a path. For example, `example-bucket/example-folder1/example-folder2/`. |   
`selfLink` | `string` | The canonical URL of the folder. For example, `https://www.googleapis.com/storage/v1/b/example-bucket/folders/example-folder1/example-folder2/`. |   
`name` | `string` | The name of the folder, expressed as a path. For example, `example-folder1/example-folder2/`. |   
`bucket` | `string` | The name of the bucket that contains the folder. |   
`createTime` | `datetime` | The time at which the folder was created, in [RFC 3339 format](https://datatracker.ietf.org/doc/html/rfc3339). |   
`updateTime` | `datetime` | The time at which the folder's metadata was last updated, in [RFC 3339 format](https://datatracker.ietf.org/doc/html/rfc3339). |   
`metageneration` | `long` | The metadata generation of the folder. |   
  
## Methods

[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/delete)
    Delete a folder.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata)
    Get the metadata of a folder.
[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/insert)
    Create a folder.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/list)
    Retrieves a list of folders matching the criteria.
[rename](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/rename)
    Rename a folder.

For information about status and error codes returned by these APIs, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
