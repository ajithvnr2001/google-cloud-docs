---
url: https://docs.cloud.google.com/docs/terraform/create-vm-instance/
title: Quickstart: Create a Compute Engine VM instance using Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:17.945072+00:00
---

# Quickstart: Create a Compute Engine VM instance using Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/create-vm-instance/

  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Create a VM instance using Terraform

In this quickstart, you learn how to use Terraform to create a Compute Engine Virtual Machine (VM) instance and connect to that VM instance.

Hashicorp Terraform is an Infrastructure as code (IaC) tool that lets you provision and manage cloud infrastructure. _Terraform provider for Google Cloud_ (_Google Cloud provider_) lets you provision and manage Google Cloud infrastructure.

## Before you begin

  1. To use an online terminal with the gcloud CLI already set up, activate Cloud Shell:

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

  2. To install the Terraform CLI, follow the [HashiCorp instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).

  3. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  6. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/compute.instanceAdmin.v1`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For examples, see [ Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users). 
     * `ROLE`: The IAM role that you grant to your user account.



## Prepare the environment

  1. Clone the GitHub repository containing Terraform samples:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
         

  2. Go to the directory that contains the quickstart sample:
         
         cd terraform-docs-samples/compute/quickstart/create_vm
         




## Review the Terraform files

Review the `main.tf` file. This file defines the Google Cloud resources that you want to create.
    
    
    cat main.tf
    

The output is similar to the following
    
    
    resource "google_compute_instance" "default" {
      name         = "my-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "ubuntu-minimal-2210-kinetic-amd64-v20230126"
        }
      }
    
      network_interface {
        network = "default"
        access_config {}
      }
    }

This file describes the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance), which is the Terraform resource for the Compute Engine VM instance. `google_compute_instance` is configured to have the following properties:

  * `name` is set to `my-vm`.
  * `machine_type` is set to `n1-standard-1`.
  * `zone` is set to `us-central1-a`.
  * `boot_disk` sets the boot disk for the instance.
  * `network_interface` is set to use the default network in your Google Cloud project.



## Create the Compute Engine VM instance

  1. In Cloud Shell, run the following command to verify that Terraform is available:
         
         terraform
         

The output should be similar to the following:
         
         Usage: terraform [global options] <subcommand> [args]
         
         The available commands for execution are listed below.
         The primary workflow commands are given first, followed by
         less common or more advanced commands.
         
         Main commands:
           init          Prepare your working directory for other commands
           validate      Check whether the configuration is valid
           plan          Show changes required by the current configuration
           apply         Create or update infrastructure
           destroy       Destroy previously-created infrastructure
         
         

  2. Initialize Terraform by running the following command. This command prepares your workspace so Terraform can apply your configuration.
         
         terraform init
         

The output should be similar to the following:
         
         Initializing the backend...
         
         Initializing provider plugins...
         - Finding latest version of hashicorp/google...
         - Installing hashicorp/google v5.35.0...
         - Installed hashicorp/google v5.35.0 (signed by HashiCorp)
         
         Terraform has created a lock file .terraform.lock.hcl to record the provider
         selections it made above. Include this file in your version control repository
         so that Terraform can guarantee to make the same selections by default when
         you run "terraform init" in the future.
         
         Terraform has been successfully initialized!
         
         

  3. Validate the Terraform configuration by running the following command. This command takes the following actions:

     * Verifies that the syntax of `main.tf` is correct.
     * Shows a preview of the resources that will be created.
    
    terraform plan
    

The output should be similar to the following:
    
    Plan: 1 to add, 0 to change, 0 to destroy.
    
    Note: You didn't use the -out option to save this plan, so Terraform can't
    guarantee to take exactly these actions if you run "terraform apply" now.
    

  4. Apply the configuration to provision resources described in the `main.tf` file:
         
         terraform apply
         

When prompted, enter `yes`.

Terraform calls Google Cloud APIs to create the VM instance defined in the `main.tf` file.

The output should be similar to the following:
         
         Apply complete! Resources: 1 added, 0 changed, 0 destroyed
         




## Connect to the VM instance

Connect to the VM instance you just created by running the following command:
    
    
    gcloud compute ssh --zone=us-central1-a my-vm
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

In Cloud Shell, run the following command to delete the Terraform resources:
    
    
    terraform destroy
    

When prompted, enter `yes`.

The output should be similar to the following:
    
    
    Destroy complete! Resources: 1 destroyed.
    

## What's next

  * Learn how to [deploy a basic Flask web server using Terraform](https://docs.cloud.google.com/docs/terraform/deploy-flask-web-server).
  * Learn how to [store Terraform state in a Cloud Storage bucket](https://docs.cloud.google.com/docs/terraform/resource-management/store-state).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
