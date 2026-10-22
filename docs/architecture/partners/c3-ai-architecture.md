---
url: https://docs.cloud.google.com/architecture/partners/c3-ai-architecture/
title: C3 AI architecture on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:48.742253+00:00
---

# C3 AI architecture on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/c3-ai-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  C3 AI architecture on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-05-02 UTC

Authors: Scott Kurinskas, VP Platform Product Management, [C3 AI](https://c3.ai) | Siddharth Desai, Partner Engineer, Google

This document describes the most effective ways to deploy [C3 AI](https://c3.ai) applications on Google Cloud.

This document is intended to help systems administrators, cloud architects, and devops engineers streamline the deployment process of the C3 AI Platform on Google Cloud. It assumes that you are familiar with cloud computing concepts, [Terraform](https://www.terraform.io/), Google Kubernetes Engine (GKE), Virtual Private Cloud (VPC), and Private Service Connect (PSC).

C3 AI is an enterprise AI software provider for accelerating digital transformation. The company offers a robust platform for developing AI applications and an expanding library of turnkey solutions. With an array of more than [40 prebuilt enterprise AI applications](https://c3.ai/industries/), C3 AI caters to the critical needs of global enterprises—spanning industries like manufacturing, finance, government, utilities, and others.

## Reference architecture

The following architecture diagram shows the data flow when you deploy the C3 AI Platform on a C3 AI tenant:

![Data flowing within the C3 AI Platform on a C3 AI tenant.](https://docs.cloud.google.com/static/architecture/images/partners/c3-ai-architecture-diagram.svg)

As shown in the preceding diagram, this example architecture contains the following features:

  * **Customer-centric projects:**

Each customer is provided with a dedicated project within [C3 AI's Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). This strategic allocation enables personalized engagement while maintaining isolation between customers. This isolation helps ensure data integrity and confidentiality.

  * **VPC Service Control perimeter:**

In the customer's project, the [VPC Service Control](https://docs.cloud.google.com/vpc-service-controls/docs) perimeter helps ensure that all infrastructure components remain securely contained within a defined perimeter. Using a defined perimeter helps prevent unauthorized data leaks and helps mitigate potential risks.




In this architecture, requests to the C3 AI Platform originate securely from the customer's VPC using PSC. The requests are then load balanced and directed to GKE. As outlined in the preceding diagram, GKE serves as the processing infrastructure for the C3 AI Platform within the customer project. Enterprise data is hosted on Cloud SQL, enabling streamlined processing. Additionally, Cloud Storage offers object storage for managing application and platform configurations. Cloud Storage also supports various ancillary tasks.

## Architecture components

The preceding diagram includes the following components:

  * [**VPC network**](https://docs.cloud.google.com/vpc/docs): A VPC network provides isolated, private spaces in Google Cloud for each customer where their resources can reside, helping to ensure a secure and controlled environment for data and applications.
  * [**Cloud network address translation (NAT)**](https://docs.cloud.google.com/nat/docs): Cloud NAT facilitates outbound internet connectivity for resources within the VPC network, maintaining security while enabling external communication.
  * [**GKE**](https://docs.cloud.google.com/kubernetes-engine/docs): The foundation of C3 AI's architecture, GKE orchestrates and accelerates computations for the C3 AI Platform. It uses dedicated GKE node pools for specific accelerator types, ensuring efficient resource allocation and optimized platform performance.
  * [**Cloud Key Management Service (KMS)**](https://docs.cloud.google.com/kms/docs): Customer-Managed Encryption Keys (CMEK) from Cloud KMS help fortify data security within the customer's VPC on the C3 AI environment. CMEKs encrypt data at rest in Cloud SQL, Cloud Storage, and within GKE clusters.
  * [**Cloud SQL**](https://docs.cloud.google.com/sql/docs): C3 AI extends the capabilities of Cloud SQL to furnish on-demand databases for storing metrics and model facets. Extending these capabilities helps to enhance the versatility and data management abilities of the architecture.
  * [**PSC**](https://docs.cloud.google.com/vpc/docs/private-service-connect): Using PSC helps ensure secure communication between the customer's Google Cloud organization and their allocated project that's hosted by C3 AI. PSC establishes a private connection that doesn't rely on the public internet. That connection helps guarantee data privacy, integrity, and a seamless connection.
  * [**Cloud Storage**](https://docs.cloud.google.com/storage/docs): Reliable and secure object storage used for the management of application and platform configuration and other ancillary tasks.



The use of these components helps optimize application performance and helps adhere to the standards of C3 AI's [terms of use](https://c3.ai/legal/terms-of-use/). By deploying and managing applications on their dedicated tenant, C3 AI helps ensure that an environment has been fine-tuned to an application's unique requirements.

## Alternative approach

This section contains an alternative approach to implementing a [C3 AI](https://c3.ai) architecture on a customer tenant. The following diagram shows the C3 AI Platform deployed within a VPC that's owned by the customer within their organization:

![Data flows through a VPC that's owned by the customer and that sits within their organization.](https://docs.cloud.google.com/static/architecture/images/partners/c3-ai-architecture-diagram-alternate.svg)

In scenarios where stringent data security, compliance, or specialized operational needs come into play, C3 AI extends its support for deploying applications on the customer's tenant. This approach caters to cases where data sovereignty, regulatory demands, or unique operational frameworks require a more personalized deployment.

An example of such a case is the General Data Protection Regulation (GDPR), which is enforced by the European Union (EU). The GDPR mandates that organizations operating within EU member states adhere to strict guidelines regarding the processing and storage of personal data. This mandate includes requirements for data localization, where sensitive information might need to be stored within the geographic boundaries of the jurisdiction where the data originates.

By deploying applications on the customer's tenant, and by maintaining control over the storage and processing of their data within specific jurisdictions, organizations can help ensure compliance with GDPR and other similar regulations.

Within the customer's organization, C3 AI has its own VPC. This dedicated environment helps ensure data isolation and serves as a customized space for C3 AI's solutions. PSC facilitates the establishment of a private, secure connection between the C3 AI VPC and the customer's network. This connection doesn't use the public internet, helping to safeguard data and enabling seamless communication.

## Products used

This reference architecture uses the following Google Cloud products:

  * Google Kubernetes Engine
  * Virtual Private Cloud
  * Cloud SQL
  * Private Service Connect
  * Cloud Storage



## Design considerations

This section provides guidance to help you use this document as a starting point to develop an architecture that meets your specific requirements for security, reliability, operational efficiency, cost, and performance.

### Security, privacy, and compliance

PSC sets up a dedicated, secure, and private connection that doesn't rely on the public internet between the customer's Google Cloud organization and their allocated project that's hosted on C3 AI's Google Cloud organization. By implementing VPC Service Controls, C3 AI helps to fortify your architecture against data exfiltration. This safeguard helps to ensure that data remains within the confines of C3 AI's designated perimeters.

### Reliability

Google Cloud products help ensure reliability in the following ways:

  * The GKE cluster is a regional GKE cluster which provides a control plane [SLA](https://cloud.google.com/kubernetes-engine/sla) of 99.95%.
  * Cloud SQL instances are deployed regionally.
  * Cloud KMS keys are regional keys.
  * Cloud NAT is regional.
  * Cloud Storage is configured regionally.



## Deployment

For a comprehensive guide that explains how to install C3 AI on Google Cloud, see [C3 AI Installation Guide – Google Cloud](https://c3.ai/wp-content/uploads/2023/07/C3-AI-Installation-Guide-Google-Cloud-Platform.pdf).

## What's next

  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Scott Kurinskas](https://www.linkedin.com/in/scottkurinskas) | VP Platform Product Management (C3 AI)
  * [Siddharth Desai](https://www.linkedin.com/in/siddharthpdesai) | Partner Engineer



Other contributors: 

  * [Zach Berger](https://www.linkedin.com/in/zsberger) | Senior Cloud Infrastructure Engineer
  * [Tanvi Desai](https://www.linkedin.com/in/tanvi-desai-43184340) | Technical Account Manager
  * [Ezra Uzosike](https://www.linkedin.com/in/ezra-uzosike-3442a7) | Cloud Solutions Architect
  * [Emily Qiao](https://www.linkedin.com/in/emily-qiao) | AI/ML Customer Engineer
  * [Jiyeon Kang](https://www.linkedin.com/in/jiyeon-kang) | Customer Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-05-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-05-02 UTC."],[],[]] 
