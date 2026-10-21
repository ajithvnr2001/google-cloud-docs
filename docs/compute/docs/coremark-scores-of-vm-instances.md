---
url: https://docs.cloud.google.com/compute/docs/coremark-scores-of-vm-instances/
title: Benchmark scores for compute instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:38.783993+00:00
---

# Benchmark scores for compute instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/coremark-scores-of-vm-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmark scores for compute instances Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get performance benchmarks for a Compute Engine instance or a specific machine series or machine type.

**Important:** If you need help benchmarking performance, or if you want to inquire about available benchmark scores for a machine type, contact your Google Cloud account team.

## How to create performance benchmarks

Performance benchmarks are created with [PerfKitBenchmarker](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker) on Compute Engine instances. For optimal parallelization, the benchmarks are run while specifying a number of threads equal to the number of vCPUs on each machine type. As a standard option in CoreMark, network sockets are used for parallelization. For each test of a compute instance, CoreMark runs five times and the first of those runs is dropped from the results.

Use the following command to generate benchmarks:
    
    
    ./pkb --cloud=GCP \
    --benchmarks=coremark \
    --machine_type=n4-standard-2 \
    --gcp_min_cpu_platform=emeraldrapids \
    --os_type=ubuntu2204 \
    --run_stage_iterations=5 \
    --zone=us-east1-b
    

Edit the machine type, CPU, OS type, and zone as necessary.

## What's next

  * Learn about [Compute Engine machine resource types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Learn about benchmarking disk performance: 
    * [for Linux](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux)
    * [for Windows](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows)
  * Learn about [benchmarking network performance](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
