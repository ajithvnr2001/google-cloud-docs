---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-thales-kms/
title: Configuring vSAN encryption using CipherTrust Manager \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:03.123202+00:00
---

# Configuring vSAN encryption using CipherTrust Manager  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-thales-kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuring vSAN encryption using CipherTrust Manager

To encrypt data at rest using vSAN encryption, one option is to switch your active key management service (KMS) to an external one. [Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/ciphertrust-manager) is an external KMS solution that's KMIP 1.1 compliant and certified by VMware for vSAN.

For information about the default vSAN encryption behavior of Google Cloud VMware Engine, see [About vSAN encryption](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption).

## Before you begin

To use the command-line examples in the CipherTrust Manager guide, you must install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

The [Thales CipherTrust Manager documentation](https://thalesdocs.com/ctp/ig/google/gcve/index.html) provides additional information about prerequisites for this integration.

## Setup overview

Setting up VMware Engine with CipherTrust Manager involves the following major steps:

  1. Access and install a CipherTrust Manager image on a Compute Engine VM.
  2. In CipherTrust Manager, configure network details and assign users to a key management domain.
  3. Create a registration token and registered client to use when configuring the key management interoperability protocol (KMIP) connection to vCenter Server.
  4. Register the KMIP client in Thales CipherTrust Manager using a private key and certificate.
  5. In vCenter Server, declare CipherTrust Manager as a standard key provider.



For a full description of the steps required for this integration, see the [Thales CipherTrust Manager documentation](https://thalesdocs.com/ctp/ig/google/gcve/index.html) for Google Cloud VMware Engine.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
