---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/cancel/
title: Method: googleapis.bigquery.v2.jobs.cancel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:51.973156+00:00
---

# Method: googleapis.bigquery.v2.jobs.cancel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/cancel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquery.v2.jobs.cancel Stay organized with collections  Save and categorize content based on your preferences. 

Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. # IAM Permissions Requires the `bigquery.jobs.update` permission on the job resource. If the user matches the creator of the job, the `bigquery.jobs.create` permission on the project is required instead.

## Arguments

Parameters  
---  
`jobId` |  `string` Required. Job ID of the job to cancel  
`projectId` |  `string` Required. Project ID of the job to cancel  
`location` |  `string` The geographic location of the job. You must [specify the location](https://cloud.google.com/bigquery/docs/locations#specify_locations) to run the job for the following scenarios: * If the location to run a job is not in the `us` or the `eu` multi-regional location * If the job's location is in a single region (for example, `us-central1`)  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`JobCancelResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#JobCancelResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel).

### YAML
    
    
    - cancel:
        call: googleapis.bigquery.v2.jobs.cancel
        args:
            jobId: ...
            projectId: ...
            location: ...
        result: cancelResult

### JSON
    
    
    [
      {
        "cancel": {
          "call": "googleapis.bigquery.v2.jobs.cancel",
          "args": {
            "jobId": "...",
            "projectId": "...",
            "location": "..."
          },
          "result": "cancelResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
