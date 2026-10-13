---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes/generateEventTypesSuggestions/
title: Method: logTypes.generateEventTypesSuggestions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:29.173810+00:00
---

# Method: logTypes.generateEventTypesSuggestions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes/generateEventTypesSuggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: logTypes.generateEventTypesSuggestions Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * EventTypesSuggestion
    * JSON representation



**Full name** : projects.locations.instances.logTypes.generateEventTypesSuggestions

logTypes.generateEventTypesSuggestions generates event types suggestions that can be mapped by a lowcode parser.

### HTTP request

`POST https://{endpoint}/v1beta/{logtype}:generateEventTypesSuggestions`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`logtype` |  `string` Required. The logtype of a parser. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{logtype}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fieldExtractors": [
        {
          object ([FieldExtractor](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/FieldExtractors#FieldExtractor))
        }
      ]
    }  
  
Fields  
---  
`fieldExtractors[]` |  `object (`[FieldExtractor](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/FieldExtractors#FieldExtractor)`)` Field extractors of a low code parser.  
  
### Response body

Response message for GenerateEventTypesSuggestionsResponse.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "eventTypeSuggestions": [
        {
          object ([EventTypesSuggestion](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes/generateEventTypesSuggestions#EventTypesSuggestion))
        }
      ]
    }  
  
Fields  
---  
`eventTypeSuggestions[]` |  `object (`[EventTypesSuggestion](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes/generateEventTypesSuggestions#EventTypesSuggestion)`)` List of EventTypeSuggestions.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `logtype` resource:

  * `chronicle.parsers.generateEventTypesSuggestions`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## EventTypesSuggestion

A suggested event type and it's confidence value.

JSON representation  
---  
      
    
    {
      "eventType": enum ([EventType](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/EventType)),
      "confidenceValue": number
    }  
  
Fields  
---  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/EventType)`)` The suggested eventType.  
`confidenceValue` |  `number` Confidence value for respective eventType, value ranges from 0-1.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
