---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-custom-domain-mapping-parent-tag/
title: Map a Cloud Run service to a custom domain \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:26.533679+00:00
---

# Map a Cloud Run service to a custom domain  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-custom-domain-mapping-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Map a Cloud Run service to a custom domain Stay organized with collections  Save and categorize content based on your preferences. 

Sample demonstrating how to map your Cloud Run service to a custom domain that you've created. Replace verified-domain.com with your custom verified domain, for example, example.com or subdomain.example.com

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "custom-domain" # Replace with your service name
      location = "us-central1"
    
      deletion_protection = false # set to true to prevent destruction of the resource
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello" # Replace with your container image
        }
      }
    }
    data "google_project" "project" {}
    
    resource "google_cloud_run_domain_mapping" "default" {
      name     = "verified-domain.com"
      location = google_cloud_run_v2_service.default.location
      metadata {
        namespace = data.google_project.project.project_id
      }
      spec {
        route_name = google_cloud_run_v2_service.default.name
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
