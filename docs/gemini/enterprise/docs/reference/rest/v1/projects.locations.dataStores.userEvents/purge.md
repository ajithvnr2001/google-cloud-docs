---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents/purge/
title: Method: projects.locations.dataStores.userEvents.purge \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:54.425531+00:00
---

# Method: projects.locations.dataStores.userEvents.purge  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents/purge/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.userEvents.purge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the catalog under which the events are created. The format is `projects/{project}/locations/global/collections/{collection}/dataStores/{dataStore}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "force": boolean
    }  
  
Fields  
---  
`filter` |  `string` Required. The filter string to specify the events to be deleted with a length limit of 5,000 characters. The eligible fields for filtering are:

  * `eventType`: Double quoted `[UserEvent.event_type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.event_type)` string.
  * `eventTime`: in ISO 8601 "zulu" format.
  * `userPseudoId`: Double quoted string. Specifying this will delete all events associated with a visitor.
  * `userId`: Double quoted string. Specifying this will delete all events associated with a user.

Note: This API only supports purging a max range of 30 days.Examples:

  * Deleting all events in a time range: `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"`
  * Deleting specific eventType in a time range: `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z" eventType = "search"`
  * Deleting all events for a specific visitor in a time range: `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z" userPseudoId = "visitor1024"`
  * Deleting the past 30 days of events inside a DataStore: `*`

The filtering fields are assumed to have an implicit AND.  
`force` |  `boolean` The `force` field is currently not supported. Purge user event requests will permanently delete all purgeable events. Once the development is complete: If `force` is set to false, the method will return the expected purge count without deleting any user events. This field will default to false if not included in the request.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.userEvents.purge`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
