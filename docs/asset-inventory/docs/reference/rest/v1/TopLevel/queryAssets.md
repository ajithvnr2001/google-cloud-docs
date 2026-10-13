---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets/
title: Method: queryAssets \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.221274+00:00
---

# Method: queryAssets  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: queryAssets Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * QueryAssetsOutputConfig
    * JSON representation
  * BigQueryDestination
    * JSON representation
  * QueryResult
    * JSON representation
  * TableSchema
    * JSON representation
  * TableFieldSchema
    * JSON representation
  * Try it!



Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).

If the query execution finishes within timeout and there's no pagination, the full query results will be returned in the `QueryAssetsResponse`.

Otherwise, full query results can be obtained by issuing extra requests with the `jobReference` from the a previous `v1.queryAssets` call.

Note, the query result has approximately 10 GB limitation enforced by [BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-output). Queries return larger results will result in errors.

### HTTP request

`POST https://cloudasset.googleapis.com/v1/{parent=*/*}:queryAssets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123").Only assets belonging to the `parent` will be returned.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string,
      "timeout": string,
      "outputConfig": {
        object ([QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryAssetsOutputConfig))
      },
    
      // Union field query can be only one of the following:
      "statement": string,
      "jobReference": string
      // End of list of possible types for union field query.
    
      // Union field time can be only one of the following:
      "readTimeWindow": {
        object ([TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TimeWindow))
      },
      "readTime": string
      // End of list of possible types for union field time.
    }  
  
Fields  
---  
`pageSize` |  `integer` Optional. The maximum number of rows to return in the results. Responses are limited to 10 MB and 1000 rows.By default, the maximum row count is 1000. When the byte or row count limit is reached, the rest of the query results will be paginated.The field will be ignored when [outputConfig] is specified.  
`pageToken` |  `string` Optional. A page token received from previous `v1.queryAssets`.The field will be ignored when [outputConfig] is specified.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Specifies the maximum amount of time that the client is willing to wait for the query to complete. By default, this limit is 5 min for the first query, and 1 minute for the following queries. If the query is complete, the `done` field in the `QueryAssetsResponse` is true, otherwise false.Like BigQuery [jobs.query API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#queryrequest) The call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete.The field will be ignored when [outputConfig] is specified.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`outputConfig` |  `object (`[QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryAssetsOutputConfig)`)` Optional. Destination where the query results will be saved.When this field is specified, the query results won't be saved in the [QueryAssetsResponse.query_result]. Instead [QueryAssetsResponse.output_config] will be set.Meanwhile, [QueryAssetsResponse.job_reference] will be set and can be used to check the status of the query job when passed to a following [v1.queryAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets) API call.  
Union field `query`.`query` can be only one of the following:  
`statement` |  `string` Optional. A SQL statement that's compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).  
`jobReference` |  `string` Optional. Reference to the query job, which is from the `QueryAssetsResponse` of previous `v1.queryAssets` call.  
Union field `time`. Specifies what time period or point in time to query asset metadata at. * unset - query asset metadata as it is right now * [read_time_window] - query asset metadata as it was at any point in time between [start_time] and [end_time]. * [read_time] - query asset metadata as it was at that point in time. If data for the timestamp/date range selected does not exist, it will simply return a valid response with no rows. `time` can be only one of the following:  
`readTimeWindow` |  `object (`[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TimeWindow)`)` Optional. [startTime] is required. [startTime] must be less than [endTime] Defaults [endTime] to now if [startTime] is set and [endTime] isn't. Maximum permitted time range is 7 days.  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Queries cloud assets as they appeared at the specified point in time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Response body

v1.queryAssets response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "jobReference": string,
      "done": boolean,
    
      // Union field response can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation#Status))
      },
      "queryResult": {
        object ([QueryResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryResult))
      },
      "outputConfig": {
        object ([QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryAssetsOutputConfig))
      }
      // End of list of possible types for union field response.
    }  
  
Fields  
---  
`jobReference` |  `string` Reference to a query job.  
`done` |  `boolean` The query response, which can be either an `error` or a valid `response`.If `done` == `false` and the query result is being saved in an output, the outputConfig field will be set. If `done` == `true`, exactly one of `error`, `queryResult` or `outputConfig` will be set. [done] is unset unless the [QueryAssetsResponse] contains a [QueryAssetsResponse.job_reference].  
Union field `response`.`response` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation#Status)`)` Error status.  
`queryResult` |  `object (`[QueryResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryResult)`)` Result of the query.  
`outputConfig` |  `object (`[QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#QueryAssetsOutputConfig)`)` Output configuration, which indicates that instead of being returned in an API response on the fly, the query result will be saved in a specific output.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## QueryAssetsOutputConfig

Output configuration query assets.

JSON representation  
---  
      
    
    {
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#BigQueryDestination))
      }
    }  
  
Fields  
---  
`bigqueryDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#BigQueryDestination)`)` BigQuery destination where the query results will be saved.  
  
## BigQueryDestination

BigQuery destination.

JSON representation  
---  
      
    
    {
      "dataset": string,
      "table": string,
      "writeDisposition": string
    }  
  
Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset where the query results will be saved. It has the format of "projects/{projectId}/datasets/{datasetId}".  
`table` |  `string` Required. The BigQuery table where the query results will be saved. If this table does not exist, a new table with the given name will be created.  
`writeDisposition` |  `string` Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result.

The default value is WRITE_EMPTY.  
  
## QueryResult

Execution results of the query.

The result is formatted as rows represented by BigQuery compatible [schema]. When pagination is necessary, it will contains the page token to retrieve the results of following pages.

JSON representation  
---  
      
    
    {
      "rows": [
        {
          object
        }
      ],
      "schema": {
        object ([TableSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableSchema))
      },
      "nextPageToken": string,
      "totalRows": string
    }  
  
Fields  
---  
`rows[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Each row hold a query result in the format of `Struct`.  
`schema` |  `object (`[TableSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableSchema)`)` Describes the format of the [rows].  
`nextPageToken` |  `string` Token to retrieve the next page of the results.  
`totalRows` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total rows of the whole query results.  
  
## TableSchema

BigQuery Compatible table schema.

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableFieldSchema))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableFieldSchema)`)` Describes the fields in a table.  
  
## TableFieldSchema

A field in TableSchema.

JSON representation  
---  
      
    
    {
      "field": string,
      "type": string,
      "mode": string,
      "fields": [
        {
          object ([TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableFieldSchema))
        }
      ]
    }  
  
Fields  
---  
`field` |  `string` The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.  
`type` |  `string` The field data type. Possible values include * STRING * BYTES * INTEGER * FLOAT * BOOLEAN * TIMESTAMP * DATE * TIME * DATETIME * GEOGRAPHY, * NUMERIC, * BIGNUMERIC, * RECORD (where RECORD indicates that the field contains a nested schema).  
`mode` |  `string` The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.  
`fields[]` |  `object (`[TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets#TableFieldSchema)`)` Describes the nested schema fields if the type property is set to RECORD.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
