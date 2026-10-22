---
url: https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview/
title: Use the Dataflow job monitoring interface \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:15.203471+00:00
---

# Use the Dataflow job monitoring interface  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use the Dataflow job monitoring interface Stay organized with collections  Save and categorize content based on your preferences. 

When you run your pipeline by using Dataflow, you can view that job and any others by using the Dataflow monitoring interface. The monitoring interface lets you see and interact with your Dataflow jobs.

You can access the Dataflow monitoring interface in the [Google Cloud console](https://console.cloud.google.com/).

Tasks that you can perform by using the monitoring interface include the following:

  * See a list of running, completed, and failed jobs.
  * View a graphical representation of a job's stages and the progress of each stage
  * View graphs of job metrics, such as data freshness, resource utilization, and I/O requests.
  * Monitor the estimated cost of a job.
  * View pipeline logs.
  * Identify which steps might cause pipeline lag.
  * Identify causes of latency in your sources and sinks.
  * Understand pipeline errors.

**Note:** Sometimes job data is intermittently unavailable. When data is missing, gaps appear in the job monitoring charts.

## Monitoring interface components

The monitoring interface contains the following visualizers and charts:

[Project monitoring dashboard ](https://docs.cloud.google.com/dataflow/docs/guides/project-monitoring)
    A dashboard that monitors your Dataflow jobs at the project level.
[Jobs list](https://docs.cloud.google.com/dataflow/docs/guides/jobs-list)
    A list of all running Dataflow jobs and all jobs run within the last 30 days, along with their status, region, elapsed time, and other information.
[Job graph](https://docs.cloud.google.com/dataflow/docs/guides/job-graph)
    A graphical representation of a pipeline. The job graph also provides a job summary, a job log, and information about each step in the pipeline.
[Execution details](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details)
    Shows the execution stages of a job, data freshness for streaming jobs, and worker progress for batch jobs.
[Job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf)
    Charts that display metrics over the duration of a job.
[Estimated cost](https://docs.cloud.google.com/dataflow/docs/guides/estimated-cost)
    The estimated cost of your Dataflow job, based on resource usage metrics.
[Recommendations](https://docs.cloud.google.com/dataflow/docs/guides/recommendations)
    Recommendations for improving job performance, reducing cost, and troubleshooting errors.
[Autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics)
    A set of charts that help you to understand the autoscaling behavior of streaming jobs.
[Turnkey alerts](https://docs.cloud.google.com/dataflow/docs/guides/turnkey-alerts)
    Pre-configured alert policies for streaming jobs that monitor backlog processing time and resource utilization.
[Pipeline logs](https://docs.cloud.google.com/dataflow/docs/guides/logging)
    Logs emitted by your pipeline and by the Dataflow service.
[Data sampling](https://docs.cloud.google.com/dataflow/docs/guides/data-sampling)
    A tool that lets you observe sampled data at each step of a pipeline.

## What's next

  * Enable [turnkey alerts](https://docs.cloud.google.com/dataflow/docs/guides/turnkey-alerts) for automated monitoring of Dataflow streaming jobs
  * Use [Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) to create custom alerts and view Dataflow metrics
  * Learn more about [building production-ready data pipelines](https://docs.cloud.google.com/architecture/building-production-ready-data-pipelines-using-dataflow-monitoring)
  * Learn how to [troubleshoot your pipeline](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
