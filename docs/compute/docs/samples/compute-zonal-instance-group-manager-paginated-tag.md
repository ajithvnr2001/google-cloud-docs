---
url: https://docs.cloud.google.com/compute/docs/samples/compute-zonal-instance-group-manager-paginated-tag/
title: Increase a managed instance group's (MIG's) size limit \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:23.522604+00:00
---

# Increase a managed instance group's (MIG's) size limit  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-zonal-instance-group-manager-paginated-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Increase a managed instance group's (MIG's) size limit Stay organized with collections  Save and categorize content based on your preferences. 

The sample creates a zonal MIG and increases the MIG's size limit from 1,000 VMs (default) to 2,000 VMs. The size limit increases when you enable pagination by setting the list_managed_instances_results argument to PAGINATED.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and remove VMs from a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance_group_manager" "default" {
      name                           = "my-igm"
      base_instance_name             = "test"
      target_size                    = 7
      zone                           = "us-central1-f"
      list_managed_instances_results = "PAGINATED"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
