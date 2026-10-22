---
url: https://docs.cloud.google.com/tpu/docs/release-notes/
title: Cloud TPU release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:09.032092+00:00
---

# Cloud TPU release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Resources ](https://docs.cloud.google.com/tpu/docs/resources)



Send feedback 

#  Cloud TPU release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud TPU. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/tpu-release-notes.xml) directly. 

## June 01, 2026

Feature

**Generally available** : Compute Engine supports Google's custom-developed accelerator Tensor Processing Unit (TPU), providing a converged experience across AI accelerators on Google Cloud. You can use the Compute Engine instance API and managed instance group (MIG) API to create and manage TPU VMs. You can perform standard VM configurations such as using a custom OS or configure boot disk size. Compute Engine APIs support the creation and management of TPU slices across all consumption options, enabling small-scale experimentation and large-scale training and inference workloads.

For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine).

## April 27, 2026

Feature

**Generally available** : Cloud TPU now offers TPU availability in AI zones. To learn more, see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

## March 31, 2026

Feature

**Generally available** : TPU7x is generally available (GA). TPU7x is the first release within the Ironwood family, Google Cloud's seventh generation TPU. TPU7x supports large-scale AI training and inference, providing performance and cost-effectiveness for demanding workloads such as large language (LLMs), mixture of experts (MoEs), and diffusion models. For more information, see the [TPU7x (Ironwood) documentation](https://docs.cloud.google.com/tpu/docs/tpu7x).

## November 24, 2025

Feature

**Preview** : TPU7x is available in Preview. TPU7x is the first release within the Ironwood family, Google Cloud's seventh generation TPU. TPU7x supports large-scale AI training and inference, providing performance and cost-effectiveness for demanding workloads such as large language models (LLMs), mixture of experts (MoEs), and diffusion models. For more information, see the [TPU7x (Ironwood) documentation](https://docs.cloud.google.com/tpu/docs/tpu7x).

## May 22, 2025

Feature

**Public preview** : You can request Cloud TPUs using future reservations in calendar mode. This mode, powered by the [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), lets you check TPU availability up to 120 days in advance and request capacity based on your schedule. You can use calendar mode to reserve TPUs for 1 to 90 days. Requesting a short-term reservation with calendar mode is a good fit for training and experimentation workloads that require precise start times and have a defined duration. For more information, see [Request a short-term reservation using calendar mode](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation).

Feature

