---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/list/
title: Method: projects.locations.goldengateConnectionAssignments.list \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:48.721795+00:00
---

# Method: projects.locations.goldengateConnectionAssignments.list  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.goldengateConnectionAssignments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists GoldengateConnectionAssignments in a given project and location.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`GET https://oracledatabase.googleapis.com/v1/{parent=projects/*/locations/*}/goldengateConnectionAssignments`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent value for the GoldengateConnectionAssignments. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of GoldengateConnectionAssignments to return. The service may return fewer than this value. If unspecified, at most 50 GoldengateConnectionAssignments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `goldengateConnectionAssignments.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `goldengateConnectionAssignments.list` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression that filters GoldengateConnectionAssignments listed in the response.  
`orderBy` |  `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "DESC" after a field name for descending.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing GoldengateConnectionAssignments.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "goldengateConnectionAssignments": [
        {
          object ([GoldengateConnectionAssignment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#GoldengateConnectionAssignment))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`goldengateConnectionAssignments[]` |  `object (`[GoldengateConnectionAssignment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments#GoldengateConnectionAssignment)`)` The list of GoldengateConnectionAssignments.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unreachable locations when listing resources across all locations using wildcard location '-'.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `oracledatabase.goldenGateConnectionAssignments.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
