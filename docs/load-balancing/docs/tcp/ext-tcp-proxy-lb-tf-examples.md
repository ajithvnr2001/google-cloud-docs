---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/ext-tcp-proxy-lb-tf-examples/
title: Terraform examples for external proxy Network Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:26.257661+00:00
---

# Terraform examples for external proxy Network Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/ext-tcp-proxy-lb-tf-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Terraform examples for external proxy Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

You can use the following examples to deploy external proxy Network Load Balancers.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Create an external proxy Network Load Balancer with a TCP proxy

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an external proxy Network Load Balancer with a managed instance group backend.

For information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp).
    
    
    # VPC
    resource "google_compute_network" "default" {
      name                    = "tcp-proxy-xlb-network"
      provider                = google-beta
      auto_create_subnetworks = false
    }
    
    # backend subnet
    resource "google_compute_subnetwork" "default" {
      name          = "tcp-proxy-xlb-subnet"
      provider      = google-beta
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.default.id
    }
    
    # reserved IP address
    resource "google_compute_global_address" "default" {
      provider = google-beta
      name     = "tcp-proxy-xlb-ip"
    }
    
    # forwarding rule
    resource "google_compute_global_forwarding_rule" "default" {
      name                  = "tcp-proxy-xlb-forwarding-rule"
      provider              = google-beta
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL"
      port_range            = "110"
      target                = google_compute_target_tcp_proxy.default.id
      ip_address            = google_compute_global_address.default.id
    }
    
    resource "google_compute_target_tcp_proxy" "default" {
      provider        = google-beta
      name            = "test-proxy-health-check"
      backend_service = google_compute_backend_service.default.id
    }
    
    # backend service
    resource "google_compute_backend_service" "default" {
      provider              = google-beta
      name                  = "tcp-proxy-xlb-backend-service"
      protocol              = "TCP"
      port_name             = "tcp"
      load_balancing_scheme = "EXTERNAL"
      timeout_sec           = 10
      health_checks         = [google_compute_health_check.default.id]
      backend {
        group           = google_compute_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        max_utilization = 1.0
        capacity_scaler = 1.0
      }
    }
    
    resource "google_compute_health_check" "default" {
      provider           = google-beta
      name               = "tcp-proxy-health-check"
      timeout_sec        = 1
      check_interval_sec = 1
    
      tcp_health_check {
        port = "80"
      }
    }
    
    # instance template
    resource "google_compute_instance_template" "default" {
      name         = "tcp-proxy-xlb-mig-template"
      provider     = google-beta
      machine_type = "e2-small"
      tags         = ["allow-health-check"]
    
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
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
    
    # MIG
    resource "google_compute_instance_group_manager" "default" {
      name     = "tcp-proxy-xlb-mig1"
      provider = google-beta
      zone     = "us-central1-c"
      named_port {
        name = "tcp"
        port = 80
      }
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
    }
    
    # allow access from health check ranges
    resource "google_compute_firewall" "default" {
      name          = "tcp-proxy-xlb-fw-allow-hc"
      provider      = google-beta
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
      allow {
        protocol = "tcp"
      }
      target_tags = ["allow-health-check"]
    }

## Create an external proxy Network Load Balancer with an SSL proxy

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an external proxy Network Load Balancer with a managed instance group backend.

For information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl).
    
    
    # VPC
    resource "google_compute_network" "default" {
      name                    = "ssl-proxy-xlb-network"
      provider                = google
      auto_create_subnetworks = false
    }
    
    # backend subnet
    resource "google_compute_subnetwork" "default" {
      name          = "ssl-proxy-xlb-subnet"
      provider      = google
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.default.id
    }
    
    # reserved IP address
    resource "google_compute_global_address" "default" {
      name = "ssl-proxy-xlb-ip"
    }
    
    
    # Self-signed regional SSL certificate for testing
    resource "tls_private_key" "default" {
      algorithm = "RSA"
      rsa_bits  = 2048
    }
    
    resource "tls_self_signed_cert" "default" {
      private_key_pem = tls_private_key.default.private_key_pem
    
      # Certificate expires after 12 hours.
      validity_period_hours = 12
    
      # Generate a new certificate if Terraform is run within three
      # hours of the certificate's expiration time.
      early_renewal_hours = 3
    
      # Reasonable set of uses for a server SSL certificate.
      allowed_uses = [
        "key_encipherment",
        "digital_signature",
        "server_auth",
      ]
    
      dns_names = ["example.com"]
    
      subject {
        common_name  = "example.com"
        organization = "ACME Examples, Inc"
      }
    }
    
    resource "google_compute_ssl_certificate" "default" {
      name        = "default-cert"
      private_key = tls_private_key.default.private_key_pem
      certificate = tls_self_signed_cert.default.cert_pem
    }
    
    resource "google_compute_target_ssl_proxy" "default" {
      name             = "test-proxy"
      backend_service  = google_compute_backend_service.default.id
      ssl_certificates = [google_compute_ssl_certificate.default.id]
    }
    
    
    
    # forwarding rule
    resource "google_compute_global_forwarding_rule" "default" {
      name                  = "ssl-proxy-xlb-forwarding-rule"
      provider              = google
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL"
      port_range            = "443"
      target                = google_compute_target_ssl_proxy.default.id
      ip_address            = google_compute_global_address.default.id
    }
    
    
    # backend service
    resource "google_compute_backend_service" "default" {
      name                  = "ssl-proxy-xlb-backend-service"
      protocol              = "SSL"
      port_name             = "tcp"
      load_balancing_scheme = "EXTERNAL"
      timeout_sec           = 10
      health_checks         = [google_compute_health_check.default.id]
      backend {
        group           = google_compute_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        max_utilization = 1.0
        capacity_scaler = 1.0
      }
    }
    
    resource "google_compute_health_check" "default" {
      name               = "ssl-proxy-health-check"
      timeout_sec        = 1
      check_interval_sec = 1
      tcp_health_check {
        port = "443"
      }
    }
    
    # instance template
    resource "google_compute_instance_template" "default" {
      name         = "ssl-proxy-xlb-mig-template"
      provider     = google
      machine_type = "e2-small"
      tags         = ["allow-health-check"]
    
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
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
          sudo apt-get update
          sudo apt-get install  -y apache2 jq
          sudo a2ensite default-ssl
          sudo a2enmod ssl
          sudo service apache2 restart
          NAME=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/hostname")
          IP=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip")
          METADATA=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=True" | jq 'del(.["startup-script"])')
          cat <<EOF > /var/www/html/index.html
          <h1>SSL Load Balancer</h1>
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
    
    # MIG
    resource "google_compute_instance_group_manager" "default" {
      name     = "ssl-proxy-xlb-mig1"
      provider = google
      zone     = "us-central1-c"
      named_port {
        name = "tcp"
        port = 443
      }
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
    }
    
    # allow access from health check ranges
    resource "google_compute_firewall" "default" {
      name          = "ssl-proxy-xlb-fw-allow-hc"
      provider      = google
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
      allow {
        protocol = "tcp"
      }
      target_tags = ["allow-health-check"]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
