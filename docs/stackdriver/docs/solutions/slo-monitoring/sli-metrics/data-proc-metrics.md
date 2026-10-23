---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-proc-metrics/
title: Data processing services \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:30.806356+00:00
---

# Data processing services  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-proc-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Data processing services Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud data services discussed on this page include those that process provided data and output the results of that processing, either in response to a request or continuously. Rather than using availability and latency as the primary SLIs for these services, more appropriate choices are the following:

  * _Correctness_ , a measure of how many processing errors the pipeline incurs.
  * _Freshness_ , a measure of how quickly data is processed.



For further information on data pipelines from the SRE perspective, see [Data Processing Pipelines](https://landing.google.com/sre/workbook/chapters/data-processing/) in the [ Site Reliability Engineering Workbook](https://landing.google.com/sre/workbook/toc).

You express a request-based correctness SLI by using the [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure to set up a ratio of items that had processing problems to all items processed. You decide how to filter the metric by using its available labels to arrive at your preferred determination of "problem" and "valid" totals.

You express a request-based freshness SLI by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure.

## Dataflow

[Dataflow](https://docs.cloud.google.com/dataflow) is a fully managed streaming analytics service that minimizes latency, processing time, and cost. You can use Dataflow to process data as a stream or in batches using the [Apache Beam SDK](https://beam.apache.org/).

For additional information, see the following:

  * Documentation for [Dataflow](https://docs.cloud.google.com/dataflow/docs).
  * List of [`dataflow.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-dataflow).



### Correctness SLIs

Dataflow writes metric data to Cloud Monitoring using the [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job) monitored-resource type and the [`job/element_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataflow/job/element_count) metric type, which counts the number of elements added to the pcollection so far. Summing across the `job_name` resource label gives you the number of elements to be processed by the job.

Separately, you can use the [``logging.googleapis.com`/log_entry_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#logging/log_entry_count) metric type with the [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job) monitored-resource type to count the number of errors logged by a particular job, by using the `severity` metric label.

You can use these metrics to express a request-based correctness SLI as a fraction of errors and all processed elements by using a [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio) structure, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"dataflow.googleapis.com/job/element_count\"
             resource.type=\"dataflow_job\"
             resource.label.\"job_name\"=\"my_job\"",
          "badServiceFilter":
            "metric.type=\"logging.googleapis.com/log_entry_count\"
             resource.type=\"dataflow_job\"
             resource.label.\"job_name\"=\"my_job\"
             metric.label.\"severity\"=\"error\"",
        }
      }
    }
    

### Freshness SLIs

Dataflow also writes metric data to Cloud Monitoring using the [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job) monitored-resource type and the [`job/per_stage_system_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataflow/job/per_stage_system_lag) metric type, which measures the current maximum duration that an item of data has been processing or awaiting processing.

You can express a freshness SLI using this metric by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure.

The following example SLO expects that the oldest data element is processed in under 100 seconds 99% of the time over a rolling one-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"dataflow.googleapis.com/job/per_stage_system_lag\"
               resource.type=\"dataflow_job\"
               resource.label.\"job_name\"=\"my_job\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "3600s",
      "displayName": "99% data elements processed under 100 s"
    }
    

You can also express a freshness SLI using a [`WindowsBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#WindowsBasedSli) structure.

The following example SLO expects that 99% of five-minute windows over a rolling one-day period see no (zero) elements processed in over 100 seconds:
    
    
    {
      "displayName": "Dataflow - windowed freshness",
      "serviceLevelIndicator": {
        "windowsBased": {
          "windowPeriod": "300s",
          "metricMeanInRange": {
            "timeSeries":
              "metric.type=\"dataflow.googleapis.com/job/per_stage_system_lag\"
               resource.type=\"dataflow_job\"
               resource.label.\"job_name\"=\"my_job\"",
            "range": {
              "min": "0",
              "max": "100"
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "86400s"
    }
    

Note that, for a window to be considered "good", the metric cannot exceed the threshold specified in `range` at any point during the evaluation window.

## Managed Service for Apache Spark

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) provides a fully managed, purpose-built cluster that can automatically scale to support any Hadoop or Spark data- or analytics-processing job.

For additional information, see the following:

  * Documentation for [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs).
  * List of [`dataproc.googleapis.com` metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-dataproc).



### Correctness SLIs

Managed Service for Apache Spark writes metric data to Cloud Monitoring using the [`cloud_dataproc_cluster`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster) monitored-resource type and the following metric types:

  * [`cluster/job/submitted_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataproc/cluster/job/submitted_count), which counts the total number of jobs submitted.
  * [`cluster/job/failed_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataproc/cluster/job/failed_count), which counts the total number of failed jobs.



You can use these metrics to express a request-based correctness SLI as a ratio, [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio), of failed jobs to all submitted jobs, as shown in the following example:
    
    
    "serviceLevelIndicator": {
      "requestBased": {
        "goodTotalRatio": {
          "totalServiceFilter":
            "metric.type=\"dataproc.googleapis.com/cluster/job/submitted_count\"
             resource.type=\"cloud_dataproc_cluster\"
             resource.label.\"cluster_name\"=\"my_cluster\"",
          "badServiceFilter":
            "metric.type=\"dataproc.googleapis.com/cluster/job/failed_count\"
             resource.type=\"cloud_dataproc_cluster\"
             resource.label.\"cluster_name\"=\"my_cluster\"",
        }
      }
    }
    

### Freshness SLIs

Managed Service for Apache Spark also writes metric data to Cloud Monitoring using the [`cloud_dataproc_cluster`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster) monitored-resource type and the following metric types:

  * [`cluster/job/duration`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataproc/cluster/job/duration), which measures how long jobs stay in processing states. You can filter data on the `state` metric label to identify time spent in specific states. For example, you can create an SLI that measures how long jobs are in the `PENDING` state, to set a maximum allowable wait time before the job begins processing.
  * [`cluster/job/completion_time`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#dataproc/cluster/job/completion_time), which measures how long jobs stay in `cluster/job/completion_time` metric. Use when job completion is a well-understood metric or when the volume of data processed by jobs in a cluster doesn't vary, which would affect processing time.



You can express a freshness SLI using these metrics by using a [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) structure, as shown in the following examples.

The following example SLO uses `cluster/job/duration` and expects that 99% of jobs in "my_cluster" are in the `PENDING` state for under 100 seconds over a rolling 24-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"dataproc.googleapis.com/cluster/job/duration\"
               resource.type=\"cloud_dataproc_cluster\"
               resource.label.\"cluster_name\"=\"my_cluster\"
               metric.label.\"state\"=\"PENDING\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "86400s",
      "displayName": "Dataproc pending jobs"
    }
    

The following example SLO uses `cluster/job/completion_time` and expects that 99% of jobs in "my_cluster" are completed in under 100 seconds over a rolling 24-hour period:
    
    
    {
      "serviceLevelIndicator": {
        "requestBased": {
          "distributionCut": {
            "distributionFilter":
              "metric.type=\"dataproc.googleapis.com/cluster/job/completion_time\"
               resource.type=\"cloud_dataproc_cluster\"
               resource.label.\"cluster_name\"=\"my_cluster\"",
            "range": {
              "min": 0,
              "max": 100
            }
          }
        }
      },
      "goal": 0.99,
      "rollingPeriod": "86400s",
      "displayName": "Dataproc completed jobs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
