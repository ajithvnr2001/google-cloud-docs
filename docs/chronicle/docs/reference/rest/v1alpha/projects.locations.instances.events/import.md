---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events/import/
title: Method: events.import \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:43.669761+00:00
---

# Method: events.import  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: events.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * EventsInlineSource
    * JSON representation



**Full name** : projects.locations.instances.events.import

events.import import the events. Note that, All events need to be valid for the request to be successful. An error in one entity will cause the entire request to be rejected.

### HTTP request

`POST https://{endpoint}/v1alpha/{parent}/events:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of events.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object ([EventsInlineSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events/import#EventsInlineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`[EventsInlineSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events/import#EventsInlineSource)`)` Required. Events to be imported are specified inline.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.events.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## EventsInlineSource

An import source with the events to import included inline.

JSON representation  
---  
      
    
    {
      "events": [
        {
          object ([Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events#Event))
        }
      ]
    }  
  
Fields  
---  
`events[]` |  `object (`[Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.events#Event)`)` Required. The events being imported.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
