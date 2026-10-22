---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-basic-parent-tag/
title: Trigger a Cloud Run service using Eventarc when an object is uploaded to a Cloud Storage bucket \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:07.277058+00:00
---

# Trigger a Cloud Run service using Eventarc when an object is uploaded to a Cloud Storage bucket  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-basic-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Trigger a Cloud Run service using Eventarc when an object is uploaded to a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Uses Terraform to create a Cloud Run service that is triggered by Eventarc when an object is uploaded to a Cloud Storage bucket

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Enable Cloud Run API
    resource "google_project_service" "run" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Eventarc API
    resource "google_project_service" "eventarc" {
      service            = "eventarc.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Pub/Sub API
    resource "google_project_service" "pubsub" {
      service            = "pubsub.googleapis.com"
      disable_on_destroy = false
    }
    
    
    # Used to retrieve project information later
    data "google_project" "project" {}
    
    # Create a dedicated service account
    resource "google_service_account" "default" {
      account_id   = "eventarc-trigger-sa"
      display_name = "Eventarc Trigger Service Account"
    }
    
    # Grant permission to receive Eventarc events
    resource "google_project_iam_member" "eventreceiver" {
      project = data.google_project.project.id
      role    = "roles/eventarc.eventReceiver"
      member  = "serviceAccount:${google_service_account.default.email}"
    }
    
    # Grant permission to invoke Cloud Run services
    resource "google_project_iam_member" "runinvoker" {
      project = data.google_project.project.id
      role    = "roles/run.invoker"
      member  = "serviceAccount:${google_service_account.default.email}"
    }
    
    
    # Cloud Storage bucket names must be globally unique
    resource "random_id" "bucket_name_suffix" {
      byte_length = 4
    }
    
    # Create a Cloud Storage bucket
    resource "google_storage_bucket" "default" {
      name          = "trigger-cloudrun-${data.google_project.project.name}-${random_id.bucket_name_suffix.hex}"
      location      = google_cloud_run_v2_service.default.location
      force_destroy = true
    
      uniform_bucket_level_access = true
    }
    
    # Grant the Cloud Storage service account permission to publish pub/sub topics
    data "google_storage_project_service_account" "gcs_account" {}
    resource "google_project_iam_member" "pubsubpublisher" {
      project = data.google_project.project.id
      role    = "roles/pubsub.publisher"
      member  = "serviceAccount:${data.google_storage_project_service_account.gcs_account.email_address}"
    
      depends_on = [data.google_storage_project_service_account.gcs_account]
    }
    
    
    # Deploy Cloud Run service
    resource "google_cloud_run_v2_service" "default" {
      name     = "hello-events"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # This container will log received events
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.default.email
      }
    
      depends_on = [google_project_service.run]
    }
    
    
    # Create an Eventarc trigger, routing Cloud Storage events to Cloud Run
    resource "google_eventarc_trigger" "default" {
      name     = "trigger-storage-cloudrun-tf"
      location = google_cloud_run_v2_service.default.location
    
      # Capture objects changed in the bucket
      matching_criteria {
        attribute = "type"
        value     = "google.cloud.storage.object.v1.finalized"
      }
      matching_criteria {
        attribute = "bucket"
        value     = google_storage_bucket.default.name
      }
    
      # Send events to Cloud Run
      destination {
        cloud_run_service {
          service = google_cloud_run_v2_service.default.name
          region  = google_cloud_run_v2_service.default.location
        }
      }
    
      # Specify a single delivery attempt with no retries
      retry_policy {
        max_attempts = 1
      }
    
      service_account = google_service_account.default.email
      depends_on = [
        google_project_service.eventarc,
        google_storage_bucket.default,
        google_project_iam_member.pubsubpublisher
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
