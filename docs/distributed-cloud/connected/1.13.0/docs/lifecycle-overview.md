---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/lifecycle-overview/
title: Hardware lifecycle overview \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:55.231521+00:00
---

# Hardware lifecycle overview  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/lifecycle-overview/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Hardware lifecycle overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of the end-to-end journey of your Google Distributed Cloud connected hardware, from the initial order to a fully functional deployment on your premises.

The process is divided into three phases:

  1. Ordering
  2. Delivery and physical installation
  3. Bring-up and configuration



## Ordering

In the ordering phase, you plan your deployment, define your requirements, and place your order.

  1. **Plan your configuration** : Work with your network administrator and Google representatives to determine your hardware and network requirements.

     * Plan your [space](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#space), [power](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#power), and [cooling](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#cooling) requirements.
     * Select and procure [certified hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#hardware) based on your workload requirements.
     * Allocate necessary [IP address blocks](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#address-blocks) for machine management, Kubernetes nodes, and control plane virtual IP addresses (VIPs). Ensure that your IP address allocations are accurate. You cannot change these network configurations after the hardware is deployed.
  2. **Validate connectivity** : Run the [network connectivity validation tool](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements#validate-connectivity) on your local network to ensure that it meets all requirements for Domain Name System (DNS), Network Time Protocol (NTP), firewalls, and bandwidth.

  3. **Place the order** : Use the [Google Cloud console](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/order#order-console) or the [GDC Hardware Management API](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/order#order-api) to submit your order in your target project. The order includes contact information, site details, hardware configuration, and network configuration. This information is provided to your Google-certified systems integrator (SI).

  4. **Order review and contract** : A Google representative reviews your order, helps finalize the configuration, and works with you to sign the contract. After the order is accepted, the order state changes to `ACCEPTED`.




For more information, see [Order hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/order).

## Delivery and physical installation

In this phase, your Google-certified SI prepares and delivers the hardware and installs it at your site.

  1. **Hardware building** : Your Google-certified systems integrator builds and preconfigures the physical machines based on your order details. The order state transitions to `BUILDING`.

  2. **Shipping** : The hardware is shipped to your site. The order state transitions to `SHIPPING`.

  3. **On-site installation** :

     * A field technician from your SI arrives at your site.
     * The technician mounts the hardware in your rack or sets up the chassis.
     * Your network administrator works with the technician to connect the hardware to the power source and your local network, specifically the top-of-rack switches.
     * The technician activates the hardware. The order state transitions to `INSTALLING`. Ensure that your upstream Border Gateway Protocol (BGP) sessions and firewalls are configured before the technician starts activation, or the process will fail to complete.
  4. **Verification** : After the hardware is installed and connected, the machines boot up and establish a secure VPN connection to Google Cloud.

     * Verify that the machines are registered and visible in the [**Edge Zones** menu in the Google Cloud console](https://console.cloud.google.com/distributed-cloud/edgezones/list).
     * Alternatively, use the [`gcloud edge-cloud container machines list`](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/container/machines/list) command to verify their status.



After verification is complete, the order state transitions to `COMPLETED`.

## Bring-up and configuration

In this phase, your cluster administrator configures the software environment, creates clusters, and prepares the platform for workloads.

  1. **Set up the Google Cloud project** :

     * [Enable the required Google Cloud APIs](https://docs.cloud.google.com/service-usage/docs/enable-disable), such as `edgecontainer.googleapis.com`, `edgenetwork.googleapis.com`, and `gkehub.googleapis.com`.
     * [Create Google service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create) for specific functions, such as image pulling and external secrets.
  2. **Create a cluster** : Use the [`gcloud edge-cloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create) command to provision a cluster on the deployed machines. It can take an hour or more to download and install the necessary software. You can [monitor the provisioning progress](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#monitor-provisioning).

  3. **Configure networking** : Initialize the zone network and create VLAN subnetworks as required for your workloads. Distributed Cloud connected restricts direct access to the pod network. To enable communication with your local network, attach your workloads, especially virtual machines, to these L2 VLAN subnetworks.

  4. **Configure access** :

     * Configure cluster access. Google recommends that you use [Connect gateway](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#gateway) as the primary access method to leverage Identity and Access Management. You can also configure [local credentials](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#credentials) for local administration.
     * [Configure Kubernetes Role-Based Access Control (RBAC)](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/users#kubernetes-rbac) to grant access to other administrators or developers.
  5. **Configure storage** : To enable persistent storage, [apply your Symcloud Storage license](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/storage), which you obtain from Google Cloud Marketplace. You only apply the license. Google manages the underlying storage operator and storage pools.

**Warning:** Do not manually upgrade or modify the Google-managed operator for Symcloud Storage. Doing so renders Symcloud Storage inoperable.



The platform is now ready. You can deploy workloads, including containers and virtual machines, to the cluster.

## Summary of responsibilities

Action | Primary responsibility | Collaborators  
---|---|---  
**Planning and ordering** | Customer network administrator | Google sales and engineering  
**Hardware provisioning** | Google-certified systems integrator | None  
**Delivery and physical installation** | Field technician | Customer network administrator and site contact  
**Google Cloud project configuration** | Customer cluster administrator | None  
**Cluster creation and bring-up** | Customer cluster administrator | None  
**Workload deployment** | Customer application owner | Customer cluster administrator  
  
## What's next

  * [Installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements)
  * [Order hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/order)
  * [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
