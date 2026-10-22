---
url: https://docs.cloud.google.com/kms/docs/key-rotation/
title: Key rotation \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:07.602082+00:00
---

# Key rotation  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/key-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key rotation Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses key rotation in Cloud Key Management Service. Key rotation is the process of creating new encryption keys to replace existing keys. By rotating your encryption keys on a regular schedule or after specific events, you can reduce the potential consequences of your key being compromised. For specific instructions to rotate a key, see [Rotating keys](https://docs.cloud.google.com/kms/docs/rotate-key).

## Why rotate keys?

For symmetric encryption, periodically and automatically rotating keys is a recommended security practice. Some industry standards, such as [Payment Card Industry Data Security Standard](https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss) (PCI DSS), require the regular rotation of keys.

Cloud Key Management Service **does not** support automatic rotation of asymmetric keys. See Considerations for asymmetric keys in this document.

Rotating keys provides several benefits:

  * Limiting the number of messages encrypted with the same key version helps prevent attacks enabled by cryptanalysis. Key lifetime recommendations depend on the key's algorithm, as well as either the number of messages produced or the total number of bytes encrypted with the same key version. For example, the recommended key lifetime for symmetric encryption keys in Galois/Counter Mode (GCM) is based on the number of messages encrypted, as noted at <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf>.

  * In the event that a key is compromised, regular rotation limits the number of actual messages vulnerable to compromise.

**If you suspect that a key version is compromised,[disable it](https://docs.cloud.google.com/kms/docs/enable-disable) and [revoke access to it](https://docs.cloud.google.com/kms/docs/iam) as soon as possible.**

  * Regular key rotation ensures that your system is resilient to manual rotation, whether due to a security breach or the need to migrate your application to a stronger cryptographic algorithm. **Validate your key rotation procedures before a real-life security incident occurs.**




You can also manually rotate a key, either because it is compromised, or to modify your application to use a different algorithm.

## How often to rotate keys

We recommend that you [rotate keys automatically](https://docs.cloud.google.com/kms/docs/rotate-key#automatic) on a regular schedule. A rotation schedule defines the frequency of rotation, and optionally the date and time when the first rotation occurs. The rotation schedule can be based on either the key's age or the number or volume of messages encrypted with a key version.

Some security regulations require periodic, automatic key rotation. Automatic key rotation at a defined period, such as every 90 days, increases security with minimal administrative complexity.

You should also [manually rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key#manual) if you suspect that it has been compromised, or when security guidelines require you to migrate an application to a stronger key algorithm. You can schedule a manual rotation for a date and time in the future. Manually rotating a key does not pause, modify, or otherwise impact an existing automatic rotation schedule for the key.

**Note:** When you rotate a key, data encrypted with previous key versions **isn't** automatically re-encrypted with the new key version. For more information, see [re-encrypting data](https://docs.cloud.google.com/kms/docs/re-encrypt-data).

Don't rely on irregular or manual rotation as a primary component of your application's security.

## After you rotate keys

Rotating keys creates new active key versions, but doesn't re-encrypt your data and doesn't disable or delete previous key versions. Previous key versions remain active and incur costs until they are destroyed. Re-encrypting data removes your reliance on old key versions, allowing you to destroy them to avoid incurring additional costs. To learn how to re-encrypt your data, see [Re-encrypting data](https://docs.cloud.google.com/kms/docs/re-encrypt-data).

You must [make sure that a key version is no longer in use](https://docs.cloud.google.com/kms/docs/destroy-restore#pre-destroy-checklist) before destroying the key version.

**Warning:** Destroying a key version that is still in use can cause permanent data loss. It's your responsibility to ensure that a key version is safe to destroy. Google is not responsible for outages, loss of data, or compliance issues that result from you destroying a key version.

## Considerations for asymmetric keys

Cloud KMS does not support automatic rotation for asymmetric keys, because additional steps are required before you can use the new asymmetric key version.

  * For asymmetric keys used for **signing** , you must distribute the public key portion of the new key version. Afterward, you can specify the new key version in calls to the [`CryptoKeyVersions.asymmetricSign`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign) method to create a signature, and update applications to use the new key version.

  * For asymmetric keys used for **encryption** , you must distribute and incorporate the public portion of the new key version into applications that encrypt data, and grant access to the private portion of the new key version, for applications that decrypt data.




## What's next

  * [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key).
  * [Enable or disable a key](https://docs.cloud.google.com/kms/docs/enable-disable).
  * Learn more about [re-encrypting data](https://docs.cloud.google.com/kms/docs/re-encrypt-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
