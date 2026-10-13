---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC/
title: Method: projects.locations.spaces.applications.importIaC \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:30.676391+00:00
---

# Method: projects.locations.spaces.applications.importIaC  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.applications.importIaC Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * State
  * Try it!



Imports IaC for an application resource.

### HTTP request

`POST https://designcenter.googleapis.com/v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:importIaC`

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
      "allowPartialImport": boolean,
      "validateIac": boolean,
    
      // Union field source can be only one of the following:
      "gcsUri": string,
      "iacModule": {
        object (IaCModule)
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`allowPartialImport` |  `boolean` Optional. If set to true, partially imports the valid edits in the IaC and ignores the invalid changes. Defaults to false, which means any edits which can't be imported must result in an error.  
`validateIac` |  `boolean` Optional. If set to true, the IaC is validated against the golden terraform without importing. Defaults to false.  
Union field `source`. The source location of terraform code. `source` can be only one of the following:  
`gcsUri` |  `string` Optional. The Cloud Storage URI of the terraform code.  
`iacModule` |  `object (`IaCModule`)` Optional. The IaC module to import.  
  
### Response body

Response message for applications.importIaC method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "application": {
        object (Application)
      },
      "errors": [
        {
          object (ImportIaCError)
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC#State))
    }  
  
Fields  
---  
`application` |  `object (`Application`)` Application template corresponding to the imported IaC.  
`errors[]` |  `object (`ImportIaCError`)` Errors encountered during import.  
`state` |  `enum (`[State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC#State)`)` The state of the import.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.applications.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## State

State of Import.

Enums  
---  
`STATE_UNSPECIFIED` | Default.  
`SUCCEEDED` | The import was successful.  
`FAILED` | The import failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
