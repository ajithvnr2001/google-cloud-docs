---
url: https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent/
title: Enable the IP Masquerade agent in Managed Airflow environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:55.315504+00:00
---

# Enable the IP Masquerade agent in Managed Airflow environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Enable the IP Masquerade agent in Managed Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/enable-ip-masquerade-agent "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to enable the IP Masquerade agent for your environment.

**Important:** Consider using the IP Masquerade agent if your project is impacted by the shortage of IP addresses. By enabling the IP Masquerade agent, you can use your environment's cluster IP addresses to communicate with external services.

## About the IP Masquerade agent in Managed Airflow

Managed Airflow supports the [IP Masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) for your environments.

_IP masquerading_ is a form of network address translation (NAT) used to perform many-to-one IP address translations. This allows multiple clients to access a destination from a single IP address.

Managed Airflow runs your workloads on GKE. For correct function, it requires IP ranges for nodes (VMs) as well as GKE Pods and Services. When Airflow DAGs and tasks communicate with other services, they use Pod IPs and these Pod IP ranges need to be routable to and from any destinations that the tasks interact with.

With the IP Masquerade agent, you have the option to translate Pod IP addresses to node IP addresses, so that destinations and services targeted from Airflow DAGs and tasks only receive packets from node IP addresses instead of Pod IP addresses. This is useful in environments that expect to only receive packets from node IP addresses or where Pod IP ranges are not routable outside of the cluster.

In addition, you can use the IP Masquerade agent to save network ranges in your networking configuration. For example, you can use a separate network range for Pods inside your environment's cluster and masquerade this traffic as coming from the node IP address range. In this way, you save IP address space in one range by using IP addresses from a different range for Pods in your environment's cluster.

For example:

  1. You use the `10.0.0.0/8` range for VMs and only this range is allowed by your firewall rules.

  2. To save network ranges, you use a different range (for example, `192.168.0.0/16`) for Pods in your environment's cluster.

  3. To be able to connect to any service from a Pod (Airflow worker), IP masquerading is needed; otherwise the service receives traffic from `192.168.0.0/16` and drops it because of a firewall rule. With the IP Masquerade agent enabled and configured, the service gets requests from `10.0.0.0/8`, which are accepted.




## Before you begin

  * It is not possible to enable the IP Masquerade agent in Google Cloud console.

  * To use this feature, you must create an environment with GKE 1.22.7 or later version.

  * The IP Masquerade agent is not available for environments that were created in earlier GKE versions, even if GKE was upgraded to 1.22.7 and later versions.

  * If you enable the IP Masquerade agent, the default [GKE's EgressNatPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot) will be replaced with Managed Airflow's definition. If the IP Masquerade agent is not enabled, the outgoing traffic won't be masqueraded and will use the default GKE's EgressNatPolicy.




## Enable the IP Masquerade agent for an existing environment

It is not possible to enable the IP Masquerade agent for an existing environment.

## Enable the IP Masquerade agent when creating an environment

You can enable the IP Masquerade agent when you create an environment.

For more information about creating Managed Airflow environments, see [Create environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments).

###  Console 

It is not possible to enable the IP Masquerade agent in Google Cloud console.

###  gcloud 

When you create an environment, the `--enable-ip-masq-agent` argument enables the IP Masqerade agent. 
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-ip-masq-agent
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.15-airflow-2.11.1 \
        --enable-ip-masq-agent
    

###  API 

Construct an [`environments.create`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. Specify the configuration in the [`Environment`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "softwareConfig": {
          "imageVersion": "composer-2.17.15-airflow-2.11.1"
        },
        "nodeConfig": {
          "enableIpMasqAgent": true
        }
      }
    }
    

Replace:

  * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `LOCATION` with the region where the environment is located.
  * `ENVIRONMENT_NAME` with the environment name.



Example:
    
    
      // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
      {
        "name": "projects/example-project/locations/us-central1/environments/example-environment",
        "config": {
          "softwareConfig": {
            "imageVersion": "composer-2.17.15-airflow-2.11.1"
          },
          "nodeConfig": {
            "enableIpMasqAgent": true
          }
        }
      }
    

###  Terraform 

When you create an environment, the `enable_ip_masq_agent` field in the `node_config` block enables the IP Masqerade agent. 
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        software_config {
          image_version = "composer-2.17.15-airflow-2.11.1"
        }
        node_config {
          enable_ip_masq_agent = true
        }
      }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        software_config {
          image_version = "composer-2.17.15-airflow-2.11.1"
        }
        node_config {
          enable_ip_masq_agent = true
        }
      }
    }
    

## Configure the IP Masquerade agent

**Caution:** Managed Airflow enables [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) on GKE clusters. Therefore, non-masquerade destinations must at least include the cluster's node and Pod IP address range(s).

For more information about using and configuring the IP Masquerade agent in Managed Airflow (Gen 2), see [Use Egress NAT Policy to configure IP masquerade in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).

## What's next

  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Configure Shared VPC networking](https://docs.cloud.google.com/composer/docs/composer-2/configure-shared-vpc)
  * [Configure Private IP networking](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
