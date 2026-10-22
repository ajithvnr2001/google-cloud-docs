---
url: https://docs.cloud.google.com/compute/docs/samples/compute-os-login-ssh-key-parent-tag/
title: Create a Compute Engine instance with a SSH key \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:53.113504+00:00
---

# Create a Compute Engine instance with a SSH key  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-os-login-ssh-key-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Compute Engine instance with a SSH key Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a Compute Engine instance with an SSH key

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_client_openid_userinfo" "me" {
    }
    
    resource "google_os_login_ssh_public_key" "default" {
      user = data.google_client_openid_userinfo.me.email
      key  = file("id_rsa.pub") # path/to/ssl/id_rsa.pub
    }
    
    
    resource "google_compute_project_metadata" "default" {
      metadata = {
        ssh-keys = <<EOF
          dev:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT dev
          test:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT test
        EOF
      }
    }
    
    resource "google_compute_instance" "default" {
      name         = "my-vm"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "ubuntu-1404-trusty-v20160627"
        }
      }
    
      # Local SSD disk
      scratch_disk {
        interface = "SCSI"
      }
    
      network_interface {
        network = "default"
        access_config {}
      }
      metadata = {
        "ssh-keys" = <<EOT
          dev:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT dev
          test:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILg6UtHDNyMNAh0GjaytsJdrUxjtLy3APXqZfNZhvCeT test
         EOT
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
