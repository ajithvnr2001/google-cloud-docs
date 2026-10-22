---
url: https://docs.cloud.google.com/memorystore/docs/cluster/create-instance-terraform/
title: Quickstart: Create a Memorystore for Redis instance by using Terraform \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:31.362829+00:00
---

# Quickstart: Create a Memorystore for Redis instance by using Terraform  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/create-instance-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Memorystore for Redis Cluster instance using Terraform

This quickstart shows you how to use Terraform to create a new Memorystore for Redis Cluster instance. It also shows you how to connect to the instance using telnet. 

This quickstart assumes you are starting a new Terraform file, and includes the Terraform resource for setting up the Google Cloud provider. However, it omits the steps for authenticating your Terraform file with the Google Cloud provider.

For instructions on authenticating Terraform with the Google Cloud provider, see [Getting started with the Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. If you haven't already, [install the Google Cloud SDK](https://docs.cloud.google.com/sdk/docs). 

When prompted, choose the project that you selected or created above.

  7. If you already have the Google Cloud SDK installed, update it.
         
         gcloud components update

  8. Enable the Memorystore for Redis Cluster API   
[Memorystore for Redis Cluster](https://console.cloud.google.com/apis/library/redis.googleapis.com)



## Configure Terraform for Memorystore

This section shows examples of five Terraform resources needed to create a Memorystore for Redis Cluster instance:

  * The Google Cloud provider configuration.

  * A Memorystore instance configuration. In this guide, it is a 39 GB cluster with three [`redis-highmem-medium`](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification) nodes in the `us-central1` region.

  * A Private Service Connect [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies).

  * A subnet for your instance.

  * A network for your instance.




The instructions for adding these Terraform resources are as follows:

  1. Add the following resources to your Terraform configuration file:
         
         provider "google" {
           project = "PROJECT_ID"
         }
         
         resource "google_redis_cluster" "cluster-ha" {
           name           = "CLUSTER_ID"
           shard_count    = 3
           psc_configs {
             network = google_compute_network.producer_net.id
           }
           region = "us-central1"
           replica_count = 1
           depends_on = [
             google_network_connectivity_service_connection_policy.default
           ]
         
         }
         
         resource "google_network_connectivity_service_connection_policy" "default" {
           name = "POLICY_NAME"
           location = "us-central1"
           service_class = "gcp-memorystore-redis"
           description   = "my basic service connection policy"
           network = google_compute_network.producer_net.id
           psc_config {
             subnetworks = [google_compute_subnetwork.producer_subnet.id]
           }
         }
         
         resource "google_compute_subnetwork" "producer_subnet" {
           name          = "SUBNET_ID"
           ip_cidr_range = "10.0.0.248/29"
           region        = "us-central1"
           network       = google_compute_network.producer_net.id
         }
         
         resource "google_compute_network" "producer_net" {
           name                    = "NETWORK_ID"
           auto_create_subnetworks = false
         }
         
         

Replace the following:

     * PROJECT_ID is your instance's project ID.
     * CLUSTER_ID is your chosen ID of the Memorystore for Redis Cluster instance you're creating. The ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.
     * POLICY_NAME is your chosen name for the Private Service Connect service connection policy for your project. For more information about the service connection policy, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).
     * SUBNET_ID is your chosen ID of the subnet created in this example that is used by the Memorystore cluster.
     * NETWORK_ID is your chosen ID of the network created in this example that is used by the Memorystore cluster.



## Deploy the Terraform configuration file

  1. Run `terraform init`.

  2. Run `terraform plan`.

  3. Run `terraform apply`.




## Connect to the instance from a Compute Engine VM

Next, connect to the newly created Memorystore for Redis Cluster instance.

You can connect to the instance from any Compute Engine VM that uses the instance's authorized network.

  1. If you don't already have a Compute Engine VM that uses that same authorized network as your instance, create one and connect to it by following [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `telnet` using `apt-get`:
         
         sudo apt-get install telnet
         

  3. From the terminal, telnet to the IP address of the instance, replacing VARIABLES with appropriate values.
         
         telnet CLUSTER_DISCOVERY_ENDPOINT_IP_ADDRESS CLUSTER_DISCOVERY_ENDPOINT_PORT_NUMBER
         

  4. In the telnet session, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the Redis instance using the following steps:

  1. Remove the `google_redis_instance` resource from your Terraform configuration file.
  2. Run Terraform `init`, `plan`, and `apply` to destroy the Redis resource.
  3. [Delete](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) any Compute Engine VMs you created for this quickstart.



## Configure Terraform to set up multiple VPC networks

The sections in this page show examples of creating a Memorystore for Redis Cluster instance and setting up connectivity in a Virtual Private Cloud (VPC) network. To find instructions and examples of using Terraform to set up connectivity in multiple VPC networks, see the [google_redis_cluster_user_created_connections](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/redis_cluster_user_created_connections) page.

## What's next

  * Learn more about [Creating instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).
  * Learn more about [High availability and replicas](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas).
  * Learn more about [Best practices for Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
