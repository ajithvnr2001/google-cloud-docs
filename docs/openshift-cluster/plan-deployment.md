---
url: https://docs.cloud.google.com/openshift-cluster/plan-deployment/
title: Plan your OpenShift cluster installation \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:15.930979+00:00
---

# Plan your OpenShift cluster installation  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/plan-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Plan your OpenShift cluster installation Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information that you can use to plan the installation of a Red Hat OpenShift cluster on Google Cloud. 

This document is intended for cloud architects, platform administrators, and developers who want to develop and deploy enterprise-grade applications on OpenShift clusters that run on Google Cloud.

## Choose an installation model

You can install the OpenShift control plane on Google Cloud either on a self-managed basis or as a managed solution.

Consider the following factors when choosing an installation model:

Factor | Self-managed OpenShift | Managed OpenShift  
---|---|---  
Management responsibility |  A self-managed OpenShift cluster on Google Cloud uses a shared responsibility model:

  * You manage the OpenShift cluster, OS, and applications.
  * Google Cloud manages the physical infrastructure and its security.
  * You manage OS hardening, and the security at the cluster and application levels.

|  A managed OpenShift cluster on Google Cloud uses a shared responsibility model:

  * Red Hat manages the OpenShift Dedicated service, and you share responsibilities for some aspects of the setup.
  * Google Cloud manages the physical infrastructure and security.

