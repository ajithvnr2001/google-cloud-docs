---
url: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-vm-instance-parent-tag/
title: Create a Compute Engine instance with SQL Server \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:08.254536+00:00
---

# Create a Compute Engine instance with SQL Server  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-vm-instance-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/sqlserver/samples)



#  Create a Compute Engine instance with SQL Server Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create an SQL Server instance on Compute Engine

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # VPC network
    resource "google_compute_network" "default" {
      provider                = google-beta
      name                    = "vpc-network"
      auto_create_subnetworks = false
    }
    
    # Subnet
    resource "google_compute_subnetwork" "default" {
      provider      = google-beta
      name          = "vpc-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "europe-west1"
      network       = google_compute_network.default.id
    }
    
    resource "google_compute_instance" "sqlserver_vm" {
      provider = google-beta
      name     = "sqlserver-vm"
      boot_disk {
        auto_delete = true
        device_name = "persistent-disk-0"
        initialize_params {
          image = "windows-sql-cloud/sql-std-2019-win-2022"
          size  = 50
          type  = "pd-balanced"
        }
        mode = "READ_WRITE"
      }
      machine_type = "n1-standard-4"
      zone         = "europe-west1-b"
      network_interface {
        access_config {
          network_tier = "PREMIUM"
        }
        network    = google_compute_network.default.id
        stack_type = "IPV4_ONLY"
        subnetwork = google_compute_subnetwork.default.id
      }
    }
    
    resource "google_compute_firewall" "sql_server_1433" {
      provider = google-beta
      name     = "sql-server-1433-3"
      allow {
        ports    = ["1433"]
        protocol = "tcp"
      }
      description   = "Allow SQL Server access from all sources on port 1433."
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      priority      = 1000
      source_ranges = ["0.0.0.0/0"]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforsqlserver). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
