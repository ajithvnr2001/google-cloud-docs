---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowInstance/
title: Method: legacyPlaybooks.legacyGetWorkflowInstance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:46.404399+00:00
---

# Method: legacyPlaybooks.legacyGetWorkflowInstance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowInstance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyPlaybooks.legacyGetWorkflowInstance Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.legacyPlaybooks.legacyGetWorkflowInstance

Returns the specific runtime instance (either completed or pending) of a playbook associated with a given alert.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacyPlaybooks:legacyGetWorkflowInstance`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to get the workflow instance for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseId": string,
      "alertIdentifier": string,
      "definitionIdentifier": string,
      "nestedStepIdentifier": string,
      "parentWorkflowInstanceId": string,
      "loopsRequestedIterations": [
        {
          object ([ApiLoopIterationRequest](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiLoopIterationRequest))
        }
      ],
      "parentWorkflowLoopIteration": integer,
      "shouldFetchSteps": boolean,
      "collapseBlocks": boolean
    }  
  
Fields  
---  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The case id.  
`alertIdentifier` |  `string` Optional. The alert identifier.  
`definitionIdentifier` |  `string` Required. The definition identifier.  
`nestedStepIdentifier` |  `string` Optional. The nested step identifier.  
`parentWorkflowInstanceId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The parent workflow instance id.  
`loopsRequestedIterations[]` |  `object (`[ApiLoopIterationRequest](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiLoopIterationRequest)`)` Optional. The loops requested iterations.  
`parentWorkflowLoopIteration` |  `integer` Optional. The parent workflow loop iteration.  
`shouldFetchSteps` |  `boolean` Optional. Indicates if the steps should be fetched.  
`collapseBlocks` |  `boolean` Optional. Indicates if the blocks should be collapsed.  
  
### Response body

If successful, the response body contains an instance of `[ApiWorkflowInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiWorkflowInstanceDataModel)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacyPlaybooks.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
