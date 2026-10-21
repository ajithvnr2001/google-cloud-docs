---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-producer-service/
title: Set up producer services \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:21.102364+00:00
---

# Set up producer services  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-producer-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Set up producer services Stay organized with collections  Save and categorize content based on your preferences. 

As a service producer, you deploy and manage the backend infrastructure, which includes virtual machines (VMs) for inspection, internal passthrough Network Load Balancers to distribute traffic, and the in-band integration resources.

This page provides details about the steps that a service producer must take to offer packet inspection services.

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

  6. Make sure that you have the following Identity and Access Management (IAM) roles on your project: 
     * [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)
     * [Intercept Deployment Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.interceptDeploymentAdmin) (`roles/networksecurity.interceptDeploymentAdmin`)
  7. Enable the Compute Engine and Network Security APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networksecurity.googleapis.com)

  8. Install the Google Cloud CLI. For more information, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't previously run the Google Cloud CLI, initialize your gcloud CLI directory by running the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init). 




## Prepare your network

In each zone where you plan to offer packet inspection services, create and configure the necessary networking and compute resources.

  1. Create a VPC network.

We recommend [creating a custom mode Virtual Private Cloud network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network), which gives you full control over [creating subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).

  2. Create subnets.

In each region that contains the zone where you want to offer the packet inspection service, create at least one subnet. You use the subnet for the network interfaces of your packet inspection VMs.

  3. Create managed or unmanaged instance groups containing your packet inspection VMs.

We recommend using managed instance groups, if possible. For full zonal isolation, use _zonal_ managed instance groups. For more information, see [Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

**Note:** NEG backends are not supported for packet inspection.
  4. Create firewall rules.

Create ingress `allow` firewall rules to permit `UDP` packets from the gateway IPv4 addresses of the producer subnets. For more information, see [Understand GENEVE format](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve).

  5. Create internal passthrough Network Load Balancers.

Create a load balancer in each zone of the region where you want to offer packet inspection services.

While configuring the load balancer, make a note of the following:

     * The load balancer's backend service protocol must be either `UDP` or `UNSPECIFIED`.

     * The load balancer's forwarding rule must use the `UDP` protocol and specify destination port `6081` to accept GENEVE-encapsulated packets.

     * Make sure that packet inspection VMs preserve each packet's 5-tuple characteristics. Packets that are allowed can't create a new connection with different packet characteristics.

     * The load-balanced network interface (NIC) of each packet inspection VM must use the same VPC network as the load balancer's backend service. For more information, see [Instance group backends and network interfaces](https://docs.cloud.google.com/load-balancing/docs/internal#ig-nic-net), [Backend service network specification](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service-network-spec), and [Backend service network rules](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service-network-rules).

     * GENEVE-encapsulated packets are routed to the packet inspection VMs with destinations that match the IP address of the internal passthrough Network Load Balancer, `UDP` protocol, and destination port `6081`.

The source IP address for each GENEVE-encapsulated packet is the gateway IPv4 address of the producer subnet. The source port is calculated by an opaque hash.

     * The health check you configure for the internal passthrough Network Load Balancer must use a [supported health check protocol](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports). Ingress `allow` firewall rules must also permit health check traffic. For more information about health checks, see [How health checks work](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method).

     * To simplify maintenance and increase availability, configure [failover for internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview).




## Configure in-band resources

Create the following resources to offer packet inspection services to consumers:

  1. Create an [intercept deployment group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview) in either the same project that contains the intercept deployments or in a different project in the same organization. For more information, see [Create and manage intercept deployment groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups).

  2. Create an [intercept deployment](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview) in each zone of the project where you have created the packet inspection VMs and internal passthrough Network Load Balancers.

Configure each intercept deployment to reference the forwarding rule of the internal passthrough Network Load Balancer with packet inspection VMs in the same zone as the intercept deployment. For more information, see [Create and manage intercept deployments](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments).

  3. Update the IAM policy of the project that contains the intercept deployment group, granting the [Intercept Deployment External User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.interceptDeploymentExternalUser) (`roles/networksecurity.interceptDeploymentExternalUser`) predefined role to the IAM principals who need to use the packet inspection services offered by the intercept deployment group.

Alternatively, you can grant a custom role that at least includes the predefined role's permissions.




While configuring the in-band resources, consider the following:

  * The intercept deployment group, its member zonal intercept deployments, their internal passthrough Network Load Balancers, and packet inspection VMs must be located in a single service producer project.

  * Within a producer VPC network that's used by VMs and internal passthrough Network Load Balancers for packet inspection, all zonal intercept deployments must belong to the same intercept deployment group.

  * Each intercept deployment references only one internal passthrough Network Load Balancer.




## What's next

  * [Intercept deployment groups overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview)
  * [Intercept deployments overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview)
  * [Create and manage intercept deployment groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups)
  * [Create and manage intercept deployments](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
