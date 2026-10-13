---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/list/
title: Method: cases.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:03.049154+00:00
---

# Method: cases.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.list

Lists Cases in an instance. Use this method to retrieve a paginated list of cases. Supports extensive filtering and ordering based on case attributes like priority, status, assignee and more.

### HTTP request

`GET https://{endpoint}/v1/{parent}/cases`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list Cases for. Format: projects/{project}/locations/{location}/instances/{instance}/cases  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of cases to return. The service may return fewer than this value. If unspecified, at most 50 Cases will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `cases.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `cases.list` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter to apply to the list of Cases. Supported filter fields: * `displayName` * `creatorUserId` * `creatorUser` * `lastModifyingUserId` * `lastModifyingUser` * `assignee` * `assignedUser` * `stage` * `priority` * `important` * `type` * `environment` * `case_data_state` * `score` * `alertsSla` * `sla` * `tags` * `products` * `closureDetails` * `tasks` Example: `filter="displayName='some_name'"`  
`orderBy` |  `string` Optional. Configures ordering of Cases in the response. If not specified, Cases are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. Supported sort fields: * `displayName` * `creatorUserId` * `creatorUser` * `lastModifyingUserId` * `lastModifyingUser` * `assignee` * `assignedUser` * `stage` * `priority` * `important` * `type` * `environment` * `case_data_state` * `score` * `alertsSla` * `sla` * `tags` * `products` * `closureDetails` * `tasks` example: "displayName desc, priority"  
`expand` |  `string` Optional. Expand the response to include the full case object. Supported values: * `tasks` * `tags` * `products` example: "tags, products"  
`distinctBy` |  `string` Optional. The field to distinct the cases by.  
  
### Request body

The request body must be empty.

### Response body

Response message for cases.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "cases": [
        {
          object ([Case](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#Case))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`cases[]` |  `object (`[Case](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#Case)`)` The list of cases.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of results matching the request.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.cases.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
