---
url: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/
title: Stellar Engine overview \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:47.645272+00:00
---

# Stellar Engine overview  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Stellar Engine overview Stay organized with collections  Save and categorize content based on your preferences. 

Stellar Engine is an infrastructure-as-code (IaC) automation framework and compliance accelerator that's designed to help public-sector customers and regulated industries bootstrap secure landing zones on Google Cloud. You can use Stellar Engine to deploy a public-sector landing zone that aligns with the strict regulatory requirements of FedRAMP High or Department of Defense (DoD) Impact Level 5 (IL5).

Stellar Engine acts as an Authorization to Operate (ATO) accelerator by automating the deployment of compliant environments with prebuilt IaC, reducing deployment times from months to hours or days. Built as a fork of the [Cloud foundation fabric repository](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric), Stellar Engine enforces compliance requirements and provides comprehensive documentation that maps implemented resources to NIST SP 800-53r5 controls.

Stellar Engine is the preferred tool for all public-sector foundational deployments that use [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs).

## Key benefits

Stellar Engine includes the following benefits:

  * **Assured Workloads companion:** serves as the preferred tool and recommended deployment process for use with Assured Workloads, implementing a landing zone that's based on regulatory best practices.
  * **Accelerated compliance:** fast-tracks ATO processes with pre-validated configurations and control mappings.
  * **IaC-driven hardening:** embeds compliance requirements directly into infrastructure, ensuring consistent and automatic implementation of controls.
  * **Flexibility and customization:** built on the Cloud foundation fabric repository, which allows for customization and enabling upstream updates.
  * **Reduced overhead:** automates landing zone deployment to reduce setup time and potential human error.



## How Stellar Engine works

Stellar Engine uses four [deployment stages](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-stages) to help ensure strict resource containment and dependency isolation:

  1. **[Stage 0 (Bootstrap)](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/0-bootstrap):** initializes core billing connections, creates administrative IaC projects, configures remote state management in [Cloud Storage](https://docs.cloud.google.com/storage/docs), and deploys global audit log sinks.
  2. **[Stage 1 (Resource management)](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/1-resman):** provisions the folder hierarchy and sets up isolated project tenants with [ Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) controls.
  3. **Stage 2 (Networking):** creates a secure hub-and-spoke [ Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) topology. This stage supports modular network patterns for [FedRAMP High](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-a-fedramp-high) and [IL5 NGFW](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-b-il5-ngfw), including deployment of Palo Alto VM-Series Next-Generation Firewalls (NGFW) for boundary traffic inspection. Boundary traffic inspection is required for IL5.
  4. **[Stage 3 (Security and audit)](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/3-security):** provisions [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) key rings to enforce customer managed encryption keys (CMEKs) and runs security lockdown scripts on service accounts.



## Target audiences and use cases

Stellar Engine enables specific critical user journeys for the following personas:

  * **Cloud platform engineers:** deploy secure, tenant-isolated landing zones using stage-specific configurations.
  * **Cybersecurity compliance leads:** generate compliance documentation (like system security plans) by mapping implemented resources to NIST controls. For more information, see [Compliance control matrix](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/compliance-controls).
  * **Network security engineers:** deploy advanced boundary protection (like Palo Alto Networks NGFWs) in high-security domains.



### Common deployment scenarios

Use Stellar Engine to create landing zones or secure mission enclaves for the following regulatory frameworks:

  * **FedRAMP High:** enable standard networking and compliance controls for civilian agencies and contractors.
  * **DoD IL5:** enable advanced boundary protection using an NGFW for Defense agencies and partners.
  * **FedRAMP Moderate:** enable compliance for state governments or regulated commercial entities.
  * **Gemini for Government or enterprise:** configure an environment for sensitive AI workloads, implementing [ Model Armor](https://docs.cloud.google.com/model-armor/overview) and private peering.



## Professional services and support

Google can help you configure your solution through direct engagement with our Impact Level and FedRAMP experts in our Public Sector Professional Services Organization. You can consult with our experts to maximize your success and accelerate your authorization.

Our experts can assist in customizing the configuration to your specific mission needs. To help create high-quality submissions and reduce the workload on your security teams, our organization can also provide associated ATO artifacts and documentation packages (such as SSP narratives and SCTM mappings).

For more information, see [Google Cloud for federal civilian agencies](https://cloud.google.com/gov/federal-civilian).

## Pricing and billing

Stellar Engine is an open-source codebase. Downstream infrastructure costs that are generated by deployed resources (such as [Compute Engine](https://docs.cloud.google.com/compute/docs), Cloud KMS, or Assured Workloads) are billed directly to your Google Cloud Billing Account as consumption charges.

## What's next

  * Read the [deployment stages](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-stages) to understand the four-stage hierarchy.
  * Explore the [compliance control matrix](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/compliance-controls) to see how controls map to NIST standards.
  * Follow the [deployment walkthrough](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-walkthrough) for step-by-step instructions.
  * Visit the [Stellar Engine GitHub repository](https://github.com/google/stellar-engine) to access the code and templates.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
