---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyRemoveCategories/
title: Method: legacyPlaybooks.legacyRemoveCategories \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:34.461865+00:00
---

# Method: legacyPlaybooks.legacyRemoveCategories  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyRemoveCategories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyPlaybooks.legacyRemoveCategories Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ApiDeleteCategoryResult
    * JSON representation



**Full name** : projects.locations.instances.legacyPlaybooks.legacyRemoveCategories

Removes multiple playbook categories in a single operation.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacyPlaybooks:legacyRemoveCategories`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to remove the categories for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ids": [
        string
      ]
    }  
  
Fields  
---  
`ids[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The ids of the categories to remove.  
  
### Response body

LegacyPlaybookRemoveCategoriesResponse is a response for removing categories.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deletedCategories": [
        {
          object ([ApiDeleteCategoryResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyRemoveCategories#ApiDeleteCategoryResult))
        }
      ],
      "deletedPlaybooks": [
        {
          object ([ApiDeleteWorkflowResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiDeleteWorkflowResult))
        }
      ]
    }  
  
Fields  
---  
`deletedCategories[]` |  `object (`[ApiDeleteCategoryResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyPlaybooks/legacyRemoveCategories#ApiDeleteCategoryResult)`)` Optional. The removed categories.  
`deletedPlaybooks[]` |  `object (`[ApiDeleteWorkflowResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ApiDeleteWorkflowResult)`)` Optional. The removed playbooks.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacyPlaybooks.delete`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ApiDeleteCategoryResult

Api result for deletion of categories

JSON representation  
---  
      
    
    {
      "id": string,
      "errorMessage": string,
      "failed": boolean
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Id of category  
`errorMessage` |  `string` Optional. Any error messages associated with the call  
`failed` |  `boolean` Required. Flag indicating whether it was successful or error  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
