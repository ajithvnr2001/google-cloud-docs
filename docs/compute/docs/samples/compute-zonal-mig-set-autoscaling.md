---
url: https://docs.cloud.google.com/compute/docs/samples/compute-zonal-mig-set-autoscaling/
title: Configure autoscaling in a managed instance group (MIG) \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:28.071220+00:00
---

# Configure autoscaling in a managed instance group (MIG)  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-zonal-mig-set-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Configure autoscaling in a managed instance group (MIG) Stay organized with collections  Save and categorize content based on your preferences. 

Configure autoscaling based on CPU utilization in a zonal MIG.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a MIG with autoscaling enabled](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_autoscaler" "default" {
      name   = "example-autoscaler"
      zone   = "us-central1-f"
      target = google_compute_instance_group_manager.default.id
    
      autoscaling_policy {
        max_replicas    = 20
        min_replicas    = 0
        cooldown_period = 90
    
        cpu_utilization {
          target = 0.60
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
