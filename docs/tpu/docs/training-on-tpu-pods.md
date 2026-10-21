---
url: https://docs.cloud.google.com/tpu/docs/training-on-tpu-pods/
title: Training on TPU slices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:03.365423+00:00
---

# Training on TPU slices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/training-on-tpu-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Training on TPU slices 

TPUs are designed to be scaled out to a TPU Pod. A TPU Pod is a collection of TPU devices connected by dedicated high-speed network interfaces. A TPU Pod lets you distribute the processing load across multiple TPUs. Each TPU board is connected to a high-performance CPU-based host machine for things like loading and preprocessing data. To take full advantage of larger numbers of TPUs, you must tune several training task parameters.

The following sections explain some common issues, changes you need to make in your models, and best practices to reduce or avoid Pod failures.

## Scaling batch size and train steps

To achieve linear scaling on larger TPU types, keep the per-core batch size the same.

For example, if you use a batch size of 1024 on a v6e-8, use a batch size of 4096 (4 * 1024) on a v6e-32. This fully utilizes the TPU hardware. You can use smaller batch sizes, but your training won't scale linearly if you do so.

Some models include a `train_steps` flag where one step corresponds to processing a single batch of data. When you increase the batch size, scale down the number of training steps so that the total number of training examples remains the same.

For example, if you have a batch size of 1000 for 100 steps, 100,000 examples are processed during training. If you now have 4 workers and an effective batch size of 4000, you would have to adjust the number of steps to 25 to process that same 100,000 examples. If your model uses an `epochs` flag, you don't need to scale the number of steps.

Larger batch sizes can change convergence behavior of the model, so you might also tune some hyperparameters, like learning rate.

## Using regional Cloud Storage buckets in the same region as the TPU Pod

In general, the best practice for TPU training is to always use resources in the same region. Resource region is particularly important when using TPU Pods because the data transfer rates are higher when your Cloud Storage bucket and TPU are in the same region.

Ensure you are using a regional Cloud Storage bucket in the same region as the TPU for training datasets and checkpoints.

## Workflow best practices for development on TPU Pods

When developing a new TPU workload, it is often optimal to begin development on the smallest TPUs and progressively iterate to larger TPU sizes. Start by using a small TPU version (for example, v6e-8).

  * Test your workload for expected behavior
  * Test and validate performance using the performance tools



Once your workload is functional and reaches your performance targets, scale up to a larger TPU type such as a v6e-32. Gradually and iteratively increase the TPU size while validating scalability (functionality and performance) until you reach the TPU size that you want.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
