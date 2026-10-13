---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/
title: Cloud Talent Solution API \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:18.659678+00:00
---

# Cloud Talent Solution API  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/apis)



Send feedback 

#  Cloud Talent Solution API Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution provides the capability to create, read, update, and delete job postings, as well as search jobs based on keywords and filters.

  * REST Resource: v4beta1.projects
  * REST Resource: v4beta1.projects.clientEvents
  * REST Resource: v4beta1.projects.companies
  * REST Resource: v4beta1.projects.jobs
  * REST Resource: v4beta1.projects.operations
  * REST Resource: v4beta1.projects.tenants
  * REST Resource: v4beta1.projects.tenants.clientEvents
  * REST Resource: v4beta1.projects.tenants.companies
  * REST Resource: v4beta1.projects.tenants.jobs



## Service: jobs.googleapis.com

We recommend that you call this service using Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to call this service using your own libraries, you should use the following information when making the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://jobs.googleapis.com/$discovery/rest?version=v4beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary) is a base URL that specifies the network address of an API service. One service may have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://jobs.googleapis.com`



## REST Resource: [v4beta1.projects](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects)

Methods  
---  
`[complete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects/complete)` |  `GET /v4beta1/{parent=projects/*}:complete`   
Completes the specified prefix with keyword suggestions.  
  
## REST Resource: [v4beta1.projects.clientEvents](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.clientEvents)

Methods  
---  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.clientEvents/create)` |  `POST /v4beta1/{parent=projects/*}/clientEvents`   
Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.  
  
## REST Resource: [v4beta1.projects.companies](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies)

Methods  
---  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies/create)` |  `POST /v4beta1/{parent=projects/*}/companies`   
Creates a new company entity.  
`[delete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies/delete)` |  `DELETE /v4beta1/{name=projects/*/companies/*}`   
Deletes specified company.  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies/get)` |  `GET /v4beta1/{name=projects/*/companies/*}`   
Retrieves specified company.  
`[list](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies/list)` |  `GET /v4beta1/{parent=projects/*}/companies`   
Lists all companies associated with the project.  
`[patch](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies/patch)` |  `PATCH /v4beta1/{company.name=projects/*/companies/*}`   
Updates specified company.  
  
## REST Resource: [v4beta1.projects.jobs](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/batchCreate)` |  `POST /v4beta1/{parent=projects/*}/jobs:batchCreate`   
Begins executing a batch create jobs operation.  
`[batchDelete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/batchDelete)` |  `POST /v4beta1/{parent=projects/*}/jobs:batchDelete`   
Deletes a list of `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)`s by filter.  
`[batchUpdate](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/batchUpdate)` |  `POST /v4beta1/{parent=projects/*}/jobs:batchUpdate`   
Begins executing a batch update jobs operation.  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/create)` |  `POST /v4beta1/{parent=projects/*}/jobs`   
Creates a new job.  
`[delete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/delete)` |  `DELETE /v4beta1/{name=projects/*/jobs/*}`   
Deletes the specified job.  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/get)` |  `GET /v4beta1/{name=projects/*/jobs/*}`   
Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.  
`[list](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/list)` |  `GET /v4beta1/{parent=projects/*}/jobs`   
Lists jobs by filter.  
`[patch](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/patch)` |  `PATCH /v4beta1/{job.name=projects/*/jobs/*}`   
Updates specified job.  
`[search](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/search)` |  `POST /v4beta1/{parent=projects/*}/jobs:search`   
Searches for jobs using the provided `SearchJobsRequest`.  
`[searchForAlert](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs/searchForAlert)` |  `POST /v4beta1/{parent=projects/*}/jobs:searchForAlert`   
Searches for jobs using the provided `SearchJobsRequest`.  
  
## REST Resource: [v4beta1.projects.operations](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.operations/get)` |  `GET /v4beta1/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v4beta1.projects.tenants](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants)

Methods  
---  
`[complete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/complete)` |  `GET /v4beta1/{parent=projects/*/tenants/*}:complete`   
Completes the specified prefix with keyword suggestions.  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/create)` |  `POST /v4beta1/{parent=projects/*}/tenants`   
Creates a new tenant entity.  
`[delete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/delete)` |  `DELETE /v4beta1/{name=projects/*/tenants/*}`   
Deletes specified tenant.  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/get)` |  `GET /v4beta1/{name=projects/*/tenants/*}`   
Retrieves specified tenant.  
`[list](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/list)` |  `GET /v4beta1/{parent=projects/*}/tenants`   
Lists all tenants associated with the project.  
`[patch](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants/patch)` |  `PATCH /v4beta1/{tenant.name=projects/*/tenants/*}`   
Updates specified tenant.  
  
## REST Resource: [v4beta1.projects.tenants.clientEvents](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.clientEvents)

Methods  
---  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.clientEvents/create)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/clientEvents`   
Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.  
  
## REST Resource: [v4beta1.projects.tenants.companies](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies)

Methods  
---  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies/create)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/companies`   
Creates a new company entity.  
`[delete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies/delete)` |  `DELETE /v4beta1/{name=projects/*/tenants/*/companies/*}`   
Deletes specified company.  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies/get)` |  `GET /v4beta1/{name=projects/*/tenants/*/companies/*}`   
Retrieves specified company.  
`[list](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies/list)` |  `GET /v4beta1/{parent=projects/*/tenants/*}/companies`   
Lists all companies associated with the project.  
`[patch](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.companies/patch)` |  `PATCH /v4beta1/{company.name=projects/*/tenants/*/companies/*}`   
Updates specified company.  
  
## REST Resource: [v4beta1.projects.tenants.jobs](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchCreate)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs:batchCreate`   
Begins executing a batch create jobs operation.  
`[batchDelete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchDelete)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs:batchDelete`   
Deletes a list of `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)`s by filter.  
`[batchUpdate](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchUpdate)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs:batchUpdate`   
Begins executing a batch update jobs operation.  
`[create](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/create)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs`   
Creates a new job.  
`[delete](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/delete)` |  `DELETE /v4beta1/{name=projects/*/tenants/*/jobs/*}`   
Deletes the specified job.  
`[get](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/get)` |  `GET /v4beta1/{name=projects/*/tenants/*/jobs/*}`   
Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.  
`[list](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/list)` |  `GET /v4beta1/{parent=projects/*/tenants/*}/jobs`   
Lists jobs by filter.  
`[patch](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/patch)` |  `PATCH /v4beta1/{job.name=projects/*/tenants/*/jobs/*}`   
Updates specified job.  
`[search](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/search)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs:search`   
Searches for jobs using the provided `SearchJobsRequest`.  
`[searchForAlert](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/searchForAlert)` |  `POST /v4beta1/{parent=projects/*/tenants/*}/jobs:searchForAlert`   
Searches for jobs using the provided `SearchJobsRequest`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
