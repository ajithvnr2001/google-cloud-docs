---
url: https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect/
title: Configure Private Service Connect in Managed Airflow \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:33.954210+00:00
---

# Configure Private Service Connect in Managed Airflow  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Configure Private Service Connect in Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page explains how to create a [Private IP](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments) environment that uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) instead of VPC peerings.

For general information about creating Private IP environments, see [Configure a private IP environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip).

## About Private Service Connect in Managed Airflow

Components of your environment are distributed between [the tenant and the customer project](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture#about-customer-tenant). In [Private IP](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments) environments, the components located in these two projects connect using [VPC peerings](https://docs.cloud.google.com/vpc/docs/vpc-peering). VPC peerings have some limitations, including the limit on the maximum number of peerings in a VPC. These limits can become more evident if you use large-scale networks with Managed Airflow environments.

With **Private Service Connect support in Managed Airflow** , your private IP environments communicate internally without the use of VPC peerings. Such environments use the [Private IP with PSC architecture](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture#private-ip-psc).

## Before you begin

  * Private Service Connect support is available only in Managed Airflow (Gen 2).

  * You can only enable Private Service Connect when you create a new environment. It is not possible to switch an existing environment to use Private Service Connect.

  * Your environment must be a [Private IP](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments) environment. Because VPC peerings are not used, you do not need to specify the CIDR ranges for the Cloud SQL instance and the internal Managed Airflow network.

  * If the **Disable Private Service Connect for Consumers** [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) denies SERVICE_PRODUCER endpoints, it is not possible to create environments with Private Service Connect. This policy does not affect existing Managed Airflow environments with Private Service Connect. Such environments can operate when this policy is enabled.


**Caution:** If you create a new subnet for the Managed Airflow connection subnetwork, use the `PRIVATE` [subnet purpose](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--purpose) for it. Do not use the `PRIVATE_SERVICE_CONNECT` purpose. Subnets reserved for Private Service Connect Services cannot be used for the Managed Airflow connection subnetwork.

## Enable Private Service Connect when you create an environment

###  Console 

To create an environment with Private Service Connect, select the **Private Service Connect** connectivity type when you create a Private IP environment. Then specify the subnetwork for the Private Service Connect connection.

When you create a Private IP environment:

  1. In the **Network configuration** section, expand the **Show network configuration** item.

  2. In the **Networking type** section, select the **Private IP environment** option to create a Private IP environment.

  3. In the **Composer connectivity** section, select **Private Service Connect**.

  4. In the **Composer connection subnetwork** drop-down list, select the subnetwork for Private Service Connect endpoints.

You can use your environment's subnetwork.

As an alternative, you can specify a different subnetwork. Doing so gives you more control over the CIDR range from which the IP address for the PSC endpoint are selected.This range can be shared by multiple Managed Airflow environments. Each environment requires one IP address. 

  5. Specify other parameters for your Private IP environment.




###  gcloud 

To create an environment with Private Service Connect, use the `--connection-subnetwork` argument when you create a Private IP environment. Then specify the subnetwork for the Private Service Connect connection.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --web-server-allow-all \
        --connection-subnetwork ENVIRONMENT_PSC_SUBNETWORK
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `ENVIRONMENT_PSC_SUBNETWORK` with the URI of the subnetwork for Private Service Connect endpoints.

You can use [your environment's subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork).

As an alternative, you can specify a different subnetwork. Doing so gives you more control over the CIDR range from which the IP address for the PSC endpoint are selected. This range can be shared by multiple Managed Airflow environments. Each environment requires one IP address. 




Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-private-environment \
        --web-server-allow-all \
        --connection-subnetwork "projects/example-project/regions/us-central1/subnetworks/default"
    

###  API 

Construct an [`environments.create`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. In the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, specify the configuration parameters for the Private Service Connect connection.
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "ENVIRONMENT_NAME",
    
      "config": {
        "softwareConfig": {
          "imageVersion": "composer-2.17.15-airflow-2.11.1"
        },
        "nodeConfig": {
          "network": "ENVIRONMENT_NETWORK",
          "subnetwork": "ENVIRONMENT_SUBNETWORK"
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "privateClusterConfig": {
            "enablePrivateEndpoint": false
          },
          "cloudComposerConnectionSubnetwork": "ENVIRONMENT_PSC_SUBNETWORK"
        }
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "0.0.0.0/0",
              "description": "Allows access from all IPv4 addresses"
            },
            {
              "value": "::0/0",
              "description": "Allows access from all IPv6 addresses"
            }
          ]
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `ENVIRONMENT_NETWORK` with the URI of your environment's network.
  * `ENVIRONMENT_SUBNETWORK` with the URI of your environment's subnetwork.
  * `ENVIRONMENT_PSC_SUBNETWORK` with the URI of the subnetwork for PSC endpoints.

You can use [your environment's subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork).

As an alternative, you can specify a different subnetwork. Doing so gives you more control over the CIDR range from which the IP address for the PSC endpoint is selected. This range can be shared by multiple Managed Airflow environments. Each environment requires one IP address. 




Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "example-environment",
      "config": {
    
        "softwareConfig": {
          "imageVersion": "composer-2.17.15-airflow-2.11.1"
        },
        "nodeConfig": {
          "network": "projects/example-project/global/networks/default",
          "subnetwork": "projects/example-project/regions/us-central1/subnetworks/default"
        },
        "privateEnvironmentConfig": {
          "enablePrivateEnvironment": true,
          "privateClusterConfig": {
            "enablePrivateEndpoint": false
          },
          "cloudComposerConnectionSubnetwork": "projects/example-project/regions/us-central1/subnetworks/default"
        }
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "0.0.0.0/0",
              "description": "Allows access from all IPv4 addresses"
            },
            {
              "value": "::0/0",
              "description": "Allows access from all IPv6 addresses"
            }
          ]
        }
      }
    }
    

