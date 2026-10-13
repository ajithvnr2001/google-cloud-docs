---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/registerDeployedResources/
title: Method: projects.locations.spaces.registerDeployedResources \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:24.384123+00:00
---

# Method: projects.locations.spaces.registerDeployedResources  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/registerDeployedResources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.registerDeployedResources Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Register deployed resources from terraform state file with App Hub.

### HTTP request

`POST https://designcenter.googleapis.com/v1alpha/{parent=projects/*/locations/*/spaces/*}:registerDeployedResources`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent space. Format: projects/{project}/locations/{location}/spaces/{space}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "apphubApplication": string,
      "serviceAccount": string,
    
      // Union field tfstate_source can be only one of the following:
      "terraformState": string,
      "tfstateSignedGcsUri": string
      // End of list of possible types for union field tfstate_source.
    }  
  
Fields  
---  
`apphubApplication` |  `string` Required. The name of the AppHub Application. Format: projects/{project}/locations/{location}/applications/{application}  
`serviceAccount` |  `string` Optional. The optional Service Account (SA) to use for calling AppHub APIs during registration. If not provided, the End-User Credentials (EUC) will be used. If provided, the EUC must have the 'serviceAccountTokenCreator' role on the SA, and the SA must have the necessary permissions for AppHub registration.  
Union field `tfstate_source`. The Terraform state (tfstate) source. `tfstate_source` can be only one of the following:  
`terraformState` |  `string` The Terraform state (tfstate) content as a raw string. For large state files exceeding 10MB, use the 'tfstateSignedGcsUri' field instead.  
`tfstateSignedGcsUri` |  `string` A securely signed Cloud Storage URI pointing to the tfstate file. The URI must be signed to grant the service temporary read access to the state file. Application Design Center imposes a limit on the maximum size of the state file accessed via this URI.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `designcenter.spaces.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
