---
url: https://docs.cloud.google.com/secure-source-manager/docs/private-network-integrations/
title: Private network integrations \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:53.552648+00:00
---

# Private network integrations  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/private-network-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Private network integrations Stay organized with collections  Save and categorize content based on your preferences. 

When integrating Secure Source Manager with other CI/CD solutions, the recommended approach often depends on your network environment. A private network integration ensures that your entire CI/CD solution: from code repository to build, artifact storage, and deployment tooling all remain within a secure private network.

A private network architecture uses these key features:

  * **Secure Source Manager**
  * **Private Service Connect**
  * **Cloud Build private pools**

![Secure Source Manager connected to Private Service Connect and Cloud Build private pools](https://docs.cloud.google.com/static/secure-source-manager/docs/images/private_network_integration.svg)Figure 1. Private network integration architecture.

## Recommended workflow: Developer Connect

For most users setting up a private network integration between Secure Source Manager and Cloud Build, Developer Connect is the recommended choice due to its simplicity.

While Developer Connect Git proxies use IAM for access control, the proxy endpoint exists on the public internet. For a defense-in-depth approach that keeps all endpoints on a private network, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to restrict access to the proxy endpoint.

For step-by-step instructions on setting up this integration, see [Integrate Secure Source Manager with Cloud Build using Developer Connect](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager).

## Alternative workflow: Cloud Build private pools

If specific requirements prevent you from exposing a Git proxy, even one protected by IAM and VPC Service Controls, then use an alternative setup to connect Secure Source Manager to Cloud Build through a Private Service Connect endpoint and Cloud Build private pools.

For step-by-step instructions on setting up this integration, see [Connect Cloud Build to a Private Service Connect instance](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build-private-service-connect).

## What's next

  * [Connect Cloud Build to a Private Service Connect instance](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build-private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
