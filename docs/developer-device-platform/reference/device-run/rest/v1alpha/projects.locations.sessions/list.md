---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/list/
title: Method: projects.locations.sessions.list \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:56.615120+00:00
---

# Method: projects.locations.sessions.list  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.locations.sessions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists previously created automation sessions.

Sessions may still be in-progress, or may have finished successfully, or unsuccessfully.

### HTTP request

`GET https://devicerun.googleapis.com/v1alpha/{parent=projects/*/locations/*}/sessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListSessionsRequest The parent of the collection of sessions. Format: `projects/{project}/locations/{location}`. It takes the form `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of sessions to return. The server may return fewer items than this value. If unspecified, at most 500 sessions will be returned. The maximum value is 1000, values above will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `sessions.list` call. Provide this to receive the subsequent page.When paginating, all other parameters provided to `sessions.list` must match the call that provided the page token.  
`filter` |  `string` Optional. The raw filter text to constrain the results.  
`orderBy` |  `string` Optional. The order to sort results by.Supported values: `name`, `name desc`, `create_time`, `create_time desc`. Values must use the snake_case field name; `createTime` is not accepted. Ordering by `create_time` is not supported when listing across all locations (`locations/-`).If unspecified, results are returned in an unspecified order.  
`view` |  `enum (`[SessionView](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/SessionView)`)` Optional. The view of the sessions to return. If not set, the `FULL` view will be returned.  
  
### Request body

The request body must be empty.

### Response body

Response including listed sessions.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessions": [
        {
          object ([Session](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Session))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`sessions[]` |  `object (`[Session](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Session)`)` The list of sessions.  
`nextPageToken` |  `string` Token to receive the next page of sessions. This will be absent if the end of the response list has been reached.  
`unreachable[]` |  `string` Unordered list. Sessions that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://docs.cloud.google.com/iam/docs) permission on the `parent` resource:

  * `devicerun.sessions.list`



For more information, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
