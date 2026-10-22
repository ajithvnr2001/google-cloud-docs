---
url: https://docs.cloud.google.com/compute/docs/samples/compute-region-igm-redistribution/
title: Create a regional MIG with proactive instance redistribution disabled \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:05.467614+00:00
---

# Create a regional MIG with proactive instance redistribution disabled  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-region-igm-redistribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a regional MIG with proactive instance redistribution disabled Stay organized with collections  Save and categorize content based on your preferences. 

Create a regional managed instance group (MIG) with proactive instance redistribution disabled.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Disable and re-enable proactive VM redistribution in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name                      = "example-rmig"
      region                    = "us-east1"
      distribution_policy_zones = ["us-east1-b", "us-east1-c"]
      update_policy {
        type                         = "PROACTIVE"
        minimal_action               = "REFRESH"
        instance_redistribution_type = "NONE"
        max_unavailable_fixed        = 3
      }
      target_size        = 30
      base_instance_name = "instance"
      version {
        instance_template = google_compute_instance_template.default.id
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
