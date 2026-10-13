---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/list/
title: Method: inboundSsoAssignments.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:56.092133+00:00
---

# Method: inboundSsoAssignments.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: inboundSsoAssignments.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`s for a `Customer`.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/inboundSsoAssignments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`filter` |  `string` A CEL expression to filter the results.The only supported filter is filtering by customer. For example: `customer==customers/C0123abc`.Omitting the filter or specifying a filter of `customer==customers/my_customer` will return the assignments for the customer that the caller (authenticated user) belongs to.  
`pageSize` |  `integer` The maximum number of assignments to return. The service may return fewer than this value.If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time.The maximum allowed value is 100, though requests with pageSize greater than that will be silently interpreted as having this maximum value. This may increase in the futue.  
`pageToken` |  `string` A page token, received from a previous `inboundSsoAssignments.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `inboundSsoAssignments.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response of the `[InboundSsoAssignmentsService.ListInboundSsoAssignments](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/list#google.apps.cloudidentity.inboundssoassignments.v1beta1.InboundSsoAssignmentsService.ListInboundSsoAssignments)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inboundSsoAssignments": [
        {
          object ([InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`inboundSsoAssignments[]` |  `object (`[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`)` The assignments.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.inboundsso.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.inboundsso`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
