---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/list/
title: Method: caseAlerts.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:10.567149+00:00
---

# Method: caseAlerts.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseAlerts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseAlerts.list

Lists CaseAlerts within a specific Case. Use this method to retrieve a paginated list of alerts associated with a case. Supports filtering by status, priority, and other alert attributes.

### HTTP request

`GET https://{endpoint}/v1/{parent}/caseAlerts`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list CaseAlerts for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of CaseAlerts to return. The service may return fewer than this value. If unspecified, at most 50 CaseAlerts will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `caseAlerts.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `caseAlerts.list` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter to apply to the list of CaseAlerts. Supported filter fields: * `displayName`: Filter by the display name. * `caseId`: Filter by the case id. * `identifier`: Filter by the identifier. * `sourceGroupingIdentifier`: Filter by the source grouping id. * `product`: Filter by the product. * `vendor`: Filter by the vendor. * `environment`: Filter by the environment. * `ticketId`: Filter by the ticket id. * `sourceSystemName`: Filter by the source system name. * `creation_method`: Filter by the creation method. * `priority`: Filter by the priority. * `status`: Filter by the status. * `startTime`: Filter by the start time. * `endTime`: Filter by the end time. * `additionalProperties`: Filter by the additional properties. * `involvedRelations`: Filter by the involved relations. Example: `filter="displayName='some_name'"`  
`orderBy` |  `string` Optional. Configures ordering of CaseAlerts in the response. If not specified, CaseAlerts are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. Supported sort fields: * `displayName`: Sort by the display name. * `caseId`: Sort by the case id. * `identifier`: Sort by the identifier. * `source_grouping_id`: Sort by the source grouping id. * `product`: Sort by the product. * `vendor`: Sort by the vendor. * `environment`: Sort by the environment. * `ticketId`: Sort by the ticket id. * `sourceSystemName`: Sort by the source system name. * `creation_method`: Sort by the creation method. * `priority`: Sort by the priority. * `status`: Sort by the status. * `startTime`: Sort by the start time. * `endTime`: Sort by the end time. * `additionalProperties`: Sort by the additional properties. example: "displayName desc, default"  
`expand` |  `string` Optional. Expand the response to include the full alert object. Supported values: * `sla` * `involvedRelations` example: "sla, involvedRelations"  
`distinctBy` |  `string` Optional. fields to distinct results. example: ?distinctBy=caseId  
  
### Request body

The request body must be empty.

### Response body

Response message for caseAlerts.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseAlerts": [
        {
          object ([CaseAlert](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#CaseAlert))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`caseAlerts[]` |  `object (`[CaseAlert](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#CaseAlert)`)` The list of CaseAlerts.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of results matching the request.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.caseAlerts.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
