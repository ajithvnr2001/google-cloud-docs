---
url: https://docs.cloud.google.com/functions/docs/tutorials/terraform-pubsub/
title: Terraform Pub/Sub Tutorial \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:35.323626+00:00
---

# Terraform Pub/Sub Tutorial  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/tutorials/terraform-pubsub/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  Terraform Pub/Sub Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to deploy a Pub/Sub function by uploading a function source code zip file to a Cloud Storage bucket, using [Terraform](https://docs.cloud.google.com/docs/terraform) to provision the resources. Terraform is an open source tool that lets you provision Google Cloud resources with declarative configuration files

This tutorial uses a Node.js function as an example, but it also works with Python, Go, and Java functions. The instructions are the same regardless of which of these runtimes you are using. See Hashicorp's [reference pages](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function) for details on using Terraform with the Cloud Functions v2 API.

## Objectives

  * Learn how to use Terraform to deploy a Pub/Sub function.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run functions](https://cloud.google.com/functions/pricing-overview)
  * [Cloud Build](https://cloud.google.com/build/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)



For details, see [Cloud Run functions pricing](https://cloud.google.com/functions/pricing-overview). 

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Functions, Cloud Build, Artifact Registry, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com&redirect=https%3A//docs.cloud.google.com/functions/docs/tutorials/terraform-pubsub)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Functions, Cloud Build, Artifact Registry, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com&redirect=https%3A//docs.cloud.google.com/functions/docs/tutorials/terraform-pubsub)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

  14. Grant [`roles/run.invoker`](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) and the [`roles/cloudbuild.builds.builder`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) to the default compute service account.
  15. Prepare your development environment.  


[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)




## Setting up your environment

In this tutorial, you run commands in Cloud Shell. Cloud Shell is a shell environment with the Google Cloud CLI already installed, including the Google Cloud CLI, and with values already set for your current project. Cloud Shell can take several minutes to initialize:

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

## Preparing the application

In Cloud Shell, perform the following steps:

  1. Clone the sample app repository to your Cloud Shell instance:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git

  2. Change to the directory that contains the Cloud Run functions sample code:
         
         cd terraform-docs-samples/functions/pubsub

The Node.js sample used in this tutorial is a basic "Hello World" Pub/Sub function. Here is the `main.tf` file:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = ">= 4.34.0"
             }
           }
         }
         
         resource "random_id" "bucket_prefix" {
           byte_length = 8
         }
         
         
         resource "google_service_account" "default" {
           account_id   = "test-gcf-sa"
           display_name = "Test Service Account"
         }
         
         resource "google_pubsub_topic" "default" {
           name = "functions2-topic"
         }
         
         resource "google_storage_bucket" "default" {
           name                        = "${random_id.bucket_prefix.hex}-gcf-source" # Every bucket name must be globally unique
           location                    = "US"
           uniform_bucket_level_access = true
         }
         
         data "archive_file" "default" {
           type        = "zip"
           output_path = "/tmp/function-source.zip"
           source_dir  = "function-source/"
         }
         
         resource "google_storage_bucket_object" "default" {
           name   = "function-source.zip"
           bucket = google_storage_bucket.default.name
           source = data.archive_file.default.output_path # Path to the zipped function source code
         }
         
         resource "google_cloudfunctions2_function" "default" {
           name        = "function"
           location    = "us-central1"
           description = "a new function"
         
           build_config {
             runtime     = "nodejs22"
             entry_point = "helloPubSub" # Set the entry point
             environment_variables = {
               BUILD_CONFIG_TEST = "build_test"
             }
             source {
               storage_source {
                 bucket = google_storage_bucket.default.name
                 object = google_storage_bucket_object.default.name
               }
             }
           }
         
           service_config {
             max_instance_count = 3
             min_instance_count = 1
             available_memory   = "256M"
             timeout_seconds    = 60
             environment_variables = {
               SERVICE_CONFIG_TEST = "config_test"
             }
             ingress_settings               = "ALLOW_INTERNAL_ONLY"
             all_traffic_on_latest_revision = true
             service_account_email          = google_service_account.default.email
           }
         
           event_trigger {
             trigger_region = "us-central1"
             event_type     = "google.cloud.pubsub.topic.v1.messagePublished"
             pubsub_topic   = google_pubsub_topic.default.id
             retry_policy   = "RETRY_POLICY_RETRY"
           }
         }




## Initialize Terraform

In the `terraform-docs-samples/functions/pubsub` directory containing the `main.tf` file, run this command to add the necessary plugins and build the `.terraform` directory:
    
    
    terraform init
    

## Validate the Terraform configuration

Preview the Terraform configuration. This step is optional, but it lets you verify that the syntax of `main.tf` is correct. This command shows a preview of the resources that will be created:
    
    
    terraform plan
    

## Apply the Terraform configuration

Deploy the function by applying the configuration. When prompted, enter `yes`:
    
    
    terraform apply
    

## Triggering the function

To test the Pub/Sub function:

  1. Publish a message to the topic (in this example, the topic name is `functions2-topic`):
         
         gcloud pubsub topics publish TOPIC_NAME --message="Friend"

  2. Read the function logs to see the result, where `FUNCTION_NAME` is the name of your function (in this example, the function name is `function`):
         
         gcloud functions logs read FUNCTION_NAME

You should see logging output that includes your new "Friend" message.

**Note:** Logs might take a few moments to appear. If you don't see them immediately, check again in a minute or two.



## Clean up

After completing the tutorial, you can delete everything that you created so that you don't incur any further costs.

Terraform lets you remove all the resources defined in the configuration file by running the `terraform destroy` command:
    
    
    terraform destroy
    

Enter `yes` to allow Terraform to delete your resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
