---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project/
title: Create a project \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:02.444204+00:00
---

# Create a project  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create a project Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create a Google Distributed Cloud (GDC) air-gapped appliance project for grouping your resources together within an environment. Projects provide a lifecycle and policy boundary for resources, allowing for multiple groups of users to manage GDC resources separately.

This page is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group, who are responsible for managing resources within their environment.

## Before you begin

To get the permissions needed to create a project, ask your Organization IAM Admin to grant you the Project Creator role (`project-creator`).

The following are used to identify your project:

  * **Project name** : A human-readable name for your project.

The project name isn't used by any GDC APIs. You can edit the project name at any time during or after project creation. Project names don't need to be unique.

Projects have the following name requirements:

    * 4 to 30 characters in length.
    * Contains lowercase letters, numbers, periods, or hyphens.
  * **Project ID** : A globally unique identifier for your project.

A project ID is a unique string used to differentiate your project from all others in GDC. You can only modify the project ID when you're creating the project.

**Note:** The namespaces propagated by a project are the same as the project name.

Project IDs have the following requirements:

    * 6 to 30 characters in length.
    * Contains lowercase letters, numbers, and hyphens.
    * Starts with a letter.
    * Must not start with the prefix `g-`, such as `g-project`.
    * Must not end with a hyphen.
    * Must not end with the string `-cluster` or `-system`. The `-system` suffix is reserved for projects created by GDC.
    * Must not be in use or previously used; this includes deleted projects.
  * **Project number** : An automatically generated unique identifier for your project.




Don't include sensitive information in your project name, project ID, or other resource names. The project ID is used in the name of many other GDC resources, and any reference to the project or related resources exposes the project ID and resource name.

## Create a new project

You can create a project to provide logical grouping of service resources. For example, you can create separate projects to hold resources for development, test, and production environments.

To get the permissions that you need to create a project, ask your Organization IAM Admin to grant you the Project Creator role. For more information on granting permissions, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

###  Console 

To create a new project using the GDC console, complete the following steps:

  1. In the navigation menu, click **Projects**.
  2. Click **Add project**.
  3. In the **Project name** field, enter a project name.
  4. Click **Next**.
  5. Select the existing clusters to attach to the project. Click **Next**.

**Important:** Clusters must be attached to at least one project.
  6. Optional: Configure your project's networking capabilities. Clear the **Enable data exfiltration protection** checkbox to disable all egress traffic to other projects inside your organization.

  7. Click **Next**.

  8. In the **Review** section, review the summary and click **Create**.

  9. To verify the new project is available, a message is displayed in the console: `Project PROJECT_NAME successfully created`.




###  gdcloud 

To create a new project using the gdcloud CLI, complete the following steps:

  1. Ensure you have the gdcloud CLI installed. For more information, see the gdcloud CLI [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download_and_install_the) page.

  2. To create a project:
         
         gdcloud projects create PROJECT_ID
         

Replace `PROJECT_ID` with the unique identifier for your new project.

  3. To verify the new project is available, run:
         
         gdcloud projects list
         




###  API 

To create a new project using the API directly, apply a custom resource to your GDC instance:

To create a new project using the `kubectl` CLI, complete the following steps:

  1. Create and apply the `Project` custom resource:
         
         kubectl apply -f - <<EOF
         apiVersion: resourcemanager.gdc.goog/v1
         kind: Project
         metadata:
             namespace: platform
             name: PROJECT_NAME
         EOF
         

Replace `PROJECT_NAME` with the name of your project.

  2. Verify the new project is available:
         
         kubectl get namespaces
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
