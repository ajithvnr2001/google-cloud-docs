---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents
title: REST Resource: projects.locations.dataAgents \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:47.113254+00:00
---

# REST Resource: projects.locations.dataAgents  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  REST Resource: projects.locations.dataAgents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataAgent
    * JSON representation
  * DataAnalyticsAgent
    * JSON representation
  * Context
    * JSON representation
  * DatasourceReferences
    * JSON representation
  * BigQueryTableReferences
    * JSON representation
  * BigQueryTableReference
    * JSON representation
  * Schema
    * JSON representation
  * Field
    * JSON representation
  * DataFilter
    * JSON representation
  * DataFilterType
  * BigQueryPropertyGraphReference
    * JSON representation
  * StudioDatasourceReferences
    * JSON representation
  * StudioDatasourceReference
    * JSON representation
  * LookerExploreReferences
    * JSON representation
  * LookerExploreReference
    * JSON representation
  * PrivateLookerInstanceInfo
    * JSON representation
  * Credentials
    * JSON representation
  * OAuthCredentials
    * JSON representation
  * SecretBased
    * JSON representation
  * TokenBased
    * JSON representation
  * AlloyDbReference
    * JSON representation
  * AlloyDbDatabaseReference
    * JSON representation
  * DatabaseTableReference
    * JSON representation
  * AgentContextReference
    * JSON representation
  * SpannerReference
    * JSON representation
  * SpannerDatabaseReference
    * JSON representation
  * Engine
  * CloudSqlReference
    * JSON representation
  * CloudSqlDatabaseReference
    * JSON representation
  * Engine
  * ConversationOptions
    * JSON representation
  * ChartOptions
    * JSON representation
  * ImageOptions
    * JSON representation
  * NoImage
  * SvgOptions
  * AnalysisOptions
    * JSON representation
  * Python
    * JSON representation
  * DatasourceOptions
    * JSON representation
  * Model
  * ExampleQuery
    * JSON representation
  * QueryParameter
    * JSON representation
  * LookerGoldenQuery
    * JSON representation
  * LookerQuery
    * JSON representation
  * Filter
    * JSON representation
  * GlossaryTerm
    * JSON representation
  * SchemaRelationship
    * JSON representation
  * SchemaPaths
    * JSON representation
  * Source
  * UserFunctions
    * JSON representation
  * BigQueryRoutine
    * JSON representation
  * BigQueryRoutineReference
    * JSON representation
  * Methods



## Resource: DataAgent

Message describing a DataAgent object.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "purgeTime": string,
    
      // Union field type can be only one of the following:
      "dataAnalyticsAgent": {
        object ([DataAnalyticsAgent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataAnalyticsAgent))
      }
      // End of list of possible types for union field type.
      "kmsKey": string
    }  
  
Fields  
---  
`name` |  `string` Optional. Identifier. The unique resource name of a DataAgent. Format: `projects/{project}/locations/{location}/dataAgents/{dataAgentId}` `{dataAgent}` is the resource id and should be 63 characters or less and must match the format described in <https://google.aip.dev/122#resource-id-segments>Example: `projects/1234567890/locations/global/dataAgents/my-agent`.It is recommended to skip setting this field during agent creation as it will be inferred automatically and overwritten with the {parent}/dataAgents/{dataAgentId}.  
`displayName` |  `string` Optional. User friendly display name.

  * Must be between 1-256 characters.

  
`description` |  `string` Optional. Description of the agent.

  * Must be between 1-1024 characters.

  
