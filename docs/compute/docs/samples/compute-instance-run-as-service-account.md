---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instance-run-as-service-account/
title: Run a VM as a service account \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:47.535474+00:00
---

# Run a VM as a service account  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instance-run-as-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Run a VM as a service account Stay organized with collections  Save and categorize content based on your preferences. 

Assign a service account for a VM, add access scopes, and set up the VM to run as a service account.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance" "default" {
      name         = "my-test-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      // Local SSD disk
      scratch_disk {
        interface = "SCSI"
      }
    
      network_interface {
        network = "default"
    
        access_config {
          // Ephemeral public IP
        }
      }
    
      service_account {
        # Google recommends custom service accounts with `cloud-platform` scope with
        # specific permissions granted via IAM Roles.
        # This approach lets you avoid embedding secret keys or user credentials
        # in your instance, image, or app code
        email  = google_service_account.default.email
        scopes = ["cloud-platform"]
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
