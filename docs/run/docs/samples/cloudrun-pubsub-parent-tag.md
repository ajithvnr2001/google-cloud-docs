---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-pubsub-parent-tag/
title: Connect a Pub/Sub subscription to a Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:42.723295+00:00
---

# Connect a Pub/Sub subscription to a Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-pubsub-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Connect a Pub/Sub subscription to a Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

Uses Terraform to create a Pub/Sub subscription to a Cloud Run service

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_project" "project" {
    }
    
    # Enable Cloud Run API
    resource "google_project_service" "cloudrun_api" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "pubsub-tutorial"
      location = "us-central1"
    
      deletion_protection = false # set to true to prevent destruction of the resource
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello" # Replace with newly created image gcr.io/<project_id>/pubsub
        }
      }
      depends_on = [google_project_service.cloudrun_api]
    }
    
    resource "google_service_account" "sa" {
      account_id   = "cloud-run-pubsub-invoker"
      display_name = "Cloud Run Pub/Sub Invoker"
    }
    
    resource "google_cloud_run_service_iam_binding" "binding" {
      location = google_cloud_run_v2_service.default.location
      service  = google_cloud_run_v2_service.default.name
      role     = "roles/run.invoker"
      members  = ["serviceAccount:${google_service_account.sa.email}"]
    }
    
    resource "google_project_service_identity" "pubsub_agent" {
      provider = google-beta
      project  = data.google_project.project.project_id
      service  = "pubsub.googleapis.com"
    }
    
    resource "google_project_iam_binding" "project_token_creator" {
      project = data.google_project.project.project_id
      role    = "roles/iam.serviceAccountTokenCreator"
      members = ["serviceAccount:${google_project_service_identity.pubsub_agent.email}"]
    }
    
    resource "google_pubsub_topic" "default" {
      name = "pubsub_topic"
    }
    
    resource "google_pubsub_subscription" "subscription" {
      name  = "pubsub_subscription"
      topic = google_pubsub_topic.default.name
      push_config {
        push_endpoint = google_cloud_run_v2_service.default.uri
        oidc_token {
          service_account_email = google_service_account.sa.email
        }
        attributes = {
          x-goog-version = "v1"
        }
      }
      depends_on = [google_cloud_run_v2_service.default]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
