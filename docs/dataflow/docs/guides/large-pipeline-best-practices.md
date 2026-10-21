---
url: https://docs.cloud.google.com/dataflow/docs/guides/large-pipeline-best-practices/
title: Best practices for large batch pipelines \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:20:23.700161+00:00
---

# Best practices for large batch pipelines  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/large-pipeline-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Best practices for large batch pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to minimize the impact of job failures for large batch pipelines. Large workload failures are particularly impactful because of the time and money required to recover from and fix these failures. Retrying these pipelines from scratch when they fail is expensive in terms of both time and money.

To reduce expensive batch pipeline failures, follow the guidelines in this page. Because you can't always completely avoid failed elements and pipeline failures, the techniques provided focus on increasing resiliency, reducing the cost of failures, and making it easier to debug and understand failures when they occur.

For general pipeline best practices, see [Dataflow pipeline best practices](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices).

## Run small experiments for large jobs

Before you run a large batch job, run one or more smaller jobs on a subset of the dataset. This technique can both provide a cost estimate and help find potential points of failure.

### Cost estimate

Running experiments can provide an estimated floor of the total cost of running the job. Typically, the calculation for the job cost is `cost of test job*size(full dataset)/size(test dataset)`. Depending on the pipeline, the cost can scale superlinearly or, less often, sublinearly. Nevertheless, this step often provides a good rough estimate of the job cost. You can also try different sizes of inputs to get a better estimate of how your costs scale. Use this information to decide whether to proceed with the existing pipeline or to rearchitect your pipeline to reduce costs.

### Find points of failure

Running experiments can expose bugs, potential points of failure, or potential configuration and efficiency issues. You can also examine other pipeline metrics, such as the following metrics:

  * If your pipeline uses almost all of the available memory, it might experience out-of-memory (OOM) exceptions under higher load or with exceptionally large records. You might need to provision more memory for your final job to avoid these OOM errors.
  * If your pipeline experiences dips in throughput, examine your pipeline logs to determine why. You might find a stuck element or a part of your dataset with particularly poor performance. You can process these data points separately, or you can enforce a timeout when processing elements. For more information, see the Time out expensive records section in this document.
  * If your pipeline performs much worse on a task on Dataflow than it does locally, examine your pipeline logic to figure out why. For example, if you're getting the same throughput with eight cores on Dataflow as you are with one core locally, the job might be bottlenecked on contention for a resource. If you find that your performance is worse than expected, consider one or more of the following options: 
    * Run more experiments with different machine or software configurations.
    * Test locally with multiple cores at the same time.
    * Inspect your code to find potential bottlenecks when deploying at scale.



If your pipeline has any Dataflow recommendations, follow them to improve performance.

## Use dead-letter queues to handle unexpected bad data

