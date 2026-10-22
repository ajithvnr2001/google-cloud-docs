---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/generate-nvidia-bug-report-for-blackwell-gpus/
title: Generate NVIDIA bug report for Blackwell GPUs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:25.854974+00:00
---

# Generate NVIDIA bug report for Blackwell GPUs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/generate-nvidia-bug-report-for-blackwell-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Generate NVIDIA bug report for Blackwell GPUs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create an NVIDIA bug report for your machine types that use [NVIDIA Blackwell GPUs](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/). If you want to identify which of your machine types are using the NVIDIA Blackwell GPU, see [GPU models](https://docs.cloud.google.com/compute/docs/gpus#gpu-models).

If your machine type uses the NVIDIA Blackwell GPU architecture, the generated NVIDIA bug report doesn't include critical low-level hardware data when you run the [nvidia-bug-report.sh](https://docs.nvidia.com/deploy/rma-process/index.html#topic_3_1) script. This data contains information such as the physical layer status of NVLink connections, internal GPU register values, and raw diagnostic segments from the firmware. This information is essential for diagnosing issues, especially those related to NVLink, which could lead to [GPU Xid errors](https://docs.nvidia.com/deploy/xid-errors/index.html#xid-error-listing) or unresolved performance degradation.

## Generate an NVIDIA bug report

To generate a bug report, complete the following steps:

  1. Connect to your GPU instance. Choose one of the following options:

     * [Connect to Linux instances](https://docs.cloud.google.com/compute/docs/connect/standard-ssh)
     * [Connect to Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)
  2. Download and install the MFT package by selecting one of the following options:




### Container-Optimized OS

If your instance uses a Container-Optimized OS (COS) as the guest operating system, use the open source [COS NVIDIA Bug Report Collector](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/cos-nvidia-bug-report) tool to generate the bug report with MFT. This tool automatically injects supported MST kernel modules that match the COS kernel, installs the userspace tool, generates the bug report, and optionally uploads the result to a Cloud Storage bucket. 

### Other OS

For other Linux OSes, complete the following steps:

  1. Download and install NVIDIA Firmware Tools (MFT) software version 4.32.0 or higher from the [NVIDIA website](https://network.nvidia.com/products/adapter-software/firmware-tools/).
  2. Install the tool. For more information, see [Compilation and installation](https://docs.nvidia.com/networking/display/mftv4320/compilation+and+installation) in the NVIDIA Firmware Tools (MFT) Documentation. After you install MFT, the [nvidia-bug-report.sh](https://docs.nvidia.com/deploy/rma-process/index.html#topic_3_1) script automatically uses the MFT tools to generate the report. You don't need to interact with MFT tools directly.
  3. Run the `nvidia-bug-report.sh` script to generate a bug report. This process takes about two minutes.
  4. Extract the report.
  5. Verify that the report includes MFT data by running the following command on your extracted bug report file: 
         
         grep -m 1 -A 30 "Starting GPU MST dump.." PATH_TO_UNZIPPED_BUG_REPORT

The output is similar to the following example:
         
         Starting GPU MST dump..
         ... (additional MFT data) ...
                         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
