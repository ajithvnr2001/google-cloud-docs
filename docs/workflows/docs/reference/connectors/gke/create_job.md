---
url: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/create_job/
title: Function: gke.create_job \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:37.572627+00:00
---

# Function: gke.create_job  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/create_job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: gke.create_job Stay organized with collections  Save and categorize content based on your preferences. 

Run a Kubernetes Job in a GKE cluster.

## Arguments

Arguments  
---  
`cluster_id` |  `string` The ID of the cluster.  
`job` |  `map` A [Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) definition.  
`location` |  `string` The location that the cluster is hosted in.  
`namespace` |  `string` The namespace to run the job in (default: `default`).  
`project` |  `string` The project that the cluster is hosted in. Default value is this workflow's project.  
`query` | Optional query parameters. If present, must be a map of simple types that will be URL-encoded and appended to the URL. For more information, see [Kubernetes API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#-strong-write-operations-job-v1-batch-strong-).  
`timeout` |  `float` The request timeout, in seconds (default: `300.0`). If the request takes longer than the timeout, a `TimeoutError` is raised. The maximum allowed timeout is `1800` seconds.  
  
## Returns

The created [Kubernetes Job](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#job-v1-batch).

## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (DNS failure, refused connection, etc.).  
`TimeoutError` | When the specified timeout is reached before the response is received.  
`HttpError` | If the response status is >= 400.  
`ValueError` | If timeout is > 1800, or if the cluster does not have status `RUNNING`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
