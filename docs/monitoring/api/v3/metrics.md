---
url: https://docs.cloud.google.com/monitoring/api/v3/metrics/
title: Metrics, time series, and resources \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:24.152431+00:00
---

# Metrics, time series, and resources  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Metrics, time series, and resources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Cloud Monitoring models the measurements it collects, those measurements help you understand how your applications and system services are performing. Cloud Monitoring's model for monitoring data consists of three primary concepts—monitored-resource types, metric types, time series:

  * _Monitored-resource types_ are the sources of the measurements, like your applications and system services. There are more than 270 types of monitored resources available. For the current list, see [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources).

  * _Metric types_ define the property that is being measured, like CPU utilization. There are more than 6,500 types of metrics available in Monitoring, for monitoring Google Cloud, AWS, and a variety of third-party software. For lists of metric types, see [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics). And if you need something that isn't already defined, you can create your own. 

  * A _time series_ is a collection of measurements from a specific monitored resource.




For an introduction to these concepts and how they are related, read this document. The following documents provide more in-depth information:

  * For information about labels and time series cardinality, and for examples of monitored resources and metric types, see [Components of the metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model).
  * For detailed information about time series, including how they are represented by the Cloud Monitoring API, see [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details). This information is particularly relevant to you if you plan to use the Monitoring API or custom metrics. 



## The Cloud Monitoring metric model

A _metric_ is a set of related measurements of some attribute of a resource you are monitoring. Measurements might include the latency of requests to a service, the amount of disk space available on a machine, the number of tables in your SQL database, the number of widgets sold, and so forth. Resources might include virtual machines (VMs), database instances, disks, and so forth.

The general notion of a _metric_ in Cloud Monitoring encompasses three primary components:

  * Information about the source of the measurements.
  * A set of measurements of some property. Each measurement is recorded as a time-stamped value.
  * Information about the values of the property being measured.



For example, suppose there is a metric that tracks the number of widgets sold by a store. The components of the model map to this example in the following ways:

  * **Source of the measurements**

The metric model records information about each resource being monitored. The particular information captured depends on the type of resource being monitored: it might include geographical locations, method names, disk IDs, and so forth, anything that might be the source of measurements.
        
        **Source information** : project? location? method?
        

The source of monitoring data is called a _monitored resource_.

**Example:** In the widget-sales example, the monitored resources are the stores selling the widgets.

  * **Measurements**

The metric model captures measurements of a property as a set of data points, consisting of time-stamped values.
        
        **Points** : [(value1, time1), (value2, time2), ...]
        

Values are typically numeric, but it depends on what you're measuring.

**Example:** In the widget-sales example, the measurements record sales information at points in time. Such measurements might look like the following:
        
        [(150, 2024-05-23T17:37:00-04:00),
         (229, 2024-05-23T17:38:00-04:00),
         (138, 2024-05-23T17:39:00-04:00),
         ...]

  * **Information about the values**

The measurement values are meaningless without information about how to interpret them. You need to have some “type” information about the values, like data type, unit, and kind of each measurement:

    * Is the value an integer or a string?
    * Does the value represent miles per hour or radians?
    * Does the value represent the total at the time, or the change since the previous value?
          
          **Type information** : integer? incremental?
          

Cloud Monitoring calls each set of characteristics about something you want to measure a _metric type_.

**Example:** In the widget-sales example, this information might tell you the following:

    * Each value is recorded as a 64-bit integer.
    * Each value represents a count of widgets sold.
    * Each value represents the number of widgets sold since the last recorded measurement.



## Time series: putting the components together

In Cloud Monitoring, the data structure that underlies this model is the _time series_ (the singular and the plural forms are the same).

Each time series encompasses the three components of the model:

  * A description of the monitored resource from which the measurements originated.
  * The set of measurements associated with a single monitored resource.
  * A description of the metric type that describes what you are measuring.
        
        **Time series** :
        
          **Source information** : project? location? method?
          **Points** : [(value1, time1), (value2, time2), ...]
          **Type information** : integer? incremental?
        




**Example:** In the widget-sales example, a time series includes the following:

  * A description of the store that sold the widgets counted in this time series.
  * The set of measurements recorded for this store.
  * A description of the values: 64-bit integers measuring the number of widgets sold since the previous recorded value.



A single Cloud Monitoring metric type or monitored-resource type can be associated with many related time series. In the widget-sales example, each store that sells widgets stores its data in a time series, so if there are 15 stores selling widgets, there can be 15 time series recording widget sales.

## What's next

  * For more information on the structure of Cloud Monitoring metrics, see 
    * [Components of the metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model) for a deeper look at metrics, resources, and time series.
    * [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details) for information about how time series map to the Cloud Monitoring API.
  * For information on time-series operations like aggregation, grouping, and filtering, see [Filtering and aggregation: manipulating time series](https://docs.cloud.google.com/monitoring/api/v3/aggregation).
  * For help with terminology, see [Notes on terminology](https://docs.cloud.google.com/monitoring/api/v3/terminology).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
