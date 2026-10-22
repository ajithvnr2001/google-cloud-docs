---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/req-resp-metrics/
title: Request-response services \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:30.833517+00:00
---

# Request-response services  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/req-resp-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Request-response services Stay organized with collections  Save and categorize content based on your preferences. 

A request-response service is one where a customer explicitly asks the service to do some work and waits for that work to be completed successfully. The most common examples of such services are:

  * Web applications that human users interact with directly by using a browser.
  * Mobile applications that consist of a client application on a user's mobile phone and an API backend that the client interacts with.
  * API backends that are utilized by other services (rather than human users).



For all of these services, the common approach is to start with availability (measuring the ratio of successful requests) and latency (measuring the ratio of requests that complete under a time threshold) SLIs. For more information on availability and latency SLIs, see [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

You express a request-based availability SLI by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of good requests to total requests. You decide how to filter the metric by using its available labels to arrive at your preferred determination of "good" or "valid".

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure.

**Note:** The filter strings in some of these examples have been line-wrapped for readability.

## Cloud Endpoints

[Cloud Endpoints](https://docs.cloud.google.com/endpoints) is a service for managing APIs. It allows you to take an existing API and expose it with authentication, quotas, and monitoring.

Endpoints is implemented as a proxy in front of the gRPC application server. By measuring the metrics at the proxy, you can correctly handle the case when all backends are unavailable and users are seeing errors. Endpoints writes data to metric types beginning with the prefix `serviceruntime.googleapis.com`.

For more information, see the following:

  * Documentation for [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs).
  * List of [`serviceruntime.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-serviceruntime).



### Availability SLIs

Cloud Endpoints writes metric data to Cloud Monitoring using the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type and the service-runtime [`api/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#serviceruntime/api/request_count) metric type, which you can filter by using the `response_code` metric label to count "good" and "total" requests.

You express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"serviceruntime.googleapis.com/api/request_count\"
             resource.type=\"api\"
             metric.label.\"response_code_class\"!=\"4xx\"",
          "goodServiceFilter":
            "metric.type=\"serviceruntime.googleapis.com/api/request_count\"
             resource.type=\"api\"
             (metric.label.\"response_code_class\"=\"1xx\"" OR
              metric.label.\"response_code_class\"=\"2xx\""),
        }
      }
    }
    

### Latency SLIs

Cloud Endpoints uses the following primary metric types to capture latency:

  * [`api/request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#serviceruntime/api/request_latencies): a distribution of latencies in seconds for non-streaming requests. Use when _overall_ user experience is of primary importance.
  * [`api/request_latencies_backend`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#serviceruntime/api/request_latencies_backend): a distribution of _backend_ latencies in seconds for non-streaming requests. Use to to measure backend latencies directly.
  * [`api/request_latencies_overhead`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#serviceruntime/api/request_latencies_overhead): a distribution of request latencies in seconds for non-streaming requests, _excluding the backend_. Use to measure the overhead introduced by the Endpoints proxy.



Note that the total request latency is the sum of the backend and overhead latencies:
    
    
    request_latencies = request_latencies_backend + request_latencies_overhead
    

Endpoints writes metric data to Cloud Monitoring using the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type and one of the request-latency metric types. None of these metric types provides a `response_code` or`response_code_class` label; therefore, they report latencies for all requests.

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure, as shown in the following examples.

The following example SLO expects that 99% of all requests in the project fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"serviceruntime.googleapis.com/ap/request_latencies\"
               resource.type=\"api\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% requests under 100 ms"
    }
    

The following example SLO expects that 98% of requests fall between 0 and 100 ms in backend latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"serviceruntime.googleapis.com/api/backend_latencies\"
               resource.type=\"api\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.98,
      "rollingPeriod": "3600s",
      "displayName": "98% requests under 100 ms"
    }
    

## Cloud Run

[Cloud Run](https://docs.cloud.google.com/run) is a fully managed compute platform for deploying and scaling containerized applications quickly and securely. It's intended to abstract away all infrastructure management by responding to changes in traffic by automatically scaling up and down from zero almost instantaneously and only charging you for the exact resources you use.

For additional information about Cloud Run observability. see the following:

  * Documentation for [Cloud Run](https://docs.cloud.google.com/run/docs).
  * List of [`run.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-run).



### Availability SLIs

