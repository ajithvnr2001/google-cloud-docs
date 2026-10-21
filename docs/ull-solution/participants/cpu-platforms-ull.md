---
url: https://docs.cloud.google.com/ull-solution/participants/cpu-platforms-ull/
title: CPU platforms for ULL Solution \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:07.719482+00:00
---

# CPU platforms for ULL Solution  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/cpu-platforms-ull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CPU platforms for ULL Solution

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

You can review the CPU platforms, processor SKUs, and frequency behaviors for Compute Engine U4 instances to choose and optimize the best resources for your workloads.

Compute Engine U4 instances have a single hardware thread per core and don't use simultaneous multithreading (SMT) or hyper-threading:

  * U4S virtual machine (VM) instances represent each hardware thread as a virtual CPU (vCPU).
  * U4P and U4C bare metal instances use physical hardware threads. The number of vCPUs listed in the machine type is equivalent to the number of physical hardware threads on the host server.



## Intel x86 processors

The following table describes the hardware specifications of the CPUs for U4 instances.

CPU processor | Processor SKU | Supported machine series and types | Base frequency (GHz) | All-core turbo frequency (GHz) | Single-core max turbo frequency (GHz)  
---|---|---|---|---|---  
Intel Xeon Scalable Processor  
(Granite Rapids)  
6th generation  
| Intel Xeon Platinum 6985P-C Processor  
| 

  * [U4S](https://docs.cloud.google.com/ull-solution/u4-machines#u4s-series)

| 2.8 | 3.9 | 4.2  
Intel Xeon Scalable Processor  
(Emerald Rapids)  
5th generation  
| Intel Xeon Platinum 8581C Processor  
| 

  * [U4P](https://docs.cloud.google.com/ull-solution/u4-machines#u4p-series) and [U4C](https://docs.cloud.google.com/ull-solution/u4-machines#u4c-series)

| 2.3 | 3.1 | 4.0  
  
## Frequency behavior

The previous tables describe the hardware specifications of the CPUs that are available with Compute Engine, but keep the following points in mind:

  * **Frequency** : A PC's frequency, or clock speed, measures the number of cycles the CPU executes per second, measured in GHz (gigahertz). Generally, higher frequencies indicate better performance. However, different CPU designs handle instructions differently, so an older CPU with a higher clock speed can be outperformed by a newer CPU with a lower clock speed because the newer architecture deals with instructions more efficiently.

  * **Base frequency** : The frequency at which the CPU runs when the system is idle or under light load. When running at its base frequency, the CPU draws less power and produces less heat.

A compute instance's guest environment reflects the base frequency, regardless of what frequency the CPU is actually running at.

  * **All-core turbo frequency** : The frequency at which each CPU typically runs when all cores in the socket are not idle at the same time. Different workloads place different demands on a system's CPU. Boost technologies address this difference and help processes adapt to the workload demands by increasing the CPU's frequency.

[U4 instances](https://docs.cloud.google.com/ull-solution/u4-machines) are able to run at all-core-max turbo frequency by setting the `advancedMachineFeatures.turboMode` field to `ALL_CORE_MAX`. If this field is unset, the instance runs at the default setting, which is unrestricted frequency.

  * **Max turbo frequency** : The frequency a CPU targets when stressed by a demanding application like a video game or design modeling application. It's the maximum single-core frequency that a CPU achieves without overclocking.

  * **Processor power management technologies** : Intel processors support multiple technologies to optimize the power consumption. These technologies are divided into two categories, or states:

    * C-states are states when the CPU has reduced or turned off selected functions.
    * P-states provide a way to scale the frequency and voltage at which the processor runs so as to reduce the power consumption of the CPU.

All U4 machine types support instance-provided C-state hints by way of the `MWAIT` instruction.

Compute Engine instances don't provide any facilities for customer control of P-states.




## What's next

  * Learn more about [Machine families](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Learn more about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).
  * Learn more about [Images](https://docs.cloud.google.com/compute/docs/images).
  * For information about built-in accelerators for CPUs, see [CPU features](https://docs.cloud.google.com/compute/docs/cpu-platforms#cpu_features).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how ULL Solution performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try ULL Solution free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
