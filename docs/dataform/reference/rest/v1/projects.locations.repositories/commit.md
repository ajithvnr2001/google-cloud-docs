---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit/
title: Method: projects.locations.repositories.commit \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:02.672975+00:00
---

# Method: projects.locations.repositories.commit  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.commit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CommitMetadata
    * JSON representation
  * FileOperation
    * JSON representation
  * WriteFile
    * JSON representation
  * DeleteFile
  * Try it!



Applies a Git commit to a Repository. The Repository must not have a value for `gitRemoteSettings.url`.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`POST https://dataform.googleapis.com/v1/{name=projects/*/locations/*/repositories/*}:commit`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The repository's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dataform.repositories.commit`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commitMetadata": {
        object ([CommitMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#CommitMetadata))
      },
      "requiredHeadCommitSha": string,
      "fileOperations": {
        string: {
          object ([FileOperation](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#FileOperation))
        },
        ...
      }
    }  
  
Fields  
---  
`commitMetadata` |  `object (`[CommitMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#CommitMetadata)`)` Required. The changes to commit to the repository.  
`requiredHeadCommitSha` |  `string` Optional. The commit SHA which must be the repository's current HEAD before applying this commit; otherwise this request will fail. If unset, no validation on the current HEAD commit SHA is performed.  
`fileOperations` |  `map (key: string, value: object (`[FileOperation](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#FileOperation)`))` Optional. A map to the path of the file to the operation. The path is the full file path including filename, from repository root.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Response body

`repositories.commit` response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commitSha": string
    }  
  
Fields  
---  
`commitSha` |  `string` The commit SHA of the current commit.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataform.repositories.commit`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CommitMetadata

Represents a Dataform Git commit.

JSON representation  
---  
      
    
    {
      "author": {
        object ([CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1/CommitAuthor))
      },
      "commitMessage": string
    }  
  
Fields  
---  
`author` |  `object (`[CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1/CommitAuthor)`)` Required. The commit's author.  
`commitMessage` |  `string` Optional. The commit's message.  
  
## FileOperation

Represents a single file operation to the repository.

JSON representation  
---  
      
    
    {
    
      // Union field operation can be only one of the following:
      "writeFile": {
        object ([WriteFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#WriteFile))
      },
      "deleteFile": {
        object ([DeleteFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#DeleteFile))
      }
      // End of list of possible types for union field operation.
    }  
  
Fields  
---  
Union field `operation`. The operation to perform on the file. `operation` can be only one of the following:  
`writeFile` |  `object (`[WriteFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#WriteFile)`)` Represents the write operation.  
`deleteFile` |  `object (`[DeleteFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit#DeleteFile)`)` Represents the delete operation.  
  
## WriteFile

Represents the write file operation (for files added or modified).

JSON representation  
---  
      
    
    {
      "contents": string
    }  
  
Fields  
---  
`contents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The file's contents.A base64-encoded string.  
  
## DeleteFile

This type has no fields.

Represents the delete file operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-27 UTC."],[],[]] 
