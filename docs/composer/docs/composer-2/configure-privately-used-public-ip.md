---
url: https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip/
title: Configure privately used public IP ranges \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:09.666232+00:00
---

# Configure privately used public IP ranges  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Configure privately used public IP ranges Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/configure-privately-used-public-ip "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to use [privately used public IP](https://docs.cloud.google.com/architecture/configuring-privately-used-public-ips-for-GKE) ranges in your [Private IP](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments) environment. For general information about creating Private IP environments, see [Configure a private IP environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip).

## About privately used public IP ranges in Managed Airflow

Google Kubernetes Engine requires many IP addresses for its resources: each node, pod, and service must have a unique IP address. This can lead to a situation where existing private IP ranges cannot accommodate enough IP addresses.

Managed Airflow environments can use some IP ranges from [non-RFC 1918 address space](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) without additional configuration.

If you want to use more IP addresses, your environment can privately use certain public IP address ranges as internal, subnet IP address ranges for pods and services. Such ranges are called _privately used public IP (PUPI) ranges_.

You can privately use any public IP address except for [certain restricted ranges](https://docs.cloud.google.com/vpc/docs/subnets#restricted-ranges).

## Before you begin

  * You can only specify public IP ranges when you create a new environment. It is not possible to change IP ranges of an existing environment.

  * Your environment must be a [Private IP](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments) environment.

  * You can create environments with PUPI ranges only using `gcloud`, Terraform, and REST API.

  * Only GKE pods and services can use public IP ranges. Other environment components such as Cloud SQL, web server, and [GKE control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) cannot use public IP ranges in a private IP environment.

  * GKE cluster is created with [default SNAT](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#how_ipmasq_works) disabled.




## Enable PUPI ranges when you create an environment

###  gcloud 

To create an environment with PUPI ranges, use the `--enable-privately-used-public-ips` argument when you create a Private IP environment. Then specify public IP ranges for pods and services.

**Subnet ranges managed by GKE**

To create subnet ranges [managed by GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#managed_by_default):
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --enable-privately-used-public-ips \
        --cluster-ipv4-cidr POD_IP_RANGE \
        --services-ipv4-cidr SERVICES_IP_RANGE
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `POD_IP_RANGE` with an IP address range in the CIDR notation. This range is added as a secondary IP address range to the [subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork) of your environment and is used as the IP address range for pods.
  * `SERVICES_IP_RANGE` with an IP address range in the CIDR notation. This range is the secondary IP address range for services in the [subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork) of your environment.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --enable-privately-used-public-ips \
        --cluster-ipv4-cidr 10.3.192.0/20 \
        --services-ipv4-cidr 172.16.194.0/23
    

**User-managed subnet ranges**

To create [user-managed ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#user-managed):
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --enable-privately-used-public-ips \
        --cluster-secondary-range-name POD_IP_RANGE_NAME \
        --services-secondary-range-name SERVICES_IP_RANGE_NAME
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `POD_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork). This range is used by pods.
  * `SERVICES_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork). This range is used by services.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --enable-privately-used-public-ips \
        --cluster-secondary-range-name "public-1" \
        --services-secondary-range-name "public-2"
    

###  API 

Construct an [`environments.create`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. In the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, specify the configuration parameters for an environment with PUPI ranges.

**Subnet ranges managed by GKE**

To create subnet ranges [managed by GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#managed_by_default):
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "ENVIRONMENT_NAME",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
            "clusterIpv4CidrBlock":"POD_IP_RANGE",
            "servicesIpv4CidrBlock":"SERVICES_IP_RANGE"
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "enablePrivatelyUsedPublicIps": true
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `POD_IP_RANGE` with an IP address range in the CIDR notation. This range is added as a secondary IP address range to the [subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork) of your environment and is used as the IP address range for pods.
  * `SERVICES_IP_RANGE` with an IP address range in the CIDR notation. This range is the secondary IP address range for services in the [subnetwork](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#NodeConfig) of your environment.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "example-environment",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
            "clusterIpv4CidrBlock":"10.3.192.0/20",
            "servicesIpv4CidrBlock":"172.16.194.0/23"
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "enablePrivatelyUsedPublicIps": true
        }
      }
    }
    

**User-managed subnet ranges**

To create [user-managed ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#user-managed):
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "ENVIRONMENT_NAME",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
            "clusterSecondaryRangeName":"POD_IP_RANGE",
            "servicesSecondaryRangeName": "SERVICES_IP_RANGE"
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "enablePrivatelyUsedPublicIps": true
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `POD_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#NodeConfig). This range is used by pods.
  * `SERVICES_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#NodeConfig). This range is used by services.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "example-environment",
      "config": {
        "nodeConfig": {
          "ipAllocationPolicy": {
            "clusterSecondaryRangeName":"public-1",
            "servicesSecondaryRangeName": "public-2"
          }
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "enablePrivatelyUsedPublicIps": true
        }
      }
    }
    

###  Terraform 

When you create an environment, the `enable_privately_used_public_ips` field in the `private_environment_config` block enables the use of PUPI ranges. You must also specify PUPI ranges for pods and services.

**Subnet ranges managed by GKE**

To create subnet ranges [managed by GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#managed_by_default):
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
    
          ip_allocation_policy = [{
            
            cluster_ipv4_cidr_block = "POD_IP_RANGE"
            services_ipv4_cidr_block = "SERVICES_IP_RANGE"
            cluster_secondary_range_name = null
            services_secondary_range_name = null
          }]
        }
    
        private_environment_config {
          enable_privately_used_public_ips = true
          // Other private ip environment parameters
        }
    
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `POD_IP_RANGE` with an IP address range in the CIDR notation. This range is added as a secondary IP address range to the [subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork) of your environment and is used as the IP address range for pods.
  * `SERVICES_IP_RANGE` with an IP address range in the CIDR notation. This range is the secondary IP address range for services in the [subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork) of your environment.



Example:
    
    
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
            
            // Specify PUPI addresses
            cluster_ipv4_cidr_block = "10.3.192.0/20"
            services_ipv4_cidr_block = "172.16.194.0/23"
            cluster_secondary_range_name = null
            services_secondary_range_name = null
          }]
        }
    
        private_environment_config {
          enable_privately_used_public_ips = true
          // Other private environment parameters
        }
    
      }
    }
    

**User-managed subnet ranges**

To create [user-managed ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#user-managed):
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
    
          ip_allocation_policy = [{
            
            cluster_ipv4_cidr_block = null
            services_ipv4_cidr_block = null
            cluster_secondary_range_name = POD_IP_RANGE_NAME
            services_secondary_range_name = SERVICES_IP_RANGE_NAME
          }]
        }
    
        private_environment_config {
          enable_privately_used_public_ips = true
          // Other private ip environment parameters
        }
    
      }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `POD_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork). This range is used by pods.
  * `SERVICES_IP_RANGE_NAME` with the name of an existing secondary IP address range in the [specified subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork). This range is used by services.



Example:
    
    
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
            
            cluster_ipv4_cidr_block = null
            services_ipv4_cidr_block = null
            // Specify existing ranges
            cluster_secondary_range_name = "public-1"
            services_secondary_range_name = "public-2"
          }]
        }
        private_environment_config {
          enable_privately_used_public_ips = true
          // Other private environment parameters
        }
    
      }
    }
    

## What's next

  * [Configuring Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip)
  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [About Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
