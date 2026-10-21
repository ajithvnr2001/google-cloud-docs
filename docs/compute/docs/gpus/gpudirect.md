---
url: https://docs.cloud.google.com/compute/docs/gpus/gpudirect/
title: Create an A3 Mega, A3 High, or A3 Edge instance with GPUDirect enabled \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:53.642479+00:00
---

# Create an A3 Mega, A3 High, or A3 Edge instance with GPUDirect enabled  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/gpudirect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an A3 Mega, A3 High, or A3 Edge instance with GPUDirect enabled Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes the setup for A3 Mega, A3 High, or A3 Edge virtual machine (VM) instances that have eight NVIDIA H100 GPUs attached and use either of the following GPUDirect technologies: GPUDirect-TCPX or GPUDirect-TCPXO. To create an A3 High instance with less than 8 GPUs, see [Create an A3 High or A2 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).

The [GPUDirect technology](https://developer.nvidia.com/gpudirect) that you use depends on the A3 machine type that you select.

  * **GPUDirect-TCPXO** : is an RDMA-like, offloaded networking stack that is supported on A3 Mega (`a3-megagpu-8g`) machine types that have eight H100 GPUs.
  * **GPUDirect-TCPX** : is an optimized version of guest TCP that provides lower latency and is supported on A3 High (`a3-highgpu-8g`) and A3 Edge (`a3-edgegpu-8g`) machine types that have eight H100 GPUs.



The [A3 accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) has 208 vCPUs, and up to 1872GB of memory. The `a3-megagpu-8g`, `a3-highgpu-8g`, and `a3-edgegpu-8g` machine types offer 80 GB GPU memory per GPU. These machine types can get up to 1,800 Gbps of network bandwidth, which makes them ideal for large transformer-based language models, databases, and high performance computing (HPC).

Both GPUDirect-TCPX and GPUDirect-TCPXO use NVIDIA GPUDirect technology to increase performance and reduce latency for your A3 VMs. They achieve this by allowing data packet payloads to transfer directly from GPU memory to the network interface, bypassing the CPU and system memory. This is a form of remote direct memory access (RDMA). When combined with Google Virtual NIC (gVNIC), A3 VMs can deliver the highest throughput between VMs in a cluster when compared to the previous generation A2 or G2 accelerator-optimized machine types.

This document describes how to create an A3 Mega, A3 High, or A3 Edge VM and enable either GPUDirect-TCPX or GPUDirect-TCPXO to test the improved GPU network performance.

## Before you begin

  * To review limitations and additional prerequisite steps for creating instances with attached GPUs, such as selecting an OS image and checking GPU quota, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



### Required roles

To get the permissions that you need to create VMs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

To test network performance with GPUDirect, complete the following steps:

  1. Set up one or more Virtual Private Cloud (VPC) networks that have a large MTU configured.
  2. Create your GPU instance.



## Set up VPC networks

To enable efficient communication for your GPU VMs, you need to create a management network and one or more data networks. The management network is used for external access, for example SSH, and for most general network communication. The data networks are used for high-performance communication between the GPUs on different VMs, for example, for Remote Direct Memory Access (RDMA) traffic.

For these VPC networks, we recommend setting the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. Higher MTU values increase the packet size and reduce the packet-header overhead, which increases payload data throughput. For more information about how to create VPC networks, see [Create and verify a jumbo frame MTU network](https://docs.cloud.google.com/vpc/docs/configure-jumbo-frame-mtu-vpc).

#### Create management network, subnet, and firewall rule

Complete the following steps to set up the management network:

  1. Create the management network by using the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create NETWORK_NAME_PREFIX-mgmt-net \
             --project=PROJECT_ID \
             --subnet-mode=custom \
             --mtu=8244
         

  2. Create the management subnet by using the [`networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create NETWORK_NAME_PREFIX-mgmt-sub \
             --project=PROJECT_ID \
             --network=NETWORK_NAME_PREFIX-mgmt-net \
             --region=REGION \
             --range=192.168.0.0/24
         

  3. Create firewall rules by using the [`firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

     1. Create a firewall rule for the management network.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-internal \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=tcp:0-65535,udp:0-65535,icmp \
                --source-ranges=192.168.0.0/16
            

     2. Create the `tcp:22` firewall rule to limit which source IP addresses can connect to your VM by using SSH.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-external-ssh \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=tcp:22 \
                --source-ranges=SSH_SOURCE_IP_RANGE
            

     3. Create the `icmp` firewall rule that can be used to check for data transmission issues in the network.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-external-ping \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=icmp \
                --source-ranges=0.0.0.0/0
            




Replace the following:

  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `PROJECT_ID` : your project ID.
  * `REGION`: the region where you want to create the networks.
  * `SSH_SOURCE_IP_RANGE`: IP range in CIDR format. This specifies which source IP addresses can connect to your VM by using SSH.



#### Create data networks, subnets, and firewall rule

The number of data networks varies depending on the type of GPU machine you are creating.

### A3 Mega

A3 Mega requires eight data networks. To create eight data networks, each with subnets and firewall rules, use the following command.
    
    
    for N in $(seq 1 8); do
    gcloud compute networks create NETWORK_NAME_PREFIX-data-net-$N \
        --project=PROJECT_ID \
        --subnet-mode=custom \
        --mtu=8244
    
    gcloud compute networks subnets create NETWORK_NAME_PREFIX-data-sub-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --region=REGION \
        --range=192.168.$N.0/24
    
    gcloud compute firewall-rules create NETWORK_NAME_PREFIX-data-internal-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --action=ALLOW \
        --rules=tcp:0-65535,udp:0-65535,icmp \
        --source-ranges=192.168.0.0/16
    done
    

### A3 High and A3 Edge

A3 High and A3 Edge require four data networks. Use the following command to create four data networks, each with subnets and firewall rules.
    
    
    for N in $(seq 1 4); do
    gcloud compute networks create NETWORK_NAME_PREFIX-data-net-$N \
        --project=PROJECT_ID \
        --subnet-mode=custom \
        --mtu=8244
    
    gcloud compute networks subnets create NETWORK_NAME_PREFIX-data-sub-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --region=REGION \
        --range=192.168.$N.0/24
    
    gcloud compute firewall-rules create NETWORK_NAME_PREFIX-data-internal-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --action=ALLOW \
        --rules=tcp:0-65535,udp:0-65535,icmp \
        --source-ranges=192.168.0.0/16
    done
    

## Create A3 Mega instances (GPUDirect-TCPXO)

Create your A3 Mega instances by using the [`cos-121-lts`](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) or later Container-Optimized OS image or the [`rocky-linux-8-optimized-gcp-nvidia-580`](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) Rocky Linux image.

###  COS 

To test network performance with GPUDirect-TCPXO, create at least two A3 Mega VM instances. Create each VM by using the `cos-121-lts` or later Container-Optimized OS image and specifying the VPC networks that you created in the previous step.

A3 Mega VMs require nine Google Virtual NIC (gVNIC) network interfaces, one for the management network and eight for the data networks.

Based on the [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) that you want to use to create your VM, select one of the following options:

### Standard
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.



If you want to apply a [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) to your VM, then use the same command with the `--resource-policies` flag. You can only create your VM wihthin the same region as the placement policy.

### Spot
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM on preemption. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`



### Flex-start
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=FLEX_START \
        --instance-termination-action=TERMINATION_ACTION \
        --max-run-duration=RUN_DURATION \
        --request-valid-for-duration=VALID_FOR_DURATION
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of its run duration. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RUN_DURATION`: the maximum time that the VM runs before Compute Engine stops or deletes it. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, a value of `30m` defines a time of 30 minutes, and a value of `1h2m3s` defines a time of one hour, two minutes, and three seconds. You can specify a value between 10 minutes and seven days.
  * `VALID_FOR_DURATION``: the maximum time to wait for provisioning your requested resources. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds: 
    * If your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90s`) and two hours (`2h`). Longer durations give you higher chances of obtaining resources.
    * If the VM can run in any zone within the region, then specify a duration of zero seconds (`0s`). This value specifies that Compute Engine only allocates resources if they are immediately available. If the creation request fails because resources are unavailable, then retry the request in a different zone.



If you want to apply a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to your VM to reduce network latency across VMs, use the same command with the `--resource-policies=RESOURCE_POLICY_NAME` flag.

### Reservation-bound
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --reservation-affinity=specific \
        --reservation=RESERVATION_URL
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of the reservation period. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RESERVATION_URL`: the URL of the reservation that you want to consume. Specify one of the following values: 
    * If you created the reservation in the same project: `RESERVATION_NAME`
    * If the reservation is in a different project, and [ your project can use it](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation): `projects/PROJECT_ID/reservations/RESERVATION_NAME`.



### Install GPU drivers

On each A3 Mega VM, install the GPU drivers.

  1. Install the NVIDIA GPU drivers.
         
         sudo cos-extensions install gpu -- --version=latest
         

  2. Remount the path.
         
         sudo mount --bind /var/lib/nvidia /var/lib/nvidia
         sudo mount -o remount,exec /var/lib/nvidia
         




### Give the NICs access to the GPUs

On each A3 Mega VM, give the NICs access to the GPUs.

  1. Adjust the firewall settings to accept all incoming TCP connections and enable communication between the nodes in your cluster: 
         
         sudo /sbin/iptables -I INPUT -p tcp -m tcp -j ACCEPT

  2. Configure the `dmabuf` module. Load the `import-helper` module, which is part of the `dmabuf` framework. This framework enables high-speed, zero-copy memory sharing between the GPU and the network interface card (NIC), a critical component for GPUDirect technology: 
         
         sudo modprobe import-helper

  3. Configure Docker to authenticate requests to Artifact Registry. 
         
         docker-credential-gcr configure-docker --registries us-docker.pkg.dev

  4. Launch `RxDM` in the container. `RxDM` is a management service that runs alongside the GPU application to manage GPU memory. This service pre-allocates and manages GPU memory for incoming network traffic, which is a key element of GPUDirect technology and essential for high-performance networking. Start a Docker container named `rxdm`: 
         
         docker run --pull=always --rm --detach --name rxdm \
             --network=host  --cap-add=NET_ADMIN  \
             --privileged \
             --volume /var/lib/nvidia:/usr/local/nvidia \
             --device /dev/nvidia0:/dev/nvidia0 \
             --device /dev/nvidia1:/dev/nvidia1 \
             --device /dev/nvidia2:/dev/nvidia2 \
             --device /dev/nvidia3:/dev/nvidia3 \
             --device /dev/nvidia4:/dev/nvidia4 \
             --device /dev/nvidia5:/dev/nvidia5 \
             --device /dev/nvidia6:/dev/nvidia6 \
             --device /dev/nvidia7:/dev/nvidia7 \
             --device /dev/nvidia-uvm:/dev/nvidia-uvm \
             --device /dev/nvidiactl:/dev/nvidiactl \
             --device /dev/dmabuf_import_helper:/dev/dmabuf_import_helper \
             --env LD_LIBRARY_PATH=/usr/local/nvidia/lib64 \
             us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/tcpgpudmarxd-dev:v1.0.21 \
             --num_hops=2 --num_nics=8

To verify that `RxDM` has successfully started, run the command. Wait for the message "Buffer manager initialization complete" to confirm successful `RxDM` initialization.
         
         docker container logs --follow  rxdm

Alternatively, check the `RxDM` initialization completion log.
         
         docker container logs rxdm 2>&1 | grep "Buffer manager initialization complete"




### Set up NCCL environment

On each A3 Mega VM, complete the following steps:

  1. Install the `nccl-net` library, a plugin for NCCL that enables GPUDirect communication over the network. The following command pulls the installer image and installs the necessary library files into `/var/lib/tcpxo/lib64/`. 
         
         NCCL_NET_IMAGE="us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-dev:v1.0.15"
         
         docker run --pull=always --rm --privileged \
             --network=host --cap-add=NET_ADMIN \
             --volume /var/lib/nvidia:/usr/local/nvidia  \
             --volume /var/lib:/var/lib \
             --device /dev/nvidia0:/dev/nvidia0   \
             --device /dev/nvidia1:/dev/nvidia1  \
             --device /dev/nvidia2:/dev/nvidia2  \
             --device /dev/nvidia3:/dev/nvidia3  \
             --device /dev/nvidia4:/dev/nvidia4  \
             --device /dev/nvidia5:/dev/nvidia5  \
             --device /dev/nvidia6:/dev/nvidia6  \
             --device /dev/nvidia7:/dev/nvidia7  \
             --device /dev/nvidia-uvm:/dev/nvidia-uvm  \
             --device /dev/nvidiactl:/dev/nvidiactl  \
             --device /dev/dmabuf_import_helper:/dev/dmabuf_import_helper  \
             --env LD_LIBRARY_PATH=/usr/local/nvidia/lib64:/var/lib/tcpxo/lib64 \
             ${NCCL_NET_IMAGE} install  --install-nccl
         
         sudo mount --bind /var/lib/tcpxo /var/lib/tcpxo && sudo mount -o remount,exec /var/lib/tcpxo
         

  2. Launch a dedicated container `nccl-tests` for NCCL testing. This container comes pre-configured with the necessary tools and utility scripts, ensuring a clean and consistent environment for verifying GPUDirect setup performance. 

This command reuses the `NCCL_NET_IMAGE` variable that you set in the previous step.
         
         docker run --pull=always --rm --detach --name nccl \
             --network=host --cap-add=NET_ADMIN \
             --privileged \
             --volume /var/lib/nvidia:/usr/local/nvidia  \
             --volume /var/lib/tcpxo:/var/lib/tcpxo \
             --shm-size=8g \
             --device /dev/nvidia0:/dev/nvidia0 \
             --device /dev/nvidia1:/dev/nvidia1 \
             --device /dev/nvidia2:/dev/nvidia2 \
             --device /dev/nvidia3:/dev/nvidia3 \
             --device /dev/nvidia4:/dev/nvidia4 \
             --device /dev/nvidia5:/dev/nvidia5 \
             --device /dev/nvidia6:/dev/nvidia6 \
             --device /dev/nvidia7:/dev/nvidia7 \
             --device /dev/nvidia-uvm:/dev/nvidia-uvm \
             --device /dev/nvidiactl:/dev/nvidiactl \
             --device /dev/dmabuf_import_helper:/dev/dmabuf_import_helper \
             --env LD_LIBRARY_PATH=/usr/local/nvidia/lib64:/var/lib/tcpxo/lib64 \
             ${NCCL_NET_IMAGE} daemon




### Run nccl-tests benchmark

To run the nccl-tests benchmark on a single A3 Mega VM, complete the following steps:

  1. Open an interactive bash shell inside the `nccl-tests` container. 
         
         docker exec -it nccl bash

From inside the `nccl-tests` container's bash shell, complete the following steps.

     1. Configure the environment for a multi-node run by setting up SSH and generating host files. Replace `VM_NAME_1` and `VM_NAME_2` with the names of each VM. 
            
            /scripts/init_ssh.sh VM_NAME_1 VM_NAME_2
            /scripts/gen_hostfiles.sh VM_NAME_1 VM_NAME_2
              

This creates a directory named `/scripts/hostfiles2`.

     2. Run the `all_gather_perf` benchmark to measure collective communication performance: 
            
            /scripts/run-nccl-tcpxo.sh all_gather_perf "${LD_LIBRARY_PATH}" 8 eth1,eth2,eth3,eth4,eth5,eth6,eth7,eth8 1M 512M 3 2 10 8 2 10




###  Rocky 

To test network performance with GPUDirect-TCPXO, create at least two A3 Mega VM instances. Create each VM by using the `rocky-linux-8-optimized-gcp-nvidia-580` or later Rocky Linux image and specifying the VPC networks that you created in the previous step.

A3 Mega VMs require nine Google Virtual NIC (gVNIC) network interfaces, one for the management network and eight for the data networks.

Based on the [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) that you want to use to create your VM, select one of the following options:

### Standard
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=rocky-linux-8-optimized-gcp-nvidia-580 \
        --image-project=rocky-linux-accelerator-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.



If you want to apply a [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) to your VM, then use the same command with the `--resource-policies` flag. You can only create your VM wihthin the same region as the placement policy.

### Spot
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=rocky-linux-8-optimized-gcp-nvidia-580 \
        --image-project=rocky-linux-accelerator-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM on preemption. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`



### Flex-start
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=rocky-linux-8-optimized-gcp-nvidia-580 \
        --image-project=rocky-linux-accelerator-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=FLEX_START \
        --instance-termination-action=TERMINATION_ACTION \
        --max-run-duration=RUN_DURATION \
        --request-valid-for-duration=VALID_FOR_DURATION
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of its run duration. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RUN_DURATION`: the maximum time that the VM runs before Compute Engine stops or deletes it. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, a value of `30m` defines a time of 30 minutes, and a value of `1h2m3s` defines a time of one hour, two minutes, and three seconds. You can specify a value between 10 minutes and seven days.
  * `VALID_FOR_DURATION`: the maximum time to wait for provisioning your requested resources. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds: 
    * If your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90s`) and two hours (`2h`). Longer durations give you higher chances of obtaining resources.
    * If the VM can run in any zone within the region, then specify a duration of zero seconds (`0s`). This value specifies that Compute Engine only allocates resources if they are immediately available. If the creation request fails because resources are unavailable, then retry the request in a different zone.



If you want to apply a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to your VM to reduce network latency across VMs, use the same command with the `--resource-policies=RESOURCE_POLICY_NAME` flag.

### Reservation-bound
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-megagpu-8g \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --image-family=rocky-linux-8-optimized-gcp-nvidia-580 \
        --image-project=rocky-linux-accelerator-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-5,subnet=NETWORK_NAME_PREFIX-data-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-6,subnet=NETWORK_NAME_PREFIX-data-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-7,subnet=NETWORK_NAME_PREFIX-data-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-8,subnet=NETWORK_NAME_PREFIX-data-sub-8,no-address \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --reservation-affinity=specific \
        --reservation=RESERVATION_URL
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of the reservation period. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RESERVATION_URL`: the URL of the reservation that you want to consume. Specify one of the following values: 
    * If you created the reservation in the same project: `RESERVATION_NAME`
    * If the reservation is in a different project, and [ your project can use it](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation): `projects/PROJECT_ID/reservations/RESERVATION_NAME`.



### Give the NICs access to the GPUs

On each A3 Mega VM, give the NICs access to the GPUs.

  1. Install the prerequisite packages for the `dmabuf` module: 
         
         sudo dnf -y install epel-release kernel-devel-$(uname -r) git
         sudo dnf -y install dkms
           

  2. Install and load the `import-helper` module, which is part of the `dmabuf` framework. This framework enables high-speed, zero-copy memory sharing between the GPU and the network interface card (NIC), a critical component for GPUDirect technology: 
         
         sudo git clone https://github.com/google/dmabuf_importer_helper.git /usr/src/import_helper-1.0
         sudo dkms install import_helper/1.0
         sudo modprobe import_helper
           

  3. Install and configure Docker to authenticate requests to Artifact Registry. 
         
         sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
         sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
         sudo systemctl --now enable docker
         sudo usermod -a -G docker $(whoami)
         curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
           sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
         export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
         sudo dnf install -y \
               nvidia-container-toolkit-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
               nvidia-container-toolkit-base-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
               libnvidia-container-tools-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
               libnvidia-container1-${NVIDIA_CONTAINER_TOOLKIT_VERSION}
         sudo nvidia-ctk runtime configure --runtime=docker
         sudo systemctl restart docker
         gcloud auth configure-docker us-docker.pkg.dev
           

After you run the preceding commands, log out and log back in for the changes to take effect.

  4. Launch `RxDM` in the container. `RxDM` is a management service that runs alongside the GPU application to manage GPU memory. This service pre-allocates and manages GPU memory for incoming network traffic, which is a key element of GPUDirect technology and essential for high-performance networking. Start a Docker container named `rxdm`: 
         
         docker run --pull=always --rm --detach --name rxdm \
             --network=host  --cap-add=NET_ADMIN  \
             --gpus all \
             --privileged \
             --device /dev/dmabuf_import_helper:/dev/dmabuf_import_helper \
             --env LD_LIBRARY_PATH=/usr/lib64  \
             us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/tcpgpudmarxd-dev:v1.0.21 \
             --num_hops=2 --nic_metric_directory=/tmp

To verify that `RxDM` has successfully started, run the following command. Wait for the message "Buffer manager initialization complete" to confirm successful `RxDM` initialization.
         
         docker container logs --follow  rxdm

Alternatively, check the `RxDM` initialization completion log.
         
         docker container logs rxdm 2>&1 | grep "Buffer manager initialization complete"




### Set up NCCL environment

On each A3 Mega VM, complete the following steps:

  1. Install the `nccl-net` library, a plugin for NCCL that enables GPUDirect communication over the network. The following command pulls the installer image and installs the necessary library files into `/var/lib/tcpxo/lib64/`. 
         
         NCCL_NET_IMAGE="us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-dev:v1.0.15"
         
         docker run --pull=always --rm --privileged \
             --network=host --cap-add=NET_ADMIN \
             --volume /var/lib:/var/lib \
             --env LD_LIBRARY_PATH=/usr/lib64:/var/lib/tcpxo/lib64 \
             ${NCCL_NET_IMAGE} install  --install-nccl
         
         sudo mount --bind /var/lib/tcpxo /var/lib/tcpxo && sudo mount -o remount,exec /var/lib/tcpxo
         

  2. Configure the aperture mount flags. 
         
         aperture_mount_flags="";
         while IFS= read -r line; do
             BDF=$( echo "$line" | awk '{print $1}' );
             host_aperture_device="/sys/bus/pci/devices/$BDF"
             # replace '/sys/bus/pci/devices' with '/dev/aperture_devices'
             container_aperture_device="${host_aperture_device/\/sys\/bus\/pci\/devices/\/dev\/aperture_devices}";
             aperture_mount_flags+="--mount type=bind,src=${host_aperture_device},target=${container_aperture_device} ";
         done < <(lspci -nn -D | grep '1ae0:0084')
         

  3. Launch a dedicated container `nccl-tests` for NCCL testing. This container comes pre-configured with the necessary tools and utility scripts, ensuring a clean and consistent environment for verifying GPUDirect setup performance. 

This command reuses the `NCCL_NET_IMAGE` variable that you set in the previous step.
         
         docker run --pull=always --rm --detach --name nccl \
             --network=host --cap-add=NET_ADMIN \
             --privileged \
             --volume /var/lib/:/var/lib  \
             --shm-size=8g \
             --gpus all \
             $aperture_mount_flags \
             --device /dev/dmabuf_import_helper:/dev/dmabuf_import_helper \
             --env LD_LIBRARY_PATH=/usr/lib64:/var/lib/tcpxo/lib64 \
             ${NCCL_NET_IMAGE} daemon




### Run nccl-tests benchmark

To run the nccl-tests benchmark, on a single A3 Mega VM, complete the following steps:

  1. Open an interactive bash shell inside the `nccl-tests` container. 
         
         docker exec -it nccl bash

From inside the `nccl-tests` container's bash shell, complete the following steps.

     1. Configure the environment for a multi-node run by setting up SSH and generating host files. Replace `VM_NAME_1` and `VM_NAME_2` with the names of each VM. 
            
            /scripts/init_ssh.sh VM_NAME_1 VM_NAME_2
            /scripts/gen_hostfiles.sh VM_NAME_1 VM_NAME_2
              

This creates a directory named `/scripts/hostfiles2`.

     2. Run the `all_gather_perf` benchmark to measure collective communication performance: 
            
            /scripts/run-nccl-tcpxo.sh all_gather_perf "${LD_LIBRARY_PATH}" 8 enp134s0,enp135s0,enp13s0,enp14s0,enp141s0,enp142s0,enp6s0,enp7s0 1M 8G 3 2 10 8 2 10 enp0s12




## Create A3 High and Edge instances (GPUDirect-TCPX)

Create your A3 High and Edge instances by using the [`cos-121-lts`](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) or later Container-Optimized OS image.

###  COS 

To test network performance with GPUDirect-TCPX, you need to create at least two A3 High or Edge VMs. Create each VM by using the `cos-121-lts` or later Container-Optimized OS image and specifying the VPC networks that you created in the previous step.

The VMs must use the Google Virtual NIC (gVNIC) network interface. For A3 High or Edge VMs, you must use gVNIC driver version 1.4.0rc3 or later. This driver version is available on the Container-Optimized OS. The first virtual NIC is used as the primary NIC for general networking and storage. The other four virtual NICs are NUMA aligned with two of the eight GPUs on the same PCIe switch.

Based on the [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) that you want to use to create your VM, select one of the following options:

### Standard
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address
    

Replace the following:

  * `VM_NAME`: the name of your VM.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `MACHINE_TYPE`: the machine type for the VM. Specify either `a3-highgpu-8g` or `a3-edgegpu-8g`.
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.



If you want to apply a [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) to your VM, then use the same command with the `--resource-policies` flag. You can only create your VM wihthin the same region as the placement policy.

### Spot
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `VM_NAME`: the name of your VM.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `MACHINE_TYPE`: the machine type for the VM. Specify either `a3-highgpu-8g` or `a3-edgegpu-8g`.
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM on preemption. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`



### Flex-start
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --provisioning-model=FLEX_START \
        --instance-termination-action=TERMINATION_ACTION \
        --max-run-duration=RUN_DURATION \
        --request-valid-for-duration=VALID_FOR_DURATION
    

Replace the following:

  * `VM_NAME`: the name of your VM.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `MACHINE_TYPE`: the machine type for the VM. Specify either `a3-highgpu-8g` or `a3-edgegpu-8g`.
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of its run duration. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RUN_DURATION`: the maximum time that the VM runs before Compute Engine stops or deletes it. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, a value of `30m` defines a time of 30 minutes, and a value of `1h2m3s` defines a time of one hour, two minutes, and three seconds. You can specify a value between 10 minutes and seven days.
  * `VALID_FOR_DURATION`: the maximum time to wait for provisioning your requested resources. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds: 
    * If your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90s`) and two hours (`2h`). Longer durations give you higher chances of obtaining resources.
    * If the VM can run in any zone within the region, then specify a duration of zero seconds (`0s`). This value specifies that Compute Engine only allocates resources if they are immediately available. If the creation request fails because resources are unavailable, then retry the request in a different zone.



