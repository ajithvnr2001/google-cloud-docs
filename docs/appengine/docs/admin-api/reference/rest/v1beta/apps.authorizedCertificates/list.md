---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/list/
title: Method: apps.authorizedCertificates.list \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:00.032419+00:00
---

# Method: apps.authorizedCertificates.list  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.authorizedCertificates.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists all SSL certificates the user is authorized to administer.

### HTTP request

`GET https://appengine.googleapis.com/v1beta/{parent=apps/*}/authorizedCertificates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Name of the parent `Application` resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
  
### Query parameters

Parameters  
---  
`view` |  `enum (`[AuthorizedCertificateView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/AuthorizedCertificateView)`)` Controls the set of fields returned in the `LIST` response.  
`pageSize` |  `integer` Maximum results to return per page.  
`pageToken` |  `string` Continuation token for fetching the next page of results.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `AuthorizedCertificates.ListAuthorizedCertificates`.

JSON representation  
---  
      
    
    {
      "certificates": [
        {
          object ([AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates#AuthorizedCertificate))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`certificates[]` |  `object (`[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates#AuthorizedCertificate)`)` The SSL certificates the user is authorized to administer.  
`nextPageToken` |  `string` Continuation token for fetching the next page of results.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
