---
url: https://docs.cloud.google.com/certificate-authority-service/docs/cas-integrations-cloud-services/
title: Integration with other Google Cloud services \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:47.259037+00:00
---

# Integration with other Google Cloud services  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/cas-integrations-cloud-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with other Google Cloud services

This document provides a summary of the Google Cloud services that have an integration with Certificate Authority Service.

## Cloud Service Mesh

Cloud Service Mesh is a suite of tools that helps you monitor and manage a reliable service mesh on-premises or on Google Cloud. You can configure Cloud Service Mesh to use CA Service for the following use cases:

  * If you need a dedicated certificate authority (CA) to sign workload certificates that's not shared with other users, or different CAs on different clusters.
  * If you need to back your signing keys in a managed HSM.
  * If you are in a highly regulated industry and are subject to compliance.
  * If you want your workload certificates in Cloud Service Mesh to chain up to an existing enterprise root CA certificate.



To learn how to use CA Service with Cloud Service Mesh, see [Install default features and Certificate Authority (CA)](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#install_ca_service).

## Cloud Service Mesh

Cloud Service Mesh lets you secure service-to-service communications in your mesh. CA Service integrates with Cloud Service Mesh to provide identity certificates to workloads running on Google Kubernetes Engine. You can modify your pods to allow workloads to receive and use these credentials for mTLS.

To learn how to use CA Service with Cloud Service Mesh, see the following pages:

  * [Set up service security with Envoy](https://docs.cloud.google.com/service-mesh/docs/security-envoy-setup)
  * [Set up service security with proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/security-proxyless-setup)



## Certificate Manager

CA Service integrates with Certificate Manager to simplify the process of managing the lifecycle of private certificates and provisioning private certificates to your _load balancers_ before the certificates expire. CA Service contains the CA pool that issues the private certificates while Certificate Manager lets you configure the issuance and provisioning of certificates to your load balancers.

To learn how to use Certificate Manager with CA Service, see [Configure CA Service integration with Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/certificates#int-cas).

## What's next

  * [Prepare your environment for Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/prepare-environment).
  * Get started with [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
