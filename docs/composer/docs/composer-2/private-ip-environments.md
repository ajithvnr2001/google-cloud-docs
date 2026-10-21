---
url: https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments/
title: Private IP environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:03.966521+00:00
---

# Private IP environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/private-ip-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Private IP environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/private-ip-environments "View this page for Managed Airflow \(Legacy Gen 1\)")

This page provides information about Private IP Managed Airflow environments.

For Private IP environments, Managed Airflow assigns only private IP ([RFC 1918](https://www.ietf.org/rfc/rfc1918.txt)) addresses to the managed Google Kubernetes Engine and Cloud SQL VMs in your environment, resulting in no inbound access to those managed VMs from the public internet. As an option, you can also use [privately used public IP addresses](https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip) and [the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent) to save the IP address space and to use non-RFC 1918 addresses.

By default, in a Private IP environment, Managed Airflow workflows do not have outbound internet access. Access to Google Cloud APIs and services is not affected by routing over Google's private network.

## VPC-native GKE cluster

When you create an environment, Managed Airflow [distributes your environment's resources](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture) between a Google-managed [tenant](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) project and your customer project.

For a Private IP environment, Managed Airflow creates a VPC-native GKE cluster for your environment in your customer project.

VPC-native clusters use [Alias IP routing](https://docs.cloud.google.com/vpc/docs/alias-ip) built into the VPC network, enabling the VPC to manage routing for pods. When you use VPC-native clusters, GKE automatically chooses a secondary range. For specific networking requirements, you can also [configure the secondary ranges](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip#secondary-range) for your GKE pods and GKE services when you create an environment.

## Private IP Managed Airflow environment

You can select a Private IP environment when you create an environment. Using private IP means that the GKE and Cloud SQL VMs in your environment are not assigned public IP addresses and communicate only over Google's internal network.

When you create a Private IP environment, the GKE cluster for your environment is [configured as a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters), and the Cloud SQL instance is [configured for private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

If your Private IP environment [uses Private Service Connect](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect), your customer project's VPC network and your tenant project's VPC network connect through a PSC endpoint.

If your Private IP environment uses VPC peerings, Managed Airflow creates a peering connection between your customer project's VPC network and your tenant project's VPC network.

With private IP enabled for your environment, the IP traffic between your environment's GKE cluster and Cloud SQL database is private, thus isolating your workflows from the public internet.

This additional layer of security affects how you connect to these resources and how your environment accesses external resources. Using private IP does not affect how you access Cloud Storage or your Airflow webserver over the public IP.

### GKE cluster

Using a private GKE cluster enables you to control [access to the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) (cluster nodes do not have public IP addresses).

When you create a private IP Managed Airflow environment, you specify whether or not access to the control plane is public and its IP range. The control plane IP range must not overlap with any subnetwork in your VPC network.

**Caution:** In Managed Airflow versions before 2.4.0, you need access to the control plane of your environment's cluster to [run Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli).Option | Description  
---|---  
Public endpoint access disabled  | To connect to the cluster, you must connect from a VM in the same region and same VPC network of the Private IP environment. The VM instance you are connecting from requires the [Access scope](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) **Allow full access to all Cloud APIs**.   
From that VM, you can run `kubectl` commands on your environment's cluster  
Public endpoint access enabled, master authorized networks enabled  | In this configuration, cluster nodes communicate with the control plane over Google's private network. Nodes can access resources in your environment and in authorized networks. You can [add authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) in GKE.   
On authorized networks, you can run `kubectl` commands on your environment's cluster  
  
### Cloud SQL

Because the Cloud SQL instance does not have a public IP address, the Cloud SQL traffic inside your Private IP environment is not exposed to the public internet.

Managed Airflow configures Cloud SQL to accept incoming connections through private service access. You can access the Cloud SQL instance on your VPC network by using its private IP address.

### Public internet access for your workflows

Operators and operations that require access to resources on unauthorized networks or on the public internet can fail. For example, the Dataflow Python operation requires a public internet connection to download Apache Beam from pip.

Allowing VMs without external IP addresses and private GKE clusters to connect to the internet requires [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview).

To use Cloud NAT, [create a NAT configuration](https://docs.cloud.google.com/nat/docs/gke-example#create-nat) using Cloud Router for the VPC network and region that your private IP Managed Airflow environment is in.

## What's next

  * [Configure Private IP networking](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip)
  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
