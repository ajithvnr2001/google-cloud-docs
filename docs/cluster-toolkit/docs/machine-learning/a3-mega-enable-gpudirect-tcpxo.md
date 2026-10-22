---
url: https://docs.cloud.google.com/cluster-toolkit/docs/machine-learning/a3-mega-enable-gpudirect-tcpxo/
title: Enable GPUDirect-TCPXO optimized NCCL communication \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:57.153349+00:00
---

# Enable GPUDirect-TCPXO optimized NCCL communication  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/machine-learning/a3-mega-enable-gpudirect-tcpxo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Enable GPUDirect-TCPXO optimized NCCL communication Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of how to enable GPUDirect-TCPXO for optimizing communication in multi-node workloads, such as ML training, by using [NCCL tests](https://github.com/NVIDIA/nccl-tests) to measure NCCL collective performance between two nodes of an A3 Mega `a3-megagpu-8g` Slurm cluster.

## Before you begin

You must have an A3 Mega Slurm cluster that you created by using Cluster Toolkit version `v1.51.1` or later. To create the cluster, see [Deploy an A3 Mega Slurm cluster for ML training](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster). A3 Mega Slurm clusters that are created by using Cluster Toolkit version `1.39.0` or later have automatic integration of topology-aware scheduling.

## Network components

The following components are used to optimize the network performance for your `a3-megagpu-8g` Slurm cluster.

GPUDirect-TCPXO
    GPUDirect-TCPXO is a custom, remote direct memory access (RDMA) networking stack that increases the network performance of your Compute Engine instances by allowing data packet payloads to transfer directly from GPU memory to the network interface without having to go through the CPU and system memory. `a3-megagpu-8g` instances can use GPUDirect-TCPXO combined with [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) to deliver higher throughput between compute instances in a cluster when compared to the A2 accelerator-optimized machine types on Google Cloud.
The Receive Data Path Manager
    

To achieve optimal application performance, an additional service called the Receive Data Path Manager (RxDM) runs alongside the applications that use GPUDirect-TCPXO.

Additionally, you must install a NCCL net plugin into the execution environment of the workload. A PyTorch Docker image distributes both the RxDM and the plugin.

The cluster deployment blueprint
    

The [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml) blueprint includes a Slurm _prolog_ and _epilog_ script that runs before and after every job running on more than one `a3-megagpu-8g` compute node.

The prolog performs the following actions:

  * Checks that the `import-helper` kernel module is loaded.
  * Installs the NCCL net plugin into `/var/lib/tcpxo/lib64/` of the host.
  * Runs the RxDM service, which is a long-lived service that runs alongside the job. Starting the RxDM can take 10-20 seconds, which blocks the start of the job until the RxDM service is initialized. While the RxDM is starting up, you won't see the slurm job `output/error` logs.



The epilog performs the following actions:

  * Stops the RxDM service.
  * Prunes any stopped containers and frees up disk space.



For more information about prolog and epilog actions, see the [Slurm documentation](https://slurm.schedmd.com/prolog_epilog.html).

Use GPUDirect-TCPXO with single-node Slurm jobs
    

By default, Slurm only launches the RxDM container for multi-node jobs on A3 instances. RxDM is not required for single-node training performance. However, if your job script enables the GPUDirect-TCPXO NCCL plugin, the plugin attempts to connect to RxDM and fails with a timeout error. To resolve this issue, you can choose from the following options:

  * Modify job scripts for single-node jobs: For jobs that run on a single node, disable the GPUDirect-TCPXO plugin to prevent the timeout. In your job script, set the `NCCL_NET_PLUGIN` environment variable to `none` to disable the plugin. We recommend that you set environment variables at the beginning of your job script. For example, add the following line at the start of your script:
        
        export NCCL_NET_PLUGIN=none
        

With this setting, NCCL falls back to a different network plugin that doesn't require RxDM. For an example of how to define environment variables, see the `run-nccl-tests.sh` script.

  * Enable RxDM for all jobs: If you frequently switch between single-node and multi-node jobs and prefer a consistent configuration, modify the Slurm prolog script on your controller node. This script, located at `/opt/apps/adm/slurm/scripts/rxdm`, contains the logic for launching RxDM. Update this script to configure it to start the RxDM container for all jobs, regardless of the node count. This configuration makes the use of the GPUDirect-TCPXO plugin transparent to your job scripts.




## Connect to the A3 Mega Slurm cluster

To turn on optimized NCCL communication tuning on your cluster, you must sign in to the Slurm login node. To sign in, you can use either Google Cloud console or Google Cloud CLI.

###  Console 

  1. Go to the **Compute Engine** > **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Locate the login node. The node has a name similar to `a3mega-login-001`.

  3. From the **Connect** column of the login node, click **SSH**.




###  gcloud 

To connect to the login node, use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).
    
    
    gcloud compute ssh $(gcloud compute instances list --filter "name ~ login" --format "value(name)") \
      --tunnel-through-iap \
      --zone ZONE
    

## Create an enroot container

