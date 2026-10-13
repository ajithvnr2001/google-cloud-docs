---
url: https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/get/
title: Method: projects.traceSinks.get \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:47.333209+00:00
---

# Method: projects.traceSinks.get  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  Method: projects.traceSinks.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Get a trace sink by name under the parent resource (GCP project).

### HTTP request

`GET https://cloudtrace.googleapis.com/v2beta1/{name=projects/*/traceSinks/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the sink:
    
    
    "projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]"
    

Example: `"projects/12345/traceSinks/my-sink-id"`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `cloudtrace.tracesinks.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[TraceSink](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks#TraceSink)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/trace.readonly`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
