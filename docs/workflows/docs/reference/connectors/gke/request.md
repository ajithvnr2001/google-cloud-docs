---
url: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/request/
title: Function: gke.request \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:38.257994+00:00
---

# Function: gke.request  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: gke.request Stay organized with collections  Save and categorize content based on your preferences. 

Send an HTTP request to a GKE cluster's control plane.

## Arguments

Arguments  
---  
`cluster_id` |  `string` The ID of the cluster.  
`path` |  `string` Path to the API endpoint (for example, `/api/v1/namespaces/default/pods`). For more information, see [Kubernetes API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/).  
`method` |  `string` The HTTP request method. One of: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `OPTIONS`, `PATCH`.  
`location` |  `string` The location that the cluster is hosted in.   
`project` |  `string` The project that the cluster is hosted in. Default value is this workflow's project.  
`timeout` |  `float` The request timeout, in seconds (default: `300.0`). If the request takes longer than the timeout, a `TimeoutError` is raised. The maximum allowed timeout is `1800` seconds.  
`body` | The request body. If a `Content-Type` header is not specified and if the body value is bytes, the header is set to `Content-Type: application/octet-stream`; otherwise, the body is JSON-encoded and the header is set to `Content-type: application/json; charset=utf-8`.  
`headers` | The HTTP request headers. If present, must be a map of simple types. If a `Content-Type` header is specified, the request body is encoded as prescribed. For example, it might be JSON or URL-encoded.  
`query` | Optional query parameters. If present, must be a map of simple types that will be URL-encoded and appended to the URL.  
  
## Returns

The HTTP response as a map with `body`, `code` (status code), and `headers` attributes.

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
