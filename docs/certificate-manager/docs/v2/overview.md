---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/overview/
title: Certificate Manager (2nd gen) overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:08.243276+00:00
---

# Certificate Manager (2nd gen) overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Certificate Manager (2nd gen) overview Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Certificate Manager (2nd gen) is a Google Cloud service that lets you centralize the management, deployment, and automation of SSL/TLS certificates across your organization. With Certificate Manager (2nd gen), you can manage certificates for various Google Cloud services, custom workloads, and on-premises environments through a single, centralized interface.

Certificate Manager mainly supports Google Cloud load balancers, whereas Certificate Manager (2nd gen) has expanded support for Google Kubernetes Engine (GKE) workloads, Compute Engine instances, and hybrid environments.

To understand the differences between the first and second generation of Certificate Manager, see [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison).

## Certificate Manager (2nd gen) features

Certificate Manager (2nd gen) lets you do the following:

  * **Monitor certificates** : Use the **Overview** page in the Google Cloud console to monitor certificate health, including active certificates for each of your services, those nearing expiration, and the distribution of cryptographic algorithms. For more information, see [Monitor certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor).

  * **Search and discover certificates:** Use the **Certificates** page in the Google Cloud console to view all your certificates, including those not directly issued by Certificate Manager. You can filter by resource type, expiration status, and management status. For more information, see [View certificate directory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory).

  * **Automate certificate lifecycles** : Control certificate generation and rotation on Google Cloud resources like load balancers, and Google Cloud workloads by defining policies using issuance configurations. You can specify the following settings for auto-managed rotation:

    * Certificate lifetime
    * Key algorithm
    * Rotation window

For more information, see [Create issuance configurations](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration), [Configure lifecycle management for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-load-balancers), and [Configure lifecycle management for managed workloads](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads).

  * **Secure workload communication** : Define and distribute trust anchors, such as the root and intermediate CA certificates, to ensure workloads only trust authorized certificates. For more information, see [Create trust configurations](https://docs.cloud.google.com/certificate-manager/docs/v2/trust-configuration).




## Supported Google Cloud services

Certificate Manager (2nd gen) integrates directly with Certificate Authority Service and Public CA to simplify management of both private and public certificates. It supports the following two integration models:

  1. Certificate Manager (2nd gen) auto-manages certificates for the following services:

     * **Managed workload identity-enabled environments:**
       * **GKE:** Automates certificate issuance and rotation for your GKE workloads.
       * **Compute Engine:** Automates certificate management for your Compute Engine instances.
     * **Cloud Load Balancing:** Certificate Manager (2nd gen) automates TLS certificate provisioning and renewal for Cloud Load Balancing by using issuance configurations. This automation includes securing mutual TLS (mTLS) communication between Application Load Balancers and their backends.
  2. CA Service auto-manages certificates for the following services, and Certificate Manager (2nd gen) observes them:

     * **Agent Identity-enabled environments:**
       * **Vertex AI Agent Engine:** Automated certificate management to enable secure authentication to Google Cloud and third-party APIs.
       * **Gemini Enterprise:** Automated certificate management for root agents, no-code agents, and Google-managed agents inside the Gemini Enterprise platform.
     * **Cloud SQL:** Cloud SQL instances with certificates issued by your CA Service appear in Certificate Manager (2nd gen) for observability and management.
     * **Secure Web Proxy:** Proxies with certificates issued by your CA Service appear in Certificate Manager (2nd gen) for observability and management.
     * **Cloud Service Mesh:** GKE workloads that leverage Cloud Service Mesh have certificates that Certificate Manager (2nd gen) observes and manages.
     * **GKE control plane authority:** GKE clusters that use custom CA and certificates (from CA Service) to sign and verify credentials within the GKE control plane have certificates that Certificate Manager (2nd gen) observes and manages.



## How Certificate Manager (2nd gen) impacts APIs, the gcloud CLI, and Terraform

Certificate Manager (2nd gen) introduces features that build upon both existing APIs and the new API.

  * **Certificate Manager (2nd gen)** : Second generation features are fully supported and manageable in the Google Cloud console.
  * **Certificate Manager** : Existing APIs aren't deprecated. You can continue to use the gcloud CLI, Terraform, and direct HTTP API calls to interact with first generation features.



Certificate Manager (2nd gen) uses both the `v1` and `v2` API namespaces.

The following list details the API namespace breakdown for each resource:

  * **`v2` namespace**: Contains the Observed Certificates API (`v2/projects.locations.observedCertificates`)
  * **`v1` namespace**: Contains the core management APIs used across both generations: 
    * Certificate API (`v1/projects.locations.certificates`)
    * Certificate Map API (`v1/projects.locations.certificateMaps`)
    * Certificate Issuance Config API (`v1/projects.locations.certificateIssuanceConfigs`)
    * Trust Config API (`v1/projects.locations.trustConfigs`)



## What's next

  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [Issue a certificate using CA Service and verify in Certificate Manager (2nd gen)](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-ca-service)
  * [Automate certificate lifecycle for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-lb-certificates)
  * [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/v2/roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
