---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateThreatDetectionOpportunity/
title: Method: instances.generateThreatDetectionOpportunity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:12.596065+00:00
---

# Method: instances.generateThreatDetectionOpportunity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/generateThreatDetectionOpportunity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.generateThreatDetectionOpportunity Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes



**Full name** : projects.locations.instances.generateThreatDetectionOpportunity

instances.generateThreatDetectionOpportunity generates a Threat Detection Opportunity (TDO).

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}:generateThreatDetectionOpportunity`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The Chronicle instance associated with the Threat Detection Opportunity. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "threat": string
    }  
  
Fields  
---  
`threat` |  `string` Required. The threat to generate a Threat Detection Opportunity for - free-form user input.  
  
### Response body

Response message for instances.generateThreatDetectionOpportunity.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instance": string,
      "threatDetectionOpportunities": [
        {
          object ([ThreatDetectionOpportunity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ThreatDetectionOpportunity))
        }
      ]
    }  
  
Fields  
---  
`instance` |  `string` The Chronicle instance associated with the Threat Detection Opportunity. Format: projects/{project}/locations/{location}/instances/{instance}  
`threatDetectionOpportunities[]` |  `object (`[ThreatDetectionOpportunity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ThreatDetectionOpportunity)`)` The generated Threat Detection Opportunities.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
