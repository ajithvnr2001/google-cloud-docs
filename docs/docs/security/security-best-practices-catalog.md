---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/
title: Google Cloud security best practices catalog \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:27.614229+00:00
---

# Google Cloud security best practices catalog  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Google Cloud security best practices catalog Stay organized with collections  Save and categorize content based on your preferences. 

You can use Google Cloud security best practices and guidelines to discover and implement security features for your workloads and supporting services on Google Cloud.

The security best practices are a Google-driven supplementary guide to existing regulatory and security practices in industries such as the financial services sector. The Google Cloud best practices and guidelines focus on foundational workload security controls.

These security best practices are intended to help chief information security officers (CISO), security practitioners, and risk and compliance officers adopt and deploy workloads in Google Cloud, while focusing on safety, security, and compliance. We align our recommendations with the requirements of the [National Institute of Standards and Technology (NIST) 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [Cyber Risk Institute (CRI)](https://cyberriskinstitute.org/) frameworks.

These best practices also support the [shared fate model](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate), where we strive to collaborate with industries to build a more secure and resilient cloud infrastructure for various workloads. The shared fate model includes deployment, operations, and risk transfer. Therefore, these recommendations focus on workload deployment and operations, particularly in relation to compliance.

We understand that implementing compliance and security isn't a simple exercise. For additional help, [contact Google Cloud Security](https://cloud.google.com/contact/security).

## Structure for security best practices

The security best practices are structured as _controls_ that you can review and implement. Each control is designed to address a different level of the AI stack. These levels are the following:

  * **Secure enterprise foundation:** core layer for authentication, access management, organization, networking, key management, secret management, logging, monitoring, alerting, security analytics, and agentic operations.
  * **AI infrastructure:** layer for containers, compute, and TPUs.
  * **Research and models:** layer for model development, and active model protection.
  * **Data management and context:** layer for data warehouses, storage, databases and sensitive data management.
  * **Tools and inference platform:** layer for the Gemini Enterprise Agent Platform, including model gardens, model builders, and agent builders.
  * **Agents and applications:** layer for Gemini Enterprise, Google Workspace, AI applications, and other software controls.



The following diagram shows how these levels stack on each other.

![Catalog AI stack.](https://docs.cloud.google.com/docs/security/images/genai-stack.svg)

The controls are structured as follows:

  * [**Recommended Identity and Access Management (IAM) roles**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/recommended-iam-groups): Recommendations for IAM roles to assign to user groups in your organization.

  * [**Secure enterprise foundation controls:**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations) These best practices let you create a secure foundation for workloads in Google Cloud.

  * [**Infrastructure controls:**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure) These best practices let you apply security controls to compute, containers, and accelerators.

  * [**Data management controls:**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management) These best practices let you apply security controls to data warehouses and data storage.

  * [**Tools and inference controls:**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/tools-inference) These best practices let you apply security controls to Gemini Enterprise Agent Platform components.

  * [**Agents and applications controls:**](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/agents-applications) These best practices let you apply security controls to applications that use generative AI.




Each recommendation is auditable and ensures a baseline of security controls is met.

## Control implementation levels

Control implementation levels are **Required** , **Recommended** , or **Optional**. The levels help identify key activities that we highly recommend you do, activities that we highly advise you consider, and activities that you might consider based on your specific requirements and goals.

The following table describes these levels.

Implementation level | Description  
---|---  
Required | Implement these guidelines for your Google Cloud environment.  
Recommended | Implement these guidelines based on specific use cases. For example, a recommended best practice might be to monitor sensitive data inside generative AI workloads if your environment includes that type of data.  
Optional | Consider additional guidelines based on your use case and risk appetite.  
  
## What's next

  * Review [Recommended user groups and Identity and Access Management roles](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/recommended-iam-groups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
