---
url: https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide/
title: FedRAMP implementation guidance on Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:02.043970+00:00
---

# FedRAMP implementation guidance on Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  FedRAMP implementation guidance on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-02-10 UTC

This document clarifies how Google Cloud supports your FedRAMP compliance needs and directs you to resources for configuring services to meet FedRAMP requirements. This document is designed for security, compliance, and IT personnel who are responsible for FedRAMP implementation and compliance on Google Cloud.

According to the shared [responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility), you're responsible for understanding your compliance and security requirements and configuring your Google Cloud environment appropriately. When implementing FedRAMP support, we highly recommend that you seek independent legal advice relating to your FedRAMP responsibilities.

## About FedRAMP

The [Federal Risk and Authorization Management Program (FedRAMP)](https://www.fedramp.gov/) framework was established by the US Federal government to standardize the security assessment, authorization, and continuous monitoring of cloud products and services across all government agencies. In 2022, Congress codified FedRAMP as a "Government-wide program that provides a standardized, reusable approach to security assessment and authorization for cloud computing products and services that process unclassified information used by agencies."

In 2025, FedRAMP started a significant program revision as part of the [FedRAMP 20x](https://www.fedramp.gov/20x/) initiative. These changes aim to adopt automated monitoring and enforcement of commercial security best practices to meet minimum security requirements for federal information systems. FedRAMP is transitioning away from costly, inefficient, manually compiled documentation towards industry-led, data-driven security reporting. For information about how Google is supporting the FedRAMP 20x initiative, see [Accelerating FedRAMP 20x: How Google Cloud is automating compliance](https://cloud.google.com/blog/topics/public-sector/accelerating-fedramp-20x-how-google-cloud-is-automating-compliance).

FedRAMP is based on the [National Institute of Standards and Technology (NIST) SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) standard, augmented by FedRAMP controls and control enhancements. All federal agency cloud deployments and service models, other than certain on-premises private clouds, must meet FedRAMP requirements at the appropriate risk impact level (Low, Moderate, or High) based on the [NIST FIPS 199](https://csrc.nist.gov/pubs/fips/199/final) guidelines. The number of [NIST SP 800-53 controls](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home) in the corresponding baseline increases as the impact level increases. For example, the FedRAMP Moderate baseline has 325 controls whereas the FedRAMP High baseline has 421 controls.

FedRAMP is an assessment and authorization program, not a one-time certification or accreditation. It includes continuous monitoring to ensure the effectiveness of security controls in a cloud service offering, adapting to evolving threat landscapes and system environment changes.

## Google Cloud FedRAMP authorization

The FedRAMP Board (formerly known as the Joint Authorization Board or JAB) is the primary governing body for FedRAMP. The FedRAMP Board includes CIOs from the Department of Defense (DoD), Department of Homeland Security (DHS), and General Services Administration (GSA).

The FedRAMP Board has issued a FedRAMP High Provisional Authority to Operate (P-ATO) to Google Cloud and the underlying Google Common Infrastructure (GCI). The FedRAMP High authorization represents the highest bar for FedRAMP compliance.

Following FedRAMP 20x improvements, the GSA became the authorizing agency for Google Cloud, which routinely submits additional services to the GSA for FedRAMP High authorization. The FedRAMP Moderate control baseline is a subset of the FedRAMP High control baseline. Therefore, a FedRAMP High authorization provides comprehensive coverage for all FedRAMP Moderate control requirements.

For more information about Google Cloud FedRAMP compliance, see [FedRAMP compliance](https://cloud.google.com/security/compliance/fedramp).

## Services in audit scope

Google Cloud maintains a comprehensive FedRAMP High P-ATO that covers more than 150 cloud services. This scope lets you build a wide range of applications on Google Cloud and pursue your FedRAMP ATO by inheriting security controls from the underlying Google Cloud platform. For example, you can use machine learning (ML) models and artificial intelligence (AI) services, including AI agents, generative AI, and multimodal AI in your Google Cloud deployments.

For more information about the Google Cloud FedRAMP audit scope, see [FedRAMP and DoD compliance scope](https://docs.cloud.google.com/docs/security/compliance/fedramp-dod-compliance-scope) and the [ Google Cloud FedRAMP Marketplace](https://marketplace.fedramp.gov/products/FR1805751477).

### AI and LLMs

Google Cloud can help you meet your FedRAMP compliance requirements for workloads that include ML models and AI applications. You can use Google Cloud FedRAMP authorized services such as [Generative AI on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs) and [ Gemini Enterprise Agent Platform Inference: Batch and Online](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-predictions) to interact with more than 200 first-party, third-party, and open-source large language models (LLMs) that are available in our [Model Garden](https://cloud.google.com/model-garden). For more information, see [Models supported by Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models).

Individual LLMs aren't independently authorized under FedRAMP and there's no record of their authorization in the FedRAMP Marketplace. Instead, the Marketplace reflects authorizations for cloud services like Generative AI on Agent Platform and Agent Platform Inference: Batch and Online, which Google submits for approval. However, the underlying cloud infrastructure used for LLM deployment must adhere to FedRAMP compliance requirements, including the infrastructure that's used for continuous monitoring. This requirement is fulfilled for Google-managed models, such as Google first-party LLMs (for example, the [Gemini family of models](https://ai.google.dev/gemini-api/docs/models)) and partner models from Anthropic, all of which support [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/supported-models). Consequently, using FedRAMP High authorized Agent Platform services allows for interaction with these supported models in a FedRAMP High environment.

Google continues to implement monitoring provisions for more LLMs that are hosted on Google-managed infrastructure. Although Google is responsible for authorizing the serving infrastructure and custom-built containers to deploy open-source models, security of open-source models is your responsibility.

For more information about self-deployed LLMs, see [Overview of self-deployed models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/self-deployed-models). If you deploy LLMs into your own Google Cloud tenant infrastructure, ensure that your FedRAMP ATO assessment covers that infrastructure, not the individual LLMs. For example, you must satisfy continuous monitoring requirements for the Google Cloud infrastructure that you provision for LLM deployment. You can collaborate with your third-party assessment organization (3PAO) and Google to pursue your ATO.

## Achieving your FedRAMP ATO

Based on ongoing [FedRAMP 20x changes](https://www.fedramp.gov/20x/faqs/), the available path to FedRAMP authorization is the [Rev. 5 Agency ATO](https://www.fedramp.gov/rev5/agency-authorization/). You must work with Google and your 3PAO to complete the steps that lead to an ATO. For information about the agency ATO process, including links to important resources such as the agency authorization playbook, see the [FedRAMP website](https://www.fedramp.gov/rev5/agency-authorization/).

If you want to use Google Cloud services to meet your FedRAMP High compliance obligations, you must use [Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/supported-products). The FedRAMP Moderate control baseline is a subset of the FedRAMP High control baseline. Therefore, if you want a FedRAMP Moderate ATO for a solution that's deployed on Google Cloud, you can use any Google Cloud service that's FedRAMP High authorized in your FedRAMP Moderate authorization boundary. You'll need to assess fewer controls for a FedRAMP Moderate ATO compared to the controls that you must assess for FedRAMP High ATO.

To help with your FedRAMP ATO, Google can provide you with the following Google Cloud FedRAMP High compliance documentation under a non-disclosure agreement (NDA):

  * **Customer Responsibility Matrix (CRM)** : detailed descriptions of your responsibilities when implementing the NIST SP 800-53 controls in the FedRAMP High control baseline.
  * **System Security Plan (SSP)** : the security authorization boundary and how the system is architected. This document also provides in-depth descriptions of NIST SP 800-53 control requirements and Google Cloud control implementation details that are applicable to the FedRAMP High control baseline.



Our [sales team](https://cloud.google.com/contact) or your Google Cloud representative can help provide access to this documentation. If you're a federal government agency, you can also request Google's FedRAMP package using the [FedRAMP package access request form](https://www.fedramp.gov/rev5/documents-templates/).

## Guidance and automation

Google provides guidance documentation and automation solutions to help you with your FedRAMP compliance obligations, as described in this section.

### Control mapping guides

Unlike the comprehensive Google Cloud FedRAMP High CRM, control mapping guides (CMGs) are service specific. These guides provide detailed control coverage for Google Cloud services so that you can configure the services to meet FedRAMP High requirements. CMGs address the relevant NIST SP 800-53 controls that require technical configuration by you. CMGs also clarify the steps you must follow for a particular service (and any supporting Google Cloud and Google Workspace services), to help ensure that these responsibilities are transparent.

CMGs are available for select Google Cloud services, including BigQuery, Data Studio Pro, Generative AI on Agent Platform, Agent Search on Agent Platform, Cloud Logging, Compute Engine, Identity and Access Management (IAM), and more. Contact our [sales team](https://cloud.google.com/contact) or your Google Cloud representative to obtain access to this documentation under a non-disclosure agreement (NDA).

### FedRAMP High implementation guides

FedRAMP High implementation guides are intended to cover service-specific APIs that are in FedRAMP High scope, including impacted service features and data fields that are suitable for storing protected data. For example, these guides describe service-specific APIs that meet FedRAMP High requirements and provide extra configuration details that you use with the particular Google Cloud service for FedRAMP High workloads. These configurations aren't enforced by default and must be managed by you.

FedRAMP High implementation guides are available for select Google Cloud services, including Apigee, BigQuery, Cloud Key Management Service, Logging, Google Kubernetes Engine (GKE), Generative AI on Agent Platform, Agent Search on Agent Platform, Cloud Storage, and more. Contact our [sales team](https://cloud.google.com/contact) or your Google Cloud representative to obtain access to this documentation under an NDA.

## Data residency and SA-9(5) compliance

When deploying your application on Google Cloud, FedRAMP data residency requirements are mandated only by the FedRAMP High control baseline. To enforce these requirements, you must choose the [Assured Workloads Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/supported-products). If you're pursuing a FedRAMP Moderate authorization and choose the Assured Workloads Data Boundary for FedRAMP Moderate, you won't have data residency controls as the requirements don't apply to you.

Google Cloud provides [data residency contractual commitments](https://cloud.google.com/terms/data-residency) for regional services, which enable you to configure a service to use a specific data location. These commitments help ensure that your FedRAMP High data is stored in a United States region, remains in the United States, and won't be moved to another region outside of the United States. Some examples of [FedRAMP High data](https://www.fedramp.gov/understanding-baselines-and-impact-levels/) include data that belongs to law enforcement, emergency services, financial services, healthcare and public health systems, or any of the 16 [critical infrastructure sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).

Certain Google Cloud services are non-regional or global by design and they don't let you specify the region where the service is deployed. This design approach is needed for global services to operate correctly. Some of these non-regional or global services aren't implicated in the processing, transmission, or storage of your FedRAMP High data. Data residency capabilities for non-regional or global services are limited.

In July 2020, FedRAMP released an update to the FedRAMP High baseline SA-9(5) control to restrict the geographic location of high-impact data information services to the United States or territories under US jurisdiction. After this update, some Google Cloud services were flagged in the [FedRAMP Marketplace](https://marketplace.fedramp.gov/products/FR1805751477) with an asterisk and the following clarification: "Services that are denoted with an asterisk (*) do not meet the SA-9(5) requirement. Please review the JAB P-ATO letter for more information."

Some Google Cloud services that were flagged in the FedRAMP Marketplace as not meeting the SA-9(5) requirements have not yet been reviewed by our 3PAO for resubmission to the GSA with updated SA-9(5) evidence. Google is actively pursuing these submissions aimed at removing SA-9(5) clarifications from the FedRAMP Marketplace. For more information about the status for these services, see the **SA-9(5)** tab in the FedRAMP High CRM document.

While the process of re-assessing FedRAMP High authorized Google Cloud services with the SA-9(5) clarification is underway, Google recommends that you implement mitigating controls as described in the [RMF guidelines](https://csrc.nist.gov/pubs/sp/800/37/r2/final) to address FedRAMP High data geographic restrictions. For example, you can use data encryption to establish sole control over FedRAMP High data, as explained in the rest of this section.

### Digital sovereignty and data residency

Google emphasizes digital sovereignty, a concept that secures data regardless of physical location. This approach relies on [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) and [software-defined community cloud](https://cloud.google.com/blog/products/identity-security/software-defined-community-cloud-new-way-government-cloud). It contrasts with conventional physical sovereignty that emphasizes data residency, Google Cloud digital sovereignty controls provide enhanced data protection.

Digital sovereignty grants you authority over data protection, eliminating the need to depend on assurances from cloud providers or third-party assessors. Digital sovereignty implies that you have sole control over access to your data through exclusive ownership of data encryption keys.

In accordance with the [RMF guidelines](https://csrc.nist.gov/pubs/sp/800/37/r2/final), Google recommends that you implement mitigating controls to address the risk of FedRAMP High data being accessed while transiting the networking infrastructure or during potential storage in a non-US cloud region. The primary mechanism for access restriction is data encryption in transit and at rest.

To help protect your FedRAMP High data and restrict access only to your authorized users, you can use customer-managed encryption keys for data encryption at rest. Google Cloud also provides data encryption in transit. The following sections describe the data encryption technologies that are available to you in Google Cloud. Data encryption helps prevent your FedRAMP High data from being read while in transit or accessed by other tenants and Google personnel while stored at rest.

### Customer-managed encryption keys

[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) in [( Cloud KMS)](https://docs.cloud.google.com/docs/security/key-management-deep-dive) give you ownership and control of the keys that protect your data at rest in Google Cloud. A Google Cloud service that can use your keys has a [_CMEK integration_](https://docs.cloud.google.com/kms/docs/cmek). You can manage these CMEKs directly or through [ Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview). Services that support CMEK integrations use your Cloud KMS keys to encrypt or wrap your data encryption keys (DEKs). Wrapping DEKs with key encryption keys (KEKs) is called [_envelope encryption_](https://docs.cloud.google.com/kms/docs/envelope-encryption). For more information, see [Recommended practices for using CMEKs](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices). For a list of services that support CMEK, see [Compatible services](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_integrations).

With [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm), you can use encryption keys that you manage externally outside Google Cloud to help protect data within Google Cloud. You can protect data at rest in [supported CMEK integration services](https://docs.cloud.google.com/kms/docs/ekm#supported_services) or by calling the Cloud Key Management Service API directly.

Google offers the [following assurances](https://docs.cloud.google.com/docs/security/key-management-deep-dive#security-of-key-materials) regarding the security of encryption keys in Cloud KMS:

  * Decrypted key material can't be exported or viewed through the API interface or another user interface.
  * Google personnel can't access unencrypted customer key material. Moreover, key material is encrypted with a KMS master key in Keystore, and the KMS master key isn't accessible to Google personnel.
  * On a [Hardware Security Module (HSM)](https://docs.cloud.google.com/docs/security/cloud-hsm-architecture#strict_security_procedures_safeguard_hsm_hardware), key material is never accessed in a decrypted state by Cloud KMS API jobs. HSMs made available to you in Google Cloud are FIPS 140 validated.
  * Google system operators are prevented from accessing, using, or extracting customer key material while performing their duties, as defined in standard operating procedures.



[FIPS 140 validation](https://cloud.google.com/security/compliance/fips-140-2-validated) is required for FedRAMP authorization. For example, the [SC-13 Cryptographic Protection](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-13) control mandates the use of FIPS 140 validated cryptography or NSA-approved cryptography. Google provides you with crypto modules for data encryption at rest and in transit that have FIPS 140 validation in place.

### Data encryption at rest

Google Cloud [encrypts data at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) by default. Google Cloud provides transparent server-side encryption for storage services using a FIPS 140 validated AES-256 symmetric block cipher. You can also create your own encryption keys that you manage with Cloud KMS and store in cloud-based or external HSMs.

[Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) lets you host encryption keys and perform cryptographic operations in a cluster of FIPS 140 validated HSMs. Cloud HSM uses Cloud KMS as its frontend to give you access to CMEK integration capabilities and other features that Cloud KMS provides. Because Google Cloud employs strong [FIPS 140 validated](https://cloud.google.com/security/compliance/fips-140-2-validated) cryptography, your encrypted data is accessible only by users who possess your CMEK.

Google Cloud also supports customer-managed keys for [encrypting disks](https://docs.cloud.google.com/compute/docs/disks/disk-encryption) that are attached to virtual machines. Moreover, Google Cloud supports [client-side encryption](https://docs.cloud.google.com/storage/docs/encryption/client-side-keys) where you can encrypt data within your own application environment prior to sending it to the cloud.

### Data encryption in transit

Google Cloud provides support for data encryption in transit, as follows:

  * Transparent encryption occurs across the Google-controlled networking backbone of network traffic between data center regions and availability zones. This encryption is implemented at the physical data link layer (Layer 2 in the networking stack) using [Media Access Control Security (MACsec)](https://1.ieee802.org/security/802-1ae/).
  * [VM-to-VM traffic](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends) within a Virtual Private Cloud (VPC) network and peered VPC networks is transparently encrypted.
  * At the application layer, Google lets you use [Transport Layer Security (TLS)](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) for data encryption in transit. Moreover, service endpoints support TLS to create a secure HTTPS connection when making API calls.
  * Connections between VPC and your on-premises infrastructure are available using Cloud VPN, which creates a [secure encrypted tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) across the Internet or through direct private circuits.



Data encryption in transit includes encryption in transit between the end user and Google, and encryption in transit within Google networks. For more information, see [Encryption in transit for Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).

## What's next

To get started with FedRAMP authorization for your Google Cloud deployment, review the following:

  * [FedRAMP and DoD compliance scope](https://docs.cloud.google.com/architecture/security/fedramp-dod-compliance-scope)
  * [Configure networks for FedRAMP and DoD in Google Cloud](https://docs.cloud.google.com/architecture/configure-networks-fedramp-dod-google-cloud)
  * [FedRAMP compliance offering on Google Cloud](https://cloud.google.com/security/compliance/fedramp)
  * [Meet regulatory, compliance, and privacy needs](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs)
  * [Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
  * [Data Boundary via Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Supported products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products)
  * [FedRAMP Marketplace entry for Google Cloud](https://marketplace.fedramp.gov/products/FR1805751477)
  * [FedRAMP 20x Initiative](https://www.fedramp.gov/20x/)
  * [FedRAMP Rev 5 Agency Authorization](https://www.fedramp.gov/rev5/agency-authorization/)
  * [FedRAMP documents and templates](https://www.fedramp.gov/rev5/documents-templates/)
  * [NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#/800-53)
  * [NIST SP 800-37: Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy](https://csrc.nist.gov/pubs/sp/800/37/r2/final)
  * [NIST FIPS 199: Standards for Security Categorization of Federal Information and Information Systems](https://csrc.nist.gov/pubs/fips/199/final)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-10 UTC."],[],[]] 
