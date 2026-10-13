---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/fetchAssessmentReport/
title: Method: projects.locations.spaces.sharedTemplates.revisions.fetchAssessmentReport \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.076548+00:00
---

# Method: projects.locations.spaces.sharedTemplates.revisions.fetchAssessmentReport  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/fetchAssessmentReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.sharedTemplates.revisions.fetchAssessmentReport Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetches the assessment report of a shared template revision if present.

### HTTP request

`GET https://designcenter.googleapis.com/v1/{name=projects/*/locations/*/spaces/*/sharedTemplates/*/revisions/*}:fetchAssessmentReport`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The shared template revision name in the following format: `projects/{project}/locations/{location}/spaces/{space}/sharedTemplates/{shared_template}/revisions/{revision}`  
  
### Request body

The request body must be empty.

### Response body

Response message for revisions.fetchAssessmentReport.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "assessmentReport": {
        object ([AssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport))
      }
    }  
  
Fields  
---  
`assessmentReport` |  `object (`[AssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/AssessmentReport)`)` Assessment report for the shared template revision.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.sharedTemplateRevisions.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
