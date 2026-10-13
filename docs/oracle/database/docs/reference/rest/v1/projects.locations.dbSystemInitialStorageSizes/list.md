---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes/list/
title: Method: projects.locations.dbSystemInitialStorageSizes.list \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:43.109423+00:00
---

# Method: projects.locations.dbSystemInitialStorageSizes.list  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.dbSystemInitialStorageSizes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists all the DbSystemInitialStorageSizes for the given project and location.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`GET https://oracledatabase.googleapis.com/v1/{parent=projects/*/locations/*}/dbSystemInitialStorageSizes`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent value for the DbSystemInitialStorageSize resource with the format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, a maximum of 50 DbSystemInitialStorageSizes will be returned. The maximum value is 1000; values above 1000 will be reset to 1000.  
`pageToken` |  `string` Optional. A token identifying the requested page of results to return. All fields except the filter should remain the same as in the request that provided this page token.  
  
### Request body

The request body must be empty.

### Response body

The response for `DbSystemInitialStorageSizes.List`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dbSystemInitialStorageSizes": [
        {
          object ([DbSystemInitialStorageSize](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#DbSystemInitialStorageSize))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dbSystemInitialStorageSizes[]` |  `object (`[DbSystemInitialStorageSize](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#DbSystemInitialStorageSize)`)` The list of DbSystemInitialStorageSizes.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `oracledatabase.dbSystemInitialStorageSizes.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
