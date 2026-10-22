---
url: https://docs.cloud.google.com/cluster-director/docs/orchestration/
title: Slurm orchestration in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.522345+00:00
---

# Slurm orchestration in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/orchestration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Slurm orchestration in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the architecture and core capabilities of the managed Slurm environment that Cluster Director uses to handle cluster management, job scheduling, and workload orchestration.

[Slurm](https://slurm.schedmd.com/documentation.html) is an open-source, scalable, and fault-tolerant cluster manager and job scheduler. Cluster Director integrates and manages Slurm as the primary orchestrator for artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads.

## Slurm architecture in Cluster Director

When you create and deploy a cluster, Cluster Director automatically sets up a pre-configured Slurm environment for you. This environment consists of the following [_nodes_](https://docs.cloud.google.com/cluster-director/docs/networking#architecture):

  * **Controller node** : the primary control plane component that monitors resources, manages system state, and processes all submitted jobs. When you create and deploy a cluster, Cluster Director automatically sets up the controller node in a fault-tolerant configuration to help ensure high availability and reliability.

**Note:** You can't connect to, modify, or delete the controller node in a cluster. Cluster Director manages the controller node for you and applies updates and patches as needed.
  * **Login nodes** : the primary entry points for users to interact with the cluster. You connect to a login node by using SSH to submit jobs, review job statuses, and manage your workflows. The login nodes are pre-configured with the necessary Slurm commands and have access to the shared file systems.

  * **Compute nodes** : these nodes are responsible for executing your jobs. Slurm manages these nodes in partitions, which are logical groupings of nodes with specific characteristics (such as machine type or GPU model). You can configure compute nodes within each partition as follows:

    * **Static nodes** : you specify a minimum number of Compute Engine instances to always be running in the cluster, which provides a baseline of available resources. If a static node encounters an error or is powered down for any reason, then Slurm attempts to restart it.

    * **Dynamic nodes** : you specify a maximum number of additional compute instances that the cluster can automatically create to handle increases in demand. These nodes are created on demand when you submit jobs. If a dynamic node remains in an `idle` state for five minutes, then Slurm automatically powers it down.




## Key Slurm capabilities

Slurm provides several key capabilities that are essential for running large-scale AI, ML, or HPC workloads as follows:

  * **Job scheduling and queuing** : Slurm manages a queue of jobs submitted by users. It allocates resources to these jobs based on priority, policies, and resource availability. This approach helps ensure that your cluster efficiently uses resources.

  * **Resource management** : Slurm has a detailed awareness of the cluster's resources, including vCPUs, memory, and GPUs. When you submit a job, you can request the specific resources your job needs, and Slurm helps ensure it runs on nodes that meet those requirements.

  * **Topology-aware workload placement** : Cluster Director uses Slurm's topology-aware scheduling capabilities to run your workloads. By leveraging information about the physical network layout, Slurm can colocate tasks of a job on compute instances that are close to each other in the network. This approach minimizes latency and is critical for the performance of tightly-coupled distributed training workloads.

  * **Fault tolerance** : if the compute nodes in your cluster have GPUs attached, then Slurm runs two automated scripts to verify the health of your GPUs:

    * **Prolog health check** : before a job starts, Slurm runs a [_prolog script_](https://slurm.schedmd.com/prolog_epilog.html) named `990_chs_gpu_health_check_hcs.sh` to check for hardware issues. If a compute node fails this check, then Slurm drains the node and prevents jobs from running on it. This check helps ensure that your jobs only run on healthy hardware, preventing job failures or incorrect results.

    * **Background health check** : every two minutes, Slurm runs a script named `health_check_program.sh` to detect errors. If the script finds an error, such as unresponsive GPUs or corrupted firmware, then the script logs the error to the compute node's system logs. You can then review the logs to troubleshoot the issue. This check helps you monitor your GPUs without draining your nodes.

  * **Custom Slurm configuration** : you can customize Slurm settings at the cluster, partition, and nodeset level to adapt your cluster to your workload requirements. For a list of supported parameters, see [Supported Slurm settings in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-settings).




## What's next

  * [Slurm controller versions in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions)

  * [Cluster creation process overview](https://docs.cloud.google.com/cluster-director/docs/create/process-overview)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)

  * [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
