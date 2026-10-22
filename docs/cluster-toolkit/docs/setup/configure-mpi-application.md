---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application/
title: Set up and scale MPI applications on H4D instances with Cloud RDMA \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:08.310196+00:00
---

# Set up and scale MPI applications on H4D instances with Cloud RDMA  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Set up and scale MPI applications on H4D instances with Cloud RDMA Stay organized with collections  Save and categorize content based on your preferences. 

H4D instances on Google Cloud are optimized for High Performance Computing (HPC) workloads and feature Cloud RDMA technology to deliver low-latency, high-bandwidth inter-node communication. This guide provides procedures for setting up and configuring Message Passing Interface (MPI) libraries to take advantage of Cloud RDMA on your H4D clusters. It also provides best practices for compiling and scaling your MPI applications on H4D instances.

## Before you begin

Before you attempt any of the tasks in this guide, you must meet the following prerequisites:

  * You have configured a Virtual Private Cloud (VPC) network and subnet [enabled for Cloud RDMA](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). 
  * Increase memory lock and open file limits.



## Overview of configuration steps

This page shows how to configure an H4D cluster for your MPI applications by completing the following steps:

  1. Create a cluster using Cluster Toolkit.
  2. Set up the MPI library.
  3. Configure the guest OS environment.
  4. Optimize and scale MPI with Cloud RDMA.
  5. Use specific commands to run MPI applications.



## Set up the HPC cluster and MPI with Cluster Toolkit

To set up the cluster and MPI using Cluster Toolkit, Terraform, and Slurm, complete the following steps:

  1. Clone a GitHub repository that contains Terraform scripts for deploying a Slurm cluster, for example the [GoogleCloudPlatform/cluster-toolkit/examples/hpc-slurm-h4d](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/) folder.
  2. Modify the Terraform configuration template to match your requirements:

     * Specify regions, zones, placement policies, and the H4D machine type.
     * Define virtual network interfaces (vNICs). To use Cloud RDMA, each Compute Engine instance must have between 2 and 10 network interfaces: one IRDMA vNIC and between one and nine standard gVNIC network interfaces.
     * Specify storage options such as Lustre, NFS, or Local SSD.
     * Reference a preconfigured Slurm scheduler setup.
  3. Create or edit a Slurm job script to define the application execution, including how to load the MPI environment.

  4. Run Terraform to deploy the Slurm cluster based on your configuration.




The following configuration steps are handled by the startup scripts within the Cluster Toolkit blueprint, which are run during deployment:

  * Creates compute instances that use a pre-curated Google HPC VM image designed for H4D, which includes the necessary network tunings, Intel RDMA drivers, and `ibverbs` libraries.
  * Installs the specified MPI library, for example Intel MPI.
  * Installs the necessary storage client software, for example, NFS, Cloud Storage FUSE, or Lustre.



## Set up the MPI library

You can use Cloud RDMA on H4D with Intel MPI or Open MPI. Your application's requirements or recommendations should determine which MPI library you use. Many applications are built and tuned for a specific MPI implementation.

### Configure Intel MPI

Install the Intel MPI library on all of the nodes in the cluster.

To successfully use Intel MPI with Cloud RDMA on H4D instances, you must use the following versions:

  * **Intel MPI** : version 2021.17.2 or later.
  * **`libfabric` library**: version 2.2.0 or later.



Refer to Intel's official documentation for the latest installation procedures. If you use Cluster Toolkit, then it runs scripts that typically handle the installation.

#### Determine the best libfabric provider for your workload

