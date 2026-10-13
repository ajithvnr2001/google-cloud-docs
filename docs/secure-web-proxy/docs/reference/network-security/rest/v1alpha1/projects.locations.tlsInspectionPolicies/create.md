---
url: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.tlsInspectionPolicies/create/
title: Method: projects.locations.tlsInspectionPolicies.create \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:44.851037+00:00
---

# Method: projects.locations.tlsInspectionPolicies.create  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.tlsInspectionPolicies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-web-proxy/docs/apis)



Send feedback 

#  Method: projects.locations.tlsInspectionPolicies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Creates a new TlsInspectionPolicy in a given project and location.

### HTTP request

`POST https://networksecurity.googleapis.com/v1alpha1/{parent=projects/*/locations/*}/tlsInspectionPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the TlsInspectionPolicy. Must be in the format `projects/{project}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networksecurity.tlsInspectionPolicies.create`

  
  
### Query parameters

Parameters  
---  
`tlsInspectionPolicyId` |  `string` Required. Short name of the TlsInspectionPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "tls_inspection_policy1". Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `tlsInspectionPolicyId`:

  * `networksecurity.tlsInspectionPolicies.create`

  
  
### Request body

The request body contains an instance of `[TlsInspectionPolicy](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/projects.locations.tlsInspectionPolicies#TlsInspectionPolicy)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
