---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains/list/
title: Method: apps.authorizedDomains.list \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:00.396278+00:00
---

# Method: apps.authorizedDomains.list  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.authorizedDomains.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * AuthorizedDomain
    * JSON representation
  * Try it!



Lists all domains the user is authorized to administer.

### HTTP request

`GET https://appengine.googleapis.com/v1beta/{parent=apps/*}/authorizedDomains`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum results to return per page.  
`pageToken` |  `string` Continuation token for fetching the next page of results.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `AuthorizedDomains.ListAuthorizedDomains`.

JSON representation  
---  
      
    
    {
      "domains": [
        {
          object ([AuthorizedDomain](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains/list#AuthorizedDomain))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`domains[]` |  `object (`[AuthorizedDomain](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains/list#AuthorizedDomain)`)` The authorized domains belonging to the user.  
`nextPageToken` |  `string` Continuation token for fetching the next page of results.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## AuthorizedDomain

A domain that a user has been authorized to administer. To authorize use of a domain, verify ownership via [Search Console](https://search.google.com/search-console/welcome).

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string
    }  
  
Fields  
---  
`name` |  `string` Full path to the `AuthorizedDomain` resource in the API. Example: `apps/myapp/authorizedDomains/example.com`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Fully qualified domain name of the domain authorized for use. Example: `example.com`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
