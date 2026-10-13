---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/list/
title: Method: projects.profiles.list \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:43.659331+00:00
---

# Method: projects.profiles.list  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  Method: projects.profiles.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists profiles which have been collected so far and for which the caller has permission to view.

### HTTP request

`GET https://cloudprofiler.googleapis.com/v2/{parent=projects/*}/profiles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of profiles. Format: projects/{user_project_id} It takes the form `projects/{project}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudprofiler.profiles.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. Default pageSize is 1000. Max limit is 1000.  
`pageToken` |  `string` Optional. The token to continue pagination and get profiles from a particular page. When paginating, all other parameters provided to `profiles.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

ListProfileResponse contains the list of collected profiles for deployments in projects which the user has permissions to view.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "profiles": [
        {
          object ([Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Profile))
        }
      ],
      "nextPageToken": string,
      "skippedProfiles": integer
    }  
  
Fields  
---  
`profiles[]` |  `object (`[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Profile)`)` List of profiles fetched.  
`nextPageToken` |  `string` Token to receive the next page of results. This field maybe empty if there are no more profiles to fetch.  
`skippedProfiles` |  `integer` Number of profiles that were skipped in the current page since they were not able to be fetched successfully. This should typically be zero. A non-zero value may indicate a transient failure, in which case if the number is too high for your use case, the call may be retried.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
