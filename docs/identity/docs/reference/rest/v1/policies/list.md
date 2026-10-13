---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/list/
title: Method: policies.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:44.029381+00:00
---

# Method: policies.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: policies.list Stay organized with collections  Save and categorize content based on your preferences. 

List policies.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/policies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of results to return. The service can return fewer than this number. If omitted or set to `0`, the default is `50` results per page. The maximum allowed value is `100`. `pageSize` values greater than `100` default to `100`.  
`pageToken` |  `string` Optional. The pagination token received from a prior call to PoliciesService.ListPolicies to retrieve the next page of results. When paginating, all other parameters provided to `ListPoliciesRequest` must match the call that provided the page token.  
`filter` |  `string` Optional. A CEL expression for filtering the results.Policies can be filtered using the expression in the following ways:

  * Filter by application: `setting.type.matches('^settings/gmail\\..*$')`
  * Filter by setting type: `setting.type.matches('^.*\\.service_status$')`
  * Filter by customer: `customer == "customers/{customer}"` Where `customer` is the `id` from the [Admin SDK `Customer` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers). You may use `customers/my_customer` to specify your own organization. When no `customer` is mentioned it will be default to `customers/my_customer`. You may only filter on policies for a single customer at a time.

The above clauses can be combined together in a single filter expression with the `&&` and `||` operators, like in the following example: `customer == "customers/my_customer" && ( setting.type.matches('^settings/gmail\\..*$') || setting.type.matches('^.*\\.service_status$') )`.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[PoliciesService.ListPolicies](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/list#google.apps.cloudidentity.policies.v1.PoliciesService.ListPolicies)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([Policy](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies#Policy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policies[]` |  `object (`[Policy](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies#Policy)`)` The results  
`nextPageToken` |  `string` The pagination token to retrieve the next page of results. If this field is empty, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.policies.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.policies`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
