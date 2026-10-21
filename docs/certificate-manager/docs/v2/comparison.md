---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/comparison/
title: Compare Certificate Manager versions \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:08.769759+00:00
---

# Compare Certificate Manager versions  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/comparison/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Compare Certificate Manager versions Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document briefly compares the first and second generation of Certificate Manager. Certificate Manager lets you deploy and manage TLS certificates specifically for Google Cloud load balancers. The second generation expands this support to include Google Kubernetes Engine (GKE) workloads, Compute Engine instances, and hybrid cloud architectures. It also provides unified certificate management across your entire infrastructure.

For information about the supported load balancers, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

## Feature differences

The following table compares the core capabilities of the two Certificate Manager versions:

Feature | Certificate Manager (2nd gen) | Certificate Manager  
---|---|---  
**Primary goal** | Enterprise-wide certificate observability and lifecycle management | Secure load balancers  
**Centralized observability** | Yes. All detected certificates. | Limited. Certificates configured for load balancers.  
**Multi-service support** | Yes. Supports Google Kubernetes Engine (GKE), Compute Engine, Vertex AI Agent Engine, and load balancers. | No. Only supports load balancers.  
**Views** | Advanced summary dashboard for tracking expiration, algorithms, and health. | List views only.  
  
## When to use which version

Use Certificate Manager (2nd gen) to centralize certificate observability and automate lifecycle management across your entire Google Cloud ecosystem. If your goal is strictly to secure load balancer certificates, you can continue using Certificate Manager. For more information, see [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy).

You can switch between versions.

## What's next

  * [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)
  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [View certificate directory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
