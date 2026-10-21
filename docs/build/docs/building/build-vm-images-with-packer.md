---
url: https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer/
title: Building VM images using Packer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:58:38.718948+00:00
---

# Building VM images using Packer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Building VM images using Packer Stay organized with collections  Save and categorize content based on your preferences. 

[Packer](https://www.packer.io/) is an open source tool for creating identical Virtual Machine (VM) images for multiple platforms from a single source configuration. This page explains how to use Packer and Cloud Build to create a VM image for use on Compute Engine.

## Before you begin

The instructions on this page assume that you are familiar with `Packer`. In addition:

  * Have your source code including the [Packer template](https://developer.hashicorp.com/packer/docs/templates) handy.
  * Have a Docker repository in Artifact Registry or [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  * If you want to use the `gcloud` commands in this page, install the [Google Cloud CLI](https://cloud.google.com/sdk).
  * Enable the following APIs:
        
        gcloud services enable compute.googleapis.com
        gcloud services enable servicemanagement.googleapis.com
        gcloud services enable storage-api.googleapis.com
        gcloud services enable artifactregistry.googleapis.com
        




### Required IAM permissions

  * To use Packer with Cloud Build, grant the [Compute Engine Instance Admin (v1) role (`roles/compute.instanceAdmin.v1`)](https://docs.cloud.google.com/compute/docs/access/iam) and the [Service Account User role (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/iam/docs/service-accounts-actas) to your build service account.

  * To store built images in Artifact Registry, grant the [Artifact Registry Writer role (`roles/artifactregistry.writer`)](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to your build service account.




## Creating a Packer builder image

Cloud Build provides a [Packer community builder image](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/packer) that you can use to invoke `packer` commands in Cloud Build. Before using this builder in a Cloud Build config file, you must build the image and push it to Artifact Registry:

  1. Clone the [cloud-builders-community](https://github.com/GoogleCloudPlatform/cloud-builders-community) repository:
         
         git clone https://github.com/GoogleCloudPlatform/cloud-builders-community.git
         

  2. Navigate to the Packer builder image:
         
         cd cloud-builders-community/packer
         

  3. Submit the builder to your project:
         
         gcloud builds submit . --config cloudbuild.yaml --substitutions=_AR_HOST=[LOCATION]-docker.pkg.dev,_AR_REPO=[REPOSITORY]
         

Where:

     * `[LOCATION]` is the [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of your Artifact Registry repository.
     * `[REPOSITORY]` is the name of your Artifact Registry repository.



## Creating a Packer template

Create a new file named `packer.pkr.hcl` and add the template configuration.

The following example shows a Packer template (`packer.pkr.hcl`) configured to build a Compute Engine VM image:
    
    
    packer {
      required_plugins {
        googlecompute = {
          version = ">= 1.1.1"
          source  = "github.com/hashicorp/googlecompute"
        }
      }
    }
    
    variable "image_name" {
      type    = string
      description = "The name of the output VM image"
      default = "my-packer-image"
    }
    variable "project_id" {
      type    = string
      description = "The GCP project ID"
    }
    variable "image_family" {
      type    = string
      description = "The family of the output VM image"
      default = "my-image-family"
    }
    variable "image_zone" {
      type    = string
      description = "The zone to build the image in"
      default = "us-central1-a"
    }
    
    source "googlecompute" "gce" {
      project_id          = var.project_id
      source_image_family = "ubuntu-2004-lts"
      source_image_project_ids = ["ubuntu-os-cloud"]
      zone                = var.image_zone
      ssh_username        = "packer"
      machine_type        = "e2-small"
      image_name          = "${var.image_name}-"
      image_family        = var.image_family
    }
    
    build {
      name    = "gce-vm-image"
      sources = ["sources.googlecompute.gce"]
    
      provisioner "shell" {
        inline = [
          "echo 'Provisioning image...'",
          "sudo apt-get update",
          "sudo apt-get install -y nginx"
        ]
      }
    }
    

## Using the Packer builder

  1. Ensure that you have your [Packer template](https://developer.hashicorp.com/packer/docs/templates) (for example, `packer.pkr.hcl`) along with your source code.

  2. In your project root directory, create a [build config file](https://docs.cloud.google.com/build/docs/build-config) named `cloudbuild.yaml` or `cloudbuild.json`.

  3. In your build config file, add a build step to invoke the `packer build` command:

###  YAML 
         
         steps:
         - name: '[LOCATION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/packer'
           args:
           - build
           - -var
           - image_name=[IMAGE_NAME]
           - -var
           - project_id=[PROJECT_ID]
           - -var
           - image_family=[IMAGE_FAMILY]
           - -var
           - image_zone=[IMAGE_ZONE]
           - packer.pkr.hcl
         

###  JSON 
         
         {
           "steps": [
            {
               "name": "[LOCATION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/packer",
               "args": [
                 "build",
                 "-var",
                 "image_name=[IMAGE_NAME]",
                 "-var",
                 "project_id=[PROJECT_ID]",
                 "-var",
                 "image_family=[IMAGE_FAMILY]",
                 "-var",
                 "image_zone=[IMAGE_ZONE]",
                 "packer.pkr.hcl"
                ]
             }
            ]
         }
         

Where:

     * `[LOCATION]` is the [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of your Artifact Registry repository.
     * `[PROJECT_ID]` is your Google Cloud project ID.
     * `[REPOSITORY]` is the name of your Artifact Registry repository.
     * `[IMAGE_NAME]` is the name of the VM image you're building.
     * `[IMAGE_FAMILY]` is the [image family](https://docs.cloud.google.com/compute/docs/images#image_families) of the VM image.
     * `[IMAGE_ZONE]` is the [image zone](https://docs.cloud.google.com/compute/docs/regions-zones).
  4. Start the build using the build config file:
         
         gcloud builds submit --region=[REGION] --config [CONFIG_FILE_PATH] [SOURCE_DIRECTORY]
         

Where:

     * `[CONFIG_FILE_PATH]` is the path to the build config file.
     * `[SOURCE_DIRECTORY]` is the path or URL to the source code.
     * `[REGION]` is one of the [supported build regions](https://docs.cloud.google.com/build/docs/locations).

If you don't specify a `[CONFIG_FILE_PATH]` and `[SOURCE_DIRECTORY]` in the `gcloud builds submit` command, Cloud Build assumes that the config file and the source code are in the current working directory.




Once the images are built, you can view them in the [Compute Engine Image page](https://console.cloud.google.com/compute/images) in the Google Cloud console.

## What's next

  * Learn how to [build containers](https://docs.cloud.google.com/build/docs/building/build-containers).
  * Learn how to [build `Go` projects](https://docs.cloud.google.com/build/docs/building/build-go).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
