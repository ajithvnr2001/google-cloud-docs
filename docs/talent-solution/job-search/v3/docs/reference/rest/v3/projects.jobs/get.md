---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/get/
title: Method: projects.jobs.get \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:19.758874+00:00
---

# Method: projects.jobs.get  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/apis)



Send feedback 

#  Method: projects.jobs.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

### HTTP request

`GET https://jobs.googleapis.com/v3/{name=projects/*/jobs/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the job to retrieve.The format is "projects/{projectId}/jobs/{job_id}", for example, "projects/api-test-project/jobs/1234".  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Job](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#Job)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/jobs`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
