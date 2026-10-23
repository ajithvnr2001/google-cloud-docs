---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc-service-controls/
title: (Optional) Configure your reporting to use VPC Service Controls \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:36.953486+00:00
---

# (Optional) Configure your reporting to use VPC Service Controls  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  (Optional) Configure your reporting to use VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Optionally, if you want to use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) in the environment in which your product's service runs, you must complete the following steps to integrate Google Cloud Marketplace reporting with VPC Service Controls.

  1. Set up your preferred implementation of VPC Service Controls in your service environment. For more information about setting up VPC Service Controls, visit [Set up a service perimeter by using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter).

  2. Ensure that the `servicecontrol.googleapis.com` service in your implementation of VPC Service Controls isn't restricted.

**Caution:** If your implementation of VPC Service Controls restricts the service `servicecontrol.googleapis.com`, reporting might not function as intended, and your users might not be charged correctly for their usage.



[ Previous arrow_back  Configure your reporting to use Virtual Private Cloud (VPC)  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
