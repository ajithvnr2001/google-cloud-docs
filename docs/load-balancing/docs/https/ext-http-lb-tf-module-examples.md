---
url: https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples/
title: Terraform examples for external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:39.919421+00:00
---

# Terraform examples for external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Terraform examples for external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page provides Terraform modules that you can use to deploy external Application Load Balancers. Depending on your preferred backend type, use one of the following examples to deploy a sample external Application Load Balancer.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

To use prebuilt Terraform templates to streamline the setup and management of Google Cloud's networking infrastructure, explore the [Simplified Cloud Networking Configuration Solutions GitHub repository](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).

## External Application Load Balancer with managed instance group (MIG) backends

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/master/examples/multi-mig-http-lb) to bring up an external HTTP load balancer with Compute Engine backends.

This module creates multiple Terraform resources, including a VPC network and subnetworks, Cloud Routers, all of the necessary load balancer components, and backend instance groups. For more information, download or clone the repository and run the `terraform plan` command in the `/terraform-google-lb-http/examples/multi-mig-http-lb` directory.

For more information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/examples/multi-mig-http-lb/README.md) on GitHub.
    
    
    module "gce-lb-http" {
      source  = "terraform-google-modules/lb-http/google"
      version = "~> 14.0"
      name    = var.network_prefix
      project = var.project
      target_tags = [
        "${var.network_prefix}-group1",
        module.cloud-nat-group1.router_name,
        "${var.network_prefix}-group2",
        module.cloud-nat-group2.router_name
      ]
      firewall_networks = [google_compute_network.default.name]
    
      backends = {
        default = {
    
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = {
            request_path = "/"
            port         = 80
          }
    
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
    
          groups = [
            {
              group = module.mig1.instance_group
            },
            {
              group = module.mig2.instance_group
            },
          ]
    
          iap_config = {
            enable = false
          }
        }
      }
    }

