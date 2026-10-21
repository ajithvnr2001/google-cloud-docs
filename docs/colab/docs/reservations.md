---
url: https://docs.cloud.google.com/colab/docs/reservations/
title: Use reservations with Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:21.774780+00:00
---

# Use reservations with Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use reservations

This document explains how to use [Compute Engine reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to gain a high level of assurance that your Colab Enterprise runtimes have enough virtual machine (VM) resources to run.

Reservations are a Compute Engine feature. They help make sure that you have the resources available to create VMs with the same hardware (memory and vCPUs) and optional resources (GPUs and Local SSD disks) whenever you need them.

When you create a reservation, Compute Engine verifies that the requested capacity is available in the specified zone. If so, then Compute Engine reserves the resources, creates the reservation, and the following happens:

  * The reserved resources are immediately available for you to consume, and they remain available until you delete the reservation.

  * You're charged for the reserved resources at the same on-demand rate as running VMs, including any applicable discounts, until the reservation is deleted. While consuming a reservation, a VM doesn't incur duplicate charges for resources since the reservation is already billed for the cost of the reserved resources. To learn more, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).




## Overview

To use a reservation with Colab Enterprise, you perform the following tasks:

  1. Create a reservation.

  2. Add your reservation to a new runtime template.

  3. Use the reservation by running code on a runtime derived from your runtime template.




## Limitations and requirements

All limitations of Compute Engine reservations apply when Colab Enterprise runtimes consume reservations. See [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).

In addition, when using reservations with Colab Enterprise, the following limitations and requirements apply:

  * [Committed use discounts](https://docs.cloud.google.com/docs/cuds) don't apply.

  * Your reservation must be one of the following:

    * In the same project as your Colab Enterprise notebook and runtime.
    * Shared with the same project as your Colab Enterprise notebook and runtime.
  * A reservation's VM properties must match exactly with your Colab Enterprise runtime to consume the reservation. For example, if a reservation specifies an `e2-standard-8` machine type, then the Colab Enterprise runtime can only consume the reservation if it also uses an `e2-standard-8` machine type. See [Requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements%22).




## Before you begin

  1. Review the [ requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) and [ restrictions](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions) for reservations. 
  2. Review the [ quota requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations) and [ restrictions](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions-shared-reservations) for shared reservations. 

  3. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to use reservations with Colab Enterprise, ask your administrator to grant you the following IAM roles on the project: 

  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Create a reservation

Create a Compute Engine reservation. It can be a single-project reservation or a shared reservation. For more information, see the following documents:

  * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project)
  * [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared)



The reservation can include GPU accelerators.

## Add your reservation to a new runtime template

To create a runtime template that uses your reservation, do the following: 

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime templates** page. 

[Go to Runtime templates](https://console.cloud.google.com/agent-platform/colab/runtime-templates)

  2. Click add_box **New template**. 

The **Create new runtime template** dialog appears.

  3. In the **Runtime basics** section, enter a **Display name**. 

  4. In the **Region** menu, select the region where you want your runtime template. 

  5. In the **Configure compute** section, in the **Machine type** menu, select a machine type. The runtime template's machine type must match your reservation's machine type. 

If the machine types for your reservation and runtime template don't match, Colab Enterprise won't be able to create a runtime from this runtime template. 
  6. In the **Reservations** menu, select the specific reservation that you want to use or select **Use automatically selected reservations**. 

For more information about consuming automatically selected or specifically targeted reservations, see the **Consumption type** section of [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work). 

  7. Complete the rest of the dialog, and then click **Create**. 

Your runtime template appears in the list on the **Runtime templates** tab. 




## Use your reservation

To use your reservation, do the following:

  1. [Create a runtime](https://docs.cloud.google.com/colab/docs/create-runtime) from your new runtime template.

  2. Open or [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart).

  3. In your notebook, [connect to the runtime](https://docs.cloud.google.com/colab/docs/connect-to-runtime), and run code.




## Stop using your reservation

To stop using your reservation, you can [delete your reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).

If you want to continue using your reservation with other resources, but don't want your Colab Enterprise notebooks to use it, delete the runtime and runtime template that are associated with your reservation.

## Billing

When consuming a Compute Engine reservation, you're billed for the following:

  * The Compute Engine resources at Compute Engine pricing. These charges have the label `goog-vertex-ai-product: colab-enterprise` on the SKU. See [Compute Engine pricing](https://cloud.google.com/compute/all-pricing).

  * Colab Enterprise management fees in addition to your infrastructure usage. See [Colab Enterprise pricing](https://cloud.google.com/colab/pricing).




## Troubleshoot

This section shows you how to resolve issues when using reservations with Colab Enterprise.

### Unable to create a runtime

An error similar to the following occurs when you try to create a runtime.
    
    
    Failed to create notebook runtime with error: Invalid value for field
    'resource.reservationAffinity': '{"consumeReservationType":
    "SPECIFIC_ALLOCATION", "key": "compute.googleapis.com/reservation-name...'.
    No available resources in specified reservations.
    

This error occurs when a reservation's VM properties don't match your Colab Enterprise runtime. For example, if a reservation specifies an `e2-standard-8` machine type, then the Colab Enterprise runtime can only consume the reservation if it also uses an `e2-standard-8` machine type. For more information, see [Requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements). 

To resolve this issue, create a runtime template with a configuration that matches the reservation's VM properties. 

## What's next

  * To grant a principal access to your runtime template, see [Manage access to a runtime template](https://docs.cloud.google.com/colab/docs/manage-access-runtime-template).

  * To learn more about Compute Engine reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
