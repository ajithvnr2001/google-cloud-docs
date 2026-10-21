---
url: https://docs.cloud.google.com/compute/docs/quickstart-mig/
title: Create a managed instance group (MIG) \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:50.986400+00:00
---

# Create a managed instance group (MIG)  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/quickstart-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a managed instance group (MIG)

Learn how to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in Compute Engine by using the Google Cloud console.

A MIG is a collection of virtual machine (VM) instances that you can manage as a single entity. MIGs support features such as autohealing, autoscaling, load balancing, multiple zone coverage, and stateful workloads.

Each VM in a MIG is based on an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates). You need to create an instance template before you create a MIG.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=compute--instance-groups--quickstart-mig)

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

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Compute Engine API.

[ Enable the API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)




### Required roles

To get the permissions that you need to create an instance template and a MIG, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance template and a MIG. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance template and a MIG:

  * Create an instance template: `compute.instanceTemplates.create`
  * Create a MIG: `compute.instanceGroupManagers.create`
  * Delete a MIG: `compute.instanceGroupManagers.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an instance template

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. To create a template that uses an Ubuntu OS, perform the following steps:

     1. In the **Boot disk** section, click **Change**.

     2. In the **Boot disk** pane that appears, in the **Operating system** list, select **Ubuntu**.

     3. Click **Select**.

The template applies these settings to all the VMs that are created using this template. Note the name of the template, which you use later in the tutorial.

  4. To create the instance template, click **Create**.




Allow a few minutes for Compute Engine to create the template. When the template is ready, it's listed on the **Instance templates** page.

## Create a MIG by using the instance template

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group** , and then perform the following steps:

     1. In the **Name** field, accept the default name or enter `quickstart-instance-group-1`.

     2. In the **Instance template** list, select the instance template that you created earlier.

     3. In the **Location** section, ensure that **Single zone** is selected.

     4. In the **Region** field, select a region where you want to create the MIG.

     5. In the **Autoscaling** section, accept the default settings unless you need to modify them.

  3. To create the MIG, click **Create**.




Allow a few minutes for Compute Engine to create the group and its VMs. After the group is ready, it's listed on the **Instance groups** page.

You have successfully created a managed instance group.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the resources

If you used an existing Google Cloud project, delete the resources that you created to avoid incurring charges to your account:

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the instance group that you want to delete.

  3. Click **Delete**.

  4. When you're prompted, enter the required value, and then click **Delete**.




### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [work with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).
  * Learn about other [basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * Learn more about [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) and about using different autoscaling signals to automatically create VMs when load increases and delete VMs when load goes down.
  * To improve the availability of your application, set up an [application-based autohealing health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs). An application-based health check tells the MIG to automatically recreate unhealthy VMs if your application fails to respond as expected.
  * To further improve availability, learn about distributing a MIG's VMs across multiple zones within a region by [creating a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * To update the configuration of the VMs in your MIG, create and apply a new instance template. For more information, see [Applying new configurations to VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).
  * If you need to support a stateful workload, learn how to [add a stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
