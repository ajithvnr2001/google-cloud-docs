---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-tf/
title: Troubleshooting TensorFlow - TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:00.096082+00:00
---

# Troubleshooting TensorFlow - TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting TensorFlow - TPU

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This guide, along with the [FAQ](https://docs.cloud.google.com/tpu/docs/faq), provides troubleshooting help for users who are training TensorFlow models on Cloud TPU. If you are troubleshooting PyTorch or JAX training, you can refer to the troubleshooting documents for those frameworks:

  * [Troubleshooting PyTorch - TPU](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-pytorch)
  * [Troubleshooting JAX - TPU](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-jax)



For more general guides on how to use Cloud TPU, see:

  * [Cloud TPU quickstart guides](https://docs.cloud.google.com/tpu/docs/quick-starts)
  * [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/tpus)

**Note:** If you aren't able to resolve your issue using this guide, see [Getting Support](https://docs.cloud.google.com/tpu/docs/getting-support) for further assistance.

## Overview

Common issues encountered with Cloud TPUs fall into the following categories:

  1. Problems connecting to the TPU

  2. Debugging common errors

  3. Reducing memory usage

  4. Improving training speed

  5. Debugging drops in model accuracy




## Trouble connecting to the TPU server

This section describes how to troubleshoot situations where TensorFlow stops responding or prints an error when connecting to the TPU. The TPU graph compilation step can take a long time for large models, so let the script execute for at least 5 minutes before concluding that it has stopped responding.

The first step is to verify whether the issue is with the server itself, or with your TensorFlow training pipeline. To do this, run your TensorFlow program and verify that it works correctly. If there are still connection issues, this confirms that it is an issue with the TPU server. In this case:

  1. Run the following command to list the available TPUs. Replace zone and project-id with your zone and project ID.
         
         (vm)$ gcloud compute tpus tpu-vm list --zone zone --project project-id

This prints output such as: 
         
         NAME       ZONE           ACCELERATOR_TYPE  NETWORK_ENDPOINT   NETWORK  RANGE          STATUS
         TPU_NAME   us-central1-b  v2-8              10.240.1.2:8470    default  10.240.1.0  READY

  2. Verify that this TPU is listed as `READY`.

  3. If your TPU is not listed as `READY` or you are still having trouble connecting, manually restart the server with:
         
         (vm)$ gcloud compute tpus tpu-vm stop TPU_NAME && gcloud compute tpus tpu-vm start TPU_NAME

This might take several minutes to complete.

  4. Re-run the `gcloud compute tpus tpu-vm list` command and wait for the TPU to be in the `READY` state. This might take several minutes.

  5. Try to run your program again.

  6. If you are still having trouble, ask for help using one of the mechanisms described in [Getting Support](https://docs.cloud.google.com/tpu/docs/getting-support).




If your code runs correctly but your model still stops responding, then the issue is likely with your training pipeline. To debug this, start by replacing the TPUStrategy in your code with the default strategy. When you use the default strategy, wherever you use `strategy.scope()` or `strategy.run()`, the model runs on CPU (or GPU if present) instead of on the TPU. If the model runs on CPU and not TPU, there must be a TPU-specific issue. If it still does not run, best practice is to debug the issue on CPU.

## Loss of `ssh` connection during training

Your `ssh` connection to the Cloud TPU might time out during a long running training (particularly if you are using the Cloud Shell). At that point, there is no output to the TPU console and it might appear as though the TPU has stopped training. To avoid this, run the training session with a terminal multiplexer or session management tool such as `tmux` or `screen`. This will keep the `ssh` connection active regardless of the length of the training.

## Debugging common errors

This section describes how to troubleshoot common errors that you might encounter when training models on Cloud TPU.

### Cannot create a TPU

When creating a Cloud TPU, you may see the following error:
    
    
    googleapiclient.errors.HttpError: < HttpError 403 when requesting https://content-tpu.googleapis.com/v1/projects/{PROJECT}/locations/{ZONE}/nodes/{TPU_NAME}?alt=json returned "Request had insufficient authentication scopes."
    

This is a permissions issue and can be resolved by running the following command:
    
    
    gcloud auth login --update-adc

This command updates your Application Default Credentials (ADC) and should solve the issue. For more information, see [gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login).

### Dynamic shapes not supported

**Error Message**
    
    
    ValueError: shape [_Shape_] must have a fixed size for dimension
    _d_ that is known at graph construction time.
    

**Frameworks and Configurations Affected**

This message only occurs during XLA compilation with TensorFlow.

**Details**

To execute a model on the TPU, Cloud TPU compiles the model using the [XLA compiler](https://www.tensorflow.org/performance/xla/). While this compilation step significantly improves training speed and memory usage, the shapes (dimension sizes) of all tensors in the graph must be known at graph compilation time. If any shapes cannot be determined at compile time, TPU compilation fails with an error like the one shown previously.

One common op that returns a dynamic shape is `dataset.batch(batch_size)`, since the number of samples remaining in a stream might be less than the batch size. Therefore, when training on the TPU, set `drop remainder=True` for `dataset.batch`. This potentially drops the last few samples from a file to ensure that every batch has a static shape of batch_size. For example:
    
    
    dataset = tf.data.Dataset.range(8)
    dataset = dataset.batch(3, drop_remainder=True)
    

### Unavailable TensorFlow op

**Error Message**
    
    
    NotFoundError: No registered '_OpName_ ' OpKernel for XLA_TPU_JIT
    devices compatible with node
    

**Frameworks and Configurations Affected**

This message can occur when training with TensorFlow.

**Details**

The model uses a TensorFlow op which is not available on the TPU.

For a list of ops available on the TPU, along with plans for future support and suggestions for workarounds, see the guide to [available TensorFlow Ops](https://docs.cloud.google.com/tpu/docs/tensorflow-ops).

### Out-of-memory error message

**Error Message**
    
    
    ResourceExhaustedError: Ran out of memory in memory space hbm; used:
    _YYY_ ; limit: 7.48G.
    

**Frameworks and Configurations Affected**

This message can occur when training with TensorFlow, PyTorch, or JAX.

**Details**

Each Cloud TPU is made of eight TPU cores, v2 TPUs have 8GB and v3 TPUs have 16GB of RAM (or HBM, High-Bandwidth Memory). This memory is used to store the weight (variable) tensors, as well as intermediate result tensors needed for gradient computation. If the model is too large to fit into TPU RAM, the initialization fails and the error message is printed. See the section on reducing memory usage for more help.

Tips for reducing memory use:

  * Check for [excessive tensor padding](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-tf#memory-tensor-padding)
  * Use the [bfloat16](https://docs.cloud.google.com/tpu/docs/bfloat16) format
  * If the input sizes or model is too large, you might be able to use TensorFlow's [experimental model parallelism](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) to address model size.



### Problems stopping execution

If TensorFlow encounters an error during TPU execution, the script sometimes seems to stop responding rather than exit to the shell. If this happens, press `CTRL+C` on the keyboard to trigger a `SIGQUIT`, which causes Python to exit immediately.

Similarly, pressing `CTRL+C` during TPU execution does _not_ shut down TensorFlow immediately, but instead waits until the end of the current iteration loop to exit cleanly.

If you encounter any new errors when re-connecting to the TPU after exiting in this manner, manually reset the TPU server with the commands: 
    
    
    gcloud compute tpus tpu-vm stop tpu-name --zone=zone
    gcloud compute tpus tpu-vm start tpu-name --zone=zone

where tpu-name is taken from the first column displayed by the `gcloud compute tpus tpu-vm list` command and zone is the zone shown in the second column.

### Excessive tensor padding

**Possible Cause of Memory Issue**

Tensors in TPU memory are padded, that is, the TPU rounds up the sizes of tensors stored in memory to perform computations more efficiently. This padding happens transparently at the hardware level and does not affect results. However, in certain cases the padding can result in significantly increased memory use and execution time.

**How to Reduce Memory Usage**

The TPU software attempts to lay out tensors in memory to maximize computational efficiency and minimize padding. This memory layout process is complex, however, for the best results the model should obey the following rule of thumb. To minimize memory overhead and maximize computational efficiency, one of the following must be true:

  * The total batch size should be a multiple of 64 (8 per TPU core), and feature dimensions should be a multiple of 128,

_or_

  * The total batch size should be a multiple of 1024 (128 per TPU core), and feature dimensions should be a multiple of 8.




Using a batch size of 1024 _and_ feature dimensions that are a multiple of 128 results in the best efficiency, although this may not be possible for all models. For clarity, "feature dimension" refers to the hidden size of a fully-connected layer or the number of output channels in a convolution. Not all layers can conform to this rule, especially the first and last layers of the network. This is fine, and it is expected that most models require some amount of padding.

## Reducing memory usage

If you encounter an out-of-memory error when executing your model on the TPU, you must take steps to reduce the model's memory usage.

The most effective ways to reduce memory usage are to:

  * Reduce excessive tensor padding
  * Reduce the batch size



### Batch size or model too large

**Possible Cause of Memory Issue**

When training a neural network on a CPU, GPU, or TPU, the memory use comes from two places:

  1. The memory use is proportional to the number of weights in the model.
  2. Storing intermediate activations from the forward pass necessary to compute the backward pass. The memory use is directly proportional to the batch size, layer sizes, and number of layers.



Therefore, the memory required by a model is largely dependent on the batch size.

The memory required by a model is dependent on the number of layers in the network.

The TPU runtime attempts to optimize operators to fit the model in memory (called [rematerialization](https://en.wikipedia.org/wiki/Rematerialization), similar to [gradient checkpointing](https://medium.com/@yaroslavvb/fitting-larger-networks-into-memory-583e3c758ff9)), but it is not always able to do this.

**How to Reduce Memory Usage**

Slowly reduce the batch size until it fits in memory, making sure that the total batch size is a multiple of 64 (the per-core batch size should be a multiple of 8). Keep in mind that larger batch sizes are more efficient on the TPU. A total batch size of 1024 (128 per core) is generally a good starting point.

If the model cannot be run on the TPU even with a small batch size (for example, 64), try reducing the number of layers or the layer sizes.

## Improving training speed

If your model is able to run successfully on the TPU, but the training speed is less than expected, this section outlines several potential ways to improve the speed. See the [Performance guide](https://docs.cloud.google.com/tpu/docs/performance-guide#model_processing_performance) for other suggestions on how to improve training performance.

### Too few steps per execution per training loop

**Description of Performance Issue**

Passing the argument `steps_per_execution` to `Model.compile` controls how many training steps are executed between host callbacks. Each host callback requires significant communication between the TPU server's host CPU and the TPU device, so if `steps_per_execution` is too small, it can slow down training.

**How to Know if Your Model is Affected**

If a TPU profile reveals frequent host CPU callbacks between TPU device steps, then your training can benefit from a larger `steps_per_execution` value.

**How to Mitigate**

Set `steps_per_execution` to a larger value. Note that `steps_per_execution` can be set to a large value, but keep in mind logging messages and saving a checkpoint can only occur after the specified number of steps have run.

### Input processing bottleneck

**Description of Performance Issue**

While the TPU is training on a particular chunk of data, the input processing function prepares the next chunk of data on the CPU. If your input function takes _longer_ than the model function, the TPU is left idle while your input function is retrieving data.

**How to Know if Your Model is Affected**

Follow the instructions in the [Cloud TPU Tools: Input Pipeline Analyzer](https://docs.cloud.google.com/tpu/docs/cloud-tpu-tools#input_pipeline_analyzer) for viewing the input pipeline analysis in TensorBoard:

![image](https://docs.cloud.google.com/static/tpu/docs/images/cloudtputools--97sbwhorfww.png)

The input pipeline analysis page displays a clear summary which shows if your model is bottlenecked by input processing. The same page also shows per-op execution time, which lets you pinpoint problematic ops.

**How to Mitigate**

There are several possible mitigations when loading data with the `Dataset` API:

  1. Store your data as a collection of `tf.train.Example` structures in `TFRecord` files, and load them with `TFRecordDataset`. See the [Dataset API tutorial](https://www.tensorflow.org/programmers_guide/datasets) or the [ResNet tutorial](https://docs.cloud.google.com/tpu/docs/tutorials/resnet) for examples.
  2. Use `dataset.cache()` or `dataset.prefetch()` to buffer the input data. This prevents sporadic slowdowns in file access from creating a bottleneck.
  3. Specify the `num_parallel_calls` parameter of the `dataset.map()` function to enable multi-threaded `map()` ops. A heuristic for the value of `num_parallel_calls` is to use the number of available CPU cores.
  4. Perform expensive data pre-processing offline as a one time cost, rather than incurring the cost through every epoch of every training.



All input processing is performed on CPUs located on the TPU server, _not_ on the local machine, so the speed of the local machine is not a factor.

### Slow step times and low MXU utilization

**Description of Performance Issue**

The Cloud TPU can perform matrix multiplications and convolutions at incredibly high speeds. The majority of other TensorFlow ops do have efficient implementations on the TPU, but these are not the TPU's primary strength relative to other hardware. Therefore, a model should be dominated by matrix multiplications or convolutions to fully take advantage of the TPU.

**How to Know if Your Model is Affected**

The symptoms you will see in this case are slow step times coupled with low MXU utilization shown when you [profile the performance.](https://docs.cloud.google.com/tpu/docs/cloud-tpu-tools#op_profile)

**How to Mitigate**

Try to reduce the number of ops that are not matrix multiplications. After reducing the number of matrix multiplications, re-benchmark to see if performance is acceptable on TPUs.

### Excessive tensor padding

**Description of Performance Issue**

The TPU pads tensors in memory so that the TPU can use its computational units efficiently. The padding can increase usage of both memory and memory bandwidth. See the section on tensor padding for help understanding and fixing tensor padding issues.

### Slow throughput and low memory usage

**Description of Performance Issue**

As a general rule, using larger batch sizes results in greater training speed on the TPU, in terms of samples/second.

**How to Know if Your Model is Affected**

The batch size of any model should always be at least 64 (8 per TPU core), since the TPU always pads the tensors to this size. The ideal batch size when training on the TPU is 1024 (128 per TPU core), since this eliminates inefficiencies related to memory transfer and padding.

**How to Mitigate**

Best practice is to use the largest batch size which fits in to memory and is a multiple of 64. The easiest way to achieve this is to start with 1024, and if this causes an out-of-memory error then try reducing the batch size until the model runs successfully. Changing the batch size of a model may require adjusting other hyperparameters to achieve the same model accuracy, such as the the learning rate, but this must be evaluated on a case-by-case basis.

### Layer sizes too small

**Description of Performance Issue**

Even when a model is dominated by matrix multiplications or convolutions, the TPU may not run at full efficiency if the input tensors are small. When compared to other hardware, the TPU runs most efficiently when both the batch size and layer sizes are large (for example, dimension >= 512).

**How to Know if Your Model is Affected**

As a general rule, layer sizes smaller than 128 achieve poor efficiency on the TPU, since 128 is the built-in dimension of the TPU matrix multiplication unit. For fully-connected layers, a minimum hidden size of 512 is recommended in order to achieve high efficiency. Note that convolutional layers typically don't need to be as large as fully connected layers to achieve an equal efficiency level.

**How to Mitigate**

If the primary motivation for small layer sizes in your model is training speed, re-benchmark your models with larger layers on the TPU. For example, increasing the output size of a layer from 256 to 512 may only increase the training time by 20% even though the model is performing 2x the computations.

### Op-level model profiling

It is often useful to measure op-level execution time and memory usage in order to identify performance bottlenecks. For instructions on how to do this,   
see the guide [Cloud TPU Tools: Trace Viewer](https://docs.cloud.google.com/tpu/docs/cloud-tpu-tools#trace_viewer).

## Debugging drops in model accuracy

One of the goals of the Cloud TPU ecosystem is that any model that is being trained on a CPU or GPU achieves a very similar accuracy when it is trained on the TPU, with perhaps minor adjustments to hyperparameters like the batch size and learning rate. Occasionally, however, users can observe a degradation in accuracy when training models on the TPU. Debugging such issues can be extremely frustrating due to the random nature of neural network training. This section provides guidance on how to pinpoint the root cause of any drops in model accuracy when porting a model to the TPU.

### Understanding data sharding (data parallelism)

One of TensorFlow's primary goals is that each op should produce nearly identical results whether it is executed on the CPU, GPU, or TPU. There are certain exceptions to this, such as random ops. In general, if you find any significant difference between the output of non-random ops on the TPU and CPU, [report it as a bug](https://docs.cloud.google.com/tpu/docs/getting-support#file_bugs_or_feature_requests).

However, for the training pipeline _as a whole_ , there is a significant difference between training on the CPU/GPU and TPU. When training on a TPU, TensorFlow performs [_data sharding_ ,](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) Each Cloud TPU contains 8 TPU cores which operate as independent processing units. For each step in the training, each TPU core receives a batch of data, computes the weight gradients, exchanges the gradients with the other TPU cores, and then computes the weight update. By default, the loss is averaged across the cores, but it can be summed by changing the parameter of `CrossShardOptimizer`.

If the total loss of the model can be computed as the average (or sum) of independent per-sample losses, then this procedure is mathematically equivalent to training on a single large batch.

The most common op which is _not_ independent per-sample is [batch normalization](https://arxiv.org/abs/1502.03167), which runs over each per-core batch separately. For example, if the total batch size is 128, then the per-core batch size is 16, and each of the 8 cores performs batch normalization over its own 16 samples. In some cases, performing batch normalization over small batches (for example, less than 32) has been found to degrade accuracy. In the ideal scenario, total batch size should be large (for example, 256 to 1024). If a batch size is too large to fit into memory, the effect of sharding must be evaluated on a case-by-case basis.

### Debugging multi-core TPU training

If your model _does_ achieve the same loss on the CPU and single-core TPU, then the issue is likely one of the following:

(a) The degradation is due to the natural random variance when training neural models with different initializations.

(b) The degradation is due to an issue related to data sharding on the TPU.

To determine whether (a) is the issue, re-train the full model on the CPU/GPU and multi-core TPU using the same weight initialization.

If you are confident that the drop in accuracy is statistically significant, then the most likely issues related to data sharding are:

  1. If your model uses batch normalization, a total batch size less than 256 (for example, less than 32 per core) might reduce accuracy.
  2. Batch-wise loss functions are affected by sharding. Such loss functions are typically quite specialized. For example, [Karras et al. 2017](http://research.nvidia.com/publication/2017-10_Progressive-Growing-of) uses a batch discriminator when training a generative adversarial network.



## `gcloud` setup troubleshooting

Problem
    `gcloud components update` displays the following error message:
    
    
    ERROR: (gcloud.components.update)
    You cannot perform this action because the Cloud SDK component manager is
    disabled for this installation.
    

Solution
    

To use the Google Cloud CLI, you need to use an installation that is not managed through a package manager. 

  1. Run the following command to remove the current gcloud CLI installation:
         
         sudo apt-get remove google-cloud-sdk

  2. Follow the instructions to [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). 



Problem
    

`gcloud compute tpus tpu-vm ssh TPU_NAME --zone ZONE` command displays the following error message:
    
    
    Waiting for SSH key to propagate.
    ssh: connect to host 34.91.136.59 port 22: Connection timed out
    ssh: connect to host 34.91.136.59 port 22: Connection timed out
    ssh: connect to host 34.91.136.59 port 22: Connection timed out
    ERROR: (gcloud.compute.tpus.tpu-vm.ssh) Could not SSH into the instance.  It is possible that your SSH key has not propagated to the instance yet. Try running this command again.  If you still cannot connect, verify that the firewall and instance are set to accept ssh traffic.
    

Solution
    

Something may be wrong with the SSH key propagation. Try moving the automatically-generated keys to a backup location to force `gcloud` to recreate them:
    
    
    mv ~/.ssh/google_compute_engine ~/.ssh/old-google_compute_engine
    mv ~/.ssh/google_compute_engine.pub ~/.ssh/old-google_compute_engine.pub

## Debug logs

The supported Cloud TPU frameworks, JAX, PyTorch, and TensorFlow access TPUs using a shared library called `libtpu` that is present on every TPU VM. This library includes the XLA compiler used to compile TPU programs, the TPU runtime used to run compiled programs, and the TPU driver used by the runtime for low-level access to the TPU.

The `libtpu` library logs information that can be useful for debugging. By default, these logs are written to `/tmp/tpu_logs` on each Cloud TPU VM. The following environment variables can be set before you begin training to modify the logging behavior:

TPU_LOG_DIR: the directory to which logs are written
    The directory location defaults to `/tmp/tpu_logs`. The directory is created if it does not already exist, but no parent directories are created. If there is an error finding or creating the specified directory, a message is printed to stderr, but it won't halt the program and logging is disabled. Set the directory name to "disabled" to disable logging to disk altogether.
TPU_MIN_LOG_LEVEL: the minimum severity that will be logged to disk
    The choices are 0 (INFO), 1 (WARNING), 2 (ERROR), and 3 (FATAL). The default is 0.
TPU_STDERR_LOG_LEVEL: the minimum severity that will be logged to stderr, in addition to disk, if applicable
    The choices are the same as TPU_MIN_LOG_LEVEL. The default is 3.
TPU_MAX_LOG_SIZE_MB: the maximum size in megabytes of each log file
    A new log file will automatically be started when the previous one reaches roughly this size. Defaults to 1024.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