If you want to apply a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to your VM to reduce network latency across VMs, use the same command with the `--resource-policies=RESOURCE_POLICY_NAME` flag.

### Reservation-bound
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE --restart-on-failure \
        --image-family=cos-121-lts \
        --image-project=cos-cloud \
        --boot-disk-size=BOOT_DISK_SIZE \
        --metadata=cos-update-strategy=update_disabled \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-mgmt-net,subnet=NETWORK_NAME_PREFIX-mgmt-sub \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-1,subnet=NETWORK_NAME_PREFIX-data-sub-1,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-2,subnet=NETWORK_NAME_PREFIX-data-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-3,subnet=NETWORK_NAME_PREFIX-data-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=NETWORK_NAME_PREFIX-data-net-4,subnet=NETWORK_NAME_PREFIX-data-sub-4,no-address \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --reservation-affinity=specific \
        --reservation=RESERVATION_URL
    

Replace the following:

  * `VM_NAME`: the name of your VM.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: a zone that [supports the machine type](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).
  * `MACHINE_TYPE`: the machine type for the VM. Specify either `a3-highgpu-8g` or `a3-edgegpu-8g`.
  * `BOOT_DISK_SIZE`: the size of the boot disk in GB—for example, `50`.
  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of the reservation period. Specify one of the following values: 
    * To stop the VM: `STOP`
    * To delete the VM: `DELETE`
  * `RESERVATION_URL`: the URL of the reservation that you want to consume. Specify one of the following values: 
    * If you created the reservation in the same project: `example-reservation`
    * If the reservation is in a different project, and [ your project can use it](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation): `projects/PROJECT_ID/reservations/example-reservation`.



