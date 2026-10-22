---
url: https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network/
title: Connect an environment to a VPC network \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:38.539876+00:00
---

# Connect an environment to a VPC network  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Connect an environment to a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page explains how your environment can access a VPC network in Managed Airflow (Gen 3), provides instructions for connecting an environment to a VPC network, and describes how to disable a previously configured connection.

  * If you want to enable or disable internet access for your environment's Airflow components, see [Change environment networking type (Private or Public IP)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type).

  * If you want to disable or enable internet access only when installing PyPI packages, see [Configure internet access when installing PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access).

  * If you want to configure Shared VPC networking, see [Configure Shared VPC](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc) for information about configuring projects and permissions.




## About VPC network access

In Managed Airflow (Gen 3), you can enable access to a VPC network for an environment.

If you enable access to a VPC network for an environment:

  * Airflow components of your environment **can access private network endpoints** in your VPC network. For example, your DAG code can access resources located in your VPC network through a configured [Airflow connection](https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections).

  * If your environment uses [Private IP networking](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type), **all traffic is routed to your VPC network** , except the traffic to Google APIs, services, and domains that [are available to Private IP environments](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#about-networking-type) through Private Google Access. This method also lets your Airflow components connect to [Privately Used Public IPs (PUPI)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configuring-privately-used-public-ips-for-gke) configured in GKE, as the traffic will be routed through the VPC network instead of being sent to the public internet.

  * Depending on how you configure your VPC network, a Private IP environment **can gain access to the internet through you VPC network**.

  * [Private DNS Zones](https://docs.cloud.google.com/dns/docs/dns-overview#private_zone) defined in your VPC network are automatically available to your environment's Airflow components.

**Note:** Managed Airflow (Gen 3) doesn't support a user-defined [`.internal` DNS zone](https://docs.cloud.google.com/compute/docs/internal-dns). If you create a DNS zone for `.internal`, it won't be possible to reach that zone.
  * The environment reserves two IP addresses in your VPC subnetwork and uses two extra IP addresses during maintenance and upgrades. Make sure that **four IP addresses per environment** are available in your VPC subnetwork.




Managed Airflow uses a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) to connect your environment to a VPC network:

  * If you specify a VPC network and subnetwork, then Managed Airflow creates a new network attachment in your project. This attachment is deleted after you [delete an environment](https://docs.cloud.google.com/composer/docs/composer-3/delete-environments), disable connection to a VPC network, or overwrite the VPC connection parameters.

  * If you specify an [existing network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments), then it must be located in the same project with the environment. This attachment is not deleted after you delete an environment, disable connection, or overwrite the VPC connection parameters.

  * In Shared VPC networking:

    * Make sure that you configured Shared VPC networking for Managed Airflow. See [Configure Shared VPC](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc) for information about configuring projects and permissions for Managed Airflow.

    * After Shared VPC networking is configured, you can connect your environment to a VPC network from the host project. If you use an existing network attachment, it must be created in the service project (where the environment is located), and attached to a Shared VPC network.




## Limitations for transitive DNS peering in Managed Airflow (Gen 3)

[Limitations for transitive DNS peering](https://docs.cloud.google.com/dns/docs/zones/zones-overview#dns_peering_limitations_and_key_points) apply to a Managed Airflow (Gen 3) environment in the following way:

  * Cloud DNS has a limitation of one transitive hop, which means that only two hops are supported in total.
  * In Managed Airflow (Gen 3), your environment's components run in the [tenant project](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture) and communicate with the project where the environment is located through a DNS peering. The transitive hop is used by the DNS peering of the tenant project, so it's possible to use only one hop in total.



As a workaround, you can create a DNS peering zone in the project where the environment is located to act as a shortcut. For more information, see [When to use peering instead](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding-peering-example) in the Cloud DNS documentation.

## About the environment's internal IP range

Managed Airflow (Gen 3) environments require several IP addresses for its components that run in the [tenant project](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture), such as your environment's cluster and Cloud SQL proxy. These IP addresses are taken from the _environment's internal IP range_.

  * The default internal IP range is `100.64.128.0/20`.

  * You can specify a different internal IP range when you create an environment. This range must use a `/20` mask.

  * You cannot change the internal IP range of an existing environment.




The internal IP range interacts with your VPC network in the following ways:

  * The internal IP range must not conflict with the VPC subnetwork that the Managed Airflow environment is connected to. It's not possible to enable a connection with a VPC subnetwork that overlaps with the internal IP range.

  * If the internal IP range of an environment overlaps with your VPC network ranges, then **endpoints from your VPC network that have overlapping IP addresses are not accessible from the environment**.

For example, if the internal range is `100.64.128.0/20` then any request to the `100.64.128.1` endpoint in your VPC network fails because the request does not leave the tenant project.

  * The internal IP range is not reserved. You can use the same internal IP range for several environments without any additional setup because the internal VPC networks used by different environments are separated.

  * You can use the internal range IP addresses for other purposes, as long as DAGs and tasks in your environment do not make requests to them.




## Connect to a VPC network

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Network configuration** section, find the **Network attachment** item and click **Edit**.

  5. In the **Network attachment** dialog:

     * To create a new network attachment, in the **Network attachment** list, select **Create a new network attachment**. In the **Network** and **Subnetwork** lists, select a VPC network and a subnetwork.

     * To use an existing network attachment, in the **Network attachment** list, select an attachment.

  6. Click **Save**.




###  gcloud 

The following Google Cloud CLI arguments specify VPC network connection parameters:

  * `--network`: VPC network ID.
  * `--subnetwork`: VPC subnetwork ID.
  * `--network-attachment`: Use an existing network attachment instead.



**New network attachment**

To connect your environment to a VPC network through a new network attachment, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --network NETWORK_ID \
      --subnetwork SUBNETWORK_ID
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located
  * `NETWORK_ID`: VPC network ID
  * `SUBNETWORK_ID`: VPC subnetwork ID



Example:
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --network projects/example-project/global/networks/example-network \
      --subnetwork projects/example-project/regions/us-central1/subnetworks/example-subnetwork
    

**Existing network attachment**

To connect your environment to a VPC network through a new network attachment, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --network-attachment NETWORK_ATTACHMENT_ID
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located
  * `NETWORK_ATTACHMENT_ID`: the network attachment in the `projects/{project}/regions/{region}/networkAttachments/{networkAttachment}` format. 



Example:
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --network-attachment projects/example-project/regions/us-central1/networkAttachments/example-network-attachment
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     * To create a new network attachment:

       1. In the `updateMask` parameter, specify the `config.node_config.network,config.node_config.subnetwork` mask.

       2. In the request body, in the `network` and `subnetwork` fields, specify your VPC network and subnetwork IDs.

     * To use an existing network attachment:

       1. In the `updateMask` parameter, specify the `config.node_config.composer_network_attachment` mask. 

       2. In the request body, provide a value for the existing network attachment in the `projects/{project}/regions/{region}/networkAttachments/{networkAttachment}` format.




Example (new network attachment):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.node_config.network,config.node_config.subnetwork
    
    "config": {
      "nodeConfig": {
        "network": "projects/example-project/global/networks/example-network",
        "subnetwork": "projects/example-project/regions/us-central1/subnetworks/example-subnetwork"
      }
    }
    

Example (existing network attachment):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.node_config.composer_network_attachment
    
    "config": {
      "nodeConfig": {
        "composerNetworkAttachment": "projects/example-project/regions/us-central1/networkAttachments/example-network-attachment"
      }
    }
    

###  Terraform 

The following fields in the `node_config` block specify VPC network connection parameters:

  * `network`: VPC network ID.
  * `subnetwork`: VPC subnetwork ID.
  * `composer_network_attachment`: Use an existing network attachment instead.



**New network attachment**
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
          network = NETWORK_ID
          subnetwork = SUBNETWORK_ID
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `NETWORK_ID`: VPC network ID
  * `SUBNETWORK_ID`: VPC subnetwork ID



Example (new network attachment):
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        node_config {
          network = "projects/example-project/global/networks/example-network"
          subnetwork = "projects/example-project/regions/us-central1/subnetworks/example-subnetwork"
        }
    
        ... other configuration parameters
      }
    }
    

**Existing network attachment**

**Caution:** If you specify an existing network attachment that you also manage in Terraform, then **Terraform will revert changes to the attachment** done by Managed Airflow when you apply configuration changes.

As a result, the environment will no longer use the attachment. To address this, make sure that Terraform ignores changes to the `producer_accept_lists` parameter of the attachment, as follows:
    
    
    resource "google_compute_network_attachment" "NETWORK_ATTACHMENT_ID" {
      lifecycle {
        ignore_changes = [producer_accept_lists]
      }
      # ... other configuration parameters
    }
    

Afterwards, specify this attachment for an environment. You can also specify an attachment that is not managed in Terraform, see the example.
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
      config {
        node_config {
          composer_network_attachment = google_compute_network_attachment.NETWORK_ATTACHMENT_ID.id
        }
        # ... other configuration parameters
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `NETWORK_ATTACHMENT_ID`: the network attachment ID.



Example (existing network attachment):
    
    
    resource "google_compute_network_attachment" "example" {
      lifecycle {
        ignore_changes = [producer_accept_lists]
      }
      # ... other configuration parameters
    }
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        node_config {
          # Attachment is managed in Terraform:
    
          composer_network_attachment = google_compute_network_attachment.NETWORK_ATTACHMENT_ID.id
    
          # Attachment is not managed in Terraform:
    
          # composer_network_attachment = projects/example-project/regions/us-central1/networkAttachments/example-network-attachment
        }
        # ... other configuration parameters
      }
    }
    

