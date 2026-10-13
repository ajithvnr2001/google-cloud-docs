---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries
title: REST Resource: projects.locations.instances.users.searchQueries \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:24.347399+00:00
---

# REST Resource: projects.locations.instances.users.searchQueries  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.users.searchQueries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SearchQuery
    * JSON representation
  * QueryType
  * QueryLanguage
  * Methods



## Resource: SearchQuery

Represents a Search Query from a Chronicle user.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        object ([EntryMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntryMetadata))
      },
      "displayName": string,
      "query": string,
      "queryId": string,
      "userId": string,
      "description": string,
      "placeholderNames": [
        string
      ],
      "placeholderDescriptions": [
        string
      ],
      "queryType": enum ([QueryType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryType)),
      "naturalLanguageQuery": string,
      "caseInsensitive": boolean,
      "columnSetLabel": string,
      "queryLanguage": enum ([QueryLanguage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryLanguage))
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the SearchQuery.  
`metadata` |  `object (`[EntryMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntryMetadata)`)` Optional. Metadata about the search query.  
`displayName` |  `string` Optional. Name of the query to be shown in the UI.  
`query` |  `string` Required. The query the user is saving.  
`queryId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The 16 byte UUID for this query.A base64-encoded string.  
`userId` |  `string` Optional. The user ID for this query.  
`description` |  `string` Optional. Description of the overall query, to be shown in the UI.  
`placeholderNames[]` |  `string` Optional. Name of query placeholder value, to be shown in the UI. Each element's position corresponds to the description in the placeholderDescriptions field.  
`placeholderDescriptions[]` |  `string` Optional. Description of the placeholder value, to be shown in the UI.  
`queryType` |  `enum (`[QueryType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryType)`)` Optional. The query type.  
`naturalLanguageQuery` |  `string` Optional. If applicable, the natural language query used to generate the UDM Search Query.  
`caseInsensitive` |  `boolean` Optional. If true, the search was performed in a case-insensitive manner.  
`columnSetLabel` |  `string` Optional. The label of the column set added to the search query. `columnSetLabel` maps to the `columnSets` field in the `PreferenceSet` resource.  
`queryLanguage` |  `enum (`[QueryLanguage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryLanguage)`)` Optional. The query language.  
  
## QueryType

The type of the query in the request.

Enums  
---  
`QUERY_TYPE_UNSPECIFIED` | The default query type.  
`QUERY_TYPE_UDM_QUERY` | Unified Data Model Query.  
`QUERY_TYPE_RAW_LOG_QUERY` | Raw Log Query.  
`QUERY_TYPE_DASHBOARD_QUERY` | Dashboards Query.  
`QUERY_TYPE_STATS_QUERY` | Stats Query.  
`QUERY_TYPE_DATA_TABLE_QUERY` | DataTable Query.  
`QUERY_TYPE_ENTITY_GRAPH_QUERY` | Entity Query.  
`QUERY_TYPE_UDM_DATATABLE_JOIN` | UDM_Datatable Joins Query.  
`QUERY_TYPE_JOIN_STATS_QUERY` | Joins in Stats Query.  
`QUERY_TYPE_JOIN_QUERY` | Joins Query.  
`QUERY_TYPE_DETECTION_QUERY` | Detections Query.  
`QUERY_TYPE_MULTISTAGE` | Multistage Query.  
`QUERY_TYPE_MULTISTAGE_JOINS` | Multistage Joins Query.  
`QUERY_TYPE_CASE_QUERY` | Case Query.  
`QUERY_TYPE_CASE_HISTORY_QUERY` | Case History Query.  
  
## QueryLanguage

The language the query is written in.

Enums  
---  
`QUERY_LANGUAGE_UNSPECIFIED` | The default query language.  
`QUERY_LANGUAGE_YL2` | The query is written in YARA-L 2.  
`QUERY_LANGUAGE_SQL` | The query is written in GoogleSQL.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries/create)`

|  Endpoint for adding a new entry to the specified collection of user data  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries/delete)`

|  Endpoint for deleting a user data saved query entry  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries/get)`

|  Endpoint for getting a user's Saved query entry  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries/list)`

|  Endpoint for listing the user data saved queries owned by the specified user  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries/patch)`

|  Endpoint for updating user data saved query  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
