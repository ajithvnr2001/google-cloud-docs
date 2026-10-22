---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/core-components/
title: How Certificate Manager (2nd gen) works \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:00.166752+00:00
---

# How Certificate Manager (2nd gen) works  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/core-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  How Certificate Manager (2nd gen) works Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the core components of Certificate Manager (2nd gen) and how they interact with your Google Cloud resources and external certificate authority sources.

Certificate Manager (2nd gen) lets you adopt features incrementally. You can start by monitoring your existing certificate inventory and then add automated issuance or trust management as your needs grow.

## Core components

Certificate Manager (2nd gen) has the following core components:

  * **Certificate directory** : A unified list of all detected and manually uploaded certificates in your project.
  * **Overview dashboard** : A monitoring tool that summarizes your certificate environment, including expiration alerts and security trends.
  * **Issuance configurations** : Reusable policies that define how Certificate Manager (2nd gen) generates and manages automated certificate renewals.
  * **Trust configurations** : Definitions for trust anchors, such as root CA certificates, that workloads use for mutual TLS (mTLS) to verify identities.



## Architecture overview

The following diagram shows how these components interact with each other:

[ ![Architecture diagram showing Certificate Manager \(2nd gen\)
         core components and their interactions with Google cloud resources
         and external CA sources.](https://docs.cloud.google.com/static/certificate-manager/images/CCMv2-arch.svg)](https://docs.cloud.google.com/static/certificate-manager/images/CCMv2-arch.svg) Certificate Manager (2nd gen) architecture showing component interactions.

The certificate inventory adds certificates from CA Service and integrated Google Cloud resources. You can use the overview dashboard to monitor certificate health, and automate lifecycle management by configuring issuance and trust settings. The following sections describe each component in detail.

### Certificate observability

Certificate Manager (2nd gen) automatically monitors your environment and populates the certificate directory from the following sources:

  * **Integrated Google Cloud services** : Certificates used by services like managed workload identity and Cloud Load Balancing (including uploaded and classic certificates).
  * **Certificate Authority Service** : Certificates issued by your [Enterprise tier](https://docs.cloud.google.com/certificate-authority-service/docs/tiers) private CA pools.



### Certificate monitoring

The overview dashboard uses the data from the certificate directory to summarize the health and security posture of your environment. You can use the dashboard to perform the following tasks:

  * **Identify expiring certificates** : Prioritize renewals by seeing which certificates are nearing expiration across all services.
  * **Audit security posture** : Monitor the distribution of cryptographic algorithms and key lengths to ensure compliance with security standards.
  * **Track issuance trends** : Gain insights into certificate usage and issuance over time.



### Automated certificate lifecycle management

You can automate the management of your certificates by configuring issuance and trust settings:

  * **Issuance configurations** : Define parameters like lifetime, key algorithm, and rotation window. When an issuance configuration is associated with a resource, Certificate Manager (2nd gen) automatically generates and renews the certificate.
  * **Trust configurations** : Distribute trust anchors to your applications to secure workload-to-workload communication using mutual TLS (mTLS). This approach ensures applications trust only approved certificates.



## What's next

  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [View certificate directory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)
  * [Create trust configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/trust-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
