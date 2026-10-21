---
url: https://docs.cloud.google.com/compute/docs/samples/compute-flask-quickstart-vpc/
title: Create a custom VPC Subnet \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:16.650946+00:00
---

# Create a custom VPC Subnet  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-flask-quickstart-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a custom VPC Subnet Stay organized with collections  Save and categorize content based on your preferences. 

Create a subnet with a custom IP address range.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deploy a basic Flask web server by using Terraform](https://docs.cloud.google.com/docs/terraform/deploy-flask-web-server)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_network" "vpc_network" {
      name                    = "my-custom-mode-network"
      auto_create_subnetworks = false
      mtu                     = 1460
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "my-custom-subnet"
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-west1"
      network       = google_compute_network.vpc_network.id
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
