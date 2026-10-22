---
url: https://docs.cloud.google.com/storage/docs/samples/storage-flask-google-cloud-quickstart-parent-tag/
title: Create a Flask application on Compute Engine \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:55.642971+00:00
---

# Create a Flask application on Compute Engine  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-flask-google-cloud-quickstart-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a Flask application on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Use Compute Engine, Networking, Storage, and KMS to create a Flask application. 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_network" "vpc_network" {
      name                    = "my-custom-mode-network"
      auto_create_subnetworks = false
      mtu                     = 1460
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "my-custom-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-west1"
      network       = google_compute_network.vpc_network.id
    }
    
    # Create a single Compute Engine instance
    resource "google_compute_instance" "default" {
      name         = "flask-vm"
      machine_type = "f1-micro"
      zone         = "us-west1-a"
      tags         = ["ssh"]
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      # Install Flask
      metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python3-pip rsync; pip install flask"
    
      network_interface {
        subnetwork = google_compute_subnetwork.default.id
    
        access_config {
          # Include this section to give the VM an external IP address
        }
      }
    }
    
    resource "google_compute_firewall" "ssh" {
      name = "allow-ssh"
      allow {
        ports    = ["22"]
        protocol = "tcp"
      }
      direction     = "INGRESS"
      network       = google_compute_network.vpc_network.id
      priority      = 1000
      source_ranges = ["0.0.0.0/0"]
      target_tags   = ["ssh"]
    }
    
    
    resource "google_compute_firewall" "flask" {
      name    = "flask-app-firewall"
      network = google_compute_network.vpc_network.id
    
      allow {
        protocol = "tcp"
        ports    = ["5000"]
      }
      source_ranges = ["0.0.0.0/0"]
    }
    
    # Create new multi-region storage bucket in the US
    # with versioning enabled
    
    resource "google_kms_key_ring" "terraform_state" {
      name     = "${random_id.bucket_prefix.hex}-bucket-tfstate"
      location = "us"
    }
    
    resource "google_kms_crypto_key" "terraform_state_bucket" {
      name            = "test-terraform-state-bucket"
      key_ring        = google_kms_key_ring.terraform_state.id
      rotation_period = "86400s"
    
      lifecycle {
        prevent_destroy = false
      }
    }
    
    # Enable the Cloud Storage service account to encrypt/decrypt Cloud KMS keys
    data "google_project" "project" {
    }
    
    resource "google_project_iam_member" "default" {
      project = data.google_project.project.project_id
      role    = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
      member  = "serviceAccount:service-${data.google_project.project.number}@gs-project-accounts.iam.gserviceaccount.com"
    }
    
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name          = "${random_id.bucket_prefix.hex}-bucket-tfstate"
      force_destroy = false
      location      = "US"
      storage_class = "STANDARD"
      versioning {
        enabled = true
      }
      encryption {
        default_kms_key_name = google_kms_crypto_key.terraform_state_bucket.id
      }
      depends_on = [
        google_project_iam_member.default
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
