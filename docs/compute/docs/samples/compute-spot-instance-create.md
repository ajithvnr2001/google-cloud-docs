---
url: https://docs.cloud.google.com/compute/docs/samples/compute-spot-instance-create/
title: Create Spot Instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.739198+00:00
---

# Create Spot Instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-spot-instance-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create Spot Instance Stay organized with collections  Save and categorize content based on your preferences. 

Create a spot instance using scheduling block

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance" "spot_vm_instance" {
      name         = "spot-instance-name"
      machine_type = "f1-micro"
      zone         = "us-central1-c"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      scheduling {
        preemptible                 = true
        automatic_restart           = false
        provisioning_model          = "SPOT"
        instance_termination_action = "STOP"
      }
    
      network_interface {
        # A default network is created for all GCP projects
        network = "default"
        access_config {
        }
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
