---
url: https://docs.cloud.google.com/service-health/docs/vpcsc/
title: Use VPC Service Controls with Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:09.255926+00:00
---

# Use VPC Service Controls with Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Use VPC Service Controls with Personalized Service Health Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can use VPC Service Controls with Personalized Service Health. [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) provides additional security to help mitigate the risk of data exfiltration. 

To use VPC Service Controls with Personalized Service Health, add your projects to [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters). These perimeters should protect resources and the Personalized Service Health service from requests that originate outside the perimeter.

**Note:** VPC Service Controls does not support the `OrganizationEvents` and `OrganizationImpacts` resources of the Service Health API. Therefore, VPC Service Controls policy checks won't occur when you call the methods for these resources. However, you can call the methods from a service perimeter using a restricted VIP.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
