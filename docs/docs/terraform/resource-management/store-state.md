---
url: https://docs.cloud.google.com/docs/terraform/resource-management/store-state/
title: Store Terraform state in a Cloud Storage bucket \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:37.570067+00:00
---

# Store Terraform state in a Cloud Storage bucket  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/resource-management/store-state/

  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



#  Store Terraform state in a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you learn how to store Terraform state in a Cloud Storage bucket.

By default, Terraform stores [state](https://www.terraform.io/docs/state/) locally in a file named `terraform.tfstate`. This default configuration can make Terraform usage difficult for teams when multiple users run Terraform at the same time and each machine has its own understanding of the current infrastructure.

To help you avoid such issues, this page shows you how to configure a [remote state](https://www.terraform.io/docs/state/remote.html) that points to a Cloud Storage bucket. Remote state is a feature of [Terraform backends](https://www.terraform.io/docs/backends).

## Objectives

This tutorial shows you how to do the following:

  * Use Terraform to provision a Cloud Storage bucket to store Terraform state.
  * Add templating in the Terraform configuration file to migrate the state from the local backend to the Cloud Storage bucket.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Cloud Storage](https://docs.cloud.google.com/storage/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

Cloud Storage incurs costs for storage, read and write operations, network egress, and replication.

The Cloud Storage bucket in this tutorial has [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled to keep the history of your deployments. Enabling Object Versioning increases storage costs, which you can mitigate by configuring [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to delete old state versions.

## Before you begin

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

Cloud Shell is preinstalled with Terraform.

  2. If you're using a local shell, perform the following steps:

     * [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).
     * Create local authentication credentials for your user account: 
           
           gcloud auth application-default login

If an authentication error is returned, confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

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

  5. Enable the Cloud Storage API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable storage.googleapis.com

  6. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For examples, see [ Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users). 
     * `ROLE`: The IAM role that you grant to your user account.

Alternately, you can create a [custom IAM role](https://docs.cloud.google.com/iam/docs/roles-overview#custom) that contains the following permissions:

     * `storage.buckets.create`
     * `storage.buckets.list`
     * `storage.objects.get`
     * `storage.objects.create`
     * `storage.objects.delete`
     * `storage.objects.update`

As a best practice, we recommend that access to the bucket and the state files stored there is controlled. Only a small set of users (for example, the main cloud administrator and the person acting as the alternative or backup administrator) should have admin permissions for the bucket. The other developers should have permissions to only write and read objects in the bucket.




## Prepare the environment

  1. Clone the GitHub repository containing Terraform samples:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
         

  2. Change to the working directory:
         
         cd terraform-docs-samples/storage/remote_terraform_backend_template
         




## Review the Terraform files

  1. Review the `main.tf` file:
         
         cat main.tf
         

The output is similar to the following
         
         resource "random_id" "default" {
           byte_length = 8
         }
         
         resource "google_storage_bucket" "default" {
           name     = "${random_id.default.hex}-terraform-remote-backend"
           location = "US"
         
           force_destroy               = false
           public_access_prevention    = "enforced"
           uniform_bucket_level_access = true
         
           versioning {
             enabled = true
           }
         }
         
         resource "local_file" "default" {
           file_permission = "0644"
           filename        = "${path.module}/backend.tf"
         
           # You can store the template in a file and use the templatefile function for
           # more modularity, if you prefer, instead of storing the template inline as
           # we do here.
           content = <<-EOT
           terraform {
             backend "gcs" {
               bucket = "${google_storage_bucket.default.name}"
             }
           }
           EOT
         }

This file describes the following resources:

     * `random_id`: This is appended to the Cloud Storage bucket name to ensure a unique name for the Cloud Storage bucket.
     * `google_storage_bucket`: The Cloud Storage bucket to store the state file. This bucket is configured to have the following properties: 
       * `force_destroy` is set to `false` to ensure that the bucket is not deleted if there are objects in it. This ensures that the state information in the bucket isn't accidentally deleted.
       * `public_access_prevention` is set to `enforced` to make sure the bucket contents aren't accidentally exposed to the public.
       * `uniform_bucket_level_access` is set to `true` to allow controlling access to the bucket and its contents using [IAM permissions instead of access control lists](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
       * `versioning` is enabled to ensure that earlier versions of the state are preserved in the bucket.
     * `local_file`: A local file. The contents of this file instructs Terraform to use Cloud Storage bucket as the remote backend once the bucket is created.



## Provision the Cloud Storage bucket

  1. Initialize Terraform:
         
         terraform init
         

When you run `terraform init` for the first time, the Cloud Storage bucket that you specified in the `main.tf` file doesn't exist yet, so Terraform initializes a local backend to store state in the local file system.

  2. Apply the configuration to provision resources described in the `main.tf` file:
         
         terraform apply
         

When prompted, enter `yes`.

When you run `terraform apply` for the first time, Terraform provisions the Cloud Storage bucket for storing the state. It also creates a local file; the contents of this file instruct Terraform to use the Cloud Storage bucket as the remote backend to store state.




## Migrate state to Cloud Storage bucket

  1. Migrate Terraform state to the remote Cloud Storage backend:
         
         terraform init -migrate-state
         

Terraform detects that you already have a state file locally and prompts you to migrate the state to the new Cloud Storage bucket. When prompted, enter `yes`.




After running this command, your Terraform state is stored in the Cloud Storage bucket. Terraform pulls the latest state from this bucket before running a command, and pushes the latest state to the bucket after running a command.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

  1. Open the `main.tf` file.

  2. In the `google_storage_bucket.default` resource, update the value of `force_destroy` to `true`.

  3. Apply the updated configuration:
         
         terraform apply
         

When prompted, enter `yes`.

  4. Delete the state file:
         
         rm backend.tf
         

  5. Reconfigure the backend to be local:
         
         terraform init -migrate-state
         

When prompted, enter `yes`.

  6. Run the following command to delete the Terraform resources:
         
         terraform destroy
         

When prompted, enter `yes`.




## What's next

  * Learn how to [manage infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code)
  * [Learn about policy validation](https://docs.cloud.google.com/docs/terraform/policy-validation).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
