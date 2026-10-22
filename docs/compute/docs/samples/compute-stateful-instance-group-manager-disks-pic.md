---
url: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-disks-pic/
title: Configure stateful disks individually for VMs in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:27.721173+00:00
---

# Configure stateful disks individually for VMs in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-disks-pic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Configure stateful disks individually for VMs in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This sample configures stateful disks individually for VMs in a managed instance group (MIG) by configuring the per-instance configuration of that VM.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_per_instance_config" "default" {
      instance_group_manager = google_compute_instance_group_manager.default.name
      zone                   = google_compute_instance_group_manager.default.zone
      name                   = "db-instance"
      preserved_state {
        disk {
          device_name = "data-disk"
          source      = google_compute_disk.default.id
          delete_rule = "NEVER"
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
