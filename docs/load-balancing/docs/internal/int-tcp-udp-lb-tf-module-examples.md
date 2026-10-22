---
url: https://docs.cloud.google.com/load-balancing/docs/internal/int-tcp-udp-lb-tf-module-examples/
title: Terraform examples for an internal passthrough Network Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:02.068182+00:00
---

# Terraform examples for an internal passthrough Network Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/int-tcp-udp-lb-tf-module-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Terraform examples for an internal passthrough Network Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

You can use the following example to deploy a sample internal passthrough Network Load Balancer.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Internal passthrough Network Load Balancer with no backends

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-internal/tree/master/examples/minimal) to bring up a minimal internal passthrough Network Load Balancer with a Virtual Private Cloud network, subnetwork, and all of the necessary load balancing components, but no backends. This can be useful if you already have some other script or process for creating your backends.

For information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-internal/blob/master/examples/minimal/README.md) in GitHub.
    
    
    module "test_ilb" {
      source = "../../"
    
      project_id   = var.project_id
      network      = google_compute_network.test.name
      subnetwork   = google_compute_subnetwork.test.name
      region       = var.region
      name         = local.resource_name
      ports        = ["8080"]
      source_tags  = ["source-tag-foo"]
      target_tags  = ["target-tag-bar"]
      backends     = []
      health_check = local.health_check
    }

## Internal passthrough Network Load Balancer with managed instance group backend

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an internal passthrough Network Load Balancer with a managed instance group backend.
    
    
    resource "google_compute_network" "ilb_network" {
      name                    = "l4-ilb-network"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "ilb_subnet" {
      name          = "l4-ilb-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "europe-west1"
      network       = google_compute_network.ilb_network.id
    }
    
    resource "google_compute_forwarding_rule" "google_compute_forwarding_rule" {
      name                  = "l4-ilb-forwarding-rule"
      backend_service       = google_compute_region_backend_service.default.id
      region                = "europe-west1"
      ip_protocol           = "TCP"
      load_balancing_scheme = "INTERNAL"
      all_ports             = true
      allow_global_access   = true
      network               = google_compute_network.ilb_network.id
      subnetwork            = google_compute_subnetwork.ilb_subnet.id
    }
    
    resource "google_compute_region_backend_service" "default" {
      name                  = "l4-ilb-backend-subnet"
      region                = "europe-west1"
      protocol              = "TCP"
      load_balancing_scheme = "INTERNAL"
      health_checks         = [google_compute_region_health_check.default.id]
      backend {
        group          = google_compute_region_instance_group_manager.mig.instance_group
        balancing_mode = "CONNECTION"
      }
    }
    
    resource "google_compute_instance_template" "instance_template" {
      name         = "l4-ilb-mig-template"
      machine_type = "e2-small"
      tags         = ["allow-ssh", "allow-health-check"]
    
      network_interface {
        network    = google_compute_network.ilb_network.id
        subnetwork = google_compute_subnetwork.ilb_subnet.id
        access_config {
          # add external ip to fetch packages
        }
      }
      disk {
        source_image = "debian-cloud/debian-12"
        auto_delete  = true
        boot         = true
      }
    
      # install nginx and serve a simple web page
      metadata = {
        startup-script = <<-EOF1
          #! /bin/bash
          set -euo pipefail
    
          export DEBIAN_FRONTEND=noninteractive
          apt-get update
          apt-get install -y nginx-light jq
    
          NAME=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/hostname")
          IP=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip")
          METADATA=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=True" | jq 'del(.["startup-script"])')
    
          cat <<EOF > /var/www/html/index.html
          <pre>
          Name: $NAME
          IP: $IP
          Metadata: $METADATA
          </pre>
          EOF
        EOF1
      }
      lifecycle {
        create_before_destroy = true
      }
    }
    
    resource "google_compute_region_health_check" "default" {
      name   = "l4-ilb-hc"
      region = "europe-west1"
      http_health_check {
        port = "80"
      }
    }
    
    resource "google_compute_region_instance_group_manager" "mig" {
      name   = "l4-ilb-mig1"
      region = "europe-west1"
      version {
        instance_template = google_compute_instance_template.instance_template.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
    }
    
    # allow all access from health check ranges
    resource "google_compute_firewall" "fw_hc" {
      name          = "l4-ilb-fw-allow-hc"
      direction     = "INGRESS"
      network       = google_compute_network.ilb_network.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16", "35.235.240.0/20"]
      allow {
        protocol = "tcp"
      }
      target_tags = ["allow-health-check"]
    }
    
    # allow communication within the subnet
    resource "google_compute_firewall" "fw_ilb_to_backends" {
      name          = "l4-ilb-fw-allow-ilb-to-backends"
      direction     = "INGRESS"
      network       = google_compute_network.ilb_network.id
      source_ranges = ["10.0.1.0/24"]
      allow {
        protocol = "tcp"
      }
      allow {
        protocol = "udp"
      }
      allow {
        protocol = "icmp"
      }
    }
    
    # allow SSH
    resource "google_compute_firewall" "fw_ilb_ssh" {
      name      = "l4-ilb-fw-ssh"
      direction = "INGRESS"
      network   = google_compute_network.ilb_network.id
      allow {
        protocol = "tcp"
        ports    = ["22"]
      }
      target_tags   = ["allow-ssh"]
      source_ranges = ["0.0.0.0/0"]
    }
    
    resource "google_compute_instance" "vm_test" {
      name         = "l4-ilb-test-vm"
      tags         = ["allow-ssh"]
      zone         = "europe-west1-b"
      machine_type = "e2-small"
      network_interface {
        network    = google_compute_network.ilb_network.id
        subnetwork = google_compute_subnetwork.ilb_subnet.id
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-12"
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
