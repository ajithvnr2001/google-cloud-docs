---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes/legacySubmitParserExtension/
title: Method: logTypes.legacySubmitParserExtension \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:12.779668+00:00
---

# Method: logTypes.legacySubmitParserExtension  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes/legacySubmitParserExtension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: logTypes.legacySubmitParserExtension Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.logTypes.legacySubmitParserExtension

logTypes.legacySubmitParserExtension creates validates and then makes the extension live.

### HTTP request

`POST https://{endpoint}/v1/{parent}:legacySubmitParserExtension`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this parser will be created. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{logtype}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "parserExtension": {
        object ([ParserExtension](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions#ParserExtension))
      }
    }  
  
Fields  
---  
`parserExtension` |  `object (`[ParserExtension](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions#ParserExtension)`)` Required. The parser extension to create.  
  
### Response body

If successful, the response body contains an instance of `[ParserExtension](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions#ParserExtension)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.parserExtensions.legacySubmitParserExtension`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
