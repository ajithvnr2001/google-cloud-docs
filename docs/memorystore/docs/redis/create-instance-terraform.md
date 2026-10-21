---
url: https://docs.cloud.google.com/memorystore/docs/redis/create-instance-terraform/
title: Quickstart: Create a Memorystore for Redis instance by using Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:46.476085+00:00
---

# Quickstart: Create a Memorystore for Redis instance by using Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/create-instance-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Memorystore for Redis instance by using Terraform

Learn how to create a Memorystore for Redis instance, connect to it, and then delete it.

This quickstart uses the [Google Cloud Platform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) for Terraform. 

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

  10. If you haven't already, [install the Google Cloud SDK](https://docs.cloud.google.com/sdk/docs). 

When prompted, choose the project that you selected or created.

  11. If you already have the Google Cloud SDK installed, then update it.
         
         gcloud components update

  12. Enable the Memorystore for Redis API.   
[Memorystore for Redis](https://console.cloud.google.com/apis/library/redis.googleapis.com)
  13. Have a Terraform file to which you can add the Memorystore resource. For instructions on setting up Terraform with Google Cloud, see [Getting Started with the Google Cloud Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started). 



### Required roles

To get the permissions that you need to create a Memorystore for Redis instance, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud Memorystore Redis Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/redis#redis.admin) (`roles/redis.admin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Memorystore for Redis instance

In this section, you create a 2-GB Memorystore for Redis instance that's located in the `us-central1` region and is in the Basic tier. For more information about tiers, see [Redis tier capabilities](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers).

  1. Add the following resource to your Terraform configuration file:
         
         resource "google_redis_instance" "my_memorystore_redis_instance" {
           name           = "myinstance"
           tier           = "BASIC"
           memory_size_gb = 2
           region         = "us-central1"
           redis_version  = "REDIS_6_X"
         }
         

  2. Add the following [output value](https://www.terraform.io/docs/configuration/outputs.html) to your Terraform configuration file to print the IP address of the instance. You need this address to connect to your instance.
         
         output "host" {
          description = "The IP address of the instance."
          value = "${google_redis_instance.my_memorystore_redis_instance.host}"
         }
         

  3. Run the `terraform init` command.

  4. Run the `terraform plan` command, and then review the instance to be created.

  5. To create the instance, run the `terraform apply` command.




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

  1. Remove the `google_redis_instance` resource from your Terraform configuration file.
  2. To delete the resource, run the `terraform init`, `terraform plan`, and `terraform apply` commands.
  3. **Optional**. If you created a Compute Engine VM for this quickstart, then [delete](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) it.



## What's next

  * Learn more about [creating and managing instances](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances).
  * Learn about other ways to [connect to your Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance).
  * Learn about the characteristics of a [Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
