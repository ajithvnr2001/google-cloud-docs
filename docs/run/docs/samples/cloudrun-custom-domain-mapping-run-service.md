---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-custom-domain-mapping-run-service/
title: Create a Cloud Run service for a custom domain \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:42.326749+00:00
---

# Create a Cloud Run service for a custom domain  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-custom-domain-mapping-run-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Create a Cloud Run service for a custom domain Stay organized with collections  Save and categorize content based on your preferences. 

Sample demonstrating how to create a Cloud Run service to use. Once created, you can map your Cloud Run service to a custom domain. Replace the value for name with your own service name.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Map custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains)



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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
