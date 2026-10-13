---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/list/
title: Method: inboundOidcSsoProfiles.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:40.597128+00:00
---

# Method: inboundOidcSsoProfiles.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: inboundOidcSsoProfiles.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` objects for a Google enterprise customer.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/inboundOidcSsoProfiles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`filter` |  `string` A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results.The only supported filter is filtering by customer. For example: `customer=="customers/C0123abc"`.Omitting the filter or specifying a filter of `customer=="customers/my_customer"` will return the profiles for the customer that the caller (authenticated user) belongs to.Specifying a filter of `customer==""` will return the global shared OIDC profiles.  
`pageSize` |  `integer` The maximum number of `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`s to return. The service may return fewer than this value.If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time.The maximum allowed value is 100. Requests with pageSize greater than that will be silently interpreted as having this maximum value.  
`pageToken` |  `string` A page token, received from a previous `inboundOidcSsoProfiles.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `inboundOidcSsoProfiles.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response of the `[InboundOidcSsoProfilesService.ListInboundOidcSsoProfiles](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/list#google.apps.cloudidentity.inboundoidcssoprofiles.v1.InboundOidcSsoProfilesService.ListInboundOidcSsoProfiles)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inboundOidcSsoProfiles": [
        {
          object ([InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`inboundOidcSsoProfiles[]` |  `object (`[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`)` List of InboundOidcSsoProfiles.  
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
