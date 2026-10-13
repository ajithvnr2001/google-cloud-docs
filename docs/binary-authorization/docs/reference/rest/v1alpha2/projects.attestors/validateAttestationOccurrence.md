---
url: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects.attestors/validateAttestationOccurrence/
title: Method: projects.attestors.validateAttestationOccurrence \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:45.800487+00:00
---

# Method: projects.attestors.validateAttestationOccurrence  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects.attestors/validateAttestationOccurrence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  Method: projects.attestors.validateAttestationOccurrence Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Returns whether the given `Attestation` for the given image URI was signed by the given `Attestor`

### HTTP request

`POST https://binaryauthorization.googleapis.com/v1alpha2/{attestor=projects/*/attestors/*}:validateAttestationOccurrence`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`attestor` |  `string` Required. The resource name of the `[Attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.attestors#Attestor)` of the [occurrence][grafeas.v1.Occurrence], in the format `projects/*/attestors/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `attestor`:

  * `binaryauthorization.attestors.verifyImageAttested`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "attestation": {
        object ([AttestationOccurrence](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/ValidateAttestationOccurrenceRequest#AttestationOccurrence))
      },
      "occurrenceNote": string,
      "occurrenceResourceUri": string
    }  
  
Fields  
---  
`attestation` |  `object (`[AttestationOccurrence](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/ValidateAttestationOccurrenceRequest#AttestationOccurrence)`)` Required. An `[AttestationOccurrence](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/ValidateAttestationOccurrenceRequest#AttestationOccurrence)` to be checked that it can be verified by the `Attestor`. It does not have to be an existing entity in Container Analysis. It must otherwise be a valid `AttestationOccurrence`.  
`occurrenceNote` |  `string` Required. The resource name of the [Note][grafeas.v1.Note] to which the containing [Occurrence][grafeas.v1.Occurrence] is associated.  
`occurrenceResourceUri` |  `string` Required. The URI of the artifact (e.g. container image) that is the subject of the containing [Occurrence][grafeas.v1.Occurrence].  
  
### Response body

If successful, the response body contains an instance of `[ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/ValidateAttestationOccurrenceResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
