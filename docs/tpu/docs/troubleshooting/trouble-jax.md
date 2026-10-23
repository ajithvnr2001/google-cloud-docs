---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-jax/
title: Troubleshooting JAX - TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:12.525935+00:00
---

# Troubleshooting JAX - TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-jax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting JAX - TPU

This guide provides pointers to JAX troubleshooting information to help you identify and resolve problems you might encounter while training JAX models on Cloud TPU.

For a more general guide to getting started with Cloud TPU, see [Quickstart: Create a TPU instance](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance).

**Note:** If you aren't able to resolve your issue using this guide, see [Getting Support](https://docs.cloud.google.com/tpu/docs/getting-support) for further assistance.

## General JAX issues

If you run into issues while developing your training model or training with JAX, see the [JAX FAQ.](https://jax.readthedocs.io/en/latest/faq.html)

For more general programming errors you might encounter when writing a training application with JAX, see [JAX Errors.](https://jax.readthedocs.io/en/latest/errors.html)

## Profile JAX performance

You can understand how your TPU resources are being utilized using the tools described in [Profiling JAX performance.](https://jax.readthedocs.io/en/latest/profiling.html)

## Troubleshoot memory issues

**Note:** TPU memory ([high bandwidth memory](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions)) is shared across TensorCores on each TPU chip. This enables efficient coordination between the on-chip TensorCores.

You can monitor how the memory is used with the [JAX device memory profiler](https://jax.readthedocs.io/en/latest/device_memory_profiling.html), but you cannot directly manage how it is used.

The JAX device memory profiler can be used to:

  * Figure out [which arrays and executables are in TPU memory](https://jax.readthedocs.io/en/latest/device_memory_profiling.html#understanding-how-a-jax-program-is-using-gpu-or-tpu-memory) at a given time, or
  * [Track down memory leaks.](https://jax.readthedocs.io/en/latest/device_memory_profiling.html#debugging-memory-leaks)



You cannot specify how TPU memory is allocated for specific operations. For more information on JAX-specific TPU performance issues, see [Performance Notes for using TPUs with JAX](https://docs.cloud.google.com/tpu/docs/run-calculation-jax#performance_notes).

## Troubleshoot TPU issues

The following sections describe how to resolve some common issues you might encounter when you run a JAX program on a TPU.

### How can I verify that the TPU is running?

Everything will be run on the TPU as long as JAX doesn't print "No GPU/TPU found, falling back to CPU."

You can verify the TPU is active by either looking at `jax.devices()`, where you should see several TPU devices displayed, or verify programmatically with: `assert jax.devices()[0].platform == 'tpu'`.

### RuntimeError: Unable to initialize backend 'tpu': UNAVAILABLE: No TPU Platform available.

You see the `RuntimeError: Unable to initialize backend 'tpu': UNAVAILABLE: No TPU Platform available` error message or find the following `/tmp/tpu_logs/tpu_driver.WARNING` warning on the TPU VM:
    
    
    W1118 17:40:20.985243   23901 tpu_version_flag.cc:57] No hardware is found. Using default TPU version:VERSION
    

This error can indicate that you're running the wrong TPU VM version. Verify that you are running the [current JAX runtime version](https://github.com/jax-ml/jax/releases) and retry.

## Troubleshoot TPU and GKE issues

To help with troubleshooting, enable verbose logging in your GKE workload manifest, and then provide the logs to GKE support.
    
    
    TPU_MIN_LOG_LEVEL=0 TF_CPP_MIN_LOG_LEVEL=0 TPU_STDERR_LOG_LEVEL=0
    

The following sections describe error messages related to TPU and GKE setups and resolutions.

### no endpoints available for service 'jobset-webhook-service'

This error means the jobset wasn't installed properly. Check to see if jobset-controller-manager deployment Kubernetes Pods are running. For more information, see the [JobSet troubleshooting documentation](https://jobset.sigs.k8s.io/docs/troubleshooting/#1-webhook-not-available-error-when-attempting-to-create-a-jobset).

### TPU initialization failed: Failed to connect

Make sure your GKE node version is 1.30.4-gke.1348000 or later (GKE 1.31 is not supported).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
