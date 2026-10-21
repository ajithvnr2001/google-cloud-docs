---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/vpc-service-controls/
title: VPC Service Controls \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:04.148280+00:00
---

# VPC Service Controls  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

You can use VPC Service Controls with AML AI to restrict data access and prevent data exfiltration, even by users and accounts which otherwise have the permissions in IAM to access data. This helps prevent access from unauthorized devices and networks.

VPC-SC for AML AI can be set up and monitored like any other VPC Service Controls service.

For more information about VPC-SC, see the [VPC SC documentation](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Applying VPC-SC to the Google AML AI

Where VPC-SC is enabled, services consumed by AML AI must be accessible within the same VPC-SC perimeter. VPC-SC allows for complex configuration, but you should consider:

  * Cloud KMS
  * The BigQuery dataset (note that the input and output datasets must be in the same project)
  * The network origin from which requests will be made



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
