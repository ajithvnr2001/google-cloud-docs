---
url: https://docs.cloud.google.com/memorystore/docs/memcached/create-instance-gcloud/
title: Quickstart: Create a Memorystore for Memcached instance by using the gcloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:49.026149+00:00
---

# Quickstart: Create a Memorystore for Memcached instance by using the gcloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/create-instance-gcloud/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Memorystore for Memcached instance by using the gcloud CLI

This quickstart walks you through the steps to create a Memorystore for Memcached instance, connect to the instance, send some Memcached commands, and delete the instance.

**Caution:** You cannot create a Memorystore for Memcached instance without first having a private services access connection established. See [Networking](https://docs.cloud.google.com/memorystore/docs/memcached/networking) for details on the private services access connection that is required for Memorystore for Memcached.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. If you haven't already, [install the Google Cloud SDK](https://docs.cloud.google.com/sdk/docs). 

When prompted, choose the project that you selected or created above.

  7. If you already have the Google Cloud SDK installed, update it.
         
         gcloud components update

  8. Enable the Service Networking API for your project.   
[Enable the Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)
  9. Enable the Memorystore for Memcached API for your project.   
[Enable the Memorystore for Memcached API](https://console.cloud.google.com/apis/api/memcache.googleapis.com)



## Creating a Memorystore for Memcached instance

To create a Memorystore for Memcached instance:

  1. Open a terminal window.

  2. Set the project you'd like to create your instance in as the default project in `gcloud` by entering the following command:
         
         gcloud config set core/project project-id
         

  3. Enter the following command to create a Memcached instance with 3 nodes (each node with 4 cores and 10GB memory) in the us-central1 region:
         
         gcloud memcache instances create myinstance --node-count=3 --node-cpu=4 \
             --node-memory=10GB --region=us-central1 --memcached-version=1.6.15
         

  4. After you create the instance, run the following `describe` command, and write down the IP address of one of your nodes.
         
         gcloud memcache instances describe myinstance --region=us-central1
         




## Connecting to your instance from a Compute Engine VM

**Note:** The connecting client must be located in the same region as the Memcached instance. Also, in order to connect the client must use the same network as the Memcached instance, or it must use a Shared VPC network.

  1. Connect to a Linux VM. For steps to connect to a Linux VM, see [Quickstart Using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance). If you used a Debian based image to create your VM instance as described in the quickstart, install `telnet` using `apt-get`:
         
         sudo apt-get install telnet
         

  2. From the terminal, telnet to the IP address of one of the Memcached nodes, replacing variables with appropriate values.
         
         telnet node-ip-address 11211
         

If it works correctly, you should see the following output with the `[bracketed-variables]` replaced by your project's variables:
         
         Trying [node-ip-address]…
         Connected to [node-ip-address]
         

  3. In the telnet session, enter some Memcached commands:

Enter:
         
         get greeting
         

Result:
         
         END
         

Enter:
         
         set greeting 1 0 11
         hello world
         

Result:
         
         STORED
         

Enter:
         
         get greeting
         

Result:
         
         VALUE greeting 1 11
         hello world
         END
         




Memorystore for Memcached supports standard open source Memcached libraries.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the instance by entering the following command:
         
         gcloud memcache instances delete myinstance --region=us-central1
         

Enter `Y` to confirm the instance deletion:
         
         You are about to delete instance [myinstance] in [us-central1].
         Any associated data will be lost.
         Do you want to continue (Y/n)? Y
         Delete request issued for: [myinstance]
         

  2. If successful, `gcloud` returns the following response:
         
         Deleted instance [myinstance]
         




## What's next

  * [Connect to a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/connecting-memcached-instance).

  * [Use the Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/using-auto-discovery).

  * [Monitor your Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
