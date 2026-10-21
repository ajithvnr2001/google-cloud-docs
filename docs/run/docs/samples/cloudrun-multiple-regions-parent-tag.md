---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-multiple-regions-parent-tag/
title: Configure multiple regions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:49.150648+00:00
---

# Configure multiple regions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-multiple-regions-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Configure multiple regions Stay organized with collections  Save and categorize content based on your preferences. 

Set a Cloud Run service to be available in multiple regions

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service" "compute_api" {
      provider                   = google-beta
      service                    = "compute.googleapis.com"
      disable_dependent_services = false
      disable_on_destroy         = false
    }
    
    resource "google_project_service" "run_api" {
      provider                   = google-beta
      service                    = "run.googleapis.com"
      disable_dependent_services = false
      disable_on_destroy         = false
    }
    
    resource "google_compute_global_address" "lb_default" {
      provider = google-beta
      name     = "myservice-service-ip"
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.compute_api
      ]
    }
    
    resource "google_compute_backend_service" "lb_default" {
      provider              = google-beta
      name                  = "myservice-backend"
      load_balancing_scheme = "EXTERNAL_MANAGED"
    
      backend {
        group = google_compute_region_network_endpoint_group.lb_default[0].id
      }
    
      backend {
        group = google_compute_region_network_endpoint_group.lb_default[1].id
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.compute_api,
      ]
    }
    
    resource "google_compute_url_map" "lb_default" {
      provider        = google-beta
      name            = "myservice-lb-urlmap"
      default_service = google_compute_backend_service.lb_default.id
    
      path_matcher {
        name            = "allpaths"
        default_service = google_compute_backend_service.lb_default.id
        route_rules {
          priority = 1
          url_redirect {
            https_redirect         = true
            redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
          }
        }
      }
    }
    
    resource "google_compute_managed_ssl_certificate" "lb_default" {
      provider = google-beta
      name     = "myservice-ssl-cert"
    
      managed {
        domains = ["example.com"]
      }
    }
    resource "google_compute_target_https_proxy" "lb_default" {
      provider = google-beta
      name     = "myservice-https-proxy"
      url_map  = google_compute_url_map.lb_default.id
      ssl_certificates = [
        google_compute_managed_ssl_certificate.lb_default.name
      ]
      depends_on = [
        google_compute_managed_ssl_certificate.lb_default
      ]
    }
    
    resource "google_compute_global_forwarding_rule" "lb_default" {
      provider              = google-beta
      name                  = "myservice-lb-fr"
      load_balancing_scheme = "EXTERNAL_MANAGED"
      target                = google_compute_target_https_proxy.lb_default.id
      ip_address            = google_compute_global_address.lb_default.id
      port_range            = "443"
      depends_on            = [google_compute_target_https_proxy.lb_default]
    }
    
    resource "google_compute_region_network_endpoint_group" "lb_default" {
      provider              = google-beta
      count                 = length(local.run_regions)
      name                  = "myservice-neg"
      network_endpoint_type = "SERVERLESS"
      region                = local.run_regions[count.index]
      cloud_run {
        service = google_cloud_run_v2_service.run_default[count.index].name
      }
    }
    
    output "load_balancer_ip_addr" {
      value = google_compute_global_address.lb_default.address
    }
    
    resource "google_cloud_run_v2_service" "run_default" {
      provider = google-beta
      count    = length(local.run_regions)
      name     = "myservice-run-app-${local.run_regions[count.index]}"
      location = local.run_regions[count.index]
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.run_api
      ]
    }
    
    resource "google_cloud_run_service_iam_member" "run_allow_unauthenticated" {
      provider = google-beta
      count    = length(local.run_regions)
      location = google_cloud_run_v2_service.run_default[count.index].location
      service  = google_cloud_run_v2_service.run_default[count.index].name
      role     = "roles/run.invoker"
      member   = "allUsers"
    }
    
    resource "google_compute_url_map" "https_default" {
      provider = google-beta
      name     = "myservice-https-urlmap"
    
      default_url_redirect {
        redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
        https_redirect         = true
        strip_query            = false
      }
    }
    
    resource "google_compute_target_http_proxy" "https_default" {
      provider = google-beta
      name     = "myservice-http-proxy"
      url_map  = google_compute_url_map.https_default.id
    
      depends_on = [
        google_compute_url_map.https_default
      ]
    }
    
    resource "google_compute_global_forwarding_rule" "https_default" {
      provider   = google-beta
      name       = "myservice-https-fr"
      target     = google_compute_target_http_proxy.https_default.id
      ip_address = google_compute_global_address.lb_default.id
      port_range = "80"
      depends_on = [google_compute_target_http_proxy.https_default]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
