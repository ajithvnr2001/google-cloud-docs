---
url: https://docs.cloud.google.com/tpu/docs/bfloat16/
title: Improve your model's performance with bfloat16 \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:25.511253+00:00
---

# Improve your model's performance with bfloat16  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/bfloat16/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Improve your model's performance with bfloat16

By default, TPUs perform matrix multiplication operations with [`bfloat16`](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format) values and accumulations with IEEE [`float32`](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) values. Using reduced-precision floating point numbers decreases time to convergence without losing accuracy.

The dynamic range of `bfloat16` and `float32` are equivalent. However, `bfloat16` uses half of the memory space. For more information about `bfloat16` performance, see [A Study of BFLOAT16 for Deep Learning Training](https://arxiv.org/abs/1905.12322).

## Use bfloat16 explicitly

While automatic format conversion in TPUs lets you avoid thinking about numerical precision, you can achieve performance improvements by explicitly casting values to `bfloat16`. There are two reasons to explicitly cast values to `bfloat16`:

  1. Storing values in `bfloat16` format saves on-chip memory, enabling Cloud TPUs to train larger models or use larger batch sizes.

  2. Some operations are memory-bandwidth-bound, which means the amount of time it takes to load data from memory can slow down the overall time spent performing the computation. Storing operands and outputs of those operations in `bfloat16` format reduces the amount of data that must be transferred, improving overall speed.




To get started, we recommend getting some experience with one of the [Cloud TPU reference models](https://docs.cloud.google.com/tpu/docs/tutorials/supported-models). After that, the [profiling tools guide](https://docs.cloud.google.com/tpu/docs/profile-tpu-vm), and [troubleshooting guide](https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshooting) provide in-depth technical information to help you create and optimize machine learning models on your own.

### Format conversion details

The format conversion from `float32` to `bfloat16` is automatically inserted by the XLA compiler. On TPU, the rounding scheme in the conversion is [round to nearest even](https://en.wikipedia.org/wiki/IEEE_754#Roundings_to_nearest) and overflow to `inf`. Also, the `bfloat16` on Cloud TPU does not support subnormals, so all subnormals are flushed to zero during the conversion. Special values, such as `NaN` and `inf`, are preserved in the conversion.

The format conversion from `bfloat16` to `float32` is also automatically inserted by the XLA compiler. Since `float32` can represent all exact values in `bfloat16`, the conversion pads 16 zeros in the mantissa bits. Special values are preserved in the conversion.

Checkpoints obtained from a model trained on Cloud TPUs can be deployed on other hardware platforms (for example, inference or fine-tuning on CPUs or GPUs) without extensive manual conversions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
