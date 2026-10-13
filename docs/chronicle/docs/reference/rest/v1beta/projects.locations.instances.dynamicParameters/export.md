---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dynamicParameters/export/
title: Method: dynamicParameters.export \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:40.804157+00:00
---

# Method: dynamicParameters.export  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dynamicParameters/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: dynamicParameters.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



**Full name** : projects.locations.instances.dynamicParameters.export

Exports all DynamicParameters defined in the instance to a CSV file. Use this method to share classification rules across SecOps instances.

### HTTP request

`POST https://{endpoint}/v1beta/{parent}/dynamicParameters:export`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Format: projects/{project}/locations/{location}/instances/{instance}/dynamicParameters:export  
  
### Request body

The request body must be empty.

### Response body

Response message for dynamicParameters.export.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fileContents": string,
      "contentType": string
    }  
  
Fields  
---  
`fileContents` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The content of the dynamic parameters CSV file.A base64-encoded string.  
`contentType` |  `string` Output only. The content type of the report.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
