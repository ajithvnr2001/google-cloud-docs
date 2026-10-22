---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message/
title: Message \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:03.082729+00:00
---

# Message  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message/

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
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userMessage": {
        object ([UserMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#UserMessage))
      },
      "systemMessage": {
        object ([SystemMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SystemMessage))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. For user messages, this is the time at which the system received the message. For system messages, this is the time at which the system generated the message.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`messageId` |  `string` Optional. unique id of the message in the conversation for persistence.  
The kind of message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userMessage` |  `object (`[UserMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#UserMessage)`)` A message from the user that is interacting with the system.  
`systemMessage` |  `object (`[SystemMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SystemMessage)`)` A message from the system in response to the user.  
End of mutually exclusive fields.  
  
## UserMessage

A message from the user that is interacting with the system.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The kind of content in the user message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Text should use this field instead of blob.  
End of mutually exclusive fields.  
  
## SystemMessage

A message from the system in response to the user. This message can also be a message from the user as historical context for multi-turn conversations with the system.

JSON representation  
---  
      
    
    {
      "citation": {
        object ([Citation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Citation))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": {
        object ([TextMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextMessage))
      },
      "schema": {
        object ([SchemaMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaMessage))
      },
      "data": {
        object ([DataMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataMessage))
      },
      "analysis": {
        object ([AnalysisMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisMessage))
      },
      "chart": {
        object ([ChartMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartMessage))
      },
      "error": {
        object ([ErrorMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ErrorMessage))
      },
      "exampleQueries": {
        object ([ExampleQueries](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ExampleQueries))
      }
      // End of mutually exclusive fields.
      "groupId": integer
    }  
  
Fields  
---  
`citation` |  `object (`[Citation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Citation)`)` Output only. Citation information for the system message.  
The kind of content in the system message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `object (`[TextMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextMessage)`)` A direct natural language response to the user message.  
`schema` |  `object (`[SchemaMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaMessage)`)` A message produced during schema resolution.  
`data` |  `object (`[DataMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataMessage)`)` A message produced during data retrieval.  
`analysis` |  `object (`[AnalysisMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisMessage)`)` A message produced during analysis.  
`chart` |  `object (`[ChartMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartMessage)`)` A message produced during chart generation.  
`error` |  `object (`[ErrorMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ErrorMessage)`)` An error message.  
`exampleQueries` |  `object (`[ExampleQueries](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ExampleQueries)`)` Optional. A message containing example queries.  
End of mutually exclusive fields.  
`groupId` |  `integer` Identifies the group that the event belongs to. Similar events are deemed to be logically relevant to each other and should be shown together in the UI.  
  
## TextMessage

A multi-part text message.

JSON representation  
---  
      
    
    {
      "parts": [
        string
      ],
      "textType": enum ([TextType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextType)),
      "thoughtSignature": string
    }  
  
Fields  
---  
`parts[]` |  `string` Optional. The parts of the message.  
`textType` |  `enum (`[TextType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextType)`)` Optional. The type of the text message.  
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
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "query": {
        object ([SchemaQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaQuery))
      },
      "result": {
        object ([SchemaResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether this message contains the query or the result of the schema resolution. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`query` |  `object (`[SchemaQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaQuery)`)` A schema resolution query.  
`result` |  `object (`[SchemaResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SchemaResult)`)` The result of a schema resolution query.  
End of mutually exclusive fields.  
  
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
          object ([Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Datasource))
        }
      ]
    }  
  
Fields  
---  
`datasources[]` |  `object (`[Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Datasource)`)` Optional. The datasources used to resolve the schema query.  
  
## Datasource

A datasource that can be used to answer questions.

JSON representation  
---  
      
    
    {
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema))
      },
      "structSchema": {
        object
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "bigqueryTableReference": {
        object ([BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryTableReference))
      },
      "studioDatasourceId": string,
      "lookerExploreReference": {
        object ([LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#LookerExploreReference))
      },
      "bigqueryPropertyGraphReference": {
        object ([BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryPropertyGraphReference))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema)`)` Optional. The schema of the datasource.  
`structSchema` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A struct representation of the schema. This is populated for datasources with schemas that cannot be fully represented by the strongly-typed `schema` field.For Looker datasources, this maps to the LookmlModelExplore type: <https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModelExplore>  
The reference to the datasource. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`bigqueryTableReference` |  `object (`[BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryTableReference)`)` A reference to a BigQuery table.  
`studioDatasourceId` |  `string` A reference to a Looker Studio datasource.  
`lookerExploreReference` |  `object (`[LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#LookerExploreReference)`)` A reference to a Looker explore.  
`bigqueryPropertyGraphReference` |  `object (`[BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryPropertyGraphReference)`)` A reference to a BigQuery property graph.  
End of mutually exclusive fields.  
  
## DataMessage

A message produced during data retrieval.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "query": {
        object ([DataQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataQuery))
      },
      "generatedSql": string,
      "result": {
        object ([DataResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataResult))
      },
      "bigQueryJob": {
        object ([BigQueryJob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#BigQueryJob))
      },
      "matchedQuery": {
        object ([MatchedQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#MatchedQuery))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether this message contains the query, the result, or generated SQL for the data retrieval. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`query` |  `object (`[DataQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataQuery)`)` A data retrieval query.  
`generatedSql` |  `string` SQL generated by the system to retrieve data.  
`result` |  `object (`[DataResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#DataResult)`)` Retrieved data.  
`bigQueryJob` |  `object (`[BigQueryJob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#BigQueryJob)`)` A BigQuery job executed by the system to retrieve data.  
`matchedQuery` |  `object (`[MatchedQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#MatchedQuery)`)` A pre-existing query that was matched to retrieve data.  
End of mutually exclusive fields.  
  
## DataQuery

A query for retrieving data.

JSON representation  
---  
      
    
    {
      "question": string,
      "name": string,
      "datasources": [
        {
          object ([Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Datasource))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "looker": {
        object ([LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#LookerQuery))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`question` |  `string` Optional. A natural language question to answer.  
`name` |  `string` Optional. A snake-case name for the query that reflects its intent. It is used to name the corresponding data result, so that it can be referenced in later steps.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"

  
`datasources[]` |  `object (`[Datasource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Datasource)`)` Optional. The datasources available to answer the question.  
The type of query to execute. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`looker` |  `object (`[LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#LookerQuery)`)` Optional. A query for retrieving data from a Looker explore.  
End of mutually exclusive fields.  
  
## DataResult

Retrieved data.

JSON representation  
---  
      
    
    {
      "name": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema))
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

  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema)`)` Optional. The schema of the data.  
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
        object ([BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryTableReference))
      },
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema))
      }
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project that the job belongs to.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`jobId` |  `string` Required. The ID of the job.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`location` |  `string` Optional. The location of the job.See [JobReference](https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference).  
`destinationTable` |  `object (`[BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#BigQueryTableReference)`)` Optional. A reference to the destination table of the job's query results.See [JobConfigurationQuery](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery).  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Schema)`)` Optional. The schema of the job's query results.See [JobStatistics2](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobstatistics2).  
  
## MatchedQuery

A matched query message represents the agent having matched one of the example queries supplied in context as being applicable to the current question. It will also contain additional info during the matching process.

JSON representation  
---  
      
    
    {
      "exampleQuery": {
        object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery))
      },
      "queryParameterValues": [
        {
          object ([QueryParameterValues](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#QueryParameterValues))
        }
      ]
    }  
  
Fields  
---  
`exampleQuery` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery)`)` The query that was matched based on an example query.  
`queryParameterValues[]` |  `object (`[QueryParameterValues](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#QueryParameterValues)`)` The extracted values for the query parameters.  
  
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
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "query": {
        object ([AnalysisQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisQuery))
      },
      "progressEvent": {
        object ([AnalysisEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisEvent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether this message contains the query or one of the events from the analysis. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`query` |  `object (`[AnalysisQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisQuery)`)` An analysis query.  
`progressEvent` |  `object (`[AnalysisEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#AnalysisEvent)`)` An event indicating the progress of the analysis.  
End of mutually exclusive fields.  
  
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
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
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
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The kind of event that occurred during the analysis. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
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
End of mutually exclusive fields.  
  
## ChartMessage

A message produced during chart generation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "query": {
        object ([ChartQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartQuery))
      },
      "result": {
        object ([ChartResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether this message contains the query or the result of the chart generation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`query` |  `object (`[ChartQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartQuery)`)` A query for generating a chart.  
`result` |  `object (`[ChartResult](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#ChartResult)`)` The result of a chart generation query.  
End of mutually exclusive fields.  
  
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
        object ([Blob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Blob))
      }
    }  
  
Fields  
---  
`vegaConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A generated Vega chart config. See <https://vega.github.io/vega/docs/config/>  
`image` |  `object (`[Blob](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Blob)`)` Optional. A rendering of the chart if this was requested in the context.  
  
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
          object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery))
        }
      ]
    }  
  
