---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/ngc-containers/
title: Use gIB NCCL plugins in NVIDIA NGC containers \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:52.060410+00:00
---

# Use gIB NCCL plugins in NVIDIA NGC containers  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/ngc-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use gIB NCCL plugins in NVIDIA NGC containers Stay organized with collections  Save and categorize content based on your preferences. 

Starting from July 2026, the gIB NCCL plugins are integrated directly into [NVIDIA's NGC deep learning containers](https://catalog.ngc.nvidia.com/orgs/nvidia/-/collections/nvidia_dlfw/-), providing an "out-of-the-box" experience that lets you achieve expected performance for collective operations on Google Cloud GPU platforms without manual configuration or tuning.

## Overview of the integration

The integrated NGC base images include the following artifacts:

  * **Environment plugin:** Automatically verifies Google Cloud residency and detects the specific hardware profile (such as H200 or GB200) to dynamically apply the optimal environment variables at runtime.
  * **Network plugin (gIB):** Provides guest-level multi-pathing for high-performance point-to-point transfers and improved load balancing on Google's networks.
  * **Tuner plugin:** Dynamically optimizes collective communication operations specifically for Google Cloud hardware topologies at scale.
  * **[Profiler plugin (CoMMA)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma):** Features advanced telemetry and profiling to detect when a workload isn't progressing and identify stalled NCCL processes.



The plugins detect when they're running on supported Google Cloud platforms and automatically self-configure, while gracefully falling back to standard configurations on unsupported environments.

The integrated gIB NCCL plugins are based on the same code previously available only as Docker container images or `.deb` and `.rpm` packages. For more information about the standalone packages, see the [release notes for x86](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-x86) and [ARM64](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/release-notes-arm64) architectures. The NGC containers include the gIB plugins version 1.1.2 or later.

## Benefits

By using the NVIDIA NGC containers with the embedded Google Cloud plugins, you can expect the following:

  * **Seamless delivery:** Immediate performance on all supported Google Cloud GPU platforms without complex setup.
  * **Optimal performance:** Automated, internal environment detection ensures optimal collective bandwidth and latency out-of-the-box.
  * **Diagnostics ready:** Advanced telemetry client built-in, helping Google support to better assist you.



## Supported platforms

The NGC containers with gIB NCCL plugins support the following Google Cloud machine types:

  * A3 Ultra (H200)
  * A4 (B200)
  * A4X (GB200)
  * A4X Max (GB300)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
