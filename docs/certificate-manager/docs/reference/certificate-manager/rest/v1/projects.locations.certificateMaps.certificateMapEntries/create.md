---
url: https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/create/
title: Method: projects.locations.certificateMaps.certificateMapEntries.create \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:19.668601+00:00
---

# Method: projects.locations.certificateMaps.certificateMapEntries.create  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-manager/docs/apis)



Send feedback 

#  Method: projects.locations.certificateMaps.certificateMapEntries.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new CertificateMapEntry in a given project and location.

### HTTP request

`POST https://certificatemanager.googleapis.com/v1/{parent=projects/*/locations/*/certificateMaps/*}/certificateMapEntries`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the certificate map entry. Must be in the format `projects/*/locations/*/certificateMaps/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certmapentries.create`

  
  
### Query parameters

Parameters  
---  
`certificateMapEntryId` |  `string` Required. A user-provided name of the certificate map entry.  
  
### Request body

The request body contains an instance of `[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries#CertificateMapEntry)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
