---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-parent-tag/
title: Trigger Cloud Workflows when an object is uploaded to a Cloud Storage bucket \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:36.220922+00:00
---

# Trigger Cloud Workflows when an object is uploaded to a Cloud Storage bucket  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Trigger Cloud Workflows when an object is uploaded to a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Uses Terraform and Eventarc to set up a Cloud Workflows workflow that is triggered when an object is uploaded to a Cloud Storage bucket

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Enable Workflows API
    resource "google_project_service" "workflows" {
      service            = "workflows.googleapis.com"
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
    
    # Create a service account for Eventarc trigger and Workflows
    resource "google_service_account" "eventarc" {
      account_id   = "eventarc-workflows-sa"
      display_name = "Eventarc Workflows Service Account"
    }
    
    # Grant permission to invoke Workflows
    resource "google_project_iam_member" "workflowsinvoker" {
      project = data.google_project.project.id
      role    = "roles/workflows.invoker"
      member  = "serviceAccount:${google_service_account.eventarc.email}"
    }
    
    # Grant permission to receive events
    resource "google_project_iam_member" "eventreceiver" {
      project = data.google_project.project.id
      role    = "roles/eventarc.eventReceiver"
      member  = "serviceAccount:${google_service_account.eventarc.email}"
    }
    
    # Grant permission to write logs
    resource "google_project_iam_member" "logwriter" {
      project = data.google_project.project.id
      role    = "roles/logging.logWriter"
      member  = "serviceAccount:${google_service_account.eventarc.email}"
    }
    
    
    # Cloud Storage bucket names must be globally unique
    resource "random_id" "bucket_name_suffix" {
      byte_length = 4
    }
    
    # Create a Cloud Storage bucket
    resource "google_storage_bucket" "default" {
      name          = "trigger-workflows-${data.google_project.project.name}-${random_id.bucket_name_suffix.hex}"
      location      = google_workflows_workflow.default.region
      force_destroy = true
    
      uniform_bucket_level_access = true
    }
    
    # Grant the Cloud Storage service account permission to publish Pub/Sub topics
    data "google_storage_project_service_account" "gcs_account" {}
    resource "google_project_iam_member" "pubsubpublisher" {
      project = data.google_project.project.id
      role    = "roles/pubsub.publisher"
      member  = "serviceAccount:${data.google_storage_project_service_account.gcs_account.email_address}"
    }
    
    
    # Create a workflow
    resource "google_workflows_workflow" "default" {
      name            = "storage-workflow-tf"
      region          = "us-central1"
      description     = "Workflow that returns information about storage events"
      service_account = google_service_account.eventarc.email
    
      deletion_protection = false # set to "true" in production
    
      # Note that $$ is needed for Terraform
      source_contents = <<EOF
      main:
        params: [event]
        steps:
          - log_event:
              call: sys.log
              args:
                text: $${event}
                severity: INFO
          - gather_data:
              assign:
                - bucket: $${event.data.bucket}
                - name: $${event.data.name}
                - message: $${"Received event " + event.type + " - " + bucket + ", " + name}
          - return_data:
              return: $${message}
      EOF
    
      depends_on = [
        google_project_service.workflows
      ]
    }
    
    # Create an Eventarc trigger, routing Cloud Storage events to Workflows
    resource "google_eventarc_trigger" "default" {
      name     = "trigger-storage-workflows-tf"
      location = google_workflows_workflow.default.region
    
      # Capture objects changed in the bucket
      matching_criteria {
        attribute = "type"
        value     = "google.cloud.storage.object.v1.finalized"
      }
      matching_criteria {
        attribute = "bucket"
        value     = google_storage_bucket.default.name
      }
    
      # Send events to Workflows
      destination {
        workflow = google_workflows_workflow.default.id
      }
    
      service_account = google_service_account.eventarc.email
    
      depends_on = [
        google_project_service.eventarc,
        google_project_service.workflows,
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
