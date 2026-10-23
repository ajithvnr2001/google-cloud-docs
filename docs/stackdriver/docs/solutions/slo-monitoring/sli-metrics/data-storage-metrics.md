---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-storage-metrics/
title: Data storage and retrieval services \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:33.903952+00:00
---

# Data storage and retrieval services  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-storage-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Data storage and retrieval services Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud data services discussed on this page include those that store and provide data as a response to a request. SLIs for these services are similar to SLIs for request-response services, described in [Request-response services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/req-resp-metrics), with a primary focus on availability and latency. Note that latency, especially when measuring database-query response time, is often a factor of how much data is being retrieved, and can vary with application workload.

You express a request-based availability SLI by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of "good" requests to total requests. You decide how to filter the metric by using its available labels to arrive at your preferred determination of "good" or "valid".

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure.

**Note:** The filter strings in some of these examples have been line-wrapped for readability.

## Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage) is Google Cloud's worldwide, highly durable object store. Cloud Storage is available in multiple [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes), which let you determine the appropriate cost and retrieval model for your service or use case.

For additional information, see the following:

  * Documentation for [Cloud Storage](https://docs.cloud.google.com/storage/docs).
  * List of [`storage.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-storage).



### Availability SLIs

Cloud Storage writes metric data to Cloud Monitoring using the [`gcs_bucket`](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket) monitored-resource type and the [`api/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#storage/api/request_count) metric type. You can filter the data by using the `response_code` metric label to count "good" requests. You can also use the `method` metric label to measure availability for a specific API method, such as `ReadObject`.

You express a request-based availability SLI for reading objects from a Cloud Storage bucket by using a ratio, [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio), of good requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"storage.googleapis.com/api/request_count\"
             resource.type=\"gcs_bucket\"
             metric.label.\"method\"=\"ReadObject\"
             resource.label.\"bucket_name\"=\"my_bucket\"",
          "goodServiceFilter":
            "metric.type=\"storage.googleapis.com/api/request_count\"
             resource.type=\"gcs_bucket\"
             metric.label.\"method\"=\"ReadObject\"
             resource.label.\"bucket_name\"=\"my_bucket\"
             metric.label.\"response_code\"=\"OK\"",
        }
      }
    }
    

### Latency SLIs

Cloud Storage doesn't provide a latency metric; if latency is a concern, consider instrumenting your service to collect this on the client.

## Bigtable

[Bigtable](https://docs.cloud.google.com/bigtable) is a fully managed, scalable NoSQL database service for large analytical and operational workloads. Bigtable is ideal for storing very large amounts of data in a key-value store. Bigtable also supports high read-and-write throughput at low latency, offering you fast access to large amounts of data.

For additional information, see the following:

  * Documentation for [Bigtable](https://docs.cloud.google.com/bigtable/docs).
  * List of [`bigtable.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-bigtable).



### Availability SLIs

Bigtable writes metric data to Cloud Monitoring using the [`bigtable_table`](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table) monitored-resource type and the following metric types:

  * [`server/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#bigtable/server/request_count), which counts the total number of requests.
  * [`server/error_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#bigtable/server/error_count), which counts the total number of failed requests.



You express a request-based availability SLI for reading objects from a Cloud Storage bucket by using a ratio, [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio), of "bad" requests to total requests, as shown in the following example:

You can use these two metrics to express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for failed requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"bigtable.googleapis.com/server/request_count\"
             resource.type=\"bigtable_table\"
             resource.label.\"table\"=\"my_table\"
             resource.label.\"cluster\"=\"my_cluster\"",
          "badServiceFilter":
            "metric.type=\"bigtable.googleapis.com/server/error_count\"
             resource.type=\"bigtable_table\"
             resource.label.\"table\"=\"my_table\"
             resource.label.\"cluster\"=\"my_cluster\"",
        }
      }
    }
    

### Latency SLIs

To measure latency, Bigtable writes metric data to Cloud Monitoring using the [`bigtable_table`](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table) monitored-resource type and the [`server/latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#bigtable/server/latencies) metric type. You can filter the data by using the `method` metric label to measure the latencies of specific methods.

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure.

The following example SLO expects 99% of all requests to the `my_table` table in the `my_cluster` cluster to fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"bigtable.googleapis.com/server/latencies\"
               resource.type=\"bigtable_table\"
               resource.label.\"table\"=\"my_table\"
               resource.label.\"cluster\"=\"my_cluster\"",
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
    

## Spanner

[Spanner](https://docs.cloud.google.com/spanner) is a fully managed relational database service that offers transactional consistency at global scale, schemas, SQL (ANSI 2011 with extensions), and automatic, synchronous replication for high availability.

For additional information, see the following:

  * Documentation for [Spanner](https://docs.cloud.google.com/spanner/docs).
  * List of [`spanner.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-spanner).



### Availability SLIs

Spanner writes metric data to Cloud Monitoring using the [`spanner_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance) monitored-resource type and the [`query_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#spanner/query_count) metric type. You can filter the data by using the `status` metric label to count successful and failed database queries.

You express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for "good" requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"spanner.googleapis.com/query_count\"
             resource.type=\"spanner_instance\"
             metric.label.\"database\"=\"my_database\"",
          "goodServiceFilter":
            "metric.type=\"spanner.googleapis.com/query_count\"
             resource.type=\"spanner_instance\"
             metric.label.\"database\"=\"my_database\"
             metric.label.\"status\"=\"ok\"",
        }
      }
    }
    

### Latency SLIs

To measure latency, Spanner writes metric data to Cloud Monitoring using the [`spanner_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance) monitored-resource type and the [`api/request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#spanner/api/request_latencies) metric type. You can filter the data by using the `method` metric label to measure the latencies of specific methods. The data includes latencies not just for queries, but for other Spanner API calls.

You express a request-based latency SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure. The following example SLO expects that 99% of all API requests to the `my_database` database fall between 0 and 100 ms in total latency over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"spanner.googleapis.com/api/request_latencies\"
               resource.type=\"spanner_instance\"
               metric.label.\"database\"=\"my_database\"",
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
    

## Datastore

[Datastore](https://docs.cloud.google.com/datastore) is a highly scalable NoSQL database for your applications. Datastore automatically handles sharding and replication, providing you with a highly available and durable database that scales automatically to handle your applications' loads.

For additional information, see the following:

  * Documentation for [Datastore](https://docs.cloud.google.com/datastore/docs).
  * List of [`datastore.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-datastore).



### Availability SLIs

Datastore writes metric data to Cloud Monitoring using the [`datastore_request`](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request) monitored-resource type and the [`api/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#datastore/api/request_count) metric type. You can filter the data by using the `response_code` metric label to count successful and failed API calls or by using the `api_method` metric label to, for example, only measure document reads.

You express a request-based availability SLI by creating a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure for successful requests to total requests, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"datastore.googleapis.com/api/request_count\"
             resource.type=\"datastore_request\"",
          "goodServiceFilter":
            "metric.type=\"datastore.googleapis.com/api/request_count\"
             resource.type=\"datastore_request\"
             metric.label.\"response_code\"=\"success\"",
        }
      }
    }
    

### Latency SLIs

Datastore doesn't currently provide a latency metric. For the available metrics, see [`datastore.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-datastore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