## External Application Load Balancer with MIG backend and custom headers

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an external Application Load Balancer with a [Cloud CDN-enabled](https://docs.cloud.google.com/cdn/docs) backend service and [custom request and response headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers).

For detailed information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple).
    
    
    # VPC
    resource "google_compute_network" "default" {
      name                    = "l7-xlb-network"
      provider                = google-beta
      auto_create_subnetworks = false
    }
    
    # backend subnet
    resource "google_compute_subnetwork" "default" {
      name          = "l7-xlb-subnet"
      provider      = google-beta
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.default.id
    }
    
    # reserved IP address
    resource "google_compute_global_address" "default" {
      provider = google-beta
      name     = "l7-xlb-static-ip"
    }
    
    # forwarding rule
    resource "google_compute_global_forwarding_rule" "default" {
      name                  = "l7-xlb-forwarding-rule"
      provider              = google-beta
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL"
      port_range            = "80"
      target                = google_compute_target_http_proxy.default.id
      ip_address            = google_compute_global_address.default.id
    }
    
    # http proxy
    resource "google_compute_target_http_proxy" "default" {
      name     = "l7-xlb-target-http-proxy"
      provider = google-beta
      url_map  = google_compute_url_map.default.id
    }
    
    # url map
    resource "google_compute_url_map" "default" {
      name            = "l7-xlb-url-map"
      provider        = google-beta
      default_service = google_compute_backend_service.default.id
    }
    
    # backend service with custom request and response headers
    resource "google_compute_backend_service" "default" {
      name                    = "l7-xlb-backend-service"
      provider                = google-beta
      protocol                = "HTTP"
      port_name               = "my-port"
      load_balancing_scheme   = "EXTERNAL"
      timeout_sec             = 10
      enable_cdn              = true
      custom_request_headers  = ["X-Client-Geo-Location: {client_region_subdivision}, {client_city}"]
      custom_response_headers = ["X-Cache-Hit: {cdn_cache_status}"]
      health_checks           = [google_compute_health_check.default.id]
      backend {
        group           = google_compute_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        capacity_scaler = 1.0
      }
    }
    
    # instance template
    resource "google_compute_instance_template" "default" {
      name         = "l7-xlb-mig-template"
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
    
    # health check
    resource "google_compute_health_check" "default" {
      name     = "l7-xlb-hc"
      provider = google-beta
      http_health_check {
        port_specification = "USE_SERVING_PORT"
      }
    }
    
    # MIG
    resource "google_compute_instance_group_manager" "default" {
      name     = "l7-xlb-mig1"
      provider = google-beta
      zone     = "us-central1-c"
      named_port {
        name = "http"
        port = 8080
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
      name          = "l7-xlb-fw-allow-hc"
      provider      = google-beta
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
      allow {
        protocol = "tcp"
      }
      target_tags = ["allow-health-check"]
    }

## External Application Load Balancer with a backend bucket and MIGs

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/master/examples/multi-backend-multi-mig-bucket-https-lb) to bring up an external HTTPS load balancer with Compute Engine backends plus static assets being served from a Cloud Storage bucket.

This module creates multiple Terraform resources, including a VPC network and subnetworks, a Cloud Storage bucket and object, Cloud Routers, a self-signed SSL certificate, all of the necessary load balancer components, and backend instance groups. For more information, download or clone the repository and run the `terraform plan` command in the `/terraform-google-lb-http/examples/multi-backend-multi-mig-bucket-https-lb` directory.

For more information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/examples/multi-backend-multi-mig-bucket-https-lb/README.md) in GitHub.
    
    
    module "gce-lb-https" {
      source  = "terraform-google-modules/lb-http/google"
      version = "~> 14.0"
      name    = var.network_name
      project = var.project
      target_tags = [
        "${var.network_name}-group1",
        module.cloud-nat-group1.router_name,
        "${var.network_name}-group2",
        module.cloud-nat-group2.router_name,
        "${var.network_name}-group3",
        module.cloud-nat-group3.router_name
      ]
      firewall_networks = [google_compute_network.default.self_link]
      url_map           = google_compute_url_map.ml-bkd-ml-mig-bckt-s-lb.self_link
      create_url_map    = false
      ssl               = true
      private_key       = tls_private_key.example.private_key_pem
      certificate       = tls_self_signed_cert.example.cert_pem
    
      backends = {
        default = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = local.health_check
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
          groups = [
            {
              group = module.mig1.instance_group
            },
            {
              group = module.mig2.instance_group
            },
            {
              group = module.mig3.instance_group
            },
          ]
    
          iap_config = {
            enable = false
          }
        }
    
        mig1 = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = local.health_check
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
          groups = [
            {
              group = module.mig1.instance_group
            },
          ]
    
          iap_config = {
            enable = false
          }
        }
    
        mig2 = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = local.health_check
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
          groups = [
            {
              group = module.mig2.instance_group
            },
          ]
    
          iap_config = {
            enable = false
          }
        }
    
        mig3 = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = local.health_check
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
          groups = [
            {
              group = module.mig3.instance_group
            },
          ]
    
          iap_config = {
            enable = false
          }
        }
      }
    }
    
    resource "google_compute_url_map" "ml-bkd-ml-mig-bckt-s-lb" {
      // note that this is the name of the load balancer
      name            = var.network_name
      default_service = module.gce-lb-https.backend_services["default"].self_link
    
      host_rule {
        hosts        = ["*"]
        path_matcher = "allpaths"
      }
    
      path_matcher {
        name            = "allpaths"
        default_service = module.gce-lb-https.backend_services["default"].self_link
    
        path_rule {
          paths = [
            "/group1",
            "/group1/*"
          ]
          service = module.gce-lb-https.backend_services["mig1"].self_link
        }
    
        path_rule {
          paths = [
            "/group2",
            "/group2/*"
          ]
          service = module.gce-lb-https.backend_services["mig2"].self_link
        }
    
        path_rule {
          paths = [
            "/group3",
            "/group3/*"
          ]
          service = module.gce-lb-https.backend_services["mig3"].self_link
        }
    
        path_rule {
          paths = [
            "/assets",
            "/assets/*"
          ]
          service = google_compute_backend_bucket.assets.self_link
        }
      }
    }
    
    resource "google_compute_backend_bucket" "assets" {
      name        = random_id.assets-bucket.hex
      description = "Contains static resources for example app"
      bucket_name = google_storage_bucket.assets.name
      enable_cdn  = true
    }
    
    resource "google_storage_bucket" "assets" {
      name     = random_id.assets-bucket.hex
      location = "US"
    
      // delete bucket and contents on destroy.
      force_destroy = true
    }
    
    // The image object in Cloud Storage.
    // Note that the path in the bucket matches the paths in the url map path rule above.
    resource "google_storage_bucket_object" "image" {
      name         = "assets/gcp-logo.svg"
      content      = file("gcp-logo.svg")
      content_type = "image/svg+xml"
      bucket       = google_storage_bucket.assets.name
    }
    
    // Make object public readable.
    resource "google_storage_object_acl" "image-acl" {
      bucket         = google_storage_bucket.assets.name
      object         = google_storage_bucket_object.image.name
      predefined_acl = "publicRead"
    }

## External Application Load Balancer with a Cloud Run backend

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/master/examples/cloudrun) to bring up an external HTTPS load balancer with a Cloud Run backend.

