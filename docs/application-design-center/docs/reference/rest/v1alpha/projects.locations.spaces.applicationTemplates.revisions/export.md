---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/export/
title: Method: projects.locations.spaces.applicationTemplates.revisions.export \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:29.001471+00:00
---

# Method: projects.locations.spaces.applicationTemplates.revisions.export  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.applicationTemplates.revisions.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Exports Terraform files for an application template revision. The generated modules can have remote sources or local sources downloaded from remote. This is an ASYNCHRONOUS operation that returns a Long Running Operation.

### HTTP request

`POST https://designcenter.googleapis.com/v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}:export`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the application template revision.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "artifactLocation": {
        object (ArtifactLocation)
      },
      "exportIacConfig": {
        object ([ExportIaCConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/ExportIaCConfig))
      }
    }  
  
Fields  
---  
`artifactLocation` |  `object (`ArtifactLocation`)` Optional. Specifies the destination for the generated IaC, which can be Cloud Storage or a Developer Connect repository. Default is Google Cloud Storage.  
`exportIacConfig` |  `object (`[ExportIaCConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/ExportIaCConfig)`)` Optional. Configuration for exporting IaC.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.applicationTemplateRevisions.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
