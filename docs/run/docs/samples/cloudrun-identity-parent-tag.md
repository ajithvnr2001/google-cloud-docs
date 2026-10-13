---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-identity-parent-tag/
title: Custom service account on a Cloud Run service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:12.177918+00:00
---

# Custom service account on a Cloud Run service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-identity-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Custom service account on a Cloud Run service Stay organized with collections  Save and categorize content based on your preferences. 

Map a custom Service Account to a Cloud Run service

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_service_account" "cloudrun_service_identity" {
      account_id = "my-service-account"
    }
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "id-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.cloudrun_service_identity.email
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
