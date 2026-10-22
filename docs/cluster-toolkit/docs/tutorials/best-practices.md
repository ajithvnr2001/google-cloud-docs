---
url: https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices/
title: Best practices for running HPC workloads \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:07.804034+00:00
---

# Best practices for running HPC workloads  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Best practices for running HPC workloads Stay organized with collections  Save and categorize content based on your preferences. 

This document provides best practices for tuning Google Cloud resources for optimal performance of high performance computing (HPC) workloads. 

**Tip:** You can configure all recommendations in this document by using a [cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint). To review cluster blueprints that follow these best practices, see [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog). 

## Use HPC or compute optimized machine types

We recommend that you use the [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines), which includes machine types that are tailored to the specific requirements of HPC and compute-intensive workloads, with a focus on delivering the highest return on investment for a given workload class or usage model.

  * H4D machine types are optimized for tightly-coupled applications that scale across multiple nodes. You can create H4D instances using a variety of consumption and provisioning models, including on-demand instance creation, one and three year committed use discounts (CUDs), and Dynamic Workload Scheduler. H4D also supports remote direct memory access (RDMA) communication between H4D instances.

For the configuration steps for H4D instances, see [Set up and scale MPI applications on H4D instances with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application#mpi-library).

  * C2 and C2D machine series. Compute Engine instances created using these machine series have a fixed virtual-to-physical core mapping. They also expose [NUMA](https://docs.kernel.org/mm/numa.html) cell architecture to the guest OS. Both features are critical for performance of tightly-coupled HPC applications.




To reduce the communication overhead between compute nodes, consolidate onto a smaller number of `c2-standard-60` or `c2d-standard-112` instances (with the same total core count) instead of launching a larger number of smaller C2 or C2D instances. Because inter-node communication often limits the performance of MPI workloads, using larger machine types helps reduce this overhead.

## Use compact placement policies

To reduce internode latency, [Compute Engine placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) let you control the placement of compute instances in Google Cloud data centers. We recommend that you use compact placement policies because they provide lower-latency communication within a single zone.

## Use the HPC VM image

Use the [HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm), which incorporates best practices for running HPC applications on Google Cloud. By default, these images are based on Rocky Linux 9 and are available at no additional cost on Google Cloud.

### Turn off automatic updates

**Caution:** If your installed software is out-of-date, turning off automatic updates can cause a security risk.

Automatic updates can significantly and unpredictably degrade performance. To turn off automatic updates, use the [`google_disable_automatic_updates` metadata flag](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#disable_automatic_updates) on compute instances that use HPC VM images version `v20240712` or later. Any VM image that has an HPC VM image as its base can also use this feature, for example, Slurm images.

For example, this setting affects `dnf` automatic package updates on the following image families:

  * HPC images, such as `hpc-rocky-linux-9` (project `cloud-hpc-image-public`)
  * Slurm images, such as `slurm-gcp-6-6-hpc-rocky-linux-9` (project `schedmd-slurm-public`)



Cluster Toolkit provides a convenient setting on relevant modules to set this metadata flag for you: `allow_automatic_updates: false`. Here is an example using the `vm-instance` module:
    
    
    - id: workstation-rocky
      source: modules/compute/vm-instance
      use: [network]
      settings:
        allow_automatic_updates: false
    

Here is an example for a Slurm nodeset:
    
    
    - id: dynamic_nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      use: [network]
      settings:
        node_count_static: 1
        node_count_dynamic_max: 4
        allow_automatic_updates: false
    

The [`examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml) blueprint is configured to automatically turn off updates by setting `allow_automatic_updates` to `false`.

## Choose the best libfabric provider for your workload

There are two [libfabric providers](https://github.com/ofiwg/libfabric?tab=readme-ov-file#providers) that you can use with Intel MPI and HPC instances:

  * **RxM** : uses Reliable Connections (RC) and establishes a unique queue pair (QP) for every communicating _process_ pair, or rank.

However, as you add more nodes and processes to support your workload, the number of required connections grows quadratically and can quickly exhaust the hardware limit of QPs.

  * **Intel PSM3** : uses Unreliable Datagram (UD) primarily for small messages. It multiplexes QPs for large messages by using a small, fixed pool of shared RC QPs to handle multiple peers.

However, using UD does not guarantee that your data will be delivered successfully. If a large amount of MPI data overwhelms the network interface with bursts of traffic, or if the receiving node runs out of receive buffers, then the network could suffer dropped packets.




For more information about how to determine which libfabric provider is best for your workload, see [Determine the number of QPs needed for your workload](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application#estimate-qps).

## Adjust HPC VM image tunings

To get the best performance on Google Cloud, use the following image tunings.

You can use the following sample command to [manually configure a compute instance](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#create_an_hpc_vm_instance) to run HPC workloads. However, Cluster Toolkit automatically handles all of this tuning when you use a cluster blueprint.

To create the compute instance manually, use the Google Cloud CLI and provide the following settings.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --image-family=hpc-rocky-linux-9  \
        --image-project=cloud-hpc-image-public \
        --machine-type=MACHINE_TYPE \
        --network-interface=nic-type=GVNIC \
        --metadata=google_mpi_tuning=--hpcthroughput \
        --threads-per-core=1
    

The preceding sample command applies the following tunings:

  * Sets [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) network interface to enable better communication performance and higher throughput: `--network-interface=nic-type=GVNIC`.

  * Sets network HPC throughput profile: `--metadata=google_mpi_tuning=--hpcthroughput`.

If the compute instance already exists, run `sudo google_mpi_tuning --hpcthroughput` to update the network HPC throughput profile setting.

  * Turns off [simultaneous multithreading](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#disable_simultaneous_multithreading) (SMT) in the guest OS: `--threads-per-core=1`.

If the machine type you entered [doesn't support SMT](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core#limitations), then omit this setting. If the compute instance already exists, run `sudo google_mpi_tuning --nosmt` to turn off simultaneous multithreading.

  * Turns off [Meltdown and Spectre mitigations](https://docs.cloud.google.com/solutions/best-practices-for-using-mpi-on-compute-engine#turn_off_meltdown_and_spectre_mitigation). The HPC VM image enables this setting by default.

**Caution:** Turning off these mitigations can incur a security risk.

If the compute instance already exists, run `sudo google_mpi_tuning --nomitigation` to turn off Meltdown and Spectre mitigations.




## Configure file system tuning

Each primary storage choice for tightly-coupled applications has its own cost, performance profile, APIs, and consistency semantics. The primary choices include the following:

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) is a highly scalable, highly durable, low cost object store. We recommend using Cloud Storage with Cloud Storage FUSE because it lets you scale your data storage in a more cost effective manner than file system services. You can use [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to colocate storage in the same zone as your HPC workloads, providing higher throughput (up to 2.5 TB/s), lower latency, and location flexibility when used with a multi-region bucket. However, this solution is not recommended for applications that require full POSIX compliance.

  * Network File System (NFS) solutions, such as [Filestore](https://docs.cloud.google.com/filestore) and [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp-volumes). These solutions let you deploy shared storage options. Both Filestore and NetApp Volumes are fully managed by Google Cloud. Use them when your application does not have extreme I/O requirements to a single dataset. For performance limits, see the [Filestore documentation](https://docs.cloud.google.com/filestore/docs) and the [NetApp Volumes documentation](https://docs.cloud.google.com/netapp/volumes/docs).

  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs) is a fully managed POSIX-based parallel file system. This solution is commonly used by MPI applications.




## Use Intel MPI

For best performance, use [Intel MPI](https://software.intel.com/en-us/mpi-library).

  * For Ansys Fluent, use Intel MPI `2018.4.274`. Set the version of Intel MPI in Ansys Fluent by using the following command. Replace `MPI_DIRECTORY` with the path to the directory that contains your Intel MPI library.
        
        export INTELMPI_ROOT="MPI_DIRECTORY/compilers_and_libraries_2018.5.274/linux/mpi/intel64/"
        

Intel MPI collective algorithms can be tuned for optimal performance. The recommended collective algorithms for Ansys Fluent is `-genv I_MPI_ADJUST_BCAST 8 -genv I_MPI_ADJUST_ALLREDUCE 10`.

  * For Simcenter STAR-CCM+, we also recommend you use the TCP fabric providers by specifying the following environment variables: `I_MPI_FABRICS shm:ofi` and `FI_PROVIDER tcp`.

  * To successfully use Intel MPI with Cloud RDMA on H4D instances, follow the configuration instructions at [Configure Intel MPI](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application#config_intel_mpi).




For information about configuring MPI applications with H4D and Cloud RDMA, see [Set up and scale MPI applications on H4D instances with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application).

## Summary of best practices

The following is a summary of the recommended best practices for running HPC workloads on Google Cloud.

Resource | Recommendation  
---|---  
Machine family |  Use a machine type from one of the following machine series:

  * H4D
  * H3
  * C2
  * C2D

  
  
OS image | 

  * Use the HPC VM image


  * Apply the HPC VM image best practices

  
File system |  Use one of the following:

  * A Google Cloud managed NFS service such as Filestore or NetApp Volumes
  * A Google Cloud managed posix-based parallel file system, such as Managed Lustre

  
MPI | 

  * Use Intel MPI
  * Review [Set up and scale MPI applications on H4D instances with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application)

  
  
## What's next

  * Run [Ansys Fluent on Google Cloud](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/ansys-fluent).
  * Run [Simcenter STAR-CCM+ on Google Cloud](https://docs.cloud.google.com/cluster-toolkit/docs/simcenter-star-ccm/run-workload). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
