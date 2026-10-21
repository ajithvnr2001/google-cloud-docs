---
url: https://docs.cloud.google.com/compute/docs/cpu-platforms/
title: CPU platforms \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:05.662185+00:00
---

# CPU platforms  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/cpu-platforms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  CPU platforms Stay organized with collections  Save and categorize content based on your preferences. 

When you create a virtual machine (VM) or bare metal instance using Compute Engine, you specify a machine series and a machine type for the instance. The machine type determines what CPU platform the compute instance runs on.

A CPU platform offers multiple physical processors, and each of these processors is referred to as a core. For the processors available on Compute Engine, a single CPU core can run as multiple hardware threads through [Simultaneous multithreading (SMT)](https://wikipedia.org/wiki/Simultaneous_multithreading), which is known on Intel processors as [Intel Hyper-Threading Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/hyper-threading/hyper-threading-technology.html). On Compute Engine, each hardware thread is called a virtual CPU (vCPU). Some machine series don't use SMT, and each vCPU instead represents a core. When vCPUs are reported to the instance as occupying different virtual cores, Compute Engine verifies that these vCPUs never share the same physical core.

The [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your compute instance specifies its number of vCPUs, and you can infer its number of physical CPU cores using the default vCPU per core ratio for that machine series:

  * For the C4A, N4A, T2D, T2A, H4D, H3, and A4X machine series, Compute Engine instances always have one vCPU per core.
  * For all other machine series, the compute instances have two vCPUs per core by default.



You can optionally [set the number of threads per core ](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core), to a non-default value, which might benefit some workloads. Importantly, when you do this, the machine type of your compute instance no longer reflects the correct number of vCPUs. Instead, the [pricing](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core#pricing) and number of physical CPU cores remains the same as it would be for the default two vCPUs per core ratio, and the number of vCPUs is half of the value indicated by the machine type.

## Frequency behavior

The processor tables in the following sections describe the hardware specifications of the CPUs that are available with Compute Engine, but keep the following points in mind:

  * **Frequency** : A PC's frequency, or clock speed, measures the number of cycles the CPU executes per second, measured in GHz (gigahertz). Generally, higher frequencies indicate better performance. However, different CPU designs handle instructions differently, so an older CPU with a higher clock speed can be outperformed by a newer CPU with a lower clock speed because the newer architecture deals with instructions more efficiently.

  * **Base frequency** : The frequency at which the CPU runs when the system is idle or under light load. When running at its base frequency, the CPU draws less power and produces less heat.

A compute instance's guest environment reflects the base frequency, regardless of what frequency the CPU is actually running at.

  * **All-core turbo frequency** : The frequency at which each CPU typically runs when all cores in the socket are not idle at the same time. Different workloads place different demands on a system's CPU. Boost technologies address this difference and help processes adapt to the workload demands by increasing the CPU's frequency.

    * Most compute instances get the all-core turbo frequency, even if only the base frequency is advertised to the guest environment.
    * Ampere Altra Arm processors can provide more predictable performance because the frequency for Arm processors is always the all-core turbo frequency.
    * [C4 instances](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) and [C4N instances](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) are able to run at all-core-max turbo frequency by setting the [AdvancedMachineFeature](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) field to `ALL_CORE_MAX`. If this field is unset, the instance runs at the default setting, which is unrestricted frequency.

The `ALL_CORE_MAX` setting isn't available with C4D or C4A compute instances.

  * **Max turbo frequency** : The frequency a CPU targets when stressed by a demanding application like a video game or design modeling application. It's the maximum single-core frequency that a CPU achieves without overclocking.

  * **Processor power management technologies** : Intel processors support multiple technologies to optimize the power consumption. These technologies are divided into two categories, or states:

    * C-states are states when the CPU has reduced or turned off selected functions.
    * P-states provide a way to scale the frequency and voltage at which the processor runs so as to reduce the power consumption of the CPU.

All C4 and C4N machine types, and certain C2 (30, 60 vCPUs), C2D (56, 112 vCPUs) and M2 (208, 416 vCPUs) machine types support instance-provided C-state hints by way of the `MWAIT` instruction.

Compute Engine instances don't provide any facilities for customer control of P-states.




## x86 processors

For most x86 processors, each vCPU is implemented as a single hardware thread.

### Intel processors

On Intel Xeon processors, [Intel Hyper-Threading Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/hyper-threading/hyper-threading-technology.html) supports multiple threads running concurrently on each core. The [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of your compute instance determines the number of its vCPUs and memory.

The H3 machine series doesn't use hyper-threading, and one vCPU represents one physical core.

CPU processor | Processor SKU | Supported machine series and types | Base frequency (GHz) | All-core turbo frequency (GHz) | Single-core max turbo frequency (GHz)  
---|---|---|---|---|---  
Intel Xeon Scalable Processor  
(Granite Rapids)  
6th generation  
  
Intel Xeon Platinum 6985P-C Processor  
| 

  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)

| 2.81 | 3.9 | 4.2  
Intel Xeon Scalable Processor  
(Emerald Rapids)  
5th generation  
| Intel Xeon Platinum 8581C Processor  
| 

  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)
  * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series)
  * [M4N](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_series)

| 2.1 | 2.9 | 4.0  
  
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)

