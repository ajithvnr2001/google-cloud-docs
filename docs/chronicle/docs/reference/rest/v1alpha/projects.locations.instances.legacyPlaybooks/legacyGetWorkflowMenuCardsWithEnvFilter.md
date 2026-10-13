---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowMenuCardsWithEnvFilter/
title: Method: legacyPlaybooks.legacyGetWorkflowMenuCardsWithEnvFilter \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:17.119967+00:00
---

# Method: legacyPlaybooks.legacyGetWorkflowMenuCardsWithEnvFilter  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowMenuCardsWithEnvFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyPlaybooks.legacyGetWorkflowMenuCardsWithEnvFilter Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * PlaybookType



**Full name** : projects.locations.instances.legacyPlaybooks.legacyGetWorkflowMenuCardsWithEnvFilter

Returns a list of available playbook definitions, specifically filtered by the environments the user has permission to access.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacyPlaybooks:legacyGetWorkflowMenuCardsWithEnvFilter`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to get the workflows that contains action for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "legacyPayload": [
        enum ([PlaybookType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowMenuCardsWithEnvFilter#PlaybookType))
      ]
    }  
  
Fields  
---  
`legacyPayload[]` |  `enum (`[PlaybookType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyGetWorkflowMenuCardsWithEnvFilter#PlaybookType)`)` Required. Playbook types to filter the workflow menu cards by.  
  
### Response body

LegacyPlaybookGetWorkflowMenuCardsWithEnvFilterResponse is a response for getting the workflows that contains action.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": [
        {
          object ([ApiWorkflowMenuCardDefinitionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiWorkflowMenuCardDefinitionDataModel))
        }
      ]
    }  
  
Fields  
---  
`payload[]` |  `object (`[ApiWorkflowMenuCardDefinitionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiWorkflowMenuCardDefinitionDataModel)`)` Optional. The workflow menu cards.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacyPlaybooks.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## PlaybookType

Playbook types to filter the workflow menu cards by.

Enums  
---  
`PLAYBOOK_TYPE_UNSPECIFIED` | Unspecified playbook type.  
`REGULAR` | Regular playbook type.  
`NESTED` | Nested playbook type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
