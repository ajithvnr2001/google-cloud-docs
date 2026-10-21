---
url: https://docs.cloud.google.com/binary-authorization/docs/set-up-asm/
title: Set up overview for Cloud Service Mesh \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:11.291411+00:00
---

# Set up overview for Cloud Service Mesh  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/set-up-asm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Set up overview for Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to set up Binary Authorization for use with Cloud Service Mesh.

## Before you begin

Before you use Binary Authorization for Cloud Service Mesh, you must first install Cloud Service Mesh on Google Kubernetes Engine (GKE). For more information, see the [quickstart](https://docs.cloud.google.com/service-mesh/docs/quickstart-asm) or the [GKE installation guides](https://docs.cloud.google.com/service-mesh/docs/all-gke-install-guides).

## Setup Steps

To set up Binary Authorization for Cloud Service Mesh, perform the following steps:

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).
  2. Configure your Binary Authorization policy.

**Note:** Skip this step if you want to use attestations.

You can configure the following features in your policy:

     * [Default rule](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule).
     * [Specific rules for your Cloud Service Mesh service identity](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm).
     * [Exempt images](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#exempt_images). [Learn more about exempt images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images).
  3. Optional: Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).

  4. Optional: [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

  5. View audit logs by following instructions in [View audit logs for GKE](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs).




## Disable Binary Authorization for GKE with Cloud Service Mesh

To disable Binary Authorization for GKE with Cloud Service Mesh enabled, follow the instructions in [Disable Binary Authorization for GKE](https://docs.cloud.google.com/binary-authorization/docs/disabling).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