| 2.3 | 3.1 | 4.0  
  
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)

| 2.1 | 2.9 | 4.0  
  
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)

| 2.1 | 2.9 | 3.3  
Intel Xeon Scalable Processor  
(Sapphire Rapids)  
4th generation | Intel Xeon Platinum 8490H Processor | 

  * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series)

| 1.9 | 2.9 | 3.5  
Intel Xeon Platinum 8481C Processor | 

  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)

| 2.2 | 3.0 | 3.0  
  
  * [Z3 bare metal](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)

| 2.2 | 3.0 | 3.8  
  
  * [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms)
  * [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms)
  * [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms)

| 2.0 | 3.8 | 2.9  
Intel Xeon Scalable Processor (Ice Lake)  
3rd Generation | Intel Xeon Platinum  
8373C Processor | 

  * [N22](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)

| 2.6 | 3.4 | 3.5  
Intel Xeon Scalable Processor (Cascade Lake)  
2nd Generation  
Intel Xeon Gold 6268CL Processor | 

  * [N22](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)

| 2.8 | 3.4 | 3.9  
Intel Xeon Gold 6253CL Processor | 

  * [C2](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_machine_types)

| 3.1 | 3.8 | 3.9  
Intel Xeon Platinum 8280L Processor | 

  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types)

| 2.5 | 3.4 | 4.0  
Intel Xeon Platinum 8273CL Processor | 

  * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)

| 2.2 | 2.9 | 3.7  
Intel Xeon Scalable Processor (Skylake)  
1st Generation | Intel Xeon Scalable Platinum 8173M Processor | 

  * [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types)
  * [`m1-megamem` memory-optimized machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)
  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)

| 2.0 | 2.7 | 3.5  
Intel Xeon E7 (Broadwell E7) | Intel Xeon E7-8880V4 Processor | 

  * [`m1-ultramem` memory-optimized machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)

| 2.2 | 2.6 | 3.3  
Intel Xeon E5 v4 (Broadwell E5) | Intel Xeon E5-2696V4 Processor | 

  * [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types)
  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)

| 2.2 | 2.8 | 3.7  
Intel Xeon E5 v3 (Haswell) | Intel Xeon E5-2696V3 Processor | 

  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)

| 2.3 | 2.8 | 3.8  
Intel Xeon E5 v2 (Ivy Bridge) | Intel Xeon E5-2696V2 Processor | 

  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)

| 2.5 | 3.1 | 3.5  
Intel Xeon E5 (Sandy Bridge) | Intel Xeon E5-2689 Processor | 

  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)

| 2.6 | 3.2 | 3.6  
  
1C4 machine types that use the Intel Granite Rapids CPU have a base frequency of 2.8, however vPMU will present 2.3 for compatibility purposes.

2N2 machine types that have 96 or more vCPUs require the Intel Ice Lake CPU.

### AMD processors

AMD processors provide optimized performance and scalability using SMT. In almost all cases, Compute Engine uses two threads per core, and each vCPU is one thread. H4D and Tau T2D are the exceptions where Compute Engine uses one thread per core and each vCPU maps to a physical core.

The [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of your compute instance determines the number of vCPUs and amount of memory allocated to the instance.

CPU processor | Processor SKU | Supported machine series | Base frequency (GHz) | Effective frequency (GHz) | Max boost frequency (GHz)  
---|---|---|---|---|---  
AMD EPYC Turin   
5th Generation | AMD EPYC 9B45 | 

  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)

| 2.7 | 3.5 | 4.1  
AMD EPYC Genoa   
4th Generation | AMD EPYC 9B14 | 

  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series)

| 2.6 | 3.3 | 3.7  
AMD EPYC Milan   
3rd Generation | AMD EPYC 7B13 | 

  * [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types)
  * [Tau T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines)
  * [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines)
  * [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types)

| 2.45 | 2.8 | 3.5  
  
## Arm processors

For Arm processors, Compute Engine uses one thread per core. Each vCPU maps to a physical core with no SMT.

The following table describes the Arm processors that are available for Compute Engine instances.