Pipelines often succeed on most input elements but fail on a small subset of the input. You might not catch this problem when you run small experiments, because these experiments only test a subset of the input. By default, Dataflow retries these [failed tasks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline#detect_an_exception_in_worker_code) four times in batch mode and an unlimited number of times in streaming mode. In batch mode, after reaching the retry limit, your entire job fails. In streaming mode, it can stall indefinitely.

In many jobs, you can exclude these failing elements from the pipeline and complete the rest of the job by using a dead-letter queue (unprocessed messages queue). The dead-letter queue passes failed records to a separate output `PCollection`, which you can manage separately from your main output. This configuration lets you design a policy for these records. For example, you can write them to Pub/Sub manually, inspect and clean them, and then reprocess the records.

Many Apache Beam transforms include built-in support for dead-letter queues. In Java, you can access them with an `[ErrorHandler](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/errorhandling/ErrorHandler.html)` object. In Python, you can access them by using the `[with_exception_handling](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.core.html#apache_beam.transforms.core.ParDo.with_exception_handling)` method. Some transforms have custom ways of defining dead-letter queues, which you can read about in the documentation for the transform. For more information, see [Use dead-letter queues for error handling](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices#dead-letter-queues).

To determine whether your job meets the criteria for a dead-letter queue, see the Limitations section in this document.

### Dead-letter queue limitations

In the following scenarios, a dead-letter queue might not be helpful:

  * **Full worker or`DoFn` lifecycle failures.** If processing fails for the whole worker or bundle, a dead-letter queue can't catch the failure. For example, if your pipeline encounters an out-of-memory (OOM) exception, all active tasks on the VM are failed and retried, without sending anything to the dead-letter queue.
  * **Combines or other aggregations.** If your pipeline performs computations that require all input elements to be present and processed as part of the result, use caution when using a dead-letter queue before this step. Using a dead-letter queue excludes part of your input data from the result. Adding a dead-letter queue might trade correctness for fault tolerance.
  * **Failures on the dead-letter queue path.** If an element fails while being sent to the dead-letter queue sink, the whole pipeline can fail. To avoid this failure, keep your dead-letter queue logic as basic as possible. You can add a wait step (see the `[wait class](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/Wait.html)`) to ensure that your main input finishes before writing your dead-letter queue elements. This configuration might reduce performance and delay error signals from your pipeline.
  * **Partially transformed elements.** If you insert a dead-letter queue part of the way through your pipeline, the dead-letter queue might output the partially transformed element and not have access to the original element. As a result, you can't clean the element and rerun the pipeline against it. Instead, you might need to apply different logic to correlate the output in the dead-letter queue to the original element, or you might need to interpret and process the partially transformed element. It might also result in inconsistent results. For example, if elements are sent down two branches of a pipeline, and each branch sends exception-causing elements to a dead-letter queue, a single input element might make it down one, the other, both, or neither of the branches.



### Time out expensive records

Pipelines might stop responding while processing a small subset of elements that are more expensive or that hit a limitation that causes unresponsiveness, like a deadlock. To mitigate this issue, some transforms let you set a timeout and fail the timed-out elements in any user-code `DoFn`s that encounter this issue. For example, you can use Python's `with_exception_handling` method. When you use timeouts with a dead-letter queue, your pipeline can continue processing healthy elements and make progress, and you can reprocess the expensive elements separately. This configuration can incur a performance cost.

To determine which `DoFn` operations are likely to require a timeout, run small experiments before launching your full pipeline.

## Enable Vertical Autoscaling

If you are unsure how much memory your job needs or think that your job is at risk of running out of memory, enable Vertical Autoscaling. This feature helps avoid OOM failures when pipelines run at larger scale or when they encounter exceptionally large elements.

Because Vertical Autoscaling might increase the cost of your job and doesn't prevent all out-of-memory failures, you still need to address excessive memory consumption issues. Vertical Autoscaling also requires Dataflow Prime, which has [additional limitations](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#unsupported_features) and a [different billing model](https://docs.cloud.google.com/dataflow/pricing#prime-compute-resources).

## Use speculative execution to avoid stragglers

For batch pipelines, you can enable _speculative execution_ , a feature to mitigate the impact of slow-running or stuck tasks. These slow or stuck tasks are also known as _stragglers_. This feature launches redundant, or backup, executions of tasks that are taking too long. The first task to finish is used, and the other is cancelled, which can improve the overall completion time of your pipeline.

Speculative execution can help pipelines complete faster by providing an alternative execution path for work items that are experiencing delays due to slow worker machines or other transient issues such as nondeterministic bugs, resource throttling, or connectivity issues.

### Limitations and considerations

Before enabling speculative execution, consider the following:

  * **Streaming pipelines:** Speculative execution is not supported for streaming pipelines.
  * **Potential change in cost** : The cost impact of this feature is difficult to estimate because stragglers and the provisioning of backup tasks are hard to predict. For example, while a backup work item consumes additional resources, potentially increasing cost, its earlier completion can conversely lead to resource savings and cost reduction. In either scenario, the overall impact is expected to be minimal.
  * **Consistent long-running work items** : Speculative execution might not significantly help with consistently long-running work items such as hot-keys, as the underlying issue causing the slowness would still persist.



For more information about stragglers in batch jobs, see [Troubleshoot stragglers in batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers).

### Enable speculative execution

To enable speculative execution, use the `map_task_backup_mode` Dataflow service option. There are two modes available:

###  Java 

  * `--dataflowServiceOptions=**map_task_backup_mode=ON**`
  * `--dataflowServiceOptions=**map_task_backup_mode=CAUTIOUS**`



###  Python / Go 

  * `--dataflow_service_options=**map_task_backup_mode=ON**`
  * `--dataflow_service_options=**map_task_backup_mode=CAUTIOUS**`



In `ON` mode, a backup task is scheduled if the original task's expected runtime is about 20% longer than a new task's expected runtime.

In `CAUTIOUS` mode, a backup task is scheduled if the original task's expected runtime is about 70% longer than a new task's expected runtime.

To confirm speculative execution is enabled, check the [log messages](https://docs.cloud.google.com/dataflow/docs/guides/logging#MonitoringLogs). Look for entries that show backup tasks were launched. This confirms that speculative execution is triggered. To see these logs, go to the **Job Logs** panel for your pipeline (**Jobs >** choose your job **> Logs section > Job logs**). The log message appears as follows:
    
    
    Backup issued in step STEP_NAME. ADDITIONAL_INFORMATION.
    

## Workarounds for failure-prone pipelines

Some pipelines are particularly error prone. While it is better to address the source of these errors, to reduce the cost of failures consider the following options.

### Materialize intermediate results

Pipelines might have one or more particularly expensive transforms that dominate pipeline execution time. Pipeline failures after this transform can be particularly harmful, because all of the work already completed is lost. To avoid this scenario, consider writing intermediate `PCollections` generated by expensive steps into a sink like Cloud Storage. This configuration reduces the cost of a failure. You need to weigh this advantage against the cost of performing the extra write. You can use this materialized result in one of the following ways:

  1. Split your original pipeline into two pipelines: one that writes the intermediate result and one that reads it.
  2. Only on pipeline failure, read and flatten results from both your original source and your materialized intermediate collection.



To ensure that these materializations are written before further processing, add a wait step (see the `[wait class](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/Wait.html)`) before any subsequent processing steps.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
