---
url: https://docs.cloud.google.com/tpu/docs/tpu-os-images/
title: TPU OS images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:14.268579+00:00
---

# TPU OS images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu-os-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU OS images

When you create a TPU VM using Compute Engine, you can use a public Google-managed operating system (OS) image or a custom image. Google-managed images are optimized for TPU performance and include the necessary drivers and agents. By default, all Google Cloud projects have access to these public OS images.

## Google-managed OS images

Google provides Ubuntu-based OS images that are pre-configured with the TPU runtime, drivers, and agents required for your workloads to function.

The following table lists the Google-managed OS images for each supported TPU version:

TPU version | OS version | Kernel version | Image project | Image family  
---|---|---|---|---  
TPU7x (Ironwood) | `Ubuntu 24.04 LTS` | **6.17** | `ubuntu-os-accelerator-images` | `ubuntu-accel-2404-amd64-tpu-tpu7x`  
v6e (Trillium), v5p | `Ubuntu 22.04 LTS` | **6.8** | `ubuntu-os-accelerator-images` | `ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e`  
  
## Custom OS images

With Compute Engine, you can use a custom OS image for TPU VMs. Custom images are useful for:

  * Pre-loading custom software and libraries to reduce VM startup time.
  * Using an OS distribution or version not included in the Google-managed list.
  * Applying custom kernel modifications or security configurations.



### Shared responsibility model

Using a custom OS image follows a shared responsibility model between you and Google, as shown in the following table:

Feature | Google responsibility | User responsibility  
---|---|---  
TPU agents and drivers | Publish modifications and release agents | Install and configure agents and drivers  
Compatibility testing | N/A | Perform compatibility and performance testing  
OS maintenance | N/A | Manage OS updates and licensing  
  
For more information about building and using your own Ubuntu image, see [Use a custom OS image](https://docs.cloud.google.com/tpu/docs/custom-os-image).

## What's next

  * Learn how to [use a custom OS image](https://docs.cloud.google.com/tpu/docs/custom-os-image).
  * [Create a TPU VM instance](https://docs.cloud.google.com/tpu/docs/create-instance-compute).
  * [Create a MIG with a multi-host TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
