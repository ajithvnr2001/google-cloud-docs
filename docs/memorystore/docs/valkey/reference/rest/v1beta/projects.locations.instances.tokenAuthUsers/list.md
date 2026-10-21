---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/list/
title: Method: projects.locations.instances.tokenAuthUsers.list \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:44.594715+00:00
---

# Method: projects.locations.instances.tokenAuthUsers.list  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  Method: projects.locations.instances.tokenAuthUsers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists all the token auth users for a token based auth enabled instance.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west15europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://memorystore.googleapis.com/v1beta/{parent=projects/*/locations/*/instances/*}/tokenAuthUsers`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent to list token auth users from. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. The maximum value is 1000; values above 1000 will be coerced to 1000. If not specified, a default value of 1000 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's `nextPageToken` to determine if there are more token auth users left to be queried.  
`pageToken` |  `string` Optional. The `nextPageToken` value returned from a previous `tokenAuthUsers.list` request, if any.  
`filter` |  `string` Optional. Expression for filtering results.  
`orderBy` |  `string` Optional. Sort results by a defined order.  
  
### Request body

The request body must be empty.

### Response body

Response message for `tokenAuthUsers.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tokenAuthUsers": [
        {
          object ([TokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers#TokenAuthUser))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`tokenAuthUsers[]` |  `object (`[TokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers#TokenAuthUser)`)` A list of token auth users in the project.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Unordered list. Token auth users that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/memorystore.read-write`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
