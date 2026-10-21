---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/always-on-secrets-encryption/
title: Using always-on secrets encryption \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:04.273524+00:00
---

# Using always-on secrets encryption  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/always-on-secrets-encryption/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Using always-on secrets encryption Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/always-on-secrets-encryption)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/always-on-secrets-encryption)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud version 1.10 supports encrypting secrets without the need for an external KMS (Key Management Service), or any other dependencies.

## Enable always-on secrets encryption

Always-on secrets encryption works by automatically generating an encryption key that is used to encrypt secrets before they are stored on the etcd database for that cluster. The encryption algorithm is A256GCM (AES GCM using 256-bit key).

The key version is a version number to indicate the key currently in use.

You can enable secrets encryption after a cluster has already been created.

  * For the admin cluster:

    1. Edit the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#secretsencryption-section) to add the `secretsEncryption` section.

    2. Run the `gkectl update` command.
           
           gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig ADMIN_CLUSTER_KUBECONFIG

  * For a user cluster:

    1. Edit the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#secretsencryption-section) to add the `secretsEncryption` section.

    2. Run the `gkectl update` command.
           
           gkectl update cluster --config USER_CONFIG_FILE --kubeconfig ADMIN_CLUSTER_KUBECONFIG




Replace the following:

  * `ADMIN_KUBECONFIG` with the path of your admin cluster kubeconfig file.
  * `ADMIN_CLUSTER_CONFIG` with the path of your admin cluster configuration file.
  * `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.



The `gkectl update` commands provided in this section can also be used for any other updates to the corresponding cluster.

## Key storage

The encryption keys for the admin cluster are stored on the admin cluster data disk. This disk is mounted on the admin master machine at `/opt/data`, and the encryption keys can be found at `/opt/data/gke-k8s-kms-plugin/generatedkeys/`. These keys must be backed up to retain access to the encrypted secrets used by that key.

## Key rotation

To rotate an existing encryption key for a cluster, increment the `keyVersion` in the corresponding [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#secretsencryption-generatedkey-version-field) or [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#secretsencryption-generatedkey-version-field), and run the appropriate `gkectl update` command. This creates a new key matching the new version number, re-encrypts each secret, and securely erases the old one. All subsequent new secrets are encrypted using the new encryption key.

## Disable always-on secrets encryption

To disable secrets encryption on an existing cluster, add a `disabled: true` field. Next, run the corresponding `gkectl update` command. This update decrypts each existing secret and stores each secret in plain text. All subsequent new secrets are stored in plain text.
    
    
    secretsEncryption:
      mode: GeneratedKey
      generatedKey:
        keyVersion: KEY_VERSION
        disabled: true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
