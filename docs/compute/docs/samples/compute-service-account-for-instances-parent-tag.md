---
url: https://docs.cloud.google.com/compute/docs/samples/compute-service-account-for-instances-parent-tag/
title: Create a Compute Engine instance with a dedicated service account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:04.398054+00:00
---

# Create a Compute Engine instance with a dedicated service account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-service-account-for-instances-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine instance with a dedicated service account Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine instance with a dedicated service account

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_service_account" "default" {
      account_id   = "service-account-id"
      display_name = "Service Account"
    }
    
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
