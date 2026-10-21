---
url: https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network/
title: Using Cloud Build in a private network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:35:46.149504+00:00
---

# Using Cloud Build in a private network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Using Cloud Build in a private network Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure commonly-used private network setups to use with private pools. For an overview of private pools, see [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## Defining the default network settings

When you create a private pool, by default you're set up to use the Virtual Private Cloud network in which the private pools reside. Use the default VPC network if:

  * You want builds to access the public internet.
  * You want [configurable machine types and sizes](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), static internal IP ranges, or one of the other features of [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).
  * You are **not** looking for builds to access resources within your private VPC network.



For instructions on connecting to the default network, see [Creating a private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool).

## Defining a static internal IP range

In some cases, you may need to have a defined static IP range for your private pool, such as when calling a service that allowlists calls from a defined IP range. With private pools, when setting up a [private connection between your VPC network and the private pool's VPC network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#setup-private-connection), you can create allocated IP address ranges with a defined CIDR range of IPs that your private pools will run on. You can also specify a smaller CIDR range within an allocated IP address range that a private pool will use.

## Running in a VPC network

To use Cloud Build with resources in a private network behind a firewall, such as in a VPC network, you can [create a private connection between the private pool and your managed VPC network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#setup-private-connection). This enables the private pool to access resources in your private network such as source repositories, artifact repositories, databases, secrets instances, and runtimes.

## Running in a shared VPC network

If you're using a shared VPC network, the project where you're creating the private pool must be attached to the host project that contains the shared VPC network. For instructions on attaching a project, see [Provisioning a shared VPC network](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).

## Connecting to resources in another peered VPC network or shared VPC network

Organizations often adopt a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) (host project) to centralize networking and Identity and Access Management across all the projects. This allows internal IP addresses to be used for Google-managed services like [private GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#create_private_cluster) and [private Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). These Google-managed services are also peered into a customer-owned shared VPC network. The issue with this setup is that private pools are not able to communicate with the Google-managed services due to the [lack of transitive peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#transit-network). Transitive peering is only an issue when multiple networks are connected to one another via VPC peering. If one of the connections is changed to use a [VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) (or [interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect)) instead of VPC peering, then the networks can establish connectivity. For instructions on this network setup, see [Accessing private Google Kubernetes Engine clusters with Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/accessing-private-gke-clusters-with-cloud-build-private-pools).

## Running in a specific region

You can create a private pool in one of the [supported regions](https://docs.cloud.google.com/build/docs/locations). You can store any built container images and artifacts in [Artifact Registry repositories](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build) and [Cloud Storage buckets](https://docs.cloud.google.com/build/docs/building/store-build-artifacts) in specified regions.

## Deploying to private GKE clusters

Private GKE clusters can have a public or private endpoint for the control plane.

To deploy to a private GKE cluster with a public endpoint, you can [create your private pool in the default network with access to the public internet](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool) and define a static internal IP range for your pool to allow list for access to the cluster.

To deploy to private GKE clusters with a private endpoint, you can follow the steps described in [Accessing private Google Kubernetes Engine clusters with Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/accessing-private-gke-clusters-with-cloud-build-private-pools). Alternatively, once peered into your VPC, you can run a network proxy on the cluster as described in [Creating private GKE clusters with network proxies](https://docs.cloud.google.com/architecture/creating-kubernetes-engine-private-clusters-with-net-proxies).

## Using with VPC Service Controls

VPC Service Controls is a Google Cloud feature that allows you to set up a secure perimeter to guard against data exfiltration. For instructions on using VPC Service Controls with private pools to add additional security to your builds, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

## Removing public IPs on private pools

You can remove public IPs on private pools by [setting `egressOption` field in the private pool config file to `NO_PUBLIC_EGRESS`](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema). However, keep in mind that removing public IPs will restrict your private pool from accessing resources in the public internet.

## Restricting egress to the public internet

There are few ways to restrict egress from private pools to the public internet:

  * Remove public IPs on private pools by [setting `egressOption` field in the private pool config file to `NO_PUBLIC_EGRESS`](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema). This will remove all access from the private pool to the public internet.

  * Create a [private pool within a VPC Service Controls perimeter](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls). This allows you to set up a secure perimeter to guard against data exfiltration.

  * [Customize firewall rules on your VPC network](https://docs.cloud.google.com/vpc/docs/vpc#firewall_rules) to restrict egress.




## Enforcing the usage of private pools

Cloud Build provides a `constraints/cloudbuild.allowedWorkerPools` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints) that you can enforce to mandate the builds in your organization to not use the default pool and only use the private pool. For instructions on using this feature, see [Setting up organization policy constraints](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#optional_setting_up_organization_policy_constraints).

## Using with private Cloud DNS zones

You can share a private Cloud DNS zone to use with private pools. For instructions, see [Sharing a private zone](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering).

## Running behind a NAT

Although you can control the IP range of your private pool in your VPC, the external IP addresses (if enabled) cannot be controlled. If you need to access a resource from a reserved IP, create a proxy VM and route traffic through it by completing steps in [Access external resource from a static source IP address using Cloud Build](https://console.cloud.google.com/?walkthrough_id=build--cloud-build-static-external-ip).

## What's next

  * Learn how to [set up your environment to create private pools](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment).
  * Learn how to [create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
