---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/fetchTemplate/
title: Method: managers.fetchTemplate \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:05.224176+00:00
---

# Method: managers.fetchTemplate  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/fetchTemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: managers.fetchTemplate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.integrations.managers.fetchTemplate

Returns a default recommended Python script template for an integration manager. Use this method to quickly start developing new managers.

### HTTP request

`GET https://{endpoint}/v1/{parent}/managers:fetchTemplate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The integration to fetch the template for. Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}  
  
### Request body

The request body must be empty.

### Response body

The response message for managers.fetchTemplate.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "template": {
        object ([IntegrationManager](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers#IntegrationManager))
      }
    }  
  
Fields  
---  
`template` |  `object (`[IntegrationManager](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers#IntegrationManager)`)` Output only. The manager definition template.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.managers.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
