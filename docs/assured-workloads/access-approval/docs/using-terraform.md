---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/using-terraform/
title: Enabling Access Approval using Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:20.426911+00:00
---

# Enabling Access Approval using Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/using-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enabling Access Approval using Terraform

[Terraform](https://terraform.io) is an open-source infrastructure-as-code software tool that lets you manage your Access Approval requests. Terraform lets you perform all the actions that you can perform using Access Approval APIs.

This page describes how you can enable Access Approval using Terraform. This tutorial uses the [Google Cloud Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

## Objective

This tutorial teaches how you can create a Terraform configuration file that:

  * Sets email addresses for Access Approval request notifications.
  * Enables Access Approval for all supported Google Cloud products. For the complete list of Google Cloud products supported by Access Approval, see [Supported services](https://docs.cloud.google.com/assured-workloads/access-approval/docs/supported-services).



## Before you begin

  * To use Access Approval and Access Transparency, your organization must meet specific support requirements. For more information, see [Requirements for using Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview#requirements).
  * Enable [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) on your organization. For more information, see [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).
  * Ensure that you have the **Access Approval Config Editor** (`roles/accessapproval.configEditor`) Identity and Access Management (IAM) role. For more information about IAM roles for Access Approval, see [Access Approval roles](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval).



## Creating a Google Cloud project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Access Approval API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=accessapproval.googleapis.com)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Access Approval API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=accessapproval.googleapis.com)




## Installing Google Cloud CLI

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

When prompted, choose the project that you selected or created earlier.

If you already have Google Cloud CLI installed, update it using the following command:
    
    
    gcloud components update
    

## Creating a Terraform configuration file

  1. [Open Cloud Shell](https://shell.cloud.google.com) to launch a standalone Cloud Shell session.
  2. Open a workspace.
  3. Create a new folder.
  4. Add a Terraform configuration file named `main.tf` to this folder.
  5. Copy the following resource, and paste it in your `main.tf` file.

### main.tf
         
         variable "parent_value" {
         type        = string
         }
         
         variable "email_1" {
         type        = string
         }
         
         variable "email_2" {
         type        = string
         }
         
         resource "google_folder" "my_folder" {
         display_name = "my-folder"
         parent       = var.parent_value
         # parent = "organizations/123456789"
         }
         
         resource "google_folder_access_approval_settings" "folder_access_approval" {
         folder_id           = google_folder.my_folder.folder_id
         notification_emails = [var.email_1, var.email_2]
         
         enrolled_services {
           cloud_product = "all"
           }
         }
         

Enter values for the following variables:

     * `email_1` and `email_2`: provide the email addresses of users who you want to set as reviewers for the access requests for this project.
**Note:** These users must have the IAM roles with required permissions to view or approve an Access Approval request. To ensure these users have sufficient permissions, follow these steps:  

     1. Go to the [**IAM** page](https://console.cloud.google.com/iam-admin/iam) in the Google Cloud console.
     2. To enable a user or service account to approve access requests for a project, grant them the **Access Approval Approver** (`roles/accessapproval.approver`) IAM role.
     * `parent_value`: name of the folder in which you want to create the `my_folder` folder. For more information about folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).




## Running the Terraform configuration file

Run the following commands in Cloud Shell.

  1. Initialize Terraform in the directory.
         
         terraform init
         

  2. Run the created Terraform configuration file.
         
         terraform apply
         

  3. When prompted to confirm if you want to run the configuration file, enter **yes**.




For more information about operating Access Approval with Terraform, see this Terraform document: [google_folder_access_approval_settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/folder_access_approval_settings).

## What's next

  * [Using Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform)
  * [Using Terraform with Access Approval](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/folder_access_approval_settings)
  * [Getting started with Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform)
  * [Kickstart Terraform on Google Cloud with Cloud Shell](https://hashicorp.com/blog/kickstart-terraform-on-gcp-with-google-cloud-shell)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
