---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-add-tag/
title: Change a Cloud Run Service to add a tag to a newly deployed revision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:46.452408+00:00
---

# Change a Cloud Run Service to add a tag to a newly deployed revision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-add-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Change a Cloud Run Service to add a tag to a newly deployed revision Stay organized with collections  Save and categorize content based on your preferences. 

A sample that shows how to change a defined Cloud Run Service to add a newly deployed revision to show how to deploy a new revision and test it prior to having traffic deployed. 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "my-service"
      location = "us-central1"
    
      deletion_protection = false # set to true to prevent destruction of the resource
    
      template {}
    
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
