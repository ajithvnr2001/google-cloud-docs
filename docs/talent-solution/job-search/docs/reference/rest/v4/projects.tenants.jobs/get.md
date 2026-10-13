---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/get/
title: Method: projects.tenants.jobs.get \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:33.619418+00:00
---

# Method: projects.tenants.jobs.get  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/docs/apis)



Send feedback 

#  Method: projects.tenants.jobs.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

### HTTP request

`GET https://jobs.googleapis.com/v4/{name=projects/*/tenants/*/jobs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the job to retrieve.The format is "projects/{projectId}/tenants/{tenantId}/jobs/{job_id}". For example, "projects/foo/tenants/bar/jobs/baz".  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Job](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/jobs`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/external/authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
