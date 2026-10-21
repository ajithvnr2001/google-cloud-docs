---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures/
title: Constructs in the API \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:22.808638+00:00
---

# Constructs in the API  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Constructs in the API Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces the structures used to represent services and SLOs in the SLO API and maps them to the concepts described in generally in [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

The SLO API is used to set up service-level objectives (SLOs) that can be used to monitor the health of your services.

Service Monitoring adds the following resources to the Monitoring API:

  * [`services`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services)
  * [`services.serviceLevelObjectives`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives)



For information on invoking the API, see [Working with the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api).

## Services

A service is represented by a [`Service`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services) object. This object includes the following fields:

  * A name: A fully qualified resource name for this service
  * A display name: A label for use in console components
  * A structure for one of the [`BasicService`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService) types.
  * A system-provided telemetry-configuration object



To define a basic service, you specify the type of service and provide a set of service-specific labels that describe the service:
    
    
    {
       "serviceType": string,
       "serviceLabels": {
          string: string,
          ...
       }
    }
    

The following sections provide examples for each type of service.

### Basic service types

This section provides examples of services definitions built on the [`BasicService`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService) type, where the value of the `serviceType` field is one of the following:

  * `APP_ENGINE`
  * `CLOUD_ENDPOINTS`
  * `CLUSTER_ISTIO`
  * `ISTIO_CANONICAL_SERVICE`
  * `CLOUD_RUN`



Each of these service types uses the [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli) service-level indicator.

###  App Engine 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "APP_ENGINE",
              "serviceLabels": {
                "module_id": "MODULE_ID"
              },
          },
        }
    

###  Cloud Endpoints 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "CLOUD_ENDPOINTS",
              "serviceLabels": {
                "service": "SERVICE"
              },
          },
        }
    

###  Cluster Istio 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "CLUSTER_ISTIO",
              "serviceLabels": {
                "location": "LOCATION",
                "cluster_name": "CLUSTER_NAME",
                "service_namespace": "SERVICE_NAMESPACE",
                "service_name": "SERVICE_NAME"
              },
          },
        }
    

###  Istio Canonical Service 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "ISTIO_CANONICAL_SERVICE",
              "serviceLabels": {
                "mesh_uid": "MESH_UID",
                "canonical_service_namespace": "CANONICAL_SERVICE_NAMESPACE",
                "canonical_service": "CANONICAL_SERVICE"
              },
          },
        }
    

###  Cloud Run 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "CLOUD_RUN",
              "serviceLabels": {
                "service_name": "SERVICE_NAME",
                "location": "LOCATION"
              },
          },
        }
    

### Basic GKE service types

This section contains examples of GKE service definitions built on the [`BasicService`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService) type, where the value of the `serviceType` field is one of the following:

  * `GKE_NAMESPACE`
  * `GKE_WORKLOAD`
  * `GKE_SERVICE`



You must define SLIs for these service types. They can't use [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli) service-level indicators. For more information, see Service-level indicators.

###  GKE namespace 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "GKE_NAMESPACE",
              "serviceLabels": {
                "project_id": "PROJECT_ID",
                "location": "LOCATION",
                "cluster_name": "CLUSTER_NAME",
                "namespace_name": "NAMESPACE_NAME"
              }
          },
        }
    

###  GKE workload 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "GKE_WORKLOAD",
              "serviceLabels": {
                "project_id": "PROJECT_ID",
                "location": "LOCATION",
                "cluster_name": "CLUSTER_NAME",
                "namespace_name": "NAMESPACE_NAME",
                "top_level_controller_type": "TOPLEVEL_CONTROLLER_TYPE",
                "top_level_controller_name": "TOPLEVEL_CONTROLLER_NAME",
              }
          },
        }
    

###  GKE service 
    
    
        {
          "displayName": "DISPLAY_NAME",
          "basicService": {
              "serviceType": "GKE_SERVICE",
              "serviceLabels": {
                "project_id": "PROJECT_ID",
                "location": "LOCATION",
                "cluster_name": "CLUSTER_NAME",
                "namespace_name": "NAMESPACE_NAME",
                "service_name": "SERVICE_NAME"
              }
          },
        }
    

### Custom services

You can create custom services if none of the basic service types is suitable. A custom service looks like the following:
    
    
        {
          "displayName": "DISPLAY_NAME",
          "custom": {}
        }
    

You must define SLIs for these service types. They can't use [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli) service-level indicators. For more information, see Service-level indicators.

## Service-level indicators

A service-level indicator (SLI) provides a measure of the performance of a service. An SLI is based on metric captured by the service. Exactly how the SLI is defined depends on the type of metric used as the indicator metric, but it is generally some comparison between acceptable results and total results.

