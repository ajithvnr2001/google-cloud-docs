---
url: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.relations/list/
title: Method: projects.locations.relations.list \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:46.716529+00:00
---

# Method: projects.locations.relations.list  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.relations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Reference ](https://docs.cloud.google.com/migration-center/docs/api)



Send feedback 

#  Method: projects.locations.relations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists all the relations in a given project and location.

### HTTP request

`GET https://migrationcenter.googleapis.com/v1alpha1/{parent=projects/*/locations/*}/relations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for `ListRelationsRequest`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` A token identifying a page of results the server should return.  
`filter` |  `string` Filtering results.  
`orderBy` |  `string` Field to sort by. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing relations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "relations": [
        {
          object ([Relation](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.relations#Relation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`relations[]` |  `object (`[Relation](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.relations#Relation)`)` A list of relations.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
