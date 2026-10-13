---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags/
title: Method: projects.locations.observationJobs.apiObservations.batchEditTags \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:51.105973+00:00
---

# Method: projects.locations.observationJobs.apiObservations.batchEditTags  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: projects.locations.observationJobs.apiObservations.batchEditTags Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * EditTagsApiObservationsRequest
    * JSON representation
  * TagAction
    * JSON representation
  * Action



apiObservations.batchEditTags adds or removes Tags for ApiObservations.

### HTTP request

`POST https://apim.googleapis.com/v1alpha/{parent=projects/*/locations/*/observationJobs/*}/apiObservations:batchEditTags`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all ApiObservations being edited. Format: projects/{project}/locations/{location}/observationJobs/{observationJob}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([EditTagsApiObservationsRequest](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#EditTagsApiObservationsRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[EditTagsApiObservationsRequest](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#EditTagsApiObservationsRequest)`)` Required. The request message specifying the resources to update. A maximum of 1000 apiObservations can be modified in a batch.  
  
### Response body

Message for response to edit Tags for ApiObservations

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "apiObservations": [
        {
          object ([ApiObservation](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations#ApiObservation))
        }
      ]
    }  
  
Fields  
---  
`apiObservations[]` |  `object (`[ApiObservation](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations#ApiObservation)`)` ApiObservations that were changed  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `apim.apiObservations.batchEditTags`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## EditTagsApiObservationsRequest

Message for requesting edit tags for ApiObservation

JSON representation  
---  
      
    
    {
      "apiObservationId": string,
      "tagActions": [
        {
          object ([TagAction](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#TagAction))
        }
      ]
    }  
  
Fields  
---  
`apiObservationId` |  `string` Required. Identifier of ApiObservation need to be edit tags Format example: "apigee.googleapis.com|us-west1|443"  
`tagActions[]` |  `object (`[TagAction](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#TagAction)`)` Required. Tag actions to be applied  
  
## TagAction

Message for edit tag action

JSON representation  
---  
      
    
    {
      "tag": string,
      "action": enum ([Action](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#Action))
    }  
  
Fields  
---  
`tag` |  `string` Required. Tag to be added or removed  
`action` |  `enum (`[Action](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags#Action)`)` Required. Action to be applied  
  
## Action

The type of action performed on a tag in a TagAction.

Enums  
---  
`ACTION_UNSPECIFIED` | Unspecified.  
`ADD` | Addition of a Tag.  
`REMOVE` | Removal of a Tag.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
