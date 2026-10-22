---
url: https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm/
title: Submit and monitor jobs with Slurm \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:58.269355+00:00
---

# Submit and monitor jobs with Slurm  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Submit and monitor jobs with Slurm Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to submit and monitor jobs by using Slurm in Cluster Director. By using hardware-optimized submission flags and checking node states, you can achieve the following:

  * Align job scheduling with the underlying physical hardware for A4X virtual machine (VM) instances to minimize network latency.

  * Verify job allocations across cluster partitions and forcefully stop unneeded nodes.




For a high-level overview of how Slurm orchestrates jobs in Cluster Director, see [Slurm orchestration in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/orchestration).

## Before you begin

If you haven't already, then connect to a login node in your cluster. For instructions, see [Connect to a cluster's login node](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

## Requirements for submitting jobs for A4X VMs

For cluster partitions that use [A4X VMs](https://docs.cloud.google.com/cluster-director/docs/compute#a4x-series), Slurm uses [block topology](https://slurm.schedmd.com/topology.html#block) to align job scheduling with the physical hardware structure of A4X machines; specifically, [NVLink domains](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#nvlink). This configuration minimizes network latency by ensuring that tasks run on VMs that are physically close to each other.

When you run the [`salloc`](https://slurm.schedmd.com/salloc.html), [`sbatch`](https://slurm.schedmd.com/sbatch.html), or [`srun` commands](https://slurm.schedmd.com/srun.html) in Slurm, you can control how the job interacts with blocks of A4X VMs by using the following flags:

  * [**`--segment= SEGMENT_SIZE`**](https://slurm.schedmd.com/sbatch.html#OPT_segment): this flag groups nodes into segments of a specific size. This configuration lets Slurm fit your job into the available capacity by bypassing nodes that are drained or unavailable. The value must be between `1` and `18`. If your job can't start because there aren't enough adjacent nodes to match your segment size, then we recommend that you use a value of `1`.

  * [**`--exclusive=topo`**](https://slurm.schedmd.com/sbatch.html#OPT_exclusive): this flag reserves an entire sub-block for a job. This isolation helps ensure that no other jobs share the NVLink domain, preventing interference.




## Verify job allocations in your cluster

To verify whether your nodes have jobs scheduled on them, check the node state suffix in Slurm. To do so, complete the following steps:

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. To view information about the nodes and partitions in your cluster, use the [`sinfo` command](https://slurm.schedmd.com/sinfo.html):
         
         sinfo
         

In the output, you can view the state for each node:

     * **`alloc`** : Slurm has assigned all vCPUs on the node to one or more jobs.

     * **`completing`** : the node has finished running a job. Slurm must wait for all associated processes to complete and for the node to return to the `idle` state before scheduling new jobs on this node.

     * **`down`** : Slurm can't schedule jobs on the node. A node enters this state if it encounters a host error, or if Cluster Director fails to obtain capacity for it.

     * **`drained`** : Slurm has removed the node from scheduling after the prolog health check identified an issue with the GPUs that are attached to the node. If workloads are already running on the node, then they may keep running until they complete. To return the node to service, see [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks).

     * **`idle`** : the node has obtained capacity and is preparing to run jobs.

     * **`#idle`** : Cluster Director is provisioning capacity to run your job on the node. If the node is a Flex-start VM, then this state also indicates that Cluster Director is attempting to obtain capacity. For more information, see [Key characteristics of Flex-start](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#key-characteristics-2).

     * **`idle~`** : the node isn't running or has stopped running.

     * **`%idle`** : Cluster Director is deleting the node.

     * **`~idle`** : Cluster Director is stopping the node.

     * **`mix`** : Slurm has allocated jobs to some, but not all, vCPUs on the node.

     * **`#mix`** : Slurm has allocated jobs to some vCPUs on the node; however, Cluster Director is still looking for capacity to run the jobs.




## Delete nodes

You can delete nodes in your cluster when, for example, you want to free up resources, scale down your cluster, or recreate nodes with a different OS image. After deletion, Slurm recreates the nodes based on their type as follows:

  * **Static nodes** : Slurm automatically starts the node recreation process. As soon as the compute instance boots, the node returns to service and you can run jobs on it.

  * **Dynamic nodes** : the nodes state changes to `idle~`. Slurm recreates the node when you submit a job that requires the additional compute capacity.




To delete nodes in your cluster, complete the following steps:

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. To delete nodes in your cluster, use the [`scontrol` command](https://slurm.schedmd.com/scontrol.html):
         
         scontrol update nodename=NODE_NAMES state=NODE_STATE
         

Replace the following:

     * `NODE_NAMES`: a comma-separated list of nodes that you want to delete—for example, `node-1,node-2`.

     * `NODE_STATE`: the power-down state for the nodes. Specify one of the following values:

       * To gracefully delete nodes after running jobs finish, specify `power_down_asap`.

       * To forcefully delete nodes when they're stuck or unresponsive, and abruptly stop the jobs that are running on them, specify `power_down_force`.




## What's next

  * Monitor your cluster:

    * [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards)

    * [Monitor clusters with custom dashboards or alerts](https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)

  * [Troubleshoot cluster errors](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
