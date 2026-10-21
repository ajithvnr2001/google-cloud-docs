---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-static-outbound-parent-tag/
title: Configure a Cloud Run service with a static IP address \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:57.643479+00:00
---

# Configure a Cloud Run service with a static IP address  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-static-outbound-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Configure a Cloud Run service with a static IP address Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create the networking setup and configurations to allocate a static IP to a Cloud Run service

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service" "compute_engine_api" {
      service            = "compute.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Cloud Run API
    resource "google_project_service" "cloudrun_api" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    # Example of setting up a Cloud Run service with a static outbound IP
    resource "google_compute_network" "default" {
      name = "cr-static-ip-network"
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "cr-static-ip"
      ip_cidr_range = "10.124.0.0/28"
      network       = google_compute_network.default.id
      region        = "us-central1"
    }
    
    resource "google_project_service" "vpc" {
      service            = "vpcaccess.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_vpc_access_connector" "default" {
      name          = "cr-conn"
      region        = "us-central1"
      min_instances = 2
      max_instances = 3
    
      subnet {
        name = google_compute_subnetwork.default.name
      }
    
      # Wait for VPC API enablement
      # before creating this resource
      depends_on = [
        google_project_service.vpc
      ]
    }
    
    resource "google_compute_router" "default" {
      name    = "cr-static-ip-router"
      network = google_compute_network.default.name
      region  = google_compute_subnetwork.default.region
    }
    
    resource "google_compute_address" "default" {
      name   = "cr-static-ip-addr"
      region = google_compute_subnetwork.default.region
    }
    
    resource "google_compute_router_nat" "default" {
      name   = "cr-static-nat"
      router = google_compute_router.default.name
      region = google_compute_subnetwork.default.region
    
      nat_ip_allocate_option = "MANUAL_ONLY"
      nat_ips                = [google_compute_address.default.self_link]
    
      source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
      subnetwork {
        name                    = google_compute_subnetwork.default.id
        source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
      }
    }
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cr-static-ip-service"
      location = google_compute_subnetwork.default.region
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # Replace with the URL of your container
          #   gcr.io/<YOUR_GCP_PROJECT_ID>/<YOUR_CONTAINER_NAME>
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        scaling {
          max_instance_count = 5
        }
        vpc_access {
          connector = google_vpc_access_connector.default.id
          egress    = "ALL_TRAFFIC"
        }
      }
      ingress = "INGRESS_TRAFFIC_ALL"
    
      # Used in sample testing. These fields may change in 'terraform plan' output, which is expected and thus non-blocking.
      lifecycle {
        ignore_changes = [
          ingress, template[0].vpc_access
        ]
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
