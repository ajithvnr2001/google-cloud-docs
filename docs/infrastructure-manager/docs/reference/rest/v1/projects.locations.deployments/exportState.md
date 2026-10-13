---
url: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments/exportState/
title: Method: projects.locations.deployments.exportState \u00a0|\u00a0 Infrastructure\u00a0Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:14.899949+00:00
---

# Method: projects.locations.deployments.exportState  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments/exportState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager)
  * [ Reference ](https://docs.cloud.google.com/infrastructure-manager/docs/apis)



Send feedback 

#  Method: projects.locations.deployments.exportState Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Exports Terraform state file from a given deployment.

### HTTP request

`POST https://config.googleapis.com/v1/{parent=projects/*/locations/*/deployments/*}:exportState`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent in whose context the statefile is listed. The parent value is in the format: 'projects/{projectId}/locations/{location}/deployments/{deployment}'. It takes the form `projects/{project}/locations/{location}/deployments/{deployment}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "draft": boolean
    }  
  
Fields  
---  
`draft` |  `boolean` Optional. If this flag is set to true, the exported deployment state file will be the draft state. This will enable the draft file to be validated before copying it over to the working state on unlock.  
  
### Response body

If successful, the response body contains an instance of `[Statefile](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/Statefile)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `config.googleapis.com/config.deployments.getState`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
