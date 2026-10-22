---
url: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-disk-policy/
title: Create a MIG with stateful disks that are deleted when its VM gets permanently deleted \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:04.947676+00:00
---

# Create a MIG with stateful disks that are deleted when its VM gets permanently deleted  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-disk-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a MIG with stateful disks that are deleted when its VM gets permanently deleted Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a managed instance group (MIG) with stateful disks and sets the disks to delete when its VM is permanently deleted from the MIG.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance_group_manager" "default" {
      name               = "example-database-group"
      base_instance_name = "shard"
      target_size        = 12
      zone               = "us-central1-f"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      stateful_disk {
        device_name = "data-disk"
        delete_rule = "ON_PERMANENT_INSTANCE_DELETION"
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
