---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobView/
title: JobView \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:37.646031+00:00
---

# JobView  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/docs/apis)



Send feedback 

#  JobView Stay organized with collections  Save and categorize content based on your preferences. 

An enum that specifies the job attributes that are returned in the `[MatchingJob.job](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/SearchJobsResponse#MatchingJob.FIELDS.job)` or `[ListJobsResponse.jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/list#body.ListJobsResponse.FIELDS.jobs)` fields.

Enums  
---  
`JOB_VIEW_UNSPECIFIED` | Default value.  
`JOB_VIEW_ID_ONLY` | A ID only view of job, with following attributes: `[Job.name](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.name)`, `[Job.requisition_id](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.requisition_id)`, `[Job.language_code](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.language_code)`.  
`JOB_VIEW_MINIMAL` | A minimal view of the job, with the following attributes: `[Job.name](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.name)`, `[Job.requisition_id](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.requisition_id)`, `[Job.title](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.title)`, `[Job.company](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.company)`, `[Job.DerivedInfo.locations](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#DerivedInfo.FIELDS.locations)`, `[Job.language_code](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.language_code)`.  
`JOB_VIEW_SMALL` | A small view of the job, with the following attributes in the search results: `[Job.name](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.name)`, `[Job.requisition_id](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.requisition_id)`, `[Job.title](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.title)`, `[Job.company](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.company)`, `[Job.DerivedInfo.locations](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#DerivedInfo.FIELDS.locations)`, `[Job.visibility](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.visibility)`, `[Job.language_code](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.language_code)`, `[Job.description](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.description)`.  
`JOB_VIEW_FULL` | All available attributes are included in the search results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
