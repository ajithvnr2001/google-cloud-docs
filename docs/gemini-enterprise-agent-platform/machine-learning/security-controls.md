---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls/
title: Security controls for machine learning services \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:45.728470+00:00
---

# Security controls for machine learning services  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Security controls for machine learning services Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform implements Google Cloud security controls to help secure your models and training data. Some security controls aren't supported by Generative AI features in Gemini Enterprise Agent Platform. The following table lists the security controls available for Gemini Enterprise Agent Platform machine learning features.

| Data residency (at-rest)1 | [Customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) | [VPC Service Controls  
(VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs/overview) | [Access Transparency (AXT)](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)  
---|---|---|---|---  
Gemini Enterprise Agent Platform | ✔ | ✔ | ✔ | ✔  
RAG Engine |  |  | ✔ |   
Vector Search | ✔ |  | ✔ |   
  
1Vertex AI Feature Store and Vertex Data Labeling don't meet data-at-rest commitments.

Learn more about Data residency by expanding [General Service Terms](https://cloud.google.com/terms/service-terms#panel0-1) and reading **1\. Data Location**.

## Learn more

  * Learn more about [Generative AI security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
