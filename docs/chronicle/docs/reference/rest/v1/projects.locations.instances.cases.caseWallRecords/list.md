---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/list/
title: Method: caseWallRecords.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:30.065546+00:00
---

# Method: caseWallRecords.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseWallRecords.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseWallRecords.list

Lists CaseWallRecords for a specific Case. Use this method to retrieve the complete investigation timeline. Supports filtering by activity type, author and other fields.

### HTTP request

`GET https://{endpoint}/v1/{parent}/caseWallRecords`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list CaseWallRecords for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseWallRecords  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of CaseWallRecords to return. The service may return fewer than this value. If unspecified, at most 50 CaseWallRecords will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `caseWallRecords.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter to apply to the list of CaseWallRecords. Supported filter fields: * `caseId` * `activityId` * `activityType` * `activityData` * `alertId` * `creatorUserId` * `createTime` * `updateTime` * `favorite`Example: `filter="email='some_name'"`  
`orderBy` |  `string` Optional. Configures ordering of CaseWallRecords in the response. If not specified, CaseWallRecords are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. Supported sort fields: * `caseId` * `activityId` * `activityType` * `activityData` * `alertId` * `creatorUserId` * `createTime` * `updateTime` * `favorite`example: "alertId desc, activityType"  
`expand` |  `string` Optional. Expand the response to include related resources. Supported values: * `tags`  
  
### Request body

The request body must be empty.

### Response body

Response message for caseWallRecords.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseWallRecords": [
        {
          object ([CaseWallRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#CaseWallRecord))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`caseWallRecords[]` |  `object (`[CaseWallRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#CaseWallRecord)`)` The list of CaseWallRecords.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` Total number of CaseWallRecords.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.caseWallRecords.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
