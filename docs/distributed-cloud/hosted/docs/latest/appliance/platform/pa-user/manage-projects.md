---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/manage-projects/
title: Manage projects and their resources \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:41.653217+00:00
---

# Manage projects and their resources  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/manage-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage projects and their resources Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance projects form the basis for creating, enabling, and using all GDC services including managing APIs, adding and removing collaborators, and managing permissions for GDC resources.

This page explains how to manage GDC projects using the GDC console, gdcloud CLI, and `kubectl` CLI.

## Before you begin

Before viewing or managing projects and their resources, you must request the necessary permissions and prepare your environment.

### Request IAM roles

Contact your Organization IAM Admin to request the following roles based on the tasks you need to perform:

  * **Project Editor** (`project-editor`): update, view, and delete an existing project and its resources.
  * **Project Viewer** (`project-viewer`): view an existing project and its resources.



### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## View project details

You can view your project's metadata to review current configurations such as labels and network settings.

###  Console 

  1. Open the navigation menu and select **Projects**.

  2. Click the project you want to view details for:




###  gdcloud 

To list the metadata for a specific project, run:
    
    
    gdcloud projects describe PROJECT_ID
    

Replace `PROJECT_ID` with the unique identifier for your project.

## Check project resources

You can check project resources to monitor the segmentation of resources within an organization. You can also check user and group access policies, which you define per project to provide boundaries between projects.

### List role bindings in a project

To list the role bindings in a project, run:
    
    
    kubectl get rolebindings -n PROJECT_NAMESPACE
    

For more information on role bindings, see [Grant access to resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

## Select a project or organization

In the GDC console, you can select a project or organization using the project picker to interact with the service resources nested under that parent resource. For example, a virtual machine (VM) is project-scoped.

The project picker automatically transitions between the most recent parent resource types when the context of the child resource changes. For example, when you access a project-scoped resource when you have an organization selected in the project picker, the picker automatically selects the last used project to seamlessly change the resource scope. Likewise, the organization is autoselected when accessing organization-scoped resources.

**Note:** If you've never chosen a project from the project picker when accessing a project-scoped resource, you must manually select a project from the dialog.

To interact with GDC resources nested in a parent resource, you must first select the organization or project to work in:

  1. From the dashboard, click the project picker drop-down.

![Select the project or organization to work in from the project picker.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/images/project-picker.png)

  2. In the **Projects** window that appears, select your project or organization.

  3. Click **Open**.




## Update a project

There are a subset of configurations for your project that can be updated after creation, such as project name and data exfiltration protection. You can update these configurations as your usage of the project evolves.

For example, you can edit the project's name by completing the following steps:

###  Console 

  1. Open the navigation menu and select **Projects**.

  2. Click the project you want to edit.

  3. Click edit **Edit** next to the **Project display name** field.

  4. Provide the updated project name and click **Save**.




###  gdcloud 

Run the following command:
    
    
    gdcloud projects update PROJECT_ID --name=PROJECT_NAME
    

Replace the following variables:

  * `PROJECT_ID`: the unique identifier for your project.
  * `PROJECT_NAME`: the new name for the project.



You can replace the `--name` parameter with any editable project field. Run `gdcloud projects update --help` for more options.

## View projects in an organization

As an Administrator, you can only view and list projects you have access to with IAM roles. The Organization IAM Admin role can view and list all projects in the organization.

###  Console 

To view all projects in an organization, go to the console's navigation menu and select **Projects**.

###  gdcloud 

To view all projects you have access to in an organization, run:
    
    
    gdcloud projects list
    

You cannot list projects you don't have permission to access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
