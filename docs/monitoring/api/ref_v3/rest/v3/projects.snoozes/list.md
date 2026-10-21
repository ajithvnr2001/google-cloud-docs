---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/list/
title: Method: projects.snoozes.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:14.214587+00:00
---

# Method: projects.snoozes.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.snoozes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the `Snooze`s associated with a project. Can optionally pass in `filter`, which specifies predicates to match `Snooze`s.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{parent}/snoozes`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose `Snooze`s should be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Optional filter to restrict results to the given criteria. The following fields are supported.

  * `interval.start_time`
  * `interval.end_time`

For example:
    
    
    interval.start_time > "2022-03-11T00:00:00-08:00" AND
        interval.end_time < "2022-03-12T00:00:00-08:00"
      
  
`pageSize` |  `integer` Optional. The maximum number of results to return for a single query. The server may further constrain the maximum number of results returned in a single page. The value should be in the range [1, 1000]. If the value given is outside this range, the server will decide the number of results to be returned.  
`pageToken` |  `string` Optional. The `nextPageToken` from a previous call to `ListSnoozesRequest` to get the next page of results.  
  
### Request body

The request body must be empty.

### Response body

The results of a successful `snoozes.list` call, containing the matching `Snooze`s.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "snoozes": [
        {
          object ([Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#Snooze))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`snoozes[]` |  `object (`[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#Snooze)`)` `Snooze`s matching this list call.  
`nextPageToken` |  `string` Page token for repeated calls to `snoozes.list`, to fetch additional pages of results. If this is empty or missing, there are no more pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
