---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/favorite/
title: Method: caseWallRecords.favorite \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:28.894295+00:00
---

# Method: caseWallRecords.favorite  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/favorite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseWallRecords.favorite Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * FavoriteRequest
    * JSON representation



**Full name** : projects.locations.instances.cases.caseWallRecords.favorite

Sets or unsets (toggles) the favorite status of a wall record. Use this method to highlight or unhighlight key pieces of evidence or critical observations on the case wall.

### HTTP request

`PATCH https://{endpoint}/v1/{favoriteRequest.name}:favorite`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`favoriteRequest.name` |  `string` Required. The resource name of the CaseWallRecords to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseWallRecords/{caseActivity}  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update. If not included, all fields with default/non-default values will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[FavoriteRequest](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/favorite#FavoriteRequest)`.

### Response body

If successful, the response body contains an instance of `[CaseWallRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#CaseWallRecord)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.caseWallRecords.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## FavoriteRequest

Request message for caseWallRecords.favorite request.

JSON representation  
---  
      
    
    {
      "name": string,
      "recordId": string,
      "activityType": enum ([WallActivityType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#WallActivityType)),
      "activityKind": enum ([ActivityKind](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#ActivityKind)),
      "favorite": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the CaseWallRecords to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseWallRecords/{caseActivity}  
`recordId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The ID of the wall record to set as a favorite.  
`activityType` |  `enum (`[WallActivityType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#WallActivityType)`)` Required. The type of the activity.  
`activityKind` |  `enum (`[ActivityKind](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#ActivityKind)`)` Optional. The kind of the activity.  
`favorite` |  `boolean` Required. Whether the activity is was marked as favorite.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
