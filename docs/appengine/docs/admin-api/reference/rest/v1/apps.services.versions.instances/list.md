---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list/
title: Method: apps.services.versions.instances.list \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:58.559364+00:00
---

# Method: apps.services.versions.instances.list  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.services.versions.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists the instances of a version.

Tip: To aggregate details about instances over time, see the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

### HTTP request

`GET https://appengine.googleapis.com/v1/{parent=apps/*/services/*/versions/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Name of the parent Version resource. Example: `apps/myapp/services/default/versions/v1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.instances.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum results to return per page.  
`pageToken` |  `string` Continuation token for fetching the next page of results.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `Instances.ListInstances`.

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#Instance))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#Instance)`)` The instances belonging to the requested version.  
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
