---
url: https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus/
title: Use higher network bandwidth \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:35.084310+00:00
---

# Use higher network bandwidth  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use higher network bandwidth Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create A2, G2 and N1 instances that use higher network bandwidths. To learn how to use higher network bandwidths for other accelerator-optimized machine series, see [Create high bandwidth GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#create_high_bandwidth_machines).

You can use higher network bandwidths, of 100 Gbps or more, to improve the performance of distributed workloads running on your GPU VMs. Higher network bandwidths are available for A2, G2 and N1 VMs with attached GPUs on Compute Engine as follows:

  * For N1 general-purpose VMs that have T4 and V100 GPUs attached, you can get a maximum network bandwidth of up to 100 Gbps, based on the combination of GPU and vCPU count.
  * For A2 and G2 accelerator-optimized VMs, you can get a maximum network bandwidth of up to 100 Gbps, based on the machine type.



To review the configurations or machine types that support these higher network bandwidths rates, see [Network bandwidths and GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

For general network bandwidth information on Compute Engine, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

## Overview

To use the higher network bandwidths available to each GPU VM, complete the following recommended steps:

  1. Create your GPU VM by using an OS image that supports Google Virtual NIC (gVNIC).
  2. Optional: Install Fast Socket. Fast Socket improves NCCL performance on 100 Gbps or higher networks by reducing the contention between multiple TCP connections. Some Deep Learning VM Images (DLVM) have Fast Socket preinstalled.



### Use Deep Learning VM Images

You can create your VMs using any GPU supported image from the Deep Learning VM Images project. All GPU supported DLVM images have the GPU driver, ML software, and gVNIC preinstalled. For a list of DLVM images, see [Choosing an image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

If you want to use Fast Socket, you can choose a DLVM image such as: `tf-latest-gpu-debian-10` or `tf-latest-gpu-ubuntu-1804`.

**Caution:** You can't use [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) on boot disks for your VMs that use G2 machine types. G2 machine types are accelerator-optimized machine series that have NVIDIA L4 GPUs attached. 

## Create VMs that use higher network bandwidths

For higher network bandwidths, it is recommended that you enable Google Virtual NIC (gVNIC). For more information, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

To create a VM that has attached GPUs and a higher network bandwidth, complete the following:

  1. Review the [maximum network bandwidth available](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth) for each machine type that has attached GPUs.
  2. Create your GPU VM. The following examples show how to create A2 and N1 with attached V100 VMs.

In these examples, VMs are created by using the Google Cloud CLI. However, you can also use either the [Google Cloud console](https://console.cloud.google.com/) or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest/instances) to create these VMs. For more information about creating GPU VMs, see [Create a VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

###  A2 (A100) 

For example, to create a VM that has a maximum bandwidth of 100 Gbps, has eight A100 GPUs attached, and uses the `tf-latest-gpu` DLVM image, run the following command:
         
         gcloud compute instances create VM_NAME \
          --project=PROJECT_ID \
          --zone=ZONE \
          --machine-type=a2-highgpu-8g \
          --maintenance-policy=TERMINATE --restart-on-failure \
          --image-family=tf-latest-gpu \
          --image-project=deeplearning-platform-release \
          --boot-disk-size=200GB \
          --network-interface=nic-type=GVNIC \
          --metadata="install-nvidia-driver=True,proxy-mode=project_editors" \
          --scopes=https://www.googleapis.com/auth/cloud-platform
         

Replace the following:

     * `VM_NAME`: the name of your VM
     * `PROJECT_ID` : your project ID
     * `ZONE`: the zone for the VM. This zone must support the specified GPU type. For more information about zones, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

###  N1 (V100) 

For example, to create a VM that has a maximum bandwidth of 100 Gbps, has eight V100 GPUs attached, and uses the `tf-latest-gpu` DLVM image, run the following command:
    
    gcloud compute instances create VM_NAME \
     --project PROJECT_ID \
     --custom-cpu 96 \
     --custom-memory 624 \
     --image-project=deeplearning-platform-release \
     --image-family=tf-latest-gpu \
     --accelerator type=nvidia-tesla-v100,count=8 \
     --maintenance-policy TERMINATE \
     --metadata="install-nvidia-driver=True"  \
     --boot-disk-size 200GB \
     --network-interface=nic-type=GVNIC \
     --zone=ZONE
    

  3. If you are not using GPU supported Deep Learning VM Images or Container-Optimized OS, install GPU drivers. For more information, see [Installing GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

  4. Optional: On the VM, Install Fast Socket.

  5. After you set up the VM, you can verify the network bandwidth.

**Note:** To achieve the higher network bandwidth rates, your applications must use multiple network streams.



## Install Fast Socket

NVIDIA Collective Communications Library (NCCL) is used by deep learning frameworks such as TensorFlow, PyTorch, Horovod for multi-GPU and multi-node training.

Fast Socket is a Google proprietary network transport for NCCL. On Compute Engine, Fast Socket improves NCCL performance on 100 Gbps networks by reducing the contention between multiple TCP connections. For more information about working with NCCL, see the [NCCL user guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html).

Current evaluation shows that Fast Socket improves all-reduce throughput by 30%–60%, depending on the message size.

To set up a Fast Socket environment, you can use either a Deep Learning VM Images that has Fast Socket preinstalled, or you can manually install Fast Socket on a Linux VM. To check if Fast Socket is preinstalled, see Verifying that Fast Socket is enabled.

**Note:** Fast Socket is not supported on Windows VMs.

Before you install Fast Socket on a Linux VM, you need to install NCCL. For detailed instructions, see [NVIDIA NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/install-guide/index.html).

###  CentOS/RHEL 

To download and install Fast Socket on a CentOS or RHEL VM, complete the following steps:

  1. Add the package repository and import public keys.
         
         sudo tee /etc/yum.repos.d/google-fast-socket.repo << EOM
         [google-fast-socket]
         name=Fast Socket Transport for NCCL
         baseurl=https://packages.cloud.google.com/yum/repos/google-fast-socket
         enabled=1
         gpgcheck=0
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
               https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         

  2. Install Fast Socket.
         
         sudo yum install google-fast-socket
         

  3. Verify that Fast Socket is enabled.




###  SLES 

To download and install Fast Socket on an SLES VM, complete the following steps:

  1. Add the package repository.
         
         sudo zypper addrepo https://packages.cloud.google.com/yum/repos/google-fast-socket google-fast-socket
         

  2. Add repository keys.
         
         sudo rpm --import https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         

  3. Install Fast Socket.
         
         sudo zypper install google-fast-socket
         

  4. Verify that Fast Socket is enabled.




###  Debian/Ubuntu 

To download and install Fast Socket on a Debian or Ubuntu VM, complete the following steps:

  1. Install the public repository GPG key to `/etc/apt/keyrings`:
         
         sudo curl https://packages.cloud.google.com/apt/doc/apt-key.gpg -o /etc/apt/keyrings/google-fast-socket-keyring.gpg
         

  2. Add the package repository:
         
         echo "deb [signed-by=/etc/apt/keyrings/google-fast-socket-keyring.gpg] https://packages.cloud.google.com/apt google-fast-socket main" | sudo tee /etc/apt/sources.list.d/google-fast-socket.list
         

  3. Install Fast Socket.
         
         sudo apt update && sudo apt install google-fast-socket
         

  4. Verify that Fast Socket is enabled.




### Verifying that Fast Socket is enabled

On your VM, complete the following steps:

  1. Locate the NCCL home directory.
         
         sudo ldconfig -p | grep nccl

For example, on a DLVM image, you get the following output:
         
         libnccl.so.2 (libc6,x86-64) => /usr/local/nccl2/lib/libnccl.so.2
         libnccl.so (libc6,x86-64) => /usr/local/nccl2/lib/libnccl.so
         libnccl-net.so (libc6,x86-64) => /usr/local/nccl2/lib/libnccl-net.so

This shows that the NCCL home directory is `/usr/local/nccl2`.

  2. Check that NCCL loads the Fast Socket plugin. To check, you need to download the NCCL test package. To download the test package, run the following command:
         
         git clone https://github.com/NVIDIA/nccl-tests.git && \
         cd nccl-tests && make NCCL_HOME=NCCL_HOME_DIRECTORY

Replace `NCCL_HOME_DIRECTORY` with the NCCL home directory.

  3. From the `nccl-tests` directory, run the `all_reduce_perf` process:
         
         NCCL_DEBUG=INFO build/all_reduce_perf

If Fast Socket is enabled, the `FastSocket plugin initialized` message displays in the output log.
         
         # nThread 1 nGpus 1 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 5 iters: 20 validation: 1
         #
         # Using devices
         #   Rank  0 Pid  63324 on fast-socket-gpu device  0 [0x00] Tesla V100-SXM2-16GB
         .....
         fast-socket-gpu:63324:63324 [0] NCCL INFO NET/FastSocket : Flow placement enabled.
         fast-socket-gpu:63324:63324 [0] NCCL INFO NET/FastSocket : queue skip: 0
         fast-socket-gpu:63324:63324 [0] NCCL INFO NET/FastSocket : Using [0]ens12:10.240.0.24
         **fast-socket-gpu:63324:63324 [0] NCCL INFO NET/FastSocket plugin initialized**
         ......
         




## Benchmark NCCL performance

When optimizing GPU performance for distributed workloads, benchmarking the NVIDIA Collective Communications Library (NCCL) is essential. NCCL performance is measured by bus bandwidth (`busbw`), typically using the `all_reduce_perf` test.

### Expected NCCL performance for A3 High and A3 Mega VMs

The following table provides expected NCCL bus bandwidth metrics for A3 High and A3 Mega VMs in a two node test that use a 1 GB to 8 GB message size.

Machine type | Number of nodes | Expected `all_reduce_perf` bus bandwidth (GBps)  
---|---|---  
A3 High | 2 | > 80 GBps  
A3+ Mega | 2 | > 160 GBps  
  
As you add more VMs to the collective operation, the bus bandwidth typically decreases. For example, a 4-node A3+ cluster might achieve 130-140 GBps.

### Run NCCL `all-reduce` performance test

Use `mpirun` to run the `all_reduce_perf` benchmark across multiple nodes.

  1. Complete the following prerequisites:

     * On each node, download and compile `nccl-tests`. For more information, see Verifying that Fast Socket is enabled.
     * Create a `hostfile`, listing the nodes and specifying 8 GPUs per node.

A hostfile is a text file that tells `mpirun` which nodes to use and how many processes to run on each node. To create one, make a text file in your working directory that lists one node per line, specifying the hostname or IP address, followed by `slots=8`. For example, to create a hostfile named `my-hostfile` for nodes `node-1` and `node-2`, add the following lines to `my-hostfile`:
    
    node-1 slots=8
    node-2 slots=8
    

  2. Run the test. The following command runs the `all-reduce-perf` test across two nodes, 16 total processes.
         
         mpirun -x LD_LIBRARY_PATH --hostfile HOSTFILE_NAME \
         -n 16 ./build/all_reduce_perf -b 1G -e 8G -f 2 -g 8
         

Replace `HOSTFILE_NAME` with the name of the `hostfile` that you created in the previous step. For example, `my-hostfile`.

     * `-n 16`: Total number of MPI processes, calculated as nodes multiplied by GPUs per node.
     * `-b 1G -e 8G`: Message size range.
     * `-f 2`: Multiplier for message size at each step.
     * `-g 8`: Number of GPUs per process.



## Check network bandwidth

This section explains how to check network bandwidth for A3 Mega, A3 High, A3 Edge, A2, G2 and N1 instances. When working with high bandwidth GPUs, you can use a network traffic tool, such as iperf2, to measure the networking bandwidth.

To check bandwidth speeds, you need at least two VMs that have attached GPUs and can both support the bandwidth speed that you are testing.

Use iPerf to perform the benchmark on Debian-based systems.

**Note:** Ensure that you are using iPerf version 2 and not version 3; iPerf version 3 does not support multi-threading (by design) and can have performance implications in your results when running multiple streams.

  1. Create two VMs that can support the required bandwidth speeds.

  2. Once both VMs are running, use SSH to connect to one of the VMs.
         
         gcloud compute ssh VM_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `VM_NAME`: the name of the first VM
     * `PROJECT_ID`: your project ID
  3. On the first VM, complete the following steps:

     1. Install `iperf`.
            
            sudo apt-get update && sudo apt-get install iperf
            

     2. Get the internal IP address for this VM. Keep track of it by writing it down.
            
            ip a
            

     3. Start up the iPerf server.
            
            iperf -s
            

This starts up a server listening for connections in order to perform the benchmark. Leave this running for the duration of the test.

  4. From a new client terminal, connect to the second VM using SSH.
         
         gcloud compute ssh VM_NAME \
            --project=PROJECT_ID
         

Replace the following:

     * `VM_NAME`: the name of the second VM
     * `PROJECT_ID`: your project ID
  5. On the second VM, complete the following steps:

     1. Install iPerf.
            
            sudo apt-get update && sudo apt-get install iperf
            

     2. Run the iperf test and specify the first VM's IP address as the target.

**Note:** The order of the arguments is important.
            
            iperf -t 30 -c internal_ip_of_instance_1 -P 16
            

This executes a 30-second test and produces a result that resembles the following output. If iPerf is not able to reach the other VM you, might need to adjust the network or [firewall settings](https://docs.cloud.google.com/vpc/docs/using-firewalls) on the VMs or perhaps in the Google Cloud console.




When you use the maximum available bandwidth of 100 Gbps or 1000 Gbps (A3 Mega, A3 High, or A3 Edge), keep the following considerations in mind:

  * Due to packet header overheads for network protocols such as Ethernet, IP, and TCP on the virtualization stack, the throughput, as measured by `netperf`, saturates at around 90 Gbps or 800 Gbps (A3 Mega, A3 High, or A3 Edge). Generally known as [goodput](https://wikipedia.org/wiki/Goodput).

TCP is able to achieve the 100 or 1000 Gbps network speed. Other protocols, such as UDP, are slower.

  * Due to factors such as protocol overhead and network congestion, end-to-end performance of data streams might be slightly lower.

  * You need to use multiple TCP streams to achieve maximum bandwidth between VM instances. Google recommends 4 to 16 streams. At 16 flows you'll frequently maximize the throughput. Depending on your application and software stack, you might need to adjust settings for your application or your code to set up multiple streams.




## What's next?

  * To monitor GPU performance, see [Monitoring GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).
  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
