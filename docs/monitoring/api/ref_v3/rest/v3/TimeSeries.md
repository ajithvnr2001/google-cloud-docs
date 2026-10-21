---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries/
title: TimeSeries \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:18.718071+00:00
---

# TimeSeries  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  TimeSeries Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Point
    * JSON representation



A collection of data points that describes the time-varying values of a metric. A time series is identified by a combination of a fully-specified monitored resource and a fully-specified metric. This type is used for both listing and creating time series.

JSON representation  
---  
      
    
    {
      "metric": {
        object ([Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric))
      },
      "resource": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
      },
      "metadata": {
        object ([MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#MonitoredResourceMetadata))
      },
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)),
      "points": [
        {
          object ([Point](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point))
        }
      ],
      "unit": string,
      "description": string
    }  
  
Fields  
---  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric)`)` The associated metric. A fully-specified metric used to identify the time series.  
`resource` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` The associated monitored resource. Custom metrics can use only certain monitored resource types in their time series data. For more information, see [Monitored resources for custom metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#custom-metric-resources).  
`metadata` |  `object (`[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#MonitoredResourceMetadata)`)` Output only. The associated monitored resource metadata. When reading a time series, this field will include metadata labels that are explicitly named in the reduction. When creating a time series, this field is ignored.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)`)` The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)`)` The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the `points` field.  
`points[]` |  `object (`[Point](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point)`)` The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `valueType` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values. This field can only be changed through timeSeries.create when it is empty.  
`description` |  `string` Input only. A detailed description of the time series that will be associated with the `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor)` for the metric. Once set, this field cannot be changed through timeSeries.create.  
  
## Point

A single data point in a time series.

JSON representation  
---  
      
    
    {
      "interval": {
        object ([TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval))
      },
      "value": {
        object ([TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue))
      }
    }  
  
Fields  
---  
`interval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval)`)` The time interval to which the data point applies. For `GAUGE` metrics, the start time is optional, but if it is supplied, it must equal the end time. For `DELTA` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying contiguous and non-overlapping intervals. For `CUMULATIVE` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
`value` |  `object (`[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue)`)` The value of the data point.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