### Install GPU drivers

On each A3 High or Edge VM, complete the following steps.

  1. Install the NVIDIA GPU drivers by running the following command: 
         
         sudo cos-extensions install gpu -- --version=latest

  2. Re-mount the path by running the following command: 
         
         sudo mount --bind /var/lib/nvidia /var/lib/nvidia
         sudo mount -o remount,exec /var/lib/nvidia




### Give the NICs access to the GPUs

On each A3 High or Edge VM, give the NICs access to the GPUs by completing the following steps:

  1. Configure the registry. 
     * If you are using Container Registry, run the following command: 
           
           docker-credential-gcr configure-docker

     * If you are using Artifact Registry, run the following command: 
           
           docker-credential-gcr configure-docker --registries us-docker.pkg.dev

  2. Configure the receive data path manager. A management service, GPUDirect-TCPX Receive Data Path Manager, needs to run alongside the applications that use GPUDirect-TCPX. To start the service on each Container-Optimized OS VM, run the following command: 
         
         docker run --pull=always --rm \
             --name receive-datapath-manager \
             --detach \
             --privileged \
             --cap-add=NET_ADMIN --network=host \
             --volume /var/lib/nvidia/lib64:/usr/local/nvidia/lib64 \
             --device /dev/nvidia0:/dev/nvidia0 \
             --device /dev/nvidia1:/dev/nvidia1 \
             --device /dev/nvidia2:/dev/nvidia2 \
             --device /dev/nvidia3:/dev/nvidia3 \
             --device /dev/nvidia4:/dev/nvidia4 \
             --device /dev/nvidia5:/dev/nvidia5 \
             --device /dev/nvidia6:/dev/nvidia6 \
             --device /dev/nvidia7:/dev/nvidia7 \
             --device /dev/nvidia-uvm:/dev/nvidia-uvm \
             --device /dev/nvidiactl:/dev/nvidiactl \
             --env LD_LIBRARY_PATH=/usr/local/nvidia/lib64 \
             --volume /run/tcpx:/run/tcpx \
             --entrypoint /tcpgpudmarxd/build/app/tcpgpudmarxd \
             us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/tcpgpudmarxd \
             --gpu_nic_preset a3vm --gpu_shmem_type fd --uds_path "/run/tcpx" --setup_param "--verbose 128 2 0"
            

  3. Verify that the `receive-datapath-manager` container started. 
         
         docker container logs --follow receive-datapath-manager

