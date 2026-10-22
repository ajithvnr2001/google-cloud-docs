---
url: https://docs.cloud.google.com/compute/docs/hpc/create-hpc-migs-gsc-reservations/
title: Create a MIG for HPC workloads with reservation-bound consumption \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:24.398708+00:00
---

# Create a MIG for HPC workloads with reservation-bound consumption  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/create-hpc-migs-gsc-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG for HPC workloads with reservation-bound consumption Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create a managed instance group (MIG) that uses a [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series). The MIG uses the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) to obtain compute resources.

Creating a MIG lets you manage multiple virtual machines (VMs) as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

To learn about HPC VM and HPC cluster creation options, see [Overview of HPC cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters).

This tutorial is intended for HPC engineers, platform administrators and operators, and for data and MPI specialists who are interested in creating a group of interconnected HPC instances to run their workloads. The resulting instances don't use an orchestrator for instance management or job scheduling.

If you want to create a managed instance group but don't need to create a [dense deployment](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#dense) of instances, see instead [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

## Objectives

  * Reserve blocks of capacity for the VM instances.
  * Optional: Create Virtual Private Cloud (VPC) networks.
  * Optional: Create a workload policy.
  * Create an instance template.
  * Create a MIG using one of the following methods: 
    * Create a MIG with a target size.
    * Create a MIG and a resize request.
  * Clean up the resources you created.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine VM instances](https://docs.cloud.google.com/compute/vm-instance-pricing)
  * [Disks](https://docs.cloud.google.com/compute/disks-image-pricing#disk-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/compute.instanceAdmin.v1,roles/compute.networkAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Reserve capacity

To use the commands in this tutorial, you must reserve the capacity for creating the instances in the MIG.

### Create a future reservation for blocks of capacity

This action lets you reserve blocks of capacity for a defined duration, starting on a specific date and time that you choose. The reservation reserves [blocks](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#block) or sub-blocks of capacity in a [cluster](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#cluster), which allows for dense deployments of VM instances.

To create a future reservation for a dense deployment, the process is as follows:

  1. Follow the process to [reserve capacity by contacting your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) in the AI Hypercomputer documentation. In your future reservation request, provide the information as documented, with the following exceptions:

     * **Machine type** : Specify H4D machine type `h4d-highmem-192-lssd`.
     * **Zone** : Specify one of the zones where H4D instances are available, as documented in the [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) table. To display the available zones only for H4D, in the **Select a machine series** list, select `H4D`.
     * **Maintenance scheduling type** : For H4D instances, you can specify either `GROUPED` or `INDEPENDENT`.
     * **Reservation operational mode** : For H4D instances, specify the value `HIGHLY_AVAILABLE_CAPACITY`.
  2. Quota is automatically increased before capacity is delivered. No action is required from you.

  3. When you create the instance template, specify the reservation-bound provisioning model. The VM instances in the MIG are provisioned from your reserved capacity.




You're charged for the entire reservation period, whether or not you use the reserved resources for the entire period. For more information, see [Reservation billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

### Create a future reservation in calendar mode

If you need to use the reserved capacity for less than 90 days, you can create a future reservation in calendar mode using Dynamic Workload Scheduler. To get future reservation resources, the process is as follows:

  1. [Search for available capacity and reserve resources](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode) by using the Google Cloud console, gcloud CLI, or Compute Engine API.
  2. No quota is charged and no action is required from you.
  3. When you create the instance template, specify the reservation-bound provisioning model. The VM instances in the MIG are provisioned from your reserved capacity.



You're charged for the entire reservation period, whether or not you use the reserved resources for the entire period. For more information, see [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).

## Optional: Create VPC networks

Unless you choose to disable it, each project has a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network), which can be used to provide network connectivity for your instances. When you create a VM, you can specify a VPC network and subnet. If you omit this configuration, the default network and subnet are used.

H4D instances can be configured to use Cloud RDMA. Cloud RDMA enables low-latency reliable messaging capabilities by using an [IRDMA network driver](https://docs.cloud.google.com/compute/docs/networking/using-irdma) that supports Remote Direct Memory Access (RDMA) between Compute Engine instances.

For this tutorial:

  * If you want to configure the H4D instances to use Cloud RDMA, complete the steps in this section.
  * If you don't want to use Cloud RDMA, then you can skip this section and use the default network instead.



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




## Create an instance template

To specify the instance and consumption properties for each instance in the MIG, create an instance template by using one of the following methods:

###  gcloud 

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



###  REST 

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



After you create the instance template, you can [view the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and review its instance properties.

## Create a MIG

Depending on your workload requirements, you can create a MIG in either of the following configurations:

  * If you have multiple or parallel jobs that can start with any number of VMs, then create the MIG with a target size.
  * If you require multiple VMs all at once to start a job, or you have a job that requires distribution across an exact number of VM instances, then create a MIG and then create a resize request in the MIG.



### Create a MIG with a target size

If you can start your job without creating all of the VM instances at once, then create a MIG with a target size. The target size determines the number of instances in the MIG. The MIG starts creating instances based on current resource availability. If any resource is temporarily unavailable, the MIG continuously attempts to create instances to meet the target size.

To create a MIG with a target size, select one of the following options:

###  gcloud 

To create a MIG with a specified target size, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

In this step, the commands to create a MIG use a workload policy to specify VM placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

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
  * `TARGET_SIZE`: the number of VMs that you want in the MIG.
  * `WORKLOAD_POLICY_URL`: Optional: the URL of the workload policy. If you don't want to use a workload policy, then you can remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create the MIG. If you use a workload policy, then specify the same region as that of the policy. For a regional MIG, instead of a region, you can specify the zones in that region by using the `--zones` flag.



###  REST 

To create a MIG with a specified target size, make a `POST` request as follows.

In this step, the requests to create a MIG use a workload policy to specify VM placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field from the request body.

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
          "instanceTemplate": "INSTANCE_TEMPLATE_URL",
          "targetSize": "TARGET_SIZE",
          "resourcePolicies": {
            "workloadPolicy": WORKLOAD_POLICY_URL
          }
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
          {
            "versions": [
              {
                "instanceTemplate": "INSTANCE_TEMPLATE_URL"
              }
            ],
            "name": "MIG_NAME",
            "instanceTemplate": "INSTANCE_TEMPLATE_URL",
            "targetSize": "TARGET_SIZE",
            "resourcePolicies": {
              "workloadPolicy": WORKLOAD_POLICY_URL
            }
          }
        


Replace the following: 
  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create a MIG. If you use a workload policy, then specify the same region as that of the policy.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of VMs that you want in the MIG.
  * `WORKLOAD_POLICY_URL`: Optional: the URL of the workload policy. If you don't want to use a workload policy, then you can remove the `resourcePolicies.workloadPolicy` field.



### Create a MIG and a resize request

To create all the requested instances at the same time, create a MIG without any instances in it. After creating the empty MIG, you then create a resize request in the MIG. When the resources are available to create all the instances at once, the resize request adds the instances to the MIG.

To create a MIG and resize request, select one of the following options:

###  gcloud 

In this step, the commands to create a MIG use a workload policy to specify VM placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows:
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               POPULATION_METHOD \
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
             

    2. Create a resize request in the regional MIG using the [beta `instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/create) as follows:
           
           gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               POPULATION_METHOD \
               --region=REGION
           




Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `WORKLOAD_POLICY_URL`: Optional: the URL of the workload policy. If you don't want to use a workload policy, then you can remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. For a regional MIG also, you must specify a zone. This zone must be the zone that contains the profile for your [VPC network](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra#setup-network) and must be a [zone where the machine type is available](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table). For more information, see Limitations.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `POPULATION_METHOD`: the method of adding instances to the MIG. Use one of the following:

    * `--resize-by=COUNT`: add the specified number of instances to the MIG all at once. The instance names are automatically-generated.
    * `--instances=INSTANCE_NAME_LIST`: add instances with the specified names to the MIG all at once. Replace INSTANCE_NAME_LIST with a comma-separated list of instance names. The number of names you provide determines the number of instances to create with this resize request.
  * `REGION`: the region in which the MIG is located.



If you want to apply a workload policy to your MIG, then include the [ `--workload-policy` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--workload-policy) in the command.

###  REST 

In this step, the requests to create a MIG use a workload policy to specify VM placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field from the request body.

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
               "workloadPolicy": WORKLOAD_POLICY_URL
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows: 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             POPULATION_METHOD
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
               "workloadPolicy": WORKLOAD_POLICY_URL
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`beta.regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/insert) as follows: 
           
           POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             POPULATION_METHOD
           }
           




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. For a regional MIG also, you must specify a zone. This zone must be the zone that contains the profile for your [VPC network](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-prereqs#setup-network) and must be a [zone where the machine type is available](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table). For more information, see Limitations.
  * `REGION`: the region in which you want to create the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `WORKLOAD_POLICY_URL`: Optional: the URL of the workload policy. If you don't want to use a workload policy, then you can remove the `resourcePolicies.workloadPolicy` field.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `POPULATION_METHOD`: the method of adding instances to the MIG. Use one of the following:

    * `"resizeBy":COUNT`: replace COUNT with the specified number of instances to add to the MIG all at once. The instance names are automatically-generated.
    * `"instanceNames":INSTANCE_NAME_LIST`: add instances with the specified names to the MIG all at once. Replace INSTANCE_NAME_LIST with a comma-separated list of instance names. The number of names you provide determines the number of instances to create with this resize request.



If you want to apply a workload policy to your MIG, then include the [ `resourcePolicies.workloadPolicy` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert#body.request_body.FIELDS.resource_policies) in the request body.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

### Delete the resources

  1. [Delete resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#delete-request).

  2. [Delete the MIG and instances](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig).

  3. If the auto-delete state for the disks was set to `False` in the instance template, then the disks are not automatically deleted when the VM instance is deleted. You can delete the disks using one of the following methods:

###  Console 

     1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

     1. Select the rows that contain the disks that you created in this tutorial. Make sure the **In use by** column is empty for each disk.

     2. Click delete **Delete** , and then click **Delete** to confirm.

###  gcloud 

Use the [`gcloud compute disks delete`command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete).
    
    gcloud compute disks delete DISK_NAME \
        --project PROJECT_ID --zone ZONE
    

Replace the following:

     * DISK_NAME : the name of the disk to delete
     * PROJECT_ID: the ID of the project that contains the disk
     * ZONE: the zone of the disk

###  REST 

Use the [`disks.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/delete) to delete the disks.
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME 
    

Replace the following:

     * PROJECT_ID: the ID of the project that contains the disk
     * ZONE: the zone of the disk
     * DISK_NAME : the name of the disk to delete

  4. [Delete the networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_a_network).

  5. [Delete the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#delete_an_instance_template).




## What's next

  * Learn more about [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)
  * Learn more about [Compute Engine consumption options](https://docs.cloud.google.com/compute/docs/instances/provisioning-models)
  * Learn about the [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [View, cancel, or delete resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
