---
url: https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery/
title: Method: projects.runAggregationQuery \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:26.323286+00:00
---

# Method: projects.runAggregationQuery  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Reference ](https://docs.cloud.google.com/datastore/docs/apis)



Send feedback 

#  Method: projects.runAggregationQuery Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * AggregationQuery
    * JSON representation
  * Aggregation
    * JSON representation
  * Count
    * JSON representation
  * Sum
    * JSON representation
  * Avg
    * JSON representation
  * AggregationResultBatch
    * JSON representation
  * AggregationResult
    * JSON representation
  * Try it!



Runs an aggregation query.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 eu us

  
`POST https://datastore.googleapis.com/v1beta3/projects/{projectId}:runAggregationQuery`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` Required. The ID of the project against which to make the request.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "partitionId": {
        object (PartitionId)
      },
      "readOptions": {
        object ([ReadOptions](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ReadOptions))
      },
      "explainOptions": {
        object ([ExplainOptions](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ExplainOptions))
      },
    
      // Union field query_type can be only one of the following:
      "aggregationQuery": {
        object ([AggregationQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationQuery))
      },
      "gqlQuery": {
        object ([GqlQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/GqlQuery))
      }
      // End of list of possible types for union field query_type.
    }  
  
Fields  
---  
`partitionId` |  `object (`PartitionId`)` Entities are partitioned into subsets, identified by a partition ID. Queries are scoped to a single partition. This partition ID is normalized with the standard default context partition ID.  
`readOptions` |  `object (`[ReadOptions](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ReadOptions)`)` The options for this query.  
`explainOptions` |  `object (`[ExplainOptions](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ExplainOptions)`)` Optional. Explain options for the query. If set, additional query statistics will be returned. If not, only query results will be returned.  
Union field `query_type`. The type of query. `query_type` can be only one of the following:  
`aggregationQuery` |  `object (`[AggregationQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationQuery)`)` The query to run.  
`gqlQuery` |  `object (`[GqlQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/GqlQuery)`)` The GQL query to run. This query must be an aggregation query.  
  
### Response body

The response for `[Datastore.RunAggregationQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#google.datastore.v1beta3.Datastore.RunAggregationQuery)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "batch": {
        object ([AggregationResultBatch](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationResultBatch))
      },
      "query": {
        object ([AggregationQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationQuery))
      },
      "explainMetrics": {
        object ([ExplainMetrics](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ExplainMetrics))
      }
    }  
  
Fields  
---  
`batch` |  `object (`[AggregationResultBatch](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationResultBatch)`)` A batch of aggregation results. Always present.  
`query` |  `object (`[AggregationQuery](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationQuery)`)` The parsed form of the `GqlQuery` from the request, if it was set.  
`explainMetrics` |  `object (`[ExplainMetrics](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/ExplainMetrics)`)` Query explain metrics. This is only present when the `[RunAggregationQueryRequest.explain_options](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#body.request_body.FIELDS.explain_options)` is provided, and it is sent only once with the last response in the stream.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/datastore`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AggregationQuery

Datastore query for running an aggregation over a `[Query](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/Query)`.

JSON representation  
---  
      
    
    {
      "aggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Aggregation))
        }
      ],
    
      // Union field query_type can be only one of the following:
      "nestedQuery": {
        object ([Query](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/Query))
      }
      // End of list of possible types for union field query_type.
    }  
  
Fields  
---  
`aggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Aggregation)`)` Optional. Series of aggregations to apply over the results of the `nestedQuery`.Requires:

  * A minimum of one and maximum of five aggregations per query.

  
Union field `query_type`. The base query to aggregate over. `query_type` can be only one of the following:  
`nestedQuery` |  `object (`[Query](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/Query)`)` Nested query for aggregation  
  
## Aggregation

Defines an aggregation that produces a single result.

JSON representation  
---  
      
    
    {
      "alias": string,
    
      // Union field operator can be only one of the following:
      "count": {
        object ([Count](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Count))
      },
      "sum": {
        object ([Sum](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Sum))
      },
      "avg": {
        object ([Avg](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Avg))
      }
      // End of list of possible types for union field operator.
    }  
  
