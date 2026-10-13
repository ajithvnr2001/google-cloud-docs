---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/generateTerraformPlanAssessmentReport/
title: Method: projects.locations.spaces.generateTerraformPlanAssessmentReport \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:23.169467+00:00
---

# Method: projects.locations.spaces.generateTerraformPlanAssessmentReport  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/generateTerraformPlanAssessmentReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.generateTerraformPlanAssessmentReport Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Generate a Terraform plan assessment report for a given Terraform plan.

### HTTP request

`POST https://designcenter.googleapis.com/v1alpha/{name=projects/*/locations/*/spaces/*}:generateTerraformPlanAssessmentReport`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The parent resource in which to generate the assessment report. Format: projects/$project/locations/$location/spaces/$space  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "terraformPlan": string,
      "additionalFrameworks": [
        string
      ]
    }  
  
Fields  
---  
`terraformPlan` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The raw JSON representation of the generated Terraform plan, provided as bytes.A base64-encoded string.  
`additionalFrameworks[]` |  `string` Optional. Additional frameworks to run assessment against. If empty, run against default frameworks. Frameworks refers to the policies.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
