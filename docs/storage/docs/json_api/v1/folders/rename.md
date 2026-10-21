---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/rename/
title: Folder: rename \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:25.644249+00:00
---

# Folder: rename  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/rename/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Folder: rename Stay organized with collections  Save and categorize content based on your preferences. 

Renames a folder within a bucket with hierarchical namespace enabled. For details about how the rename operation works, see [ Rename folders](https://docs.cloud.google.com/storage/docs/rename-hns-folders). 

## Required permissions

The authenticated user must have the following IAM permissions to use this method: 

  * `storage.folders.rename`
    * This permission is needed to rename the source folder.
  * `storage.folders.create`
    * This permission is needed to create the destination folder.



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/folders/sourcePath/renameTo/folders/destinationPath

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the folder.   
`sourcePath` | `string` |  The URL-encoded name of the source folder, expressed as a path. For example, `src-folder/`, URL-encoded as `src-folder%2F`.   
`destinationPath` | `string` |  The URL-encoded name of the destination folder, expressed as a path. For example, `dest-folder/`, URL-encoded as `dest-folder%2F`.   
**Optional query parameters**  
`ifMetagenerationMatch` | `long` |  If set, only rename the folder if the source folder's metageneration matches this value.   
`ifMetagenerationNotMatch` | `long` |  If set, only rename the folder if the source folder's metageneration doesn't match this value.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an instance of the [long-running operation](https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto) in the response body:
    
    
    {
      "name": "string",
      "metadata": {object},
      "done": boolean,
      // Result can include either an error or response:
      "error": {object (Status)},
      "response": {object (Folder)}
    }

Property name | Value | Description  
---|---|---  
`name` | `string` | The server-assigned name of the operation.  
`metadata` | `object` | An object of type `google.storage.control.v2.RenameFolderMetadata`:
    
    
      {
        "sourceFolderId": "string",
        "destinationFolderId": "string",
        "commonMetadata":
          {
            "createTime": "datetime",
            "endTime": "datetime",
            "updateTime": "datetime",
            "type": "string",
            "requestedCancellation": boolean,
            "progressPercent": integer,
          }
      }

Where: 

  * `sourceFolderId` is the path of the folder you want to rename.
  * `destinationFolderId` is the new name you want to give the folder.
  * `createTime` is the time when the operation started.
  * `endTime` is the time when the operation finished, regardless of whether it succeeded or failed.
  * `updateTime` is the time when the metadata was last updated.
  * `type` is the operation type. For rename folder operations, this is always `rename-folder`.
  * `requestedCancellation` identifies whether the user has requested cancellation of the operation. **Caution:** The rename folder operation cannot be canceled once initiated. Even if you attempt to cancel, the rename folder operation continues until completion.
  * `progressPercent` indicates the operation's progress as a percentage, ranging from 0 (not started) to 100 (completed). The value -1 means the progress is unknown. 

  
`done` | `boolean` | If `false`, indicates that the operation is still in progress, and neither `error` nor `response` is set. If `true`, it indicates that the operation is completed and either `error` or `response` is set.  
`error` | `object` | If the operation fails, this field is returned in the response body and contains the error details. The rename operation fails if any of the child folders exceed either the maximum folder name length limit or maximum folder depth limit. For information about folder name length and folder depth limits, see [Considerations](https://docs.cloud.google.com/storage/docs/folders-overview#considerations).  
If a failure occurs, the folders are reverted to their original state prior to the rename attempt. For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).  
`response` | `object` | If the operation succeeds, an object of type `google.storage.control.v2.Folder` is returned. 
    
    
    {
      "name": "string",
      "metageneration": integer,
      "createTime": "datetime"",
      "updateTime": "datetime",
    }

Where: 

  * `name` is the name of the folder resource.
  * `metageneration` is the metageneration of the folder.
  * `createTime` is the time when the folder was created.
  * `updateTime` is the time when the folder was last updated.

  
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
