---
url: https://docs.cloud.google.com/tpu/docs/faq/
title: Frequently Asked Questions - Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:14.579447+00:00
---

# Frequently Asked Questions - Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Resources ](https://docs.cloud.google.com/tpu/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Frequently Asked Questions - Cloud TPU

This document contains a list of frequently asked questions about Cloud TPUs. It is broken up into sections:

  1. Framework independent FAQs - questions about using Cloud TPUs regardless of what ML framework you are using.
  2. JAX FAQs - questions about using Cloud TPUs with JAX.
  3. PyTorch FAQs - questions about using Cloud TPUs with PyTorch.



## Framework independent FAQs

### How do I check which process is using the TPU on a Cloud TPU VM?

Run `tpu-info` on the Cloud TPU VM to print the process ID and other information about the process using the TPU. See [supported metrics](https://docs.cloud.google.com/tpu/docs/tpu-monitoring-library#list-all-supported-metric-names) for the metrics and their corresponding definitions.
    
    
       tpu-info
    

The output from `tpu-info` is similar to the following:
    
    
       TPU Chips
       ┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┓
       ┃ Chip        ┃ Type        ┃ Devices ┃ PID    ┃
       ┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━┩
       │ /dev/accel0 │ TPU v4 chip │ 1       │ 130007 │
       │ /dev/accel1 │ TPU v4 chip │ 1       │ 130007 │
       │ /dev/accel2 │ TPU v4 chip │ 1       │ 130007 │
       │ /dev/accel3 │ TPU v4 chip │ 1       │ 130007 │
       └─────────────┴─────────────┴─────────┴────────┘
    
       TPU Runtime Utilization
       ┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
       ┃ Device ┃ Memory usage         ┃ Duty cycle ┃
       ┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
       │ 0      │ 0.00 GiB / 31.75 GiB │      0.00% │
       │ 1      │ 0.00 GiB / 31.75 GiB │      0.00% │
       │ 2      │ 0.00 GiB / 31.75 GiB │      0.00% │
       │ 3      │ 0.00 GiB / 31.75 GiB │      0.00% │
       └────────┴──────────────────────┴────────────┘
    
       TensorCore Utilization
       ┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
       ┃ Chip ID ┃ TensorCore Utilization ┃
       ┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
       │ 0       │                  0.00% │
       │ 1       │                  0.00% │
       │ 3       │                  0.00% │
       │ 2       │                  0.00% |
       └─────────┴────────────────────────┘
    
       Buffer Transfer Latency
       ┏━━━━━━━━━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━━┓
       ┃ Buffer Size ┃ P50 ┃ P90 ┃ P95 ┃ P999 ┃
       ┡━━━━━━━━━━━━━╇━━━━━╇━━━━━╇━━━━━╇━━━━━━┩
       │       8MB+  | 0us │ 0us │ 0us │  0us |
       └─────────────┴─────┴─────┴─────┴──────┘
    
    

### How do I add a persistent disk volume to a Cloud TPU VM?

For more information, see [Attach durable block storage to a TPU VM](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute).

### What storage options are supported or recommended for training with TPU VM?

For more information, see [Cloud TPU storage options](https://docs.cloud.google.com/tpu/docs/storage-options).

## JAX FAQs

### How do I know if the TPU is being used by my program?

There are a few ways to double check JAX is using the TPU:

  1. Use the `jax.devices()` function. For example:
         
         assert jax.devices()[0].platform == 'tpu'
         

  2. Profile your program and verify the profile contains TPU operations. For more information, see [Profiling JAX programs](https://github.com/google/jax/blob/main/docs/profiling.md)




For more information, see [JAX FAQ](https://jax.readthedocs.io/en/latest/faq.html)

## PyTorch FAQs

### How do I know if the TPU is being used by my program?

You can verify that PyTorch is using the TPU with TorchTPU in the following ways:

  1. Check the active accelerator device in Python:
         
         import torch
         
         assert torch.accelerator.current_accelerator().type == "tpu"
         

  2. Profile your workload with `torch.profiler` and verify that TPU operations appear in the trace. For more information, see [Performance profiling with XProf](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/).




For more information, see [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu), the [TorchTPU documentation](https://torchtpu.readthedocs.io/en/latest/), and the [TorchTPU FAQ](https://torchtpu.readthedocs.io/en/latest/faq/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
