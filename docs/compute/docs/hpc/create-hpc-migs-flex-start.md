---
url: https://docs.cloud.google.com/compute/docs/hpc/create-hpc-migs-flex-start/
title: Create a MIG with H4D machine types and flex-start \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:59.638369+00:00
---

# Create a MIG with H4D machine types and flex-start  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/create-hpc-migs-flex-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with H4D machine types and flex-start Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create a managed instance group (MIG) that uses an [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series). The MIG creates [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)—virtual machine (VM) instances that run for up to seven days at a discounted price. When created this way, Compute Engine places VMs in close proximity to minimize network latency, making them ideal for running HPC workloads.

Creating a MIG lets you manage multiple VMs as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

To learn about HPC VM and HPC cluster creation options, see [Overview of HPC cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters).

This tutorial is intended for HPC engineers, platform administrators and operators, and for data and MPI specialists who are interested in creating a group of interconnected HPC instances for short duration workloads. The resulting instances don't use an orchestrator for instance management or job scheduling.

## Objectives

  1. Optional: Request preemptible quota.
  2. Optional: Create Virtual Private Cloud networks.
  3. Optional: Create a workload policy.
  4. Create an instance template.
  5. Create a MIG and a resize request.
  6. Clean up.



## Costs

This tutorial uses billable components of Google Cloud, including: 

  * [ Compute Engine VM instances](https://docs.cloud.google.com/compute/vm-instance-pricing)
  * [Disks](https://docs.cloud.google.com/compute/disks-image-pricing#disk-pricing)



To generate a cost estimate based on your projected usage, use the [Pricing Calculator](https://cloud.google.com/products/calculator).

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



## Optional: Request preemptible quota

The VM instances added to the MIG consume [regional quota](https://docs.cloud.google.com/compute/resource-usage). VM instance, instance group, CPU, and disk quotas can be consumed by any VM instance in the region, regardless of zone.

The quota can be either standard quota or preemptible quota when using Flex-start.

  * Standard quota: If your project does not have preemptible quota, and you have never requested preemptible quota, then the instance resources consume standard quota.
  * Preemptible quota: Requesting preemptible quotas can help you improve quota obtainability by providing separate quotas for temporary resources. However, after Compute Engine grants you preemptible quota in a region, all applicable resources consume only preemptible quota. If this quota is depleted, you must request additional preemptible quota for the VM resources.



You can request preemptible quota by following the steps documented in [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

### Types of quota needed

To use instance groups, you must have available quota for all the resources that the group uses (for example, CPU quota) and available [quota for the group resource](https://docs.cloud.google.com/compute/resource-usage#instance_groups) itself. For H4D instances, the following quota types might be used, depending on the machine type used by the instances:

Resource | Standard quota | Preemptible quota  
---|---|---  
CPUs | `CPUS_PER_VM_FAMILY` | `Preemptible CPUs`  
Local SSDs | `Local SSD per machine family (GB)` | `Preemptible Local SSDs (GB)`  
  
To create the resources in this tutorial, the following additional regional quota might be required:

  * Zonal (single-zone) managed instance group: `Instance group managers` and `Instance groups`
  * Google Cloud Hyperdisk:

    * `Hyperdisk Balanced Capacity (GB)`
    * `Hyperdisk Balanced Throughput (MB/s)`
    * `Hyperdisk Balanced IOPS`



## Optional: Create VPC networks

Unless you choose to disable it, each project has a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network), which can be used to provide network connectivity for your instances. When you create a VM, you can specify a VPC network and subnet. If you omit this configuration, the default network and subnet are used.

H4D instances can be configured to use Cloud RDMA. Cloud RDMA enables low-latency reliable messaging capabilities by using an [IRDMA network driver](https://docs.cloud.google.com/compute/docs/networking/using-irdma) that supports Remote Direct Memory Access (RDMA) between Compute Engine instances.

For this tutorial:

  * If you want to configure the H4D instances to use Cloud RDMA, complete the steps in this section.
  * If you don't want to use Cloud RDMA, then you can skip this section and use the default network instead.



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



## Optional: Create a workload policy

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

To use the Flex-start consumption option, you create an empty MIG and then create a resize request for the MIG. When your requested capacity becomes available, Compute Engine provisions it and creates the instances in the MIG. You obtain resources for up to seven days.

To specify the instance and consumption properties for each instance in the MIG, create an instance template by using one of the following methods:

###  gcloud 

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



###  REST 

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



After you create the instance template, you can [view the template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and review its instance properties.

## Create a MIG with a resize request

To create all the requested Flex-start instances at the same time, create a MIG and then create a resize request in the MIG as described in this section.

### Create the MIG

To create the MIG, select one of the following options:

###  gcloud 

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
        
        gcloud compute instance-groups managed create MIG_NAME \
                --template=INSTANCE_TEMPLATE_URL \
                --size=0 \
                --default-action-on-vm-failure=do-nothing \
                --workload-policy=WORKLOAD_POLICY_URL \
                --zone=ZONE
            

  * To create a regional MIG, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
        
        gcloud compute instance-groups managed create MIG_NAME \
                --template=INSTANCE_TEMPLATE_URL \
                --size=0 \
                --default-action-on-vm-failure=do-nothing \
                --zones=ZONE \
                --target-distribution-shape=any-single-zone \
                --instance-redistribution-type=none
            




If you want to apply a workload policy to your MIG, then include the [ `--workload-policy` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--workload-policy) in the command.

###  REST 

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
        
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
             

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
        
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
             




If you want to apply a workload policy to your MIG, then include the [ `resourcePolicies.workloadPolicy` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert#body.request_body.FIELDS.resource_policies) in the request body.

### Create the resize request

To create the resize request in the MIG, select one of the following options:

###  gcloud 

Create a resize request as follows:

  * To create a resize request in a zonal MIG, use the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows:
        
        gcloud compute instance-groups managed resize-requests create MIG_NAME \
                --resize-request=RESIZE_REQUEST_NAME \
                POPULATION_METHOD \
                --zone=ZONE
            

  * To create a resize request in a regional MIG, use the [beta `instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/create) as follows: 
        
        gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
                  --resize-request=RESIZE_REQUEST_NAME \
                  POPULATION_METHOD \
                  --region=REGION
              




If you want to apply a workload policy to your MIG, then include the [ `--workload-policy` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--workload-policy) in the command.

###  REST 

Create a resize request in a zonal or regional MIG as follows:

  * To create a resize request in a zonal MIG, make a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows: 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
              {
                "name": "RESIZE_REQUEST_NAME",
                POPULATION_METHOD
              }
              

  * To create a resize request in a regional MIG, make a `POST` request to the [`beta.regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/insert) as follows: 
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
              {
                "name": "RESIZE_REQUEST_NAME",
                POPULATION_METHOD
              }
              




If you want to apply a workload policy to your MIG, then include the [`resourcePolicies.workloadPolicy` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert#body.request_body.FIELDS.resource_policies) in the request body.

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
  * Learn more about [Dynamic Workload Scheduler flex-start](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) and other consumption options
  * Learn about the [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [View, cancel, or delete resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
