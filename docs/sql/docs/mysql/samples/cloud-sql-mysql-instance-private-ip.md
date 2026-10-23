---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-private-ip/
title: Create MySQL Private IP \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:49.365192+00:00
---

# Create MySQL Private IP  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-instance-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Create MySQL Private IP Stay organized with collections  Save and categorize content based on your preferences. 

Sample demonstrating how to create the private IP for use with a MySQL Database. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_network" "peering_network" {
      name                    = "private-network"
      auto_create_subnetworks = "false"
    }
    
    resource "google_compute_global_address" "private_ip_address" {
      name          = "private-ip-address"
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 16
      network       = google_compute_network.peering_network.id
    }
    
    resource "google_service_networking_connection" "default" {
      network                 = google_compute_network.peering_network.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
    }
    
    resource "google_sql_database_instance" "instance" {
      name             = "private-ip-sql-instance"
      region           = "us-central1"
      database_version = "MYSQL_8_0"
    
      depends_on = [google_service_networking_connection.default]
    
      settings {
        tier = "db-f1-micro"
        ip_configuration {
          ipv4_enabled    = "false"
          private_network = google_compute_network.peering_network.id
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }
    
    resource "google_compute_network_peering_routes_config" "peering_routes" {
      peering              = google_service_networking_connection.default.peering
      network              = google_compute_network.peering_network.name
      import_custom_routes = true
      export_custom_routes = true
    }
    
    
    ## Uncomment this block after adding a valid DNS suffix
    
    # resource "google_service_networking_peered_dns_domain" "default" {
    #   name       = "example-com"
    #   network    = google_compute_network.peering_network.name
    #   dns_suffix = "example.com."
    #   service    = "servicenetworking.googleapis.com"
    # }
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