`labels` |  `map (key: string, value: string)` Optional. Labels to help users filter related agents. For example, "sales", "business", "etl", and so on. Note labels are used only for filtering and not for policies. See the [labels documentation](https://cloud.google.com/resource-manager/docs/labels-overview) for more details on label usage.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the data agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the data agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The time the data agent was soft deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`purgeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp in UTC of when this data agent is considered expired. This is _always_ provided on output, regardless of what was sent on input.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `type`. The type of the agent. Can be one of the following: * Data analytics agent. * Data engineering agent `type` can be only one of the following:  
`dataAnalyticsAgent` |  `object (`[DataAnalyticsAgent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataAnalyticsAgent)`)` Data analytics agent.  
`kmsKey` |  `string` Optional. Customer managed encryption key (CMEK) to use for encrypting the DataAgent resources. Cloud KMS CryptoKeys must reside in the same location as the DataAgent. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.  
  
## DataAnalyticsAgent

Message describing a DataAnalyticsAgent object.

JSON representation  
---  
      
    
    {
      "stagingContext": {
        object ([Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context))
      },
      "publishedContext": {
        object ([Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context))
      },
      "lastPublishedContext": {
        object ([Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context))
      }
    }  
  
Fields  
---  
`stagingContext` |  `object (`[Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context)`)` Optional. The staging context for the agent. This context is used to test and validate changes before publishing.  
`publishedContext` |  `object (`[Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context)`)` Optional. The published context for the agent. This context is used by the Chat API in production.  
`lastPublishedContext` |  `object (`[Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Context)`)` Output only. The last published context for the agent. This is an output-only field populated by the system when the published context is updated. It is used to restore the agent to a previous state.  
  
## Context

A collection of context to apply to this conversation

JSON representation  
---  
      
    
    {
      "systemInstruction": string,
      "datasourceReferences": {
        object ([DatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatasourceReferences))
      },
      "options": {
        object ([ConversationOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ConversationOptions))
      },
      "exampleQueries": [
        {
          object ([ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ExampleQuery))
        }
      ],
      "lookerGoldenQueries": [
        {
          object ([LookerGoldenQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerGoldenQuery))
        }
      ],
      "glossaryTerms": [
        {
          object ([GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#GlossaryTerm))
        }
      ],
      "schemaRelationships": [
        {
          object ([SchemaRelationship](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaRelationship))
        }
      ],
      "userFunctions": {
        object ([UserFunctions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#UserFunctions))
      }
    }  
  
Fields  
---  
`systemInstruction` |  `string` Optional. The basic entry point for data owners creating domain knowledge for Agent.Why: Business jargon (e.g., YTD revenue is calculated as…, Retirement Age is 65 in the USA, etc) and system instructions (e.g., answer like a Pirate) can help the model understand the business context around a user question.  
`datasourceReferences` |  `object (`[DatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatasourceReferences)`)` Required. Data sources that are available for answering the question.  
`options` |  `object (`[ConversationOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ConversationOptions)`)` Optional. Additional options for the conversation.  
`exampleQueries[]` |  `object (`[ExampleQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ExampleQuery)`)` Optional. A list of example queries, providing examples of relevant and commonly used SQL queries and their corresponding natural language queries optionally present. Currently only used for BigQuery data sources and databases (alloydb, cloudsql, spanner) data sources.  
`lookerGoldenQueries[]` |  `object (`[LookerGoldenQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerGoldenQuery)`)` Optional. A list of golden queries, providing examples of relevant and commonly used Looker queries and their corresponding natural language queries optionally present. Only supported for Looker data sources.  
`glossaryTerms[]` |  `object (`[GlossaryTerm](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#GlossaryTerm)`)` Optional. Term definitions (currently, only user authored) Not supported for databases (alloydb, cloudsql, spanner) data sources.  
`schemaRelationships[]` |  `object (`[SchemaRelationship](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaRelationship)`)` Optional. Relationships between table schema, including referencing and referenced columns.  
`userFunctions` |  `object (`[UserFunctions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#UserFunctions)`)` Optional. A collection of user functions to be included in context.  
  
## DatasourceReferences

A collection of references to datasources.

JSON representation  
---  
      
    
    {
    
      // Union field references can be only one of the following:
      "bq": {
        object ([BigQueryTableReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryTableReferences))
      },
      "studio": {
        object ([StudioDatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#StudioDatasourceReferences))
      },
      "looker": {
        object ([LookerExploreReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerExploreReferences))
      },
      "alloydb": {
        object ([AlloyDbReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AlloyDbReference))
      },
      "spannerReference": {
        object ([SpannerReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SpannerReference))
      },
      "cloudSqlReference": {
        object ([CloudSqlReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#CloudSqlReference))
      }
      // End of list of possible types for union field references.
    }  
  
Fields  
---  
Union field `references`. The datasources to use. `references` can be only one of the following:  
`bq` |  `object (`[BigQueryTableReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryTableReferences)`)` References to BigQuery tables.  
`studio` |  `object (`[StudioDatasourceReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#StudioDatasourceReferences)`)` References to Looker Studio datasources.  
`looker` |  `object (`[LookerExploreReferences](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerExploreReferences)`)` References to Looker Explores.  
`alloydb` |  `object (`[AlloyDbReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AlloyDbReference)`)` Reference to an AlloyDB database. Only supported for the `QueryData` method.  
`spannerReference` |  `object (`[SpannerReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SpannerReference)`)` Reference to a Spanner database. Only supported for the `QueryData` method.  
`cloudSqlReference` |  `object (`[CloudSqlReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#CloudSqlReference)`)` Reference to a CloudSql database. Only supported for the `QueryData` method.  
  
## BigQueryTableReferences

Message representing references to BigQuery tables and property graphs. At least one of `tableReferences`, `propertyGraphReferences`, or `searchScope` must be populated.

JSON representation  
---  
      
    
    {
      "tableReferences": [
        {
          object ([BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryTableReference))
        }
      ],
      "propertyGraphReferences": [
        {
          object ([BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryPropertyGraphReference))
        }
      ]
    }  
  
Fields  
---  
`tableReferences[]` |  `object (`[BigQueryTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryTableReference)`)` Optional. References to BigQuery tables.  
`propertyGraphReferences[]` |  `object (`[BigQueryPropertyGraphReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryPropertyGraphReference)`)` Optional. References to BigQuery graphs.Note: "property graph" is the former name for BigQuery Graph. The field and message names retain the original term for backward compatibility; both refer to the same resource.  
  
## BigQueryTableReference

Message representing a reference to a single BigQuery table.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "tableId": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema))
      }
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project that the table belongs to.  
`datasetId` |  `string` Required. The dataset that the table belongs to.  
`tableId` |  `string` Required. The table id.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema)`)` Optional. The schema of the datasource.  
  
## Schema

The schema of a Datasource or QueryResult instance.

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Field))
        }
      ],
      "description": string,
      "synonyms": [
        string
      ],
      "tags": [
        string
      ],
      "displayName": string,
      "filters": [
        {
          object ([DataFilter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataFilter))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Field)`)` Optional. The fields in the schema.  
`description` |  `string` Optional. A textual description of the table's content and purpose. For example: "Contains information about customer orders in our e-commerce store." Currently only used for BigQuery data sources.  
`synonyms[]` |  `string` Optional. A list of alternative names or synonyms that can be used to refer to the table. For example: ["sales", "orders", "purchases"]. Currently only used for BigQuery data sources.  
`tags[]` |  `string` Optional. A list of tags or keywords associated with the table, used for categorization. For example: ["transaction", "revenue", "customer_data"]. Currently only used for BigQuery data sources.  
`displayName` |  `string` Optional. Table displayName (same as label in cloud/data_analytics/anarres/data/looker/proto/model_explore.proto), not required, currently only Looker has this field.  
`filters[]` |  `object (`[DataFilter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataFilter)`)` Optional. The filters on the datasource's underlying data. Currently only used for Looker data sources.  
  
## Field

A field in a schema.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "description": string,
      "mode": string,
      "synonyms": [
        string
      ],
      "tags": [
        string
      ],
      "displayName": string,
      "subfields": [
        {
          object ([Field](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Field))
        }
      ],
      "category": string,
      "valueFormat": string
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the field.  
`type` |  `string` Optional. The type of the field.  
`description` |  `string` Optional. A brief description of the field.  
`mode` |  `string` Optional. The mode of the field (e.g., NULLABLE, REPEATED).  
`synonyms[]` |  `string` Optional. A list of alternative names or synonyms that can be used to refer to this field. For example: ["id", "customerid", "cust_id"]. Currently only used for BigQuery data sources.  
`tags[]` |  `string` Optional. A list of tags or keywords associated with the field, used for categorization. For example: ["identifier", "customer", "pii"]. Currently only used for BigQuery data sources.  
`displayName` |  `string` Optional. Field displayName (same as label in  
`subfields[]` |  `object (`[Field](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Field)`)` Optional. Recursive property for nested schema structures.  
`category` |  `string` Optional. Field category, not required, currently only useful for Looker.  
`valueFormat` |  `string` Optional. Looker only. Value format of the field. Ref: <https://cloud.google.com/looker/docs/reference/param-field-value-format>  
  
## DataFilter

A filter on a datasource's underlying data. Filter syntax documentation: <https://cloud.google.com/looker/docs/filter-expressions>

JSON representation  
---  
      
    
    {
      "field": string,
      "value": string,
      "type": enum ([DataFilterType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataFilterType))
    }  
  
Fields  
---  
`field` |  `string` Optional. The field to filter on. For example: ["event_date", "customer_id", "product_category"]  
`value` |  `string` Optional. The default value used for this filter if the filter is not overridden in a query. For example: ["after 2024-01-01", "123", "-fashion"]  
`type` |  `enum (`[DataFilterType](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DataFilterType)`)` Optional. The type of filter present on a datasource, such as ALWAYS_FILTER.  
  
## DataFilterType

The type of filter present on a datasource, such as ALWAYS_FILTER.

Enums  
---  
`DATA_FILTER_TYPE_UNSPECIFIED` | The filter type was not specified.  
`ALWAYS_FILTER` | A filter that the user configures, and any queries to the Explore will always apply this filter by default. Currently only used for Looker data sources.  
  
## BigQueryPropertyGraphReference

Message representing a reference to a single BigQuery property graph.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "propertyGraphId": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project that the property graph belongs to.  
`datasetId` |  `string` Required. The dataset that the property graph belongs to.  
`propertyGraphId` |  `string` Required. The property graph id.  
  
## StudioDatasourceReferences

Message representing references to Looker Studio datasources.

JSON representation  
---  
      
    
    {
      "studioReferences": [
        {
          object ([StudioDatasourceReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#StudioDatasourceReference))
        }
      ]
    }  
  
Fields  
---  
`studioReferences[]` |  `object (`[StudioDatasourceReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#StudioDatasourceReference)`)` Optional. The references to the studio datasources.  
  
## StudioDatasourceReference

Message representing a reference to a single Looker Studio datasource.

JSON representation  
---  
      
    
    {
      "datasourceId": string
    }  
  
Fields  
---  
`datasourceId` |  `string` Required. The id of the datasource.  
  
## LookerExploreReferences

Message representing references to Looker explores.

JSON representation  
---  
      
    
    {
      "exploreReferences": [
        {
          object ([LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerExploreReference))
        }
      ],
      "credentials": {
        object ([Credentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Credentials))
      }
    }  
  
Fields  
---  
`exploreReferences[]` |  `object (`[LookerExploreReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerExploreReference)`)` Required. References to Looker explores.  
`credentials  
**(deprecated)**` |  `object (`[Credentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Credentials)`)` This item is deprecated!Optional. Deprecated: Use credentials in ChatRequest. The credentials to use when calling the Looker API.Currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk).  
  
## LookerExploreReference

Message representing a reference to a single Looker explore.

JSON representation  
---  
      
    
    {
      "lookmlModel": string,
      "explore": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema))
      },
    
      // Union field instance can be only one of the following:
      "lookerInstanceUri": string,
      "privateLookerInstanceInfo": {
        object ([PrivateLookerInstanceInfo](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#PrivateLookerInstanceInfo))
      }
      // End of list of possible types for union field instance.
    }  
  
Fields  
---  
`lookmlModel` |  `string` Required. Looker model, as outlined in [Major LookML structures](https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures). Name of the LookML model.  
`explore` |  `string` Required. Looker Explore, as outlined in [Major LookML structures](https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures). Name of the LookML Explore.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema)`)` Optional. The schema of the datasource.  
Union field `instance`. The instance of the Looker explore. `instance` can be only one of the following:  
`lookerInstanceUri` |  `string` Required. The base url of the Looker instance.  
`privateLookerInstanceInfo` |  `object (`[PrivateLookerInstanceInfo](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#PrivateLookerInstanceInfo)`)` Private Looker instance info.  
  
## PrivateLookerInstanceInfo

Message representing a private Looker instance info required if the Looker instance is behind a private network.

JSON representation  
---  
      
    
    {
      "lookerInstanceId": string,
      "serviceDirectoryName": string
    }  
  
Fields  
---  
`lookerInstanceId` |  `string` The Looker instance id.  
`serviceDirectoryName` |  `string` The service directory name of the Looker instance.  
  
## Credentials

Represents different forms of credential specification.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "oauth": {
        object ([OAuthCredentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#OAuthCredentials))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of credentials. `kind` can be only one of the following:  
`oauth` |  `object (`[OAuthCredentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#OAuthCredentials)`)` OAuth credentials.  
  
## OAuthCredentials

Represents OAuth credentials.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "secret": {
        object ([SecretBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SecretBased))
      },
      "token": {
        object ([TokenBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#TokenBased))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of OAuth credentials. `kind` can be only one of the following:  
`secret` |  `object (`[SecretBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SecretBased)`)` Secret-based OAuth credentials.  
`token` |  `object (`[TokenBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#TokenBased)`)` Token-based OAuth credentials.  
  
## SecretBased

The name of the secret containing the access token. Represents secret-based OAuth credentials.

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. An OAuth client ID.  
`clientSecret` |  `string` Required. An OAuth client secret.  
  
## TokenBased

Read more about Looker access tokens here: <https://developers.looker.com/api/advanced-usage/looker-api-oauth>

JSON representation  
---  
      
    
    {
      "accessToken": string
    }  
  
Fields  
---  
`accessToken` |  `string` Required. The name of the secret containing the access token.  
  
## AlloyDbReference

Message representing reference to an AlloyDB database and agent context. Only supported for the `QueryData` method.

JSON representation  
---  
      
    
    {
      "databaseReference": {
        object ([AlloyDbDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AlloyDbDatabaseReference))
      },
      "agentContextReference": {
        object ([AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference))
      }
    }  
  
Fields  
---  
`databaseReference` |  `object (`[AlloyDbDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AlloyDbDatabaseReference)`)` Required. Singular proto that supports specifying which database and tables to include.  
`agentContextReference` |  `object (`[AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference)`)` Optional. Parameters for retrieving data from Agent Context.  
  
## AlloyDbDatabaseReference

Message representing a reference to a single AlloyDB database.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "region": string,
      "clusterId": string,
      "instanceId": string,
      "databaseId": string,
      "tableIds": [
        string
      ],
      "databaseTableReferences": [
        {
          object ([DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference))
        }
      ]
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project the instance belongs to.  
`region` |  `string` Required. The region of the instance.  
`clusterId` |  `string` Required. The cluster id.  
`instanceId` |  `string` Required. The instance id.  
`databaseId` |  `string` Required. The database id.  
`tableIds[]` |  `string` Optional. The table ids. Denotes all tables if unset.  
`databaseTableReferences[]` |  `object (`[DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference)`)` Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query.  
  
## DatabaseTableReference

Message representing a table including its schema.

JSON representation  
---  
      
    
    {
      "tableId": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema))
      }
    }  
  
Fields  
---  
`tableId` |  `string` Required. The name of the table as defined in the database.Note: The precise rules for table naming, including valid characters, length limits, and case sensitivity, are determined by the specific database system.Requirements: - Exact Match: The provided name must be identical to the name stored in the database. - Case Sensitivity: Respect the case sensitivity rules of the specific database system and how the table was created. For example, "Orders" and "orders" may be distinct table names. - Special Characters/Keywords: If the table name includes spaces, special characters, or is a database reserved keyword, provide the literal name as it is stored. Do not add any database-specific identifier quoting characters (e.g., ", `, []).Examples: - Simple name: "orders", "UserActivity" - Case sensitive: "MyTable" - Name with spaces: "Order Details" - Name with other special characters: "user/data", "order-items" - Name that is a keyword: "Group", "Order"Permissions: The caller's credentials must have the necessary database permissions to access the table's schema and data.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Schema)`)` Optional. The schema of the table.  
  
## AgentContextReference

Message representing a reference to Agent Context.

JSON representation  
---  
      
    
    {
      "contextSetId": string
    }  
  
Fields  
---  
`contextSetId` |  `string` Required. Context set ID to retrieve.  
  
## SpannerReference

Message representing reference to a Spanner database and agent context. Only supported for the `QueryData` method.

JSON representation  
---  
      
    
    {
      "databaseReference": {
        object ([SpannerDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SpannerDatabaseReference))
      },
      "agentContextReference": {
        object ([AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference))
      }
    }  
  
Fields  
---  
`databaseReference` |  `object (`[SpannerDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SpannerDatabaseReference)`)` Required. Singular proto that supports specifying which database and tables to include.  
`agentContextReference` |  `object (`[AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference)`)` Optional. Parameters for retrieving data from Agent Context.  
  
## SpannerDatabaseReference

Message representing a reference to a single Spanner database.

JSON representation  
---  
      
    
    {
      "engine": enum ([Engine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Engine)),
      "projectId": string,
      "instanceId": string,
      "databaseId": string,
      "tableIds": [
        string
      ],
      "databaseTableReferences": [
        {
          object ([DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference))
        }
      ],
      "priority": string,
      "requestTag": string
    }  
  
Fields  
---  
`engine` |  `enum (`[Engine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Engine)`)` Required. The engine of the Spanner instance.  
`projectId` |  `string` Required. The project the instance belongs to.  
`instanceId` |  `string` Required. The instance id.  
`databaseId` |  `string` Required. The database id.  
`tableIds[]` |  `string` Optional. The table ids. Denotes all tables if unset.  
`databaseTableReferences[]` |  `object (`[DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference)`)` Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query.  
`priority` |  `string` Optional. Priority for the queries to Spanner. Should be a value supported by Cloud Spanner e.g.: LOW, MEDIUM, HIGH. Unsupported values will be ignored. See <https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority> for complete list.  
`requestTag` |  `string` Tag to be attached to all queries to Spanner. Allows to identify and monitor queries sent to Spanner by the GDA service.  
  
## Engine

The database engine.

Enums  
---  
`ENGINE_UNSPECIFIED` | Engine is not specified.  
`GOOGLE_SQL` | Google SQL  
`POSTGRESQL` | PostgreSQL  
  
## CloudSqlReference

Message representing reference to a CloudSQL database and agent context. Only supported for the `QueryData` method.

JSON representation  
---  
      
    
    {
      "databaseReference": {
        object ([CloudSqlDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#CloudSqlDatabaseReference))
      },
      "agentContextReference": {
        object ([AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference))
      }
    }  
  
Fields  
---  
`databaseReference` |  `object (`[CloudSqlDatabaseReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#CloudSqlDatabaseReference)`)` Required. Singular proto that supports specifying which database and tables to include.  
`agentContextReference` |  `object (`[AgentContextReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AgentContextReference)`)` Optional. Parameters for retrieving data from Agent Context.  
  
## CloudSqlDatabaseReference

Message representing a reference to a single CloudSQL database.

JSON representation  
---  
      
    
    {
      "engine": enum ([Engine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Engine_1)),
      "projectId": string,
      "region": string,
      "instanceId": string,
      "databaseId": string,
      "tableIds": [
        string
      ],
      "databaseTableReferences": [
        {
          object ([DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference))
        }
      ]
    }  
  
Fields  
---  
`engine` |  `enum (`[Engine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Engine_1)`)` Required. The engine of the Cloud SQL instance.  
`projectId` |  `string` Required. The project the instance belongs to.  
`region` |  `string` Required. The region of the instance.  
`instanceId` |  `string` Required. The instance id.  
`databaseId` |  `string` Required. The database id.  
`tableIds[]` |  `string` Optional. The table ids. Denotes all tables if unset.  
`databaseTableReferences[]` |  `object (`[DatabaseTableReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatabaseTableReference)`)` Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query.  
  
## Engine

The database engine.

Enums  
---  
`ENGINE_UNSPECIFIED` | Engine is not specified.  
`POSTGRESQL` | PostgreSQL  
`MYSQL` | MySQL  
  
## ConversationOptions

Options for the conversation.

JSON representation  
---  
      
    
    {
      "chart": {
        object ([ChartOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ChartOptions))
      },
      "analysis": {
        object ([AnalysisOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AnalysisOptions))
      },
      "datasource": {
        object ([DatasourceOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatasourceOptions))
      },
      "model": enum ([Model](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Model))
    }  
  
Fields  
---  
`chart` |  `object (`[ChartOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ChartOptions)`)` Optional. Options for chart generation.  
`analysis` |  `object (`[AnalysisOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#AnalysisOptions)`)` Optional. Options for analysis.  
`datasource` |  `object (`[DatasourceOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#DatasourceOptions)`)` Optional. Options for datasources.  
`model` |  `enum (`[Model](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Model)`)` Optional. The model to use for the agent loop.  
  
## ChartOptions

Options for chart generation.

JSON representation  
---  
      
    
    {
      "image": {
        object ([ImageOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ImageOptions))
      }
    }  
  
Fields  
---  
`image` |  `object (`[ImageOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#ImageOptions)`)` Optional. When specified, the agent will render generated charts using the provided format. Defaults to no image.  
  
## ImageOptions

Options for rendering images of generated charts.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "noImage": {
        object ([NoImage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#NoImage))
      },
      "svg": {
        object ([SvgOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SvgOptions))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of image to render. `kind` can be only one of the following:  
`noImage` |  `object (`[NoImage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#NoImage)`)` No image.  
`svg` |  `object (`[SvgOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SvgOptions)`)` SVG format.  
  
## NoImage

This type has no fields.

No image.

## SvgOptions

This type has no fields.

SVG options.

## AnalysisOptions

Options for analysis.

JSON representation  
---  
      
    
    {
      "python": {
        object ([Python](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Python))
      }
    }  
  
Fields  
---  
`python` |  `object (`[Python](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Python)`)` Optional. Options for Python analysis.  
  
## Python

Options for Python analysis.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether to enable Python analysis. Defaults to false.  
  
## DatasourceOptions

Options for datasources configurations.

JSON representation  
---  
      
    
    {
      "bigQueryMaxBilledBytes": string
    }  
  
Fields  
---  
`bigQueryMaxBilledBytes` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Optional. This option applies to datasources that require BigQuery queries only. Limits the bytes billed for each BigQuery query job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge). If unspecified, no limit will be applied.  
  
## Model

Allowed models for the agent/conversation.

Enums  
---  
`MODEL_UNSPECIFIED` | No model specified. The model may be set on the chat request, or the default model will be used.  
`LATEST_GA_MODEL` | Use the most up-to-date non-preview model. This may constrain certain request level settings.  
  
## ExampleQuery

Example of relevant and commonly used SQL query and its corresponding natural language queries optionally present. Currently only used for BigQuery data sources.

JSON representation  
---  
      
    
    {
      "naturalLanguageQuestion": string,
      "parameters": [
        {
          object ([QueryParameter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#QueryParameter))
        }
      ],
    
      // Union field query can be only one of the following:
      "sqlQuery": string
      // End of list of possible types for union field query.
    }  
  
Fields  
---  
`naturalLanguageQuestion` |  `string` Optional. A natural language question that a user might ask. For example: "How many orders were placed last month?"  
`parameters[]` |  `object (`[QueryParameter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#QueryParameter)`)` Optional. The list of query parameters. Example: The parameterized SQL query "SELECT * FROM my_table WHERE id = @id" can be matched with any value of id.  
Union field `query`. The SQL or Looker query that should be generated to answer the natural language query. `query` can be only one of the following:  
`sqlQuery` |  `string` Optional. The SQL query that should be generated to answer the natural language question. For example: "SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31'"  
  
## QueryParameter

A query parameter message represents a parameter that can be used to parameterize a SQL query.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "dataType": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the parameter reference in the SQL query.  
`description` |  `string` Optional. The description of the parameter that can be used by LLM to extract the parameter value from the user question.  
`dataType` |  `string` Required. The data type of the parameter, e.g. "STRING", "INT64", "DATE", etc. For valid values, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types). This will be used to populate google.cloud.bigquery.v2.QueryParameterType.type.  
  
## LookerGoldenQuery

A golden query for Looker, including natural language questions and a corresponding Looker Query. Analogous to ExampleQuery.

JSON representation  
---  
      
    
    {
      "naturalLanguageQuestions": [
        string
      ],
      "lookerQuery": {
        object ([LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerQuery))
      }
    }  
  
Fields  
---  
`naturalLanguageQuestions[]` |  `string` Optional. Natural language questions that a user might ask. For example: "How many orders were placed last month?"  
`lookerQuery` |  `object (`[LookerQuery](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#LookerQuery)`)` Optional. The Looker Query corresponding to the natural language questions.  
  
## LookerQuery

Looker Query Object [Looker API documentation](https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_inline_query).

JSON representation  
---  
      
    
    {
      "model": string,
      "explore": string,
      "fields": [
        string
      ],
      "filters": [
        {
          object ([Filter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Filter))
        }
      ],
      "sorts": [
        string
      ],
      "limit": string,
      "queryId": string,
      "clientId": string
    }  
  
Fields  
---  
`model` |  `string` Required. The LookML model used to generate the query.  
`explore` |  `string` Required. The LookML explore used to generate the query.  
`fields[]` |  `string` Optional. The fields to retrieve from the explore.  
`filters[]` |  `object (`[Filter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Filter)`)` Optional. The filters to apply to the explore.  
`sorts[]` |  `string` Optional. The sorts to apply to the explore.  
`limit` |  `string` Optional. Limit in the query.  
`queryId` |  `string` Optional. The primary identifier for the query resource in Looker, used for API operations. Maps to `id` (or `slug`) in the Looker API `Query` resource.  
`clientId` |  `string` Optional. The short alphanumeric identifier for the query, used for share links and Explore URLs (e.g., in the `qid` parameter). Maps to `clientId` in the Looker API `Query` resource.  
  
## Filter

A Looker query filter.

JSON representation  
---  
      
    
    {
      "field": string,
      "value": string
    }  
  
Fields  
---  
`field` |  `string` Required. The field to filter on.  
`value` |  `string` Optional. The value for the field to filter on. Optional so we can preserve the default value as an empty string, important to get a valid and working Looker Explore url.  
  
## GlossaryTerm

Definition of a term within a specific domain.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
      "labels": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Required. User friendly display name of the glossary term being defined. For example: "CTR", "conversion rate", "pending"  
`description` |  `string` Required. The description or meaning of the term. For example: "Click-through rate", "The percentage of users who complete a desired action", "An order that is waiting to be processed."  
`labels[]` |  `string` Optional. A list of general purpose labels associated to this term. For example: ["click rate", "clickthrough", "waiting"]  
  
## SchemaRelationship

The relationship between two tables, including referencing and referenced columns. This is a derived context retrieved from Dataplex Dataset Insights.

JSON representation  
---  
      
    
    {
      "leftSchemaPaths": {
        object ([SchemaPaths](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaPaths))
      },
      "rightSchemaPaths": {
        object ([SchemaPaths](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaPaths))
      },
      "sources": [
        enum ([Source](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Source))
      ],
      "confidenceScore": number
    }  
  
Fields  
---  
`leftSchemaPaths` |  `object (`[SchemaPaths](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaPaths)`)` An ordered list of fields for the join from the first table. The size of this list must be the same as `rightSchemaPaths`. Each field at index i in this list must correspond to a field at the same index in the `rightSchemaPaths` list.  
`rightSchemaPaths` |  `object (`[SchemaPaths](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#SchemaPaths)`)` An ordered list of fields for the join from the second table. The size of this list must be the same as `leftSchemaPaths`. Each field at index i in this list must correspond to a field at the same index in the `leftSchemaPaths` list.  
`sources[]` |  `enum (`[Source](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#Source)`)` Optional. Sources which generated the schema relation edge.  
`confidenceScore` |  `number` Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score.  
  
## SchemaPaths

Represents an ordered set of paths within the table schema.

JSON representation  
---  
      
    
    {
      "tableFqn": string,
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`tableFqn` |  `string` The service-qualified full resource name of the table Ex: bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID  
`paths[]` |  `string` The ordered list of paths within the table schema.  
  
## Source

Source which generated the schema relation edge.

Enums  
---  
`SOURCE_UNSPECIFIED` | The source of the schema relationship is unspecified.  
`BIGQUERY_JOB_HISTORY` | The source of the schema relationship is BigQuery job history.  
`LLM_SUGGESTED` | The source of the schema relationship is LLM suggested.  
`BIGQUERY_TABLE_CONSTRAINTS` | The source of the schema relationship is BigQuery table constraints.  
  
## UserFunctions

A collection of user functions to be included in context.

JSON representation  
---  
      
    
    {
      "bqRoutines": [
        {
          object ([BigQueryRoutine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryRoutine))
        }
      ]
    }  
  
Fields  
---  
`bqRoutines[]` |  `object (`[BigQueryRoutine](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryRoutine)`)` A list of BigQuery routines to include in the context.  
  
## BigQueryRoutine

A reference to a BigQuery routine.

JSON representation  
---  
      
    
    {
      "routineReference": {
        object ([BigQueryRoutineReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryRoutineReference))
      },
      "description": string
    }  
  
Fields  
---  
`routineReference` |  `object (`[BigQueryRoutineReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#BigQueryRoutineReference)`)` The reference to the BigQuery routine.  
`description` |  `string` User override or addition to description, to tell the agent when to use the UDF.  
  
## BigQueryRoutineReference

A reference to a BigQuery routine.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "routineId": string
    }  
  
Fields  
---  
`projectId` |  `string` The project ID of the routine.  
`datasetId` |  `string` The dataset ID of the routine.  
`routineId` |  `string` The routine ID of the routine.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/create)`

|  Creates a new DataAgent in a given project and location.  
  
### `[createSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/createSync)`

|  Creates a new DataAgent in a given project and location synchronously.  
  
### `[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/delete)`

|  Deletes a single DataAgent.  
  
### `[deleteSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/deleteSync)`

|  Deletes a single DataAgent synchronously.  
  
### `[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/get)`

|  Gets details of a single DataAgent.  
  
### `[getIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/getIamPolicy)`

|  Gets the IAM policy for DataAgent  
  
### `[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/list)`

|  Lists DataAgents in a given project and location.  
  
### `[listAccessible](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/listAccessible)`

|  Lists DataAgents that are accessible to the caller in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/patch)`

|  Updates the parameters of a single DataAgent.  
  
### `[setIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/setIamPolicy)`

|  Sets the IAM policy for a DataAgent.  
  
### `[updateSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/updateSync)`

|  Updates the parameters of a single DataAgent synchronously.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
