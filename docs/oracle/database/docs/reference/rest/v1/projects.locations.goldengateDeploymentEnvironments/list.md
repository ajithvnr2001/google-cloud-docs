---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments/list/
title: Method: projects.locations.goldengateDeploymentEnvironments.list \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:50.107282+00:00
---

# Method: projects.locations.goldengateDeploymentEnvironments.list  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.goldengateDeploymentEnvironments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists GoldengateDeploymentEnvironments in a given project and location.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`GET https://oracledatabase.googleapis.com/v1/{parent=projects/*/locations/*}/goldengateDeploymentEnvironments`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of GoldengateDeploymentEnvironments. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, at most 50 deployment environments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing GoldengateDeploymentEnvironments

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "goldengateDeploymentEnvironments": [
        {
          object ([GoldengateDeploymentEnvironment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#GoldengateDeploymentEnvironment))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`goldengateDeploymentEnvironments[]` |  `object (`[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments#GoldengateDeploymentEnvironment)`)` The list of GoldengateDeploymentEnvironment  
`nextPageToken` |  `string` A token identifying a page of results the server should return. If this field is empty, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `oracledatabase.goldenGateDeploymentEnvironments.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