###  Terraform 

When you create an environment, the `cloud_composer_connection_subnetwork` field in the `private_environment_config` block enables Private Service Connect.
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        software_config {
          image_version = "composer-2.17.15-airflow-2.11.1"
        }
    
        node_config {
          network = "ENVIRONMENT_NETWORK"
          subnetwork = "ENVIRONMENT_SUBNETWORK"
    
        }
    
        private_environment_config {
          // Other private IP environment parameters
          cloud_composer_connection_subnetwork = "ENVIRONMENT_PSC_SUBNETWORK"
        }
    
        web_server_network_access_control  {
          allowed_ip_range {
            value = "0.0.0.0/0"
            description = "Allows access from all IPv4 addresses"
          }
    
          allowed_ip_range {
            value = "::0/0"
            description = "Allows access from all IPv6 addresses"
          }
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `ENVIRONMENT_NETWORK` with the URI of your environment's network.
  * `ENVIRONMENT_SUBNETWORK` with the URI of your environment's subnetwork.
  * `ENVIRONMENT_PSC_SUBNETWORK` with the URI of the subnetwork for PSC endpoints.

You can use [your environment's subnetwork](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create#--subnetwork).

As an alternative, you can specify a different subnetwork. Doing so gives you more control over the CIDR range from which the IP address for the PSC endpoint is selected. This range can be shared by multiple Managed Airflow environments. Each environment requires one IP address. 




Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        environment_size = "ENVIRONMENT_SIZE_SMALL"
    
        software_config {
          image_version = "composer-2.17.15-airflow-2.11.1"
        }
    
        node_config {
          network = "projects/example-project/global/networks/default"
          subnetwork = "projects/example-project/regions/us-central1/subnetworks/default"
        }
    
        private_environment_config {
          // Other private IP environment parameters
          enable_private_endpoint = "true"
          cloud_composer_connection_subnetwork = "projects/example-project/regions/us-central1/subnetworks/default"
        }
    
        web_server_network_access_control  {
          allowed_ip_range {
            value = "0.0.0.0/0"
            description = "Allows access from all IPv4 addresses"
          }
    
          allowed_ip_range {
            value = "::0/0"
            description = "Allows access from all IPv6 addresses"
          }
        }
     }
    }
    

## What's next

  * [Configuring Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip)
  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture)
  * [About Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
