---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-gpu/
title: Create an instance template for a MIG of GPU VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:16.180053+00:00
---

# Create an instance template for a MIG of GPU VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create an instance template for a MIG of GPU VMs Stay organized with collections  Save and categorize content based on your preferences. 

Create a global instance template that you can use to create a managed instance group (MIG) of GPU VMs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance_template" "default" {
      name         = "gpu-template"
      machine_type = "n1-standard-2"
    
      disk {
        source_image = "debian-cloud/debian-13"
      }
    
      network_interface {
        network = "default"
      }
    
      guest_accelerator {
        type  = "nvidia-tesla-t4"
        count = 1
      }
    
      scheduling {
        on_host_maintenance = "TERMINATE"
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
