---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-authorized-networks/
title: Configure authorized networks in Managed Airflow \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:05.334974+00:00
---

# Configure authorized networks in Managed Airflow  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-authorized-networks/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure authorized networks in Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to configure [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) for your environment.

## About authorized networks in Managed Airflow

[Authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) allow you to specify CIDR ranges that can access your environment's cluster control plane using HTTPS.

For example, in Managed Airflow (Legacy Gen 1), such access to your environment's cluster is required in Private IP environments to [run Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli)(`gcloud composer environments run`). Networks from where such requests are originated must be authorized to access the control plane of your environment's cluster.

## Authorized networks in Private and Public IP environments

You can specify authorized networks both for Public IP and [Private IP](https://docs.cloud.google.com/composer/docs/composer-1/private-ip-environments) environments.

  * In Private IP environments you can configure authorized networks to allow a certain range of IP addresses to access the control plane of your environment's cluster. For example, to allow certain IP ranges to run `kubectl` and Airflow CLI commands. By default, in Private IP environments you can run these commands only from a VM in the VPC subnetwork of the Private IP environment.

  * In Public IP environments, you can configure authorized networks to restrict the range of IP addresses that can access the control plane of your environment's cluster. By default, in Public IP environments there are no restrictions on IP ranges that can run `kubectl` and Airflow CLI commands.




## Before you begin

  * You can specify authorized networks only using `gcloud`, Terraform, and REST API.

  * You can specify authorized networks when you [create an environment](https://docs.cloud.google.com/composer/docs/composer-1/create-environments), or for an existing environment.




## Create environments with authorized networks

###  gcloud 

To create an environment with authorized networks, use the `--enable-master-authorized-networks` argument when you create an environment. Then provide a comma-separated list of CIDR ranges in the `--master-authorized-networks` argument.

To specify authorized networks for a Private IP environment:
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --enable-ip-alias \
        --enable-private-environment \
        --enable-master-authorized-networks \
        --master-authorized-networks AUTHORIZED_NETWORKS_IP_RANGES
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `AUTHORIZED_NETWORKS_IP_RANGES` with a comma-separated list of IP address ranges in the CIDR notation. These ranges are added as authorized networks for your environment's cluster.



Example (Private IP environment):
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --enable-ip-alias \
        --enable-private-environment \
        --enable-privately-used-public-ips \
        --enable-master-authorized-networks \
        --master-authorized-networks 192.0.2.0/23,192.0.4.0/23
    

###  API 

Construct an [`environments.create`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. In the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, specify the configuration parameters for an environment with authorized networks.

To specify authorized networks for a Private IP environment:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "ENVIRONMENT_NAME",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
    
            "useIpAliases": true,
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
        },
        "masterAuthorizedNetworksConfig": {
          "enabled": true,
          "cidrBlocks": [
            {
              "displayName": "AUTHORIZED_NETWORK_NAME",
              "cidrBlock": "AUTHORIZED_NETWORK_RANGE"
            }
          ]
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `AUTHORIZED_NETWORK_NAME` with the name for the authorized network IP range. You use this name to identify this block. This field is optional.
  * `AUTHORIZED_NETWORK_RANGE` with an IP address range in the CIDR notation. This range is added as an authorized networks for your environment's cluster.
  * If you want to use several IP ranges, add extra ranges to `cidrBlocks`.



Example (Private IP environment):
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "example-environment",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
            "useIpAliases": true,
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
        },
        "masterAuthorizedNetworksConfig": {
          "enabled": true,
          "cidrBlocks": [
            {
              "displayName": "example_range_1",
              "cidrBlock": "192.0.2.0/23"
            },
            {
              "displayName": "example_range_2",
              "cidrBlock": "192.0.4.0/23"
            }
          ]
        }
      }
    }
    

###  Terraform 

When you create an environment, the `master_authorized_networks_config` block in the `config` block controls authorized networks for your environment.

To specify authorized networks for a Private IP environment:
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        node_config {
          ip_allocation_policy = [{
            use_ip_aliases = true
          }]
        }
        private_environment_config {
          // Private environment parameters
        }
    
        master_authorized_networks_config {
    
          enabled = true
    
          cidr_blocks {
              cidr_block = "AUTHORIZED_NETWORK_RANGE"
              display_name = "AUTHORIZED_NETWORK_NAME"
          }
    
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `AUTHORIZED_NETWORK_RANGE` with an IP address range in the CIDR notation. This range is added as an authorized networks for your environment's cluster.
  * `AUTHORIZED_NETWORK_NAME` with the name for the authorized network IP range. You use this name to identify this block.
  * If you want to use several IP ranges, add extra `cidr_blocks` blocks to to `master_authorized_networks_config`.



Example (Private IP environment):
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        node_config {
    
          // Specify your network and subnetwork
          network    = google_compute_network.example_network.id
          subnetwork = google_compute_subnetwork.example_subnet.id
    
          ip_allocation_policy = [{
            use_ip_aliases = true
          }]
        }
    
        private_environment_config {
          // Private environment parameters
        }
    
        master_authorized_networks_config {
    
          enabled = true
    
          cidr_blocks {
              cidr_block = "192.0.2.0/23"
              display_name = "example_range_1"
          }
    
          cidr_blocks {
              cidr_block = "192.0.4.0/23"
              display_name = "example_range_2"
          }
        }
      }
    }
    

