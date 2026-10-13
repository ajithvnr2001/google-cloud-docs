---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/generate/
title: Method: projects.locations.spaces.applications.generate \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:14.059778+00:00
---

# Method: projects.locations.spaces.applications.generate  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.applications.generate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Generates Terraform files for an application.

### HTTP request

`POST https://designcenter.googleapis.com/v1/{name=projects/*/locations/*/spaces/*/applications/*}:generate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the application.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "iacFormat": enum ([IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/IACFormat)),
      "gcsUri": string,
      "artifactLocation": {
        object ([ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation))
      }
    }  
  
Fields  
---  
`iacFormat` |  `enum (`[IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/IACFormat)`)` Optional. The IaC format to generate.  
`gcsUri  
**(deprecated)**` |  `string` Optional. The Cloud Storage URI to write the generated IaC to. DEPRECATED: Use the 'artifactLocation' field instead.  
`artifactLocation` |  `object (`[ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation)`)` Optional. Specifies the destination for the generated IaC, which can be Cloud Storage or a Developer Connect repository.  
  
### Response body

If successful, the response body contains an instance of `[GenerateApplicationIaCResponse](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/GenerateApplicationIaCResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.applications.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
