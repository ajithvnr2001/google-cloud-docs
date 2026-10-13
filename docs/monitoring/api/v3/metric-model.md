---
url: https://docs.cloud.google.com/monitoring/api/v3/metric-model/
title: Components of the metric model \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:50.146535+00:00
---

# Components of the metric model  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/metric-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Components of the metric model Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring's model for monitoring data consists of three primary concepts:

  * Monitored-resource types
  * Metric types
  * Time series



The document [The metric model](https://docs.cloud.google.com/monitoring/api/v3/metrics) describes these Cloud Monitoring concepts in general terms. If these concepts are new to you, read that page first.

This page describes metric types, monitored resources, and time series, along with some related concepts, in more detail. These concepts underlie all Monitoring metrics.

You should understand the information on this page if you want to do any of the following: 

  * Inspect metric data by using [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

  * Create alerting policies to notify you when a value goes outside its normal limits, as described in [Using alerting policies](https://docs.cloud.google.com/monitoring/alerts).

  * Retrieve raw or aggregated monitoring data using the Monitoring API, as described in [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

  * Create your own metric types, as described in [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics).


For more detail on these concepts and how they map to the Cloud Monitoring API, see [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details), particularly if you plan to use the Monitoring API or custom metrics. 

## A word about labels

Monitored-resource types and metric types both support _labels_ , which allow data to be classified during analysis. For example:

  * A monitored-resource type for a virtual machine might include labels for the location of the machine and the project ID associated with the machine. When information about the monitored resource is recorded, the information includes the values for the labels. A monitored resource might also have system- or user-provided metadata labels, in addition to the labels defined for the monitored-resource type.


  * A metric type that counts API requests might have labels to record the name of the method invoked and the status of the request.



The use of labels is discussed in more detail in [Labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info).

## Monitored-resource types

A _monitored resource_ is a resource from which metric data is captured. Cloud Monitoring supports approximately 270 types of monitored resources.

Types of monitored resources include generic nodes and tasks, architectural components in Google Kubernetes Engine, tables in Bigtable, various AWS resources, and many more. 

Each type of monitored resource is formally described in a data structure called a _monitored-resource descriptor_. For more information, see [Monitored resource descriptors](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-monresdesc).

Each of the supported monitored-resource types has an entry in the [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources). The entries in the list are created from the monitored-resource descriptors. This section describes the information captured in a monitored-resource descriptor and shows how it is presented in the list.

### A sample monitored-resource type

The following image shows the [entry in the list](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket) for a Cloud Storage bucket:

![Listing for the Cloud Storage bucket.](https://docs.cloud.google.com/static/monitoring/images/resource-gcs-bucket.png)

All entries in the list include the following information:

  * **Type** : The header in the entry lists the monitored-resource type; `gcs_bucket` in the example.
  * **Display name** : A short description of the monitored resource.
  * **Description** : A longer description of the monitored resource.
  * **Labels** : A set of dimensions for classifying data. For more information, see [Labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info).



## Metric types

A _metric type_ describes measurements that can be collected from a monitored resource. A metric type includes a description of what is being measured and how the measurements are interpreted. Cloud Monitoring supports approximately 6,500 types of metrics, and it provides you the ability to define new types. 

Metric types include counts of API calls, disk-usage statistics, storage consumption, and many more.

Each metric type is formally described in a data structure called a _metric descriptor_. For more information, see [Metric descriptors](https://docs.cloud.google.com/monitoring/api/v3/metrics-details#intro-metdesc).

Each of the built-in metric types has an entry in the [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) pages. The entries in these tables are created from the metric descriptors. This section describes the information captured in a metric type and shows how it is presented in reference material.

### A sample metric type

The following image shows an entry for a Cloud Storage metric type:

![An excerpt of the metric list for Cloud Storage.](https://docs.cloud.google.com/static/monitoring/images/storage-metric-sample.png)

The metric types are displayed in a table, and the table header explains the layout of the information. This section uses one entry as an example, but all the tables use the same format.

The sample Cloud Storage table entry gives you the following information about one metric type:

  * **Metric type** : An identifier for the metric type, `storage.googleapis.com/api/request_count` in the example.

The prefix `storage.googleapis.com` acts as a namespace for Cloud Storage. All metric types associated with a particular monitored-resource type use the same namespace.

Namespaces are omitted from entries in the tables.

All the metric types associated with Cloud Storage are listed in the [table for Cloud Storage metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage).

  * **Launch stage** : A colored block that indicates the launch stage of the metric type with a value like Alpha, Beta, and GA.

  * **Display name** : A brief string describing the metric type, “Request count” in the example.

  * **Kind, Type, Unit** : This line provides information for interpreting the data values: the example shows a delta metric recorded as a 64-bit integer with no unit (that's the `1` value).

    * **Kind:** This example is a _delta_ metric, which records a change over a period of time. That is, each data point records the number of API calls since the previous data point was written. For more information on kinds, see [Value types and metric kinds](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

    * **Type:** This example records its values as 64-bit integers. For more information on types, see [Value types and metric kinds](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

    * **Unit** : This metric doesn't need an explicit unit because it represents a count; the digit `1` is used to indicate that no unit is needed.

  * **Monitored resources** : The monitored resources for which this metric type is available. The values here are the same as those described in [Monitored-resource types](https://docs.cloud.google.com/monitoring/api/v3/metric-model#resource-overview).

  * **Description** : More detailed information about what is recorded and how. Set in italics to distinguish it from the labels.

  * **Labels** : A set of dimensions for classifying data. For more information, see [Labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info).




When you access monitoring data through the Cloud Monitoring API, you include a Google Cloud project in the API call. You can retrieve only the data that is visible to that Google Cloud project. For example, if you request your project's data for the metric type `storage.googleapis.com/api/request_count`, then you see API counts only for Cloud Storage buckets in your project. If your project isn't using any Cloud Storage buckets, then no metric data is returned.

### Built-in metric types

Built-in metric types are defined by Google Cloud services, including Cloud Monitoring. These metric types describe standard measurements for a wide array of common infrastructure and are available for anyone to use.

The [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) shows the entire set of built-in metric types. Metrics listed in the [External metrics list](https://docs.cloud.google.com/monitoring/api/metrics_other) page are a special subset of built-in metrics that are defined by Cloud Monitoring in partnership with open-source projects or third-party providers. Typically, these metrics have a prefix of `external.googleapis.com`. 

### Custom metrics

When you build your application, you might have certain properties you want to measure, things for which there are no metrics built into Cloud Monitoring. With Cloud Monitoring, you can define your own metric types or import metric types from external sources. These metric types are called _custom metrics_. If a metric has a prefix of `custom.googleapis.com` or `prometheus.googleapis.com`, then it is a custom metric. The latter metrics usually come from [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

For example, if you want to track the number of widgets sold by your stores, you need to use a custom metric. For more information, see [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics). 

## Labels

A label is key-value pair that can be used to provide information about a data value.

### Metric and monitored-resource labels

The definitions of both metric and monitored-resource types include labels. Labels are classifiers for the data being collected; they help to categorize the data for deeper analysis. For example:

  * The Cloud Storage metric type `storage.googleapis.com/api/request_count` has two labels, `response_code` and `method`.
  * The Cloud Storage monitored-resource type `gcs_bucket` has three labels, `project_id`, `bucket_name`, and `location`. The labels identify specific instances of the resource type.



Therefore, all data collected for API requests from a Cloud Storage bucket is classified by the method that was called, the response code for the call, the name, location, and project of the bucket involved. The set of labels varies with the metric or monitored-resource type; the available labels are documented in the [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) and [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources) pages.

By tracking the response code, method name, and location when counting API calls, you can then fetch the number of calls to a particular API method, or the number of failing calls to any method, or the number of failing calls to a specific method in a specific location.

The number of labels and the number of values each can assume is referred to as _cardinality_. The cardinality is the number of possible time series that might be collected for a pair of metric and monitored-resource types: there is one time series for each combination of values of their labels. For more information, see [Cardinality: time series and labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality).

### Resource metadata labels

In addition to the labels defined on the metric and monitored-resource types, Monitoring internally collects additional information on monitored resources and stores this information in system metadata labels. These system metadata labels are available to users as read-only values. Some resources also allow users to create their own resource metadata labels when configuring resources like VM instances in the Google Cloud console.

The system and user metadata labels are collectively called _resource metadata labels_. You can use these labels like the labels defined on the metric and monitored-resource types in time-series filters.

**Note:** Don't rely on the values of system- or user-defined resource metadata labels when selecting time series for sensitive alerting policies or for other responsive operations like autoscaling. Instead, use the values of labels defined by the [monitored-resource types](https://docs.cloud.google.com/monitoring/api/resources). 

Resource metadata labels are added asynchronously to time series and aren't subject to the same [ latency expectations](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention#latency) as values of labels defined metric types or monitored-resource types. Therefore, an alerting policy or other responsive operation that depends on metadata values to trigger an action can behave erratically if the population of resource metadata labels is delayed.

Resource metadata labels only appear in the query result if you explicitly aggregate by them.

For more information on filtering, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters). 

## Time series: data from a monitored resource

This section discusses what monitoring data is and how it's organized in time series. This is where the conceptual components of the metric model become concrete artifacts.

Cloud Monitoring store regular measurements over time for pairs of metric and monitored-resource types. The measurements are collected into _time series_ , and each time series contains the following items:

  * The name of the metric type to which the time series belongs, and one combination of values for the metric's labels.

  * A series of (_timestamp_ , _value_) pairs. The _value_ is the measurement, and the _timestamp_ is the time at which the measurement was taken.

  * The monitored resource that is the source of the time series data, and one combination of values for the resource's labels.




A time series is created for each combination of metric and resource labels that generates data.

**Stylized example** : The metric type `storage.googleapis.com/api/request_count` could have many time series for your project's Cloud Storage buckets. The following table shows some possible time series.

In the table, the value `bucket: xyz` represents the value of the `bucket_name` label in the monitored-resource type, and `response_code` and `method` are labels in the metric type. There is one time series for each combination of values in the resource and metric labels; the table shows some of them:

Monitored  
resource label | Metric labels | Metric data  
---|---|---  
`bucket: 1234` | `response_code: OK,  
method: read` | `{  
(3, Wed 2:00pm),  
(2, Wed 2:05pm),  
(8, Wed 2:10pm),  
...}`  
`bucket: 1234` | `response_code: OK,  
method: write` | `{  
(1, Wed 2:01pm),  
(2, Wed 2:04pm),  
(7, Wed 2:09pm),  
...}`  
`bucket: 1234` | `response_code: FAIL,  
method: write` | `{  
(1, Wed 2:01pm),  
(0, Wed 2:04pm),  
(0, Wed 2:09pm),  
...}`  
`bucket: 9876` | `response_code: OK,  
method: read` | `{  
(2, Wed 1:59pm),  
(4, Wed 2:05pm),  
(3, Wed 2:10pm),  
...}`  
  
Cloud Monitoring doesn't record “empty” time series. In the Cloud Storage buckets example, if you're not using a particular bucket or never call a particular API method, then no data is collected for that label, and no time series mentions it. This means that, if your project has no data at all for a particular metric, you never see the metric type.

The metric types don't indicate what types of monitored resources are found in the metrics' time series. For Cloud Storage, there is only one monitored resource type—`gcs_bucket`. Some metric types pair with more than one monitored resource.

**Live example** : If you have a Google Cloud project, you can try the APIs Explorer widget, located on the reference page for the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method in the Monitoring API.

  1. Open the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) reference page.

  2. In the pane labeled **Try this method** , enter the following:

     * **name** : `projects/PROJECT_ID` Replace `PROJECT_ID` with the ID of your Google Cloud project.
     * **filter** : `metric.type="logging.googleapis.com/log_entry_count" resource.type="gce_instance"`
     * **interval.start_time** : Enter the start time and ensure that it is 20 minutes earlier than the end time.
     * **interval.end_time** : Enter the end time.



If the request succeeds, it will return the time-series data that matches the request. It will look like the following snippet:
    
    
    {
      "timeSeries": [
        {
          "metric": {
            "labels": {
              "severity": "INFO",
              "log": "compute.googleapis.com/activity_log"
            },
            "type": "logging.googleapis.com/log_entry_count"
          },
          "resource": {
            "type": "gce_instance",
            "labels": {
              "instance_id": "0",
              "zone": "us-central1",
              "project_id": "your-project-id"
            }
          },
          "metricKind": "DELTA",
          "valueType": "INT64",
          "points": [
            {
            "interval": {
                "startTime": "2024-03-29T13:53:00Z",
                "endTime": "2024-03-29T13:54:00Z"
              },
              "value": {
                "int64Value": "0"
              }
            },
            ...
          ]
        },
        ...
      ]
    }
    

For more information on using the APIs Explorer widget, including troubleshooting, see [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer). 

## Cardinality: time series and labels

Every time series is associated with a specific pair of metric and monitored-resource types. The metric and monitored-resource types each provide some number of labels. In Cloud Monitoring, the number of unique combinations of values for the set of labels is the cardinality of the metric type or monitored-resource type. These values are referred to as _metric cardinality_ and _resource cardinality_ , and they determine how many possible time series, the _total cardinality_ , might be generated.

### Metric, resource, and total cardinality

Suppose you have a metric type that specifies two labels, `color` and `zone`. The metric cardinality depends on the number of possible values those labels have:

  * If there are only three possible colors, “red,” “green,” and “blue,” then the `color` label can have up to three distinct values.
  * If there are only two possible zones, “east” and “west”, then the `zone` label can have up to two distinct values.



The cardinality of this metric is 6 (3×2). If there are 1,000 possible values for the `color` label, and if every color can appear in every zone, then the metric cardinality is 2,000 (1,000×2). The same calculation applies if these are labels on a monitored-resource type rather than on a metric type.

This cardinality value is a maximum, based on the number of combinations of possible label values. The effective, real-world value might be significantly lower when all combinations of label values don't actually occur. For example, if each color appears in only one zone, not in both zones, then the maximum number of time series you see in the running system is 1,000. But the usefulness of effective cardinality depends on the reasons that certain combinations don't appear and whether they might in the future.

![Cardinality depends the values any labels can have.](https://docs.cloud.google.com/static/monitoring/images/cardinality.png)

When time series data is written, it is classified by metric and monitored-resource types. For any pair of metric and resource types, the _total cardinality_ is the product of the metric cardinality and the resource cardinality. If you have a metric with cardinality of 1,000, and a resource with cardinality of 100, and if every label value appears, then you have 100,000 time series (1,000×100).

When designing your own metrics, ensure that the set of possible values for any label is constrained. A small set of discrete values (like “red,” “green,” and “blue,”) is the preferred approach. If, for example, you use 8-bit RGB values for a `color` label, you can have over 16 million different values. Do _not_ use high-resolution values like timestamps, any kind of unique identifier, user IDs, IP addresses, unparameterized URLs, and so forth, for metric labels. 

### Query performance and cardinality

When you issue a query for data, the volume of data you request is the biggest factor in query performance: a query for one hour of data is generally faster than the same query covering six months. But the volume of data returned by a request is also sensitive to the number of time series in a request. A query retrieving two months of data for a low-cardinality metric is likely to be faster than another query retrieving two months of data for a very high-cardinality metric, because of the amount of data being retrieved.

Cardinality depends primarily on the number of values your labels can have, not on the number of labels. In general, you don't have control over the cardinality of resources, as when the number of pods or VMs changes based on business needs. But when ingesting metrics into Cloud Monitoring, rather than using system metrics, you often have some control over metric cardinality. For example, with user-defined custom metrics, you determine the labels and the possible values for them. If you are ingesting Prometheus metrics, you can use [relabeling](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#filter-metrics) to modify the set of labels and drop time series you don't want to ingest.

You can use the Cloud Monitoring **Metrics Management** page to identify metrics that might have cardinality problems. To view the **Metrics Management** page, do the following: 

  1. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, select your time window. By default, the **Metrics Management** page displays information about the metrics collected in the previous one day.



For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

For technical background about the way Cloud Monitoring stores and retrieves time series data, see [Monarch: Google's Planet-Scale In-Memory Time Series Database](https://research.google/pubs/pub50652/).

For information about limits on user-defined metrics in Cloud Monitoring, see [User-defined metrics](https://docs.cloud.google.com/monitoring/quotas#custom_metrics_quotas). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
