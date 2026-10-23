---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-create-serviceaccount/
title: Create a trigger using Terraform (service account) \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:47.011150+00:00
---

# Create a trigger using Terraform (service account)  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-create-serviceaccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create a trigger using Terraform (service account) Stay organized with collections  Save and categorize content based on your preferences. 

Creates a service account and grants permissions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
