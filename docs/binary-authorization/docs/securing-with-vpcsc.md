---
url: https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc/
title: Secure with VPC Service Controls \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:14.514283+00:00
---

# Secure with VPC Service Controls  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Secure with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improves your ability to mitigate the risk of unauthorized copying or transfer of data from your Google-managed services and resources.

With VPC Service Controls, you can configure security perimeters and control the movement of data across the perimeter boundary.

Binary Authorization stores data, including the policy, attestors, and attestations. By adding Binary Authorization to the security perimeter, VPC Service Controls can help protect these resources and services.

Additionally, Binary Authorization supports separation of duties by using separate Google Cloud projects for deployments, attestors and attestations. If using Binary Authorization in this way, each such project should be included in your VPC Service Controls perimeter. See [Multi-project setup](https://docs.cloud.google.com/binary-authorization/docs/multi-project-setup-cli) for an end-to-end tutorial that describes how to use multiple projects to establish separation of duties.

With Binary Authorization, you may use Artifact Analysis to store attestors and attestations as notes and occurrences, respectively. In this case, you must also include Artifact Analysis in the VPC Service Controls perimeter. See [VPC Service Controls guidance for Artifact Analysis](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#artifact-analysis) for additional details.

To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To learn about the limitations in using Binary Authorization with VPC Service Controls, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
