---
url: https://docs.cloud.google.com/monitoring/api/v3/metrics-details/
title: Structure of time series \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:27.042562+00:00
---

# Structure of time series  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/metrics-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Structure of time series Stay organized with collections  Save and categorize content based on your preferences. 

This page is an in-depth continuation of the discussion and examples presented in [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics) and [Components of the metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model). To get the most from this page, read those pages first.

This page is intended for readers who want a deeper understanding of time series and the implementation of the Cloud Monitoring metric model, particularly those readers who are using the Monitoring API. This includes users of custom (user-defined) metrics. 

  * This page maps the general metric model to the Cloud Monitoring API, so it is useful for anyone using the Monitoring API directly. Users whose primary interaction is with the Google Cloud console probably don't need this level of detail.

  * It is also useful to anyone using a third-party integration like [OpenTelemetry](https://opentelemetry.io). As data from an external source reaches Cloud Monitoring through an integration, it is mapped to the Cloud Monitoring metric model and treated like any other metric data.




For more on collecting your own metrics, see [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics). 

## Review of the metric model

A prerequisite for understanding the structure of time series is familiarity with the metric model used by Cloud Monitoring. This model is described in [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). This section provides a brief review.

In general terms, monitoring data is recorded in _time series_. Each individual time series includes three pieces of information relevant to this discussion:

  * A set of time-stamped data points.
  * A reference to the metric type that tells you how to interpret the data points.
  * A reference to the monitored resource from which the data originated.


    
    
    **Time series** :
    
        **Points** : [(value1, time1), (value2, time2), ...]
        **Metric type information** : integer? incremental?
        **Monitored resource** : project? location? method?
    

Each time series holds the measurements from a single physical or logical source. If your environment has hundreds of resources, each contributes at least one time series. In fact, if your metric type and monitored-resource type have labels, you get one time series per combination of label values; see [Cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality) for more information.

## A sample time series

A time series is represented as an instance of a [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) object. The following is a complete instance of a single time series:
    
    
        {
          **"metric"** : {
            "labels": {
              "log": "kubelet",
              "severity": "DEFAULT"
            },
            "type": "logging.googleapis.com/log_entry_count"
          },
          **"resource"** : {
            "type": "gce_instance",
            "labels": {
              "instance_id": "5106847938295940291",
              "zone": "us-central1-a",
              "project_id": "a-gcp-project"
            }
          },
          "metricKind": "DELTA",
          "valueType": "INT64",
          **"points"** : [
            {
              "interval": {
                "startTime": "2019-12-20T20:25:38Z",
                "endTime": "2019-12-20T20:26:38Z"
              },
              "value": {
                "int64Value": "20"
              }
            }
          ]
        }
    

Most time series include a lot more data points; this one covers a one-minute interval. All time series have the same structure, with the following fields:

  * The `metric` field records

    * The metric-label values for this particular time series, representing one combination of label values.
    * The metric type with which the data is associated. The metric type specifies the available labels and describes what is represented by the data points.

The information in this field is described in more detail in [Metrics](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-metric).

  * The `resource` field records:

    * The resource-label values for this particular time series, representing one combination of label values.
    * The specific monitored resource from which the data was collected.

The information in this field is described in more detail in [Monitored-resource objects](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-monres).

  * The `metricKind` and `valueType` fields tell you how to interpret the values. For more information, see [Metric kinds and types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

  * The `points` field is an array of timestamped values. The metric type tells you what the values represent. The sample time series has an array with a single data point; in most time series, the array has many more values.




For a live example that retrieves time series data, see [Time series: data from a monitored resource](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series).

This rest of this page looks at the information in the `metric` and `resource` fields in more detail.

## Monitored resources

Cloud Monitoring collects data from monitored resources and records it in time series. Each time series created includes a description of the monitored resource from which the data was collected.

### Monitored-resource objects

A monitored resource is represented by an instance of a [`MonitoredResource`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource) object. The monitored resource describes the source of the values in a time series. The `MonitoredResource` object is embedded into the time series and identifies a specific instance of a monitored-resource type known to Monitoring: it points to a physical or logical entity.

For example, here is a monitored-resource object describing a particular Compute Engine instance, extracted from the example time series:
    
    
          **"resource"** : {
            "type": "gce_instance",
            "labels": {
              "instance_id": "5106847938295940291",
              "zone": "us-central1-a",
              "project_id": "a-gcp-project"
            }
          }
    

This instance of a monitored resource is of the type `gce_instance`, it has a specific `instance_id` value (5106847938295940291) in the project `a-gcp-project`. The instance is located in the US. Another time series might originate from a different instance of this monitored resource. Each combination of label values identifies a unique resource from which data is collected.

Different sets of labels make sense for different resources. The set of labels for a resource is determined by the monitored-resource descriptor for that type.

### Monitored-resource descriptors

The information about a monitored-resource type is held in a data structure called a _monitored-resource descriptor_. For a definition of this data structure, see [`MonitoredResourceDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor).

A monitored-resource descriptor is like a schema or specification for a record structure. It doesn't contain the data about a particular instance of the monitored resource; it tells you how to describe a monitored resource of a specific type. For example, here is the monitored-resource descriptor for the `gce_instance` resource:
    
    
    {
      **"type"** : "gce_instance",
      "displayName": "VM Instance",
      "description": "A virtual machine instance hosted in Compute Engine.",
      **"name"** : "projects/[PROJECT_ID]/monitoredResourceDescriptors/gce_instance"
      **"labels"** : [
        {
          "key": "project_id",
          "description": "The identifier of the GCP project associated with this resource, such as \"my-project\"."
        },
        {
          "key": "instance_id",
          "description": "The numeric VM instance identifier assigned by Compute Engine."
        },
        {
          "key": "zone",
          "description": "The Compute Engine zone in which the VM is running."
        }
      ],
    }
    

Compare this monitored-resource descriptor to the specific instance of a `gce_instance` resource shown in [Monitored-resource objects](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-monres). This descriptor doesn't describe a particular monitored resource; instead, the descriptor specifies the labels, and each combination of label values identifies a particular monitored resource.

You can retrieve the monitored-resource descriptors in your Google Cloud project by using the Cloud Monitoring API. See, for example, the reference pages for the [`monitoredResourceDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list) and [`monitoredResourceDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get) methods.

**Live example:** If you have a Google Cloud project, you can retrieve this descriptor by using the APIs Explorer widget as follows:

  1. Open the [`monitoredResourceDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list) reference page.

  2. In the pane labeled **Try this method** , enter the following:

     * **name** : `projects/PROJECT_ID/monitoredResourceDescriptors/gce_instance`

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  3. Click **Execute**.




The request returns the preceding descriptor.

For examples using the Monitoring API methods, see [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics).

## Metrics

Each time series created by Cloud Monitoring records a set of data points as well as information about the organization and meaning of those data points.

### Metric objects

Each time series includes a reference to the description of the data being recorded in a metric object.

The metric object contained in a time series specifies the type of measurements and metric-specific information about those measurements. For a definition of the metric object data structure, see [`Metric`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric). For example, here is the metric object extracted from the time series in [A sample time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#real-ts-example):
    
    
        {
          **"metric"** : {
            "labels": {
              "log": "kubelet",
              "severity": "DEFAULT"
            },
            "type": "logging.googleapis.com/log_entry_count"
          }
    

This object tells you that the time series contains `logging.googleapis.com/log_entry_count` measurements. The label values tell you that this specific time series counts only log entries of severity `DEFAULT` in the log file called `kubelet`.

There is one time series for each combination of label values, so `INFO` entries to the same log file appear in a different time series.

The set of labels collected in a metric object is specified in the descriptor for that metric type.

### Metric descriptors

The information about a metric type is held in a data structure called a _metric descriptor_. For a definition of this data structure, see [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor).

A metric descriptor is a schema or specification for a record structure. It doesn't contain the data about a particular metric; rather, it tells you how to interpret the data associated with a specific metric type.

Here is an example metric descriptor:
    
    
    {
      "type": "logging.googleapis.com/log_entry_count",
      "name": "projects/a-gcp-project/metricDescriptors/logging.googleapis.com/log_entry_count",
      "labels": [
        {
          "key": "log",
          "description": "Name of the log."
        },
        {
          "key": "severity",
          "description": "Severity of the log entry."
        }
      ],
      "metricKind": "DELTA",
      "valueType": "INT64",
      "unit": "1",
      "description": "Number of log entries that contributed to user-defined metrics.",
      "displayName": "Log entries",
      "metadata": {
        "launchStage": "GA",
        "samplePeriod": "60s"
      },
      "launchStage": "GA"
    }
    

Compare this metric descriptor to the metric object shown in [Metric objects](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-metric). The descriptor tells you what the label values mean, as well as how to interpret the values of the data points.

You can retrieve metric descriptors by using the Cloud Monitoring API. See, for example, the reference pages for the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) and [`metricDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get) methods.

**Live example:** If you have a Google Cloud project, you can retrieve this descriptor by using the APIs Explorer widget as follows:

  1. Open the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) reference page.

  2. In the pane labeled **Try this method** , enter the following:

     * **name** : `projects/PROJECT_ID/metricDescriptors/logging.googleapis.com/log_entry_count` Replace `PROJECT_ID` with the ID of your Google Cloud project.
  3. Click **Execute**.




The request returns the preceding descriptor.

For examples using the Monitoring API methods, see [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics).

Most of the fields in the metric descriptor are self-explanatory. The two likely to need further explanation are the metric kind and value type, which are described further in [Metric kinds and types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

Cloud Monitoring has approximately 6,500 built-in metric types; see the [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) for details. You can also create your own metric descriptors to capture custom metrics. For more information, see [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
