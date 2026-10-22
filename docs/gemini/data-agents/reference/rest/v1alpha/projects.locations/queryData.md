---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData/
title: Method: projects.locations.queryData \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:48.709548+00:00
---

# Method: projects.locations.queryData  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: projects.locations.queryData Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * QueryDataContext
    * JSON representation
  * ParameterizedSecureViewParameters
    * JSON representation
  * Parameter
    * JSON representation
  * GenerationOptions
    * JSON representation
  * ExecutedQueryResult
    * JSON representation
  * Column
    * JSON representation
  * Row
    * JSON representation
  * Value
    * JSON representation



Queries data from a natural language user query.

### HTTP request

`POST https://geminidataanalytics.googleapis.com/v1alpha/{parent=projects/*/locations/*}:queryData`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource to generate the query for. Format: projects/{project}/locations/{location}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "prompt": string,
      "context": {
        object ([QueryDataContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#QueryDataContext))
      },
      "generationOptions": {
        object ([GenerationOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#GenerationOptions))
      }
    }  
  
Fields  
---  
`prompt` |  `string` Required. The natural language query for which to generate query. Example: "What are the top 5 best selling products this month?"  
`context` |  `object (`[QueryDataContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#QueryDataContext)`)` Required. The context for the data query, including the data sources to use.  
`generationOptions` |  `object (`[GenerationOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#GenerationOptions)`)` Optional. Options to control query generation and execution behavior.  
  
### Response body

Response containing the generated query and related information.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "generatedQuery": string,
      "intentExplanation": string,
      "queryResult": {
        object ([ExecutedQueryResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#ExecutedQueryResult))
      },
      "naturalLanguageAnswer": string,
      "disambiguationQuestion": [
        string
      ]
    }  
  
Fields  
---  
`generatedQuery` |  `string` Generated query for the given user prompt.  
`intentExplanation` |  `string` A natural language explanation of the generated query. Populated if options.generate_explanation was true in the request.  
`queryResult` |  `object (`[ExecutedQueryResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#ExecutedQueryResult)`)` The result of executing the query. Populated if options.generate_query_result or options.generate_natural_language_answer was true in the request, and execution was successful or attempted.  
`naturalLanguageAnswer` |  `string` A natural language answer to the query, based on the queryResult. Populated if options.generate_natural_language_answer was true in the request and query execution was successful based in the response from executeSql API.  
`disambiguationQuestion[]` |  `string` If ambiguity was detected in the natural language query and options.generate_disambiguation_question was true, this field contains a question to the user for clarification. The returned represents the service's best effort based on the ambiguous input.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## QueryDataContext

References to data sources and context to use for the query.

JSON representation  
---  
      
    
    {
      "datasourceReferences": {
        object ([DatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#DatasourceReferences))
      },
      "parameterizedSecureViewParameters": {
        object ([ParameterizedSecureViewParameters](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#ParameterizedSecureViewParameters))
      }
    }  
  
Fields  
---  
`datasourceReferences` |  `object (`[DatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#DatasourceReferences)`)` Required. The datasource references to use for the query.  
`parameterizedSecureViewParameters` |  `object (`[ParameterizedSecureViewParameters](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#ParameterizedSecureViewParameters)`)` Optional. Parameters for parameterized secure views.  
  
## ParameterizedSecureViewParameters

Parameters for parameterized secure views. These parameters are used to enforce row-level security during SQL generation and query execution.

JSON representation  
---  
      
    
    {
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Parameter))
        }
      ]
    }  
  
Fields  
---  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Parameter)`)` Optional. Named parameters for parameterized secure views.  
  
## Parameter

Represents a single parameter for parameterized secure views.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. The parameter key (e.g., `"userId"`).  
`value` |  `string` Required. The parameter value (e.g., `"123"`).  
  
## GenerationOptions

Options to control query generation, execution, and response format.

JSON representation  
---  
      
    
    {
      "generateQueryResult": boolean,
      "generateNaturalLanguageAnswer": boolean,
      "generateExplanation": boolean,
      "generateDisambiguationQuestion": boolean
    }  
  
Fields  
---  
`generateQueryResult` |  `boolean` Optional. If true, the generated query will be executed, and the result data will be returned in the response.  
`generateNaturalLanguageAnswer` |  `boolean` Optional. If true, a natural language answer based on the query execution result will be generated and returned in the response.  
`generateExplanation` |  `boolean` Optional. If true, an explanation of the generated query will be returned in the response.  
`generateDisambiguationQuestion` |  `boolean` Optional. If true (default to false), the service may return a clarifying_question if the input query is ambiguous.  
  
## ExecutedQueryResult

The result of a query execution. The design is generic for all dialects.

JSON representation  
---  
      
    
    {
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Column))
        }
      ],
      "rows": [
        {
          object ([Row](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Row))
        }
      ],
      "totalRowCount": string,
      "partialResult": boolean,
      "queryExecutionError": string
    }  
  
Fields  
---  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Column)`)` The columns in the result set, in order.  
`rows[]` |  `object (`[Row](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Row)`)` The rows returned by the query.  
`totalRowCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of rows in the full result set, if known. This may be an estimate or an exact count.  
`partialResult` |  `boolean` Set to true if the returned rows in `queryResult` are a subset of the full result. This can happen, for example, if the query execution hits a row limit. When true, the `queryResult` does not contain all rows. To retrieve the complete result, consider using the `generatedQuery` in `QueryDataResponse` and executing it in your own environment.  
`queryExecutionError` |  `string` The error message if the query execution failed.  
  
## Column

Describes a single column in the result set.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string
    }  
  
Fields  
---  
`name` |  `string` The name of the column.  
`type` |  `string` The type of the column (e.g., "VARCHAR", "INT64", "TIMESTAMP").  
  
## Row

Represents a single row in the result set.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Value](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Value))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[Value](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData#Value)`)` The values in the row, corresponding positionally to the columns.  
  
## Value

Represents a single value within a row.

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` The cell value, represented in a string format. Timestamps could be formatted, for example, using RFC3339Nano. This field is used if the value is not null.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
