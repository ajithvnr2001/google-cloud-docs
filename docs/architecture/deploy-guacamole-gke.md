---
url: https://docs.cloud.google.com/architecture/deploy-guacamole-gke/
title: Apache Guacamole on GKE and Cloud SQL \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:03.151338+00:00
---

# Apache Guacamole on GKE and Cloud SQL  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deploy-guacamole-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Apache Guacamole on GKE and Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-09 UTC

[Apache Guacamole](https://guacamole.apache.org/) offers a fully browser-based way to access remote desktops through Remote Desktop Protocol (RDP), Virtual Network Computing (VNC), and Secure Shell Protocol (SSH) on Compute Engine virtual machines (VMs). Identity-Aware Proxy (IAP) provides access to Guacamole with improved security.

This reference architecture document is intended for server administrators and engineers who want to host Apache Guacamole on Google Kubernetes Engine (GKE) and Cloud SQL. This document assumes you are familiar with deploying workloads to Kubernetes and Cloud SQL for MySQL. This document also assumes you are familiar with Identity and Access Management and Google Compute Engine.

**Note:** Apache Guacamole is not a full Virtual Desktop Infrastructure (VDI) solution by itself. For alternative solutions that provide a full VDI, see [Virtual Desktops Solutions](https://docs.cloud.google.com/solutions/virtual-desktops).

## Architecture

The following diagram shows how a Google Cloud load balancer is configured with IAP, to protect an instance of the Guacamole client running in GKE:

![Architecture for Google Cloud load balancer configured with IAP.](https://docs.cloud.google.com/static/architecture/images/deploy-guacamole-gke-architecture-diagram.svg)

This architecture includes the following components:

  * **Google Cloud load balancer:** Distributes traffic across multiple instances, which reduces the risk of performance issues.
  * **IAP:** Provides improved security through a custom authentication extension.
  * **Guacamole client:** Runs in GKE and connects to the guacd backend service.
  * **Guacd backend service:** Brokers remote desktop connections to one or more Compute Engine VMs.
  * **Guacamole database in Cloud SQL:** Manages configuration data for Guacamole.
  * **Compute Engine instances:** VMs hosted on the Google infrastructure.



## Design considerations

The following guidelines can help you to develop an architecture that meets your organization's requirements for security, cost, and performance.

### Security and compliance

This architecture uses IAP to help protect access to the Guacamole service. Authorized users sign in to the Guacamole instance through a custom IAP authentication extension. For details, see the [custom extension in GitHub](https://github.com/GoogleCloudPlatform/guacamole-on-gcp/tree/main/client/extensions/guacamole-auth-googleiap).

When you add additional users (through the Guacamole user interface), these additional users must have permissions through IAM, with the `IAP-secured Web App User` role.

The OAuth configuration that this deployment creates is set to [internal](https://support.google.com/cloud/answer/6158849). Because of this setting, you must use a Google account in the same organization as the one you use to deploy Guacamole. If you use a Google account outside the organization, you receive an `HTTP/403 org_internal` error.

### Performance

Google Cloud load balancer and GKE distributes traffic across multiple instances, which helps to reduce the risk of performance issues.

## Deployment

To deploy this architecture, see [Deploy Apache Guacamole on GKE and Cloud SQL](https://docs.cloud.google.com/architecture/deploy-guacamole-gke/deployment).

## What's Next?

  * Review the GKE guidance on [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * Review [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) to increase security for secrets, such as database credentials and OAuth credentials.
  * Review [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to learn how to provide more granular control for user access to Guacamole.
  * Understand more about how IAP integration works by reviewing the custom authentication provider in the [GitHub repository](https://github.com/GoogleCloudPlatform/guacamole-on-gcp).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Richard Grime](https://www.linkedin.com/in/richard-grime-53777880) | Principal Architect, UK Public Sector

Other contributors: 

  * [Aaron Lind](https://www.linkedin.com/in/the-aaron-lind/) | Solution Engineer, Application Innovation
  * [Eyal Ben Ivri](https://www.linkedin.com/in/eyalbenivri) | Cloud Solutions Architect
  * [Ido Flatow](https://www.linkedin.com/in/idoflatow) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-09 UTC."],[],[]] 
