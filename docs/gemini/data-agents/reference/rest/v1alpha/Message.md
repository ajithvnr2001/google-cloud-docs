---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message/
title: Message \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:53.919727+00:00
---

# Message  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Message Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserMessage
    * JSON representation
  * SystemMessage
    * JSON representation
  * TextMessage
    * JSON representation
  * TextType
  * SchemaMessage
    * JSON representation
  * SchemaQuery
    * JSON representation
  * SchemaResult
    * JSON representation
  * Datasource
    * JSON representation
  * DataMessage
    * JSON representation
  * DataQuery
    * JSON representation
  * DataResult
    * JSON representation
  * BigQueryJob
    * JSON representation
  * MatchedQuery
    * JSON representation
  * QueryParameterValues
    * JSON representation
  * AnalysisMessage
    * JSON representation
  * AnalysisQuery
    * JSON representation
  * AnalysisEvent
    * JSON representation
  * ChartMessage
    * JSON representation
  * ChartQuery
    * JSON representation
  * ChartResult
    * JSON representation
  * Blob
    * JSON representation
  * ErrorMessage
    * JSON representation
  * ExampleQueries
    * JSON representation
  * ClarificationMessage
    * JSON representation
  * ClarificationQuestion
    * JSON representation
  * SelectionMode
  * ClarificationQuestionType
  * Citation
    * JSON representation
  * CitationSource
    * JSON representation
  * CitationAnchor
    * JSON representation
  * TextMessageCitationAnchor
    * JSON representation



A message from an interaction between the user and the system.

