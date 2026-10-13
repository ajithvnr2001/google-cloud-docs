---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.companies/create/
title: Method: projects.companies.create \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:26.599306+00:00
---

# Method: projects.companies.create  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.companies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/apis)



Send feedback 

#  Method: projects.companies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



Creates a new company entity.

### HTTP request

`POST https://jobs.googleapis.com/v3p1beta1/{parent=projects/*}/companies`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the project under which the company is created.The format is "projects/{projectId}", for example, "projects/api-test-project".  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "company": {
        object ([Company](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.companies#Company))
      }
    }  
  
Fields  
---  
`company` |  `object (`[Company](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.companies#Company)`)` Required. The company to be created.  
  
### Response body

If successful, the response body contains a newly created instance of `[Company](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.companies#Company)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/jobs`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
