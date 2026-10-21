---
url: https://docs.cloud.google.com/compute/docs/hpc/create-mig-hpc-dense/
title: Create a HPC MIG with H4D machine series \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:56:31.249712+00:00
---

# Create a HPC MIG with H4D machine series  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/create-mig-hpc-dense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a HPC MIG with H4D machine series Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a managed instance group (MIG) that uses a [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

Creating a MIG lets you manage multiple virtual machines (VMs) as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

To learn about HPC VM and HPC cluster creation options, see [Overview of HPC cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters).

If you want to create a MIG but aren't using H4D machine types, or you don't need to create a [dense deployment](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#dense) of instances, then see [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

## Before you begin

  * **Choose a consumption option** : to create compute instances in bulk and enable enhanced cluster management capabilities, you can choose a Future Reservation in Calendar mode or [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

If you choose to use Spot VMs, the VMs might not be compactly collocated. Also, Spot VMs can be preempted as needed and they are not eligible for [managing host maintenance events for groups of VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d). 

  * **Obtain capacity** : the process to obtain capacity differs for each consumption option.

To learn more, see [Choose a consumption option and obtain capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity).

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




## Overview

Creating a MIG with the H4D machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a workload policy Optional: Create a compact placement policy
  3. Create an instance template
  4. Create a MIG
  5. Install GPU drivers



## Limitations

When you create a MIG with H4D VMs, the following limitations apply:

  * You must turn off repairs in the MIG, as described in this document.



  * If you create a regional MIG that uses RDMA networking, then the MIG can only create H4D instances in the zone where you [configured the network profile for RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra#setup-network). 

  * You can't configure [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) in the MIG.



  * the [limitations for workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#limitations).



#### Limitations for MIG resize requests

For MIG resize requests, the following limitations apply:

  * In regional MIGs, you can use only the `ANY_SINGLE_ZONE` [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

  * You can only set the [standby pool mode of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig#standby_policy) to `manual` (default).

  * You can't set [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler).

  * If the MIG contains accepted resize requests, then you can't change the [target size of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size).

  * You can't delete or abandon the managed instances in a `CREATING` status that the MIG creates for a resize request. To delete those managed instances, you must [cancel the resize request](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#cancel-request).




For more information, see [all the limitations for resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations).

## Optional: Create VPC networks

When you create a compute instance, you can specify a VPC network and subnet. If you omit this configuration, the default network and subnet are used.

If you want to configure the H4D instances in the MIG to use Cloud RDMA, then complete the steps in this section; otherwise, you can skip this section and use the default network instead.

To use Cloud RDMA with H4D instances, you must have at least two networks configured, one for each type of network interface (NIC):

  * NIC type `GVNIC`: uses the `gve` driver for TCP/IP and Internet traffic for normal VM-VM and VM-Internet communication.
  * NIC type `IRDMA`: uses IDPF/iRDMA drivers for Cloud RDMA networking between instances.



Instances that use Cloud RDMA can have only one `IRDMA` interface. You can add up to eight additional `GVNIC` network interfaces for a total of 10 vNICs per instance.

To set up the [Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#overview) to use with your instances, you can either follow the documented instructions or use the provided script.

### Instruction guides

To create the networks, you can use the following instructions: 

  * To create the host networks for the `GVNIC` network interfaces, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

If you are configuring only one `GVNIC` network interface, you can use the default VPC network and the auto subnet that's in the same region as the instance.

  * To create a network for the `IRDMA` network interface, see [Create a VPC network with a Falcon VPC network profile](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma). Use the default value for the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) for a Falcon VPC network, which is `8896`.




### Script

You can create up to nine gVNIC network interfaces and one IRDMA network interface per instance. Each network interface must attach to a separate network. To create the networks, you can use the following script, which creates two networks for gVNIC and one network for IRDMA. 

  1. Optional: Before running the script, list the Falcon VPC network profiles to verify there is one available. 
         
         gcloud compute network-profiles list
           

  2. Copy the following code and run it in a Linux shell window.
         
         #!/bin/bash
           # Set the number of GVNIC interfaces to create. You can create up to 9.
           NUM_GVNIC=NUMBER_OF_GVNIC
         
           # Create regular VPC networks and subnets for the GVNIC interfaces
             for N in $(seq 0 $(($NUM_GVNIC - 1))); do
               gcloud compute networks create GVNIC_NAME_PREFIX-net-$N \
                   --subnet-mode=custom
         
               gcloud compute networks subnets create GVNIC_NAME_PREFIX-sub-$N \
                   --network=GVNIC_NAME_PREFIX-net-$N \
                   --region=REGION \
                   --range=10.$N.0.0/16
         
               gcloud compute firewall-rules create GVNIC_NAME_PREFIX-internal-$N \
                   --network=GVNIC_NAME_PREFIX-net-$N \
                   --action=ALLOW \
                   --rules=tcp:0-65535,udp:0-65535,icmp \
                   --source-ranges=10.0.0.0/8
           done
         
           # Create SSH firewall rules
           gcloud compute firewall-rules create GVNIC_NAME_PREFIX-ssh \
               --network=GVNIC_NAME_PREFIX-net-0 \
               --action=ALLOW \
               --rules=tcp:22 \
               --source-ranges=IP_RANGE
         
           # Optional: Create a firewall rule for the external IP address for the
           #  first GVNIC network interface
           gcloud compute firewall-rules create GVNIC_NAME_PREFIX-allow-ping-net-0 \
               --network=GVNIC_NAME_PREFIX-net-0 \
               --action=ALLOW \
               --rules=icmp \
               --source-ranges=IP_RANGE
         
           # Create a Falcon VPC network for the Cloud RDMA network interface
           gcloud compute networks create RDMA_NAME_PREFIX-irdma \
               --network-profile=ZONE-vpc-falcon \
               --subnet-mode custom
         
           # Create a subnet in the Falcon VPC network
           gcloud compute networks subnets create RDMA_NAME_PREFIX-irdma-sub \
               --network=RDMA_NAME_PREFIX-irdma \
               --region=REGION \
               --range=10.2.0.0/16  # offset to avoid overlap with GVNIC subnet ranges
           

Replace the following:

     * `NUMBER_OF_GVNIC`: the number of GVNIC interfaces to create. Specify a number from 1 to 9.
     * `GVNIC_NAME_PREFIX`: the name prefix to use for the regular VPC network and subnet that uses a GVNIC NIC type.
     * `REGION`: the region where you want to create the networks. This must correspond to the zone specified for the `--network-profile` flag, when creating the Falcon VPC network. For example, if you specify the zone as `europe-west4-b`, then your region is `europe-west4`.
     * `IP_RANGE`: the range of IP addresses outside of the VPC network to use for the [SSH firewall rules](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies). As a best practice, specify the specific IP address ranges that you need to allow access from, rather than all IPv4 or IPv6 sources. Don't use `0.0.0.0/0` or `::/0` as a source range because this allows traffic from all IPv4 or IPv6 sources, including sources outside of Google Cloud.
     * `RDMA_NAME_PREFIX`: the name prefix to use for the VPC network and subnet that uses the IRDMA NIC type.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where you want to create the networks and compute instances. Use either `us-central1-a` or `europe-west4-b`.
  3. Optional: To verify that the VPC network resources are created successfully, check the network settings in the Google Cloud console:

     1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. Search the list for the networks that you created in the previous step.
     3. To view the subnets, firewall rules, and other network settings, click the name of the network.



### Optional: Create a workload policy

If you want Compute Engine to place VM instances in a single block or adjacent blocks, then specify instance placement by creating a [workload policy](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies). However, if you want Compute Engine to place your instances on a specific block, skip this step and provide the name of the block in the reservation affinity when you create the instance template.

To create a workload policy, select one of the following options:

### gcloud

To create a workload policy, use the [ `gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy).

  * For a best-effort placement of VMs, specify the `--type=high-throughput` flag in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --region=REGION
        

  * For strict colocation of VMs, specify the `--max-topology-distance` and `--type=high-throughput` flags in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --max-topology-distance=TOPOLOGY_DISTANCE \
            --region=REGION
        




Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `TOPOLOGY_DISTANCE`: the maximum topology distance. Specify one of the following values: 
    * To place VMs in the same sub-block: `SUBBLOCK`
    * To place VMs in the same block: `BLOCK`
    * To place VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [ Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).

  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions and zones, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).



### REST

To create a workload policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert).

  * For a best-effort placement of VMs, specify the `type` field in the request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
          {
            "name": "WORKLOAD_POLICY_NAME"
            "workloadPolicy": {
              "type": "HIGH_THROUGHPUT"
            }
          }
        

  * For strict colocation of VMs, specify the `maxTopologyDistance` and `type` fields in the request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
          {
            "name": "WORKLOAD_POLICY_NAME"
            "workloadPolicy": {
              "type": "HIGH_THROUGHPUT",
              "maxTopologyDistance": "TOPOLOGY_DISTANCE"
            }
          }
        




Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions and zones, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `TOPOLOGY_DISTANCE`: the maximum topology distance. Specify one of the following values: 
    * To place VMs in the same sub-block: `SUBBLOCK`
    * To place VMs in the same block: `BLOCK`
    * To place VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).




### Create an instance template

To specify the instance and consumption properties for each instance in the MIG, create an instance template by using one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) that you are using for this deployment. Select the tab that corresponds to your consumption option and provisioning model.

### Flex-start

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-templates/create).
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-0, \
          subnet=GVNIC_NAME_PREFIX-sub-0, \
          stack-type=STACK_TYPE, \
          address=EXTERNAL_IPV4_ADDRESS \
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-1, \
          subnet=GVNIC_NAME_PREFIX-sub-1,no-address \
    --network-interface=nic-type=IRDMA, \
          network=RDMA_NAME_PREFIX-irdma, \
          subnet=RDMA_NAME_PREFIX-irdma-sub, \
          stack-type=IPV4_ONLY,no-address \
        
        --instance-termination-action=DELETE \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        --provisioning-model=FLEX_START
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the H4D machine type to use for the instance.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available.
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `STACK_TYPE`: Optional: the stack type to use for the gVNIC interface. Specify either `IPV4_ONLY` or `IPV4_IPV6`. If you don't specify a value, `IPV4_ONLY` is used by default.
  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following:

    * Specify a valid IPv4 address from the subnet.
    * Use the flag `no-address` if you don't want the network interface to have an external IP address.
    * Specify `address=''` if you want the network interface to receive an ephemeral external IP address.

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `RUN_DURATION`: the duration you want the requested instances to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days. 



### Reservation-bound

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-0, \
          subnet=GVNIC_NAME_PREFIX-sub-0, \
          stack-type=STACK_TYPE, \
          address=EXTERNAL_IPV4_ADDRESS \
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-1, \
          subnet=GVNIC_NAME_PREFIX-sub-1,no-address \
    --network-interface=nic-type=IRDMA, \
          network=RDMA_NAME_PREFIX-irdma, \
          subnet=RDMA_NAME_PREFIX-irdma-sub, \
          stack-type=IPV4_ONLY,no-address \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=DELETE \
        --maintenance-policy=TERMINATE
    
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the H4D machine type to use for the instance.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available.
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `STACK_TYPE`: Optional: the stack type to use for the gVNIC interface. Specify either `IPV4_ONLY` or `IPV4_IPV6`. If you don't specify a value, `IPV4_ONLY` is used by default.
  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following:

    * Specify a valid IPv4 address from the subnet.
    * Use the flag `no-address` if you don't want the network interface to have an external IP address.
    * Specify `address=''` if you want the network interface to receive an ephemeral external IP address.

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `RESERVATION`: the name of the reservation that you want to use.

`RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Spot

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-0, \
          subnet=GVNIC_NAME_PREFIX-sub-0, \
          stack-type=STACK_TYPE, \
          address=EXTERNAL_IPV4_ADDRESS \
    --network-interface=nic-type=GVNIC, \
          network=GVNIC_NAME_PREFIX-net-1, \
          subnet=GVNIC_NAME_PREFIX-sub-1,no-address \
    --network-interface=nic-type=IRDMA, \
          network=RDMA_NAME_PREFIX-irdma, \
          subnet=RDMA_NAME_PREFIX-irdma-sub, \
          stack-type=IPV4_ONLY,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the H4D machine type to use for the instance.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available.
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `STACK_TYPE`: Optional: the stack type to use for the gVNIC interface. Specify either `IPV4_ONLY` or `IPV4_IPV6`. If you don't specify a value, `IPV4_ONLY` is used by default.
  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following:

    * Specify a valid IPv4 address from the subnet.
    * Use the flag `no-address` if you don't want the network interface to have an external IP address.
    * Specify `address=''` if you want the network interface to receive an ephemeral external IP address.

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the Spot VMs on preemption.

**Important:** Make sure your application can handle preemption. For example, we recommend that you handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



###  REST 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) that you are using for this deployment. Select the tab that corresponds to your consumption option and provisioning model.

### Flex-start

**Preview — Flex-start**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name":"INSTANCE_TEMPLATE_NAME",
      "properties":{
        "disks":[
          {
            "boot":true,
            "initializeParams":{
              "diskSizeGb":"DISK_SIZE",
              "diskType":"hyperdisk-balanced",
              "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            },
            "mode":"READ_WRITE",
            "type":"PERSISTENT"
          }
        ],
        "machineType":"MACHINE_TYPE",
        
            "networkInterfaces": [
            {
              "network": "GVNIC_NAME_PREFIX-net-0",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-0",
              "accessConfigs": [
                {
                    "type": "ONE_TO_ONE_NAT",
                    "name": "External IP",
                    "natIP": "EXTERNAL_IPV4_ADDRESS"
                }
              ],
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "GVNIC_NAME_PREFIX-net-1",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-1",
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "RDMA_NAME_PREFIX-irdma",
              "subnetwork": "RDMA_NAME_PREFIX-irdma-sub",
              "stackType": "IPV4_ONLY",
              "nicType": "IRDMA",
          }
        ],
    ,
        "scheduling": {
            "instanceTerminationAction": "DELETE",
            "maxRunDuration": {
              "seconds": RUN_DURATION
            },
            "onHostMaintenance": "TERMINATE",
            "provisioningModel": "FLEX_START"
          }
    
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the instance. Specify a H4D machine type. For more information, see [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `RUN_DURATION`: the duration, in seconds, you want the requested instances to run. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).



### Reservation-bound

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name":"INSTANCE_TEMPLATE_NAME",
      "properties":{
        "disks":[
          {
            "boot":true,
            "initializeParams":{
              "diskSizeGb":"DISK_SIZE",
              "diskType":"hyperdisk-balanced",
              "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            },
            "mode":"READ_WRITE",
            "type":"PERSISTENT"
          }
        ],
        "machineType":"MACHINE_TYPE",
        
            "networkInterfaces": [
            {
              "network": "GVNIC_NAME_PREFIX-net-0",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-0",
              "accessConfigs": [
                {
                    "type": "ONE_TO_ONE_NAT",
                    "name": "External IP",
                    "natIP": "EXTERNAL_IPV4_ADDRESS"
                }
              ],
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "GVNIC_NAME_PREFIX-net-1",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-1",
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "RDMA_NAME_PREFIX-irdma",
              "subnetwork": "RDMA_NAME_PREFIX-irdma-sub",
              "stackType": "IPV4_ONLY",
              "nicType": "IRDMA",
          }
        ],
    ,
        "reservationAffinity":{
            "consumeReservationType":"SPECIFIC_RESERVATION",
            "key":"compute.googleapis.com/reservation-name",
            "values":[
              "RESERVATION"
            ]
          },
        "scheduling":{
            "provisioningModel":"RESERVATION_BOUND",
            "instanceTerminationAction":"DELETE",
            "onHostMaintenance": "TERMINATE",
            "automaticRestart":true
          }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the instance. Specify a H4D machine type. For more information, see [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `RESERVATION`: the name of the reservation that you want to use.

`RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Spot

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name":"INSTANCE_TEMPLATE_NAME",
      "properties":{
        "disks":[
          {
            "boot":true,
            "initializeParams":{
              "diskSizeGb":"DISK_SIZE",
              "diskType":"hyperdisk-balanced",
              "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            },
            "mode":"READ_WRITE",
            "type":"PERSISTENT"
          }
        ],
        "machineType":"MACHINE_TYPE",
        
            "networkInterfaces": [
            {
              "network": "GVNIC_NAME_PREFIX-net-0",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-0",
              "accessConfigs": [
                {
                    "type": "ONE_TO_ONE_NAT",
                    "name": "External IP",
                    "natIP": "EXTERNAL_IPV4_ADDRESS"
                }
              ],
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "GVNIC_NAME_PREFIX-net-1",
              "subnetwork": "GVNIC_NAME_PREFIX-sub-1",
              "stackType": "IPV4_ONLY",
              "nicType": "GVNIC",
          },
          {
              "network": "RDMA_NAME_PREFIX-irdma",
              "subnetwork": "RDMA_NAME_PREFIX-irdma-sub",
              "stackType": "IPV4_ONLY",
              "nicType": "IRDMA",
          }
        ],
    ,
        "scheduling":
        {
          "provisioningModel": "SPOT",
          "instanceTerminationAction": "TERMINATION_ACTION"
        }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the instance. Specify a H4D machine type. For more information, see [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * `IMAGE_PROJECT`: the project ID of the OS image.
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `DISK_SIZE`: the size of the boot disk in GiB.
  * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the standard VPC networks and subnets for the gVNIC interfaces.

If you are using the default network, include only a single `--network-interface` field with the `nic-type` field set to `GVNIC`. Also, omit the `network` and `subnetwork` settings for this network interface.

  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the gVNIC network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 

To specify an external IPv6 address for the GVNIC network interface, use the flag `--external-ipv6-address` instead.

  * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA network interface.

If you are not using Cloud RDMA with your H4D instances, omit the `--network-interface` field for the IRDMA interface.

  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the Spot VMs on preemption.

**Important:** Make sure your application can handle preemption. For example, we recommend that you handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



After you create the instance template, you can [view the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and review its instance properties.

### Create a MIG

After you complete all the previous steps, create a MIG based on your scenario as follows:

Scenario | Method to create a MIG and VMs in it | Example  
---|---|---  
You have multiple or parallel jobs that can start with any number of VMs. | Create a MIG and use the target size to specify the number of VMs that you want in the group.  
See Create a MIG with target size. | ML inference jobs  
You have a job that requires distribution across an exact number of VMs. | Create a MIG without any VMs in it, and then create a resize request in the MIG. The resize request helps you to obtain VMs all at once.   
See Create a MIG and a resize request. | Distributed ML training and fine-tuning jobs  
  
#### Create a MIG with target size

If you can start your job without creating all of the VMs at once, then create a MIG with a _target size_. The target size determines the number of VMs in the MIG. The MIG starts creating VMs based on current resource availability. If any resource is temporarily unavailable, the MIG continuously attempts to create VMs to meet the target size.

To create a MIG with a target size, select one of the following options:

###  gcloud 

To create a MIG with a specified target size, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `--default-action-on-vm-failure=do-nothing` flag to the command. 

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
          --template=INSTANCE_TEMPLATE_URL \
          --size=TARGET_SIZE \
          --workload-policy=WORKLOAD_POLICY_URL \
          --zone=ZONE
        

  * To create a regional MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
            --template=INSTANCE_TEMPLATE_URL \
            --size=TARGET_SIZE \
            --workload-policy=WORKLOAD_POLICY_URL \
            --region=REGION
        


Replace the following: 
  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create the MIG. If you use a workload policy, then specify the same region as that of the policy. For a regional MIG, instead of a region, you can specify the zones in that region by using the `--zones` flag.



###  REST 

To create a MIG with a specified target size, make a `POST` request.

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `"defaultActionOnFailure": "DO_NOTHING"` field to the request. 

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        {
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ],
          "name": "MIG_NAME",
          "targetSize": TARGET_SIZE,
          "resourcePolicies": {
            "workloadPolicy": "WORKLOAD_POLICY_URL"
          }
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
          {
            "name": "MIG_NAME",
            "instanceTemplate": "INSTANCE_TEMPLATE_URL",
            "targetSize": TARGET_SIZE,
            "resourcePolicies": {
              "workloadPolicy": "WORKLOAD_POLICY_URL"
            }
          }
        


Replace the following: 
  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create the MIG. If you use a workload policy, then specify the same region as that of the policy. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field. 



#### Create a MIG and a resize request

If you require multiple VMs all at once to start a job, then create a MIG, and create a [resize request](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) in the MIG as described in this section.

To create a resize request in a MIG, select one of the following options.

###  gcloud 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model. 

### Reservation-bound

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zones=ZONE \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### Flex-start

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --default-action-on-vm-failure=do-nothing \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --default-action-on-vm-failure=do-nothing \
           
               --workload-policy=WORKLOAD_POLICY_URL \
           
               --region=REGION \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none \
               --workload-policy=WORKLOAD_POLICY_URL
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### Spot

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zones=ZONE \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




Replace the following: 

  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. For a regional MIG also, you must specify a zone. This zone must be the zone that contains the profile for your VPC network and must be a [zone where the machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `COUNT`: the number of instances to add to the MIG all at once.
  * `REGION`: the region in which you want to create the MIG.



#### Create a resize request by specifying a list of VM names

If your workload requires specific VM names, then specify a list of names to create the VMs. The number of names that you specify determines the number of VMs that the MIG creates all at once.

To create a resize request with specific VM names in a MIG, use the [beta `gcloud compute instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/create) with the `--instances` flag:

  * In a zonal MIG, run the following command:
        
        gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --instances=INSTANCE_NAMES \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --instances=INSTANCE_NAMES \
            --region=REGION
        


Replace `INSTANCE_NAMES` with a comma-separated list of names for the VMs. For example, `instance-1,instance-2,instance-3`. 

###  REST 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model. 

### Reservation-bound

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### Flex-start

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "instanceLifecyclePolicy": {
               "defaultActionOnFailure": "DO_NOTHING"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "instanceLifecyclePolicy": {
               "defaultActionOnFailure": "DO_NOTHING"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### Spot

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




Replace the following: 

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. This zone must be the same as the zone that contains the profile for your VPC network and must be a [zone where your chosen machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations. 
  * `REGION`: the region in which you want to create the MIG. This region must be the same region that contains the profile for your VPC network and must contain a [zone where your chosen machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `COUNT`: the number of instances to add to the MIG all at once



#### Create a resize request by specifying a list of VM names

If your workload requires specific VM names, then specify a list of names to create the VMs. The number of names that you specify determines the number of VMs that the MIG creates all at once.

To create a resize request with specific VM names in a MIG, use one of the following methods:

  * In a zonal MIG, send a `POST` request by using the [`beta.instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
        

  * In a regional MIG, send a `POST` request by using the [`beta.regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
        




For example, to specify two VM names, include the following in the request body:
    
    
    {
      "name": "RESIZE_REQUEST_NAME",
      "instances": [
        {
          "name": "INSTANCE_NAME_1"
        },
        {
          "name": "INSTANCE_NAME_2"
        }
      ]
    }
    

  
Replace `INSTANCE_NAME_1, INSTANCE_NAME_2` with the names for the VMs. 

## What's next?

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View VMs topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/vms-topology)
  * [Monitor VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)
  * [View, cancel, or delete resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
