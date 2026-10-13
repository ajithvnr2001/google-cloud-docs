---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/dataflow/v1b3/projects.locations.jobs/list/
title: Method: googleapis.dataflow.v1b3.projects.locations.jobs.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:43.447111+00:00
---

# Method: googleapis.dataflow.v1b3.projects.locations.jobs.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/dataflow/v1b3/projects.locations.jobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.dataflow.v1b3.projects.locations.jobs.list Stay organized with collections  Save and categorize content based on your preferences. 

List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, as you can only get the list of jobs that are running in `us-central1`.

## Arguments

Parameters  
---  
`location` |  `string` Required. The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.  
`projectId` |  `string` Required. The project which owns the jobs.  
`filter` |  `enum` The kind of filter to use.  
Enum type. Can be one of the following:  
`UNKNOWN` | The filter isn't specified, or is unknown. This returns all jobs ordered on descending `JobUuid`.  
`ALL` | Returns all running jobs first ordered on creation timestamp, then returns all terminated jobs ordered on the termination timestamp.  
`TERMINATED` | Filters the jobs that have a terminated state, ordered on the termination timestamp. Example terminated states: `JOB_STATE_STOPPED`, `JOB_STATE_UPDATED`, `JOB_STATE_DRAINED`, etc.  
`ACTIVE` | Filters the jobs that are running ordered on the creation timestamp.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` If there are many jobs, limit response to at most this many. The actual number of jobs returned will be the lesser of max_responses and an unspecified server-defined limit.  
`pageToken` |  `string` Set this to the 'next_page_token' field of a previous response to request additional results in a long list.  
`view` |  `enum` Deprecated. ListJobs always returns summaries now. Use GetJob for other JobViews.  
Enum type. Can be one of the following:  
`JOB_VIEW_UNKNOWN` | The job view to return isn't specified, or is unknown. Responses will contain at least the `JOB_VIEW_SUMMARY` information, and may contain additional information.  
`JOB_VIEW_SUMMARY` | Request summary information only: Project ID, Job ID, job name, job type, job status, start/end time, and Cloud SDK version details.  
`JOB_VIEW_ALL` | Request all information available for this job.  
`JOB_VIEW_DESCRIPTION` | Request summary info and limited job description data for steps, labels and environment.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListJobsResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/dataflow/v1b3/Overview#ListJobsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/list).

### YAML
    
    
    - list:
        call: googleapis.dataflow.v1b3.projects.locations.jobs.list
        args:
            location: ...
            projectId: ...
            filter: ...
            pageSize: ...
            pageToken: ...
            view: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.dataflow.v1b3.projects.locations.jobs.list",
          "args": {
            "location": "...",
            "projectId": "...",
            "filter": "...",
            "pageSize": "...",
            "pageToken": "...",
            "view": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
