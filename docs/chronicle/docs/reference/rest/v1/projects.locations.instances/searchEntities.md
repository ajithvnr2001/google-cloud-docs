---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/searchEntities/
title: Method: instances.searchEntities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:25.964991+00:00
---

# Method: instances.searchEntities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/searchEntities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.searchEntities Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.searchEntities

Identifies the entity type and retrieves relevant data associated with a specified indicator. The API returns a maximum of 1000 entities.

### HTTP request

`GET https://{endpoint}/v1/{instance}:searchEntities`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The ID of the Instance to search entities for. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Query parameters

Parameters  
---  
`indicator` |  `string` Required. Value of indicator tied to an entity.  
  
### Request body

The request body must be empty.

### Response body

Response message for search entities.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity))
        }
      ]
    }  
  
Fields  
---  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities#Entity)`)` A list of entities.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.entities.searchEntities`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
