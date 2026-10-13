---
url: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/enable/
title: Method: projects.locations.secrets.versions.enable \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:14.556951+00:00
---

# Method: projects.locations.secrets.versions.enable  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secret-manager/docs/apis)



Send feedback 

#  Method: projects.locations.secrets.versions.enable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Enables a `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`.

Sets the `[state](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion.FIELDS.state)` of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)` to `[ENABLED](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion.State.ENUM_VALUES.ENABLED)`.

### HTTP request

Choose a location:

me-central2 me-west1 us-central1 us-east1 us-central2 us-west1 us-west2 us-west3 us-west4 us-east4 us-east5 us-south1 europe-west3 europe-west8 europe-west9 europe-west6

  


The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)` to enable in the format `projects/*/locations/*/secrets/*/versions/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `secretmanager.secrets.enable`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "etag": string
    }  
  
Fields  
---  
`etag` |  `string` Optional. Etag of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`. The request succeeds if it matches the etag of the currently stored secret version object. If the etag is omitted, the request succeeds.  
  
### Response body

If successful, the response body contains an instance of `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
