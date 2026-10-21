---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/rejoin/
title: Method: projects.locations.catalogs.userEvents.rejoin \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:34:57.006930+00:00
---

# Method: projects.locations.catalogs.userEvents.rejoin  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/rejoin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.userEvents.rejoin Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * UserEventRejoinScope
  * Try it!



Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent catalog resource name, such as `projects/1234/locations/global/catalogs/default_catalog`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userEventRejoinScope": enum ([UserEventRejoinScope](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/rejoin#UserEventRejoinScope))
    }  
  
Fields  
---  
`userEventRejoinScope` |  `enum (`[UserEventRejoinScope](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents/rejoin#UserEventRejoinScope)`)` The type of the user event rejoin to define the scope and range of the user events to be rejoined with the latest product catalog. Defaults to `USER_EVENT_REJOIN_SCOPE_UNSPECIFIED` if this field is not set, or set to an invalid integer value.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `retail.userEvents.rejoin`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UserEventRejoinScope

The scope of user events to be rejoined with the latest product catalog. If the rejoining aims at reducing number of unjoined events, set `UserEventRejoinScope` to `UNJOINED_EVENTS`. If the rejoining aims at correcting product catalog information in joined events, set `UserEventRejoinScope` to `JOINED_EVENTS`. If all events needs to be rejoined, set `UserEventRejoinScope` to `USER_EVENT_REJOIN_SCOPE_UNSPECIFIED`.

Enums  
---  
`USER_EVENT_REJOIN_SCOPE_UNSPECIFIED` | Rejoin all events with the latest product catalog, including both joined events and unjoined events.  
`JOINED_EVENTS` | Only rejoin joined events with the latest product catalog.  
`UNJOINED_EVENTS` | Only rejoin unjoined events with the latest product catalog.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
