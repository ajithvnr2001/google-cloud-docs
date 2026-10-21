---
url: https://docs.cloud.google.com/vpc/docs/configure-larger-instance-netmask-single/
title: Configure a larger netmask for a single instance \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:20.798645+00:00
---

# Configure a larger netmask for a single instance  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-larger-instance-netmask-single/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a larger netmask for a single instance

This page describes how to create a Compute Engine instance that has a larger netmask—the same size as the subnet's netmask—by configuring a custom image.

As an alternative, you can create a subnet that configures larger netmasks for all compute instances that are connected to the subnet. For ease of maintenance and to get support for secondary ranges, we recommend [configuring larger instance netmasks through a subnet](https://docs.cloud.google.com/vpc/docs/configure-larger-instance-netmask-subnet) instead of creating custom images.

If creating a subnet doesn't work for your use case, you can create a custom image and use this image to create compute instances that have larger netmasks. The DHCP server configures the instance interfaces with the subnet's netmask, instead of `/32`, and the instance can directly communicate with other instances that are connected to the primary IPv4 range of the subnet. Secondary IPv4 ranges are not affected.

For more information about compute instance netmasks, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).

## Before you begin

  1. Read the following guides about Compute Engine images: 
     * [OS images](https://docs.cloud.google.com/compute/docs/images)
     * [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom)

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




### Required roles

To get the permissions that you need to create a custom image and an instance, ask your administrator to grant you the Compute Instance Admin (v1) (`role/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a custom image that configures the `MULTI_IP_SUBNET` option

There are multiple ways to specify a source image when you create a custom image. The following example shows you how to create a custom image based on an image family. For more information about creating custom images, see [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).

###  gcloud CLI 
    
    
    gcloud compute images create IMAGE_NAME \
        --source-image-family=SOURCE_IMAGE_FAMILY \
        --source-image-project=PROJECT \
        --guest-os-features=MULTI_IP_SUBNET
    

Replace the following:

  * `IMAGE_NAME`: a name for your custom image.
  * `SOURCE_IMAGE_FAMILY`: the source image family that you want to use to create this image. For example, `debian-13`.
  * `PROJECT`: the source project where the image family is located—for example, `debian-cloud` or a project URI.



## Create a compute instance from a `MULTI_IP_SUBNET` custom image

To create a compute instance that uses the custom image, specify the image that you created. For more information about creating instances, see [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image).

###  gcloud CLI 
    
    
    gcloud compute instances create INSTANCE_NAME \
        --image=IMAGE_NAME \
        --zone=ZONE \
        --subnet=SUBNET_NAME
    

Replace the following:

  * `INSTANCE_NAME`: a name for your instance.
  * `IMAGE_NAME`: the name of the custom image that you created.
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
