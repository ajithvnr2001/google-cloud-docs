---
url: https://docs.cloud.google.com/compute/docs/samples/compute-disk-parent-tag/
title: Create a Compute Engine instance with an attached disk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:24.596400+00:00
---

# Create a Compute Engine instance with an attached disk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-disk-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine instance with an attached disk Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine instance with an attached disk

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_disk" "default" {
      name  = "disk-name1"
      type  = "pd-ssd"
      zone  = "us-central1-a"
      image = "debian-13-trixie-v20260908"
      labels = {
        environment = "dev"
      }
      physical_block_size_bytes = 4096
    }
    
    resource "google_compute_snapshot" "snapdisk" {
      name        = "snapshot-name"
      source_disk = google_compute_disk.default.name
      zone        = "us-central1-a"
    }
    
    resource "google_compute_region_disk" "regiondisk" {
      name                      = "region-disk-name"
      snapshot                  = google_compute_snapshot.snapdisk.id
      type                      = "pd-ssd"
      region                    = "us-central1"
      physical_block_size_bytes = 4096
      size                      = 11
    
      replica_zones = ["us-central1-a", "us-central1-f"]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
