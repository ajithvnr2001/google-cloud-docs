---
url: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions/access/
title: Method: projects.secrets.versions.access \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:11.974315+00:00
---

# Method: projects.secrets.versions.access  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secret-manager/docs/apis)



Send feedback 

#  Method: projects.secrets.versions.access Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Accesses a `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions#SecretVersion)`. This call returns the secret data.

`projects/*/secrets/*/versions/latest` is an alias to the `latest` `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions#SecretVersion)`.

### HTTP request

`GET https://secretmanager.googleapis.com/v1beta1/{name=projects/*/secrets/*/versions/*}:access`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions#SecretVersion)` in the format `projects/*/secrets/*/versions/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `secretmanager.versions.access`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `[SecretManagerService.AccessSecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions/access#google.cloud.secrets.v1beta1.SecretManagerService.AccessSecretVersion)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "payload": {
        object ([SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/SecretPayload))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions#SecretVersion)` in the format `projects/*/secrets/*/versions/*`.  
`payload` |  `object (`[SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1beta1/SecretPayload)`)` Secret payload  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
