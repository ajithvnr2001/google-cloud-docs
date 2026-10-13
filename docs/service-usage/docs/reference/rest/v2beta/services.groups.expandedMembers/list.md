---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/services.groups.expandedMembers/list/
title: Method: services.groups.expandedMembers.list \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:06.375105+00:00
---

# Method: services.groups.expandedMembers.list  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/services.groups.expandedMembers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  Method: services.groups.expandedMembers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ExpandedMember
    * JSON representation



List the expanded members that belong to a given service group or transitively to any of the groups that are members of the service group. The expanded members are always services. The service group is defined by service producers. It throws NOT_FOUND if the given service group is not defined.

### HTTP request

`GET https://serviceusage.googleapis.com/v2beta/{parent=*/*/services/*/groups/*}/expandedMembers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The group that the expandedMembers.list method is called on.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of expanded members to return. It may return fewer than this value. If unspecified, at most 50 expanded members will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous `expandedMembers.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `expandedMembers.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

The response message of the `expandedMembers.list` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "members": [
        {
          object ([ExpandedMember](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/services.groups.expandedMembers/list#ExpandedMember))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`members[]` |  `object (`[ExpandedMember](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/services.groups.expandedMembers/list#ExpandedMember)`)` The expanded members of the given service group.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ExpandedMember

An expanded member that belongs to a certain service group directly or indirectly. It is always a service.

JSON representation  
---  
      
    
    {
      "parent": string,
      "serviceName": string
    }  
  
Fields  
---  
`parent` |  `string` Output only. The group that the expandedMembers.list method is called on.  
`serviceName` |  `string` Output only. The name of this expanded member, which is always a service in the format of `services/{service}`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-11 UTC."],[],[]] 
