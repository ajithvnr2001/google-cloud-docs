---
url: https://docs.cloud.google.com/memorystore/docs/redis/create-instance-console/
title: Quickstart: Create a Memorystore for Redis instance by using the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:58.101830+00:00
---

# Quickstart: Create a Memorystore for Redis instance by using the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/create-instance-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Memorystore for Redis instance by using the Google Cloud console

Learn how to create a Memorystore for Redis instance, connect to it, and then delete it.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?tutorial=memorystore_redis_console_quickstart)

* * *

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

  5. Enable the Memorystore for Redis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=redis.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Memorystore for Redis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=redis.googleapis.com)




### Required roles

To get the permissions that you need to create a Memorystore for Redis instance, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud Memorystore Redis Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/redis#redis.admin) (`roles/redis.admin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Memorystore for Redis instance

In this section, you create a 2-GB Memorystore for Redis instance that's located in the `us-central1` region and is in the Basic tier. For more information about tiers, see [Redis tier capabilities](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers).

  1. In the Google Cloud console, go to the **Memorystore for Redis** page.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click **Create instance**.

  3. In the **Create a Redis instance** page, make the following configurations for the instance that you're creating:

     * In the **Instance ID** field, enter `my-instance-1`.
     * In the **Display name** field, enter `My Quickstart Instance`.
     * In the **Tier selection** section, select **Basic**. This tier designates a standalone Redis node, as opposed to the Standard tier, which uses a replica node to backup your data.
     * In the **Capacity** field, enter `5`. This sets the capacity of your instance to 5 GB.
     * From the **Region** menu, select **us-central1 (Iowa)**.
     * From the **Network** menu, select **default**.
     * Expand the **Configuration** node, and then from the **Version** menu, select   
**7.2 (Recommended)**.
  4. Click **Create instance**.

**Note:** Memorystore for Redis doesn't support legacy-mode networks. To create an instance, use a VPC network. For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  5. After you create the instance, obtain your instance's `IP address` by following these steps:

     1. In the Google Cloud console, go to the **Memorystore for Redis** page.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
     2. Click the ID of your instance: `my-instance-1`.
     3. In the **Connections** section, make a note of your instance's **Primary Endpoint** and **Port** number of `6379`. You need the endpoint and port number to connect to the instance.



## Connect to the Memorystore for Redis instance from a Compute Engine VM

You can connect to the Memorystore for Redis instance from any Compute Engine VM that uses the instance's authorized network with a [supported RFC 1918 IP address](https://docs.cloud.google.com/memorystore/docs/redis/networking#supported_and_unsupported_networks).

  1. If you don't have a Compute Engine VM that uses that same authorized network as your instance, then create one and connect to the VM by using SSH. To do this, follow the steps in [Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Use `apt-get` to install `telnet`:
         
         sudo apt-get install telnet
         

  3. From the terminal, telnet to the IP address of the instance. Replace VARIABLES with appropriate values.
         
         telnet INSTANCE_IP_ADDRESS 6379
         

If you can connect to the instance, then the command returns this result:
         
         Trying INSTANCE_IP_ADDRESS…
         Connected to INSTANCE_IP_ADDRESS
         

  4. In the telnet session, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         

Enter
         
         SET HELLO WORLD
         

Result:
         
         +OK
         

Enter:
         
         GET HELLO
         

Result:
         
         $5
         WORLD
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Memorystore for Redis** page.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
  2. Click the ID of the instance that you want to delete.
  3. Click **Delete**.
  4. In the prompt that appears, enter the instance ID.
  5. Click **Delete**.
  6. **Optional**. If you created a Compute Engine VM for this quickstart, then [delete](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) it.



## What's next

  * Learn more about [creating and managing instances](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances).
  * Learn about other ways to [connect to your Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/connecting-redis-instance).
  * Learn about the characteristics of a [Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
