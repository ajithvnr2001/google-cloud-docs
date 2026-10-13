---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats/
title: Method: organizations.environments.securityStats.queryTimeSeriesStats \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:51.528636+00:00
---

# Method: organizations.environments.securityStats.queryTimeSeriesStats  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.securityStats.queryTimeSeriesStats Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * WindowSize
  * Sequence
    * JSON representation
  * Try it!



Retrieve security statistics as a collection of time series.

### HTTP request

`POST https://apigee.googleapis.com/v1/{orgenv=organizations/*/environments/*}/securityStats:queryTimeSeriesStats`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`orgenv` |  `string` Required. Should be of the form organizations//environments/.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dimensions": [
        string
      ],
      "metrics": [
        {
          object ([MetricAggregation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/MetricAggregation))
        }
      ],
      "filter": string,
      "windowSize": enum ([WindowSize](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats#WindowSize)),
      "timeRange": {
        object ([Interval](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Interval))
      },
      "timestampOrder": enum ([Order](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Order)),
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`dimensions[]` |  `string` List of dimension names to group the aggregations by. If no dimensions are passed, a single trend line representing the requested metric aggregations grouped by environment is returned.  
`metrics[]` |  `object (`[MetricAggregation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/MetricAggregation)`)` Required. List of metrics and their aggregations.  
`filter` |  `string` Filter further on specific dimension values. Follows the same grammar as custom report's filter expressions. Example, apiproxy eq 'foobar'. <https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters>  
`windowSize` |  `enum (`[WindowSize](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats#WindowSize)`)` Time buckets to group the stats by.  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Interval)`)` Required. Time range for the stats.  
`timestampOrder` |  `enum (`[Order](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Order)`)` Order the sequences in increasing or decreasing order of timestamps. Default is descending order of timestamps (latest first).  
`pageSize` |  `integer` Page size represents the number of time series sequences, one per unique set of dimensions and their values.  
`pageToken` |  `string` Page token stands for a specific collection of time series sequences.  
  
### Response body

Represents security stats result as a collection of time series sequences.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Sequence](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats#Sequence))
        }
      ],
      "columns": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`values[]` |  `object (`[Sequence](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats#Sequence)`)` Results of the query returned as a JSON array.  
`columns[]` |  `string` Column names corresponding to the same order as the inner values in the stats field.  
`nextPageToken` |  `string` Next page token.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## WindowSize

Supported time series window sizes.

Enums  
---  
`WINDOW_SIZE_UNSPECIFIED` | Unspecified window size. Default is 1 hour.  
`MINUTE` | 1 Minute window  
`HOUR` | 1 Hour window  
`DAY` | 1 Day window  
`MONTH` | 1 Month window  
  
## Sequence

A sequence of time series.

JSON representation  
---  
      
    
    {
      "dimensions": {
        string: string,
        ...
      },
      "points": [
        array
      ]
    }  
  
Fields  
---  
`dimensions` |  `map (key: string, value: string)` Map of dimensions and their values that uniquely identifies a time series sequence.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`points[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` List of points. First value of each inner list is a timestamp.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
