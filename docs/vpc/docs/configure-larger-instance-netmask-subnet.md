---
url: https://docs.cloud.google.com/vpc/docs/configure-larger-instance-netmask-subnet/
title: Configure larger instance netmasks for all instances in a subnet \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:11.637793+00:00
---

# Configure larger instance netmasks for all instances in a subnet  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-larger-instance-netmask-subnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure larger instance netmasks for all instances in a subnet

This page describes how to configure all Compute Engine instances in a subnet with larger than default netmasks. To use this configuration, you create a subnet and configure the **Resolve subnet mask** (`--resolve-subnet-mask`) setting. When you connect compute instances to the subnet, the instances are configured with a netmask that's the same size as the subnet's netmask, instead of `/32`. For more information about compute instance netmasks, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




### Required roles

To get the permissions that you need to create a subnet, ask your administrator to grant you the Compute Network Admin (`role/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a subnet to configure larger instance netmasks

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select a VPC network.

  3. Click the **Subnets** tab.

  4. Click **Add subnet**.

  5. For **Name** , enter a name for the subnet.

  6. For **Region** , select a region.

  7. For **Purpose** , select **None**.

  8. For **IP stack type** , select **IPv4 (single stack)**.

  9. For **Primary IPv4 range** , enter a [valid IPv4 address range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

  10. If you want to add a secondary IPv4 range, do the following:

     1. For **Subnet range name** , enter a name for the secondary IPv4 range.
     2. For **Secondary IPv4 range** , enter a valid IPv4 address range.
  11. In **Resolve subnet mask** , select one of the following:

     * **All ranges**
     * **Primary range only**
  12. Click **Add**.




###  gcloud 
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --network=NETWORK_NAME \
        --range=IP_RANGE \
        --region=REGION \
        --resolve-subnet-mask=ARP_RANGES
    

Replace the following:

  * `SUBNET_NAME`: a name for the subnet.
  * `NETWORK_NAME`: the network to create the subnet in.
  * `IP_RANGE`: the primary IPv4 address range for the subnet.
  * `REGION`: the region for the subnet.
  * `ARP_RANGES`: the ranges that you want to receive ARP replies from. Valid values are `ARP_PRIMARY_RANGE` and `ARP_ALL_RANGES`.



## Create a compute instance in the subnet

Create a compute instance that is connected to the subnet. For more information about creating instances, see [Create an instance in a specific subnet](https://docs.cloud.google.com/compute/docs/instances/create-vm-specific-subnet).

###  gcloud CLI 
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --subnet=SUBNET_NAME
    

Replace the following:

  * `INSTANCE_NAME`: a name for your instance.
  * `ZONE`: the zone to create the instance in.
  * `SUBNET_NAME`: the name of the subnet to connect the instance to.



## Verify the configuration

After you create a compute instance, you can verify that the DHCP server configures the correct netmask on the instance, and that the instance receives ARP replies. You can verify ARP replies by using only one instance because [Google Cloud always sends a reply for IP addresses in the subnet's range](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks#how-arp-works-vpc).

The following steps show you how to verify the configuration on a Linux instance.

  1. Connect to your instance by using SSH.
  2. Check the network interface configuration to verify that the netmask matches the subnet's netmask (not `/32`).
         
         ip addr show
         

In the output, look for the `inet` line for your network interface, for example, `ens4`.

  3. Verify that the instance can receive ARP replies for a different IP address in the subnet. You can use the `ping` command to trigger an ARP request. You can choose an IP address that's not in use—Google Cloud sends an ARP reply even if there is no reply to the `ping` request.
         
         ping -c 3 OTHER_IP_ADDRESS_IN_SUBNET
         

Replace `OTHER_IP_ADDRESS_IN_SUBNET` with an IP address from the same subnet. This IP address doesn't need to be in use.

  4. Check the ARP table to see the MAC address associated with the other IP address.
         
         ip neighbor
         

The output displays the MAC address of the other IP address.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
