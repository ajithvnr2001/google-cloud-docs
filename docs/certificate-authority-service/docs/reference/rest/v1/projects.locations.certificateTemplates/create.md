---
url: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates/create/
title: Method: projects.locations.certificateTemplates.create \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:19.423559+00:00
---

# Method: projects.locations.certificateTemplates.create  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback 

#  Method: projects.locations.certificateTemplates.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Create a new `[CertificateTemplate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates#CertificateTemplate)` in a given Project and Location.

### HTTP request

`POST https://privateca.googleapis.com/v1/{parent=projects/*/locations/*}/certificateTemplates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the location associated with the `[CertificateTemplate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates#CertificateTemplate)`, in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `privateca.certificateTemplates.create`

  
  
### Query parameters

Parameters  
---  
`certificateTemplateId` |  `string` Required. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`  
`requestId` |  `string` Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[CertificateTemplate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates#CertificateTemplate)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