## Specify authorized networks for an existing environment

You can specify authorized networks for an existing environment.

###  gcloud 

To specify authorized networks, use the `--enable-master-authorized-networks` argument. Then provide a comma-separated list of CIDR ranges in the `--master-authorized-networks` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --enable-master-authorized-networks \
      --master-authorized-networks AUTHORIZED_NETWORKS_IP_RANGES
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `AUTHORIZED_NETWORKS_IP_RANGES` with a comma-separated list of IP address ranges in the CIDR notation. These ranges are added as authorized networks for your environment's cluster.



Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --enable-master-authorized-networks \
      --master-authorized-networks 192.0.2.0/23,192.0.4.0/23
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.softwareConfig.masterAuthorizedNetworksConfig` mask.

     2. In the request body, specify CIDR ranges for authorized networks.



    
    
    "config": {
    
      "masterAuthorizedNetworksConfig": {
        "enabled": true,
        "cidrBlocks": [
          {
            "displayName": "AUTHORIZED_NETWORK_NAME",
            "cidrBlock": "AUTHORIZED_NETWORK_RANGE"
          }
        ]
      }
    }
    

Replace:

  * `AUTHORIZED_NETWORK_NAME` with the name for the authorized network IP range. You use this name to identify this block. This field is optional.
  * `AUTHORIZED_NETWORK_RANGE` with an IP address range in the CIDR notation. This range is added as an authorized network for your environment's cluster.
  * If you want to use several IP ranges, add extra ranges to `cidrBlocks`.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.masterAuthorizedNetworksConfig
    
    "config": {
      "masterAuthorizedNetworksConfig": {
        "enabled": true,
        "cidrBlocks": [
          {
            "displayName": "example_range_1",
            "cidrBlock": "192.0.2.0/23"
          },
          {
            "displayName": "example_range_2",
            "cidrBlock": "192.0.4.0/23"
          }
        ]
      }
    }
    

###  Terraform 

The `master_authorized_networks_config` block in the `config` block controls authorized networks for your environment.

To add authorized networks for a Private IP environment, add this block to your environment definition:
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example_environment"
      region = "us-central1"
    
      config {
    
        // Other environment parameters
    
        master_authorized_networks_config {
    
          enabled = true
    
          cidr_blocks {
              cidr_block = "AUTHORIZED_NETWORK_RANGE"
              display_name = "AUTHORIZED_NETWORK_NAME"
          }
    
        }
      }
    }
    

Replace:

  * `AUTHORIZED_NETWORK_RANGE` with an IP address range in the CIDR notation. This range is added as an authorized networks for your environment's cluster.
  * `AUTHORIZED_NETWORK_NAME` with the name for the authorized network IP range. You use this name to identify this block.
  * If you want to use several IP ranges, add extra `cidr_blocks` blocks to to `master_authorized_networks_config`.



Example:
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        // Other environment parameters
    
        master_authorized_networks_config {
    
          enabled = true
    
          cidr_blocks {
              cidr_block = "192.0.2.0/23"
              display_name = "example_range_1"
          }
    
          cidr_blocks {
              cidr_block = "192.0.4.0/23"
              display_name = "example_range_2"
          }
        }
      }
    }
    

## Disable authorized networks

You can disable authorized networks for an existing environment:

  * For Private IP environments, this removes access for ranges that were previously added as authorized network.
  * For Public IP environments, this removes previously configured restrictions.




###  gcloud 

To disable authorized networks, use the `--disable-master-authorized-networks` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --disable-master-authorized-networks
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --disable-master-authorized-networks
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.softwareConfig.masterAuthorizedNetworksConfig` mask.

     2. In the request body, specify `false` in the `enabled` field.



    
    
    "config": {
    
      "masterAuthorizedNetworksConfig": {
        "enabled": false
      }
    }
    

Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.masterAuthorizedNetworksConfig
    
    "config": {
      "masterAuthorizedNetworksConfig": {
        "enabled": false,
      }
    }
    

###  Terraform 

The `master_authorized_networks_config` block in the `config` block controls authorized networks for your environment.

To disable authorized networks, set the `enabled` field in the `master_authorized_networks_config` block to `false`.

Example:
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example_environment"
      region = "us-central1"
    
      config {
    
        // Other environment parameters
    
        master_authorized_networks_config {
          enabled = false
        }
      }
    }
    

## What's next

  * [Configuring Private IP environments](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip)
  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [About Private IP environments](https://docs.cloud.google.com/composer/docs/composer-1/private-ip-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
