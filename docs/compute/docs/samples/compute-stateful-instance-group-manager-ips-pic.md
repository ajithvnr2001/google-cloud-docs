---
url: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-ips-pic/
title: Configure static IP addresses on VM creation in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:17.613766+00:00
---

# Configure static IP addresses on VM creation in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-stateful-instance-group-manager-ips-pic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Configure static IP addresses on VM creation in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

Configure static IP addresses on VM creation in a managed instance group (MIG).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_region_per_instance_config" "default" {
      region_instance_group_manager = google_compute_region_instance_group_manager.default.name
      region                        = google_compute_region_instance_group_manager.default.region
      name                          = "proxy-node-03-ip"
      preserved_state {
        internal_ip {
          interface_name = "nic0"
          auto_delete    = "NEVER"
          ip_address {
            address = google_compute_address.default.id
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
