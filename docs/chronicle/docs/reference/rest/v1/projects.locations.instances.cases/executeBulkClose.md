---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkClose/
title: Method: cases.executeBulkClose \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:59.850749+00:00
---

# Method: cases.executeBulkClose  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkClose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.executeBulkClose Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * DynamicParameters
    * JSON representation



**Full name** : projects.locations.instances.cases.executeBulkClose

Closes multiple cases in a single operation. A valid closure reason and root cause must be provided for all affected cases.

### HTTP request

`POST https://{endpoint}/v1/{parent}/cases:executeBulkClose`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to execute bulk close on. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "casesIds": [
        integer
      ],
      "closeReason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CloseReason)),
      "rootCause": string,
      "closeComment": string,
      "dynamicParameters": [
        {
          object ([DynamicParameters](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkClose#DynamicParameters))
        }
      ]
    }  
  
Fields  
---  
`casesIds[]` |  `integer` Required. Cases to close.  
`closeReason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CloseReason)`)` Required. Close reason.  
`rootCause` |  `string` Optional. Root cause of closing the cases.  
`closeComment` |  `string` Optional. Comment to add to the cases when closing them.  
`dynamicParameters[]` |  `object (`[DynamicParameters](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkClose#DynamicParameters)`)` Optional. Dynamic parameters added to the close case action.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.cases.close`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## DynamicParameters

Dynamic parameters added to the close case action.

JSON representation  
---  
      
    
    {
      "id": integer,
      "values": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `integer` Required. Id of the dynamic parameter used.  
`values[]` |  `string` Required. List of values given for the parameter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