JSON representation  
---  
      
    
    {
      "timestamp": string,
      "messageId": string,
    
      // Union field kind can be only one of the following:
      "userMessage": {
        object ([UserMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#UserMessage))
      },
      "systemMessage": {
        object ([SystemMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SystemMessage))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. For user messages, this is the time at which the system received the message. For system messages, this is the time at which the system generated the message.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`messageId` |  `string` Optional. unique id of the message in the conversation for persistence.  
Union field `kind`. The kind of message. `kind` can be only one of the following:  
`userMessage` |  `object (`[UserMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#UserMessage)`)` A message from the user that is interacting with the system.  
`systemMessage` |  `object (`[SystemMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SystemMessage)`)` A message from the system in response to the user.  
  
## UserMessage

A message from the user that is interacting with the system.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "text": string
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of content in the user message. `kind` can be only one of the following:  
`text` |  `string` Text should use this field instead of blob.  
  
## SystemMessage

A message from the system in response to the user. This message can also be a message from the user as historical context for multi-turn conversations with the system.

JSON representation  
---  
      
    
    {
      "citation": {
        object ([Citation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Citation))
      },
    
      // Union field kind can be only one of the following:
      "text": {
        object ([TextMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextMessage))
      },
      "schema": {
        object ([SchemaMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaMessage))
      },
      "data": {
        object ([DataMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataMessage))
      },
      "analysis": {
        object ([AnalysisMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisMessage))
      },
      "chart": {
        object ([ChartMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartMessage))
      },
      "error": {
        object ([ErrorMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ErrorMessage))
      },
      "exampleQueries": {
        object ([ExampleQueries](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ExampleQueries))
      },
      "clarification": {
        object ([ClarificationMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationMessage))
      }
      // End of list of possible types for union field kind.
      "groupId": integer
    }  
  
Fields  
---  
`citation` |  `object (`[Citation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Citation)`)` Output only. Citation information for the system message.  
Union field `kind`. The kind of content in the system message. `kind` can be only one of the following:  
`text` |  `object (`[TextMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextMessage)`)` A direct natural language response to the user message.  
`schema` |  `object (`[SchemaMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaMessage)`)` A message produced during schema resolution.  
`data` |  `object (`[DataMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataMessage)`)` A message produced during data retrieval.  
`analysis` |  `object (`[AnalysisMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisMessage)`)` A message produced during analysis.  
`chart` |  `object (`[ChartMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartMessage)`)` A message produced during chart generation.  
`error` |  `object (`[ErrorMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ErrorMessage)`)` An error message.  
`exampleQueries` |  `object (`[ExampleQueries](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ExampleQueries)`)` Optional. A message containing example queries.  
`clarification  
**(deprecated)**` |  `object (`[ClarificationMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationMessage)`)` This item is deprecated!Optional. Deprecated: Use TextMessage with TextType.FINAL_RESPONSE instead. A message containing clarification questions.  
`groupId` |  `integer` Identifies the group that the event belongs to. Similar events are deemed to be logically relevant to each other and should be shown together in the UI.  
  
## TextMessage

A multi-part text message.

JSON representation  
---  
      
    
    {
      "parts": [
        string
      ],
      "textType": enum ([TextType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextType)),
      "thoughtSignature": string
    }  
  
Fields  
---  
`parts[]` |  `string` Optional. The parts of the message.  
`textType` |  `enum (`[TextType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextType)`)` Optional. The type of the text message.  
`thoughtSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. An opaque signature for a thought so it can be reused in subsequent requests.A base64-encoded string.  
  
## TextType

The type of the text message.

Enums  
---  
`TEXT_TYPE_UNSPECIFIED` | The default text type.  
`FINAL_RESPONSE` | The text is a final response to the user question.  
`THOUGHT` | The text is a thought from the model.  
`PROGRESS` | The text is an informational message about the agent's progress, such as a tool being invoked. This is distinct from the agent's internal thought process (`THOUGHT`) and the final answer to the user (`FINAL_RESPONSE`). These messages provide insight into the agent's actions.  
`FOLLOWUP_QUESTIONS` | The text is a list of follow-up questions suggested. Each item in parts is a follow-up question.  
  
## SchemaMessage

A message produced during schema resolution.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "query": {
        object ([SchemaQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaQuery))
      },
      "result": {
        object ([SchemaResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaResult))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Whether this message contains the query or the result of the schema resolution. `kind` can be only one of the following:  
`query` |  `object (`[SchemaQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaQuery)`)` A schema resolution query.  
`result` |  `object (`[SchemaResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SchemaResult)`)` The result of a schema resolution query.  
  
## SchemaQuery

A query for resolving the schema relevant to the posed question.

JSON representation  
---  
      
    
    {
      "question": string
    }  
  
Fields  
---  
`question` |  `string` Optional. The question to send to the system for schema resolution.  
  
## SchemaResult

The result of schema resolution.

JSON representation  
---  
      
    
    {
      "datasources": [
        {
          object ([Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Datasource))
        }
      ]
    }  
  
Fields  
---  
`datasources[]` |  `object (`[Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Datasource)`)` Optional. The datasources used to resolve the schema query.  
  
## Datasource

A datasource that can be used to answer questions.

JSON representation  
---  
      
    
    {
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema))
      },
      "structSchema": {
        object
      },
    
      // Union field reference can be only one of the following:
      "bigqueryTableReference": {
        object ([BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryTableReference))
      },
      "studioDatasourceId": string,
      "lookerExploreReference": {
        object ([LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerExploreReference))
      },
      "alloyDbReference": {
        object ([AlloyDbReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#AlloyDbReference))
      },
      "spannerReference": {
        object ([SpannerReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#SpannerReference))
      },
      "cloudSqlReference": {
        object ([CloudSqlReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#CloudSqlReference))
      },
      "bigqueryPropertyGraphReference": {
        object ([BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryPropertyGraphReference))
      }
      // End of list of possible types for union field reference.
    }  
  
Fields  
---  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema)`)` Optional. The schema of the datasource.  
`structSchema` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A struct representation of the schema. This is populated for datasources with schemas that cannot be fully represented by the strongly-typed `schema` field.For Looker datasources, this maps to the LookmlModelExplore type: <https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModelExplore>  
Union field `reference`. The reference to the datasource. `reference` can be only one of the following:  
`bigqueryTableReference` |  `object (`[BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryTableReference)`)` A reference to a BigQuery table.  
`studioDatasourceId` |  `string` A reference to a Looker Studio datasource.  
`lookerExploreReference` |  `object (`[LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerExploreReference)`)` A reference to a Looker explore.  
`alloyDbReference` |  `object (`[AlloyDbReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#AlloyDbReference)`)` A reference to an AlloyDB database.  
`spannerReference` |  `object (`[SpannerReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#SpannerReference)`)` A reference to a Spanner database.  
`cloudSqlReference` |  `object (`[CloudSqlReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#CloudSqlReference)`)` A reference to a CloudSQL database.  
`bigqueryPropertyGraphReference` |  `object (`[BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryPropertyGraphReference)`)` A reference to a BigQuery property graph.  
  
## DataMessage

A message produced during data retrieval.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "query": {
        object ([DataQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataQuery))
      },
      "generatedSql": string,
      "result": {
        object ([DataResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataResult))
      },
      "generatedLookerQuery": {
        object ([LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerQuery))
      },
      "bigQueryJob": {
        object ([BigQueryJob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#BigQueryJob))
      },
      "matchedQuery": {
        object ([MatchedQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#MatchedQuery))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Whether this message contains the query, the result, or generated SQL for the data retrieval. `kind` can be only one of the following:  
`query` |  `object (`[DataQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataQuery)`)` A data retrieval query.  
`generatedSql` |  `string` SQL generated by the system to retrieve data.  
`result` |  `object (`[DataResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#DataResult)`)` Retrieved data.  
`generatedLookerQuery  
**(deprecated)**` |  `object (`[LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerQuery)`)` This item is deprecated!Deprecated: generated looker query is now under DataQuery.looker. Looker Query generated by the system to retrieve data.  
`bigQueryJob` |  `object (`[BigQueryJob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#BigQueryJob)`)` A BigQuery job executed by the system to retrieve data.  
`matchedQuery` |  `object (`[MatchedQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#MatchedQuery)`)` A pre-existing query that was matched to retrieve data.  
  
## DataQuery

A query for retrieving data.

JSON representation  
---  
      
    
    {
      "question": string,
      "name": string,
      "datasources": [
        {
          object ([Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Datasource))
        }
      ],
    
      // Union field query_type can be only one of the following:
      "looker": {
        object ([LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerQuery))
      }
      // End of list of possible types for union field query_type.
    }  
  
Fields  
---  
`question` |  `string` Optional. A natural language question to answer.  
`name` |  `string` Optional. A snake-case name for the query that reflects its intent. It is used to name the corresponding data result, so that it can be referenced in later steps.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"

  
`datasources[]` |  `object (`[Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Datasource)`)` Optional. The datasources available to answer the question.  
Union field `query_type`. The type of query to execute. `query_type` can be only one of the following:  
`looker` |  `object (`[LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#LookerQuery)`)` Optional. A query for retrieving data from a Looker explore.  
  
## DataResult

Retrieved data.

JSON representation  
---  
      
    
    {
      "name": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema))
      },
      "data": [
        {
          object
        }
      ],
      "formattedData": [
        {
          object
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Optional. A snake-case name for the data result that reflects its contents. The name is used to pass the result around by reference, and serves as a signal about its meaning.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"

  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema)`)` Optional. The schema of the data.  
`data[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the data. Each row is a struct that matches the schema. Simple values are represented as strings, while nested structures are represented as lists or structs.  
`formattedData[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Formatted representation of the data, when applicable. Each row is a struct that directly corresponds to the row at the same index within the `data` field. Its values are string representations of the original data, formatted according to data source specifications (e.g., "$1,234.56" for currency). Columns without formatting will default to their raw value representation. If no columns have formatting rules, this field will be empty.  
  
## BigQueryJob

A BigQuery job executed by the system.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "jobId": string,
      "location": string,
      "destinationTable": {
        object ([BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryTableReference))
      },
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema))
      }
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project that the job belongs to.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`jobId` |  `string` Required. The ID of the job.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`location` |  `string` Optional. The location of the job.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`destinationTable` |  `object (`[BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#BigQueryTableReference)`)` Optional. A reference to the destination table of the job's query results.See [JobConfigurationQuery](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery).  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#Schema)`)` Optional. The schema of the job's query results.See [JobStatistics2](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobstatistics2).  
  
## MatchedQuery

A matched query message represents the agent having matched one of the example queries supplied in context as being applicable to the current question. It will also contain additional info during the matching process.

JSON representation  
---  
      
    
    {
      "exampleQuery": {
        object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery))
      },
      "queryParameterValues": [
        {
          object ([QueryParameterValues](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#QueryParameterValues))
        }
      ]
    }  
  
Fields  
---  
`exampleQuery` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery)`)` The query that was matched based on an example query.  
`queryParameterValues[]` |  `object (`[QueryParameterValues](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#QueryParameterValues)`)` The extracted values for the query parameters.  
  
## QueryParameterValues

A query parameter values message represents the values for the query parameters that were extracted from the user question by LLM, based on the example query.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the parameter.  
`value` |  `string` Required. The value of the parameter.  
  
## AnalysisMessage

A message produced during analysis.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "query": {
        object ([AnalysisQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisQuery))
      },
      "progressEvent": {
        object ([AnalysisEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisEvent))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Whether this message contains the query or one of the events from the analysis. `kind` can be only one of the following:  
`query` |  `object (`[AnalysisQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisQuery)`)` An analysis query.  
`progressEvent` |  `object (`[AnalysisEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#AnalysisEvent)`)` An event indicating the progress of the analysis.  
  
## AnalysisQuery

A query for performing an analysis.

JSON representation  
---  
      
    
    {
      "question": string,
      "dataResultNames": [
        string
      ]
    }  
  
Fields  
---  
`question` |  `string` Optional. An analysis question to help answer the user's original question.  
`dataResultNames[]` |  `string` Optional. The names of previously retrieved data results to analyze.  
  
## AnalysisEvent

An event indicating the progress of an analysis.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "plannerReasoning": string,
      "coderInstruction": string,
      "code": string,
      "executionOutput": string,
      "executionError": string,
      "resultVegaChartJson": string,
      "resultNaturalLanguage": string,
      "resultCsvData": string,
      "resultReferenceData": string,
      "error": string
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of event that occurred during the analysis. `kind` can be only one of the following:  
`plannerReasoning` |  `string` Python codegen planner's reasoning.  
`coderInstruction` |  `string` Instructions issued for code generation.  
`code` |  `string` Generated code.  
`executionOutput` |  `string` Output from code execution.  
`executionError` |  `string` An error from code execution.  
`resultVegaChartJson` |  `string` Result as Vega chart JSON string.  
`resultNaturalLanguage` |  `string` Result as NL string.  
`resultCsvData` |  `string` Result as CSV string.  
`resultReferenceData` |  `string` Result as a reference to a data source.  
`error` |  `string` A generic error message.  
  
## ChartMessage

A message produced during chart generation.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "query": {
        object ([ChartQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartQuery))
      },
      "result": {
        object ([ChartResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartResult))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Whether this message contains the query or the result of the chart generation. `kind` can be only one of the following:  
`query` |  `object (`[ChartQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartQuery)`)` A query for generating a chart.  
`result` |  `object (`[ChartResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ChartResult)`)` The result of a chart generation query.  
  
## ChartQuery

A query for generating a chart.

JSON representation  
---  
      
    
    {
      "instructions": string,
      "dataResultName": string
    }  
  
Fields  
---  
`instructions` |  `string` Optional. Natural language instructions for generating the chart.  
`dataResultName` |  `string` Optional. The name of a previously retrieved data result to use in the chart.  
  
## ChartResult

The result of a chart generation query.

JSON representation  
---  
      
    
    {
      "vegaConfig": {
        object
      },
      "image": {
        object ([Blob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Blob))
      }
    }  
  
Fields  
---  
`vegaConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A generated Vega chart config. See <https://vega.github.io/vega/docs/config/>  
`image` |  `object (`[Blob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#Blob)`)` Optional. A rendering of the chart if this was requested in the context.  
  
## Blob

A blob of data with a MIME type.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the message data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The data represented as bytes.A base64-encoded string.  
  
## ErrorMessage

An error message from a tool call. This message is used to represent an error that occurred while an agent was trying to use a tool. It's important to note that not all errors are terminal. Many are recoverable, and the agent may use the information from this error message to self-correct and retry the tool call or try a different approach.

For example, if a data query fails, the agent might receive an `ErrorMessage`, analyze it, and then generate a corrected query.

Clients should be cautious about interpreting this message as a definitive failure. It can be part of the agent's normal, iterative process of completing a task. Surfacing these errors directly to end-users without context (e.g., as a "hard failure") may be misleading.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Output only. The text of the error.  
  
## ExampleQueries

A message containing derived and authored example queries.

JSON representation  
---  
      
    
    {
      "exampleQueries": [
        {
          object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery))
        }
      ]
    }  
  
Fields  
---  
`exampleQueries[]` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery)`)` Optional. A list of derived and authored example queries, providing examples of relevant and commonly used SQL queries and their corresponding natural language queries optionally present. Currently only used for BigQuery data sources.  
  
