---
url: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-metadata-pic/
title: Set stateful metadata on VM instance creation in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:38.779556+00:00
---

# Set stateful metadata on VM instance creation in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-metadata-pic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Set stateful metadata on VM instance creation in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

In a managed instance group (MIG), create a managed instance with a custom name and set stateful metadata on that VM.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configuring stateful metadata in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_per_instance_config" "default" {
      instance_group_manager = google_compute_instance_group_manager.default.name
      zone                   = google_compute_instance_group_manager.default.zone
      name                   = "node-12"
      preserved_state {
        metadata = {
          mode    = "active"
          logging = "elaborate"
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
