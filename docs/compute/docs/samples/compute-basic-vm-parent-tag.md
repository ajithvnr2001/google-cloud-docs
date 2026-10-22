---
url: https://docs.cloud.google.com/compute/docs/samples/compute-basic-vm-parent-tag/
title: Create a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:20.247418+00:00
---

# Create a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-basic-vm-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine instance

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create a VM instance from a public image
    # in the `default` VPC network and subnet
    
    resource "google_compute_instance" "default" {
      name         = "my-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "ubuntu-minimal-2210-kinetic-amd64-v20230126"
        }
      }
    
      network_interface {
        network = "default"
        access_config {}
      }
    }
    
    resource "google_compute_network" "custom" {
      name                    = "my-network"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "custom" {
      name          = "my-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "europe-west1"
      network       = google_compute_network.custom.id
    }
    
    
    # Create a VM in a custom VPC network and subnet
    
    resource "google_compute_instance" "custom_subnet" {
      name         = "my-vm-instance"
      tags         = ["allow-ssh"]
      zone         = "europe-west1-b"
      machine_type = "e2-small"
      network_interface {
        network    = google_compute_network.custom.id
        subnetwork = google_compute_subnetwork.custom.id
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-12"
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