CPU processor | Processor SKU | Supported machine series and types  
---|---|---  
NVIDIA Grace Processors with Arm Neoverse V2 cores | Superchip | [A4X Max and A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)  
Google Axion Processors with Neoverse V2 Armv9 cores |  | [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)  
Google Axion Processors with Neoverse N3 Armv9.2 cores |  | [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series)  
Ampere Altra Arm Neoverse N1 cores | Q64-30 | [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines)  
  
## Machine types that support multiple CPU platforms

Each Compute Engine zone has a default CPU platform for each machine type. After you create the instance, to see the value of the default CPU platform, you can connect to the guest OS and use the `lscpu` command. This is also referred to as the _Guest CPU_. The Guest CPU for an instance doesn't change while the instance is running.

Some machine types can run on more than one CPU platform. For these machine types you can specify a minimum CPU platform for the instance. If you don't specify a value for the minimum CPU for your instance, or if you use the value `Automatic` for the minimum CPU platform, then your compute instance uses the default CPU platform assigned to the machine type and zone. The parameter is named _minimum CPU_ because when this parameter is set, the compute instance can only be hosted on servers that use CPUs of the specified type, or newer generation CPUs.

The default CPU platform for a zone can change under certain circumstances. If the default CPU platform for the machine type changes in the zone where the instance is running, if you stop and restart the instance, the Guest OS displays the new CPU platform.

