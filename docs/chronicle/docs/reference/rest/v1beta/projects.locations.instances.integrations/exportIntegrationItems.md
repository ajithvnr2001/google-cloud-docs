---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations/exportIntegrationItems/
title: Method: integrations.exportIntegrationItems \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:32.567138+00:00
---

# Method: integrations.exportIntegrationItems  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations/exportIntegrationItems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: integrations.exportIntegrationItems Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.integrations.exportIntegrationItems

Exports specific items from an integration into a ZIP folder. Use this method to extract only a subset of capabilities (e.g., just the connectors) for reuse.

### HTTP request

`GET https://{endpoint}/v1beta/{name}:exportItems`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the integration to retrieve items from. Format: projects/{project}/locations/{region}/instances/{instance}/integrations/{integration}  
  
### Query parameters

Parameters  
---  
`actions` |  `string` Optional. A separated comma string of the ids of the actions to export. Format: 1,2,3  
`jobs` |  `string` Optional. A separated comma string of the ids of the jobs to export. Format: 1,2,3  
`connectors` |  `string` Optional. A separated comma string of the ids of the connectors to export. Format: 1,2,3  
`managers` |  `string` Optional. A separated comma string of the ids of the managers to export. Format: 1,2,3  
`transformers` |  `string` Optional. A separated comma string of the ids of the transformers to export. Format: 1,2,3  
`logicalOperators` |  `string` Optional. A separated comma string of the ids of the logical operators to export. Format: 1,2,3  
  
### Request body

The request body must be empty.

### Response body

Zipped folder with all the exported items. Includes the following folders according to the chosen items: Actions, Connectors, Jobs, Managers Each folder includes json files and a python file for the script.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "media": {
        object ([Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media))
      }
    }  
  
Fields  
---  
`media` |  `object (`[Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media)`)` Information representing the exported data. Information representing the imported data  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.integrations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