A SLI is represented by the [`ServiceLevelIndicator`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelIndicator) object. This object is a collective way to refer the three supported types of SLIs:

  * A basic SLI, which is created automatically for instances of the the [`BasicService`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService) service type. This type of SLI is described in [Service-level-objectives](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#defn-slo); it is represented by a [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli) object and measures availability or latency.

  * A request-based SLI, which you can use to count events that represent acceptable service. Use of this type of SLI is described in [Request-based SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-type-request); it is represented by a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) object.

  * A window-based SLI, which you can use to count periods of time that meet some goodness criterion. Use of this type of SLI is described in [Windows-based SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-type-time); it is represented by a [`WindowsBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#WindowsBasedSli) object.




For example, the following shows a basic availability SLI: 
    
    
    {
      "basicSli": {
        "availability": {},
        "location": [
          "us-central1-c"
        ]
      }
    }
    

### Structures for request-based SLIs

A request-based SLI is based on a metric that counts units of service as a ratio between a particular outcome and the total. For example, if you use a metric that counts requests, you can build the ratio between the number of requests that return success and the total number of requests.

There are two ways to build a request-based SLI:

  * As a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio), when the ratio of good service to total service is computed from two time series whose values have a metric kind of `DELTA` or `CUMULATIVE`.
  * As a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut), when the time series has value type `DISTRIBUTION` and whose values have a metric kind of `DELTA` or `CUMULATIVE`. The good-service value is the count of items that fall into the histogram buckets in a specified range, and the total is the count of all values in the distribution.



The following shows the JSON representation of an SLI that uses a time-series ratio: 
    
    
    {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter": "resource.type=https_lb_rule metric.type="loadbalancing.googleapis.com/https/request_count"",
          "goodServiceFilter": "resource.type=https_lb_rule metric.type="loadbalancing.googleapis.com/https/request_count" metric.label.response_code_class=200",
        }
      }
    }
    

The time series in this ratio are identified by the pair of monitored-resource type and metric type:

  * Resource: `https_lb_rule`
  * Metric type: `loadbalancing.googleapis.com/https/request_count`



The value for the `totalServiceFilter` is represented by the pair of metric and resource type. The value for the `goodServiceFilter` is represented by the same pair but where some label has a particular value; in this case, when the value of the `response_code_class` label is `200`.

The ratio between the filters measures the number of requests that return a 2xx HTTP status over the total number of requests.

The following shows the JSON representation of an SLI that uses a distribution cut: 
    
    
    {
      "requestBased": {
        "distribution_cut": {
          "distribution_filter": "resource.type=https_lb_rule  metric.type="loadbalancing.googleapis.com/https/backend_latencies" metric.label.response_code_class=200",
          "range": {
            "min": "-Infinity",
            "max": 500.0
          }
        }
      }
    }
    

The time series is identified by the monitored-resource type, metric type, and value for a metric label:

  * Resource: `https_lb_rule`
  * Metric type: `loadbalancing.googleapis.com/https/backend_latencies`
  * Label-value pair: `response_code_class` = `200`



The range of latencies considered good is designated by the `range` field. This SLI computes the ratio of latencies of 2xx-class responses below 500 to the latencies of all 200-class responses.

### Structures for windows-based SLIs

A windows-based SLI counts time windows in which the provided service is considered good. The criterion for determining how good service is part of the SLI definition.

All windows-based SLIs include a window period, 60–86,400 seconds (1 day).

There are two ways to specify the good-service criterion for a windows-based SLI:

  * Create a filter string, described in [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters#time-series-filter) that returns a time series with boolean values. A window is good if the value for that window is `true`. This filter is called the `goodBadMetricFilter`.
  * Create a [`PerformanceThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#PerformanceThreshold) object that represents a threshold for acceptable performance. This object is specified as the value of the `goodTotalRatioThreshold`.

A `PerformanceThreshold` object specifies a threshold value and a performance SLI. If the value of the performance SLI meets or exceeds the threshold value, then the time window counts as good.

There are two ways to specify the performance SLI:

    * As a [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli) object in the `basicPerformanceSli` field.
    * As a [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli) object in the `performance` field. If you use a request-based SLI, then the metric kind of your SLI must be `DELTA` or `CUMULATIVE`. You can't use `GAUGE` metrics in request-based SLIs.



The following shows the JSON representation a windows-based SLI built on a performance threshold for a basic availability SLI:
    
    
    {
      "windowsBased": {
         "goodTotalRatioThreshold": {
           "threshold": 0.9,
           "basicSliPerformance": {
             "availability": {},
             "location": [
               "us-central1-c"
             ]
           }
         },
         "windowPeriod": "300s"
       }
    }
    

This SLI specifies good performance as a 5-minute window in which availability reaches 90% or better. The structure of a basic SLI is shown in [Service-level indicators](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#sli-structs).

You can also embed a request-based SLI in the windows-based SLI. For more information on the embedded structures, see [Structures for request-based SLIs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#request-sli-structs).

## Service-level objectives

A service-level objective (SLO) is represented by a [`ServiceLevelObjective`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelObjective) object. This object includes the following fields:

  * A name
  * A display name
  * The target SLI; an embedded [`ServiceLevelIndicator` object](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#sli-structs)
  * The performance goal for the SLI
  * The compliance period for the SLI



The following shows the JSON representation of an SLO that uses a basic availability SLI as the value of the `serviceLevelIndicator` field: 
    
    
    {
       "name": "projects/PROJECT_NUMBER/services/PROJECT_ID-zone-us-central1-c-csm-main-default-currencyservice/serviceLevelObjectives/3kavNVTtTMuzL7KcXAxqCQ",
       "serviceLevelIndicator": {
         "basicSli": {
           "availability": {},
           "location": [
             "us-central1-c"
           ]
         }
       },
       "goal": 0.98,
       "calendarPeriod": "WEEK",
       "displayName": "98% Availability in Calendar Week"
    }
    

This SLO sets the performance goal at 98 percent availability over a period of a week.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
