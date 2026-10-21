---
url: https://docs.cloud.google.com/dataflow/docs/concepts/about-bottleneck-detector/
title: About the Dataflow bottleneck detector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:12:56.493327+00:00
---

# About the Dataflow bottleneck detector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/about-bottleneck-detector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  About the Dataflow bottleneck detector Stay organized with collections  Save and categorize content based on your preferences. 

![Bottleneck detection in the console due to long processing time operations.](https://docs.cloud.google.com/static/dataflow/images/bottleneck-detector-console_lro.jpeg)

Use the Dataflow bottleneck detector to diagnose progress blocks and optimize pipeline performance in your Dataflow streaming jobs. The detector automatically highlights components in your data pipelines that limit throughput and cause backlogs.

By identifying the exact location and likely cause of execution delays, the bottleneck detector lets you troubleshoot complex Apache Beam streaming pipelines without trial-and-error guesswork.

## How bottleneck detection works

Streaming pipelines usually consist of a sequence of steps connected by queues. Data flows sequentially from upstream sources through intermediate transforms to downstream sinks.

In many pipelines, overall throughput is constrained by a single component or step, creating a _bottleneck_ , or slowdown in job progress. If a downstream component can't process data as quickly as an upstream component produces data, the queue between them begins to fill. For example, if an upstream streaming shuffle component produces data more quickly than a slow downstream user-defined `DoFn` can process the data, the queue fills.

Over time, this delay affects all steps in a pipeline. The backlog increases upstream, eventually limiting the rate at which the pipeline can ingest and process input from the original source. This behavior is called _backlog propagation_.

When backlog propagation occurs, multiple stages of the pipeline can appear unhealthy or slow, even though only a single step is causing the underlying constraint. The bottleneck detector continuously monitors execution delays across all components, including the following:

  * Streaming shuffles
  * User-defined functions (`DoFn` threads)
  * Persistent state commits



When a component experiences a processing delay that exceeds five minutes, the Dataflow bottleneck detector registers it as a bottleneck. It highlights the step in the job execution graph and provides detailed diagnostic information.

## Kinds of bottlenecks

![Bottleneck detection in the console due to hot keys or insufficient key parallelism.](https://docs.cloud.google.com/static/dataflow/images/bottleneck-detector-console_key-parallelism.jpeg)

When a bottleneck is active, the bottleneck detector classifies it into one of the following states:

  * **Processing is stuck and not making progress** : The pipeline's progress is completely halted at the affected step.
  * **Processing is ongoing but falling behind** : The current step is functioning but can't process incoming data as quickly as it arrives, resulting in a growing backlog.
  * **Processing is ongoing but the backlog is steady** : The step is processing data at a rate equal to the incoming rate. The backlog is not growing, but it remains elevated.
  * **Processing is ongoing and catching up from a backlog** : The step is successfully clearing the backlog. If you start a pipeline with an existing backlog, this state is normal and does not require intervention.



For more information about viewing bottleneck detector diagnostics and how to address them, see [Detect and resolve bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks).

## What's next

  * Learn how to [detect and resolve Dataflow pipeline bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks).
  * Review [Troubleshoot slow or stuck streaming jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).
  * For advanced performance profiling, see [Monitor pipeline performance using Cloud Profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
