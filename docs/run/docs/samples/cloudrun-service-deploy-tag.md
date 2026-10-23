---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-deploy-tag/
title: Update a Cloud Run Service and create a tagged immutable revision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:04.448191+00:00
---

# Update a Cloud Run Service and create a tagged immutable revision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-deploy-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Update a Cloud Run Service and create a tagged immutable revision Stay organized with collections  Save and categorize content based on your preferences. 

A sample to show how to update a Cloud Run Service and create a tagged immutable revision of a newly deployed image that will not yet serve traffic.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "my-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # image or tag must be different from previous revision
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        revision = "blue"
      }
    
      # Define the traffic split for each revision
      # https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#traffic
      traffic {
        percent = 100
        # This revision needs to already exist
        revision = "green"
        type     = "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION"
      }
    
      traffic {
        # Deploy new revision with 0% traffic
        percent  = 0
        revision = "blue"
        tag      = "tag-name"
        type     = "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION"
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
