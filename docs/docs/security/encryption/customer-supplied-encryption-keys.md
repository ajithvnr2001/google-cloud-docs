---
url: https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys/
title: Customer-supplied encryption keys \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:28.768575+00:00
---

# Customer-supplied encryption keys  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Customer-supplied encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

_**This content was last updated in February 2025 and represents the status quo as of the time that it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers**_.

Customer-supplied encryption keys (CSEK) are a feature in [Cloud Storage](https://docs.cloud.google.com/storage). If you supply your own encryption keys, Google uses your key to protect the Google generated keys that encrypt and decrypt your data.

This document describes how CSEKs work and how they are protected in Google Cloud.

**Caution:** Customer-supplied encryption keys (CSEK) for Compute Engine are [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). For more information and instructions on alternatives, see [CSEK deprecation in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine). 

## How CSEKs work with Cloud Storage

When you use CSEKs in Cloud Storage, the following keys are part of the wrapping process:

  * **Raw CSEK:** You provide a raw CSEK as part of an API call. The raw CSEK key is transmitted from the Google Front End (GFE) to the storage system's memory. This key is the key encryption key (KEK) in Cloud Storage for your data.
  * **Wrapped chunk keys:** The raw CSEK is used to wrap the wrapped chunk keys.
  * **Raw chunk keys:** The wrapped chunk keys wrap the raw chunk keys in memory. The raw chunk keys are used to encrypt the data chunks that are stored in the storage systems. These keys are used as the data encryption keys (DEKs) in Cloud Storage for your data.



The following diagram shows the key wrapping process.

![Cloud Storage CSEK.](https://docs.cloud.google.com/static/docs/security/images/csek-cloud-storage.svg)

The following table describes the keys.

Keys | Stored in | Purpose | Accessible until  
---|---|---|---  
Raw CSEK | Storage system memory | Protects the wrapped chunk keys. | Customer-requested operation (for example, `insertObject` or `getObject`) is complete.  
Wrapped chunk keys | Storage devices | Protect raw chunk keys stored at rest. | Storage object is deleted.  
Raw chunk keys | Storage devices' memory | Protect the data that you read or write to the disk. | Customer-requested operation is complete  
  
## How CSEKs are protected

This section provides information on how CSEKs are protected on disk, as they move around the Google Cloud infrastructure, and in memory.

Raw CSEKs, CSEK-derived keys, and raw disk keys are never stored on disk unencrypted. Raw disk keys are stored wrapped with CSEK-derived keys and with Google keys when automatic restart is used. Google doesn't permanently store your keys on its servers.

Each service uses access management features provided by the infrastructure to specify exactly which other services can communicate with it. The service is configured with the allowlist of the allowed service account identities, and this access restriction is then automatically enforced by Google Cloud infrastructure. For more information, see [service identity, integrity, and isolation](https://docs.cloud.google.com/docs/security/infrastructure/design#service_identity_integrity_and_isolation).

The infrastructure also provides cryptographic privacy and integrity for RPC data on the network. Services can configure the level of cryptographic protection they want for each infrastructure RPC, and these are enabled for CSEKs. For more information, see [Encryption of inter-workload communication](https://docs.cloud.google.com/docs/security/infrastructure/design#encryption-inter-service).

Key material lives in various systems' memory, including cluster manager memory and VMM memory. Access to these systems' memory is by exception (for example, as part of an incident) and managed by access control lists. These systems have memory dumps disabled or automatically scan for key material in memory dumps. For information about protections to these jobs, see [How Google protects its production services](https://docs.cloud.google.com/docs/security/production-services-protection).

## What's next

  * [Customer-supplied encryption keys in Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
