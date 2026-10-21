---
url: https://docs.cloud.google.com/cdn/docs/cdn-terraform-examples/
title: Automate Cloud CDN setup with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:49.351979+00:00
---

# Automate Cloud CDN setup with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/cdn-terraform-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Automate Cloud CDN setup with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Use the following examples to deploy sample backends with Cloud CDN enabled.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Using a Cloud Storage bucket

The following sample configures Cloud CDN with a public Cloud Storage bucket. The sample also includes load balancing and caching configurations. The configurations can be modified, as required.

For details about each section of the sample, see [Set up a backend bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#terraform_1).
    
    
    # Cloud Storage bucket
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name                        = "${random_id.bucket_prefix.hex}-my-bucket"
      location                    = "us-east1"
      uniform_bucket_level_access = true
      storage_class               = "STANDARD"
      // delete bucket and contents on destroy.
      force_destroy = true
      // Assign specialty files
      website {
        main_page_suffix = "index.html"
        not_found_page   = "404.html"
      }
    }
    
    
    # make bucket public
    resource "google_storage_bucket_iam_member" "default" {
      bucket = google_storage_bucket.default.name
      role   = "roles/storage.objectViewer"
      member = "allUsers"
    }
    
    resource "google_storage_bucket_object" "index_page" {
      name    = "index-page"
      bucket  = google_storage_bucket.default.name
      content = <<-EOT
        <html><body>
        <h1>Congratulations on setting up Google Cloud CDN with Storage backend!</h1>
        </body></html>
      EOT
    }
    
    resource "google_storage_bucket_object" "error_page" {
      name    = "404-page"
      bucket  = google_storage_bucket.default.name
      content = <<-EOT
        <html><body>
        <h1>404 Error: Object you are looking for is no longer available!</h1>
        </body></html>
      EOT
    }
    
    # image object for testing, try to access http://<your_lb_ip_address>/test.jpg
    resource "google_storage_bucket_object" "test_image" {
      name = "test-object"
      # Uncomment and add valid path to an object.
      #  source       = "/path/to/an/object"
      #  content_type = "image/jpeg"
    
      # Delete after uncommenting above source and content_type attributes
      content      = "Data as string to be uploaded"
      content_type = "text/plain"
    
      bucket = google_storage_bucket.default.name
    }
    
    # reserve IP address
    resource "google_compute_global_address" "default" {
      name = "example-ip"
    }
    
    # forwarding rule
    resource "google_compute_global_forwarding_rule" "default" {
      name                  = "http-lb-forwarding-rule"
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL"
      port_range            = "80"
      target                = google_compute_target_http_proxy.default.id
      ip_address            = google_compute_global_address.default.id
    }
    
    # http proxy
    resource "google_compute_target_http_proxy" "default" {
      name    = "http-lb-proxy"
      url_map = google_compute_url_map.default.id
    }
    
    # url map
    resource "google_compute_url_map" "default" {
      name            = "http-lb"
      default_service = google_compute_backend_bucket.default.id
    }
    
    # backend bucket with CDN policy with default ttl settings
    resource "google_compute_backend_bucket" "default" {
      name        = "cat-backend-bucket"
      description = "Contains beautiful images"
      bucket_name = google_storage_bucket.default.name
      enable_cdn  = true
      cdn_policy {
        cache_mode        = "CACHE_ALL_STATIC"
        client_ttl        = 3600
        default_ttl       = 3600
        max_ttl           = 86400
        negative_caching  = true
        serve_while_stale = 86400
      }
    }

## Using MIG and custom headers

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up an external HTTP load balancer with a Cloud CDN backend service and [custom request and response headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers).

For information about the load balancer setup, see the [primary setup guide](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-mig).
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
