---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/list/
title: Method: caseComments.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:27.176221+00:00
---

# Method: caseComments.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseComments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseComments.list

Lists CaseComments associated with a specific Case. Use this method to retrieve a chronological record of analyst interactions and observations for a case. Supports filtering by author, creation time and other fields.

### HTTP request

`GET https://{endpoint}/v1/{parent}/caseComments`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list CaseComments for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseComments  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of CaseComments to return. The service may return fewer than this value. If unspecified, at most 50 CaseComments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `caseComments.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter to apply to the list of CaseComments. Supported filter fields: * `createTime`: Filter by the create time. * `updateTime`: Filter by the update time. * `user`: Filter by the user. * `comment`: Filter by the comment. * `deletionInvoker`: Filter by the deletion invoker. * `favorite`: Filter by the favorite. * `alert`: Filter by the alert. * `deleted`: Filter by the deleted.Example: `filter="comment='some_comment'"`  
`orderBy` |  `string` Optional. Configures ordering of CaseComments in the response. If not specified, CaseComments are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. Supported sort fields: * `createTime` * `updateTime` * `user` * `comment` * `deletionInvoker` * `favorite` * `alert` * `deleted`For example: "comment desc, favorite"  
`expand` |  `string` Optional. Expand the response to include the full comment object. Supported values: * `caseAttachment` example: "?expand=caseAttachment"  
  
### Request body

The request body must be empty.

### Response body

Response message for caseComments.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseComments": [
        {
          object ([CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`caseComments[]` |  `object (`[CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment)`)` The list of CaseComments.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of CaseComments.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.caseComments.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
