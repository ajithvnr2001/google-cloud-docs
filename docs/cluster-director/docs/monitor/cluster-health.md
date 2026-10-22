---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health/
title: Manage cluster health \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.292439+00:00
---

# Manage cluster health  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Manage cluster health Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to manage cluster health and perform host maintenance events in Cluster Director.

In addition to running [automated health checks for the GPUs attached to your compute nodes](https://docs.cloud.google.com/cluster-director/docs/orchestration#capabilities), Cluster Director provides the following tools to help you proactively manage cluster resilience and help ensure optimal operation for your clusters. Specifically, you can do one or more of the following:

  * Manually start planned host maintenance events.

  * Verify cluster health.

  * Bypass the prolog health check for a specific job.




## Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Required roles

To get the permissions that you need to view and manage clusters health, ask your administrator to grant you the [Hypercompute Cluster Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view and manage clusters health. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and manage clusters health:

  * To view the details of a single cluster: `hypercomputecluster.clusters.describe`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Perform cluster management tasks

The following sections describe how you can manage the health of your cluster.

### Manually start planned host maintenance events

If a [host maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) is planned for your cluster, then you can immediately start maintenance rather than waiting for the planned time.

To manually start a planned host maintenance event for your cluster by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to view the details of. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  4. Click the **Topology** tab. Then, if a maintenance event is scheduled for your cluster, click **Start maintenance now**.




### Verify cluster health

Before running a job on a compute node, Slurm automatically runs a quick GPU health check on the node. If the node fails the check, then Slurm drains the node and prevents scheduling new jobs on it.

To more thoroughly test GPU health and network bandwidth across the compute nodes in a cluster partition, you can manually run [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl). If an NCCL test identifies any unhealthy nodes, then you can modify your jobs to run on different nodes. Running NCCL tests helps you verify a partition's health and troubleshoot issues before you run critical workloads.

Based on the machine series that the compute nodes in a cluster partition use, select one of the following options:

###  A4X 

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. In the `$HOME` directory, download the following NCCL scripts:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.101.0/examples/machine-learning/a4x-highgpu-4g/system_benchmarks/run-nccl-tests-via-ramble.sh
         

  3. To view a list of network interface names that the compute nodes in a cluster partition use, run the following command:
         
         srun -N 1 --partition=PARTITION_NAME ip addr show
         

Replace `PARTITION_NAME` with the name of the cluster partition that you want to test. To review the partitions in your cluster, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

  4. To help ensure that the network interface names and the name of the partition to test are correct, complete the following steps:

     1. Open the `run-nccl-tests-via-ramble.sh` file with a text editor of your choice.

     2. Compare the network interface names in the `run-nccl-tests-via-ramble.sh` file with the network interface names that you viewed in the output of the previous command. If they don't match, then, in the `env_vars` section within the `run-nccl-tests-via-ramble.sh` file, edit the `OMPI_MCA_btl_tcp_if_include`, `UCX_NET_DEVICES`, and `NCCL_SOCKET_IFNAME` variables as follows:
            
            env_vars:
              set:
                **OMPI_MCA_btl_tcp_if_include: TCP_INTERFACE_NAME**
                PMIX_MCA_gds: ^ds12
                **UCX_NET_DEVICES: UCX_NET_DEVICES_LIST**
                PMIX_MCA_psec: native
                UCX_IB_FORK_INIT: n
                NCCL_NET: gIB
                **NCCL_SOCKET_IFNAME: NCCL_SOCKET_IFNAMES**
                LD_LIBRARY_PATH: /usr/local/gib/lib64:usr/local/nvidia/lib
            

Replace the following:

        * `TCP_INTERFACE_NAME`: the name of the Transmission Control Protocol (TCP) interface to include—for example, `enp0s1`.

        * `UCX_NET_DEVICES_LIST`: a comma-separated list of Unified Communication X (UCX) network devices—for example, `gpu0rdma0,gpu1rdma0,gpu2rdma0,gpu3rdma0`.

        * `NCCL_SOCKET_IFNAMES`: a comma-separated list of NCCL socket interface names—for example, `enp0s1,enp192s1`.

     3. If the partition where the node that you want to test isn't the default partition, then, at the end of the `sbatch` section, add the following line:
            
            #SBATCH --partition=PARTITION_NAME
            

     4. By default, the test runs the [`AllGather`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allgather), [`AllReduce`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allreduce), and [`ReduceScatter` benchmarks](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#reducescatter) across an incremental and increasing number of nodes, up to the number of nodes that are available in the cluster partition. The test submits a separate job for each combination of benchmarks and number of nodes to test. To edit the benchmarks to run or the number of nodes to test, in the `applications` section, edit the `workload` and `n_nodes` variables as follows:
            
            applications:
              nccl-tests:
                workloads:
                  '{workload}':
                    experiments:
                      '{workload}-{n_nodes}':
                        variables:
                          **workload: [ NCCL_BENCHMARK]**
                          **n_nodes: [ NUMBER_OF_NODES]**
                        matrix:
                        - n_nodes
                        - workload
            

Replace the following:

        * `NCCL_BENCHMARK`: a comma-separated list of NCCL benchmarks to run on the nodes—for example, `all-gather, all-reduce, reduce-scatter`.

        * `NUMBER_OF_NODES`: a comma-separated list of the different number of nodes the test runs against. Specify values between `1` and the number of nodes in your cluster partition—for example, `2, 4, 8, 16, 32`.

  5. To run the NCCL test script, run the following command:
         
         nohup bash ./run-nccl-tests-via-ramble.sh "$HOME" >& nccl-$(date -Iseconds).log & tail -f nccl-*.log
         

Running the NCCL test can take some time to complete. When it does complete, the output is similar to the following:
         
         ...
         ---- SUMMARY for >1GB Message Sizes ----
         workload        n_nodes msg_size        busbw
         all-gather      2       1073741824      XXX.XX
         all-gather      2       2147483648      XXX.XX
         all-gather      2       4294967296      XXX.XX
         all-gather      2       8589934592      XXX.XX
         ...
         all-reduce      2       1073741824      XXX.XX
         ...
         reduce-scatter  2       1073741824      XXX.XX
         ...
         
         -------- Benchmarking Complete -------
         




###  A4 

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. In the `$HOME` directory, download the following NCCL scripts:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.88.0/examples/machine-learning/a4-highgpu-8g/system_benchmarks/run-nccl-tests-via-ramble.sh
         

  3. To view a list of network interface names that the compute nodes in a cluster partition use, run the following command:
         
         srun -N 1 --partition=PARTITION_NAME ip addr show
         

Replace `PARTITION_NAME` with the name of the cluster partition that you want to test. To review the partitions in your cluster, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

  4. To help ensure that the network interface names and the name of the partition to test are correct, complete the following steps:

     1. Open the `run-nccl-tests-via-ramble.sh` file with a text editor of your choice.

     2. Compare the network interface names in the `run-nccl-tests-via-ramble.sh` file with the network interface names that you viewed in the output of the previous command. If they don't match, then, in the `env_vars` section within the `run-nccl-tests-via-ramble.sh` file, edit the `OMPI_MCA_btl_tcp_if_include` and `NCCL_SOCKET_IFNAME` variables as follows:
            
            env_vars:
              set:
                **OMPI_MCA_btl_tcp_if_include: TCP_INTERFACE_NAME**
                PMIX_MCA_gds: ^ds12
                NCCL_NET: gIB
                **NCCL_SOCKET_IFNAME: NCCL_SOCKET_IFNAMES**
                LD_LIBRARY_PATH: /usr/local/gib/lib64:usr/local/nvidia/lib
            

Replace the following:

        * `TCP_INTERFACE_NAME`: the name of the Transmission Control Protocol (TCP) interface to include—for example, `enp0s1`.

        * `NCCL_SOCKET_IFNAMES`: a comma-separated list of NCCL socket interface names—for example, `enp0s1,enp192s1`.

     3. If the partition where the node that you want to test isn't the default partition, then, at the end of the `sbatch` section, add the following line:
            
            #SBATCH --partition=PARTITION_NAME
            

     4. By default, the test runs the [`AllGather`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allgather), [`AllReduce`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allreduce), and [`ReduceScatter` benchmarks](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#reducescatter) across an incremental and increasing number of nodes, up to the number of nodes in the cluster partition. The test submits a separate job for each combination of benchmarks and number of nodes to test. To edit the benchmarks to run or the number of nodes to test, in the `applications` section, edit the `workload` and `n_nodes` variables as follows:
            
            applications:
              nccl-tests:
                workloads:
                  '{workload}':
                    experiments:
                      '{workload}-{n_nodes}':
                        variables:
                          **workload: [ NCCL_BENCHMARK]**
                          **n_nodes: [ NUMBER_OF_NODES]**
                        matrix:
                        - n_nodes
                        - workload
            

Replace the following:

        * `NCCL_BENCHMARK`: a comma-separated list of NCCL benchmarks to run on the nodes—for example, `all-gather, all-reduce, reduce-scatter`.

        * `NUMBER_OF_NODES`: a comma-separated list of the different number of nodes the test runs against. Specify values between `1` and the number of nodes in your cluster partition—for example, `2, 4, 8, 16, 32`.

  5. To run the NCCL test script, run the following command:
         
         nohup bash ./run-nccl-tests-via-ramble.sh "$HOME" >& nccl-$(date -Iseconds).log & tail -f nccl-*.log
         

Running the NCCL test can take some time to complete. When it does complete, the output is similar to the following:
         
         ...
         ---- SUMMARY for >1GB Message Sizes ----
         workload        n_nodes msg_size        busbw
         all-gather      2       1073741824      XXX.XX
         all-gather      2       2147483648      XXX.XX
         all-gather      2       4294967296      XXX.XX
         all-gather      2       8589934592      XXX.XX
         ...
         all-reduce      2       1073741824      XXX.XX
         ...
         reduce-scatter  2       1073741824      XXX.XX
         ...
         
         -------- Benchmarking Complete -------
         




###  A3 Ultra 

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. In the `$HOME` directory, download the following NCCL scripts:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-ultragpu-8g/nccl-tests/import_pytorch_container.sh
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-ultragpu-8g/nccl-tests/build-nccl-tests.sh
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-ultragpu-8g/nccl-tests/run-nccl-tests.sh
         

  3. To view a list of network interface names that the compute nodes in a cluster partition use, run the following command:
         
         srun -N 1 --partition=PARTITION_NAME ip addr show
         

Replace `PARTITION_NAME` with the name of the cluster partition that you want to test. To review the partitions in your cluster, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

  4. To help ensure that the network interface names and the name of the partition to test are correct, complete the following steps:

     1. Open the `build-nccl-tests.sh` and `run-nccl-tests.sh` files with a text editor of your choice.

     2. Compare the network interface names in the `run-nccl-tests.sh` file with the network interface names that you viewed in the output of the previous command. If they don't match, then, in the `run-nccl-tests.sh` file, edit the `NCCL_SOCKET_IFNAME` variable as follows:
            
            source /usr/local/gib/scripts/set_nccl_env.sh
            export NCCL_NET=gIB
            **export NCCL_SOCKET_IFNAME=NCCL_SOCKET_IFNAMES**
            

Replace `NCCL_SOCKET_IFNAMES` with a comma-separated list of NCCL socket interface names—for example, `enp0s1,enp192s1`.

     3. If the partition where your node exists isn't the default cluster's partition, then, in the `sbatch` section of the `build-nccl-tests.sh` and `run-nccl-tests.sh` files, add the following line:
            
            #SBATCH --partition=PARTITION_NAME
            

     4. Optional: To run a different NCCL benchmark than the default [`AllGather` benchmark](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allgather), edit the last line of the `run-nccl-tests.sh` file as follows:
            
            /nccl/nccl-tests/build/NCCL_BENCHMARK -b 8M -e 8G -f 2 -g 1 -w 5 --iters 200;
            

Replace `NCCL_BENCHMARK` with the type of NCCL benchmark that you want to run on the cluster nodes—for example, `all_reduce_perf`.

  5. To import the squash container image, run the following command:
         
         bash ./import_pytorch_container.sh
         

Importing the squash container image takes approximately 10 minutes to complete.

  6. To build the test, as well as grant the test access to all of a node's resources by using the [`--exclusive` flag](https://slurm.schedmd.com/sbatch.html#OPT_exclusive), run the following command:
         
         sbatch --partition=PARTITION_NAME --exclusive build-nccl-tests.sh
         

Building the test takes approximately five minutes to complete.

  7. To run the NCCL test, run the following command:
         
         sbatch -N TEST_SIZE --partition=PARTITION_NAME --exclusive run-nccl-tests.sh
         

Replace `TEST_SIZE` with the number of nodes that you want to test in your nodeset. Specify a value between `1` and the number of nodes in your cluster partition.

Running the NCCL test takes approximately five minutes to complete. When the test completes, the system creates and stores an `slurm-JOB_ID.out` file in the `$HOME` directory with the results of your test.




###  A3 Mega 

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. In the `$HOME` directory, download the following NCCL scripts:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-megagpu-8g/nccl-tests/import_pytorch_container.sh
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-megagpu-8g/nccl-tests/build-nccl-tests.sh
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/tags/v1.65.0/examples/machine-learning/a3-megagpu-8g/nccl-tests/run-nccl-tests.sh
         

  3. To view a list of network interface names that the compute nodes in a cluster partition use, run the following command:
         
         srun -N 1 --partition=PARTITION_NAME ip addr show
         

Replace `PARTITION_NAME` with the name of the cluster partition that you want to test. To review the partitions in your cluster, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

  4. To help ensure that the network interface names and the name of the partition to test are correct, complete the following steps:

     1. Open the `build-nccl-tests.sh` and `run-nccl-tests.sh` files with a text editor of your choice.

     2. Compare the network interface names in the `run-nccl-tests.sh` file with the network interface names that you viewed in the output of the previous command. If they don't match, then, in the `run-nccl-tests.sh` file, edit the `NCCL_FASTRAK_CTRL_DEV`, `NCCL_FASTRAK_IFNAME`, and `NCCL_SOCKET_IFNAME` variables as follows:
            
            NCCL_LIB_DIR="/var/lib/tcpxo/lib64" source /var/lib/tcpxo/lib64/nccl-env-profile.sh
            **export NCCL_FASTRAK_CTRL_DEV=NCCL_FASTRAK_CTRL_DEV**
            **export NCCL_FASTRAK_IFNAME=NCCL_FASTRAK_IFNAME**
            **export NCCL_SOCKET_IFNAME=NCCL_SOCKET_IFNAMES**
            export NCCL_FASTRAK_LLCM_DEVICE_DIRECTORY=/dev/aperture_devices
            

Replace the following:

        * `NCCL_FASTRAK_CTRL_DEV`: the NCCL fastrak control device interface name—for example, `enp0s12`.

        * `NCCL_FASTRAK_IFNAME`: a comma-separated list of NCCL fastrak interface names—for example, `enp6s0,enp7s0,enp13s0`.

        * `NCCL_SOCKET_IFNAMES`: a comma-separated list of NCCL socket interface names—for example, `enp0s1`.

     3. If the partition where your node exists isn't the default cluster's partition, then, in the `sbatch` section of the `build-nccl-tests.sh` and `run-nccl-tests.sh` files, add the following line at the end of the section:
            
            #SBATCH --partition=PARTITION_NAME
            

     4. Optional: To run a different NCCL benchmark than the default [`AllGather` benchmark](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html#allgather), edit the last line of the `run-nccl-tests.sh` file as follows:
            
            /nccl/nccl-tests/build/NCCL_BENCHMARK -b 8M -e 8G -f 2 -g 1 -w 5 --iters 200;
            

Replace `NCCL_BENCHMARK` with the type of NCCL benchmark that you want to run on the cluster nodes—for example, `all_reduce_perf`.

  5. To import the squash container image, run the following command:
         
         bash ./import_pytorch_container.sh
         

Importing the squash container image takes approximately 10 minutes to complete.

  6. To build the test, as well as grant the test access to all of a node's resources by using the [`--exclusive` flag](https://slurm.schedmd.com/sbatch.html#OPT_exclusive), run the following command:
         
         sbatch --partition=PARTITION_NAME --exclusive build-nccl-tests.sh
         

Building the test takes approximately five minutes to complete.

  7. To run the NCCL test, run the following command:
         
         sbatch -N TEST_SIZE --partition=PARTITION_NAME --exclusive run-nccl-tests.sh
         

Replace `TEST_SIZE` with the number of nodes that you want to test in your nodeset. Specify a value between `1` and the number of nodes in your cluster partition.

Running the NCCL test takes approximately five minutes to complete. When the test completes, the system creates and stores an `slurm-JOB_ID.out` file in the `$HOME` directory with the results of your test.




### Bypass the prolog health check for a specific job

You can configure Slurm to submit a job on a compute node but skip the node's [prolog health check](https://docs.cloud.google.com/cluster-director/docs/orchestration#capabilities). This approach is useful in the following scenarios:

  * **Suspected false positives** : you believe that the health check failed due to a false positive after you [troubleshoot the node](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks).

  * **Fault-tolerant workloads** : your workload is designed to be resilient to the specific hardware issue that a health check detected.


**Caution:** Disabling health checks doesn't resolve any underlying hardware issues in your GPUs. If the node is unhealthy, then your job might fail or produce incorrect results.

To submit a job on a compute node while skipping the prolog health check, complete the following steps:

  1. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  2. If the prolog health check failed, then manually undrain the node if you haven't already:
         
         sudo scontrol update nodename=NODE_NAME state=RESUME
         

Replace NODE_NAME with the name of the node.

  3. Submit a job for the specific node but skip the prolog health check:
         
         sbatch --export=ALL,SLURM_JOB_EXTRA="healthchecks_prolog=off" JOB_SCRIPT
         

Replace JOB_SCRIPT with the path to the job that you want to run.




## What's next

  * [Troubleshoot errors in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors)

  * [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks)

  * [View audit logs](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
