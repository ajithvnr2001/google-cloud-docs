---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects/
title: Select and view projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:06.723438+00:00
---

# Select and view projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Select and view projects Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to select a Google Distributed Cloud (GDC) air-gapped project and view details of all projects to which you have access. GDC projects form the basis for creating, enabling, and using all GDC services including managing APIs, adding and removing collaborators, and managing permissions for GDC resources.

This document is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group, who are responsible for managing resources within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To perform the tasks in this document, you must complete the following requirements:

  * To get the permissions that you need to view a project and its resources, ask your IAM Org Admin to grant you the Project Viewer role (`project-viewer`).

  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).




## View project details

You can view your project's metadata to review current configurations, such as labels and network settings.

###  Console 

  1. Open the navigation menu and select **Projects**.

  2. Click the project you want to view details for.




![View project details such as project name and network settings.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/project-details.png)

###  gdcloud 

  * To list the metadata for a specific project, run:
        
        gdcloud projects describe PROJECT_ID
        

Replace `PROJECT_ID` with the unique identifier for your project.




## Check project resources

You can check project resources to monitor the segmentation of resources within an organization. You can also check user and group access policies, which you define per project to provide boundaries between projects.

### Check a cluster

You can check that a project is attached to a Kubernetes cluster, which is required for the container workloads that reside in your project.

  * Print information about a project's cluster:
        
        kubectl describe clusters CLUSTER_NAME -n CLUSTER_NAMESPACE
        




For more information on attaching projects to a cluster, see [Move clusters in project hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#move-clusters).

### List role bindings in a project

You can list the role bindings associated with your project namespace to monitor the roles to which users within the project are assigned.

  * List the role bindings in a project:
        
        kubectl get rolebindings -n PROJECT_NAMESPACE
        




For more information on project role bindings, see the [Assign a role binding to the service identity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/service-identity#assign_a_role_binding_to_the_service_identity) documentation.

## View projects in an organization

You can view and list projects you have access to with IAM roles.

The GDC console and gdcloud CLI don't list system projects, such as those hosted in the `gpc-system` namespace. To view system projects you have access to, you must call the API directly with the kubectl CLI.

###  Console 

  * To view all projects in an organization, go to the navigation menu and select **Projects**.

You cannot list system projects or projects you don't have permission to access.




###  gdcloud 

  * To view all projects you have access to in an organization, run:
        
        gdcloud projects list
        

You cannot list system projects or projects you don't have permission to access.




###  API 

  * To view all projects you have access to in an organization, run:
        
        kubectl get projects --all
        

You cannot list projects you don't have permission to access.




## Select a project or organization

In the GDC console, you can select a project or organization using the project picker to interact with the service resources that belong to that parent resource. For more information about how resources are organized, see the [GDC resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy). For example, a Kubernetes cluster is organization-scoped, whereas a virtual machine (VM) is project-scoped.

The project picker automatically transitions between the most recent parent resource types when the context of the child resource changes. For example, when you access a project-scoped resource when you have an organization selected in the project picker, the picker automatically selects the last used project to seamlessly change the resource scope. Likewise, the organization is autoselected when accessing organization-scoped resources.

**Note:** If you've never chosen a project from the project picker when accessing a project-scoped resource, you must manually select a project from the dialog.

To interact with GDC resources that belong to a parent resource, you must first select the organization or project to work in:

  1. From the dashboard, click the project picker drop-down.

![Select the project or organization to work in from the project picker.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/project-picker.png)

  2. In the **Projects** window that appears, select your project or organization.

  3. Click **Open**.




## What's next

  * [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project)
  * [Delete a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-a-project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
