---
url: https://docs.cloud.google.com/functions/docs/tutorials/terraform/
title: Terraform Tutorial \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:04.330035+00:00
---

# Terraform Tutorial  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/tutorials/terraform/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  Terraform Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to deploy an HTTP function by uploading a function source code zip file to a Cloud Storage bucket, using [Terraform](https://docs.cloud.google.com/docs/terraform) to provision the resources. Terraform is an open source tool that lets you provision Google Cloud resources with declarative configuration files.

This tutorial uses a Node.js HTTP function as an example, but it also works with Python, Go, and Java HTTP functions. The instructions are the same regardless of which of these runtimes you are using.

When you deploy with Terraform, you must [upload your function's zipped source file to a Cloud Storage bucket (`source_archive_bucket`)](https://docs.cloud.google.com/storage/docs/uploading-objects), and also specify the Cloud Storage object name (`source_archive_object`) in the Terraform configuration. For more information, see the [Terraform specification guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function#source_archive_bucket-1).

Cloud Run functions copies the source file you upload in the `source_archive_bucket` to a bucket in your project with a bucket name that follows the format [`gcf-v2-sources-PROJECT_NUMBER-REGION`(Cloud Run functions)](https://docs.cloud.google.com/functions/docs/building), or [`gcf-sources-PROJECT_NUMBER-REGION` Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/building). This configuration varies depending on the CMEK dependency.

## Objectives

  * Learn how to use Terraform to deploy an HTTP function.



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

  4. Enable the Cloud Functions, Cloud Run, Cloud Build, Artifact Registry, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com&redirect=https%3A//docs.cloud.google.com/functions/docs/tutorials/terraform)

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

  10. Enable the Cloud Functions, Cloud Run, Cloud Build, Artifact Registry, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com,cloudfunctions.googleapis.com,storage.googleapis.com&redirect=https%3A//docs.cloud.google.com/functions/docs/tutorials/terraform)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

  14. Prepare your development environment.  


[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)




## Required roles

  * Users deploying functions must have the [Cloud Functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) (`roles/cloudfunctions.developer`) IAM role or a role that includes the same permissions. See also [Additional configuration for deployment](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

  * To get the permissions to access the Cloud Storage bucket, ask your administrator to grant the IAM identity that deploys the function the [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) role. For more details on Cloud Storage roles and permissions, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).




## Setting up your environment

In this tutorial, you run commands in Cloud Shell. Cloud Shell is a shell environment with the Google Cloud CLI already installed, including the Google Cloud CLI, and with values already set for your current project. Cloud Shell can take several minutes to initialize:

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

## Preparing the application

In Cloud Shell, perform the following steps:

  1. Clone the sample app repository to your Cloud Shell instance:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git

  2. Change to the directory that contains the Cloud Run functions sample code examples:
         
         cd terraform-docs-samples/functions/basic

The Node.JS sample used in this tutorial is a basic "Hello World" HTTP function. Here is the `main.tf` file:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = ">= 4.34.0"
             }
           }
         }
         
         resource "random_id" "default" {
           byte_length = 8
         }
         
         resource "google_storage_bucket" "default" {
           name                        = "${random_id.default.hex}-gcf-source" # Every bucket name must be globally unique
           location                    = "US"
           uniform_bucket_level_access = true
         }
         
         data "archive_file" "default" {
           type        = "zip"
           output_path = "/tmp/function-source.zip"
           source_dir  = "functions/hello-world/"
         }
         resource "google_storage_bucket_object" "object" {
           name   = "function-source.zip"
           bucket = google_storage_bucket.default.name
           source = data.archive_file.default.output_path # Add path to the zipped function source code
         }
         
         resource "google_cloudfunctions2_function" "default" {
           name        = "function-v2"
           location    = "us-central1"
           description = "a new function"
         
           build_config {
             runtime     = "nodejs22"
             entry_point = "helloHttp" # Set the entry point
             source {
               storage_source {
                 bucket = google_storage_bucket.default.name
                 object = google_storage_bucket_object.object.name
               }
             }
           }
         
           service_config {
             max_instance_count = 1
             available_memory   = "256M"
             timeout_seconds    = 60
           }
         }
         
         resource "google_cloud_run_service_iam_member" "member" {
           location = google_cloudfunctions2_function.default.location
           service  = google_cloudfunctions2_function.default.name
           role     = "roles/run.invoker"
           member   = "allUsers"
         }
         
         output "function_uri" {
           value = google_cloudfunctions2_function.default.service_config[0].uri
         }




## Initialize Terraform

In the `terraform-docs-samples/functions/basic` directory containing the `main.tf` file, run this command to add the necessary plugins and build the `.terraform` directory:
    
    
    terraform init
    

## Apply the Terraform configuration

In the same `terraform-docs-samples/functions/basic` directory containing the `main.tf` file, deploy the function by applying the configuration. When prompted, enter `yes`:
    
    
    terraform apply
    

## Test the function

  1. When the function finishes deploying, take note of the URI property or find it using the following command:
         
         gcloud functions describe function-v2 --gen2 --region=us-central1 --format="value(serviceConfig.uri)"
         

  2. Make a request to this URL to see your function's "Hello World" message. Note that the function is deployed requiring [authentication](https://docs.cloud.google.com/functions/docs/securing/authenticating). Therefore you must provide credentials in your request:
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" YOUR_FUNCTION_URL


**Note:** For security reasons, it is best practice to require authentication for HTTP function invocation. If required, you can enable unauthenticated invocation [after the function has been deployed](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#after_deployment).

## Clean up

After completing the tutorial, you can delete everything that you created so that you don't incur any further costs.

Terraform lets you remove all the resources defined in the configuration file by running the `terraform destroy` command in the `terraform-docs-samples/functions/basic` directory containing your `main.tf` file:
    
    
    terraform destroy
    

Enter `yes` to allow Terraform to delete your resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
