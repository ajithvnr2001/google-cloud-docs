---
url: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates/revoke/
title: Method: projects.locations.certificateAuthorities.certificates.revoke \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:12.146162+00:00
---

# Method: projects.locations.certificateAuthorities.certificates.revoke  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates/revoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback 

#  Method: projects.locations.certificateAuthorities.certificates.revoke Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes



Revoke a `[Certificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates#Certificate)`.

### HTTP request

`POST https://privateca.googleapis.com/v1beta1/{name=projects/*/locations/*/certificateAuthorities/*/certificates/*}:revoke`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name for this `[Certificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates#Certificate)` in the format `projects/*/locations/*/certificateAuthorities/*/certificates/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `privateca.certificates.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "reason": enum ([RevocationReason](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/RevocationReason)),
      "requestId": string
    }  
  
Fields  
---  
`reason` |  `enum (`[RevocationReason](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/RevocationReason)`)` Required. The `[RevocationReason](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/RevocationReason)` for revoking this certificate.  
`requestId` |  `string` Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Response body

If successful, the response body contains an instance of `[Certificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities.certificates#Certificate)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
