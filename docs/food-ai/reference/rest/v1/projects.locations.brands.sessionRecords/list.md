---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/list/
title: Method: projects.locations.brands.sessionRecords.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:25.573237+00:00
---

# Method: projects.locations.brands.sessionRecords.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.sessionRecords.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists SessionRecords for a given brand.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/sessionRecords`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The brand to list order sessions for. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of session records to return. The service may return fewer than this value. If unspecified, at most 50 sessions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `sessionRecords.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160. This field allows filtering session records based on various attributes.Supported Filter Fields:

  * session_id (String): The ID of the session. Operators: = Example: `session_id = "session-123"`
  * storeId (String): The ID of the store. Operators: =, != Example: `storeId = "store-123"`
  * storeIds (String): A comma-separated list of store IDs. Operators: =, !=, : Example: `storeIds = "store-123,store-456"`
  * sessionStartTime (Timestamp): The start time of the session. Timestamps expect an RFC-3339 formatted string (e.g. 2012-04-21T11:30:00-04:00). UTC offsets are supported Operators: =, !=,

> , >=, <, <= Example: `sessionStartTime >= "2025-10-01T00:00:00Z"`

  * outcomeLabel (String): The final outcome label of the session. Operators: =, != Example: `outcomeLabel = "SUCCESS"`
  * outcomeGroupLabel (String): The group label for the session outcome. Operators: =, != Example: `outcomeGroupLabel = "SUCCESS"`
  * predictedFailureCategory (String): The predicted failure category for the session from the intervention analysis. Operators: =, != Example: `predictedFailureCategory = "Menu"`
  * agent_utterances (String): Text spoken by the agent. Operator: : (HAS token/Full Text Search) Example: `agent_utterances:"anything else"`
  * user_utterances (String): Text spoken by the user. Operator: : (HAS token/Full Text Search) Example: `user_utterances:"burger"`

Logical Operators:Conditions can be combined using `AND`, `OR`, and `NOT`. Parentheses `()` can be used to group expressions to control the order of evaluation. Example: `(user_utterances:"help" OR agent_utterances:"issue") AND storeId != "test-store"` Example: `user_utterances:"order" AND sessionStartTime >= "2025-10-03T00:00:00Z"`  
  
### Request body

The request body must be empty.

### Response body

Response message for [SessionRecordService.ListSessionRecords][].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessionRecords": [
        {
          object ([SessionRecord](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#SessionRecord))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`sessionRecords[]` |  `object (`[SessionRecord](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#SessionRecord)`)` The list of session records.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
