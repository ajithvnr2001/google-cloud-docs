---
url: https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support/
title: Dataflow support for TPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:15.665629+00:00
---

# Dataflow support for TPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow support for TPUs Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Dataflow TPU offering is generally available with an allowlist. To get access to this feature, reach out to your account team.

Google Cloud TPUs are custom-designed AI accelerators created by Google that are optimized for training and using of large AI models. They are designed to scale cost-efficiently for a wide range of AI workloads and provide versatility to accelerate inference workloads on AI frameworks, including PyTorch, JAX, and TensorFlow. For more details about TPUs, see [Introduction to Google Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).

## Prerequisites for using TPUs in Dataflow

  * Your Google Cloud projects must be approved to use this GA offering.



## Limitations

This offering is subject to the following limitations:

  * **Only single-host TPU accelerators are supported** : The Dataflow TPU offering supports only single-host TPU configurations where each Dataflow worker manages one or many TPU devices that are not interconnected with TPUs managed by other workers.
  * **Only homogenous TPU worker pools are supported** : Features like Dataflow right fitting and Dataflow Prime don't support TPU workloads.



## Pricing

Dataflow jobs that use TPUs are billed for worker TPU chip-hours consumed and are not billed for worker CPU and memory. For more information, see the Dataflow [pricing page](https://cloud.google.com/dataflow/pricing).

## Availability

The following TPU accelerators and processing regions are available.

### Supported TPU accelerators

The supported TPU accelerator combinations are identified by the tuple (TPU type, TPU topology).

  * **TPU type** refers to the model of the TPU device.
  * **TPU topology** refers to the number and physical arrangement of the TPU chips in a slice.



To configure the type and topology of TPUs for Dataflow workers, use the [`worker_accelerator` pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/service-options) formatted as `type:TPU_TYPE;topology:TPU_TOPOLOGY`.

The following TPU configurations are supported with Dataflow:

TPU type | Topology | Required `worker_machine_type`  
---|---|---  
tpu-v5-lite-podslice | 1x1 | ct5lp-hightpu-1t  
tpu-v5-lite-podslice | 2x2 | ct5lp-hightpu-4t  
tpu-v5-lite-podslice | 2x4 | ct5lp-hightpu-8t  
tpu-v6e-slice | 1x1 | ct6e-standard-1t  
tpu-v6e-slice | 2x2 | ct6e-standard-4t  
tpu-v6e-slice | 2x4 | ct6e-standard-8t  
tpu-v5p-slice | 2x2x1 | ct5p-hightpu-4t  
  
### Regions

For information about available regions and zones for TPUs, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones) in the Cloud TPU documentation.

## What's next

  * Learn how to [run an Apache Beam pipeline on Dataflow with TPUs](https://docs.cloud.google.com/dataflow/docs/tpu/use-tpus).
  * Learn how to [troubleshoot your Dataflow TPU job](https://docs.cloud.google.com/dataflow/docs/tpu/troubleshoot-tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