The output should resemble the following:
         
         I0000 00:00:1687813309.406064       1 rx_rule_manager.cc:174] Rx Rule Manager server(s) started...

  4. To stop viewing the logs, press `ctrl-c`.
  5. Install IP table rules. 
         
         sudo iptables -I INPUT -p tcp -m tcp -j ACCEPT

  6. Configure the NVIDIA Collective Communications Library (NCCL) and GPUDirect-TCPX plugin. 

Using NCCL with GPUDirect-TCPX requires a specific NCCL library version and GPUDirect-TCPX plugin binary combination. Google Cloud has provided packages that meet this requirement.

To install the Google Cloud package, run the following command:
         
         docker run --rm -v /var/lib:/var/lib us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/nccl-plugin-gpudirecttcpx install --install-nccl
         sudo mount --bind /var/lib/tcpx /var/lib/tcpx
         sudo mount -o remount,exec /var/lib/tcpx

If this command is successful, then the `libnccl-net.so` and `libnccl.so` files are placed in the `/var/lib/tcpx/lib64` directory.




### Run tests

On each A3 High or Edge VM, run an NCCL test by completing the following steps:

  1. Start the container. 
         
         #!/bin/bash
         
         function run_tcpx_container() {
         docker run \
            -u 0 --network=host \
            --cap-add=IPC_LOCK \
            --userns=host \
            --volume /run/tcpx:/tmp \
            --volume /var/lib/nvidia/lib64:/usr/local/nvidia/lib64 \
            --volume /var/lib/tcpx/lib64:/usr/local/tcpx/lib64 \
            --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
            --device /dev/nvidia0:/dev/nvidia0 \
            --device /dev/nvidia1:/dev/nvidia1 \
            --device /dev/nvidia2:/dev/nvidia2 \
            --device /dev/nvidia3:/dev/nvidia3 \
            --device /dev/nvidia4:/dev/nvidia4 \
            --device /dev/nvidia5:/dev/nvidia5 \
            --device /dev/nvidia6:/dev/nvidia6 \
            --device /dev/nvidia7:/dev/nvidia7 \
            --device /dev/nvidia-uvm:/dev/nvidia-uvm \
            --device /dev/nvidiactl:/dev/nvidiactl \
            --env LD_LIBRARY_PATH=/usr/local/nvidia/lib64:/usr/local/tcpx/lib64 \
            "$@"
         }
         

