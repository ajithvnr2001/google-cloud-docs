---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/lb-metrics/
title: Using Cloud Load Balancing metrics \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:45.388468+00:00
---

# Using Cloud Load Balancing metrics  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/lb-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Using Cloud Load Balancing metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page reviews the types of load balancers available from [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) and describes how to use the Cloud Monitoring metrics exposed by them as SLIs.

Cloud Load Balancing services often provide the first entry point for applications hosted in Google Cloud. Load balancers are automatically instrumented to provide information about traffic, availability, and latency of the Google Cloud services that they expose; therefore, load balancers often act as an excellent source of SLI metrics without the need for application instrumentation.

When getting started, you might choose to focus on availability and latency as the primary dimensions of reliability and create SLIs and SLOs to measure and alert on those dimensions. This page provides implementation examples.

For additional information, see the following:

  * [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
  * Documentation for [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
  * List of [`loadbalancing.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing)

**Note:** The filter strings in some of these examples have been line-wrapped for readability.

## Availability SLIs and SLOs

For non-UDP applications, a [request-based](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-type-request) availability SLI is the most appropriate, since service interactions map neatly to requests.

You express a request-based availability SLI by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of good requests to total requests, as shown in the following availability examples. To arrive at your preferred determination of "good" or "valid", you filter the metric using its available labels.

### External layer 7 (HTTP/S) load balancer

HTTP/S load balancers are used to expose applications that are accessed over HTTP/S and to distribute traffic to resources located in multiple regions.

[External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-simple)s write metric data to Monitoring using the [`https_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_http_lb_rule) monitored-resource type and metric types with the prefix `loadbalancing.googleapis.com`. The metric type that is most relevant to availability SLOs is [`https/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/request_count), which you can filter by using the `response_code_class` metric label.

If you choose to not count those requests that result in a 4xx error response code as "valid" because they might indicate client errors, rather than service or application errors, you can write the filter for "total" like this:
    
    
    "totalServiceFilter":
      "metric.type=\"loadbalancing.googleapis.com/https/request_count\"
       resource.type=\"https_lb_rule\"
       resource.label.\"url_map_name\"=\"my-app-lb\"
       metric.label.\"response_code_class\"!=\"400\"",
    

You also need to determine how to count "good" requests. For example, if you choose to count only those that return a 200 OK success status response code, you can write the filter for "good" like this:
    
    
    "goodServiceFilter":
      "metric.type=\"loadbalancing.googleapis.com/https/request_count\"
       resource.type=\"https_lb_rule\"
       resource.label.\"url_map_name\"=\"my-app-lb\"
       metric.label.\"response_code_class\"=\"200\"",
    

You can then express a request-based SLI like this:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"loadbalancing.googleapis.com/https/request_count\"
             resource.type=\"https_lb_rule\"
             resource.label.\"url_map_name\"=\"my-app-lb\"
             metric.label.\"response_code_class\"!=\"400\"",
          "goodServiceFilter":
            "metric.type=\"loadbalancing.googleapis.com/https/request_count\"
             resource.type=\"https_lb_rule\"
             resource.label.\"url_map_name\"=\"my-app-lb\"
             metric.label.\"response_code_class\"=\"200\"",
        }
      }
    },
    

For applications where traffic is served by multiple backends, you might choose to define SLIs for a specific backend. To create an availability SLI for a specific backend, use the [`https/backend_request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/backend_request_count) metric with the `backend_target_name` resource label in your filters, as shown in this example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"loadbalancing.googleapis.com/https/backend_request_count\"
             resource.type=\"https_lb_rule\"
             resource.label.\"url_map_name\"=\"my-app-lb\"
             resource.label.\"backend_target_name\"=\"my-app-backend\"
             metric.label.\"response_code_class\"!=\"400\"",
          "goodServiceFilter":
            "metric.type=\"loadbalancing.googleapis.com/https/backend_request_count\"
             resource.type=\"https_lb_rule\" resource.label.\"url_map_name\"=\"my-app-lb\"
             resource.label.\"backend_target_name\"=\"my-app-backend\"
             metric.label.\"response_code_class\"=\"200\"",
        }
      }
    }
    

### Internal layer 7 (HTTP/S) load balancer

[Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)s write metric data to Monitoring using the [`internal_http_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule) monitored-resource type and metric types with the prefix `loadbalancing.googleapis.com`. The metric type that is most relevant to availability SLOs is [`https/internal_request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/internal_request_count), which you can filter by using the `response_code_class` metric label.

The following shows an example of a request-based availability SLI:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"loadbalancing.googleapis.com/https/internal/request_count\"
             resource.type=\"internal_http_lb_rule\"
             resource.label.\"url_map_name\"=\"my-internal-lb\"
             metric.label.\"response_code_class\"!=\"400\"",
          "goodServiceFilter":
             "metric.type=\"loadbalancing.googleapis.com/https/internal/request_count\"
              resource.type=\"internal_http_lb_rule\"
              resource.label.\"url_map_name\"=\"my-internal-lb\"
              metric.label.\"response_code_class\"=\"200\"",
        }
      }
    },
    

### Layer 3 (TCP) load balancers

TCP load balancers don't provide request metrics because the applications that use these might not be based on the request-response model. None of the `loadbalancing.googleapis.com` metrics provided by these load balancers lend themselves to good availability SLIs.