This module creates multiple Terraform resources, including a Cloud Run service, a self-signed SSL certificate, a URL map that sets up an HTTP-to-HTTPs redirect, all of the necessary load balancer components, and backend instance groups. For more information, download or clone the repository and run the `terraform plan` command in the `/terraform-google-lb-http/examples/cloudrun` directory.

For more information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/examples/cloudrun/README.md) in GitHub.
    
    
    module "lb-http" {
      source  = "terraform-google-modules/lb-http/google//modules/serverless_negs"
      version = "~> 14.0"
    
      name    = var.lb_name
      project = var.project_id
    
      ssl                             = var.ssl
      managed_ssl_certificate_domains = [var.domain]
      https_redirect                  = var.ssl
      labels                          = { "example-label" = "cloud-run-example" }
    
      backends = {
        default = {
          description = null
          groups = [
            {
              group = google_compute_region_network_endpoint_group.serverless_neg.id
            }
          ]
          enable_cdn = false
    
          iap_config = {
            enable = false
          }
          log_config = {
            enable = false
          }
        }
      }
    }
    
    resource "google_compute_region_network_endpoint_group" "serverless_neg" {
      provider              = google-beta
      name                  = "serverless-neg"
      network_endpoint_type = "SERVERLESS"
      region                = var.region
      cloud_run {
        service = google_cloud_run_service.default.name
      }
    }
    
    resource "google_cloud_run_service" "default" {
      name     = "example"
      location = var.region
      project  = var.project_id
    
      template {
        spec {
          containers {
            image = "gcr.io/cloudrun/hello"
          }
        }
      }
      metadata {
        annotations = {
          # For valid annotation values and descriptions, see
          # https://cloud.google.com/sdk/gcloud/reference/run/deploy#--ingress
          "run.googleapis.com/ingress" = "all"
        }
      }
    }
    
    resource "google_cloud_run_service_iam_member" "public-access" {
      location = google_cloud_run_service.default.location
      project  = google_cloud_run_service.default.project
      service  = google_cloud_run_service.default.name
      role     = "roles/run.invoker"
      member   = "allUsers"
    }

## External Application Load Balancer with an HTTP-to-HTTPS redirect

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/master/examples/https-redirect) to bring up an external HTTPS load balancer with HTTP-to-HTTPS redirection.

This module creates multiple Terraform resources, including a VPC network and subnetwork, a self-signed SSL certificate, a Cloud Router, all of the necessary load balancer components, and a backend instance group. For more information, download or clone the repository and run the `terraform plan` command in the `/terraform-google-lb-http/examples/https-redirect` directory.

For more information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/examples/https-redirect/README.md) in GitHub.
    
    
    module "gce-lb-http" {
      source            = "terraform-google-modules/lb-http/google"
      version           = "~> 14.0"
      name              = "ci-https-redirect"
      project           = var.project
      target_tags       = [var.network_name]
      firewall_networks = [google_compute_network.default.name]
      ssl               = true
      ssl_certificates  = [google_compute_ssl_certificate.example.self_link]
      https_redirect    = true
    
      backends = {
        default = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = {
            request_path = "/"
            port         = 80
          }
    
          log_config = {
            enable = false
          }
    
          groups = [
            {
              group = module.mig.instance_group
            }
          ]
          iap_config = {
            enable = false
          }
        }
      }
    }

## External Application Load Balancer with Shared VPC

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/master/examples/shared-vpc) to bring up an external Application Load Balancer in a Shared VPC setup.

This module creates multiple Terraform resources, including a VPC network and subnetwork, a Cloud Router, all of the necessary load balancer components, and a backend instance group. For more information, download or clone the repository and run the `terraform plan` command in the `/terraform-google-lb-http/examples/shared-vpc` directory.

For more information about this example and to learn how to run it, see the [README](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/examples/shared-vpc/README.md) in GitHub.
    
    
    module "gce-lb-http" {
      source  = "terraform-google-modules/lb-http/google"
      version = "~> 14.0"
    
      name              = "group-http-lb"
      project           = var.service_project
      target_tags       = ["allow-shared-vpc-mig"]
      firewall_projects = [var.host_project]
      firewall_networks = [var.network]
    
      backends = {
        default = {
          protocol    = "HTTP"
          port        = 80
          port_name   = "http"
          timeout_sec = 10
          enable_cdn  = false
    
          health_check = {
            request_path = "/"
            port         = 80
          }
    
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
    
          groups = [
            {
              group = module.mig.instance_group
            }
          ]
    
          iap_config = {
            enable = false
          }
        }
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