From the login node on your cluster, import a Pytorch image from the [NVIDIA container registry](https://catalog.ngc.nvidia.com/containers).

To import the PyTorch image, use the Slurm `srun` command from the login node:
    
    
    srun -N 1 enroot import docker://nvcr.io#nvidia/pytorch:24.04-py3

This runs on one of your `a3-megagpu-8g` nodes that has more CPU and memory than the login node, which enroot can use to more quickly import the container. When the import completes, you should have a file named `nvidia+pytorch+24.04-py3.sqsh` in the directory where you ran the command.

## Build NCCL test

Next, build the NCCL-test binaries by running the following command from the same directory as the previous step:
    
    
    CONTAINER_IMAGE=./nvidia+pytorch+24.04-py3.sqsh
    
    git clone https://github.com/NVIDIA/nccl-tests.git
    
    srun --partition a3mega \
          --ntasks-per-node=1 \
          --gpus-per-node=8 \
          --container-mounts="$PWD:/nccl" \
          --container-image=${CONTAINER_IMAGE} \
          bash -c "
              cd /nccl/nccl-tests/ &&
              MPI=1 CC=mpicc CXX=mpicxx make -j
            "
    

This creates a directory named `nccl-tests`. The preceding command uses `--container-mounts` to mount your current working directory `$PWD` into the `/nccl` directory inside the container. After the `srun` command finishes, verify that the `nccl-tests/build` folder contains several binaries, including `all_gather_perf`.

## Run a NCCL test

As part of the cluster deployment process, Slurm prolog and epilog scripts are installed that automatically install a custom `libnccl-net.so` library and start a sidecar process to enable GPUDirect-TCPXO optimized communication.

To run any job on an A3 Mega cluster, you must set several environment variables to turn on high-performance networking with GPUDirect-TCPXO. Because you use enroot containers in this procedure to launch workloads, you must set these variables in the container environment instead of the host environment.

**Note:** The GPUDirect-TCPXO NCCL plugin is internally referred to as FasTrak. You might see this name in environment variables and configuration files.

To run the NCCL test, complete the following steps.

  1. Use a text editor to create a file named `run-nccl-tests.sh` and add the following content to the file.

**Note:** You can also add `export NCCL_NET=FasTrak`. This causes the process to fail if any of the configuration are not set properly.
         
         #!/bin/bash
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         #SBATCH --partition=a3mega
         #SBATCH --mem=0
         #SBATCH -N 2
         #SBATCH --gpus-per-node=8
         #SBATCH --ntasks-per-node=8
         
         # Usage: sbatch run-nccl-tests.sh
         
         set -x
         # This should be set to the squashfs file that you created for your application
         CONTAINER_IMAGE=./nvidia+pytorch+24.04-py3.sqsh
         
         # Set up NCCL Environment variables
         # The following two can be useful for debugging
         # export NCCL_DEBUG=INFO
         # export NCCL_DEBUG_SUBSYS=INIT,NET
         
         # These parameters should not be modified
         NCCL_LIB_DIR="/var/lib/tcpxo/lib64" source /var/lib/tcpxo/lib64/nccl-env-profile.sh
         export NCCL_FASTRAK_CTRL_DEV=enp0s12
         export NCCL_FASTRAK_IFNAME=enp6s0,enp7s0,enp13s0,enp14s0,enp134s0,enp135s0,enp141s0,enp142s0
         export NCCL_SOCKET_IFNAME=enp0s12
         export NCCL_FASTRAK_LLCM_DEVICE_DIRECTORY=/dev/aperture_devices
         
         # Here we grab all the environment variables that need to be
         # passed down into the container. Slurm would otherwise only pass these env vars
         # to the job environment on the host.
         # shellcheck disable=SC2001
         HOST_VARS=$(sed 's/ \{1,\}/,/g' <<<"${!NCCL*}")
         
         # Mount /var/tmp to allow the rest of the enroot container to be read-only, and
         # mount current $PWD to /nccl to for accessing nccl-tests binary
         CONTAINER_MOUNTS="/var/tmp:/var/tmp"
         
         # Mount PWD to /nccl in the enroot container
         CONTAINER_MOUNTS=${CONTAINER_MOUNTS},"$PWD:/nccl"
         
         # Mount required directories for GPUDirect-TCPXO functionality
         CONTAINER_MOUNTS=${CONTAINER_MOUNTS},"/var/lib/tcpxo/lib64/"
         
         # Run the workload
         srun -l \
         	-N "${SLURM_NNODES}" \
         	--mpi=pmi2 \
         	--ntasks-per-node=8 \
         	--container-image="${CONTAINER_IMAGE}" \
         	--container-env="${HOST_VARS}" \
         	--container-mounts="${CONTAINER_MOUNTS}" \
         	sh -c "
           export LD_LIBRARY_PATH=/var/lib/tcpxo/lib64:/usr/lib/x86_64-linux-gnu:\$LD_LIBRARY_PATH;
           /nccl/nccl-tests/build/all_gather_perf -b 8M -e 8G -f 2 -g 1 -w 5 --iters 200;
           "
         

  2. Submit the script.
         
         sbatch run-nccl-tests.sh

This results in a `slurm-XX.out` file that contains the results of the nccl `all_gather_perf` benchmark.

The output is similar to the following:
         
         #
         #                                                              out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
           268435456       4194304     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
           536870912       8388608     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
           1073741824      16777216     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
           2147483648      33554432     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
           4294967296      67108864     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
           8589934592     134217728     float    none      -1    XXXXX  XXX.XX  XXX.XX    N/A   XXXXXX  XXX.XX  XXX.XX    N/A
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : XXX.XX
         #
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
