---
url: https://docs.cloud.google.com/confidential-computing/docs/split-trust-encryption-tool/
title: Split-trust Encryption Tool \u00a0|\u00a0 Confidential Computing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:49:26.792359+00:00
---

# Split-trust Encryption Tool  |  Confidential Computing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/docs/split-trust-encryption-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Computing ](https://docs.cloud.google.com/confidential-computing/docs)



Send feedback 

#  Split-trust Encryption Tool Stay organized with collections  Save and categorize content based on your preferences. 

The Split-Trust Encryption Tool (STET) allows for secure key data transfer in and out of Google Cloud in a way that is verifiably and cryptographically protected from Google Cloud insiders.

This is achieved by using two key management systems (KMS), one internal to Google Cloud, the other external. Even if one KMS is compromised, the second is in place to help keep your data private.

What follows is a series of examples involving data transmitted to [Cloud Storage](https://docs.cloud.google.com/storage) and computed using [Compute Engine](https://docs.cloud.google.com/compute) VMs. The examples step through increasing levels of security to help explain how STET fits into your security flow.

## Level 1: Cloud Storage

![A flow diagram from on-premises compute to Compute Engine](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-cloud-storage.svg)

When ingesting data into Google Cloud, you can use Cloud Storage to make the data available to your cloud workloads. You can upload the data from your on-premises computing environments to a Cloud Storage bucket, give your workload access to that bucket, and have the workload (or multiple workloads) consume that data when necessary. This strategy avoids the complexity of creating an active connection directly to the workload to send it the data it needs.

Cloud Storage always encrypts your data at rest. However, if you are entrusting Cloud Storage with doing that encryption for you, it has access to the unencrypted data (plaintext) prior to encryption, as well as the encryption keys used to create the encrypted data (ciphertext). Depending on your threat model, it might be desirable to encrypt the data before you send it to Cloud Storage, so that Cloud Storage never has visibility to the plaintext.

## Level 2: Client-side encryption

![A flow diagram from on-premises compute to Compute Engine](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-client-side-encryption.svg)

When using [client-side encryption](https://docs.cloud.google.com/storage/docs/encryption/client-side-keys), you encrypt the data before it is uploaded to Cloud Storage and only decrypt it after it is downloaded into your workload. As a result, Cloud Storage has access to the ciphertext but not the plaintext. Cloud Storage adds another layer of encryption before storing it, but the primary protection for the data is the encryption performed prior to uploading.

With this approach, you now need to give the workload access to the encryption key needed to decrypt the data. This itself is a potentially difficult task, as the encryption key grants the ability to remove your original layer of encryption and gain visibility to the data.

## Level 3: External key management

![A flow diagram from on-premises compute to Compute Engine with an external key manager](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-ekm.svg)

A common approach to this key management problem is to use a dedicated Key Management Service (KMS) that holds the keys and manages access to them. On each encryption or decryption attempt, a request must be sent to the KMS. The KMS has the ability to grant access based on various criteria to ensure that only appropriate parties are able to decrypt the data.

KMS systems have the ability to require a number of different criteria before authorizing access to the encryption key, but they typically require a credential that matches a policy configured on the KMS. Therefore, any party in possession of that credential will be able to access the encryption key and would be able to decrypt the data.

## Level 4: Confidential Computing

![A flow diagram from on-premises compute to Compute Engine with an external key manager and attestation](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-confidential-computing.svg)

[Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instances run with their memory encrypted, providing additional protections against unintended access to the data while in use. For many threat models, Confidential VM instances are more trusted than standard instances, allowing them to be used for sensitive workloads.

If your threat model relies on Confidential Computing, one issue is ensuring that a workload is running in a Confidential VM instance. [Remote attestation](https://en.wikipedia.org/wiki/Trusted_Computing#Remote_attestation) is a means by which the workload can prove to a remote party that they are running in a Confidential VM instance and can confirm many other properties about the configuration and environment of the workload. Because the attestations are generated by the platform, the workload can't create false attestations that don't reflect its actual environment.

A KMS can require and evaluate these attestations before allowing access to keys. This requirement helps ensure that only the intended workload is allowed to decrypt the data, even if the normal credentials are compromised.

## Level 5: Split trust

![A flow diagram from on-premises compute to Compute Engine with split trust](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-split-trust.svg)

When using a single KMS, that KMS has sole control over the encryption keys. If the KMS operator were to acquire the ciphertext of your encrypted data, they would have everything needed to decrypt it into your plaintext. While this risk might be acceptable if the KMS is operated by a completely trusted entity, some threat models create a need to remove unilateral control from the KMS.

With STET, you have the option to split this trust between two KMS systems, with neither KMS having enough information to decrypt your data. It would require collusion between both KMS operators (and access to the ciphertext) in order to decrypt your data.

If you're using Confidential VM, STET also facilitates the encryption and decryption of data using keys stored in a KMS that requires attestations.

All together, STET helps ensure that the only entities that have access to your plaintext data are the originator of the data (for example, an on-premises system) and the consumer of the data (for example, a workload running in a Confidential VM instance).

For more information on using STET, see the [GitHub repository](https://github.com/GoogleCloudPlatform/stet) and [quickstart guide](https://github.com/GoogleCloudPlatform/stet/blob/main/docs/quickstart_guide.md).

### Confidential Space with STET

![A flow diagram from on-premises compute to Compute Engine with split trust and Confidential Space](https://docs.cloud.google.com/static/confidential-computing/docs/images/ude-confidential-space.svg)

If you use [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs), STET can use the attestation token from Confidential Space as attestation evidence when accessing the key-encryption-key (KEK) that is stored in Cloud KMS.

STET handles access to Cloud KMS keys for your workload, and supports using Confidential Space to perform attestation for the encryption workflow, the decryption workflow, or both the encryption and decryption workflows.

You can create a STET configuration that includes information such as the workload identity pool (WIP) name, Cloud KMS URIs, and decryption information. STET then uses that information to integrate into your Confidential Space set up.

For more information, see the [GitHub repository](https://github.com/GoogleCloudPlatform/stet) and the [Confidential Space integration guide](https://github.com/GoogleCloudPlatform/stet/blob/main/docs/confidential_space.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