Fields  
---  
`exampleQueries[]` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery)`)` Optional. A list of derived and authored example queries, providing examples of relevant and commonly used SQL queries and their corresponding natural language queries optionally present. Currently only used for BigQuery data sources.  
  
## Citation

Source attributions for content.

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([CitationSource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#CitationSource))
        }
      ],
      "anchors": [
        {
          object ([CitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#CitationAnchor))
        }
      ]
    }  
  
Fields  
---  
`sources[]` |  `object (`[CitationSource](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#CitationSource)`)` Output only. List of the sources being cited.  
`anchors[]` |  `object (`[CitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#CitationAnchor)`)` Output only. List of the anchors of the citations.  
  
## CitationSource

The source of the citation.

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "uri": string,
      "exampleQuery": {
        object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery))
      },
      "glossaryTerm": {
        object ([GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#GlossaryTerm))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`id` |  `string` Output only. Unique identifier of the source. This ID is service-generated and is unique within the scope of a single `Citation` message.  
`title` |  `string` Output only. The title of the source.  
The source of the citation, which can be one of the supported types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`uri` |  `string` Output only. The uri used as the source, such as a web grounding URL.  
`exampleQuery` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#ExampleQuery)`)` Output only. The example query used as the source.  
`glossaryTerm` |  `object (`[GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#GlossaryTerm)`)` Output only. The glossary term used as the source.  
End of mutually exclusive fields.  
  
## CitationAnchor

The anchor of the citation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textMessageAnchor": {
        object ([TextMessageCitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextMessageCitationAnchor))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The anchor of the citation, which can be one of the supported types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textMessageAnchor` |  `object (`[TextMessageCitationAnchor](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#TextMessageCitationAnchor)`)` Output only. Only set if the citation is for a TextMessage.  
End of mutually exclusive fields.  
  
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