If you need your compute instance to always use the default CPU platform that it was created with, then [set minimum CPU for the instance](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#assignmincpuplatformstoppedvm) to the same value as the default CPU platform. This ensures that the Guest CPU remains the same for the instance for as long as that CPU platform is supported.

The following machine types can run on more than one CPU platform:

Machine types | Supported CPU platforms | Minimum CPU values  
(in addition to `Automatic`)  
---|---|---  
C4 machine types with: 

  * 144 vCPUs
  * 288 vCPUs
  * attached Titanium SSD disks

| Intel Granite Rapids | Intel Granite Rapids  
C4 machine types with: 

  * 192 vCPUs and no Titanium SSD disks
  * less than 144 vCPUs and no Titanium SSD disks

| 

  * Intel Granite Rapids
  * Intel Emerald Rapids

| 

  * Intel Granite Rapids1
  * Intel Emerald Rapids

  
E2 | 

  * Intel Broadwell
  * AMD EPYC Milan

| Not available  
N2 with less than 96 vCPUs | 

  * Intel Cascade Lake
  * Intel Ice Lake

| 

  * Intel Cascade Lake
  * Intel Ice Lake

  
N2 with 96 or more vCPUs | Intel Ice Lake | Intel Ice Lake  
N1 | 

  * Intel Sandy Bridge
  * Intel Ivy Bridge
  * Intel Haswell
  * Intel Broadwell
  * Intel Skylake

| 

  * Intel Sandy Bridge
  * Intel Ivy Bridge
  * Intel Haswell
  * Intel Broadwell
  * Intel Skylake

  
  
1 Available only in select regions, as described in C4 minimum CPU regional availability

### C4 minimum CPU regional availability

C4 instances can run on either the Intel Granite Rapids or Intel Emerald Rapids CPU platform. However, the ability to specify Intel Granite Rapids on all shapes is limited to specific regions and zones, as described in the following table.

APACNorth AmericaSouth AmericaEuropeMiddle EastAfrica

Clear all

Zones | Location | MinCPU supported  
---|---|---  
`asia-south2-a`  
`asia-south2-c` | Delhi, India, APAC | Yes  
`asia-southeast3-b` | Bangkok, Thailand, APAC | Yes  
`europe-north1-b`  
`europe-north1-c` | Hamina, Finland, Europe | Yes  
`europe-southwest1-b` | Madrid, Spain, Europe | Yes  
`europe-west4-ai1a` | De Kooy, Netherlands, Europe | Yes  
`europe-west6-a` | Zurich, Switzerland, Europe | Yes  
`europe-west8-c` | Milan, Italy, Europe | Yes  
`northamerica-northeast1-a` | Montréal, Québec, North America | Yes  
`southamerica-west1-c` | Santiago, Chile, South America | Yes  
`us-west2-b` | Los Angeles, California, North America | Yes  
`us-west3-c` | Salt Lake City, Utah, North America | Yes  
  
## CPU features

Chip manufacturers add advanced technologies for computations, graphics, virtualization, and memory management to the CPUs they produce. Google Cloud supports the use of some of these advanced features with Compute Engine.

### Advanced Vector Extensions

Advanced Vector Extensions (AVX) are single instruction, multiple data (SIMD) extensions to the x86 instruction set architecture for microprocessors from Intel and Advanced Micro Devices (AMD). AVX provides new instructions and a new coding scheme.

For more information, see [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions).

AVX is available with all x86 processors used by Compute Engine.

#### Advanced Vector Extensions (AVX2)

AVX2 (also known as Haswell New Instructions) introduces the following additions to AVX:

  * Expands most vector integer SSE and AVX instructions to 256 bits
  * Adds support for Gather, enabling vector elements to be loaded from non-contiguous memory locations
  * Any-to-any permutes with DWORD- and QWORD-granularity
  * Vector shifts



AVX2 is available with the following CPU platforms:

  * Intel Xeon E5 v3 (Haswell) and newer processors
  * All AMD processors



#### Advanced Vector Extensions (AVX512)

AVX-512 expands AVX to 512-bit support using the EVEX prefix encoding. AVX-512 provides built-in acceleration for demanding workloads that involve heavy vector-based processing. The large register for the AVX-512 accelerator supports 32 double-precision and 64 single-precision floating-point numbers, in addition to eight 64-bit and 16 32-bit integers.

Vector Neural Network Instruction (VNNI) is a set of instructions primarily designed for accelerating neural network operations, particularly matrix multiplications, on x86-64 processors. It is part of the AVX-512 instruction set extension and is used for integer dot-product operations.

For more information about AVX-512, see [What is Intel AVX-512?](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/what-is-intel-avx-512.html).

AVX-512 is available with the following CPU platforms:

  * Intel Xeon Scalable Processor (Skylake) 1st Generation and newer processors
  * AMD EPYC Genoa 4th Generation and newer processors



### Advanced Matrix Extensions

[Intel Advanced Matrix Extensions (AMX)](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html) is a new instruction set architecture (ISA) extension designed to accelerate artificial intelligence (AI) and machine learning (ML) workloads. AMX introduces new instructions that can be used to perform matrix multiplication and convolution operations, which are two of the most common operations in AI and ML.

AMX introduces 2-dimensional registers called _tiles_ upon which accelerators can perform operations. AMX is intended as an extensible architecture. The first accelerator implemented is called tile matrix multiply unit (TMUL). Each CPU core of the Sapphire Rapids processor has an independent AMX TMUL unit.

For technical details about Intel AMX, see [Intel AMX support in 5.16](https://lwn.net/Articles/874846/). Intel offers a tutorial on AMX at [Code Sample: Intel Advanced Matrix Extensions (Intel AMX) - Intrinsics Functions](https://www.intel.com/content/www/us/en/developer/articles/code-sample/advanced-matrix-extensions-intrinsics-functions.html#gs.u3cqw2).

AMX is available with Intel Xeon 4th generation (Sapphire Rapids) and later processors. AMX is not available with AMD or Arm processors.

#### Requirements for using AMX

Intel AMX instructions have certain minimum software requirements such as:

  * For custom images, AMX is supported with Linux kernel version 5.16 or later.
  * Compute Engine offers support for AMX in the following [public images](https://docs.cloud.google.com/compute/docs/images/os-details): 
    * CentOS Stream 9
    * Container-Optimized OS 109 LTS or later
    * RHEL 8 (latest build) or later
    * Rocky Linux 8 (latest build) or later
    * Ubuntu 22.04 or later
    * Windows Server 2022 or later
  * [Tensorflow](https://blog.tensorflow.org/2023/01/optimizing-tensorflow-for-4th-gen-intel-xeon-processors.html) 2.9.1 or greater
  * Intel extension for [Intel Optimization for PyTorch](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-for-pytorch-using-google-cloud-platform.html)



### CPU features available to bare metal instances

In addition to offering all the raw compute resources of the server, bare metal instances that run on 4th generation and later Intel Xeon Scalable Processors can use several on board, function-specific accelerators and offloads:

  * **Intel-QAT** : Intel QuickAssist Technology (Intel QAT) accelerates compression, encryption, and decryption
  * **Intel-DLB** : Intel Dynamic Load Balancer (Intel DLB) helps to speed up data queues
  * **Intel IAA** : Intel In-Memory Analytics Accelerator (Intel IAA) improves query processing performance.
  * **Intel DSA** : Intel Data Streaming Accelerator (Intel DSA) helps to copy and move data faster.



### Confidential Computing

To protect your data while it's in use, CPU platforms that support Confidential Computing technologies can be used to create [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instances.

To learn more about the requirements for creating a Confidential VM instance, see [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations).

## What's next

  * Learn more about [Machine families](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Learn more about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).
  * Learn more about [Images](https://docs.cloud.google.com/compute/docs/images).
  * Learn how to [Specify a minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