**Public preview** : You can enable reservation sharing for Cloud TPU. This feature lets you share a reservation across multiple projects. You can also share a reservation with Vertex AI for training or serving workloads. For more information, see [Share a Cloud TPU reservation](https://docs.cloud.google.com/tpu/docs/share-reservation).

## March 31, 2025

Feature

[Flex-start for Cloud TPU](https://docs.cloud.google.com/tpu/docs/request-using-flex-start), powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), is available in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Flex-start is a flexible and cost-effective consumption option for AI workloads. Flex-start enables you to dynamically provision TPUs for up to 7 days using the queued resources API, without long-term reservations. This option is ideal for quick experimentation, small-scale testing, dynamic inference provisioning, and model fine-tuning. For more information about Flex-start for Cloud TPU, see [Request Cloud TPUs using Flex-start](https://docs.cloud.google.com/tpu/docs/request-using-flex-start).

## December 16, 2024

Announcement

This Release Note announces General Availability of Trillium AKA v6e. Trillium is the 6th generation and latest Cloud TPU. It is fully integrated with our AI Hypercomputer architecture to deliver compelling value to our Google Cloud Platform AI customers. 

We used Trillium TPUs to train the new Gemini 2.0, Google's most capable AI model yet, and now enterprises and startups alike can take advantage of the same powerful, efficient, and sustainable infrastructure. Today, Trillium is generally available for Google Cloud customers and this week we will be delivering our first large tranches of Trillium capacity to some of our biggest Google Cloud Platform customers.

Here are some of the key improvements that Trillium delivers over the prior generations, v5e and v5p:

  * Over 4x improvement in training performance.

  * Up to 3x increase in inference throughput.

  * A 67% increase in energy efficiency.

  * An impressive 4.7x increase in peak compute performance per chip.

  * Double the High Bandwidth Memory (HBM) capacity.

  * Double the Interchip Interconnect (ICI) bandwidth.

  * 100,000 Trillium chips per Jupiter network fabric with 13 Petabits/sec of bisection bandwidth, capable of scaling a single distributed training job to hundreds of thousands of accelerators. 

  * Trillium provides up to 2.1x increase in performance per dollar over Cloud TPU v5e and up to 2.5x increase in performance per dollar over Cloud TPU v5p in training dense LLMs like Llama2-70b and Llama3.1-405b.

  * GKE integration enables seamless AI workload orchestration using Google Compute Engine MIGs including XPK for faster iterative development.

  * Multislice training with Trillium scales from one to hundreds of thousands of chips across pods using DCN.

  * Training and serving fungibility enables use of same Cloud TPU quota for both training and inference.

  * Support for collection scheduling with collection SLOs being defended.

  * Full-host VM support to enable inference support for larger models (70B+ parameters).

  * Official Libtpu releases that guarantees stability across all three frameworks (Jax/Pytorch-XLA/Tensorflow).




These enhancements enable Trillium to excel across a wide range of AI workloads, including:

  * Scaling AI training workloads like LLMs including dense and Mixture of Experts (MoE) models

  * Inference performance and collection scheduling

  * Embedding-intensive models acceleration

  * Delivering training and inference price-performance




## November 01, 2024

Feature

You can now request Cloud TPUs as queued resources in the Google Cloud Console. Queuing your request for TPU resources can help alleviate stockout issues. If the resources you request are not immediately available, your request is added to a queue until the request succeeds or you delete it. You can also specify a time range in which you want to fulfill the resource request. For more information, see [Manage queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).

Feature

Creating a Multislice TPU environment is now available in the Google Cloud Console. You can use Multislice to run training jobs using multiple TPU slices within a single Pod or on slices in multiple Pods. You must use a queued resource request to create a Multislice environment. For more information, see [Cloud TPU Multislice overview](https://docs.cloud.google.com/tpu/docs/multislice-introduction).

## March 11, 2024

Change

Cloud TPU now supports TensorFlow 2.16.1. For more information see the [TensorFlow 2.16.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.16.1).

## December 04, 2023

Change

Cloud TPU now supports TensorFlow 2.14.1. For more information see the [TensorFlow 2.14.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.14.1).

## November 13, 2023

Change

Cloud TPU now supports TensorFlow 2.15.0, which adds support for PJRT. For more information see the [TensorFlow 2.15.0 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.15.0).

## October 05, 2023

Change

Cloud TPU now supports TensorFlow 2.13.1. For more information see the [TensorFlow 2.13.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.13.1).

## September 27, 2023

Change

Cloud TPU now supports TensorFlow 2.14.0. For more information see the [TensorFlow 2.14.0 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.14.0).

## August 29, 2023

Announcement

You can now create Cloud Tensor Processing Unit (TPU) nodes in Google Kubernetes Engine (GKE) to run AI workloads, from training to inference models. GKE manages your cluster by automating TPU resource provisioning, scaling, scheduling, repairing, and upgrading. GKE provides TPU infrastructure metrics in Cloud Monitoring, TPU logs, and error reports for better visibility and monitoring of TPU node pools in GKE clusters. TPUs are available with GKE Standard clusters. GKE supports TPU v4 in version 1.26.1.gke-1500 and later, and supports TPU v5e in version 1.27.2-gke.1500 and later. To learn more, see [TPUs in GKE introduction](https://docs.cloud.google.com/tpu/docs/tpus-in-gke).

## July 21, 2023

Change

Cloud TPU now supports TensorFlow 2.12.1. For more information see the [TensorFlow 2.12.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.12.1).

## July 10, 2023

Change

Cloud TPU now supports TensorFlow 2.13.0. For more information see the [TensorFlow 2.13.0 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.13.0).

## June 07, 2023

Change

You can now view historical logs of maintenance events on your TPU in [system event audit logs](https://cloud.google.com/tpu/docs/audit-logs#audited_operations). For additional information see the [maintenance events documentation](https://docs.cloud.google.com/tpu/docs/maintenance-events).

## March 31, 2023

Change

Cloud TPU now supports Tensorflow 2.11.1. For more information see the [TensorFlow 2.11.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.11.1).

## March 27, 2023

Change

Cloud TPU now supports Tensorflow 2.12.0. For more information see the [TensorFlow 2.12 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.12.0).

## March 24, 2023

Change

Cloud TPUs now support the [PyTorch 2.0 release](https://github.com/pytorch/pytorch/releases), via PyTorch/XLA integration. On top of the underlying improvements and bug fixes in PyTorch's 2.0 release, this release introduces several features, and PyTorch/XLA specific bug fixes.

### **Beta Features**

#### PJRT runtime

  * Checkout our newest [document](https://github.com/pytorch/xla/blob/r2.0/docs/pjrt.md); PjRt is the default runtime in 2.0.
  * New Implementation of `xm.rendezvous` with XLA collective communication which scales better ([#4181](https://github.com/pytorch/xla/pull/4181))
  * New PJRT TPU backend through the C-API ([#4077](https://github.com/pytorch/xla/pull/4077))
  * Use PJRT to default if no runtime is configured ([#4599](https://github.com/pytorch/xla/pull/4599))
  * Experimental support for torch.distributed and DDP on TPU v2 and v3 (`[#4520](https://github.com/pytorch/xla/pull/4520)`)



#### FSDP

  * Add `auto_wrap_policy` into XLA FSDP for automatic wrapping ([#4318](https://github.com/pytorch/xla/pull/4318))



### **Stable Features**

#### Lazy Tensor Core Migration

  * Migration is completed, checkout this [dev discussion](https://dev-discuss.pytorch.org/t/pytorch-xla-2022-q4-dev-update/961) for more detail.
  * Naively inherits LazyTensor ([#4271](https://github.com/pytorch/xla/pull/4271))
  * Adopt even more LazyTensor interfaces ([#4317](https://github.com/pytorch/xla/pull/4317))
  * Introduce XLAGraphExecutor ([#4270](https://github.com/pytorch/xla/pull/4270))
  * Inherits LazyGraphExecutor ([#4296](https://github.com/pytorch/xla/pull/4296))
  * Adopt more LazyGraphExecutor virtual interfaces ([#4314](https://github.com/pytorch/xla/pull/4314))
  * Rollback to use `xla::Shape` instead of `torch::lazy::Shape` ([#4111](https://github.com/pytorch/xla/pull/4111))
  * Use TORCH_LAZY_COUNTER/METRIC ([#4208](https://github.com/pytorch/xla/pull/4208))



#### Improvements & Additions

  * Add an option to increase the worker thread efficiency for data loading ([#4727](https://github.com/pytorch/xla/pull/4727))
  * Improve numerical stability of torch.sigmoid ([#4311](https://github.com/pytorch/xla/pull/4311))
  * Add an api to clear counter and metrics ([#4109](https://github.com/pytorch/xla/pull/4109))
  * Add `met.short_metrics_report` to display more concise metrics report ([#4148](https://github.com/pytorch/xla/pull/4148))
  * Document environment variables ([#4273](https://github.com/pytorch/xla/pull/4273))
  * Op Lowering 
    * `_linalg_svd` ([#4537](https://github.com/pytorch/xla/pull/4537))
    * `Upsample_bilinear2d` with scale ([#4464](https://github.com/pytorch/xla/pull/4464))



### **Experimental Features**

#### TorchDynamo (`torch.compile`) support

  * Checkout our newest [doc](https://github.com/pytorch/xla/blob/r2.0/docs/dynamo.md).
  * Dynamo bridge python binding ([#4119](https://github.com/pytorch/xla/pull/4119))
  * Dynamo bridge backend implementation ([#4523](https://github.com/pytorch/xla/pull/4523))
  * Training optimization: make execution async ([#4425](https://github.com/pytorch/xla/pull/4425))
  * Training optimization: reduce graph execution per step ([#4523](https://github.com/pytorch/xla/pull/4523))



#### PyTorch/XLA GSPMD on single host

  * Preserve parameter sharding with sharded data placeholder ([#4721)](https://github.com/pytorch/xla/pull/4721)
  * Transfer shards from server to host ([#4508](https://github.com/pytorch/xla/pull/4508))
  * Store the sharding annotation within XLATensor(#[4390](https://github.com/pytorch/xla/pull/4390))
  * Use d2d replication for more efficient input sharding ([#4336](https://github.com/pytorch/xla/pull/4336))
  * Mesh to support custom device order. ([#4162](https://github.com/pytorch/xla/pull/4162))
  * Introduce virtual SPMD device to avoid unpartitioned data transfer ([#4091](https://github.com/pytorch/xla/pull/4091))



### **Ongoing development**

  * Ongoing Dynamic Shape implementation 
    * Implement missing `XLASymNodeImpl::Sub` ([#4551](https://github.com/pytorch/xla/pull/4551))
    * Make `empty_symint` support dynamism. ([#4550](https://github.com/pytorch/xla/pull/4550))
    * Add dynamic shape support to `SigmoidBackward` ([#4322](https://github.com/pytorch/xla/pull/4322))
    * Add a forward pass NN model with dynamism test ([#4256](https://github.com/pytorch/xla/pull/4256)) 
  * Ongoing SPMD multi host execution ([#4573](https://github.com/pytorch/xla/pull/4573))



### **Bug fixes & improvements**

  * Support int as index type ([#4602](https://github.com/pytorch/xla/pull/4602))
  * Only alias inputs and outputs when `force_ltc_sync == True` ([#4575](https://github.com/pytorch/xla/pull/4575))
  * Fix race condition between execution and buffer tear down on GPU when using `bfc_allocator` (`[#4542](https://github.com/pytorch/xla/pull/4542)`)
  * Release the GIL during TransferFromServer ([#4504](https://github.com/pytorch/xla/pull/4504))
  * Fix type annotations in FSDP ([#4371](https://github.com/pytorch/xla/pull/4371))



## December 19, 2022

Change

Cloud TPU now supports TensorFlow patches: [2.8.4](https://pypi.org/project/tensorflow/2.8.4/), [2.9.3](https://pypi.org/project/tensorflow/2.9.3/), and [2.10.1](https://pypi.org/project/tensorflow/2.10.1/). See the TensorFlow release notes for details:

  * [2.8.4 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.8.4)
  * [2.9.3 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.9.3)
  * [2.10.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.10.1)



## December 01, 2022

Change

Cloud TPU now supports Tensorflow 2.11.0. For more information see [TensorFlow 2.11 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.11.0).

## September 13, 2022

Change

Cloud TPU now supports Tensorflow 2.10.0. For more information see [TensorFlow 2.10 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.10.0).

## June 24, 2022

Change

Cloud TPU now supports [TensorFlow 2.6.5](https://pypi.org/project/tensorflow/2.6.5/) and [TensorFlow 2.7.3](https://pypi.org/project/tensorflow/2.7.3/). 

For more information see [TensorFlow 2.6.5](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.5) and [TensorFlow 2.7.3](https://github.com/tensorflow/tensorflow/releases/tag/v2.7.3) release notes.

## May 27, 2022

Change

Cloud TPU now supports Tensorflow 2.8.2 and 2.9.1. For more information see [TensorFlow 2.8.2 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.8.2) and [TensorFlow 2.9.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.9.1).

## March 18, 2022

Change

Cloud TPU now supports Tensorflow 2.6.3. For more information see [TensorFlow 2.6.3 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.3).

## March 09, 2022

Change

Cloud TPU now supports Tensorflow 2.5.3 and 2.7.1. For more information see [TensorFlow 2.5.3 release notes ](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.3) and [TensorFlow 2.7.1 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.7.1).

## February 03, 2022

Change

Cloud TPU now supports Tensorflow 2.8.0. For more information, see [TensorFlow 2.8.0 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.8.0).

## December 02, 2021

Change

Cloud TPU team just released TF-2.4.4, TF-2.5.2 and TF-2.6.2 on Cloud TPUs. The TensorFlow release notes for these releases are shown below.

  * [TF 2.4.4](https://github.com/tensorflow/tensorflow/releases/tag/v2.4.4)
  * [TF 2.5.2](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.2)
  * [TF 2.6.2](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.2)



## November 05, 2021

Change

Cloud TPU now supports Tensorflow 2.7.0. For more information, see [Tensorflow 2.7.0 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.7.0)

## August 24, 2021

Change

Cloud TPU team just released TF-2.3.4, TF-2.4.3 and TF-2.5.1 on Cloud TPUs. The TensorFlow release notes for these releases are shown below.

  * [Tensoflow-2.3.4 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.4)

  * [Tensoflow-2.4.3 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.4.3)

  * [Tensoflow-2.5.1 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.1)




## August 12, 2021

Change

Cloud TPU now supports Tensorflow 2.6.0. For more information, see [Tensorflow 2.6.0 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0).

In TF 2.6.0, TensorFlow has introduced a new version of the TF/XLA bridge using the MLIR compiler infrastructure. The MLIR bridge is enabled by default. To explicitly disable it at runtime, add the following code snippet to your model's code:

tf.config.experimental.disable_mlir_bridge()

## June 22, 2021

Change

The Cloud TPU team has released support for TensorFlow 2.4.2. The corresponding Tensorflow release notes are:

[Tensoflow-2.4.2 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.4.2)

## June 17, 2021

Change

Cloud TPU team just released TF-2.1.4, TF-2.2.3 and TF-2.3.3 on Cloud TPUs. The TensorFlow release notes for these releases are shown below.

  * [Tensoflow-2.1.4 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.4)

  * [Tensoflow-2.2.3 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.2.3)

  * [Tensoflow-2.3.3 Release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.3)




## June 07, 2021

Change

Cloud TPU now supports Tensorflow 2.5.0. For more information, see [Tensorflow 2.5.0 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)

## June 01, 2021

Change

New Cloud TPU VMs make training your ML models on TPUs easier than ever

The new Cloud TPU VM architecture makes it easier than ever before to use our industry-leading TPU hardware. The Cloud TPU VMs provide direct access to TPU host machines, offering a new and improved user experience for developing and deploying TensorFlow, PyTorch, and JAX on Cloud TPUs. Instead of accessing Cloud TPUs remotely over the network, Cloud TPU VMs let you set up your own interactive development environment on each TPU host machine. Now you can write and debug an ML model line-by-line using a single TPU VM, and then scale it up on a Cloud TPU Pod slice to take advantage of the super-fast TPU interconnects. You have root access to every TPU VM you create, so you can install and run any code you wish in a tight loop with your TPU accelerators. You can use local storage, execute custom code in your input pipelines, and more easily integrate Cloud TPUs into your research and production workflows. Google supports Cloud TPU integrations with TensorFlow, PyTorch, and JAX, and you can even write your own integrations via a new libtpu shared library on the VM. For more information, see https://cloud.google.com/blog/products/compute/introducing-cloud-tpu-vms.

## December 14, 2020

Feature

Cloud TPU now supports Shared VPC

Shared VPC allows an organization to connect resources from multiple projects to a common VPC network to communicate with each other securely and efficiently using internal IPs from that network. This release enables connecting to Cloud TPU Nodes from Shared VPC networks.

## September 11, 2020

Feature

#### Compute Engine TPU Metrics and Logs In-Context

New Monitoring tab for TPUs provides key TPU Metrics and access to logs at a glance. You can see a variety of key TPU metrics including MXU utilization, CPU, memory, sent/received traffic, and more. In addition, it provides instant access to TPU logs which give insight into important events.

## August 20, 2020

Feature

### PyTorch/XLA 1.6 Release (GA)

#### Highlights

Cloud TPUs now support the [PyTorch 1.6 release](https://github.com/pytorch/pytorch/releases/tag/v1.6.0), via PyTorch/XLA integration. With this release we mark our general availability (GA) with the models such as ResNet, FairSeq Transformer and RoBERTa, and HuggingFace GLUE task models that have been rigorously tested and optimized.

In addition, with our PyTorch/XLA 1.6 release, you no longer need to run the [env-setup.py](https://github.com/pytorch/xla/blob/master/contrib/scripts/env-setup.py) script on Colab/Kaggle as those are now compatible with native `torch` wheels. You can still continue to use that script if you would like to run with our latest unstable releases.

#### New Features

  * XLA RNG state checkpointing/loading (https://github.com/pytorch/xla/pull/2096)
  * Device Memory XRT API (https://github.com/pytorch/xla/pull/2295)
  * [Kaggle/Colab] Small host VM memory environment utility (https://github.com/pytorch/xla/pull/2025)
  * [Advanced User] XLA Builder Support (https://github.com/pytorch/xla/pull/2125)
  * New op supported on PyTorch/XLA 
    * Hardsigmoid (https://github.com/pytorch/xla/pull/1940)
    * true_divide (https://github.com/pytorch/xla/pull/1782)
    * max_unpool2d (https://github.com/pytorch/xla/pull/2188)
    * max_unpool3d (https://github.com/pytorch/xla/pull/2188)
    * Replication_pad1d (https://github.com/pytorch/xla/pull/2188)
    * Replication_pad2d (https://github.com/pytorch/xla/pull/2188)
  * Dynamic shape support on XLA:CPU and XLA:GPU (experimental)



#### Bug Fixes

  * RNG Fix (proper dropout)
  * Manual all-reduce in backward pass (https://github.com/pytorch/xla/pull/2325)



## August 19, 2020

Feature

Cloud TPU now supports Shared VPC in Beta.

Shared VPC allows an organization to connect resources from multiple projects to a common VPC network to communicate with each other securely and efficiently using internal IPs from that network. This release enables connecting to Cloud TPU Nodes from Shared VPC networks.

## May 29, 2020

Change

Cloud TPU now supports TensorFlow version 1.15.3. See the [TensorFlow 1.15.3 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.3).

## May 21, 2020

Change

Cloud TPU now supports TensorFlow 2.1.1 with Keras support. See the [TensorFlow 2.1.1 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.1) for a complete list of features included in this release.

## May 12, 2020

Change

Cloud TPU currently supports TensorFlow version 1.15.2. See the [Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.2).

TensorFlow 1.15 supported Python 2, but that support has been discontinued with TensorFlow 1.15.2.

## May 08, 2020

Change

Cloud TPU now supports TensorFlow 2.2. See the [TensorFlow 2.2 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.2.0) for a complete list of features included with this release. New models for Image segmentation and Image classification have been added to the official cloud [TPU supported models list](https://docs.cloud.google.com/tpu/docs/tutorials/support-matrix).

## April 21, 2020

Feature

Cloud TPUs and Cloud TPU Pods now support PyTorch 1.5 via the PyTorch/XLA integration. This integration makes it possible for PyTorch users to do everything they can do on GPUs on Cloud TPUs, while minimizing changes to the user experience. You can try out PyTorch on an 8-core Cloud TPU device for free via Google Colab, and you can use PyTorch on Cloud TPUs at a much larger scale on Google Cloud (all the way up to full Cloud TPU Pods).

See the ⁠[PyTorch/XLA 1.5 Release Notes](https://github.com/pytorch/xla/releases/tag/v1.5.0) for a complete list of features included in this release.

## January 09, 2020

Feature

Cloud TPU now supports TensorFlow 2.1 with Keras support. See the [TensorFlow 2.1 Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.0) for a complete list of features included in this release.

## December 05, 2019

Feature

Cloud TPU v2 and v3 Pods are now Generally Available for TensorFlow version 1.x. Supported models can be found [here](https://docs.cloud.google.com/tpu/docs/tutorials/supported-models).

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can request portions of Cloud TPU Pods in slices or sets of cores, so that you purchase only the processing power you need.

Cloud TPU v2 and v3 Pod advantages over a single v2 or v3 Cloud TPU device:

  * Increased training speeds for fast iteration in R&D *Increased human productivity by providing automatically scalable machine learning (ML) compute
  * Ability to train much larger models



Cloud TPU v3 Pod advantages over Cloud TPU v2 Pod:

  * Faster processing and larger memory: 
    * v2 Pod: 11.5 petaflops and 4 TB on-chip memory (HBM)
    * v3 Pod: 100 petaflops and 32 TB HBM, with liquid cooling* Can train even larger models



## October 22, 2019

Change

Cloud TPU now supports TensorFlow version 1.15 ([Release Notes](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.0), [API Documentation](https://www.tensorflow.org/versions/r1.15/api_docs/)). See the current supported TensorFlow versions in the [Cloud TPU supported versions document](https://docs.cloud.google.com/tpu/docs/supported-versions). 

Cloud TPU support for TensorFlow 1.15 includes the following changes:

  * The [official Cloud TPU supported models list](https://docs.cloud.google.com/tpu/docs/tutorials/support-matrix) has been updated.



## July 29, 2019

Change

Cloud TPU now supports [TensorFlow version 1.14](https://www.tensorflow.org/versions/r1.14/api_docs/). Support for Tensorflow versions 1.11 is removed. See the current supported TensorFlow versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

Cloud TPU support for TensorFlow 1.14 includes the following changes:

  * Improved Error Messages: Cloud TPU errors in TensorFlow 1.14 are aggregated across multiple TPU cores and across multiple workers. This change makes error messages more comprehensible for user code.
  * Redesigned object detection codebase: The [object detection codebase](https://github.com/tensorflow/tpu/tree/master/models/official/detection) provides optimized training performance, clean and configurable parameter management, and advanced features such as spatial partition, [NAS-FPN](https://arxiv.org/abs/1904.07392) and [AutoAugment](https://arxiv.org/abs/1805.09501).



## May 07, 2019

Feature

Cloud TPU v3 Pod is available in Beta release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you purchase only the processing power you need.

[Cloud TPU Pod (beta) advantages over a single v3 Cloud TPU device:](https://docs.cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D
  * Increased human productivity by providing automatically scalable machine learning (ML) compute
  * Ability to train much larger models



Cloud TPU v3 Pod _(beta)_ advantages over Cloud TPU v2 Pod _(beta)_ :

  * Faster processing and larger memory: 
    * v2 Pod: 11.5 petaflops and 4 TB on-chip memory (HBM)
    * v3 Pod: 100 petaflops and 32 TB HBM, with liquid cooling* Can train even larger models



Feature

Cloud TPU v2 Pod is available in Beta release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you purchase only the processing power you need.

[Cloud TPU Pod (beta) advantages over a single Cloud TPU v2 device:](https://docs.cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D
  * Increased human productivity by providing automatically scalable machine learning (ML) compute
  * Ability to train much larger models



## March 11, 2019

Change

Cloud TPU now supports [TensorFlow version 1.13](https://www.tensorflow.org/versions/r1.13/api_docs/). Support for Tensorflow versions 1.8 and 1.9 have been removed.

See the current supported TensorFlow versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## January 31, 2019

Feature

Cloud TPU v3 is now GA (generally available). Cloud TPU v3 has double the memory of v2. This gives improved performance and enables support for more classes of models, for example deeper ResNets and larger images with RetinaNet. Existing models that run on Cloud TPU v2 will continue to work. Refer to [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions) for more information.

## November 08, 2018

Change

Cloud TPU now supports [TensorFlow version 1.12](https://www.tensorflow.org/versions/r1.12/api_docs/). This release includes improvements for Keras on Cloud TPUs, performance optimizations throughout the software stack, and improved APIs, error messages, and reliability.

See the current supported TensorFlow versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## November 07, 2018

Feature

Cloud TPU v2 Pod is available in Alpha release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you purchase only the processing power you need.

[Cloud TPU Pod (alpha) advantages:](https://docs.cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D
  * Increased human productivity by providing automatically scalable machine learning (ML) compute
  * Ability to train much larger models than on a single ML accelerator



## October 10, 2018

Feature

Cloud TPU v3 is available in Beta release. You now have a choice between v2 and v3 in your configuration.

  * Cloud TPU v3 has double the memory of v2. This gives improved performance and enables support for more classes of models, for example deeper ResNets and larger images with RetinaNet.
  * Existing models that run on Cloud TPU v2 will continue to work.
  * Refer to [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions) for more information.



Change

Preemptible TPUs are now GA (generally available). A preemptible TPU is a Cloud TPU node that you can create and run at a much lower price than normal nodes. However, Cloud TPU may terminate (preempt) these nodes if it requires access to the resources for another purpose.

  * See how to [use a preemptible TPU](https://docs.cloud.google.com/tpu/docs/preemptible).
  * Review the [pricing](https://cloud.google.com/tpu/docs/pricing) for preemptible and normal Cloud TPU nodes.



## September 27, 2018

Change

Cloud TPU now supports [TensorFlow version 1.11](https://www.tensorflow.org/versions/r1.11/api_docs/). TensorFlow 1.11 introduces experimental support for all of the following on Cloud TPU: Keras, Colab, eager execution, LARS, RNNs, and [Mesh TensorFlow](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md). This release also introduces a high-performance [Cloud Bigtable](https://docs.cloud.google.com/bigtable) integration, new XLA compiler optimizations, other performance optimizations throughout the software stack, and it provides improved APIs, error messages, and reliability.

See the current supported TensorFlow versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## September 07, 2018

Change

Support for TensorFlow version 1.7 ended on September 7, 2018. See the current supported versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## July 24, 2018

Change

We're delighted to announce promotional pricing for Cloud TPU, resulting in significant price reductions. The following table shows the previous pricing and the new pricing available from today:

**US**

| Previous price per TPU per hour | New price per TPU per hour  
---|---|---  
Cloud TPU | $6.50 USD | $4.50 USD  
Preemptible TPU | $1.95 USD | $1.35 USD  
  
**Europe**

| Previous price per TPU per hour | New price per TPU per hour  
---|---|---  
Cloud TPU | $7.15 USD | $4.95 USD  
Preemptible TPU | $2.15 USD | $1.485 USD  
  
**Asia Pacific**

| Previous price per TPU per hour | New price per TPU per hour  
---|---|---  
Cloud TPU | $7.54 USD | $5.22 USD  
Preemptible TPU | $2.26 USD | $1.566 USD  
  
See the [pricing guide](https://cloud.google.com/tpu/docs/pricing) for details.

## July 12, 2018

Feature

Cloud TPU is now available in Google Kubernetes Engine as a Beta feature. Run your machine learning workload in a Kubernetes cluster on Google Cloud, and let GKE manage and scale the Cloud TPU resources for you.

  * See [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) for more information.
  * Refer to the [GKE setup guide](https://docs.cloud.google.com/tpu/docs/kubernetes-engine-setup) for quick instructions on running Cloud TPU with GKE.



## July 02, 2018

Change

Cloud TPU now supports [TensorFlow version 1.9](https://www.tensorflow.org/versions/r1.9/api_docs/). TensorFlow 1.9 brings increases in Cloud TPU performance as well as improved APIs, error messages, and reliability.

## June 27, 2018

Feature

Cloud TPU is now GA (generally available). Google's revolutionary TPUs are designed to accelerate machine learning workloads with TensorFlow. Each Cloud TPU provides up to 180 teraflops of performance, providing the computational power to train and run cutting-edge machine learning models.

  * Follow the [quickstart guide](https://docs.cloud.google.com/tpu/docs/quickstart) to set up your Cloud TPU.
  * Choose a [tutorial](https://docs.cloud.google.com/tpu/docs/tutorials) to run a specific model on your Cloud TPU.



## June 18, 2018

Feature

Preemptible TPUs are now available in _Beta_. A preemptible TPU is a Cloud TPU node that you can create and run at a much lower price than normal nodes. However, Cloud TPU may terminate (preempt) these nodes if it requires access to the resources for another purpose.

  * See how to [use a preemptible TPU](https://docs.cloud.google.com/tpu/docs/preemptible).
  * Review the [pricing](https://cloud.google.com/tpu/docs/pricing) for preemptible and normal Cloud TPU nodes.



Change

Cloud TPU is now available in the European (EU) and Asia Pacific (APAC) regions as well as the United States (US). See the the [pricing details](https://cloud.google.com/tpu/docs/pricing) per region. The following zones are available:

  * **US**
    * `us-central1-b`
    * `us-central1-c`
    * `us-central1-f` ([TFRC program](https://www.tensorflow.org/tfrc/) only)
  * **EU**
    * `europe-west4-a`
  * **APAC**
    * `asia-east1-c`



## June 12, 2018

Change

Support for TensorFlow version 1.6 ended on June 12, 2018. See the current supported versions in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## April 20, 2018

Change

Cloud TPU now supports [TensorFlow version 1.8](https://www.tensorflow.org/versions/r1.8/api_docs/). TensorFlow 1.8 brings increases in Cloud TPU performance as well as improved APIs, error messages, and reliability.

Support for TensorFlow version 1.7 ends on June 20, 2018. See the details in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## April 02, 2018

Change

Cloud TPU now supports [TensorFlow version 1.7](https://www.tensorflow.org/versions/r1.7/api_docs/). Support for TensorFlow version 1.6 ends on June 2, 2018. See the details in the [Cloud TPU versioning policy](https://docs.cloud.google.com/tpu/docs/supported-versions).

## February 12, 2018

Feature

Cloud TPU is available in Beta release. Google's revolutionary TPUs are designed to accelerate machine learning workloads with TensorFlow. Each Cloud TPU provides up to 180 teraflops of performance, providing the computational power to train and run cutting-edge machine learning models.

  * See how to [request TPU quota](https://docs.cloud.google.com/tpu/docs/quota).
  * Follow the [quickstart guide](https://docs.cloud.google.com/tpu/docs/quickstart) to set up your Cloud TPU.
  * Choose a [tutorial](https://docs.cloud.google.com/tpu/docs/tutorials) to run a specific model on your Cloud TPU.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
