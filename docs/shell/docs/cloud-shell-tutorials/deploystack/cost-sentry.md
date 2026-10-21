---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/cost-sentry/
title: Cost Sentry \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.337516+00:00
---

# Cost Sentry  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/cost-sentry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Cost Sentry Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-costsentry.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-costsentry.svg)

Cost Sentry is a set of scripts and configurations that allow you to shut down resources when Google Cloud Billing Budgets are exceeded.

This script consists of the following components :

  * Events - Queue - Pub/Sub
  * Billing - Cost Controls - Budgets
  * Events - Event Handling - Cloud Functions
  * Compute - VMs - Compute Engine
  * Compute - Serverless - Cloud Run



This script will set up a budget, a messaging queue, and Cloud Function to manage all this. It then spins up a sample VM and a container backed service that is managed by the system.

**Warning:** By default Cost Sentry will only shut down resources that it sets up. This is to prevent accidental shut downs of your resources. You can try this safely without worrying about it affecting existing infrastructure. 

* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-cost-sentry&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-cost-sentry)

* * *

## Cost Sentry components

The Cost Sentry architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_pubsub.svg) | **Google Cloud Pub/Sub** |  Google Cloud Pub/Sub is a messaging bus for integrating applications on different services on different cloud components into an integrated system.  |  [smart_display](https://www.youtube.com/watch?v=jLI-84UjZLE) |  [description](https://cloud.google.com/pubsub/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=pubsub--publish_receive_messages_console)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_billing.svg) | **Billing Budgets** |  Billing Budgets allow you to get notified and take action when your billing surpasses thresholds that you set.  |  [smart_display](https://www.youtube.com/watch?v=F4omjjMZ54k) |  [description](https://cloud.google.com/billing/docs/how-to/budgets) |  [keyboard](https://console.cloud.google.com/?tutorial=billing_create_budgets)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_functions.svg) | **Cloud Functions** |  Cloud Functions is a functions a service platform that allows you to listen for Cloud Storage file uploads and run code to create thumbnails of them.  |  [smart_display](https://www.youtube.com/watch?v=vM-2O-uKBNQ) |  [description](https://cloud.google.com/functions/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=functions_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_run.svg) | **Cloud Run** |  Cloud Run allows you to run applications in a container, but in a serverless way, no having to configure number of instances, processors, or memory. Upload a container, get a url.  |  [smart_display](https://www.youtube.com/watch?v=nhwYc4StHIc) |  [description](https://cloud.google.com/run/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_run_quickstart_index)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Cost Sentry. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable Services

Google Cloud Services are disabled in a project by default. To use Cost Sentry, activate the following services:

  * Billing Budgets - track billing and manage billing alerts.
  * Cloud Build - create container images and deploy to Cloud Run.
  * Compute Engine - implement virtual machines and networking services, like load balancing.
  * Cloud Functions - respond to service platform events.
  * Cloud Run - host containers in a serverless environment, and provide URLs to access the application.


    
    
    variable "gcp_service_list" {
            description = "The list of apis necessary for the project"
            type        = list(string)
            default = [
                "cloudresourcemanager.googleapis.com",
                "cloudbilling.googleapis.com",
                "billingbudgets.googleapis.com",
                "cloudbuild.googleapis.com",
                "compute.googleapis.com",
                "cloudfunctions.googleapis.com",
                "storage.googleapis.com",
                "run.googleapis.com"
            ]
    }
    
    resource "google_project_service" "all" {
        for_each           = toset(var.gcp_service_list)
        project            = var.project_number
        service            = each.key
        disable_on_destroy = false
    }
    

#### Create Pub/Sub channel

Creates a Pub/Sub channel to listen for billing budget events and respond with Cloud Functions
    
    
    resource "google_pubsub_topic" "costsentry" {
        name = "${var.basename}-billing-channel"
        project    = var.project_number
    }
    

#### Create Cloud Run Service to enforce

Create a sample Cloud Run service on which to run billing enforcement.
    
    
    resource "google_cloud_run_service" "app" {
        name     = "${var.basename}-run-service"
        location = var.region
        project  = var.project_id
    
        metadata {
            labels = {"${var.label}"=true}
        }
    
        template {
            spec {
                containers {
                    image = "us-docker.pkg.dev/cloudrun/container/hello"
                }
            }
    
            metadata {
                annotations = {
                    "autoscaling.knative.dev/maxScale" = "1000"
                    "run.googleapis.com/client-name"   = "terraform"
                }
            }
        }
        autogenerate_revision_name = true
        depends_on = [google_project_service.all]
    }
    

#### Create VM instance

Create a sample Compute Engine instance on which to run enforcement.
    
    
    resource "google_compute_instance" "example" {
        name         = "${var.basename}-example"
        machine_type = "n1-standard-1"
        zone         = var.zone
        project      = var.project_id
        tags                    = ["http-server"]
        labels = {"${var.label}"=true}
    
        boot_disk {
            auto_delete = true
            device_name = "${var.basename}-example"
            initialize_params {
                image = "family/debian-10"
                size  = 200
                type  = "pd-standard"
            }
        }   
    
        network_interface {
            network = "default"
            access_config {
            // Ephemeral public IP
            }
        }
    
        depends_on = [google_project_service.all]
    }
    

#### Create a budget

Creates a budget to monitor spending on in your projects.
    
    
    provisioner "local-exec" {
        command = <<-EOT
        gcloud beta billing budgets create --display-name ${var.basename}-budget \
        --billing-account ${var.billing_account} --budget-amount ${var.budgetamount} \
        --all-updates-rule-pubsub-topic=projects/${var.project_id}/topics/${var.basename}-billing-channel
        EOT
    }
    

#### Create a service account and set permissions

Creates a service account for the Cloud Function calls.
    
    
    resource "google_service_account" "functions_accounts" {
        account_id   = local.safunctionuser
        description  = "Service Account for the costsentry to run as"
        display_name = local.safunction
        project      = var.project_number
    }
    

#### Set permissions

The following command sets IAM roles and permissions that allow Cloud Build to deploy the required services.

The series of commands implements the following: Grants permission to the Cloud Function Service Account to manage Cloud Run. Grants permission to the Cloud Function Service Account to stop Compute Engine instances. Grants permission to the Cloud Build Service Account to act on behalf of the Compute service account.
    
    
    variable "build_roles_list" {
            description = "The list of roles that fucntions needs for"
            type        = list(string)
            default = [
                "roles/run.admin",
                "roles/compute.instanceAdmin",
                "roles/iam.serviceAccountUser"
            ]
    }
    
    resource "google_project_iam_member" "allbuild" {
        for_each   = toset(var.build_roles_list)
        project    = var.project_number
        role       = each.key
        member     = "serviceAccount:${google_service_account.functions_accounts.email}"
        depends_on = [google_project_service.all,google_service_account.functions_accounts]
    }
    

#### Deploy a Cloud Function

The following command deploys a Cloud Function that deactivates resources when an alert is triggered.
    
    
    resource "google_storage_bucket" "function_bucket" {
        name     = "${var.project_id}-function-deployer"
        project  = var.project_number
        location = var.location
    }
    
    resource "null_resource" "cloudbuild_function" {
        provisioner "local-exec" {
            command = <<-EOT
            cp code/function/function.go .
            cp code/function/go.mod .
            zip index.zip function.go
            zip index.zip go.mod
            rm go.mod
            rm function.go
            EOT
        }
    
        depends_on = [
            google_project_service.all
        ]
    }
    
    resource "google_storage_bucket_object" "archive" {
        name   = "index.zip"
        bucket = google_storage_bucket.function_bucket.name
        source = "index.zip"
        depends_on = [
            google_project_service.all,
            google_storage_bucket.function_bucket,
            null_resource.cloudbuild_function
        ]
    }
    
    resource "google_cloudfunctions_function" "function" {
        name    = var.basename
        project = var.project_id
        region  = var.region
        runtime = "go116"
        service_account_email = google_service_account.functions_accounts.email
        available_memory_mb   = 128
        source_archive_bucket = google_storage_bucket.function_bucket.name
        source_archive_object = google_storage_bucket_object.archive.name
        entry_point           = "LimitUsage"
        event_trigger {
            event_type = "google.pubsub.topic.publish"
            resource   = google_pubsub_topic.costsentry.name
        }
    
        environment_variables = {
            GOOGLE_CLOUD_PROJECT = var.project_id
            LABEL= var.label
        }
    
        depends_on = [
            google_storage_bucket.function_bucket,
            google_storage_bucket_object.archive,
            google_project_service.all
        ]
    }
    

* * *

## Conclusion

Once run you should now have a cost control solution running in your project. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