The command performs the following actions:

     * Mounts NVIDIA devices from `/dev` into the container
     * Sets network namespace of the container to the host
     * Sets user namespace of the container to host
     * Adds `CAP_IPC_LOCK` to the capabilities of the container
     * Mounts `/tmp` of the host to `/tmp` of the container
     * Mounts the installation path of NCCL and GPUDirect-TCPX NCCL plugin into the container and add the mounted path to `LD_LIBRARY_PATH`
  2. After you start the container, applications that use NCCL can run from inside the container. For example, to run the `run-allgather` test, complete the following steps: 
     1. On each A3 High or Edge VM, run the following: 
            
            $ run_tcpx_container -it --rm us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/nccl-plugin-gpudirecttcpx shell

     2. On one VM, run the following commands: 
        1. Set up connection between the VMs. Replace `VM-0` and `VM-1` with the names of each VM. 
               
               /scripts/init_ssh.sh VM-0 VM-1
               pushd /scripts && /scripts/gen_hostfiles.sh VM-0 VM-1; popd

This creates a `/scripts/hostfiles2` directory on each VM.

        2. Run the script. 
               
               /scripts/run-allgather.sh 8 eth1,eth2,eth3,eth4 1M 512M 2

The `run-allgather` script takes about two minutes to run. At the end of the logs, you'll see the `all-gather` results.

If you see the following line in your NCCL logs, then this line verifies that GPUDirect-TCPX is initialized successfully.
    
    NCCL INFO NET/GPUDirectTCPX ver. 3.1.1.
    




## Multi-Instance GPU

A [Multi-Instance GPU](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) partitions a single NVIDIA H100 GPU within the same VM into as many as seven independent GPU instances. They run simultaneously, each with its own memory, cache and streaming multiprocessors. This setup enables the NVIDIA H100 GPU to deliver consistent quality-of-service (QoS) at up to 7x higher utilization compared to earlier GPU models.

You can create up to seven Multi-instance GPUs. With the H100 80GB GPUs each Multi-instance GPU is allocated 10 GB of memory.

For more information about using Multi-Instance GPUs, see [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/).

To create Multi-Instance GPUs, complete the following steps:

  1. Create your A3 Mega, A3 High, or A3 Edge instances.

  2. Install the GPU drivers.

  3. Enable MIG mode. For instructions, see [Enable MIG](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#enable-mig).

  4. Configure your GPU partitions. For instructions, see [Work with GPU partitions](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#work-with-gpu-partitions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
