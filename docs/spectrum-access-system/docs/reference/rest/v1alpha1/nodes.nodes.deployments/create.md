---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.nodes.deployments/create/
title: Method: nodes.nodes.deployments.create \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:04.057934+00:00
---

# Method: nodes.nodes.deployments.create  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.nodes.deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  Method: nodes.nodes.deployments.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes



Creates a new `[deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.

### HTTP request

`POST https://sasportal.googleapis.com/v1alpha1/{parent=nodes/*/nodes/*}/deployments`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name where the deployment is to be created.  
  
### Request body

The request body contains an instance of `[Deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.

### Response body

If successful, the response body contains a newly created instance of `[Deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