Cloud Run writes metric data to Cloud Monitoring using the [`cloud_run_revision`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision) monitored-resource type and [`request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#run/request_count) metric type. You can filter the data by using the `response_code`or the `response_code_class` metric label to count "good" and "total" requests.

You express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"run.googleapis.com/request_count\"
             resource.type=\"cloud_run_revision\"
             metric.label.\"response_code_class\"!=\"4xx\"",
          "goodServiceFilter":
            "metric.type=\"run.googleapis.com/request_count\"
             resource.type=\"cloud_run_revision\"
             (metric.label.\"response_code_class\"=\"1xx\"" OR
              metric.label.\"response_code_class\"=\"2xx\""),
         }
      }
    }
    

### Latency SLIs

To measure latency, Cloud Run writes metric data to Cloud Monitoring using the [`cloud_run_revision`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision) monitored-resource type and [`request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#run/request_latencies) metric type. The data is a distribution of request latency in milliseconds reaching the revision. You can filter the data by using the `response_code`or the `response_code_class` metric label if you need to explicitly measure the latency of all requests or only the successful requests.

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"run.googleapis.com/request_latencies\"
               resource.type=\"cloud_run_revision"",
            "range": {
               "min": 0,
               "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% requests under 100 ms"
    }
    

## Cloud Run functions

[Cloud Run functions](https://docs.cloud.google.com/functions) is a scalable pay-as-you-go Functions-as-a-Service offering that runs your code without the need to manage any infrastructure. Functions are used in many architecture patterns to do things like event processing, automation, and serving HTTP/S requests.

For information on Cloud Run functions observability, see the following:

  * Documentation for [Cloud Run functions](https://docs.cloud.google.com/functions/docs).
  * List of [`run.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudfunctions).



### Availability SLIs

Cloud Run functions writes metric data to Cloud Monitoring using the [`cloud_function`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function) monitored-resource type and [`function/execution_time`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#cloudfunctions/function/execution_time) metric type. You can filter the data by using the `status` metric label to count "good" and "total" executions.

You express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"cloudfunctions.googleapis.com/function/execution_count\"
             resource.type=\"cloud_function\"",
          "goodServiceFilter":
            "metric.type=\"cloudfunctions.googleapis.com/function/execution_count\"
             resource.type=\"cloud_function\
             metric.label.\"status\"=\"ok\"",
         }
      }
    }
    

### Latency SLIs

To measure latency, Cloud Run functions writes metric data to Cloud Monitoring using the [`cloud_function`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function) monitored-resource type and [`function/execution_times`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#cloudfunctions/function/execution_times) metric type. The data is a distribution of functions execution times in nanoseconds." You can filter the data by using the `status` if you need to explicitly measure the latency of all executions or only the successful executions.

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example SLO expects that 99% of all Cloud Run functions executions fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"cloudfunctions.googleapis.com/function/execution_times\"
               resource.type=\"cloud_function\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% requests under 100 ms"
    }
    

## App Engine

[App Engine](https://docs.cloud.google.com/appengine) provides a fully managed serverless platform to build and run applications. You have the choice of two environments, standard or flexible; for more information, see [Choosing an App Engine environments](https://docs.cloud.google.com/appengine/docs/the-appengine-environments).

For more information on App Engine, see the following:

  * Documentation for [App Engine](https://docs.cloud.google.com/appengine/docs).
  * List of [`appengine.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-appengine).



### Availability SLIs

App Engine writes metric data to Cloud Monitoring using the [`gae_app`](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app) monitored-resource type and the [`http/server/response_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#appengine/http/server/response_count) metric type. You can filter the data by using the `response_code` metric label to count "good" and "total" responses.

You express a request-based availability SLI for App Engine by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"appengine.googleapis.com/http/server/response_count\"
             resource.type=\"gae_app\"
             metric.label.\"response_code\">\"499\"
             metric.label.\"response_code\"<\"399\"",
          "goodServiceFilter":
            "metric.type=\"appengine.googleapis.com/http/server/response_count\"
             resource.type=\"gae_app\"
             metric.label.\"response_code\"<\"299\"",
         }
      }
    }
    

### Latency SLIs

To measure latency, App Engine writes metric data to Cloud Monitoring using the [`gae_app`](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app) monitored-resource type and the [`http/server/response_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#appengine/http/server/response_latencies) metric type. You can filter the data by using the `response_code` metric label to count "good" and "total" executions.

You express a request-based latency SLI for App Engine by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example SLO expects that 99% of all requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"appengine.googleapis.com/http/server/response_latencies\"
               resource.type=\"gae_app\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% requests under 100 ms"
    }
    

## GKE and Istio

[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) is Google's secured and managed Kubernetes service with four-way auto scaling and multi-cluster support. [Istio](https://istio.io/) is an open-source service mesh that allows you to connect, secure, control, and observe services. Istio can be installed on GKE as an add-on—[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)—or by the user from the open source project. In both cases, Istio provides excellent telemetry, including information about traffic, errors, and latency for each service managed by the mesh.

For a full list of Istio metrics, see [`istio.io` metric types](https://docs.cloud.google.com/monitoring/api/metrics_istio).

### Availability SLIs

Istio writes metric data to Cloud Monitoring using the [`service/server/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_istio#istio/service/server/request_count) metric type and one of the following monitored-resource types:

  * [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)
  * [`istio_canonical_service`](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)
  * [`k8s_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)



You can filter the data by using the `response_code` metric label to count "good" and "total" requests. You can also use the `destination_service_name` metric label to count requests for a specific service.

You express a request-based availability SLI for a service running on GKE managed by the Istio service mesh by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"istio.io/service/server/request_count\"
             resource.type=\"k8s_container\"
             metric.label.\"destination_service_name\"=\"frontend\"",
          "goodServiceFilter":
            "metric.type=\istio.io/server/response_count\"
             resource.type=\"k8s_container\"
             metric.label.\"destination_service_name\"=\"frontend\"
             metric.label.\"response_code\"<\"299\"",
        }
      }
    }
    

### Latency SLIs

To measure latency, Istio writes metric data to Cloud Monitoring using the [`service/server/response_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_istio#istio/service/server/response_latencies) metric type and one of the following monitored-resource types:

  * [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)
  * [`istio_canonical_service`](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)
  * [`k8s_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)



You can filter the data by using the `response_code` metric label to count `"good" and "total" requests. You can also use the`destination_service_name` metric label to count requests for a specific service.

You express a request-based latency SLI for a service running on GKE managed by the Istio service mesh by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example SLO expects that 99% of all requests to the `frontend` service fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"istio.io/server/response_latencies\"
               resource.type=\"k8s_container\"
               metric.label.\"destination_service_name\"=\"frontend\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% requests under 100 ms"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
