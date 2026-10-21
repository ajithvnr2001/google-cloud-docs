---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project/
title: Create a project \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:39.542325+00:00
---

# Create a project  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a project Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Google Distributed Cloud (GDC) air-gapped project for grouping your resources within an organization. Projects provide a lifecycle and policy boundary for resources, allowing for multiple groups of users to manage GDC resources separately.

This document is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group who are responsible for managing resources within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To perform the tasks in this document, you must complete the following:

  * To get the permissions that you need to create a project, ask your Organization IAM Admin to grant you the Project Creator role (`project-creator`).

  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).

  * To use Terraform, ensure you have it configured. For more information, see [Configure Terraform](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform).




## Create a new project

You can create a project to provide logical grouping of service resources. For example, you can create separate projects to hold resources for development, test, and production environments.

To get the permissions that you need to create a project, ask your Organization IAM Admin to grant you the Project Creator role. For more information on granting permissions, see the [Assign a role binding to the service identity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/service-identity#assign_a_role_binding_to_the_service_identity) section.

###  Console 

To create a new project using the GDC console, complete the following steps:

  1. In the navigation menu, click **Projects**.
  2. Click **Add project**.
  3. In the **Project name** field, enter a project name.
  4. Specify the billing account ID to associate with the project. To track project resource costs, your project must be linked to a billing account. For more information, see [Create and link billing accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts).
  5. Click **Continue**.
  6. Optional: Configure your project's networking capabilities. Clear the **Enable data exfiltration protection** checkbox to disable all egress traffic to other projects inside your organization.
  7. Click **Continue**.
  8. In the **Review** section, review the summary and click **Create**.
  9. To verify the new project is available, a message is displayed in the console: `Project PROJECT_NAME successfully created`.



###  gdcloud 

To create a new project using the gdcloud CLI, complete the following steps:

  1. To create a project, run:
         
         gdcloud projects create PROJECT_ID
         

Replace `PROJECT_ID` with the unique identifier for your new project.

**Important:** The gdcloud CLI doesn't support attaching a project to a Kubernetes cluster. After creating a project, you can attach it to a cluster using the GDC console. For more information, see [Attach project to a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#attach-project-to-cluster).
  2. Verify the new project is available:
         
         gdcloud projects list
         

The output is similar to the following:
         
         METADATA.NAME
         my-project
         

  3. [Link your new project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#link-bil-account-to-project-or-org) with a billing account. To track project resource costs, you must have an associated billing account linked to your project.




###  API 

To create a new project using the API directly, complete the following steps:

  1. Set an environment variable for the global management API server kubeconfig file:
         
         export KUBECONFIG=GLOBAL_API_SERVER_KUBECONFIG
         

If you don't have the global management API server kubeconfig file, [generate one](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).

  2. Create and apply the `Project` custom resource:
         
         kubectl --kubeconfig=${KUBECONFIG} apply -f - <<EOF
         apiVersion: resourcemanager.global.gdc.goog/v1
         kind: Project
         metadata:
           namespace: platform
           name: PROJECT_ID
         EOF
         

Replace `PROJECT_ID` with the unique identifier for your new project.

**Important:** The `Project` Kubernetes manifest doesn't support attaching a Kubernetes cluster. After your project is provisioned, you can attach it to a cluster using the GDC console. For more information, see [Attach project to a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#attach-project-to-cluster).
  3. Verify the new project is available:
         
         kubectl --kubeconfig=${KUBECONFIG} get projects -n platform
         

The output is similar to the following:
         
         NAME           READY
         my-project
         

  4. [Link your new project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#link-bil-account-to-project-or-org) with a billing account. To track project resource costs, you must have an associated billing account linked to your project.




###  Terraform 

To create a new project using Terraform, complete the following steps:

  1. Ensure you have Terraform configured and the appropriate permissions set. For more information, see the [Configure Terraform](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform) page.

  2. In a Terraform configuration file, insert the following code snippet:
         
         provider "kubernetes" {
           config_path = "GLOBAL_API_SERVER_KUBECONFIG"
         }
         

Replace `GLOBAL_API_SERVER_KUBECONFIG` with the path to the global management API server's kubeconfig file. If you don't have this kubeconfig file, [generate one](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).

  3. In a Terraform configuration file, such as `main.tf`, insert the following code snippet:
         
         resource "kubernetes_manifest" "project-create" {
           manifest = {
             "apiVersion" = "resourcemanager.global.gdc.goog/v1"
             "kind" = "Project"
             "metadata" = {
               "name" = "PROJECT_ID"
               "namespace" = "platform"
             }
           }
         }
         

Replace `PROJECT_ID` with the unique identifier for your new project.

**Important:** The `Project` Kubernetes manifest doesn't support attaching a Kubernetes cluster. After your project is provisioned, you can attach it to a cluster using the GDC console. For more information, see [Attach project to a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#attach-project-to-cluster).
  4. Apply the new project using Terraform:
         
         terraform apply
         

  5. [Link your new project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#link-bil-account-to-project-or-org) with a billing account. To track project resource costs, you must have an associated billing account linked to your project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
