---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/delete/
title: Method: googleapis.bigquery.v2.jobs.delete \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:43.833947+00:00
---

# Method: googleapis.bigquery.v2.jobs.delete  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquery.v2.jobs.delete Stay organized with collections  Save and categorize content based on your preferences. 

Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. # IAM Permissions Requires the `bigquery.jobs.delete` permission on the job resource.

## Arguments

Parameters  
---  
`jobId` |  `string` Required. Job ID of the job for which metadata is to be deleted. If this is a parent job which has child jobs, the metadata from all child jobs will be deleted as well. Direct deletion of the metadata of child jobs is not allowed.  
`projectId` |  `string` Required. Project ID of the job for which metadata is to be deleted.  
`location` |  `string` The geographic location of the job. Required. For more information, see how to [specify locations](https://cloud.google.com/bigquery/docs/locations#specify_locations).  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response will be empty.

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/delete).

### YAML
    
    
    - delete:
        call: googleapis.bigquery.v2.jobs.delete
        args:
            jobId: ...
            projectId: ...
            location: ...
        result: deleteResult

### JSON
    
    
    [
      {
        "delete": {
          "call": "googleapis.bigquery.v2.jobs.delete",
          "args": {
            "jobId": "...",
            "projectId": "...",
            "location": "..."
          },
          "result": "deleteResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
