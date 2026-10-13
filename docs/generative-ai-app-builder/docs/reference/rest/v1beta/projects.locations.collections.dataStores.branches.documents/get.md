---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/get/
title: Method: projects.locations.collections.dataStores.branches.documents.get \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:34.744337+00:00
---

# Method: projects.locations.collections.dataStores.branches.documents.get  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/get/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.branches.documents.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Gets a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Full resource name of `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}/documents/{document}`.If the caller does not have permission to access the `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.If the requested `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)` does not exist, a `NOT_FOUND` error is returned.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.documents.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
