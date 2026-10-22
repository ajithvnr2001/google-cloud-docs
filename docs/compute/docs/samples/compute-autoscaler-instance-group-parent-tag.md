---
url: https://docs.cloud.google.com/compute/docs/samples/compute-autoscaler-instance-group-parent-tag/
title: Create a Compute Engine managed instance group with schedule-based autoscaling \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:48.632364+00:00
---

# Create a Compute Engine managed instance group with schedule-based autoscaling  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-autoscaler-instance-group-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine managed instance group with schedule-based autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine managed instance group (MIG) with schedule-based autoscaling.

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_autoscaler" "default" {
      provider = google-beta
      name     = "my-autoscaler"
      zone     = "us-central1-f"
      target   = google_compute_instance_group_manager.default.id
    
      autoscaling_policy {
        max_replicas    = 5
        min_replicas    = 1
        cooldown_period = 60
    
        scaling_schedules {
          name                  = "every-weekday-morning"
          description           = "Increase to 2 every weekday at 7AM for 12 hours."
          min_required_replicas = 2
          schedule              = "0 7 * * MON-FRI"
          time_zone             = "America/New_York"
          duration_sec          = 43200
        }
      }
    }
    
    resource "google_compute_instance_template" "default" {
      name           = "my-instance-template"
      machine_type   = "e2-medium"
      can_ip_forward = false
    
      tags = ["tag1", "tag2"]
    
      disk {
        source_image = data.google_compute_image.debian_11.id
      }
    
      network_interface {
        network = "default"
      }
    
      metadata = {
        name = "value"
      }
    
      service_account {
        scopes = ["userinfo-email", "compute-ro", "storage-ro"]
      }
    }
    
    
    resource "google_compute_instance_group_manager" "default" {
    
      name = "my-igm"
      zone = "us-central1-f"
    
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
    
      base_instance_name = "autoscaler-sample"
    }
    
    data "google_compute_image" "debian_11" {
    
      family  = "debian-13"
      project = "debian-cloud"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