To create availability SLIs for these load balancers, you must create custom or logs-based metrics. For more information, see [Using custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics) or [Using logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

## Latency SLIs and SLOs

For request-response applications, there are two ways to write latency SLOs:

  * As request-based SLOs.
  * As window-based SLOs.



### Request-based latency SLOs

A request-based SLO applies a latency threshold and counts the fraction of requests that complete under the threshold within a given compliance window. An example of a request-based SLO is "99% of requests complete in under 100 ms within a rolling one-hour window".

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure, as shown in the following latency examples.

A single request-based SLO can't capture both typical performance and the degradation of user experience, where the "tail" or slowest requests see increasingly longer response times. A SLO for typical performance doesn't support understanding tail latency. For a discussion of tail latency, see the section "Worrying About Your Tail" in [Chapter 6: Monitoring Distributed Systems](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/) of [ Site Reliability Engineering](https://landing.google.com/sre/sre-book/toc/).

To mitigate this limitation, you can write a second SLO to focus specifically on tail latency, for example, "99.9% of requests complete in under 1000 ms over a rolling 1 hour window". The combination of the two SLOs capture degradations in both typical user experience and tail latency.

### Window-based latency SLOs

A window-based SLO defines a goodness criterion for time period of measurements and computes the ratio of "good" intervals to the total number of intervals. An example of a window-based SLO is "The 95th percentile latency metric is less than 100 ms for at least 99% of one-minute windows, over a 28-day rolling window":

  * A "good" measurement period is a one-minute span in which 95% of the requests have latency under 100 ms.
  * The measure of compliance is the fraction of such "good" periods. The service is compliant if this fraction is at least 0.99, calculated over the compliance period.



You must use a window-based SLO if the raw metric available to you is a latency percentile; that is, when both of the following are true:

  * The data is bucketed into time periods (for example, into one-minute intervals).
  * The data is expressed in percentile groups (for example, p50, p90, p95, p99).



For this kind of data, each percentile group indicates the time dividing the data groups above and below that percentile. For example, a one-minute interval with a p95 latency metric of 89 ms tells you that, for that minute, the service responded to 95% of the requests in 89 ms or less.

### External Application Load Balancer

External Application Load Balancers use the following primary metric types to capture latency:

  * [`https/total_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/total_latencies): a distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte. Use when overall user experience is of primary importance.

  * [`https/backend_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/backend_latencies): a distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. Use to measure latencies of specific backends serving traffic behind the load balancer.




These metrics are written against the [`https_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_http_lb_rule) monitored-resource type.

**Note:** Both metrics have value type [`DISTRIBUTION`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution), which means that they contain histograms representing distribution of values across buckets. The bucket boundaries for these metrics are created using powers of 1.4; that is, the first bucket is 0-1.4, the second is 1.4-1.96, and so forth. If you have very precise alerting requirements, then you might consider this as you set your thresholds, but most of the time, relying on interpolation for thresholds that fall within a bucket is adequate.

#### Total latency

This example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
                 "metric.type=\"loadbalancing.googleapis.com/https/total_latencies\"
                  resource.type=\"https_lb_rule\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "98% requests under 100 ms"
    }
    

#### Backend latency

This example SLO expects that 98% of requests to the "my-app-backend" backend target fall between 0 and 100 ms in latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"loadbalancing.googleapis.com/https/backend_latencies\"
               resource.type=\"https_lb_rule\"
               resource.label.\"backend_target_name\"=\"my-app-backend\"",
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
    

### Internal Application Load Balancer

Internal Application Load Balancers use two primary metric types to capture latency:

  * [`https/internal/total_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/internal/total_latencies): a distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte. Use when overall user experience is of primary importance.

  * [`https/internal/backend_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/https/internal/backend_latencies): a distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. Use to measure latencies of specific backends serving traffic behind the load balancer.




These metrics are written against the [`internal_http_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule) monitored-resource type.

**Note:** Both metrics have value type [`DISTRIBUTION`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution), which means that they contain histograms representing distribution of values across buckets. The bucket boundaries for these metrics are created using powers of 2 with a scale of 1e-06. If you have very precise alerting requirements, then you might consider this as you set your thresholds, but most of the time, relying on interpolation for thresholds that fall within a bucket is adequate.

#### Total latency

This example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"loadbalancing.googleapis.com/https/internal/total_latencies\"
               resource.type=\"internal_http_lb_rule\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "98% requests under 100 ms"
    }
    

This example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period.

#### Backend latency

This example SLO expects that 98% of requests to the "my-internal-backend" backend target fall between 0 and 100 ms in latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"loadbalancing.googleapis.com/https/internal/backend_latencies\"
               resource.type=\"https_lb_rule\"
               resource.label.\"backend_target_name\"=\"my-internal-backend\"",
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
    

### External layer 3 (TCP) load balancer

External TCP load balancers use a single metric type, [`l3/external/rtt_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/l3/external/rtt_latencies), which records distribution of round-trip time measured over TCP connections for external load-balancer flows.

This metric is written against the [`tcp_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule) resource.

This example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"loadbalancing.googleapis.com/l3/external/rtt_latencies\"
               resource.type=\"tcp_lb_rule\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "98% requests under 100 ms"
    }
    

### Internal layer 3 (TCP) load balancer

Internal TCP load balancers use a single metric type, [`l3/internal/rtt_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#loadbalancing/l3/internal/rtt_latencies), which records distribution of round-trip time measured over TCP connections for internal load-balancer flows.

This metric is written against the [`internal_tcp_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule) resource.

This example SLO expects that 99% of requests fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"loadbalancing.googleapis.com/l3/internal/rtt_latencies\"
               resource.type=\"internal_tcp_lb_rule\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "98% requests under 100 ms"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
