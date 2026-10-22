---
url: https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms/
title: Benchmark higher network bandwidth for VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:44.519476+00:00
---

# Benchmark higher network bandwidth for VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmark higher network bandwidth for VM instances Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to test per VM Tier_1 networking performance by creating two VMs and streaming traffic back and forth to observe network performance. To take advantage of this feature, you must create your VM with [operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that support the [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). Per VM Tier_1 networking performance requires larger VM sizes, so confirm you have enough [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) to create the VMs.

## Before you begin

  * Ensure that you are using a public [image that supports gVNIC](https://docs.cloud.google.com/compute/docs/images/os-details#networking) or [create a custom image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create-custom-image) in your project. 
  * Verify that you created VPC firewall rules to allow ingress on port TCP:5001, or another port of your choosing, to allow for `iperf` performance testing. 
  * Use iPerf version 2, not version 3, to perform the benchmarking.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Setting up VMs for benchmarking

Create two `n2-standard-64` vCPU machines with per VM Tier_1 networking performance enabled and the highest [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) setting. This gives your VMs up to 75 Gbps of maximum egress bandwidth (using internal IPs).

**Note:** To benchmark the egress for external IP addresses, you will need to associate external IP addresses with the VMs, and use those IP addresses as the target during testing.

###  gcloud 

  1. To create an image, use the [gcloud compute images create command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create).
         
         gcloud compute images create IMAGE_NAME \
            --project=PROJECT_ID \
            --source-image-family=SOURCE_IMAGE_FAMILY \
            --source-image-project=SOURCE_IMAGE_PROJECT \
            --guest-os-features=GVNIC
         

Replace the following:

     * PROJECT_ID: the name of your project.
     * IMAGE_NAME: the name of the image that you want to create.
     * SOURCE_IMAGE_FAMILY: required version of a public image. For this test, use `ubuntu-2004-lts`.
     * SOURCE_IMAGE_PROJECT: the name of the project that contains the source image. For this test, use `ubuntu-os-cloud`.

**Example**
    
    gcloud compute images create benchmark-image-test \
      --project=my-project \
      --source-image-family=ubuntu-2004-lts \
      --source-image-project=ubuntu-os-cloud \
      --guest-os-features=GVNIC
    

  2. Create an auto mode VPC network that uses the maximum MTU setting:
         
         gcloud compute networks create NETWORK_NAME \
           --project=PROJECT_ID \
           --subnet-mode=AUTO --mtu=8896
         

Replace the following:

     * PROJECT_ID: the name of your project.
     * NETWORK_NAME: a name for the network.
  3. Create two identical instances:
         
         gcloud compute instances create \
               VM_NAME_1 VM_NAME_2 \
               --project=PROJECT_ID \
               --zone=ZONE \
               --machine-type=n2-standard-64 \
               --image=projects/PROJECT_ID/global/images/IMAGE_NAME \
               --network-interface=network=NETWORK_NAME,nic-type=GVNIC \
               --network-performance-configs=total-egress-bandwidth-tier=TIER_1
         

Replace the following:

     * VM_NAME_1, VM_NAME_2: the names of the VM instances that you want to create.
     * PROJECT_ID: your project name.
     * ZONE: your VM's zone. Both VMs must reside in the same zone.
     * PROJECT_NAME/global/images/IMAGE_NAME: your project name and the image name.
     * NETWORK_NAME: the name of the network you configured with the maximum MTU setting.



## Performing the benchmark

Your two VMs must reside in the same zone and on the same [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). During the benchmark, these two VMs conduct bi-directional testing of the VPC network path.

### Verify the MTU setting

Confirm the Virtual Private Cloud (VPC) network has the maximum MTU setting configured by using `ifconfig` in the guest OS of one of the VMs.

  1. [Connect to one of the VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

  2. In the terminal window, run the following command:
         
         /sbin/ifconfig | grep mtu
         

The reported MTU should be 8896.
         
         ens4: flags=4163  mtu 8896
          lo: flags=73  mtu 65536
         




### Verify the VM configuration

Confirm the virtual machines have Tier_1 networking enabled by examining the virtual machine properties.

###  gcloud 

To view the instances, use the [gcloud compute instances describe command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe).
    
    
    gcloud compute instances describe VM_NAME_1 \
        --project=PROJECT_ID \
        --zone=ZONE \
        --format="text(networkPerformanceConfig)"
    
    
    
    gcloud compute instances describe VM_NAME_2 \
        --project=PROJECT_ID \
        --zone=ZONE \
        --format="text(networkPerformanceConfig)"
    

Replace the following:

  * VM_NAME_1: the names of the VM instance that you want to view.
  * VM_NAME_2: the names of the VM instance that you want to view.
  * PROJECT_ID: your project name.
  * ZONE: your VM's zone. Both VMs must reside in the same zone.



In the response you should see the following:

`networkPerformanceConfig.totalEgressBandwidthTier: TIER_1`

### Use iPerf to perform the benchmark on Debian-based systems

**Note:** Ensure that you are using iPerf version 2 and not version 3; iPerf version 3 does not support multi-threading (by design) and can have performance implications in your results when running multiple streams.

###  gcloud 

  1. If you haven't already done so, complete the steps in Setting up VMs for benchmarking.

  2. After both VMs are running, use SSH to connect to one of the VMs.
         
         gcloud compute ssh VM_NAME_1 \
           --project=PROJECT_ID
         

Replace the following:

     * VM_NAME_1: the name of your first VM.
     * PROJECT_ID: your project name.
  3. On the first VM, complete the following steps:

     1. Install `iperf`.
            
            sudo apt-get update && sudo apt-get install iperf
            

     2. Get the internal IP address for this VM. Make note of the internal IP address for later use.
            
            ip a
            

     3. Start up the iPerf server.
            
            iperf -s
            

This starts up a server listening for connections in order to perform the benchmark. Leave the iPerf server running for the duration of the test.

  4. In a separate client terminal, connect to the second VM using SSH.
         
         gcloud compute ssh VM_NAME_2 \
            --project=PROJECT_ID
         

Replace the following:

     * VM_NAME_2: the name of your second VM.
     * PROJECT_ID: your project name.
  5. On the second VM, complete the following steps:

     1. Install iPerf.
            
            sudo apt-get update && sudo apt-get install iperf
            

     2. Run the iperf test and specify the first VM's IP address as the target.

**Note:** The order of the arguments is important.
            
            iperf -t 30 -c internal_ip_of_instance_1 -P 16
            

This executes a 30-second test. If iPerf is not able to reach the other VM you, might need to adjust the network or [firewall settings](https://docs.cloud.google.com/vpc/docs/using-firewalls) on the VMs or perhaps in the Google Cloud console.

Your results should look something like the following example. It shows the 75 Gbps egress bandwidth limit for `n2-standard-64` with [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) enabled, exceeding the default 32 Gbps egress bandwidth limit.
            
            ------------------------------------------------------------
            Client connecting to 10.128.0.10, TCP port 5001
            TCP window size: 1.59 MByte (default)
            ------------------------------------------------------------
            [ 12] local 10.128.0.11 port 57722 connected with 10.128.0.10 port 5001
            [ 11] local 10.128.0.11 port 57720 connected with 10.128.0.10 port 5001
            [ 16] local 10.128.0.11 port 57730 connected with 10.128.0.10 port 5001
            [  6] local 10.128.0.11 port 57710 connected with 10.128.0.10 port 5001
            [ 13] local 10.128.0.11 port 57724 connected with 10.128.0.10 port 5001
            [  8] local 10.128.0.11 port 57712 connected with 10.128.0.10 port 5001
            [  9] local 10.128.0.11 port 57716 connected with 10.128.0.10 port 5001
            [ 14] local 10.128.0.11 port 57726 connected with 10.128.0.10 port 5001
            [ 15] local 10.128.0.11 port 57728 connected with 10.128.0.10 port 5001
            [ 10] local 10.128.0.11 port 57718 connected with 10.128.0.10 port 5001
            [  4] local 10.128.0.11 port 57706 connected with 10.128.0.10 port 5001
            [  5] local 10.128.0.11 port 57708 connected with 10.128.0.10 port 5001
            [  3] local 10.128.0.11 port 57704 connected with 10.128.0.10 port 5001
            [ 17] local 10.128.0.11 port 57732 connected with 10.128.0.10 port 5001
            [  7] local 10.128.0.11 port 57714 connected with 10.128.0.10 port 5001
            [ 18] local 10.128.0.11 port 57734 connected with 10.128.0.10 port 5001
            [ ID] Interval       Transfer     Bandwidth
            [ 12]  0.0-30.0 sec  7.63 GBytes  2.19 Gbits/sec
            [ 11]  0.0-30.0 sec  17.7 GBytes  5.07 Gbits/sec
            [ 16]  0.0-30.0 sec  9.15 GBytes  2.62 Gbits/sec
            [  6]  0.0-30.0 sec  43.8 GBytes  12.6 Gbits/sec
            [ 13]  0.0-30.0 sec  23.6 GBytes  6.76 Gbits/sec
            [  8]  0.0-30.0 sec  13.3 GBytes  3.80 Gbits/sec
            [  9]  0.0-30.0 sec  9.29 GBytes  2.66 Gbits/sec
            [ 14]  0.0-30.0 sec  19.6 GBytes  5.62 Gbits/sec
            [ 15]  0.0-30.0 sec  12.5 GBytes  3.58 Gbits/sec
            [ 10]  0.0-30.0 sec  11.1 GBytes  3.19 Gbits/sec
            [  4]  0.0-30.0 sec  19.0 GBytes  5.43 Gbits/sec
            [  5]  0.0-30.0 sec  7.32 GBytes  2.10 Gbits/sec
            [  3]  0.0-30.0 sec  8.78 GBytes  2.51 Gbits/sec
            [ 17]  0.0-30.0 sec  17.5 GBytes  5.02 Gbits/sec
            [  7]  0.0-30.0 sec  33.4 GBytes  9.57 Gbits/sec
            [ 18]  0.0-30.0 sec  7.64 GBytes  2.19 Gbits/sec
            [SUM]  0.0-30.0 sec   261 GBytes  74.9 Gbits/sec
            




## Remove resources after benchmark testing

Remove the resources you created during the benchmark testing to avoid charges for the image and additional VMs.

###  gcloud 

  1. Use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) to remove the instances you created for benchmark testing.
         
         gcloud compute instances delete \
           VM_NAME_1 VM_NAME_2 \
            --project=PROJECT_ID \
            --zone=ZONE
         

Replace the following:

     * VM_NAME_1, VM_NAME_2: the names of the two VM instances that you want to delete.
     * PROJECT_ID: your project name.
     * ZONE: your VM's zone. Both VMs should be in the same zone.
  2. Use the [`gcloud compute networks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/delete) to remove the network you created for benchmark testing.
         
         gcloud compute networks delete NETWORK_NAME  \
            --project=PROJECT_ID
         

Replace the following:

     * NETWORK_NAME: the name of the network that you want to delete.
     * PROJECT_ID: your project name.
  3. Use the [`gcloud compute images delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/delete) to remove the image you created for benchmark testing.
         
         gcloud compute images delete IMAGE_NAME  \
             --project=PROJECT_ID
         

Replace the following:

     * IMAGE_NAME: the name of the image that you want to delete.
     * PROJECT_ID: your project name.



## What's next

  * Learn about [Tier_1 networking pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing).
  * Review [bandwidth tiers](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) for additional machine types.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