## Disable connection to a VPC network

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Network configuration** section, find the **Network attachment** item and click **Edit**.

  5. In the **Network attachment** dialog, select **None** and click **Save**.




###  gcloud 

The `--disable-vpc-connectivity` argument disables the VPC network connection of your environment:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --disable-vpc-connectivity
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located



Example:
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --disable-vpc-connectivity
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.node_config.network,config.node_config.subnetwork` mask.

     2. In the request body, in the `network` and `subnetwork` fields, specify empty values.




Example:
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.node_config.network,config.node_config.subnetwork
    
    "config": {
      "nodeConfig": {
        "network": "",
        "subnetwork": ""
      }
    }
    

###  Terraform 

It's not possible to detach a VPC network using Terraform. Instead, you can attach a different VPC network in its place, or detach the network using other tools like Google Cloud CLI.

## Routing Cloud Run traffic through the network attachment

If you [restrict ingress to internal endpoints](https://docs.cloud.google.com/run/docs/securing/ingress) for your Cloud Run service, you cannot access this endpoint from a Managed Airflow environment. The access is restricted because Airflow workers in the [tenant project](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture) of the environment don't belong to the same VPC network as the environment.

As an option, you can route traffic to the function's endpoint through the network attachment instead of the default route to Google APIs, thus enabling access.

After the change, traffic to the following two domains is routed through the network attachment of your environment:

  * `.run.app`
  * `.cloudfunctions.net`



If your app uses custom domains and you use a Private IP environment with a connected VPC network, then traffic to non-Google addresses already goes through the environment's network attachment by default.

The following restrictions apply to an environment where the connectivity is configured in this way:

  * The environment must use Private IP networking. If your environment uses Public IP, you can [change its networking type](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type).
  * It's not possible to disconnect an environment from a VPC network. To disconnect, you must revert to the default traffic routing first.



To configure traffic routing to Cloud Run:

###  gcloud 

Use the `--cloud-run-functions-routing` argument when creating or updating the environment:

  * (Default) `direct`: Route traffic to Cloud Run in the same way as to other Google APIs and services.
  * `via-network-attachment`: Route traffic to Cloud Run through the environment's network attachment.



You can use this argument in the same operation with connecting the VPC network.

To enable routing through the environment's network attachment, run the following command in gcloud CLI:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --cloud-run-functions-routing via-network-attachment
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located



Example:
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --cloud-run-functions-routing via-network-attachment
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `node_config.TrafficRoutingConfig` mask.

     2. In the request body, in the `cloud_run_functions_routing` field, specify how traffic to Cloud Run must be routed:

        * (Default) `DIRECT`: Route traffic to Cloud Run in the same way as to other Google APIs and services.
        * `VIA_NETWORK_ATTACHMENT`: Route traffic to Cloud Run through the environment's network attachment.



You can use this argument in the same operation with connecting the VPC network.

Example:
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.node_config.TrafficRoutingConfig
    
    {
      "config": {
        "nodeConfig": {
          "trafficRoutingConfig": {
            "cloudRunFunctionsRouting": "VIA_NETWORK_ATTACHMENT"
          }
        }
      }
    }
    

###  Terraform 

The `cloud_run_functions_routing` field in the `config.node_config.traffic_routing_config` block determines how traffic to Cloud Run must be routed:

  * (Default) `DIRECT`: Route traffic to Cloud Run in the same way as to other Google APIs and services.
  * `VIA_NETWORK_ATTACHMENT`: Route traffic to Cloud Run through the environment's network attachment.



To use the `VIA_NETWORK_ATTACHMENT` option, configure the following:

  * Configure the environment to use [Private IP configuration](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type) by setting `enable_private_environment` to `true`.
  * Configure VPC connectivity by specifying either the `network` and `subnetwork` fields, or an existing network attachment in the `composer_network_attachment` field.



Example:
    
    
    resource "google_composer_environment" "example" {
      name   = "..."
      region = "us-central1"
      config {
        node_config {
          network    = "..."
          subnetwork = "..."
          traffic_routing_config {
            cloud_run_functions_routing = "VIA_NETWORK_ATTACHMENT"
          }
        }
        software_config {
          image_version = "composer-3-airflow-2"
        }
        enable_private_environment = true
      }
    }
    

## What's next

  * [Change environment networking type (Private or Public IP)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type)
  * [Configure internet access when installing PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
