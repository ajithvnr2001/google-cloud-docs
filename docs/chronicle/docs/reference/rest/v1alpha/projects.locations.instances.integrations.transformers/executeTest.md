---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.transformers/executeTest/
title: Method: transformers.executeTest \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:15.174351+00:00
---

# Method: transformers.executeTest  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.transformers/executeTest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: transformers.executeTest Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.integrations.transformers.executeTest

Executes a test run of a transformer's Python script. Use this method to verify transformation logic and ensure data is being parsed and formatted correctly before saving or deploying the transformer.

### HTTP request

`POST https://{endpoint}/v1alpha/{integration}/transformers:executeTest`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`integration` |  `string` Required. The parent identifier (from route) Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transformer": {
        object ([TransformerDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.transformers#TransformerDefinition))
      }
    }  
  
Fields  
---  
`transformer` |  `object (`[TransformerDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.transformers#TransformerDefinition)`)` Required. The transformer to test The full transformer is needed as there is an option to run the test without saving the transformer first.  
  
### Response body

Response message for ExecuteTest.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "outputMessage": string,
      "debugOutputMessage": string,
      "resultValue": string
    }  
  
Fields  
---  
`outputMessage` |  `string` Output only. Human-readable output message set by the script.  
`debugOutputMessage` |  `string` Output only. The script debug output.  
`resultValue` |  `string` Output only. The script result value.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `integration` resource:

  * `chronicle.transformerDefinitions.execute`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
