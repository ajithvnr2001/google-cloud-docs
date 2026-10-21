---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/projects.locations/signSshPublicKey/
title: Method: projects.locations.signSshPublicKey \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:08.772839+00:00
---

# Method: projects.locations.signSshPublicKey  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/projects.locations/signSshPublicKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.signSshPublicKey Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Signs an SSH public key for a user to authenticate to a virtual machine on Google Compute Engine.

### HTTP request

`POST https://oslogin.googleapis.com/v1beta/{parent=projects/*/locations/*}:signSshPublicKey`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent for the signing request. Format: projects/{project}/locations/{location}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sshPublicKey": string,
      "serviceAccount": string,
    
      // Union field resource can be only one of the following:
      "computeInstance": string,
      "appEngineInstance": string,
      "cloudRunResource": string
      // End of list of possible types for union field resource.
    }  
  
Fields  
---  
`sshPublicKey` |  `string` Required. The SSH public key to sign.  
`serviceAccount` |  `string` Optional. The service account for the instance. If the instance in question does not have a service account, this field should be left empty. If the wrong service account is provided, this operation will return a signed certificate that will not be accepted by the VM.  
Union field `resource`. Required. The resource to sign the SSH public key for. Signed SSH public keys are scoped to a specific resource; attempting to use them to sign into another resource will fail. During rollout of the new regionalized SignSshPublicKey API, this field will be required for all requests, but the VM will not initially carry out the verification of this resource unless it updates to a package that supports this feature. `resource` can be only one of the following:  
`computeInstance` |  `string` The Compute instance to sign the SSH public key for. Expected format: projects/{project}/zones/{zone}/instances/{numericInstanceId}  
`appEngineInstance` |  `string` The App Engine instance to sign the SSH public key for. Expected format: apps/{app}/services/{service}/versions/{version}/instances/{instance}  
`cloudRunResource` |  `string` Optional. The Cloud Run resource to sign the SSH public key for.Expected formats: - `projects/{project}/locations/{location}/services/{service}` \- `projects/{project}/locations/{location}/workerPools/{worker_pool}` \- `projects/{project}/locations/{location}/jobs/{job}` \- `projects/{project}/locations/{location}/instances/{instance}`  
  
### Response body

The response message for signing an SSH public key.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "signedSshPublicKey": string
    }  
  
Fields  
---  
`signedSshPublicKey` |  `string` The signed SSH public key to use in the SSH handshake.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
