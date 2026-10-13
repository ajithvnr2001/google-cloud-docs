---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/readFile/
title: Method: projects.locations.repositories.workspaces.readFile \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:22.577821+00:00
---

# Method: projects.locations.repositories.workspaces.readFile  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/readFile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.workspaces.readFile Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Returns the contents of a file (inside a Workspace).

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://dataform.googleapis.com/v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:readFile`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`workspace` |  `string` Required. The workspace's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `workspace`:

  * `dataform.workspaces.readFile`

  
  
### Query parameters

Parameters  
---  
`path` |  `string` Required. The file's full path including filename, relative to the workspace root.  
`revision` |  `string` Optional. The Git revision of the file to return. If left empty, the current contents of `path` will be returned.  
  
### Request body

The request body must be empty.

### Response body

`workspaces.readFile` response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fileContents": string
    }  
  
Fields  
---  
`fileContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The file's contents.A base64-encoded string.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `workspace` resource:

  * `dataform.workspaces.readFile`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-27 UTC."],[],[]] 
