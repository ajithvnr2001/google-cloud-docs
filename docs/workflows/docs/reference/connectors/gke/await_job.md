---
url: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/await_job/
title: Function: gke.await_job \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:37.008584+00:00
---

# Function: gke.await_job  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/await_job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: gke.await_job Stay organized with collections  Save and categorize content based on your preferences. 

Wait for a Kubernetes Job to complete.

## Arguments

Arguments  
---  
`cluster_id` |  `string` The ID of the cluster.  
`job_name` |  `string` Name of the job.  
`location` |  `string` The location that the cluster is hosted in.  
`namespace` |  `string` The namespace of the job (default: `default`).  
`project` |  `string` The project that the cluster is hosted in. Default value is this workflow's project.  
`query` | Optional query parameters for fetching the job. If present, must be a map of simple types that will be URL-encoded and appended to the URL. For more information, see [Kubernetes API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#read-job-v1-batch).  
`timeout` |  `float` The timeout, in seconds (default: `1800.0`). If the job doesn't complete within the timeout, a `TimeoutError` is raised. The maximum allowed timeout is one year.  
`polling_policy` |  `dict` Policy for polling the job's status. Supported fields are `initial_delay`, `max_delay`, and `multiplier`. For details, see [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).  
  
## Returns

The completed [Kubernetes Job](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#job-v1-batch).

## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (DNS failure, refused connection, etc.).  
`TimeoutError` | When the specified timeout is reached before the response is received.  
`HttpError` | If the response status is >= 400.  
`ValueError` | If the cluster does not have status `RUNNING`.  
`FailedJobError` | If the job failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