For more information, see the Red Hat document [Responsibility assignment matrix](https://docs.redhat.com/en/documentation/openshift_dedicated/4/html-single/introduction_to_openshift_dedicated/index#policy-responsibility-matrix).  
Use case | 

  * You want to migrate OpenShift clusters to Google Cloud that have a substantial history of customization and configuration.
  * You want to keep your application architecture consistent between OpenShift and other environments, such as on-premises.

|  You want to quickly deploy applications on OpenShift without the operational burden of managing the underlying infrastructure.  
Installation method |  To install a self-managed OpenShift cluster on Google Cloud, you use the Red Hat OpenShift Container Platform. For more information about this platform, see [Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/overview/index). For information about the deployment architecture of OpenShift Container Platform, see [OpenShift Container Platform architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/architecture/architecture). |  To install an OpenShift cluster on Google Cloud as a managed solution, you use Red Hat OpenShift Dedicated - a managed cloud service provided by Red Hat. For more information about this service, see [Red Hat OpenShift Dedicated](https://cloud.google.com/solutions/redhat#red-hat-openshift-dedicated) service. For information about the deployment architecture of OpenShift Dedicated, see [OpenShift Dedicated architecture](https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/architecture/architecture).  
Benefits | 

  * The self-managed option offers you more control and flexibility for managing OpenShift clusters.
  * You can streamline the usage of Google services with your self-managed OpenShift clusters by using Cluster Services for OpenShift. This service provides built-in OpenShift integrations for Google services. Cluster Services for OpenShift is jointly developed and supported by Google Cloud and Red Hat. For more information about Cluster Services for OpenShift, see [Overview of Cluster Services for OpenShift](https://docs.cloud.google.com/openshift-cluster/overview).

| 

  * OpenShift Dedicated helps you accelerate application deployment and streamline operations on the OpenShift platform.
  * OpenShift Dedicated is supported by Red Hat site reliability engineers and includes an SLA. For more information, see [OpenShift Online Terms of Service](https://access.redhat.com/support/offerings/openshift/sla). This managed support lets you focus on your business instead of managing the underlying infrastructure and services.

  
  
## Choose an installation method

You can install the OpenShift control plane on Google Cloud by using a graphical user interface (GUI), command-line interface (CLI), application programming interface (API), or an Infrastructure as Code (IaC) tool.

The availability of these installation methods depends on the installation model that you choose, as described in the following table:

Installation method | Availability for self-managed OpenShift | Availability for managed OpenShift | Description  
---|---|---|---  
Graphical user interface (GUI) | No | Yes |  The Google Cloud console provides a dedicated GUI that shows you how to install self-managed and managed OpenShift on Google Cloud. Click the following button to access this GUI: [Go to Red Hat OpenShift on Google Cloud](https://console.cloud.google.com/redhat-openshift/landing)  
Command-line interface (CLI) | Yes | Yes |  To install self-managed OpenShift on Google Cloud, you use the OpenShift Container Platform installer. For more information, see [Installing OpenShift Container Platform on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/installing_on_google_cloud/index). To install managed OpenShift on Google Cloud, you use the `ocm-cli` tool. For more information, see [Using the `ocm-cli` to manage clusters in OpenShift Cluster Manager](https://access.redhat.com/articles/6114701) (requires a Red Hat account).  
Application programming interface (API) | No | Yes |  To install managed OpenShift on Google Cloud, you use the [OpenShift Cluster Manager API](https://api.openshift.com/).  
Infrastructure as Code (IaC) tool | Yes | No |  To install self-managed OpenShift on Google Cloud, follow the instructions to [install an OpenShift cluster on user-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/installing_on_google_cloud/installing-gcp-user-infra), with an IaC tool such as Terraform.  
  
## Understand billing

Running OpenShift clusters on Google Cloud includes the following two categories of charges:

  * **Infrastructure charges:** To run OpenShift clusters on Google Cloud, you use services such as Compute Engine, Persistent Disk, Hyperdisk, and Cloud Load Balancing. These services are billed according to their respective billing models.

  * **Software related costs:** Running OpenShift clusters also involves software related charges in the form of OpenShift entitlements or Red Hat OpenShift subscriptions. These charges are separate from the infrastructure charges.




## Get an OpenShift subscription

To run enterprise-ready OpenShift clusters on Google Cloud, you require a Red Hat OpenShift subscription. This subscription provides a comprehensive enterprise Kubernetes platform, including the container platform, management tools, security services, and technical support.

You can get an OpenShift subscription by using the following options:

  * **Google Cloud Marketplace:** You can go to Cloud Marketplace to get subscriptions for both self-managed and managed OpenShift control planes.

To run self-managed OpenShift on Google Cloud, you can get the following subscriptions from Cloud Marketplace:

    * [Red Hat OpenShift Container Platform](https://console.cloud.google.com/marketplace/product/redhat-marketplace/red-hat-openshift-container-platform-prod): A comprehensive offering that includes OpenShift Container Platform and additional tools for advanced cluster security, management, and a global container registry. This subscription is suitable for enterprises needing a full suite of capabilities across multiple clusters and hybrid cloud deployments.
    * [Red Hat OpenShift Platform Plus](https://console.cloud.google.com/marketplace/product/redhat-marketplace/openshift-platform-plus): This is the core enterprise Kubernetes platform. It provides a robust and scalable environment for building, deploying, and running containerized applications. This is the standard choice for most self-managed deployments.
    * [Red Hat OpenShift Kubernetes Engine](https://console.cloud.google.com/marketplace/product/redhat-marketplace/openshift-kubernetes-engine): An offering that provides essential Kubernetes Engine components for running applications on OpenShift. This subscription is suitable for users who need the core OpenShift runtime without the broader platform management features.

To run managed OpenShift on Google Cloud, you can get a subscription for [Red Hat OpenShift Dedicated](https://console.cloud.google.com/marketplace/product/redhat-marketplace/red-hat-openshift-dedicated).

For more information about OpenShift subscriptions, see the Red Hat document [Red Hat OpenShift subscription editions](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide#section-3).

  * **Bring Your Own Subscription (BYOS) model:** The BYOS model lets you bring to Google Cloud any existing OpenShift entitlements or Red Hat OpenShift subscriptions that you own.

For example, if you're migrating an OpenShift cluster from an on-premises environment to Google Cloud, then you can re-use the Red Hat OpenShift subscription that you own for running that OpenShift cluster on-premises.




## Migrate OpenShift clusters to Google Cloud

If you're considering moving your OpenShift clusters to Google Cloud, then you can reach out to Google Cloud and ask for a migration assessment.

If you're already using Google Cloud, then you can reach out to your Technical Account Manager (TAM). If you're new to Google Cloud, then you can reach out to [Google Cloud Sales](https://cloud.google.com/contact).

The migration assessment process begins with a review of your migration goals and the architecture of your existing OpenShift environments. Google Cloud experts then collaborate with you to design a migration strategy that also helps you optimize your OpenShift environments for performance, cost, and scalability.

## Best practices for running OpenShift on Google Cloud

For running OpenShift clusters on Google Cloud, we recommend the following best practices.

### Security best practices

  * To let your OpenShift clusters authenticate with Google Cloud APIs, we recommend that you use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) instead of storing service account keys on hosts.

Workload Identity Federation lets you do the following:

    * Set permissions for individual components of the OpenShift platform by using Kubernetes service accounts.
    * Use managed short-lived authentication tokens.
    * Avoid the need to store authentication keys on the host.

For more information, see the Red Hat document [Configuring a Google Cloud cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_gcp/installing-gcp-customizations#installing-gcp-with-short-term-creds_installing-gcp-customizations).

  * To help protect your data at rest in Google Cloud, we recommend that you use customer-managed encryption keys (CMEK) for storage. We recommend this configuration for the following components of your OpenShift deployment:

    * Persistent volumes or Persistent volume claims (PV/PVCs), which manages persistent storage for applications and workloads that run on OpenShift clusters.
    * The boot disks of the Compute Engine instances that you use to host the Openshift clusters.

For information about CMEK, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).




### High availability best practices

To help ensure high availability for the applications that run on your OpenShift clusters on Google Cloud, we recommend that you install both the control plane and the worker nodes in multiple [zones](https://docs.cloud.google.com/compute/docs/regions-zones).

For more information, see [Best practices for high availability with OpenShift](https://docs.cloud.google.com/openshift-cluster/best-practices-for-ha).

### Disaster recovery best practices

To help ensure resilience for the applications that run on your OpenShift clusters on Google Cloud, implement the best practices as described in the following documents:

  * [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr)
  * [Disaster recovery strategies for active-passive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups)
  * [Disaster recovery strategies for active-inactive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups)



## What's next

  * Learn about [Cluster Services for OpenShift](https://docs.cloud.google.com/openshift-cluster/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