There are two [libfabric providers](https://github.com/ofiwg/libfabric?tab=readme-ov-file#providers) that you can use with H4D instances:

  * **RxM** : uses Reliable Connections (RC) and establishes a unique queue pair (QP) for every communicating _process_ pair, or rank.

However, as you add more nodes and processes to support your workload, the number of required connections grows quadratically and can quickly exhaust the hardware limit of QPs.

  * **Intel PSM3** : uses Unreliable Datagram (UD) primarily for small messages. It multiplexes QPs for large messages by using a small, fixed pool of shared RC QPs to handle multiple peers.

However, using UD does not guarantee that your data will be delivered successfully. If a large amount of MPI data overwhelms the network interface with bursts of traffic, or if the receiving node runs out of receive buffers, then the network could suffer dropped packets.




##### Determine the number of QPs needed for your workload

To determine whether RxM or PSM3 is the best fit for your workload, you need to estimate the number of RC QPs that your application generates. RxM generally has higher absolute performance, but it's bound by a hardware limit of QPs per node.

You can find the maximum number of QP connections per compute instance by executing the following command on the RDMA-enabled instance, and then looking for the value of `max_qp`. On H4D instances, the limit on the number of QPs is 899,000.
    
    
    ibv_devinfo -v
    

To determine the number of RC QPs that your application generates, you can use either of the following methods:

  * **Estimate the required number of QPs**

You can calculate the theoretical maximum total connections (TC) per node for dense communications to determine the number of [queue pairs](https://man7.org/linux/man-pages/man3/ibv_create_qp.3.html) that are needed for your application. Use the following formula:
        
        TC = PPN * PPN * (N - 1)
        

Replace the following:

    * PPN: number of MPI processes or ranks per node
    * N: number of nodes
    * TC: maximum total connections per node

If the calculated total number of QP connections per node is less than the hardware limit for QPs, then you can use RxM. If the calculated number of QP connections is greater than the hardware limit for QPs, then use PSM3 instead.

  * **Determine actual QP usage by using profiling**

Instead of calculating a theoretical limit, you can use PSM3 and run the application with connection statistics enabled. After the job completes, check the maximum PSM3 connections established per node. If the connection count never exceeds the hardware limit of QPs on any node, then you can safely switch to RxM for optimal performance in future runs.

The PSM3 statistics provide a way to obtain exact QP usage. You can enable these statistics by configuring the following environment variable before you run the application:
        
        PSM3_PRINT_STATS=-1
        

The `max_connected_outgoing` statistic counts the number of outgoing connections per rank. A sum of all the `max_connected_outgoing` values across all the ranks in a node is the total number of outgoing connections per node.
        
        Max QPs per Node = SUM(max_connected_outgoing + 1 UD QP) across all ranks
        

If the observed number of QPs is less than the hardware limit for QPs, then you can use RxM. If the observed number of QPs is greater than the hardware limit for QPs, then continue using PSM3.




##### Recommended libfabric provider

Use the following guidelines to determine which libfabric provider is best for your MPI workload:

  * **When to use RxM**

    * If your calculated number of total connections is under the QP hardware limit, then you should use the RxM provider.
    * If your calculated number of total connections exceeds the QP hardware limit, Google highly recommends that you test the workload with RxM first. In practice, most HPC applications intelligently manage their communication topologies and rarely reach this estimated maximum.
    * If the application crashes because it hits the QP hardware limit, then you should then switch to PSM3 and apply the tuning parameters outlined in Using PSM3 with RV kernel module and libfabric.
  * **When to use PSM3**

    * If your calculated or observed total connection count greatly exceeds the QP hardware limit, then use PSM3.
    * If the application jobs are short-lived and use a high number of connections, then you should use PSM3. The overhead of establishing connections can consume the majority of the total elapsed time for a job. Because PSM3 establishes fewer connections by leveraging UD QPs and multiplexing traffic over shared RC QPs, PSM3 should deliver better performance.



#### Use RXM with libfabric

After installation, to ensure that Intel MPI uses the Cloud RDMA interface with RxM, set the following environment variables in your job scripts or user environment:
    
    
    export FI_PROVIDER="verbs;ofi_rxm"
    export FI_VERBS_INLINE_SIZE=39
    export FI_OFI_RXM_BUFFER_SIZE=4096
    export FI_OFI_RXM_USE_SRX=0
    export FI_UNIVERSE_SIZE=N_MPI_RANKS
    

Replace `N_MPI_RANKS` with a value that is based on the number of H4D instances you have provisioned. For example, if you have a 16-node cluster, and there are 192 PPN, then you would use the value 3072, which is `192 * 16` machines.

#### Use PSM3 with RV kernel module with libfabric

To enable PSM3 with Intel MPI, the rendezvous (RV) kernel module is required. To install the PSM3 RV kernel module and libfabric, run the following command on every compute node:
    
    
    curl -sL https://raw.githubusercontent.com/GoogleCloudPlatform/irdma-idpf-oot/main/hpc/rl810_rv_install.sh | bash
    

The recommended configuration for PSM3 for Intel MPI is as follows:
    
    
    # libfabric logs
    FI_LOG_LEVEL=""
    FI_PROVIDER="psm3"
    
    # Cloud RDMA
    IRDMA_SHARED_UD_CREDITS=64
    IRDMA_TRANSPARENT_UD_QD_OVERRIDE=1
    
    # Intel MPI config defined in: https://www.intel.com/content/www/us/en/docs/mpi-library/developer-reference-linux/2021-8/overview.html
    I_MPI_ADJUST_ALLREDUCE=4
    I_MPI_ADJUST_ALLTOALL=1
    I_MPI_ADJUST_BARRIER=7
    I_MPI_ADJUST_BCAST=4
    I_MPI_ADJUST_IALLTOALL=1
    I_MPI_ADJUST_IBCAST=1
    I_MPI_ADJUST_REDUCE=3
    I_MPI_FABRICS="shm:ofi"
    I_MPI_PIN_DOMAIN='omp'
    
    # PSM3 config defined in: https://downloadmirror.intel.com/913765/632489_Intel_Ethernet_Fabric_Host_Software_User_Guide_v1.11.pdf
    PSM3_ALLOW_ROUTERS=1
    PSM3_ERRCHK_TIMEOUT="2000:2000"
    PSM3_FLOW_CREDITS=256
    PSM3_HAL="verbs"
    PSM3_IDENTIFY=1
    PSM3_MEMORY="large"
    PSM3_MQ_RNDV_NIC_THRESH=65536
    PSM3_MR_CACHE_MODE=1
    PSM3_MR_CACHE_SIZE=512
    PSM3_MTU="-1"
    PSM3_NUM_RECV_WQES=32767
    PSM3_NUM_RECV_CQES=65536
    PSM3_RDMA=1
    PSM3_RV_FR_PAGE_LIST_LEN=256
    PSM3_RV_MR_CACHE_SIZE=1024
    PSM3_SEND_REAP_THRESH=1
    

For information on how to set these parameters, see the MPI documentation, [Intel MPI](https://www.intel.com/content/www/us/en/docs/mpi-library/get-started-guide-linux/2021-14/overview.html).

### Configure Open MPI

Install the Open MPI library on all nodes in the cluster.

To successfully use Open MPI with Cloud RDMA on H4D instances, you must use the following versions:

  * **Open MPI** : version 5.0.9 or later.
  * **Unified Communication X (UCX) framework** : version 1.20.0 or later.



To configure your instances to use Open MPI, complete the following steps:

  1. Install the Open MPI library on all nodes in the cluster. You can often install Open MPI using system package managers or compile from source. If you use Cluster Toolkit, then it runs scripts that typically handle the installation.

  2. Ensure your Open MPI installation is built with Unified Communication X (UCX) framework and libfabric support. Open MPI uses UCX by default in many configurations.

  3. After installation, to ensure that Open MPI uses the Cloud RDMA interface, set the following environment variables in your job scripts or user environment:
         
         # Open MPI flags
         -mca pml ucx
         
         # Environment variables
         UCX_TLS=rc,sm
         UCX_UD_VERBS_TIMEOUT=1800s
         UCX_RC_VERBS_TIMEOUT=5s
         UCX_UD_VERBS_TIMER_TICK=1s
         UCX_UD_VERBS_TX_MIN_INLINE=128
         UCX_RC_VERBS_RX_QUEUE_LEN=32752
         UCX_RC_VERBS_TX_POLL_ALWAYS=y
         UCX_RC_VERBS_SEG_SIZE=4096
         UCX_RC_VERBS_FC_WND_SIZE=8
         IRDMA_TRANSPARENT_UD_QD_OVERRIDE=1
         

For information on how to set these parameters, see the MPI documentation, [Open MPI](https://docs.open-mpi.org/en/main/quickstart.html).

An example command for Open MPI resembles the following:
         
         mpirun -mca pml ucx -x UCX_TLS=rc,sm -x UCX_UD_VERBS_TIMEOUT=1800s -x UCX_RC_VERBS_TIMEOUT=5s -x UCX_UD_VERBS_TIMER_TICK=1s -x UCX_UD_VERBS_TX_MIN_INLINE=128 -x UCX_RC_VERBS_RX_QUEUE_LEN=32752 -x UCX_RC_VERBS_TX_POLL_ALWAYS=y -x UCX_RC_VERBS_SEG_SIZE=4096 -x UCX_RC_VERBS_FC_WND_SIZE=8 -x IRDMA_TRANSPARENT_UD_QD_OVERRIDE=1
         




## Configure the guest OS environment

After you have created the H4D instances, configure the guest environment.

### Set up user limits for MPI

In the guest OS of each H4D instance, increase the memory lock and open file limits, using the values shown in the following example:
    
    
    cat << EOF | sudo tee -a /etc/security/limits.conf
    *  hard    memlock         unlimited
    *  soft    memlock         unlimited
    *  hard    nofile          65535
    *  soft    nofile          65535
    EOF
    

### Set environment variables for Intel MPI

You can optionally set the following environment variables:

  * To pin MPI processes within NUMA nodes, potentially improving locality, set the following:
        
        export I_MPI_PIN_DOMAIN=numa
        

  * To increase output verbosity for troubleshooting and debugging, use the following:
        
        export I_MPI_DEBUG=5
        




## Optimize and scale MPI with Cloud RDMA

To achieve optimal performance with MPI on H4D instances, use the following configuration steps to optimize and scale your MPI applications.

### Network tuning for Cloud RDMA

Use the following information when configuring your H4D instances to use Cloud RDMA:

  * **Interface selection** : Explicitly configure your MPI library to use the IRDMA network interface for inter-node communication. This is often configured by using environment variables that select the fabric provider, for example `FI_PROVIDER` for MPIs based on libfabric. See Set up the MPI library.
  * **MTU** : The Falcon VPC network used with Cloud RDMA supports a large [MTU size](https://docs.cloud.google.com/vpc/docs/mtu). Ensure your interface and MPI configuration take advantage of a larger MTU size to reduce overhead. If you use Cluster Toolkit to deploy your cluster, then the MTU size is set to 8896.
  * **Buffer sizes** : Tuning MPI buffer sizes can sometimes improve performance, but default settings are often a good starting point.



### Adjust the SAR threshold for libfabric

When using RxM (RDM over unreliable messaging), set the segmentation and reassembly (SAR) threshold to `2147483648` (2 GB).

The SAR threshold setting determines the message size (in bytes) at which the communication protocol switches from an in-order messaging protocol (also called _eager_) to the rendezvous protocol.

The rendezvous protocol is used to avoid excessive buffering by requiring a handshake between the sender and receiver before transferring data directly from the source to the destination buffer. The rendezvous protocol is generally used for larger messages to avoid consuming excessive memory buffers on the receiving side.

The default value for the SAR threshold ranges from 16 KB to 256 KB.

Except for StarCCM+ applications, use the environment variable `FI_OFI_RXM_SAR_LIMIT` to adjust the threshold to 2 GB.
    
    
      export FI_OFI_RXM_SAR_LIMIT="2147483648"
    

### Pin MPI processes

Binding MPI processes to specific CPU cores is crucial for performance, especially on NUMA systems like H4D instances. This minimizes remote memory access and helps to ensure consistent performance.

  * **Intel MPI** : Use `I_MPI_PIN_DOMAIN` or related environment variables, or command-line options with `mpirun` like `-genv I_MPI_PIN_PROCESSOR_LIST`.
  * **Open MPI** : Use `--map-by` and `--bind-to` options with `mpirun`. For example, the following pins N processes per node to cores: `--map-by ppr:N:node --bind-to core`



Experiment with different pinning strategies (for example, per core or per NUMA node) based on your application's characteristics. Simultaneous multi-threading (SMT) is disabled on H4D instances, so each vCPU represents a physical core.

### Optimize MPI collectives

Collective communication, such as `MPI_Bcast` or `MPI_Allreduce`, can significantly impact performance at scale.

  * **Intel MPI** : Explore environment variables like `I_MPI_COLL_ALGO` to select different algorithms for collectives. Intel MPI often has tuned algorithms for various message sizes and process counts.
  * **Open MPI** : Different collective algorithms can be selected through Modular Component Architecture (MCA) parameters. Open MPI's `hcoll` or `ucx` components often provide optimized collectives.



### Compile applications

Compile your HPC applications with [compiler flags optimized for the AMD EPYC Turin architecture](https://docs.amd.com/r/en-US/63857-AOCC-quick-start-guide/AMD-EPYC-9xx5-Series-Processors-Compiler-Options-Quick-Reference).

  * **Use modern compilers** : Use recent versions of GNU compiler collection (GCC), Intel compilers, or AMD Optimizing C/C++ Compiler (AOCC), if available within your environment.
  * **Architecture flags** : Use flags like `-march=znver4` for AMD EPYC Turin architecture if using GCC or AOCC.
  * **Optimization levels** : Employ appropriate optimization levels, for example `-O2`, `-O3`, or `-Ofast`.
  * **Vectorization** : Ensure vectorization is enabled, which is often the default when using optimization level `-O2` or higher.
  * **Link time optimization (LTO)** : Consider using LTO with flags like `-flto`.



### Optimize application scaling

  * **Load Balancing** : Ensure work is evenly distributed across MPI processes.
  * **Communication Patterns** : Analyze and optimize communication patterns to reduce synchronization overhead and latency. Use point-to-point communication instead of collectives where possible, or use non-blocking operations.
  * **I/O** : For large-scale jobs, parallel I/O solutions like Lustre or other parallel file systems accessible from your cluster are critical to avoid bottlenecks. H4D supports Hyperdisk Balanced disks with capped performance; for I/O intensive needs, we recommend using Local SSD.



### Keep the drivers up to date

If you disable automatic updates on your H4D instances, then you should regularly run the `dnf update` command on the instance to keep the Cloud RDMA driver up to date.

Alternatively, if you used Cluster Toolkit to create your H4D instances, then you can use the `install_cloud_rdma_drivers` setting in the `startup-script` module to ensure that the latest Cloud RDMA drivers are installed on instance startup.

## Run MPI applications

To run your MPI application, use the `mpirun` command from your chosen MPI library.

###  Open MPI 

Create a host file that lists the network names of the H4D instances in the cluster. Then use the following command:
    
    
    # Example for Open MPI
    mpirun -np TOTAL_PROCESSES --hostfile HOST_FILE --map-by ppr:PROCESSES_PER_NODE:node ./YOUR_APPLICATION
    

###  Intel MPI 

Create a host file that lists the network names of the H4D instances in the cluster. Then use the following command:
    
    
    # Example for Intel MPI
    mpirun -n TOTAL_PROCESSES -ppn PROCESSES_PER_NODE -hosts HOST_FILE ./YOUR_APPLICATION
    

###  Intel MPI within a Slurm script 

To run your MPI application, use the `mpirun` command from your chosen MPI library within your Slurm job script.

Depending on which libfabric provider you decided to use, refer to either Use RxM or Use PSM3 with RV kernel module for the environment variables to set for RDMA.

In the following code example, replace the following:

  * `NUMBER_OF_NODES`: the number of instances in your cluster
  * `PROCESSES_PER_NODE`: the number of processes per node


    
    
    # Example for Intel MPI in a Slurm script
    #SBATCH --nodes=NUMBER_OF_NODES
    #SBATCH --ntasks-per-node=PROCESSES_PER_NODE
    
    # Load Intel MPI module if necessary
    module load intelmpi
    
    # Set environment variables for Cloud RDMA
    
    # < _add variables here for RxM or PSM3 with RV_ >
    
    # Run the application
    mpirun ./your_application
    

## What's next

  * Explore [Best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices).
  * Review the [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) documentation.
  * Review the tuning guidelines at [Improve performance of MPI applications that use PSM3](https://docs.cloud.google.com/compute/docs/hpc/mpi-psm3-tuning).
  * Consult the documentation for your specific MPI library and HPC application for detailed tuning and environment variable options.
  * Explore the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit) for HPC examples.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
