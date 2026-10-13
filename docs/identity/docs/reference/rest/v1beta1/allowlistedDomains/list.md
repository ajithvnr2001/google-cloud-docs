---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/list/
title: Method: allowlistedDomains.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:45.256740+00:00
---

# Method: allowlistedDomains.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: allowlistedDomains.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the domains in the allowlist.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/allowlistedDomains`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Specifies the requested page size. If unspecified, the service returns at most 5000 domains. The maximum value is 5000; values above 5000 coerce to 5000. The limits can change over time.  
`pageToken` |  `string` Optional. Identifies a token from a previous page of results, if any.  
`filter` |  `string` Optional. Provides an optional filter for list results. Currently, only exact matches on the domain are supported, such as "domain = 'google.com'", with no composite conditions.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[AllowlistedDomainsService.ListAllowlistedDomains](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/list#google.apps.cloudidentity.allowlisteddomains.v1beta1.AllowlistedDomainsService.ListAllowlistedDomains)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "allowlistedDomains": [
        {
          object ([AllowlistedDomain](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains#AllowlistedDomain))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`allowlistedDomains[]` |  `object (`[AllowlistedDomain](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains#AllowlistedDomain)`)` Contains the list of domains in the allowlist. There is no defined ordering of domains within a result.  
`nextPageToken` |  `string` Contains the next page token if the result is not exhaustive. If there are no more results, this token is empty.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains`
  * `https://www.googleapis.com/auth/cloud-identity`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
