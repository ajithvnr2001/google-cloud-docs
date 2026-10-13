---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyRuleText/
title: Method: instances.verifyRuleText \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:31.292158+00:00
---

# Method: instances.verifyRuleText  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyRuleText/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.verifyRuleText Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.verifyRuleText

Verifies the given rule text.

### HTTP request

`POST https://{endpoint}/v1/{instance}:verifyRuleText`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance associated with the request. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ruleText": string
    }  
  
Fields  
---  
`ruleText` |  `string` Required. The rule text to verify as a UTF-8 string.  
  
### Response body

Response message for instances.verifyRuleText method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "success": boolean,
      "compilationDiagnostics": [
        {
          object ([CompilationDiagnostic](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#CompilationDiagnostic))
        }
      ],
      "allowedRunFrequencies": [
        enum ([RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#RunFrequency))
      ],
      "nearRealTimeLiveRuleEligible": boolean,
      "inputsUsed": {
        object ([InputsUsed](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#InputsUsed))
      }
    }  
  
Fields  
---  
`success` |  `boolean` Whether or not the rule text was successfully verified.  
`compilationDiagnostics[]` |  `object (`[CompilationDiagnostic](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#CompilationDiagnostic)`)` A list of a rule's corresponding compilation diagnostic messages such as compilation errors and compilation warnings.  
`allowedRunFrequencies[]` |  `enum (`[RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#RunFrequency)`)` The run frequencies that are allowed for the rule.  
`nearRealTimeLiveRuleEligible` |  `boolean` Indicates whether the rule can run as a near real-time live rule. If this is true, the rule runs as a near real-time live rule when the run frequency is set to LIVE.  
`inputsUsed` |  `object (`[InputsUsed](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules#InputsUsed)`)` Optional. The sources of events (if any) used in the rule.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.rules.verifyRuleText`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
