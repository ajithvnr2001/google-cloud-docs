---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute/
title: Method: sdlConnectors.execute \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:20.545446+00:00
---

# Method: sdlConnectors.execute  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Method: sdlConnectors.execute Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * ColumnMetadata
    * JSON representation
  * ColumnDataType
  * QueryResult
    * JSON representation
  * Try it!



**Full name** : projects.locations.instances.sdlConnectors.execute

Execute Query executes the given query in the request and returns the response.

### HTTP request

`POST https://chronicle.googleapis.com/v1alpha/{parent}/sdlConnectors:execute`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which points to the customer. Format: projects/{project}/locations/{region}/instances/{instance}/sdlconnector  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "query": string
    }  
  
Fields  
---  
`query` |  `string` Required. query is the google sql query which is to be executed.  
  
### Response body

ExecuteQueryResponse contains the details of the query output.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "columns_metadata": [
        {
          object ([ColumnMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#ColumnMetadata))
        }
      ],
      "query_results": [
        {
          object ([QueryResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#QueryResult))
        }
      ]
    }  
  
Fields  
---  
`columns_metadata[]` |  `object (`[ColumnMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#ColumnMetadata)`)` columnName and datatype returned in result. Repeats for every column  
`query_results[]` |  `object (`[QueryResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#QueryResult)`)` result of query , repeats for every row  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ColumnMetadata

ColumnMetadata contains details about the column like name and type.

JSON representation  
---  
      
    
    {
      "name": string,
      "datatype": enum ([ColumnDataType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#ColumnDataType))
    }  
  
Fields  
---  
`name` |  `string` name of column returned in result  
`datatype` |  `enum (`[ColumnDataType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.sdlConnectors/execute#ColumnDataType)`)` Datatype of column returned  
  
## ColumnDataType

ColumnDataType mentions the data type of the column.

Enums  
---  
`COLUMN_DATA_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`COLUMN_DATA_TYPE_STRING` | String type  
`COLUMN_DATA_TYPE_INTEGER` | Integer type  
`COLUMN_DATA_TYPE_FLOAT` | Float type  
`COLUMN_DATA_TYPE_BOOLEAN` | Boolean type  
`COLUMN_DATA_TYPE_SIGNEDINT` | Signed int type  
`COLUMN_DATA_TYPE_UNSIGNEDINT` | Unsigned int type  
`COLUMN_DATA_TYPE_DATE` | Date type  
`COLUMN_DATA_TYPE_TIMESTAMP` | Timestamp type  
`COLUMN_DATA_TYPE_OBJECT` | Object type  
  
## QueryResult

Query result contains the result of the query executed.

JSON representation  
---  
      
    
    {
      "columns_value": [
        string
      ]
    }  
  
Fields  
---  
`columns_value[]` |  `string` repeats for every column value  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
