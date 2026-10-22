---
url: https://docs.cloud.google.com/compute/docs/samples/compute-add-persistent-disk-parent-tag/
title: Add a persistent disk to Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:14.530071+00:00
---

# Add a persistent disk to Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-add-persistent-disk-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Add a persistent disk to Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine instance with a persistent disk 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service" "compute_api" {
      service            = "compute.googleapis.com"
      disable_on_destroy = false
    }
    
    # Using pd-standard because it's the default for Compute Engine
    
    resource "google_compute_disk" "default" {
      name = "disk-data"
      type = "pd-standard"
      zone = "us-west1-a"
      size = "5"
    }
    
    resource "google_compute_instance" "test_node" {
      name         = "test-node"
      machine_type = "f1-micro"
      zone         = "us-west1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      attached_disk {
        source      = google_compute_disk.default.id
        device_name = google_compute_disk.default.name
      }
    
      network_interface {
        network = "default"
        access_config {
          # Ephemeral IP
        }
      }
    
      # Ignore changes for persistent disk attachments
      lifecycle {
        ignore_changes = [attached_disk]
      }
    
    
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
