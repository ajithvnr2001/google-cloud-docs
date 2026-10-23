---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-vpc-access-connector-parent-tag/
title: Configure VPC access \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:18.064374+00:00
---

# Configure VPC access  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-vpc-access-connector-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Configure VPC access Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to configure a Cloud Run service to use VPC access connector

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service" "vpcaccess_api" {
      service            = "vpcaccess.googleapis.com"
      disable_on_destroy = false
    }
    
    # VPC
    resource "google_compute_network" "default" {
      name                    = "cloudrun-network"
      auto_create_subnetworks = false
    }
    
    # VPC access connector
    resource "google_vpc_access_connector" "connector" {
      name          = "vpcconn"
      region        = "us-west1"
      ip_cidr_range = "10.8.0.0/28"
      network       = google_compute_network.default.name
      depends_on    = [google_project_service.vpcaccess_api]
      min_instances = 2
      max_instances = 3
    }
    
    # Cloud Router
    resource "google_compute_router" "router" {
      name    = "router"
      region  = "us-west1"
      network = google_compute_network.default.id
    }
    
    # NAT configuration
    resource "google_compute_router_nat" "router_nat" {
      name                               = "nat"
      region                             = "us-west1"
      router                             = google_compute_router.router.name
      source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
      nat_ip_allocate_option             = "AUTO_ONLY"
    }
    
    # Cloud Run service
    resource "google_cloud_run_v2_service" "gcr_service" {
      name     = "mygcrservice"
      location = "us-west1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          resources {
            limits = {
              cpu    = "1000m"
              memory = "512Mi"
            }
          }
          # the service uses this SA to call other Google Cloud APIs
          # service_account_name = myservice_runtime_sa
        }
    
        scaling {
          # Limit scale up to prevent any cost blow outs!
          max_instance_count = 5
        }
    
        vpc_access {
          # Use the VPC Connector
          connector = google_vpc_access_connector.connector.id
          # all egress from the service should go through the VPC Connector
          egress = "ALL_TRAFFIC"
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
