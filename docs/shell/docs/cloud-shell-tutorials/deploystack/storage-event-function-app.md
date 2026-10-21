---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/storage-event-function-app/
title: Storage Event Function App \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:39.172392+00:00
---

# Storage Event Function App  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/storage-event-function-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Storage Event Function App Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-scaler.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-scaler.svg)

Storage Event Function App is an image directory and thumbnail maker. It is made up of the following components:

  * A client application where users can upload images. 
    * Container hosted API and static site - Golang - Cloud Run
    * Storage - File Storage - Cloud Storage
  * An image processor that creates thumbnails of the images. 
    * Functions as a Service - Golang - Cloud Functions
  * A deployment pipeline. 
    * Deployment - Cloud Build



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-storage-event-function-app&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-storage-event-function-app)

* * *

## Storage Event Function App components

The Storage Event Function App architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_run.svg) | **Cloud Run** |  Cloud Run allows you to run applications in a container, but in a serverless way, no having to configure number of instances, processors, or memory. Upload a container, get a url.  |  [smart_display](https://www.youtube.com/watch?v=nhwYc4StHIc) |  [description](https://cloud.google.com/run/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_run_quickstart_index)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_storage.svg) | **Cloud Storage** |  Cloud Storage provides file storage and public serving of images over http(s).  |  [smart_display](https://www.youtube.com/watch?v=zvqJ-pcQChE) |  [description](https://cloud.google.com/storage/docs/quickstart-console) |  [keyboard](https://console.cloud.google.com/?tutorial=storage--quickstart-basic-tasks)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_functions.svg) | **Cloud Functions** |  Cloud Functions is a functions a service platform that allows you to listen for Cloud Storage file uploads and run code to create thumbnails of them.  |  [smart_display](https://www.youtube.com/watch?v=vM-2O-uKBNQ) |  [description](https://cloud.google.com/functions/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=functions_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_build.svg) | **Cloud Build** |  Cloud Build is the tool that packages up the containers and deploys them to be available as Cloud Run services.  |  [smart_display](https://www.youtube.com/watch?v=w7dMHiEyGAs) |  [description](https://cloud.google.com/build/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_build_quickstart)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Storage Event Function App. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable services

Google Cloud Services are disabled in a project by default. In order to use any of the solutions here we have to activate the following:

  * **Cloud Build** \- creates container images and deploys to Cloud Run
  * **Cloud Storage** \- hosts static files
  * **Cloud Functions** \- Functions as a Service platform
  * **Cloud Run** \- the serverless tool which will host the container and provide a URLS from which to access the application.
  * **Artifact Registry** \- stores the Docker images for use with Cloud Build.


    
    
    variable "gcp_service_list" {
        description = "The list of apis necessary for the project"
        type        = list(string)
        default = [
            "cloudbuild.googleapis.com",
            "storage.googleapis.com",
            "cloudfunctions.googleapis.com",
            "run.googleapis.com",
            "artifactregistry.googleapis.com",
        ]
    }
    
    resource "google_project_service" "all" {
        for_each                   = toset(var.gcp_service_list)
        project                    = var.project_number
        service                    = each.key
        disable_dependent_services = false
        disable_on_destroy         = false
    }
    

#### Set permissions

Sets IAM roles and permissions that allow Cloud Build to deploy all of the services.

  * Enable Cloud Build Service Account to deploy to Cloud Run
  * Enable Cloud Build Service Account to perform Service Account activities
  * Enable Cloud Build Service Account to publish to Cloud Run
  * Enable Cloud Build Service Account to store containers in Artifact Registry


    
    
    variable "build_roles_list" {
        description = "The list of roles that build needs for"
        type        = list(string)
        default = [
            "roles/run.developer",
            "roles/iam.serviceAccountUser",
            "roles/run.admin",
            "roles/cloudfunctions.admin",
            "roles/artifactregistry.admin",
        ]
    }
    
    resource "google_project_iam_member" "allbuild" {
        for_each   = toset(var.build_roles_list)
        project    = var.project_number
        role       = each.key
        member     = "serviceAccount:${local.sabuild}"
        depends_on = [google_project_service.all]
    }
    

#### Create Storage buckets

Creates the Storage location for the uploaded images and thumbnails, and provides a temporary storage location for the Cloud Functions upload.
    
    
    resource "google_storage_bucket" "target_bucket" {
        name     = var.bucket
        project  = var.project_number
        location = var.location
    }
    
    resource "google_storage_bucket" "function_bucket" {
        name     = "${var.project_id}-function-deployer"
        project  = var.project_number
        location = var.location
    }
    

#### Create Artifact Registry repoistory

The following code outlines the parameters for the Artifact Registry repository in which the containers are stored.
    
    
    resource "google_artifact_registry_repository" "app" {
        provider      = google-beta
        format        = "DOCKER"
        location      = var.region
        project       = var.project_id
        repository_id = "${var.basename}-app"
        depends_on    = [google_project_service.all]
    }
    

#### Build container for Cloud Run application

The following builds an image and uploads it to Artifact Registry for use with Cloud Build.
    
    
    resource "null_resource" "cloudbuild_app" {
        provisioner "local-exec" {
            working_dir = "${path.module}/code/app"
            command     = "gcloud builds submit . --substitutions=_REGION=${var.region},_BASENAME=${var.basename}"
        }
    
        depends_on = [
            google_artifact_registry_repository.app,
            google_project_service.all
        ]
    }
    

#### Deploy to Cloud Run

The following uses Cloud Build to deploy the client web app to Cloud Run.
    
    
    resource "google_cloud_run_service" "app" {
        name     = "${var.basename}-app"
        location = var.region
        project  = var.project_id
    
        template {
            spec {
                containers {
                    image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.basename}-app/prod"
                    env {
                    name  = "BUCKET"
                    value = var.bucket
                    }
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
        depends_on = [
            null_resource.cloudbuild_app,
        ]
    }
    
    data "google_iam_policy" "noauth" {
        binding {
            role = "roles/run.invoker"
            members = [
            "allUsers",
            ]
        }
    }
    
    resource "google_cloud_run_service_iam_policy" "noauth_app" {
        location    = google_cloud_run_service.app.location
        project     = google_cloud_run_service.app.project
        service     = google_cloud_run_service.app.name
        policy_data = data.google_iam_policy.noauth.policy_data
    }
    

#### Deploy function code to Cloud Functions

Push directly to functions and activate.
    
    
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
    
        available_memory_mb   = 128
        source_archive_bucket = google_storage_bucket.function_bucket.name
        source_archive_object = google_storage_bucket_object.archive.name
        entry_point           = "OnFileUpload"
        event_trigger {
            event_type = "google.storage.object.finalize"
            resource   = google_storage_bucket.target_bucket.name
        }
    
        depends_on = [
            google_storage_bucket.function_bucket,
            google_storage_bucket.target_bucket,
            google_storage_bucket_object.archive,
            google_project_service.all
        ]
    }
    

### ./code/app/cloudbuild.yaml

#### Build API Container

The following makes a Docker image for the web app.
    
    
    - name: "gcr.io/cloud-builders/docker"
      args: [ "build", "-t", "$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/prod", ".", ]
    

#### Push API container to Artifact Registry

Pushing the container to Artifact Registry makes it possible for Cloud Run to get the image and serve it.
    
    
    - name: "gcr.io/cloud-builders/docker"
      args: ["push", "$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/prod"]
    

#### Substitutions

Create a variable with a default so that these values can be changed at deploy time.
    
    
    substitutions:
      _REGION: us-central1
      _BASENAME: scaler
    

* * *

## Conclusion

You now have a thumbnail-creating solution running in your project using Cloud Functions to respond to changes in a Storage Bucket. You also have all of the code to modify or extend this solution 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
