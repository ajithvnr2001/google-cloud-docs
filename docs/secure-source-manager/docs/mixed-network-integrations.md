---
url: https://docs.cloud.google.com/secure-source-manager/docs/mixed-network-integrations/
title: Mixed network integrations \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:30.125297+00:00
---

# Mixed network integrations  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/mixed-network-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Mixed network integrations Stay organized with collections  Save and categorize content based on your preferences. 

When integrating Secure Source Manager with other CI/CD solutions, the recommended approach often depends on your network environment. If your CI/CD solution combines public and private networks, and some deployment tooling isn't a Google Cloud service, then you can use a mixed-network integration.

Architecture for a mixed-network integration generally involves connecting Secure Source Manager to third-party CI/CD tools that are on-premises or in an external network.

![Mixed network architecture diagram showing Secure Source Manager
       communicating via Private Service Connect and public endpoints](https://docs.cloud.google.com/static/secure-source-manager/docs/images/mixed_network_integration.svg)Figure 1. Mixed network integration architecture.

For step-by-step instructions on setting up this type of integration with third-party tools, see:

  * [Connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins)
  * [Create a Private Service Connect instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance)



## What's next

  * [Learn about webhooks](https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
