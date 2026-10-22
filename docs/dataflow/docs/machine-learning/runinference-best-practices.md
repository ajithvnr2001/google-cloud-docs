---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/runinference-best-practices/
title: RunInference transform best practices \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:18.312056+00:00
---

# RunInference transform best practices  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/runinference-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  RunInference transform best practices Stay organized with collections  Save and categorize content based on your preferences. 

When using Dataflow for ML inference, we recommend that you use the `RunInference` transform. Using this transform comes with a number of benefits, including:

  * Intelligent model memory management optimized for a Dataflow worker when performing local inference.
  * Dynamic batching which uses pipeline characteristics and user-defined constraints to optimize performance.
  * ML-aware Dataflow backend features which can provide better throughput and latency.
  * Intelligent backoff and autoscaling mechanisms when running into remote inference quotas.
  * Production-ready metrics and operational features.



When using `RunInference`, there are several things to consider:

## Memory management

When you load a medium or large ML model, your machine might run out of memory. Dataflow provides tools to help avoid out-of-memory (OOM) errors when loading ML models.

To effectively tune your pipeline, it's important to understand the different units of compute in Dataflow:

  * **VM** : The virtual machine instance (machine type), such as `n1-standard-8`. In Dataflow documentation, this is sometimes referred to as a _worker_.
  * **Process** : A Python SDK worker process. By default, Dataflow launches one process per vCPU on the VM.
  * **Thread** : A single executable task running within a process. Each thread executes a `DoFn`.



### Model memory versus data memory

OOM errors generally fall into two categories:

  1. **Model-related memory issues** : Occur when the ML model itself is too large to fit multiple copies in memory.
  2. **Data-related memory issues** : Occur when processing large amounts of data (unrelated to the model size) exceeds the available memory.



Use the following table to determine the appropriate approach for your scenario.

