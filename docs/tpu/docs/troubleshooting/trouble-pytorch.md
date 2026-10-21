---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-pytorch/
title: Troubleshooting PyTorch - TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:00.522012+00:00
---

# Troubleshooting PyTorch - TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-pytorch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting PyTorch - TPU

**Deprecated:** This page applies to PyTorch/XLA, which is deprecated and replaced by [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu). The PyTorch/XLA repo will be archived on November 15, 2026. Start new PyTorch workloads with TorchTPU and migrate existing PyTorch/XLA workloads to TorchTPU. 

This guide provides troubleshooting information to help you identify and resolve problems you might encounter while training PyTorch models on Cloud TPU. For a more general guide to getting started with Cloud TPU, see [Quickstart: Create a TPU instance](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance).

**Note:** If you aren't able to resolve your issue using this guide, see [Getting Support](https://docs.cloud.google.com/tpu/docs/getting-support) for further assistance.

## Troubleshooting slow training performance

If your model trains slowly, [generate and review a metrics report.](https://pytorch.org/xla/release/r2.6/learn/troubleshoot.html#get-a-metrics-report)

To automatically analyze the metrics report and provide a summary, run your workload with PT_XLA_DEBUG=1.

For more information about issues that might cause your model to train slowly, see [Known performance caveats](https://pytorch.org/xla/release/r2.6/learn/troubleshoot.html#known-performance-caveats).

## Performance profiling

To profile your workload in-depth to discover bottlenecks, review these resources:

  * [PyTorch/XLA performance profiling](https://cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm)
  * [Sample MNIST training script with profiling](https://github.com/pytorch/xla/blob/master/test/test_profile_mp_mnist.py)



## More debugging tools

You can specify [environment variables](https://pytorch.org/xla/release/r2.6/learn/troubleshoot.html#environment-variables) to control the behavior of the PyTorch/XLA software stack.

If you encounter an unexpected bug and need help, [file a GitHub issue](https://github.com/pytorch/xla).

## Managing XLA tensors

[XLA tensor Quirks](https://pytorch.org/xla/release/r2.6/learn/troubleshoot.html#xla-tensor-quirks) describes what you should and shouldn't do when working with XLA tensors and shared weights.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
