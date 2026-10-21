---
url: https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks/
title: Detect and resolve Dataflow pipeline bottlenecks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:57.628813+00:00
---

# Detect and resolve Dataflow pipeline bottlenecks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Detect and resolve Dataflow pipeline bottlenecks Stay organized with collections  Save and categorize content based on your preferences. 

In streaming pipelines, a slow step or transform can constrain throughput and cause backlog propagation, increasing overall job latency. The Dataflow bottleneck detector automatically identifies and highlights the specific steps causing backlogs in the Google Cloud Console, helping you quickly diagnose and resolve execution delays without trial-and-error debugging.

For a conceptual overview of how Dataflow identifies bottlenecks and propagates backlogs, see [About the Dataflow bottleneck detector](https://docs.cloud.google.com/dataflow/docs/concepts/about-bottleneck-detector).

## Before you begin

Before you use the bottleneck detector for troubleshooting, make sure your job and project meet the following requirements:

  * You have a running streaming Dataflow job.
  * Your job is run using **Streaming Engine**. Bottleneck detection is not supported for jobs that don't run on Streaming Engine.
  * You have the Identity and Access Management (IAM) permissions required to view Dataflow jobs. For more information, see [Dataflow IAM roles](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#roles).



## View active bottlenecks in the Google Cloud Console

You can view active bottleneck notifications and alerts directly in the Dataflow monitoring interface.

  1. In the Google Cloud Console, go to the **Dataflow** page.

[Go to Dataflow](https://console.cloud.google.com/dataflow)

  2. In the jobs list, select your streaming job to open the job details page.

  3. Under the **Job graph** tab, review the execution graph:

     * Steps experiencing active bottlenecks display a colored warning or alert icon.
     * An alert indicates that a processing delay of more than five minutes has occurred at this step.
  4. Click the step that displays the warning icon.

![A sample job graph with the failing step identified.](https://docs.cloud.google.com/static/dataflow/images/bottleneck-detector-console_steps_pubsub.jpeg)

  5. In the **Step Info** panel on the right side of the screen, locate the **Bottlenecks** section. This section displays:

     * The kind of bottleneck. For example, falling behind, backlog is steady, or stuck.
     * The likely cause, if identified by the diagnostic engine.
     * The duration and related diagnostic details.

![Bottleneck detection in the Step Info panel.](https://docs.cloud.google.com/static/dataflow/images/bottleneck-detector-console_pubsub.jpeg)




## Resolve bottleneck causes

To resolve a bottleneck, identify the likely cause in the **Step Info** panel and follow the step-by-step guidance for the cause in [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks#causes).

## Monitor bottlenecks with Monitoring

If you want to set up programmatic alerting or view bottleneck activity over time, use Monitoring. The bottleneck detector exports the following metrics:

  * **[`dataflow.googleapis.com/job/is_bottleneck`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/is_bottleneck)** : A boolean value indicating whether the stage is an active bottleneck, along with labels specifying the kind of bottleneck and the likely cause.
  * **[`dataflow.googleapis.com/job/backlogged_keys`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/backlogged_keys)** : The number of keys backed up in the bottlenecked stage.
  * **[`dataflow.googleapis.com/job/recommended_parallelism`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/recommended_parallelism)** : The recommended parallelism value to alleviate the bottleneck in the affected stage.



For information on creating charts and alerts using these metrics, see [Use Monitoring for Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).

## What's next

  * Learn more about the [Dataflow bottleneck detector concepts](https://docs.cloud.google.com/dataflow/docs/concepts/about-bottleneck-detector).
  * Follow the general guide to [Troubleshoot and debug Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
