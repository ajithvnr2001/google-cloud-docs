---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/lookup/
title: Method: groups.memberships.lookup \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:39.425271+00:00
---

# Method: groups.memberships.lookup  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.memberships.lookup Stay organized with collections  Save and categorize content based on your preferences. 

Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=groups/*}/memberships:lookup`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent `Group` resource under which to lookup the `Membership` name.Must be of the form `groups/{group}`.  
  
### Query parameters

Parameters  
---  
`memberKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` Required. The `[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)` of the member to lookup.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[MembershipsService.LookupMembershipName](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/lookup#google.apps.cloudidentity.groups.v1.MembershipsService.LookupMembershipName)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` The [resource name](https://cloud.google.com/apis/design/resource_names) of the looked-up `Membership`.Must be of the form `groups/{group}/memberships/{membership}`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
