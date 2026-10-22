---
url: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-batch-jobs/
title: Troubleshoot slow or stuck batch jobs \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:50.585169+00:00
---

# Troubleshoot slow or stuck batch jobs  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-batch-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Troubleshoot slow or stuck batch jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to troubleshoot common causes of slow or stuck Dataflow batch jobs.

If your batch job is slow or stuck, use the [Execution details](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details) tab to find more information about the job and to identify the stage or worker that's causing a bottleneck.

## Identify the root cause

  1. Check whether the job is running into issues during worker startup. For more information, see [Error syncing pod](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#error-syncing-pod).

To verify the job has started processing data, look in the [job-message](https://docs.cloud.google.com/dataflow/docs/guides/logging#log-types) log for the following log entry:
         
         All workers have finished the startup processes and began to receive work requests
         

  2. To compare job performance between different jobs, make sure the volume of input data, worker configuration, autoscaling behavior, and [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) settings are the same.

  3. Check the [job-message](https://docs.cloud.google.com/dataflow/docs/guides/logging#log-types) logs for issues such as quota limits, stockout issues, or IP address exhaustion.

  4. In the [**Execution details**](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details) tab, compare the [stage progress](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details#progress-batch) to identify stages that took longer.

  5. Look for any stragglers in the job. For more information, see [Troubleshooting stragglers in batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers).

  6. Check the throughput, CPU, and memory utilization metrics.

  7. Check the [worker logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#log-types) for warnings and errors.

     * If the worker logs contain errors, view the stack trace. Investigate whether the error is caused by a bug in your code.
     * Look for Dataflow errors. See [Troubleshoot Dataflow errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors).
     * Look for [out-of-memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom#find-errors), which can cause a stuck pipeline. If you see out-of-memory errors, follow the steps in [Troubleshoot Dataflow out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).
     * To identify a slow or stuck step, check the worker logs for `Operation ongoing` messages. View the stack trace to see where the step is spending time. For more information, see [Processing stuck or operation ongoing](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck).
  8. Check for hot keys.

  9. If you aren't using [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), check the [shuffler logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#log-types) for warnings and errors during shuffle operation. If you see an [RPC timeout error](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-networking#worker-communicate-firewall-ports) on port 12345 or 12346, your job might be missing a firewall rule. See [Firewall rules for Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#firewall_rules).

  10. If the Portable Runner is enabled, check the [harness](https://docs.cloud.google.com/dataflow/docs/guides/logging#log-types) logs for errors. For more information, see [Troubleshoot the Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner#debugging).




## Identify stragglers

A straggler is a work item that is slow relative to other work items in the stage. For information about identifying and fixing stragglers, see [Troubleshoot stragglers in batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers).

## Identify slow or stuck stages

To identify slow or stuck stages, use the [**Stage progress**](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details#progress-batch) view. Longer bars indicate that the stage takes more time. Use this view to identify the slowest stages in your pipeline.

After you find the bottleneck stage, you can take the following steps:

  * Identify the lagging worker within that stage.
  * If there are no lagging workers, identify the slowest step by using the [**Stage info**](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details#stage-info) panel. Use this information to identify candidates for user code optimization.



## Identify a lagging worker

To identify a lagging worker for a specific stage, use the [**Worker progress**](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details#worker-progress) view. This view shows whether all workers are processing work until the end of the stage, or if a single worker is stuck on a lagging task. If you find a lagging worker, take the following steps:

  * View the log files for that worker. For more information, see [Monitor and view pipeline logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#MonitoringLogs).
  * View the [CPU utilization metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#cpu-use) and the [worker progress](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details#worker-progress) details for lagging workers. If you see unusually high or low CPU utilization, in the log files for that worker, look for the following issues: 
    * [`A hot key ... was detected`](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#hot-key-detected)
    * [`Processing stuck ... Operation ongoing`](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck)



## Tools for debugging

When you have a slow or stuck pipeline, the following tools can help you diagnose the problem.

  * To correlate incidents and identify bottlenecks, use [Cloud Monitoring for Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).
  * To monitor pipeline performance, use [Cloud Profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline).
  * Some transforms are better suited to high-volume pipelines than others. Log messages can [identify a stuck user transform](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck) in either batch or streaming pipelines.
  * To learn more about a stuck job, use [Dataflow job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf).



For additional metrics that aren't included in the Dataflow monitoring web interface, see the complete list of Dataflow metrics in [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-dataflow).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
