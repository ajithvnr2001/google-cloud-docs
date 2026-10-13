---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch/
title: Method: instances.udmSearch \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:27.909322+00:00
---

# Method: instances.udmSearch  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.udmSearch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * QueryDialect
  * StatsData
    * JSON representation
  * StatsColumnData
    * JSON representation
  * StatsColumnType
    * JSON representation
  * StatsColumnValue
    * JSON representation
  * StatsList
    * JSON representation



**Full name** : projects.locations.instances.udmSearch

Performs a UDM search that returns matching events for the query.

### HTTP request

`GET https://{endpoint}/v1/{instance}:udmSearch`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`query` |  `string` Required. The boolean query to search for. Example: 'ip=/172.*/ AND metadata.event_type!="NETWORK_CONNECTION" AND ( target.ip = "3.225.179.73" OR target.ip = "23.47.48.70")'  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. Time range to search for [Inclusive start time, exclusive end time).  
`limit` |  `integer` Maximum number of results to be returned for the query. Anything over 10000 will be coerced to 10000.  
`queryDialect` |  `enum (`[QueryDialect](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#QueryDialect)`)` Optional. Specifies the language that the query string is written in.  
`simulatedDataVisibility` |  `enum (`[SimulatedDataVisibility](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/SimulatedDataVisibility)`)` Optional. Specifies visibility of simulated data to include in search results.  
  
### Request body

The request body must be empty.

### Response body

Returns results matching the query and time range in UdmSearchRequest.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "events": [
        {
          object ([Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events#Event))
        }
      ],
      "moreDataAvailable": boolean,
      "stats": {
        object ([StatsData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsData))
      }
    }  
  
Fields  
---  
`events[]` |  `object (`[Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events#Event)`)` List of matched events.  
`moreDataAvailable` |  `boolean` Too many events matched the search criterion, some results have been omitted.  
`stats` |  `object (`[StatsData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsData)`)` Stats response for the query.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.events.udmSearch`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## QueryDialect

Specifies the dialect a UDM Search Query is written in.

Enums  
---  
`QUERY_DIALECT_UNSPECIFIED` | Defaults to YL2.  
`YL2` | YL2 query dialect.  
`SQL` | SQL query dialect.  
  
## StatsData

Stats results when the query is for statistics

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([StatsColumnData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnData))
        }
      ],
      "tooManyResults": boolean,
      "hasJoin": boolean,
      "hasDataTable": boolean
    }  
  
Fields  
---  
`results[]` |  `object (`[StatsColumnData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnData)`)` Result rows that are queried.  
`tooManyResults` |  `boolean` If true, there are too many results to return and some have been omitted.  
`hasJoin` |  `boolean` Indicates to the frontend that the result is a join-stats result.  
`hasDataTable` |  `boolean` Indicates to the frontend that the result contains a data-table.  
  
## StatsColumnData

Represents a single column in the set of columns returned as the stats query result.

JSON representation  
---  
      
    
    {
      "column": string,
      "values": [
        {
          object ([StatsColumnType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnType))
        }
      ]
    }  
  
Fields  
---  
`column` |  `string` Used to store column names.  
`values[]` |  `object (`[StatsColumnType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnType)`)` Store list of values in a column.  
  
## StatsColumnType

Singular vs list of values in a column.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "value": {
        object ([StatsColumnValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnValue))
      },
      "list": {
        object ([StatsList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsList))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Store single value or list of values in a column. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`value` |  `object (`[StatsColumnValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnValue)`)` Single value in a column.  
`list` |  `object (`[StatsList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsList)`)` List of values in a column e.g. IPs  
End of mutually exclusive fields.  
  
## StatsColumnValue

Represents a single value in the set of values returned as the stats query result.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "nullVal": boolean,
      "boolVal": boolean,
      "bytesVal": string,
      "doubleVal": number,
      "int64Val": string,
      "uint64Val": string,
      "stringVal": string,
      "timestampVal": string,
      "dateVal": {
        object ([Date](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Date))
      },
      "protoVal": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Value of the column based on data type The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`nullVal` |  `boolean` True if the value is NULL.  
`boolVal` |  `boolean` Boolean value.  
`bytesVal` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Bytes value.A base64-encoded string.  
`doubleVal` |  `number` Double value.  
`int64Val` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Integer value (signed).  
`uint64Val` |  `string` Un-signed integer value.  
`stringVal` |  `string` String value. Enum values are returned as strings.  
`timestampVal` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp values.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dateVal` |  `object (`[Date](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Date)`)` Date values.  
`protoVal` |  `object` For any proto values that are not any of the above.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
End of mutually exclusive fields.  
  
## StatsList

Store list of values in a column.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([StatsColumnValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnValue))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[StatsColumnValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch#StatsColumnValue)`)` List of values in one cell of the column.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
