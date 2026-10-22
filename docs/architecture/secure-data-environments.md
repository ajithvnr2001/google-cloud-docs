---
url: https://docs.cloud.google.com/architecture/secure-data-environments/
title: Secure data environments in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:02.223286+00:00
---

# Secure data environments in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/secure-data-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Secure data environments in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-04-16 UTC

This document provides a high-level architecture for securing massive datasets that contain sensitive data, including personally identifiable information (PII), in Google Cloud. The architecture is designed to help secure sensitive data against accidental exposure and malicious exfiltration. It's intended for Data Compliance Officers and Cloud Security Engineers who are familiar with foundational cloud networking and identity concepts. The architecture highlights the use of network perimeters that explicitly override permissive Identity and Access Management (IAM) settings to prevent unauthorized public access, even when resources are misconfigured.

The deployment section of this document provides a Terraform code sample to self-deploy this perimeter and simulate a public access block.

## Architecture

The following architecture diagram illustrates a robust, multi-layered data protection strategy on Google Cloud. It effectively shows how data moves from an unstructured state into a secured, governed environment.

![Cloud KMS Autokey and Sensitive Data Protection help to secure data in BigQuery and Cloud Storage.](https://docs.cloud.google.com/static/architecture/images/secure-data-environments-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/secure-data-environments-architecture.svg)

The preceding diagram shows how each Google service provides security for the data from the initial data upload through data access:

  1. A user with appropriate IAM permissions uploads data to the BigQuery or Cloud Storage data storage service. The storage services are configured to use customer-managed encryption keys (CMEK) and Cloud KMS Autokey.
  2. The service encrypts the data by using a CMEK that's fetched from Cloud KMS Autokey.
  3. Sensitive Data Protection continually inspects, classifies, and de‑identifies sensitive data in the repository. To de‑identify sensitive data, Sensitive Data Protection masks the data by using templates and options that you configure.
  4. The storage services are inside a VPC Service Controls perimeter, which blocks data access from outside the perimeter. To grant access permission to designated users and systems (IAM [principals](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow)), you use an Access Context Manager [access level](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) template. The designated principals can then access data that's inside the perimeter.
  5. VPC Service Controls denies access to anyone who isn't specified in the access level template.



## Products used

  * [ VPC Service Controls](https://cloud.google.com/security/vpc-service-controls): A managed networking functionality that minimizes data exfiltration risks for your Google Cloud resources.
  * [ Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection): A fully managed service that's designed to help you discover, classify, and protect your valuable data assets, including personally identifiable information (PII).
  * [ Cloud Key Management Service (Cloud KMS)](https://cloud.google.com/security/products/security-key-management): A service that lets you create, import, and manage cryptographic keys and perform cryptographic operations in a single centralized cloud service.
  * [ Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs): A service that lets you define fine-grained, attribute-based access control policies for your projects and resources in Google Cloud. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Use cases

This architecture provides a robust security framework for handling sensitive data in Google Cloud. It focuses on data protection, access control, and exfiltration prevention. The architecture helps to establish a secure environment for sensitive data by combining strong encryption with automated data de‑identification and network perimeter controls. This implementation helps to ensure that data is encrypted with customer-controlled keys (CMEKs), that sensitive information is automatically detected and masked, and that access is strictly confined and contextually managed. These measures help to significantly mitigate data exfiltration risks.

The following are examples of use cases for the architecture that's described in this document:

  * **Regulated industries (finance, healthcare, public sector)** : Industries that are heavily regulated require security frameworks that help achieve compliance and data security. In order to achieve compliance and protect sensitive customer data, it's crucial to ensure that data is secured at rest, that sensitive data is discovered, and that access controls are in place. We recommend that regulated industries implement this design to help achieve data compliance.
  * **Unregulated industries** : Industries that aren't subject to data regulations can benefit from implementing a robust security framework. It's important to prevent sensitive data from being exposed, to store data securely, and to have policies in place that control access to data. The architecture in this document can help an unregulated industry to achieve the same level of security as a heavily regulated industry. We recommend that unregulated industries implement this design as a best practice.



## Design considerations

  * To analyze log violations and prevent accidental lockouts of production workloads, always implement VPC Service Controls in [dry-run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) first.
  * To ensure that trusted corporate networks and administrative devices can interact with protected resources, define precise [Access Context Manager policies and levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-policies).
  * To quickly and cost-effectively identify where sensitive data _might_ reside, run Sensitive Data Protection with sampling enabled on large datasets. For more information, see the following resources:

    * [Inspect BigQuery for sensitive data with sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-bigquery-with-sampling)
    * [Inspect Cloud Storage with sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-gcs-with-sampling)

To ensure comprehensive protection on those datasets, run a comprehensive scan after you inspect data with sampling. For more information, see [Overview of sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

  * To help ensure automated encryption enforcement, before you create resources, [enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey) at the folder or project level.




## Deployment

To deploy a sample implementation of this architecture, use the [data-security code sample](https://github.com/GCP-Architecture-Guides/data-security) that's available in GitHub.

## What's next

  * To gain experience with Cloud KMS Autokey, see the [Encrypt Resources Easily with Cloud KMS Autokey](https://codelabs.developers.google.com/codelabs/cloud-kms-autokey#0) Codelab.
  * Learn how to use [VPC Service Controls with Access Context Manager](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Manish Gaur](https://www.linkedin.com/in/manishkgaur/) | Security Architect
  * [James Meyer](https://www.linkedin.com/in/james-meyer-89377b1b/) | Security Architect



Other contributors: 

  * [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer
  * [Susan Wu](https://www.linkedin.com/in/susanwu88) | Outbound Product Manager
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Biodun Awojobi](https://www.linkedin.com/in/bioawojobi/) | Head of Customer Engineering, Security and Compliance



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
