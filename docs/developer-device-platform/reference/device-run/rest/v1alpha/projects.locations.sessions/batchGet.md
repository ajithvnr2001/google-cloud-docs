---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet/
title: Method: projects.locations.sessions.batchGet \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:57.392483+00:00
---

# Method: projects.locations.sessions.batchGet  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.locations.sessions.batchGet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves multiple automation sessions in a single batch request.

Sessions are returned in the same order as the `names` in the request. If any of the requested sessions does not exist, the whole request fails with `NOT_FOUND` and no sessions are returned.

When calling this method over HTTP/REST with a large number of `names`, the request URL may exceed the maximum URL length (about 16 KB) and be rejected. In that case, send a `POST` request to the same URL with the `X-HTTP-Method-Override: GET` header and pass the request parameters in a JSON (`application/json`) or form-encoded (`application/x-www-form-urlencoded`) body. See [Long request URLs](https://docs.cloud.google.com/apis/docs/http#long_request_urls).

### HTTP request

`GET https://devicerun.googleapis.com/v1alpha/{parent=projects/*/locations/*}/sessions:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all sessions being retrieved. Format: `projects/{project}/locations/{location}`. The `parent` field in the `BatchGetSessionsRequest` message must match the `parent` of all `Session` resource names in `names`. It takes the form `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`names[]` |  `string` Required. The names of the sessions to retrieve. A maximum of 500 sessions can be retrieved in a batch. Format: `projects/{project}/locations/{location}/sessions/{session}`.  
  
### Request body

The request body must be empty.

### Response body

Response including the requested sessions.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessions": [
        {
          object ([Session](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Session))
        }
      ]
    }  
  
Fields  
---  
`sessions[]` |  `object (`[Session](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Session)`)` The requested sessions, in the same order as the `names` in the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://docs.cloud.google.com/iam/docs) permission on the `parent` resource:

  * `devicerun.sessions.get`



For more information, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
