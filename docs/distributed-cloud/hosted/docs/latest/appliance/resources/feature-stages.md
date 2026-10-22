---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/feature-stages/
title: Feature stages \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:00.007029+00:00
---

# Feature stages  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/feature-stages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Feature stages Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the lifecycle stages that Google Distributed Cloud (GDC) air-gapped appliance features might transition through, such as the following launch stages:

  * Preview
  * General Availability (GA)
  * Accredited



There are also the following end-of-life stages:

  * Deprecated
  * Decommissioned



## Launch stages

GDC air-gapped features have unique standards that must pass increased security requirements. Because of these heightened standards, some features might require going through an accreditation process to satisfy a set of compliance requirements. For these features that need to go through an accreditation review by a third-party entity, they can be certified as production ready, but might not be available to use.

The lifecycle of GDC air-gapped features allows some features to be released to a subset of customers, which lets them test and approve them for their unique use cases.

The following sections describe the stages of a GDC air-gapped feature. Features are not required to go through all stages.

### Preview

At Preview, a feature is ready for testing by customers before adopting it for production use at GA. Preview offerings are often publicly announced, but are not necessarily feature-complete, and Google provides no Service Level Agreements (SLA) or technical support commitments for these. Unless stated otherwise by Google, Preview offerings are intended for use in test environments only. Features in Preview are typically expected to reach GA within 12 months, but this might vary.

This _Preview_ icon, along with an accompanying note, indicates Preview features in documentation.

### General Availability (GA)

General Availability (GA) features are _production ready_ , though not always universally available. Some GA features might only be available to a limited group of customers. For customers with increased accreditation standards, some GA features are not available to use.

### Accredited

Accredited features are GA features that have received approval from the concerned accreditation agencies and are ready for customer onboarding. Customers with regulated deployments might require some production-ready features be accredited before they can use them. This feature type is identified as a Significant Change Request (SCR) feature and is undergoing further review. This feature has not received an Authority to Operate (ATO) within a regulated environment. Reach out to your IO with questions regarding feature accessibility.

This _In Review_ icon, along with an accompanying note, indicates features being actively reviewed for accreditation in documentation.

## End-of-life stages

If a feature is determined to be obsolescent, it transitions to end-of-life stages. A feature is first marked as _deprecated_ , which warns against future use with the intention of phasing it out. After a set time to allow for migration away from the feature, it is then removed from the product.

### Deprecated

Marking an offering deprecated is an announcement that GDC is discontinuing a service or feature that it supports. See the Google Cloud deprecation policy for more information: <https://cloud.google.com/terms/deprecation>.

This _Deprecated_ icon, along with an accompanying note, indicates Deprecated features in documentation.

### Decommissioned

Decommissioning an offering means that the feature is no longer available. Calling decommissioned software can result in unpredictable behavior or invalid responses.

## Feature gates

Feature gates are a mechanism used by your Infrastructure Operator (IO) to manage features that are in the following feature stages:

  * Preview
  * In review for accreditation



Based on your deployment, the features in the following table might not be available to use. Check with your operator for more information.

Feature | Stage | Description  
---|---|---  
API Platform for Vertex AI services | In review | API Platform authentication workflow for Vertex AI pre-trained and prediction APIs.  
KubeVirt CSI | In review | Capability to use the KubeVirt Container Storage Interface (CSI) driver for storage enhancements.  
VM disk cloning | In review | Capability to clone a virtual machine (VM) disk from an existing disk.  
VM metadata server | In review | Capability for a VM to store its metadata on a metadata server.  
VM guest agent streaming | In review | Communication method between the VM guest agent and the host VM.  
Server disk encryption with LUKS | In review | Process for using Linux Unified Key Setup (LUKS) with Trusted Platform Module (TPM) sealed keys to encrypt bare metal server disks at rest.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
