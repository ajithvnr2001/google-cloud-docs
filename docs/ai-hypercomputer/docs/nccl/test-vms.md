---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms/
title: Run NCCL on Compute Engine instances \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:40.244330+00:00
---

# Run NCCL on Compute Engine instances  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run NCCL on Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page describes how to run NCCL tests with [NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) on A4X Max, A4X, A4, and A3 Ultra instances. The example in this page is for a two node NCCL test.

If you use schedulers such as Cluster Director, Cluster Toolkit, or GKE, you don't need to follow the steps on this page. Instead, see the following:

  * [Run NCCL on GKE clusters that use Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke)
  * [Run NCCL on GKE clusters that use A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x-max)
  * [Run NCCL on GKE clusters that use A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x)
  * [Run NCCL on GKE clusters that use A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom)
  * [Run NCCL tests on Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)
  * [Run NCCL tests on Slurm clusters in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#verify-health)



To run NCCL tests on A3 Mega and A3 High, see [Create an A3 Mega or A3 High instance with GPUDirect enabled](https://docs.cloud.google.com/compute/docs/gpus/gpudirect).

## Before you begin

Before you run NCCL tests, make sure you [install NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl) in your runtime environment.

## Run NCCL tests

To run NCCL tests in a non-scheduled environment:

  1. Install CUDA 12.8 (or later).
  2. Install Open MPI.
  3. Set up [non-interactive ssh logins](https://docs.open-mpi.org/en/v5.0.x/launching-apps/ssh.html#non-interactive-ssh-logins) among the compute instances.
  4. Build [nccl-tests](https://github.com/NVIDIA/nccl-tests) with MPI enabled. When building nccl-tests, set `NCCL_HOME=/usr/local/gib`.



To run the script shipped with the NCCL/gIB package:
    
    
    # The script assumes binaries at /opt/nccl-tests/build/
    $ /usr/local/gib/scripts/run_nccl_tests.sh -d /opt/nccl-tests/build/ -p 22 -t all_gather -m 0x0 -b 4K -e 16G a4-vm-1 a4-vm-2
    

We also publish a diagnostic container image with everything included at <http://us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:latest>.

The following example shows output on two A4 instances:
    
    
    NCCL version 2.25.1+cuda12.8
    #
    #                                                              out-of-place                       in-place
    #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
    #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
            4096            64     float    none      -1    59.97    0.07    0.06      0    57.49    0.07    0.07      0
            8192           128     float    none      -1    58.17    0.14    0.13      0    58.36    0.14    0.13      0
           16384           256     float    none      -1    59.07    0.28    0.26      0    59.03    0.28    0.26      0
           32768           512     float    none      -1    60.93    0.54    0.50      0    60.79    0.54    0.51      0
           65536          1024     float    none      -1    61.93    1.06    0.99      0    62.17    1.05    0.99      0
          131072          2048     float    none      -1    64.62    2.03    1.90      0    64.48    2.03    1.91      0
          262144          4096     float    none      -1    66.50    3.94    3.70      0    67.05    3.91    3.67      0
          524288          8192     float    none      -1    69.37    7.56    7.09      0    67.83    7.73    7.25      0
         1048576         16384     float    none      -1    117.2    8.95    8.39      0    113.7    9.22    8.64      0
         2097152         32768     float    none      -1    118.8   17.65   16.55      0    118.1   17.75   16.64      0
         4194304         65536     float    none      -1    122.2   34.32   32.17      0    122.6   34.22   32.08      0
         8388608        131072     float    none      -1    132.2   63.44   59.48      0    130.7   64.20   60.18      0
        16777216        262144     float    none      -1    139.2  120.49  112.96      0    139.7  120.07  112.56      0
        33554432        524288     float    none      -1    152.0  220.81  207.01      0    152.1  220.59  206.81      0
        67108864       1048576     float    none      -1    227.6  294.87  276.44      0    225.9  297.08  278.51      0
       134217728       2097152     float    none      -1    431.7  310.87  291.44      0    438.0  306.41  287.26      0
       268435456       4194304     float    none      -1    728.6  368.44  345.41      0    735.9  364.79  341.99      0
       536870912       8388608     float    none      -1   1404.2  382.33  358.44      0   1418.4  378.51  354.85      0
      1073741824      16777216     float    none      -1   2795.8  384.06  360.05      0   2768.9  387.79  363.55      0
      2147483648      33554432     float    none      -1   5440.1  394.75  370.08      0   5418.7  396.31  371.54      0
      4294967296      67108864     float    none      -1    10754  399.40  374.43      0    10746  399.67  374.69      0
      8589934592     134217728     float    none      -1    21434  400.77  375.72      0    21421  401.01  375.95      0
     17179869184     268435456     float    none      -1    42679  402.53  377.38      0    42792  401.48  376.38      0
    

## What's next

  * [Collect and understand NCCL Logs for troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand).
  * [Monitor compute instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).
  * [Troubleshoot slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
