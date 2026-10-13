---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.customLists/list/
title: Method: customLists.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:18.104329+00:00
---

# Method: customLists.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.customLists/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: customLists.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.customLists.list

Lists all custom list entries in the instance. Use this method to browse the available custom lists. Supports filtering by category or entity identifier.

### HTTP request

`GET https://{endpoint}/v1/{parent}/customLists`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list Custom Lists for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of CustomLists to return.  
`pageToken` |  `string` Optional. A page token, received from a previous `customLists.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression that matches a subset of the CustomLists to show.  
`orderBy` |  `string` Optional. Configures ordering of CustomLists in the response. If not specified, CustomLists are returned in descending order of their create time.  
  
### Request body

The request body must be empty.

### Response body

Response message to list custom lists.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customLists": [
        {
          object ([CustomList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.customLists#CustomList))
        }
      ],
      "totalSize": integer,
      "nextPageToken": string
    }  
  
Fields  
---  
`customLists[]` |  `object (`[CustomList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.customLists#CustomList)`)` Output only. The list of CustomLists, ordered by ModificationTimeUnixTimeInMs ascending by default.  
`totalSize` |  `integer` Output only. The total number of custom lists.  
`nextPageToken` |  `string` Output only. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.customLists.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
