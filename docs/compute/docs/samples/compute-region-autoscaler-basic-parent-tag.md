---
url: https://docs.cloud.google.com/compute/docs/samples/compute-region-autoscaler-basic-parent-tag/
title: Create a Compute Engine managed instance group with autoscaling enabled \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:11.470902+00:00
---

# Create a Compute Engine managed instance group with autoscaling enabled  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-region-autoscaler-basic-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine managed instance group with autoscaling enabled Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a regional managed instance group (MIG) with autoscaling enabled.

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_region_autoscaler" "foobar" {
      name   = "my-region-autoscaler"
      region = "us-central1"
      target = google_compute_region_instance_group_manager.foobar.id
    
      autoscaling_policy {
        max_replicas    = 5
        min_replicas    = 1
        cooldown_period = 60
    
        cpu_utilization {
          target = 0.5
        }
      }
    }
    
    resource "google_compute_instance_template" "foobar" {
      name         = "my-instance-template"
      machine_type = "e2-standard-4"
    
      disk {
        source_image = "debian-cloud/debian-13"
        disk_size_gb = 250
      }
    
      network_interface {
        network = "default"
    
        # default access config, defining external IP configuration
        access_config {
          network_tier = "PREMIUM"
        }
      }
    
      # To avoid embedding secret keys or user credentials in the instances, Google recommends that you use custom service accounts with the following access scopes.
      service_account {
        scopes = [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
      }
    }
    
    resource "google_compute_target_pool" "foobar" {
      name   = "my-target-pool"
      region = "us-central1"
    }
    
    resource "google_compute_region_instance_group_manager" "foobar" {
      name   = "my-region-igm"
      region = "us-central1"
    
      version {
        instance_template = google_compute_instance_template.foobar.id
        name              = "primary"
      }
    
      target_pools       = [google_compute_target_pool.foobar.id]
      base_instance_name = "foobar"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
