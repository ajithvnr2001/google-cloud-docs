---
url: https://docs.cloud.google.com/secure-source-manager/docs/public-network-integrations/
title: Public network integrations \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:20.124863+00:00
---

# Public network integrations  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/public-network-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Public network integrations Stay organized with collections  Save and categorize content based on your preferences. 

When integrating Secure Source Manager with other CI/CD solutions, the recommended approach depends on your network environment. If your CI/CD tools exist within public networks, you can use public endpoints to connect them.

In a default public network configuration, services connect over the public internet. This configuration requires fewer steps to set up than private network integrations, but exposes the services to the internet.

Secure Source Manager supports a built-in integration with Cloud Build using build configuration and trigger files. For other CI/CD solutions, you can use webhooks.

![Architecture showing Secure Source Manager connected to external tools through public endpoints](https://docs.cloud.google.com/static/secure-source-manager/docs/images/public_network_integration.svg)Public network integration architecture

For more information about setting up Secure Source Manager on a public network, see:

  * [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build)
  * [Connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins)
  * [Set up webhooks](https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks)



## What's next

  * [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
