---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-secure-services-parent-tag/
title: Secure Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:47.837386+00:00
---

# Secure Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-secure-services-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Secure Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

Create two services; one a public front end, the other a secure backend. Uses IAM policies to configure access. 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_cloud_run_v2_service" "renderer" {
      name     = "renderer"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # Replace with the URL of your Secure Services > Renderer image.
          #   gcr.io/<PROJECT_ID>/renderer
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.renderer.email
      }
    }
    
    resource "google_cloud_run_v2_service" "editor" {
      name     = "editor"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # Replace with the URL of your Secure Services > Editor image.
          #   gcr.io/<PROJECT_ID>/editor
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          env {
            name  = "EDITOR_UPSTREAM_RENDER_URL"
            value = google_cloud_run_v2_service.renderer.uri
          }
        }
        service_account = google_service_account.editor.email
    
      }
    }
    
    resource "google_service_account" "renderer" {
      account_id   = "renderer-identity"
      display_name = "Service identity of the Renderer (Backend) service."
    }
    
    resource "google_service_account" "editor" {
      account_id   = "editor-identity"
      display_name = "Service identity of the Editor (Frontend) service."
    }
    
    resource "google_cloud_run_service_iam_member" "editor_invokes_renderer" {
      location = google_cloud_run_v2_service.renderer.location
      service  = google_cloud_run_v2_service.renderer.name
      role     = "roles/run.invoker"
      member   = "serviceAccount:${google_service_account.editor.email}"
    }
    
    data "google_iam_policy" "noauth" {
      binding {
        role = "roles/run.invoker"
        members = [
          "allUsers",
        ]
      }
    }
    
    resource "google_cloud_run_service_iam_policy" "noauth" {
      location = google_cloud_run_v2_service.editor.location
      project  = google_cloud_run_v2_service.editor.project
      service  = google_cloud_run_v2_service.editor.name
    
      policy_data = data.google_iam_policy.noauth.policy_data
    }
    
    output "backend_url" {
      value = google_cloud_run_v2_service.renderer.uri
    }
    
    output "frontend_url" {
      value = google_cloud_run_v2_service.editor.uri
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