Scenario | Solution  
---|---  
The models are small enough to fit in memory. |  Use the `RunInference` transform without any additional configurations. The `RunInference` transform shares the models across threads. If you can fit one model per CPU core on your machine, then your pipeline can use the default configuration. This loads one model copy per **process**.   
Multiple differently-trained models are performing the same task. |  Use per-model keys. For more information, see [Run ML inference with multiple differently-trained models](https://docs.cloud.google.com/dataflow/docs/notebooks/per_key_models).   
One model is loaded into memory, and all processes on a VM share this model. |  Use `large_model=true`. This loads one model copy per **VM** and shares it across all processes on that VM. For more information, see [Run ML inference with multiple differently-trained models](https://docs.cloud.google.com/dataflow/docs/notebooks/per_key_models). If you're building a custom model handler, instead of using the `large_model` parameter, override the [`share_model_across_processes`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.ModelHandler.share_model_across_processes) parameter.  
You need to configure the exact number of models loaded onto your machine. |  To control exactly how many models are loaded per VM, set the `large_model=True` and set the [`model_copies=INT`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.ModelHandler.model_copies) to load a specific number of copies. If you're building a custom model handler, override the `model_copies` parameter. To use `model_copies=INT`, you must set `large_model=True`. A value of `1` (the default) effectively loads a single copy per VM when `large_model=True`.  
You are running out of memory due to data processing, not the model size (data exceeds memory). |  Try the following options in order:

  1. Reduce the number of threads by using the `num_worker_harness_threads` pipeline option.
  2. Use a high-memory machine type (for example, `n1-highmem-8`).
  3. As a last resort, use the pipeline option `--experiments=no_use_multiple_sdk_containers`. Note that this severely limits parallelism due to Python's Global Interpreter Lock (GIL).

  
  
For more information about memory management with Dataflow, see [Troubleshoot Dataflow out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).

## Batching

There are many ways to do batching in Beam, but when performing inference we recommended you let the `RunInference` transform handle the batching. If your model performs best with a specific batch size, consider constraining the target batch size parameters of `RunInference`. Most model handlers expose the maximum and minimum batch sizes as parameters. For example, to control the batch size fed into a HuggingFace pipeline, you could define the following model handler:
    
    
    mh = HuggingFacePipelineModelHandler('text-classification', min_batch_size=4, max_batch_size=16)
    

The `RunInference` transform always honors the maximum batch size. Minimum batch size is a target, but is not guaranteed to be honored in all cases. For example, see Bundle-Based Batching in the following section.

### Bundle-Based Batching

Dataflow passes data to transforms in [bundles](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#error_and_exception_handling). These bundles can vary in size depending on Dataflow-defined heuristics. Typically, bundles in batch pipelines are quite large (O(100s) elements), while for streaming pipelines they can be quite small (including size 1).

By default, `RunInference` generates batches out of each bundle and doesn't batch across bundles. This means if you have a minimum batch size of 8, but only 3 elements left in your bundle, `RunInference` uses a batch size of 3. Most model handlers expose a `max_batch_duration_secs` parameter that lets you override this behavior. If `max_batch_duration_secs` is set, `RunInference` batches across bundles. If the transform cannot achieve its target batch size with a single bundle, it waits at most `max_batch_duration_secs` before yielding a batch. For example, to enable cross-bundle batching when using a HuggingFace pipeline, you can define the following model handler:
    
    
    mh = HuggingFacePipelineModelHandler('text-classification', min_batch_size=4, max_batch_size=16, max_batch_duration_secs=3)
    

This feature helps if you experience very low batch sizes in your pipeline. Otherwise, the synchronization cost to batch across bundles usually isn't worth using, because it can cause an expensive [shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch).

## Handling Failures

Handling errors is an important part of any production pipeline. Dataflow processes elements in arbitrary bundles and retries the complete bundle if an error occurs for any element in that bundle. If you don't apply additional error handling, Dataflow retries bundles that include a failing item four times when running in batch mode. The pipeline fails completely when a single bundle fails four times. When running in streaming mode, Dataflow retries a bundle that includes a failing item indefinitely, which might cause your pipeline to permanently stall.

`RunInference` provides a built-in error handling mechanism with its [`with_exception_handling` function](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference.with_exception_handling). When you apply this function, it routes all failures to a separate failure `PCollection` along with their error messages. This lets you reprocess them. If you associate preprocessing or postprocessing operations with your model handler, `RunInference` routes those to the failure collection as well. For example, to gather all failures from a model handler with preprocessing and postprocessing operations, use the following logic:
    
    
    main, other = pcoll | RunInference(model_handler.with_preprocess_fn(f1).with_postprocess_fn(f2)).with_exception_handling()
    
    # handles failed preprocess operations, indexed in the order in which they were applied
    other.failed_preprocessing[0] | beam.Map(logging.info)
    
    # handles failed inferences
    other.failed_inferences | beam.Map(logging.info)
    
    # handles failed postprocess operations, indexed in the order in which they were applied
    other.failed_postprocessing[0] | beam.Map(logging.info)
    

### Timeouts

When you use the `with_exception_handling` feature of `RunInference`, you can also set a timeout for each operation, which is counted per batch. This lets you avoid a single stuck inference making the entire pipeline unresponsive. If a timeout occurs, the timed-out record is routed to the failure `PCollection`, all model state is cleaned up and recreated, and normal execution continues.
    
    
    # Timeout execution after 60 seconds
    main, other = pcoll | RunInference(model_handler).with_exception_handling(timeout=60)
    

Starting with Beam 2.68.0, you can also specify a timeout using the `--element_processing_timeout_minutes` pipeline option. In this case, a timeout causes a failed work item to be retried until it succeeds, instead of routing the failed inference to a [dead-letter queue](https://docs.cloud.google.com/dataflow/docs/guides/large-pipeline-best-practices#use-dlqs).

## Working with Accelerators

When using accelerators, many model handlers have accelerator-specific configurations you can enable. For example, when using a GPU and Hugging Face pipelines, we recommend you set the `device` parameter to GPU:
    
    
    mh = HuggingFacePipelineModelHandler('text-classification', device='GPU')
    

If you are loading more than one copy of your model onto a single GPU (for example, by using `model_copies > 1`), we recommend enabling NVIDIA Multi-Process Service (MPS). MPS allows multiple processes to share GPU resources concurrently, which can significantly improve throughput and parallelism. For more information, see [Improve performance on a shared GPU by using NVIDIA MPS](https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps).

We also recommend that you start with a single VM instance and run your pipeline locally there. To do this, follow the steps described in the [GPU troubleshooting guide](https://docs.cloud.google.com/dataflow/docs/gpu/troubleshoot-gpus#debug-job). This can significantly reduce the amount of time needed to get a pipeline running. This approach can also help you better understand your job's performance.

For more information on using accelerators in Dataflow, see Dataflow's documentation on [GPUs](https://docs.cloud.google.com/dataflow/docs/gpu) and [TPUs](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support).

## Dependency Management

ML pipelines often include large and important dependencies, such as PyTorch or TensorFlow. To manage these dependencies, we recommend using [custom containers](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) when you deploy your job to production. This ensures that your job executes in a stable environment over multiple runs and simplifies debugging.

For more information on dependency management, see Beam's [Python Dependency Management page](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/).

## What's next

  * Explore the [Dataflow ML notebooks](https://docs.cloud.google.com/dataflow/docs/machine-learning/notebooks) for practical examples.
  * Get in-depth information about using ML with Apache Beam in the [AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) documentation.
  * Learn more about the [`RunInference` API](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.html#apache_beam.ml.inference.RunInference).
  * Learn about the [metrics](https://beam.apache.org/documentation/ml/runinference-metrics/) that you can use to monitor your `RunInference` transform.
  * Return to the [About Dataflow ML](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-about) page for an overview of Dataflow's ML capabilities.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
