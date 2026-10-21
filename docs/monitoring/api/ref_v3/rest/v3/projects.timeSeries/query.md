---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query/
title: Method: projects.timeSeries.query \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:14.932190+00:00
---

# Method: projects.timeSeries.query  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.timeSeries.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * TimeSeriesDescriptor
    * JSON representation
  * ValueDescriptor
    * JSON representation
  * TimeSeriesData
    * JSON representation
  * LabelValue
    * JSON representation
  * PointData
    * JSON representation
  * Try it!



This item is deprecated!

Queries time series by using Monitoring Query Language (MQL). We recommend using PromQL instead of MQL. For more information about the status of MQL, see the [MQL deprecation notice](https://cloud.google.com/stackdriver/docs/deprecations/mql).

### HTTP request

`POST https://monitoring.googleapis.com/v3/{name}/timeSeries:query`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "query": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`query` |  `string` Required. The query in the [Monitoring Query Language](https://cloud.google.com/monitoring/mql/reference) format. The default time zone is in UTC.  
`pageSize` |  `integer` A positive number that is the maximum number of timeSeriesData to return.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
### Response body

This item is deprecated!

The `timeSeries.query` response. For information about the status of Monitoring Query Language (MQL), see the [MQL deprecation notice](https://cloud.google.com/stackdriver/docs/deprecations/mql).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "timeSeriesDescriptor": {
        object ([TimeSeriesDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#TimeSeriesDescriptor))
      },
      "timeSeriesData": [
        {
          object ([TimeSeriesData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#TimeSeriesData))
        }
      ],
      "nextPageToken": string,
      "partialErrors": [
        {
          object ([Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status))
        }
      ]
    }  
  
Fields  
---  
`timeSeriesDescriptor` |  `object (`[TimeSeriesDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#TimeSeriesDescriptor)`)` The descriptor for the time series data.  
`timeSeriesData[]` |  `object (`[TimeSeriesData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#TimeSeriesData)`)` The time series data.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
`partialErrors[]` |  `object (`[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status)`)` Query execution errors that may have caused the time series data returned to be incomplete. The available data will be available in the response.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## TimeSeriesDescriptor

A descriptor for the labels and points in a time series.

JSON representation  
---  
      
    
    {
      "labelDescriptors": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor))
        }
      ],
      "pointDescriptors": [
        {
          object ([ValueDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#ValueDescriptor))
        }
      ]
    }  
  
Fields  
---  
`labelDescriptors[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor)`)` Descriptors for the labels.  
`pointDescriptors[]` |  `object (`[ValueDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#ValueDescriptor)`)` Descriptors for the point data value columns.  
  
## ValueDescriptor

A descriptor for the value columns in a data point.

JSON representation  
---  
      
    
    {
      "key": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)),
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)),
      "unit": string
    }  
  
Fields  
---  
`key` |  `string` The value key.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)`)` The value type.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)`)` The value stream kind.  
`unit` |  `string` The unit in which `timeSeries` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. `unit` is only valid if `valueType` is INTEGER, DOUBLE, DISTRIBUTION.  
  
## TimeSeriesData

Represents the values of a time series associated with a TimeSeriesDescriptor.

JSON representation  
---  
      
    
    {
      "labelValues": [
        {
          object ([LabelValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#LabelValue))
        }
      ],
      "pointData": [
        {
          object ([PointData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#PointData))
        }
      ]
    }  
  
Fields  
---  
`labelValues[]` |  `object (`[LabelValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#LabelValue)`)` The values of the labels in the time series identifier, given in the same order as the `labelDescriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `labelDescriptors`.  
`pointData[]` |  `object (`[PointData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query#PointData)`)` The points in the time series.  
  
## LabelValue

A label value.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "boolValue": boolean,
      "int64Value": string,
      "stringValue": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The label value can be a bool, int64, or string. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`boolValue` |  `boolean` A bool label value.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An int64 label value.  
`stringValue` |  `string` A string label value.  
End of mutually exclusive fields.  
  
## PointData

A point's value columns and time interval. Each point has one or more point values corresponding to the entries in `pointDescriptors` field in the TimeSeriesDescriptor associated with this object.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue))
        }
      ],
      "timeInterval": {
        object ([TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval))
      }
    }  
  
Fields  
---  
`values[]` |  `object (`[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue)`)` The values that make up the point.  
`timeInterval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval)`)` The time interval associated with the point.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