## ClarificationMessage

This item is deprecated!

Deprecated: Use TextMessage with TextType.FINAL_RESPONSE instead. A message of questions to help clarify the user's query. This is returned when the system cannot confidently answer the user's question.

JSON representation  
---  
      
    
    {
      "questions": [
        {
          object ([ClarificationQuestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationQuestion))
        }
      ]
    }  
  
Fields  
---  
`questions[]  
**(deprecated)**` |  `object (`[ClarificationQuestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationQuestion)`)` This item is deprecated!Required. Deprecated: The parent message is deprecated. A batch of clarification questions to ask the user.  
  
## ClarificationQuestion

This item is deprecated!

Deprecated: Use TextMessage with TextType.FINAL_RESPONSE instead. Represents a single question to the user to help clarify their query.

JSON representation  
---  
      
    
    {
      "question": string,
      "selectionMode": enum ([SelectionMode](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SelectionMode)),
      "options": [
        string
      ],
      "clarificationQuestionType": enum ([ClarificationQuestionType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationQuestionType))
    }  
  
Fields  
---  
`question  
**(deprecated)**` |  `string` This item is deprecated!Required. Deprecated: The parent message is deprecated. The natural language question to ask the user.  
`selectionMode  
**(deprecated)**` |  `enum (`[SelectionMode](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#SelectionMode)`)` This item is deprecated!Required. Deprecated: The parent message is deprecated. The selection mode for this question.  
`options[]  
**(deprecated)**` |  `string` This item is deprecated!Required. Deprecated: The parent message is deprecated. A list of distinct options for the user to choose from. The number of options is limited to a maximum of 5.  
`clarificationQuestionType  
**(deprecated)**` |  `enum (`[ClarificationQuestionType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#ClarificationQuestionType)`)` This item is deprecated!Optional. Deprecated: The parent message is deprecated. The type of clarification question.  
  
## SelectionMode

This item is deprecated!

Deprecated: The parent message is deprecated. The selection mode for the clarification question.

Enums  
---  
`SELECTION_MODE_UNSPECIFIED` | Deprecated: The parent message is deprecated. Unspecified selection mode.This item is deprecated!  
`SINGLE_SELECT` | Deprecated: The parent message is deprecated. The user can select only one option.This item is deprecated!  
`MULTI_SELECT` | Deprecated: The parent message is deprecated. The user can select multiple options.This item is deprecated!  
  
## ClarificationQuestionType

This item is deprecated!

Deprecated: The parent message is deprecated. The type of clarification question. This enum may be extended with new values in the future.

Enums  
---  
`CLARIFICATION_QUESTION_TYPE_UNSPECIFIED` | Deprecated: The parent message is deprecated. Unspecified clarification question type.This item is deprecated!  
`FILTER_VALUES` | Deprecated: The parent message is deprecated. The clarification question is for filter values.This item is deprecated!  
`FIELDS` | Deprecated: The parent message is deprecated. The clarification question is for data fields. This is a generic term encompassing SQL columns, Looker fields (dimensions/measures), or nested data structure properties.This item is deprecated!  
  
## Citation

Source attributions for content.

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([CitationSource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#CitationSource))
        }
      ],
      "anchors": [
        {
          object ([CitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#CitationAnchor))
        }
      ]
    }  
  
Fields  
---  
`sources[]` |  `object (`[CitationSource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#CitationSource)`)` Output only. List of the sources being cited.  
`anchors[]` |  `object (`[CitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#CitationAnchor)`)` Output only. List of the anchors of the citations.  
  
## CitationSource

The source of the citation.

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
    
      // Union field source_type can be only one of the following:
      "uri": string,
      "exampleQuery": {
        object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery))
      },
      "glossaryTerm": {
        object ([GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#GlossaryTerm))
      }
      // End of list of possible types for union field source_type.
    }  
  
Fields  
---  
`id` |  `string` Output only. Unique identifier of the source. This ID is service-generated and is unique within the scope of a single `Citation` message.  
`title` |  `string` Output only. The title of the source.  
Union field `source_type`. The source of the citation, which can be one of the supported types. `source_type` can be only one of the following:  
`uri` |  `string` Output only. The uri used as the source, such as a web grounding URL.  
`exampleQuery` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#ExampleQuery)`)` Output only. The example query used as the source.  
`glossaryTerm` |  `object (`[GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#GlossaryTerm)`)` Output only. The glossary term used as the source.  
  
## CitationAnchor

The anchor of the citation.

JSON representation  
---  
      
    
    {
    
      // Union field anchor_type can be only one of the following:
      "textMessageAnchor": {
        object ([TextMessageCitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextMessageCitationAnchor))
      }
      // End of list of possible types for union field anchor_type.
    }  
  
Fields  
---  
Union field `anchor_type`. The anchor of the citation, which can be one of the supported types. `anchor_type` can be only one of the following:  
`textMessageAnchor` |  `object (`[TextMessageCitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message#TextMessageCitationAnchor)`)` Output only. Only set if the citation is for a TextMessage.  
  
## TextMessageCitationAnchor

Citation anchor within a TextMessage.

JSON representation  
---  
      
    
    {
      "partIndex": integer,
      "startOffsetBytes": integer,
      "endOffsetBytes": integer,
      "sourceIds": [
        string
      ]
    }  
  
Fields  
---  
`partIndex` |  `integer` Output only. The 0-based index of the part within the TextMessage.parts field.  
`startOffsetBytes` |  `integer` Output only. The offset, measured in UTF-8 bytes, within the part string where the citation begins (inclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.  
`endOffsetBytes` |  `integer` Output only. The offset, measured in UTF-8 bytes, within the part string where the citation ends (exclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.  
`sourceIds[]` |  `string` Output only. The ids of the sources that are cited.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
