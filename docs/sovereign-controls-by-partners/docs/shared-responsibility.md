---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/shared-responsibility/
title: Shared responsibility in Sovereign Controls by Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:36.889563+00:00
---

# Shared responsibility in Sovereign Controls by Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs)
  * [ Guides ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/overview)



Send feedback 

#  Shared responsibility in Sovereign Controls by Partners Stay organized with collections  Save and categorize content based on your preferences. 

This page describes shared responsibility in Sovereign Controls by Partners. For general information about shared responsibility in Google Cloud, see [Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).

## Shared responsibility for data

You're the expert in knowing the security and regulatory requirements for your business and knowing the requirements for protecting your confidential data and resources. When you run your workloads on Google Cloud, you must identify the security controls that you need to configure in Google Cloud to help protect your confidential data and each workload. To decide which security controls to implement, you must consider the following factors:

  * Your regulatory compliance obligations
  * Your organization's security standards and risk management plan
  * Security requirements of your customers and your vendors



The protection of your data is a primary design consideration for all of Google's infrastructure, products, and personnel operations. Google Cloud provides strong security for many data types, including [Customer Data](https://cloud.google.com/terms/data-processing-addendum) and [Service Data](https://cloud.google.com/terms/cloud-privacy-notice). However, if your workloads must meet specific regulatory requirements or are subject to national standards that require elevated security controls, your internal policies may differ from default configuration options. If you have such requirements, we recommend adopting additional tools and techniques to help maintain your required level of compliance and enable your team to follow the best practices of data management and overall cybersecurity management.

## Configure Google Cloud and Sovereign Controls by Partners for shared responsibility

The following areas are customer responsibilities as a user of any public cloud:

  * Understanding what portions of your data have different compliance and security requirements. Most cloud customers have some IT infrastructure which requires general commercial security, and some customers have specific data, such as health data, which must meet a higher compliance requirement. Sovereign Controls by Partners can help to meet those higher compliance requirements. Place any sensitive or regulated data with specific access or residency requirements inside appropriate Sovereign Controls by Partners folders or projects and keep it there.
  * Configuring Identity and Access Management (IAM) to ensure that the contents of your organization are accessed and modifiable by the appropriate personnel.
  * Creating and organizing your organizational hierarchy such that it does not expose personal data.
  * Ensuring you have read all documentation to understand and follow best practices.
  * Sharing information prudently during technical support sessions and troubleshooting, and **not placing or sharing sensitive or regulated data** outside compliant Sovereign Controls by Partners folders.



The scope of sensitive or regulated data can vary depending on many factors including regulations you or your customers are subject to and can include:

  * Account information
  * Health information
  * Personal identifiers for customers or users
  * Cardholder data
  * ID numbers



## Google's responsibilities in the shared responsibility model

In the shared responsibility partnership between Google and customers, Google takes responsibility for the foundational elements and infrastructure of building a successful cloud business, some of which rely on customers undertaking their responsibilities to configure Google Cloud to adequately protect their data. Examples of Google's responsibilities include:

  * Applying [default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [infrastructure controls](https://docs.cloud.google.com/docs/security/infrastructure/design).
  * Enforcing the IAM policies that you set to restrict workload administration and data access to the identities that you identify.
  * Configuring and enforcing any customer-selected Sovereign Controls by Partners controls associated with your selected compliance regime, for the protected data types in the resources you have configured it for. This includes restrictions on where data will be stored and which Google employees can have access to your data in the course of their appropriate business activities.
  * Providing configurations and controls through Sovereign Controls by Partners for regulated industries and locationally sensitive data.
  * Providing [Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) and [resource settings](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) that let you configure policies throughout your hierarchy of folders and projects.
  * Providing [Policy Intelligence tools](https://docs.cloud.google.com/policy-intelligence/docs/overview) that give you insights on access to accounts and resources.



## Configuration specific to Europe and the EU

When using Sovereign Controls by Partners, customers have additional technical controls on top of the GDPR assurances made on Google Cloud that they can use to adjust their data residency and security controls as part of their compliance efforts. Some of these controls include:

  * An EU data boundary as further described in [Data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency).
  * Support routing to EU persons in EU locations, including subprocessors.
  * Visibility into Administrative Access requests and accesses.
  * Policy-driven access approvals (Sovereign Controls only).
  * Custom options for data encryption and key management.



## Examples of common fields that are not recommended for sensitive or regulated data

We strongly recommend all regulated and sovereign customers to exercise caution when inputting data into Google Cloud services. It's critical to avoid adding sensitive or regulated data into common input fields that may not be protected by technical controls or aren't included in the Sovereign Controls by Partners technical control boundary. This practice is necessary to maintain compliance with regulatory requirements and safeguards your sensitive or regulated information. To assist you, we compiled a list of examples across various Google Cloud services where extra vigilance is required.

Avoid placing your sensitive or regulated data in the following common fields:

  * Resource names and IDs
  * Project or folder names and IDs
  * Any description fields or labels
  * Log-based metrics
  * VM sizes and similar service configurations
  * URIs or file paths
  * Timestamps
  * User IDs
  * Firewall rules
  * Security scanning configurations
  * Customer IAM policies



## What's next

  * Learn more about [Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
