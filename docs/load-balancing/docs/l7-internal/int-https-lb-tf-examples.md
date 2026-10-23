---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/int-https-lb-tf-examples/
title: Terraform examples for a regional internal Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:08.438086+00:00
---

# Terraform examples for a regional internal Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/int-https-lb-tf-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Terraform examples for a regional internal Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

You can use the following examples to deploy a sample regional internal Application Load Balancer.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Regional internal Application Load Balancer with a MIG backend

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an internal HTTP load balancer with a managed instance group backend.

For information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).
    
    
    # VPC network
    resource "google_compute_network" "ilb_network" {
      name                    = "l7-ilb-network"
      provider                = google-beta
      auto_create_subnetworks = false
    }
    
    # proxy-only subnet
    resource "google_compute_subnetwork" "proxy_subnet" {
      name          = "l7-ilb-proxy-subnet"
      provider      = google-beta
      ip_cidr_range = "10.0.0.0/24"
      region        = "europe-west1"
      purpose       = "REGIONAL_MANAGED_PROXY"
      role          = "ACTIVE"
      network       = google_compute_network.ilb_network.id
    }
    
    # backend subnet
    resource "google_compute_subnetwork" "ilb_subnet" {
      name          = "l7-ilb-subnet"
      provider      = google-beta
      ip_cidr_range = "10.0.1.0/24"
      region        = "europe-west1"
      network       = google_compute_network.ilb_network.id
    }
    
    # forwarding rule
    resource "google_compute_forwarding_rule" "google_compute_forwarding_rule" {
      name                  = "l7-ilb-forwarding-rule"
      provider              = google-beta
      region                = "europe-west1"
      depends_on            = [google_compute_subnetwork.proxy_subnet]
      ip_protocol           = "TCP"
      load_balancing_scheme = "INTERNAL_MANAGED"
      port_range            = "80"
      target                = google_compute_region_target_http_proxy.default.id
      network               = google_compute_network.ilb_network.id
      subnetwork            = google_compute_subnetwork.ilb_subnet.id
      network_tier          = "PREMIUM"
    }
    
    # HTTP target proxy
    resource "google_compute_region_target_http_proxy" "default" {
      name     = "l7-ilb-target-http-proxy"
      provider = google-beta
      region   = "europe-west1"
      url_map  = google_compute_region_url_map.default.id
    }
    
    # URL map
    resource "google_compute_region_url_map" "default" {
      name            = "l7-ilb-regional-url-map"
      provider        = google-beta
      region          = "europe-west1"
      default_service = google_compute_region_backend_service.default.id
    }
    
    # backend service
    resource "google_compute_region_backend_service" "default" {
      name                  = "l7-ilb-backend-subnet"
      provider              = google-beta
      region                = "europe-west1"
      protocol              = "HTTP"
      load_balancing_scheme = "INTERNAL_MANAGED"
      timeout_sec           = 10
      health_checks         = [google_compute_region_health_check.default.id]
      backend {
        group           = google_compute_region_instance_group_manager.mig.instance_group
        balancing_mode  = "UTILIZATION"
        capacity_scaler = 1.0
      }
    }
    
    # instance template
    resource "google_compute_instance_template" "instance_template" {
      name         = "l7-ilb-mig-template"
      provider     = google-beta
      machine_type = "e2-small"
      tags         = ["http-server"]
    
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
    
    # health check
    resource "google_compute_region_health_check" "default" {
      name     = "l7-ilb-hc"
      provider = google-beta
      region   = "europe-west1"
      http_health_check {
        port_specification = "USE_SERVING_PORT"
      }
    }
    
    # MIG
    resource "google_compute_region_instance_group_manager" "mig" {
      name     = "l7-ilb-mig1"
      provider = google-beta
      region   = "europe-west1"
      version {
        instance_template = google_compute_instance_template.instance_template.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
    }
    
    # allow all access from IAP and health check ranges
    resource "google_compute_firewall" "fw_iap" {
      name          = "l7-ilb-fw-allow-iap-hc"
      provider      = google-beta
      direction     = "INGRESS"
      network       = google_compute_network.ilb_network.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16", "35.235.240.0/20"]
      allow {
        protocol = "tcp"
      }
    }
    
    # allow http from proxy subnet to backends
    resource "google_compute_firewall" "fw_ilb_to_backends" {
      name          = "l7-ilb-fw-allow-ilb-to-backends"
      provider      = google-beta
      direction     = "INGRESS"
      network       = google_compute_network.ilb_network.id
      source_ranges = ["10.0.0.0/24"]
      target_tags   = ["http-server"]
      allow {
        protocol = "tcp"
        ports    = ["80", "443", "8080"]
      }
    }
    
    # test instance
    resource "google_compute_instance" "vm_test" {
      name         = "l7-ilb-test-vm"
      provider     = google-beta
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

## Regional internal Application Load Balancer with a MIG backend and an HTTP-to-HTTPS redirect

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an internal HTTPS load balancer with a MIG backend and an HTTP-to-HTTPS redirect.

For information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect).
    
    
    # VPC network
    resource "google_compute_network" "default" {
      name                    = "l7-ilb-network"
      auto_create_subnetworks = false
    }
    
    # Proxy-only subnet
    resource "google_compute_subnetwork" "proxy_subnet" {
      name          = "l7-ilb-proxy-subnet"
      ip_cidr_range = "10.0.0.0/24"
      region        = "europe-west1"
      purpose       = "REGIONAL_MANAGED_PROXY"
      role          = "ACTIVE"
      network       = google_compute_network.default.id
    }
    
    # Backend subnet
    resource "google_compute_subnetwork" "default" {
      name          = "l7-ilb-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "europe-west1"
      network       = google_compute_network.default.id
    }
    
    # Reserved internal address
    resource "google_compute_address" "default" {
      name         = "l7-ilb-ip"
      provider     = google-beta
      subnetwork   = google_compute_subnetwork.default.id
      address_type = "INTERNAL"
      address      = "10.0.1.5"
      region       = "europe-west1"
      purpose      = "SHARED_LOADBALANCER_VIP"
    }
    
    # Regional forwarding rule
    resource "google_compute_forwarding_rule" "default" {
      name                  = "l7-ilb-forwarding-rule"
      region                = "europe-west1"
      depends_on            = [google_compute_subnetwork.proxy_subnet]
      ip_protocol           = "TCP"
      ip_address            = google_compute_address.default.id
      load_balancing_scheme = "INTERNAL_MANAGED"
      port_range            = "443"
      target                = google_compute_region_target_https_proxy.default.id
      network               = google_compute_network.default.id
      subnetwork            = google_compute_subnetwork.default.id
      network_tier          = "PREMIUM"
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
    
    resource "google_compute_region_ssl_certificate" "default" {
      name_prefix = "my-certificate-"
      private_key = tls_private_key.default.private_key_pem
      certificate = tls_self_signed_cert.default.cert_pem
      region      = "europe-west1"
      lifecycle {
        create_before_destroy = true
      }
    }
    
    # Regional target HTTPS proxy
    resource "google_compute_region_target_https_proxy" "default" {
      name             = "l7-ilb-target-https-proxy"
      region           = "europe-west1"
      url_map          = google_compute_region_url_map.https_lb.id
      ssl_certificates = [google_compute_region_ssl_certificate.default.self_link]
    }
    
    # Regional URL map
    resource "google_compute_region_url_map" "https_lb" {
      name            = "l7-ilb-regional-url-map"
      region          = "europe-west1"
      default_service = google_compute_region_backend_service.default.id
    }
    
    # Regional backend service
    resource "google_compute_region_backend_service" "default" {
      name                  = "l7-ilb-backend-service"
      region                = "europe-west1"
      protocol              = "HTTP"
      port_name             = "http-server"
      load_balancing_scheme = "INTERNAL_MANAGED"
      timeout_sec           = 10
      health_checks         = [google_compute_region_health_check.default.id]
      backend {
        group           = google_compute_region_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        capacity_scaler = 1.0
      }
    }
    
    # Instance template
    resource "google_compute_instance_template" "default" {
      name         = "l7-ilb-mig-template"
      machine_type = "e2-small"
      tags         = ["http-server"]
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
    
    # Regional health check
    resource "google_compute_region_health_check" "default" {
      name   = "l7-ilb-hc"
      region = "europe-west1"
      http_health_check {
        port_specification = "USE_SERVING_PORT"
      }
    }
    
    # Regional MIG
    resource "google_compute_region_instance_group_manager" "default" {
      name   = "l7-ilb-mig1"
      region = "europe-west1"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      named_port {
        name = "http-server"
        port = 80
      }
      base_instance_name = "vm"
      target_size        = 2
    }
    
    # Allow all access to health check ranges
    resource "google_compute_firewall" "default" {
      name          = "l7-ilb-fw-allow-hc"
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16", "35.235.240.0/20"]
      allow {
        protocol = "tcp"
      }
    }
    
    # Allow http from proxy subnet to backends
    resource "google_compute_firewall" "backends" {
      name          = "l7-ilb-fw-allow-ilb-to-backends"
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["10.0.0.0/24"]
      target_tags   = ["http-server"]
      allow {
        protocol = "tcp"
        ports    = ["80", "443", "8080"]
      }
    }
    
    # Test instance
    resource "google_compute_instance" "default" {
      name         = "l7-ilb-test-vm"
      zone         = "europe-west1-b"
      machine_type = "e2-small"
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-12"
        }
      }
    }
    
    ### HTTP-to-HTTPS redirect ###
    
    # Regional forwarding rule
    resource "google_compute_forwarding_rule" "redirect" {
      name                  = "l7-ilb-redirect"
      region                = "europe-west1"
      ip_protocol           = "TCP"
      ip_address            = google_compute_address.default.id # Same as HTTPS load balancer
      load_balancing_scheme = "INTERNAL_MANAGED"
      port_range            = "80"
      target                = google_compute_region_target_http_proxy.default.id
      network               = google_compute_network.default.id
      subnetwork            = google_compute_subnetwork.default.id
      network_tier          = "PREMIUM"
    }
    
    # Regional HTTP proxy
    resource "google_compute_region_target_http_proxy" "default" {
      name    = "l7-ilb-target-http-proxy"
      region  = "europe-west1"
      url_map = google_compute_region_url_map.redirect.id
    }
    
    # Regional URL map
    resource "google_compute_region_url_map" "redirect" {
      name            = "l7-ilb-redirect-url-map"
      region          = "europe-west1"
      default_service = google_compute_region_backend_service.default.id
      host_rule {
        hosts        = ["*"]
        path_matcher = "allpaths"
      }
    
      path_matcher {
        name            = "allpaths"
        default_service = google_compute_region_backend_service.default.id
        path_rule {
          paths = ["/"]
          url_redirect {
            https_redirect         = true
            host_redirect          = "10.0.1.5:443"
            redirect_response_code = "PERMANENT_REDIRECT"
            strip_query            = true
          }
        }
      }
    }

## Regional internal Application Load Balancer that uses Shared VPC and a cross-project backend service

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up a regional internal Application Load Balancer that uses Shared VPC and a cross-project backend service. The following architecture diagram shows where the load balancer components are created.

[ ![Load balancer frontend and backend in different service projects.](https://docs.cloud.google.com/static/load-balancing/images/reg-int-https-lb-l7-shared-vpc-service-lb.svg)](https://docs.cloud.google.com/static/load-balancing/images/reg-int-https-lb-l7-shared-vpc-service-lb.svg) **Figure 1.** Load balancer frontend and backend in different service projects.

Before you start setting up a regional internal Application Load Balancer that uses Shared VPC, ensure that you have the required [IAM permissions on the host and service projects](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc#shared-vpc-permissions). For more detailed information about the load balancer setup, see the [ primary setup guide](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc#cross-project).
    
    
    # VPC network
    resource "google_compute_network" "default" {
      name                    = "l7-ilb-network"
      auto_create_subnetworks = false
      project                 = "my-host-project"
    }
    
    # proxy-only subnet
    # https://cloud.google.com/load-balancing/docs/proxy-only-subnets#proxy_only_subnet_create
    resource "google_compute_subnetwork" "proxy_subnet" {
      name          = "l7-ilb-proxy-subnet"
      ip_cidr_range = "10.0.0.0/24"
      region        = "us-central1"
      purpose       = "REGIONAL_MANAGED_PROXY"
      role          = "ACTIVE"
      network       = google_compute_network.default.id
      project       = "my-host-project"
    }
    
    # backend subnet
    resource "google_compute_subnetwork" "ilb_subnet" {
      name          = "l7-ilb-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.default.id
      project       = "my-host-project"
    }
    
    # allow all access from IAP and health check ranges
    resource "google_compute_firewall" "fw_iap" {
      project       = "my-host-project"
      name          = "l7-ilb-fw-allow-iap-hc"
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16", "35.235.240.0/20"]
      allow {
        protocol = "tcp"
      }
    }
    
    # allow http from proxy subnet to backends
    resource "google_compute_firewall" "fw_ilb_to_backends" {
      project       = "my-host-project"
      name          = "l7-ilb-fw-allow-ilb-to-backends"
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["0.0.0.0/0"]
      target_tags   = ["http-server"]
      allow {
        protocol = "tcp"
        ports    = ["80", "443", "8080"]
      }
    }
    
    # forwarding rule
    resource "google_compute_forwarding_rule" "default" {
      name                  = "l7-ilb-forwarding-rule"
      region                = "us-central1"
      ip_protocol           = "TCP"
      load_balancing_scheme = "INTERNAL_MANAGED"
      port_range            = "80"
      target                = google_compute_region_target_http_proxy.default.id
      network               = google_compute_network.default.id
      subnetwork            = google_compute_subnetwork.ilb_subnet.id
      network_tier          = "PREMIUM"
      project               = "my-service-project-01"
      depends_on            = [google_compute_subnetwork.proxy_subnet]
    }
    
    # HTTP target proxy
    resource "google_compute_region_target_http_proxy" "default" {
      name    = "l7-ilb-target-http-proxy"
      region  = "us-central1"
      url_map = google_compute_region_url_map.default.id
      project = "my-service-project-01"
    }
    
    # URL map
    resource "google_compute_region_url_map" "default" {
      name            = "l7-ilb-regional-url-map"
      region          = "us-central1"
      default_service = google_compute_region_backend_service.default.id
      project         = "my-service-project-01"
    }
    
    # regional health check
    resource "google_compute_region_health_check" "default" {
      project = "my-service-project-02"
      name    = "l7-ilb-rhc"
      region  = "us-central1"
      http_health_check {
        port_specification = "USE_SERVING_PORT"
      }
    }
    
    # regional backend service
    resource "google_compute_region_backend_service" "default" {
      project               = "my-service-project-02"
      name                  = "l7-ilb-backend-service"
      region                = "us-central1"
      protocol              = "HTTP"
      load_balancing_scheme = "INTERNAL_MANAGED"
      timeout_sec           = 10
      health_checks         = [google_compute_region_health_check.default.id]
      backend {
        group           = google_compute_region_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        capacity_scaler = 1.0
      }
    }
    
    # health check
    resource "google_compute_health_check" "default" {
      project            = "my-service-project-02"
      name               = "l7-ilb-hc"
      timeout_sec        = 1
      check_interval_sec = 1
      tcp_health_check {
        port = "80"
      }
    }
    
    # instance template
    resource "google_compute_instance_template" "default" {
      project      = "my-service-project-02"
      name         = "l7-ilb-mig-template"
      machine_type = "e2-small"
      tags         = ["http-server"]
    
      network_interface {
        network    = google_compute_network.default.id
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
    }
    
    # MIG
    resource "google_compute_region_instance_group_manager" "default" {
      project = "my-service-project-02"
      name    = "l7-ilb-mig1"
      region  = "us-central1"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
      auto_healing_policies {
        health_check      = google_compute_health_check.default.id
        initial_delay_sec = 300
      }
      depends_on = [google_project_iam_binding.default]
    }
    
    data "google_project" "service_project02" {
      project_id = "my-service-project-02"
    }
    
    # IAM Role
    resource "google_project_iam_binding" "default" {
      project = "my-host-project"
      role    = "roles/compute.networkUser"
    
      members = [
        "serviceAccount:${data.google_project.service_project02.number}@cloudservices.gserviceaccount.com",
      ]
    }
    
    # test instance
    resource "google_compute_instance" "test_vm" {
      project      = "my-service-project-02"
      name         = "l7-ilb-test-vm"
      zone         = "us-central1-b"
      machine_type = "e2-small"
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.ilb_subnet.id
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-12"
        }
      }
      lifecycle {
        ignore_changes = [
          metadata["ssh-keys"]
        ]
      }
      depends_on = [google_project_iam_binding.default]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
