---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateRules/
title: Method: instances.generateRules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:26.983019+00:00
---

# Method: instances.generateRules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateRules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.generateRules Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * GeneratedRule
    * JSON representation



**Full name** : projects.locations.instances.generateRules

Generates a proposed rule given an input Threat Detection Opportunity (TDO).

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}:generateRules`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The Chronicle instance associated with the request. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "threatDetectionOpportunity": {
        object ([ThreatDetectionOpportunity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ThreatDetectionOpportunity))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The originating artifacts that should be used to generate a rule. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`threatDetectionOpportunity` |  `object (`[ThreatDetectionOpportunity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ThreatDetectionOpportunity)`)` The input ThreatDetectionOpportunity to generate a rule from. In the case of the Detection Engineering Agent, this is created by calling the GenerateDetectionOpportunity tool.  
End of mutually exclusive fields.  
  
### Response body

Response message for instances.generateRules.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instance": string,
      "generatedRules": [
        {
          object ([GeneratedRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateRules#GeneratedRule))
        }
      ]
    }  
  
Fields  
---  
`instance` |  `string` The Chronicle instance associated with the Threat Detection Opportunity. Format: projects/{project}/locations/{location}/instances/{instance}  
`generatedRules[]` |  `object (`[GeneratedRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateRules#GeneratedRule)`)` The generated Rules.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## GeneratedRule

A generated Rule.

JSON representation  
---  
      
    
    {
      "ruleText": string,
      "feedbackId": string
    }  
  
Fields  
---  
`ruleText` |  `string` The core YARA-L text for the generated Rule.  
`feedbackId` |  `string` The ID of the feedback report.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
