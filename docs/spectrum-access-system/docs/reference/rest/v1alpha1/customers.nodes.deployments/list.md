---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes.deployments/list/
title: Method: customers.nodes.deployments.list \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:39.166047+00:00
---

# Method: customers.nodes.deployments.list  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes.deployments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  Method: customers.nodes.deployments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes



Lists `[deployments](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.

### HTTP request

`GET https://sasportal.googleapis.com/v1alpha1/{parent=customers/*/nodes/*}/deployments`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, for example, "nodes/1", customer/1/nodes/2.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of deployments to return in the response.  
`pageToken` |  `string` A pagination token returned from a previous call to `[deployments.list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/list#spectrum.sas.portal.v1alpha1.DeviceManager.ListDeployments)` that indicates where this listing should continue from.  
`filter` |  `string` The filter expression. The filter should have the following format: "DIRECT_CHILDREN" or format: "direct_children". The filter is case insensitive. If empty, then no deployments are filtered.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListDeploymentsResponse](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/ListDeploymentsResponse)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
