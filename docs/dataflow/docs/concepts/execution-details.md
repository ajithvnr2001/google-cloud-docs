---
url: https://docs.cloud.google.com/dataflow/docs/concepts/execution-details/
title: Execution details \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:22.164358+00:00
---

# Execution details  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/execution-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Execution details Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the **Execution details** tab in the Dataflow monitoring interface.

## Overview

When Dataflow runs a job, it converts the _steps_ of the pipeline into _stages_. Whereas each step represents an individual transform, a stage represents a single unit of work that is performed by Dataflow. To optimize the pipeline, Dataflow might [fuse](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization) multiple steps into one stage.

The **Execution details** tab in the Dataflow monitoring interface displays information about the stages of a job. You can use the **Execution details** tab to troubleshoot performance issues, such as:

  * Slow stages that cause performance bottlenecks
  * Stuck stages that are not advancing
  * Worker VMs that are lagging behind other workers



## View execution details

To view the execution details for a job, perform the following steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Execution details** tab.

  4. Select one of the following views:

     * **Stage progress**
     * **Stage workflow**
     * **Worker progress** (batch jobs only)



The following sections describe each of these views.

## Stage progress view

The **Stage progress** view lets you observe the overall progress of the job and compare relative progress between stages. The layout of the **Stage progress** view differs between batch jobs and streaming jobs.

### Stage progress for batch jobs

For batch jobs, the **Stage progress** view shows the job stages in order of their start times. For each stage, it displays the following elements:

  * A bar that shows the start and end times.
  * A line chart that shows the progress of the stage over time as a percentage of the stage's total work.
  * The total time spent in the stage.



![An example of the stage progress view for a batch job.](https://docs.cloud.google.com/static/dataflow/images/exec-details-batch-stage-progress.png)

To filter which stages are displayed, click **Filter stages**. To view the critical path, toggle **Critical path**. The critical path is the sequence of stages that contribute to the overall job runtime. For example, it excludes branches that finished earlier than the overall job, and inputs that did not delay downstream processing.

The **Stage Info** panel shows more detailed information about a stage. To view the details for a stage, click the progress bar for that stage. The **Stage Info** panel shows the following information about a stage:

  * Status
  * Progress as a percentage
  * Start and end times
  * The pipeline steps that this stage encompasses
  * The slowest steps by wall time
  * Details about any [stragglers](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers)



If the panel is not visible, click last_page **Toggle panel "Stage info"**.

### Stage progress for streaming jobs

For streaming jobs, the **Stage progress** view has two visualizations of data freshness. [Data freshness](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#data_freshness_streaming) is the difference between a data element's timestamp and the time when the element is processed. Larger values mean the pipeline is taking longer to process the input data.

The first visualization shows data freshness per stage as a line graph. To see the data freshness at a specific instant of time, hold the pointer over the graph. To select the time range, use the time picker or click the graph and drag to select the range. To filter which stages are displayed, click **Filter stages**.

The graph also highlights anomalies in the data:

  * Potential slowness: Data freshness exceeds the 95th percentile for the selected time window.
  * Potential stuckness: Data freshness exceeds the 99th percentile for the selected time window.



The second visualization shows the stages as a series of bars. The stages are arranged in topological order. Stages with no descendants are shown first, followed by their descendants. The lengths of the bars represent data freshness. To see the data freshness values at a specific point, click the graph. The bars update to show data freshness at the selected time.

The following image shows a job with four stages. At the selected timestamp, the data freshness ranges from 9 seconds to 13 seconds.

![The stage progress view for a streaming job, showing data freshness between 8 and 13 seconds.](https://docs.cloud.google.com/static/dataflow/images/exec-details-streaming-stage-progress.png)

The next image shows the same job with a different timestamp selected. At this point, the data freshness for all stages exceeds 4 minutes, signaling that the pipeline might be stuck.

![The stage progress view for a streaming job, showing data freshness exceeding 4 minutes.](https://docs.cloud.google.com/static/dataflow/images/exec-details-streaming-stage-progress2.png)

The **Stage Info** panel shows more detailed information about a stage. To view the details for a stage, click the progress bar for that stage. The **Stage Info** panel shows the following information about a stage:

  * Status
  * [System lag](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/per_stage_system_lag): The maximum time that an item of data has been awaiting processing
  * [Data watermark](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/per_stage_data_watermark_age): The estimated completion time of data input for this stage
  * Details about any [stragglers](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-stragglers)
  * The pipeline steps that this stage encompasses



If the panel is not visible, click last_page **Toggle panel "Stage info"**.

## Stage workflow

**Stage workflow** view shows the job stages as a workflow graph. To view the details for a stage, click the box for that stage.

![Stage workflow view, showing the hierarchy of execution stages of a job.](https://docs.cloud.google.com/static/dataflow/images/exec-details-batch-stage-workflow.png)

For batch jobs, click **Critical path** to view only the stages that directly contribute to the job's overall runtime.

## Worker progress

For batch jobs, the **Worker progress** view shows the workers for a particular stage. This view is not available for streaming jobs. To access this view, select **Worker progress** and select the stage in **Filter workers by stage**. Alternatively, you can activate this view from the **Stage progress** view as follows:

  1. In the **Stage progress** view, identify the stage that you want to view.
  2. Hold the pointer over the bar for that stage.
  3. In the **Stage** card, click **View workers**. The **Worker progress** view is shown with the stage pre-selected.



Each bar maps to a work item scheduled to a worker. A sparkline that tracks CPU utilization on a worker is located with each worker, making it easier to spot underutilization issues.

![The worker progress view. The workers have bars and sparklines that correspond to work item scheduling and CPU utilization.](https://docs.cloud.google.com/static/dataflow/images/exec-details-batch-worker-progress.png)

## What's next

  * Learn more about [troubleshooting Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).
  * Read about the different components of [Dataflow's web-based monitoring user interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
