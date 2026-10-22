---
url: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-stages/
title: Stellar Engine deployment stages \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:46.682712+00:00
---

# Stellar Engine deployment stages  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-stages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Stellar Engine deployment stages Stay organized with collections  Save and categorize content based on your preferences. 

Stellar Engine is designed with layered stages to implement dependency isolation, security containment, and repeatable deployments. The repository is divided into four sequential stages, and each stage is responsible for a specific domain of the landing zone.

## Stage 0: Bootstrap

The [Bootstrap stage](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/0-bootstrap) initializes the minimum viable infrastructure that's required to manage the deployment process itself, acting as the root of trust for the IaC pipeline.

This stage uses the principle of least privilege for the initial deployer service account and strict separation of administrative hierarchy.

The objective of this stage is to create the following:

  * Administrative foundation
  * Remote state management
  * Initial security perimeter



The following resources are created:

  * Core Billing Account connections and budget alerts
  * Dedicated administrative IaC project to host deployment service accounts
  * Locked-down [Cloud Storage](https://docs.cloud.google.com/storage/docs) buckets for Terraform remote state with object versioning enabled
  * Global Audit Log sinks that are integrated with a central [Cloud Logging](https://docs.cloud.google.com/logging/docs) bucket
  * Essential Contacts configuration to help ensure security, technical, and billing notifications are only routed to authorized agency domains



## Stage 1: Resource management

The [Resource management stage](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/1-resman) creates the organization hierarchy, access boundaries, and tenant isolation.

The objective of this stage is to define the folders, projects, and custom [ Identity and Access Management](https://docs.cloud.google.com/iam/docs) roles that are required for specific regulatory frameworks.

This stage uses the separation of duties principle across different administrative domains and strict resource isolation.

The following resources are created:

  * Compliance-aligned folder hierarchy (for example, `Prod`, `Non-Prod`, `Security`, and `Shared`)
  * Dedicated tenant projects that are isolated by environment and function
  * Granular IAM role bindings and custom roles to enforce least privilege



## Stage 2: Networking

The Networking stage provisions the communication pathways, boundary security controls, and hybrid connectivity. Stellar Engine supports multiple networking modules, including [FedRAMP High](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-a-fedramp-high) and [IL5 NGFW](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-b-il5-ngfw).

The objective of this stage is to establish secure connectivity patterns, packet filtering, and ingress or egress controls.

This stage focuses on strict boundary protection, centralized traffic inspection, and deep packet filtering. After you run this stage, integrate a SIEM solution to monitor the resources. Segment your SIEM in a separate Google Cloud project and on a separate VPC from where it is collecting data.

The following resources are created:

  * Hub-and-spoke [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) topology or [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center) architectures that minimize public exposure
  * VPC Peering, [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn), or Dedicated Interconnect connections for hybrid workloads
  * Standard VPC routing or advanced service chaining using Palo Alto VM-Series Next-Generation Firewalls (NGFW) (required for DoD IL5 enclaves) in a specialized Inspection VPC



## Stage 3: Security and audit

The [Security and audit stage](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/3-security) applies encryption enforcements, final lockdowns, and service accountability.

The objective of this stage is to enhance data protection, audit traceability, and cryptographic sovereignty.

This stage focuses on sovereignty-at-rest, sovereignty-in-use, and strict cryptographic isolation of data.

The following resources are created:

  * [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) (Cloud KMS) key rings and keys to satisfy customer-managed encryption keys (CMEK) requirements for all storage services
  * Security lockdown scripts and Organization Policy Service constraints that are applied to the service accounts that are used during deployment
  * Dead-letter topics and alerts for failed audit log ingestion



## Deployment principles

The following table describes the principles that Stellar Engine uses for its deployment process.

Principle | Description  
---|---  
State isolation |  Terraform state files are strictly segregated by stage. For example, a bug or state corruption in Stage 2 cannot access or corrupt the core state or credentials of the Stage 0 or Stage 1 stages.  
Module version pinning |  Blueprints reference modular dependencies using pinned Git tags or commit hashes. Pinning helps ensure that upstream changes in the module registry aren't automatically introduced into target environments without explicit review.  
Impact containment |  Updates are executed locally within stage directories. Impact containment helps ensure that a code change to firewall rules in Stage 2 doesn't affect Cloud KMS keys in Stage 3.  
Failure containment |  Cloud Storage state buckets are configured with object versioning enabled. If a bad code change or manual state edit corrupts the state file, the file can be immediately restored to a previous version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