Fields  
---  
`alias` |  `string` Optional. Optional name of the property to store the result of the aggregation.If not provided, Datastore will pick a default name following the format `property_<incremental_id++>`. For example:
    
    
    AGGREGATE
      COUNT_UP_TO(1) AS count_up_to_1,
      COUNT_UP_TO(2),
      COUNT_UP_TO(3) AS count_up_to_3,
      COUNT(*)
    OVER (
      ...
    );
    

becomes:
    
    
    AGGREGATE
      COUNT_UP_TO(1) AS count_up_to_1,
      COUNT_UP_TO(2) AS property_1,
      COUNT_UP_TO(3) AS count_up_to_3,
      COUNT(*) AS property_2
    OVER (
      ...
    );
    

Requires:

  * Must be unique across all aggregation aliases.
  * Conform to `entity property name` limitations.

  
Union field `operator`. The type of aggregation to perform, required. `operator` can be only one of the following:  
`count` |  `object (`[Count](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Count)`)` Count aggregator.  
`sum` |  `object (`[Sum](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Sum)`)` Sum aggregator.  
`avg` |  `object (`[Avg](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Avg)`)` Average aggregator.  
  
## Count

Count of entities that match the query.

The `COUNT(*)` aggregation function operates on the entire entity so it does not require a field reference.

JSON representation  
---  
      
    
    {
      "upTo": string
    }  
  
Fields  
---  
`upTo` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Optional. Optional constraint on the maximum number of entities to count.This provides a way to set an upper bound on the number of entities to scan, limiting latency, and cost.Unspecified is interpreted as no bound.If a zero value is provided, a count result of zero should always be expected.High-Level Example:
    
    
    AGGREGATE COUNT_UP_TO(1000) OVER ( SELECT * FROM k );
    

Requires:

  * Must be non-negative when present.

  
  
## Sum

Sum of the values of the requested property.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns 0.

  * Returns a 64-bit integer if all aggregated numbers are integers and the sum result does not overflow. Otherwise, the result is returned as a double. Note that even if all the aggregated values are integers, the result is returned as a double if it cannot fit within a 64-bit signed integer. When this occurs, the returned value will lose precision.

  * When underflow occurs, floating-point aggregation is non-deterministic. This means that running the same query repeatedly without any changes to the underlying values could produce slightly different results each time. In those cases, values should be stored as integers over floating-point numbers.


JSON representation  
---  
      
    
    {
      "property": {
        object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/PropertyReference))
      }
    }  
  
Fields  
---  
`property` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/PropertyReference)`)` The property to aggregate on.  
  
## Avg

Average of the values of the requested property.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns `NULL`.

  * Always returns the result as a double.


JSON representation  
---  
      
    
    {
      "property": {
        object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/PropertyReference))
      }
    }  
  
Fields  
---  
`property` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/PropertyReference)`)` The property to aggregate on.  
  
## AggregationResultBatch

A batch of aggregation results produced by an aggregation query.

JSON representation  
---  
      
    
    {
      "aggregationResults": [
        {
          object ([AggregationResult](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationResult))
        }
      ],
      "moreResults": enum ([MoreResultsType](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/MoreResultsType)),
      "readTime": string
    }  
  
Fields  
---  
`aggregationResults[]` |  `object (`[AggregationResult](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#AggregationResult)`)` The aggregation results for this batch.  
`moreResults` |  `enum (`[MoreResultsType](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/MoreResultsType)`)` The state of the query after the current batch. Only COUNT(*) aggregations are supported in the initial launch. Therefore, expected result type is limited to `NO_MORE_RESULTS`.  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Read timestamp this batch was returned from.In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch's read timestamp is valid for all preceding batches.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AggregationResult

The result of a single bucket from a Datastore aggregation query.

The keys of `aggregateProperties` are the same for all results in an aggregation query, unlike entity queries which can have different fields present for each result.

JSON representation  
---  
      
    
    {
      "aggregateProperties": {
        string: {
          object (Value)
        },
        ...
      }
    }  
  
Fields  
---  
`aggregateProperties` |  `map (key: string, value: object (`Value`))` The result of the aggregation functions, ex: `COUNT(*) AS total_entities`.The key is the `[alias](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1beta3/projects/runAggregationQuery#Aggregation.FIELDS.alias)` assigned to the aggregation function on input and the size of this map equals the number of aggregation functions in the query.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 
