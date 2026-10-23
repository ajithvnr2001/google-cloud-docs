---
url: https://docs.cloud.google.com/tpu/docs/runtimes/
title: TPU software versions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:17.121439+00:00
---

# TPU software versions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/runtimes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU software versions

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document provides guidance on selecting the appropriate TPU software version when you create Cloud TPUs.

When you create TPU resources, you specify the software version, also called runtime version, which refers to the software environment that is pre-installed on your TPU VM. This includes the Ubuntu operating system, Docker, and other software required to run your code on TPUs.

If you're using the Google Cloud CLI, you specify the TPU software version using the `--version` or `--runtime-version` parameter. If you're using the Google Cloud console, you select a TPU software version from the **TPU software version** list.

## PyTorch and JAX

Use the following common TPU software versions for PyTorch and JAX, then install the framework you want to use.

TPU version | TPU software version  
---|---  
Trillium (v6e) | v2-alpha-tpuv6e  
v5p | v2-alpha-tpuv5  
v5e | v2-alpha-tpuv5-lite  
v4 and older | tpu-ubuntu2204-base  
  
For more information about installation and getting started with JAX or PyTorch, see [Run a calculation on a Cloud TPU VM using JAX](https://docs.cloud.google.com/tpu/docs/run-calculation-jax) and [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).

## TensorFlow

**Note:** TensorFlow is not supported on Ironwood (TPU7x).

TPU software versions for TensorFlow follow a specific naming convention:

`tpu-vm-tf-x.y.z[-{pod}][-{device_api}]`

  * `x.y.z`: Represents the major, minor, and patch versions of TensorFlow.
  * `-pod` (optional): Indicates that you're using a multi-host TPU slice.
  * `-{device_api}` (optional): Specifies the device API, for example, `-pjrt` (if you're using the [PJRT API](https://docs.cloud.google.com/tpu/docs/runtimes#pjrt-support)).



See the following sections for more information on how to specify a TPU software version.

There are TPU software versions specific to each version of TensorFlow. The following table shows the supported TensorFlow versions and associated libtpu versions:

TensorFlow version | libtpu.so version  
---|---  
[2.18.0](https://pypi.org/project/tensorflow-tpu/2.18.0/#files) | [1.12.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.12.0/libtpu.so)  
[2.17.1](https://pypi.org/project/tensorflow-tpu/2.17.1/#files) | [1.11.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.11.1/libtpu.so)  
[2.17.0](https://pypi.org/project/tensorflow-tpu/2.17.0/#files) | [1.11.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.11.0/libtpu.so)  
[2.16.2](https://pypi.org/project/tensorflow-tpu/2.16.2/#files) | [1.10.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.10.1/libtpu.so)  
[2.16.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.16.1/tensorflow-2.16.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.10.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.10.1/libtpu.so)  
[2.15.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.15.0/tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.9.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.9.0/libtpu.so)  
[2.15.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.15.0/tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.9.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.9.0/libtpu.so)  
[2.14.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.14.1/tensorflow-2.14.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.8.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.8.1/libtpu.so)  
[2.14.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.14.0/tensorflow-2.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.8.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.8.0/libtpu.so)  
[2.13.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.13.1/tensorflow-2.13.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.7.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.7.1/libtpu.so)  
[2.13.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.13.0/tensorflow-2.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.7.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.7.0/libtpu.so)  
[2.12.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.12.1/tensorflow-2.12.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.6.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.6.1/libtpu.so)  
[2.12.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.12.0/tensorflow-2.12.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.6.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.6.0/libtpu.so)  
[2.11.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.11.1/tensorflow-2.11.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.5.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.5.1/libtpu.so)  
[2.11.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.11.0/tensorflow-2.11.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.5.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.5.0/libtpu.so)  
[2.10.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.10.1/tensorflow-2.10.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.4.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.4.1/libtpu.so)  
[2.10.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.10.0/tensorflow-2.10.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.4.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.4.0/libtpu.so)  
[2.9.3](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.9.3/tensorflow-2.9.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.3.2](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.3.2/libtpu.so)  
[2.9.1](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.9.1/tensorflow-2.9.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.3.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.3.0/libtpu.so)  
[2.8.3](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.8.3/tensorflow-2.8.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.2.3](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.2.3/libtpu.so)  
[2.8.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.8.0/tensorflow-2.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.2.0](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.2.0/libtpu.so)  
[2.7.3](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/tensorflow/tf-2.7.3/tensorflow-2.7.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl) | [1.1.2](https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/libtpu/1.1.2/libtpu.so)  
  
For more information about TensorFlow patch versions, see [Supported TensorFlow patch versions](https://docs.cloud.google.com/tpu/docs/supported-patches).

### TPU v6e, v5p, and v5e

TPU v6e, v5e, and v5p support TensorFlow 2.15.0 and newer. You specify the TPU software version using the form: `tpu-vm-tf-x.y.z-{pod}-pjrt` where `x` is the major TensorFlow version, `y` is the minor version, and `z` is the TensorFlow patch version. Add `pod` after the TensorFlow version if you are using a multi-host TPU. For example, if you are using TensorFlow 2.16.0 on a multi-host TPU, use the `tpu-vm-tf-2.16.0-pod-pjrt` TPU software version. For other versions of TensorFlow, replace `2.16.0` with the major and patch versions of TensorFlow you are using. If you are using a single-host TPU, omit `pod`.

### TPU v4

If you're using TPU v4 and TensorFlow 2.10.1 or newer, follow the instructions for TPU v2 and v3. If you're using TensorFlow 2.10.0 or earlier, use a v4-specific TPU software version:

TensorFlow version | TPU software version  
---|---  
2.10.0 | tpu-vm-tf-2.10.0-v4  
tpu-vm-tf-2.10.0-pod-v4  
2.9.3 | tpu-vm-tf-2.9.3-v4  
tpu-vm-tf-2.9.3-pod-v4  
2.9.2 | tpu-vm-tf-2.9.2-v4  
tpu-vm-tf-2.9.2-pod-v4  
2.9.1 | tpu-vm-tf-2.9.1-v4  
tpu-vm-tf-2.9.1-pod-v4  
  
### TPU v2 and v3

If you are using TPU v2 or v3, use the TPU software version that matches the version of TensorFlow you are using. For example if you are using TensorFlow 2.14.1, use the `tpu-vm-tf-2.14.1` TPU software version. For other versions of TensorFlow, replace `2.14.1` with the TensorFlow version you are using. If you are using a multi-host TPU, append pod to the end of the TPU software version, for example `tpu-vm-tf-2.14.1-pod`.

Beginning with TensorFlow 2.15.0, you must also specify a device API as part of the software version name. For example, if you are using TensorFlow 2.16.1 with the PJRT API, use the TPU software version `tpu-vm-tf-2.16.1-pjrt`. If you are using the stream executor API with the same version of TensorFlow, use the `tpu-vm-tf-2.16.1-se` TPU software version. TensorFlow versions older than 2.15.0 only support stream executor.

### TensorFlow PJRT support

Beginning with TensorFlow 2.15.0, you can use the PJRT interface for TensorFlow on TPU. PJRT features automatic device memory defragmentation and simplifies the integration of hardware with frameworks. For more information about PJRT, see [PJRT: Simplifying ML Hardware and Framework Integration](https://opensource.googleblog.com/2023/05/pjrt-simplifying-ml-hardware-and-framework-integration.html).

**Important:** TPU v5e and future TPU generations only support PJRT. Not all features of TPU v2, v3, and v4 have been migrated to the PJRT API. The following table describes which features are supported on PJRT or stream executor.Accelerator | Feature | PJRT support | Stream executor support  
---|---|---|---  
TPU v2 - v4 | Dense compute (no TPU embedding API) | Yes | Yes  
TPU v2 - v4 | Dense compute API + TPU embedding API | No | Yes  
TPU v2 - v4 | tf.summary/tf.print with soft device placement | No | Yes  
TPU v5e | Dense compute (no TPU embedding API) | Yes | No  
TPU v5e | TPU embedding API | N/A | No  
TPU v5p | Dense compute (no TPU embedding API) | Yes | No  
TPU v5p | TPU embedding API | Yes | No  
  
## What's next

  * See [TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) to learn more about TPU architecture.
  * See [When to use TPUs](https://docs.cloud.google.com/tpu/docs/tpus#when_to_use_tpus) to learn about the types of models that are well suited to Cloud TPU.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
