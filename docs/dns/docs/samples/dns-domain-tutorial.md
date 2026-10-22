---
url: https://docs.cloud.google.com/dns/docs/samples/dns-domain-tutorial/
title: Set up a domain using Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:53.055193+00:00
---

# Set up a domain using Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/samples/dns-domain-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Samples ](https://docs.cloud.google.com/dns/docs/samples)



#  Set up a domain using Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

Register a domain, set up a sample web server, and use Cloud DNS to point the domain URL to the server.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Tutorial: Set up a domain by using Cloud DNS](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # to setup a web-server
    
    resource "random_id" "rnd" {
      byte_length = 4
    }
    
    resource "google_compute_instance" "default" {
      name         = "dns-compute-instance"
      machine_type = "g1-small"
      zone         = "us-central1-b"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      network_interface {
        network = "default"
        access_config {
          // Ephemeral public IP
        }
      }
      metadata_startup_script = <<-EOF
      sudo apt-get update && \
      sudo apt-get install apache2 -y && \
      echo "<!doctype html><html><body><h1>Hello World!</h1></body></html>" > /var/www/html/index.html
      EOF
    }
    
    # to allow http traffic
    resource "google_compute_firewall" "default" {
      name    = "allow-http-traffic"
      network = "default"
      allow {
        ports    = ["80"]
        protocol = "tcp"
      }
      source_ranges = ["0.0.0.0/0"]
    }
    
    # to create a DNS zone
    resource "google_dns_managed_zone" "default" {
      name          = "example-zone-googlecloudexample"
      dns_name      = "example-${random_id.rnd.hex}.com."
      description   = "Example DNS zone"
      force_destroy = "true"
    }
    
    # to register web-server's ip address in DNS
    resource "google_dns_record_set" "default" {
      name         = google_dns_managed_zone.default.dns_name
      managed_zone = google_dns_managed_zone.default.name
      type         = "A"
      ttl          = 300
      rrdatas = [
        google_compute_instance.default.network_interface[0].access_config[0].nat_ip
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddns). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
