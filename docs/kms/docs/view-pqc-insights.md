---
url: https://docs.cloud.google.com/kms/docs/view-pqc-insights/
title: View asymmetric post-quantum cryptography (PQC) insights \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:05.890523+00:00
---

# View asymmetric post-quantum cryptography (PQC) insights  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/view-pqc-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  View asymmetric post-quantum cryptography (PQC) insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the **Post-quantum cryptography (PQC) insights** chart in the Cloud KMS **Key management overview** in the Google Cloud console to help evaluate your inventory of asymmetric keys and prepare for future cryptographic modernization.

The advent of quantum computing poses a potential threat to widely used public-key cryptographic algorithms. The **PQC insights** chart helps you identify and inventory classical asymmetric keys, providing the visibility needed to plan for future modernization and ensure long-term resilience.

Symmetric keys (such as those used for `ENCRYPT_DECRYPT`) are generally considered resistant to quantum computer attacks and are not included in this dashboard. For more information about algorithms supported by Cloud KMS, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).

[Wiz](https://cloud.google.com/wiz), now part of Google Cloud, offers a cryptographic inventory and risk assessment that can help you understand your cryptographic readiness posture and plan your migration to post-quantum algorithms. These capabilities are included as part of Wiz's Cloud and AI security platform, complementing the key management features of Cloud KMS.

## Before you begin

To get the permissions that you need to view PQC insights, ask your administrator to grant you the [Cloud KMS Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.viewer) (`roles/cloudkms.viewer`) IAM role on on the project

  * You can also query the Cloud Asset viewer directly. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View PQC insights

The **Asymmetric PQC insights** chart provides a high-level visual breakdown of your asymmetric keys based on the categorization of the algorithms they use.

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the **Overview** tab, and then go to **Asymmetric PQC insights** chart.

  3. Optional: Click a segment of the chart to view the number of keys that it represents. You can also click **View** for a segment to view a table of **Asymmetric PQC insights details**.




This chart categorizes keys into two main groups:

  * **Post-quantum:** Keys that use cryptographic algorithms specifically designed to be resistant to attacks from future quantum computers.
  * **Classical:** Keys that use classical asymmetric algorithms (such as RSA or ECC) that remain secure against classical attacks today, but are susceptible to attacks from future quantum computers.



The chart further segments these keys by their cryptographic purpose and cryptography type.

## Understand the Details Table

The table on this page lists your asymmetric keys within the current project and provides the following information:

  * **Key name:** The name of the key. Click the name to go to the **Key Details** page for that specific key.
  * **Location:** The location where the key resides.
  * **Protection Level:** The protection level of the key.
  * **Purpose:** The cryptographic purpose of the key—for example, `ASYMMETRIC_SIGN`.
  * **Cryptography type:** Indicates whether the key uses a PQC or classical algorithm.



You can use the filter bar above the table to refine the list of keys based on any of these attributes.

## Assess classical keys for future modernization

You should review your existing asymmetric keys for classical asymmetric algorithms that could be transitioned to post-quantum alternatives. These keys still offer strong protection against classical attacks. However, adopting post-quantum algorithms helps to ensure long-term resilience against potential future quantum threats. The following table lists key purposes and algorithms and whether each is considered post-quantum secure.

Purpose | Algorithms | Cryptography type | Post-quantum alternative  
---|---|---|---  
`ASYMMETRIC_SIGN` | `EC_SIGN_*` | Classical | `ASYMMETRIC_SIGN` with `PQ_SIGN_*` algorithms  
`ASYMMETRIC_SIGN` | `RSA_SIGN_*` | Classical | `ASYMMETRIC_SIGN` with `PQ_SIGN_*` algorithms  
`ASYMMETRIC_SIGN` | `PQ_SIGN_*` | PQC | _Post-quantum safe_  
`ASYMMETRIC_DECRYPT` | `RSA_DECRYPT_*` | Classical | `KEY_ENCAPSULATION` algorithms  
`KEY_ENCAPSULATION` | All | PQC | _Post-quantum safe_  
  
Adopting PQC standards sooner rather than later provides these benefits:

  * Replacing `ASYMMETRIC_DECRYPT` keys with `KEY_ENCAPSULATION` keys helps to protect your encrypted data against "store now, decrypt later" (SNDL) attacks, where a bad actor intercepts your ciphertext with no way to decrypt it, but stores the ciphertext in the hopes of one day cracking the encryption.
  * Replacing `ASYMMETRIC_SIGN` keys that use `EC_SIGN_*` or `RSA_SIGN_*` algorithms with a `PQ_SIGN_*` algorithm provides long-term non-repudiation for your signatures.



## Identify keys with Cloud Asset Inventory

You can use Cloud Asset Inventory to programmatically list and filter your Cloud KMS assets by algorithm type.

### Search across an organization

  1. To list keys that use post-quantum algorithms such as `PQ_SIGN_*`, `ML_KEM_*`, or `KEM_XWING`, run the following command:
         
         gcloud asset list \
           --organization=ORGANIZATION_ID \
           --asset-types="cloudkms.googleapis.com/CryptoKey" \
           --content-type=resource \
           --filter='(resource.data.purpose = "ASYMMETRIC_SIGN" OR resource.data.purpose = "ASYMMETRIC_DECRYPT" OR resource.data.purpose = "KEY_ENCAPSULATION") AND (resource.data.versionTemplate.algorithm:PQ_SIGN* OR resource.data.versionTemplate.algorithm:ML_KEM* OR resource.data.versionTemplate.algorithm = "KEM_XWING")' \
           --format='table(name.segment(1):label=PROJECT, name.segment(-3):label=KEY_RING, name.segment(-1):label=CRYPTO_KEY, resource.data.purpose:label=PURPOSE, resource.data.versionTemplate.algorithm:label=ALGORITHM)'
         

  2. To list asymmetric keys that don't use post-quantum algorithms—in other words, asymmetric keys that use classical algorithms—run the following command:
         
         gcloud asset list \
           --organization=ORGANIZATION_ID \
           --asset-types="cloudkms.googleapis.com/CryptoKey" \
           --content-type=resource \
           --filter='(resource.data.purpose = "ASYMMETRIC_SIGN" OR resource.data.purpose = "ASYMMETRIC_DECRYPT" OR resource.data.purpose = "KEY_ENCAPSULATION") AND NOT (resource.data.versionTemplate.algorithm:PQ_SIGN* OR resource.data.versionTemplate.algorithm:ML_KEM* OR resource.data.versionTemplate.algorithm = "KEM_XWING")' \
           --format='table(name.segment(1):label=PROJECT, name.segment(-3):label=KEY_RING, name.segment(-1):label=CRYPTO_KEY, resource.data.purpose:label=PURPOSE, resource.data.versionTemplate.algorithm:label=ALGORITHM)'
         




### Search across a project

  1. Ensure your Google Cloud CLI targets the correct project:
         
         gcloud config set project PROJECT_ID
         

  2. To list keys that use post-quantum algorithms such as `PQ_SIGN_*`, `ML_KEM_*`, or `KEM_XWING`, run the following command:
         
         gcloud asset list \
           --project="$(gcloud config get-value project)" \
           --asset-types="cloudkms.googleapis.com/CryptoKey" \
           --content-type=resource \
           --filter='(resource.data.purpose = "ASYMMETRIC_SIGN" OR resource.data.purpose = "ASYMMETRIC_DECRYPT" OR resource.data.purpose = "KEY_ENCAPSULATION") AND (resource.data.versionTemplate.algorithm:PQ_SIGN* OR resource.data.versionTemplate.algorithm:ML_KEM* OR resource.data.versionTemplate.algorithm = "KEM_XWING")' \
           --format='table(name.segment(-3):label=KEY_RING, name.segment(-1):label=CRYPTO_KEY, resource.data.purpose:label=PURPOSE, resource.data.versionTemplate.algorithm:label=ALGORITHM)'
         

  3. To list asymmetric keys that don't use post-quantum algorithms—in other words, asymmetric keys that use classical algorithms—run the following command:
         
         gcloud asset list \
           --project="$(gcloud config get-value project)" \
           --asset-types="cloudkms.googleapis.com/CryptoKey" \
           --content-type=resource \
           --filter='(resource.data.purpose = "ASYMMETRIC_SIGN" OR resource.data.purpose = "ASYMMETRIC_DECRYPT" OR resource.data.purpose = "KEY_ENCAPSULATION") AND NOT (resource.data.versionTemplate.algorithm:PQ_SIGN* OR resource.data.versionTemplate.algorithm:ML_KEM* OR resource.data.versionTemplate.algorithm = "KEM_XWING")' \
           --format='table(name.segment(-3):label=KEY_RING, name.segment(-1):label=CRYPTO_KEY, resource.data.purpose:label=PURPOSE, resource.data.versionTemplate.algorithm:label=ALGORITHM)'
         




## Recommended modernization paths

To mitigate risks from quantum attacks, transition away from asymmetric keys that use classical algorithms.

  * **For asymmetric decryption keys:** For keys that are used for asymmetric decryption, you can modernize your inventory by replacing asymmetric encryption with hybrid public key encryption (HPKE). In HPKE, you use keys with the purpose `KEY_ENCAPSULATION` that use a post-quantum algorithm such as `ML_KEM_768` to share a secret. For more information, see [Key encapsulation mechanisms](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms).
  * **For asymmetric signing keys:** For digital signatures, you can modernize your inventory by creating new keys with the purpose `ASYMMETRIC_SIGN` that use a post-quantum algorithm such as `PQ_SIGN_ML_DSA_65`.

**Note:** Because the purpose of an existing key cannot be changed, modernization often involves creating a new key or new key version with a post-quantum configuration and updating your applications to use the new key.

## Post-quantum resilience of symmetric keys

Unlike the asymmetric keys that are the focus of the **asymmetric PQC insights** chart, symmetric keys are generally considered resistant to quantum computer attacks. The notable exception is `MAC` keys that use the `HMAC-SHA1` algorithm. For more information about different algorithms, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).

## What's next

  * Review the available [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).
  * Learn more about [key encapsulation](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
