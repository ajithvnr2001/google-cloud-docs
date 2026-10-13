---
url: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/organizations.locations.operations/delete/
title: Method: organizations.locations.operations.delete \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:15.779117+00:00
---

# Method: organizations.locations.operations.delete  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1alpha1/organizations.locations.operations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-web-proxy/docs/apis)



Send feedback 

#  Method: organizations.locations.operations.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

### HTTP request

`DELETE https://networksecurity.googleapis.com/v1alpha1/{name=organizations/*/locations/*/operations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the operation resource to be deleted.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
