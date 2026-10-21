---
url: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/compliance-controls/
title: Stellar Engine compliance control matrix \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:42.344633+00:00
---

# Stellar Engine compliance control matrix  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/compliance-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Stellar Engine compliance control matrix Stay organized with collections  Save and categorize content based on your preferences. 

Stellar Engine is an Authorization to Operate (ATO) accelerator that maps implemented Terraform resources directly to compliance control families. It is designed to significantly reduce the documentation burden for public sector agencies and regulated industries.

For a list of supported frameworks with [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs), see [Common deployment scenarios](https://docs.cloud.google.com/docs/security/compliance/stellar-engine#deployment-scenarios).

## NIST SP 800-53r5 mapping

Stellar Engine provides a comprehensive System Security Plan (SSP) template and a Security Control Traceability Matrix (SCTM) that map implemented resources to NIST SP 800-53r5 controls.

To help provide comprehensive coverage for ATO packages, Stellar Engine provides mapping for the following critical control families:

  * **Access Control (AC):** enforced using least-privilege [Identity and Access Management](https://docs.cloud.google.com/iam/docs) role bindings, service account lockdowns, and strict folder-level access boundaries.
  * **System and Communications Protection (SC):** satisfied using hub-and-spoke [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) topologies, boundary firewalls (including Palo Alto Next-Generation Firewall support), communication segregation, and integration with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).
  * **Identification and Authentication (IA):** managed using IAM hierarchy and integration with organization-level identity providers, enforcing modern authentication mechanisms.
  * **Audit and Accountability (AU):** fulfilled through global audit log sinks, central logging storage (for example, using [BigQuery](https://docs.cloud.google.com/bigquery/docs) or [ Cloud Storage](https://docs.cloud.google.com/storage/docs)), and immutable retention policies to ensure traceability.
  * **Configuration Management (CM):** addressed by infrastructure as code (IaC) itself, ensuring consistent deployments and enabling automated drift detection.
  * **Contingency Planning (CP):** supported by localized state management with object versioning enabled in Cloud Storage buckets, enabling rapid recovery of configuration state.



## Deliverables for ATO acceleration

You can use Stellar Engine to gain access to the following compliance artifacts:

  * **Compliance Mapping Spreadsheet (SCTM):** prepackaged templates matching controls directly to Terraform configurations.
  * **System Security Plan (SSP) Templates:** baseline narratives for FedRAMP High and DoD IL5 enclaves.
  * **Path to Authorization Framework:** step-by-step guidance on how to use Stellar Engine deliverables to submit for ATO approval.



## Embedded compliance and shared responsibility

By embedding compliance requirements directly into IaC, Stellar Engine helps ensures that foundational controls are implemented consistently and automatically, reducing the risk of drift or human error.

### Shared responsibility

Although Stellar Engine can accelerate the ATO process, you or your Independent Software Vendor (ISV) retains responsibility for application-level encryption (for example, Additional Authenticated Data (AAD)), identity provider integration, operational key rotation, and other application-specific safeguards. For more information about the shared responsibility model, see the [Google Cloud FedRAMP Implementation Guide](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide) or the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility).

### Data residency

Stellar Engine relies on the [(`gcp.resourceLocations`) organization policy constraint](https://docs.cloud.google.com/organization-policy/restrict-locations) to restrict resource creation to authorized regions. This constraint is implemented by default in Stellar Engine and Assured Workloads and is a foundational requirement for FedRAMP High and DoD IL5.

## What's next

  * Contact [Google Cloud Public Sector Professional Services Organization](https://docs.cloud.google.com/docs/security/compliance/stellar-engine#professional-services) for help configuring your deployment and accessing ATO artifacts and documentation packages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
