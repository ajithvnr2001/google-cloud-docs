---
url: https://docs.cloud.google.com/video-intelligence/docs/reference/rest/
title: Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:18.585723+00:00
---

# Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/reference/rest/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/video-intelligence/docs/apis)



Send feedback 

#  Cloud Video Intelligence API Stay organized with collections  Save and categorize content based on your preferences. 

Detects objects, explicit content, and scene changes in videos. It also specifies the region for annotation and transcribes speech to text. Supports both asynchronous API and streaming API.

  * REST Resource: v1.operations.projects.locations.operations
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.videos



## Service: videointelligence.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://videointelligence.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://videointelligence.googleapis.com`



## REST Resource: [v1.operations.projects.locations.operations](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/operations.projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/operations.projects.locations.operations/cancel)` |  `POST /v1/operations/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/operations.projects.locations.operations/delete)` |  `DELETE /v1/operations/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/operations.projects.locations.operations/get)` |  `GET /v1/operations/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.videos](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos)

Methods  
---  
`[annotate](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate)` |  `POST /v1/videos:annotate`   
Performs asynchronous video annotation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
