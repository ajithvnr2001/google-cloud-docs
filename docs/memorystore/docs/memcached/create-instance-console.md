---
url: https://docs.cloud.google.com/memorystore/docs/memcached/create-instance-console/
title: Quickstart: Create a Memorystore for Memcached instance by using the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:48.089143+00:00
---

# Quickstart: Create a Memorystore for Memcached instance by using the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/create-instance-console/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Memorystore for Memcached instance by using the Google Cloud console

This quickstart walks you through the steps to create a Memorystore for Memcached instance, connect to the instance, set a value, retrieve a value, and delete the instance.

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

  6. Enable the Service Networking API for your project.   
[Enable the Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)
  7. Enable the Memorystore for Memcached API for your project.   
[Enable the Memorystore for Memcached API](https://console.cloud.google.com/apis/api/memcache.googleapis.com)



## Creating a Memcached instance

  1. Go to the Memorystore for Memcached page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the **Create Instance** button.

  3. Select the configurations for your new instance on the **Create a Memcached instance** page in the Google Cloud console:

     * Enter an instance ID using only lowercase letters, numbers, and hyphens. Start with a letter. 
       * For example, `my-memcached-instance-1`.
     * Choose `us-central1` from the **Region** dropdown.
     * Choose `Automatically distribute` from the **Zone** dropdown.
     * Enter `2` under **Nodes** to create two nodes.
     * Choose 1 GB of **Memory per node**.
     * Choose 1 for **Cores per node**.
     * Select `default` for the **Authorized network**.

**Note:** If you see the **Private service connection required** panel, you need to [establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).
  4. Click **Create**.

  5. After the instance is created, click the instance ID to view the instance details page.

  6. Write down the `IP address` of one of your nodes.




## Connecting to your instance from a Compute Engine VM

**Note:** To connect to a Memcached instance, your client VM must be located in the same region, and must be connected to the same network, as your instance.

To test the connection:

  1. Connect to a Linux VM. For steps to connect to a Linux VM, see [Quickstart Using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance). If you used a Debian based image to create your VM instance as described in the quickstart, install `telnet` using `apt-get`:
         
         sudo apt-get install telnet
         

  2. From the terminal, telnet to the IP address of one of the Memcached nodes. Replace node-ip-address with the IP address of your node.
         
         telnet node-ip-address 11211
         

You should see the following output with the `[bracketed-variables]` replaced your project's variables:
         
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

  1. Go to the Memorystore for Memcached page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the ID of the instance you want to delete.

  3. Click the **Delete** button.

  4. In the prompt that appears, enter the instance's ID.

  5. Click the **Delete** button.




## What's next

  * [Connect to a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/connecting-memcached-instance).

  * [Use the Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/using-auto-discovery).

  * [Monitor your Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
