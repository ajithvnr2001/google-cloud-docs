---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataAccessScopes/list/
title: Method: dataAccessScopes.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:38.616431+00:00
---

# Method: dataAccessScopes.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataAccessScopes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: dataAccessScopes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.dataAccessScopes.list

Lists all existing data access scopes for the customer.

### HTTP request

`GET https://{endpoint}/v1beta/{parent}/dataAccessScopes`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this data access scope will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of data access scopes to return. The service may return fewer than this value. If unspecified, at most 100 data access scopes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous `ListDataAccessScopesRequest` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter which should follow the guidelines of AIP-160. Supports filtering on all fieds of DataAccessScope and all operations as mentioned in <https://google.aip.dev/160>. example filter: "createTime greater than "2023-04-21T11:30:00-04:00" OR displayName:"-21-1"".  
  
### Request body

The request body must be empty.

### Response body

Response message for dataAccessScopes.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataAccessScopes": [
        {
          object ([DataAccessScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataAccessScopes#DataAccessScope))
        }
      ],
      "nextPageToken": string,
      "globalDataAccessScopeGranted": boolean
    }  
  
Fields  
---  
`dataAccessScopes[]` |  `object (`[DataAccessScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataAccessScopes#DataAccessScope)`)` List of data access scopes.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`globalDataAccessScopeGranted` |  `boolean` Whether or not global scope is granted to the user.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.dataAccessScopes.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
