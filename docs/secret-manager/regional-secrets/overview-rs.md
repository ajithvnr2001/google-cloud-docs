---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs/
title: Secret Manager overview \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:01.791959+00:00
---

# Secret Manager overview  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Secret Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager is a secrets and credential management service that lets you store and manage sensitive data such as API keys, usernames, passwords, certificates, and more.

This is the documentation for the _regional_ service, which lets you specify that your secrets can only be stored or accessed in a particular region. To learn about the default global service, see the [global service documentation](https://docs.cloud.google.com/secret-manager/docs/overview). If you're not sure which service you need, see [Global and regional service options](https://docs.cloud.google.com/secret-manager/regional-secrets/global-regionalized-service-comparison).

## Key concepts

A [_secret_](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret) is a resource that contains a collection of metadata and secret versions. The metadata can include replication locations, labels, annotations, and permissions.

A [_secret version_](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs) stores the actual secret data, such as API keys, passwords, or certificates. Each version is identified by a unique ID or timestamp. Versions provide an audit trail, allowing you to track how a secret has changed over time.

Using Secret Manager, you can do the following:

  * **Manage rollback, recovery, and auditing using versions** : Versions help you manage gradual rollouts and emergency rollback, If a secret is accidentally changed or compromised, you can revert to a previous, known-good version. This minimizes potential downtime and security breaches. Versioning maintains a historical record of changes made to a secret, including who made the changes and when. It helps you audit secret data and track any unauthorized access attempts. You can pin secret versions to specific workloads and add [aliases](https://docs.cloud.google.com/secret-manager/regional-secrets/assign-alias-to-secret-version-rs) for easier access to secret data. You can also [disable](https://docs.cloud.google.com/secret-manager/regional-secrets/disable-regional-secret-version) or [destroy](https://docs.cloud.google.com/secret-manager/regional-secrets/destroy-regional-secret-version) secret versions that you don't require.

  * **Encrypt your secret data in transit and at rest** : All secrets are encrypted by default, both in transit using TLS and at rest with AES-256-bit encryption keys. For those requiring more granular control, you can encrypt your secret data with [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/secret-manager/regional-secrets/create-secret-cmek-encryption). Using CMEK, you can generate new encryption keys or import existing ones to meet your specific requirements.

  * **Manage access to secrets using fine-grained Identity and Access Management (IAM) roles and conditions** : With [IAM roles and permissions](https://docs.cloud.google.com/secret-manager/regional-secrets/access-control-rs), you can [ provide granular access](https://docs.cloud.google.com/secret-manager/regional-secrets/manage-access-regional-secrets) to specific Secret Manager resources. You can segregate responsibilities for accessing, managing, auditing, and rotating secrets.

  * **Rotate secrets automatically to meet your security and compliance requirements** : [Rotating your secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/about-rotation-schedules-rs) protects against unauthorized access and data breaches. Regularly changing your secrets reduces the risk of stale or forgotten secrets and ensures compliance with many regulatory frameworks that require periodic rotation of sensitive credentials.

  * **Enforce data residency using regional secrets** : [Data residency](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs#control_data_residency) requires that certain types of data, often belonging to specific individuals or organizations, be stored within a defined geographic location. You can create [regional secrets](https://docs.cloud.google.com/secret-manager/docs/create-regional-secrets) and store your sensitive data within a specific location to comply with data sovereignty laws and regulations.

  * **Manage operational parameters for your applications using Parameter Manager** : [Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) is an extension to the Secret Manager service that you can use to store and manage application configurations such as database connection strings, feature flags, environment names, port numbers to listen on, and settings for application features. You can also [reference secrets](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter) stored in Secret Manager within your parameter configurations. To use Parameter Manager, you must enable the Parameter Manager API and grant your users the [required IAM roles](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/access-control).




## Difference between secrets management and key management

Secrets management and key management are both critical components of data security, but they serve distinct purposes and handle different types of sensitive information. The choice between secrets management and key management depends on your specific needs. If you want to securely store and manage confidential data, a secrets management system is the right tool. If you want to manage encryption keys and perform cryptographic operations, a key management system is the better choice.

You can use the following table to understand the key differences between Secret Manager and a key management system, such as [Cloud Key Management Service(Cloud KMS)](https://docs.cloud.google.com/kms/docs).

Feature | Secret Manager | Cloud KMS  
---|---|---  
Primary function | Store, manage, and access secrets as binary blobs or text strings. | Manage cryptographic keys and use them to encrypt or decrypt data.  
Data stored | Actual secret values. With the appropriate permissions, you can view the contents of the secret. | Cryptographic keys. You can't view, extract, or export the actual cryptographic secrets (the bits and bytes) that are used for encryption and decryption operations.  
Encryption | Encrypts secrets at rest and in transit using Google-owned and managed keys or customer-managed keys. | Provides encryption and decryption capabilities for other services.  
Typical use cases | Store configuration information such as database passwords, API keys, or TLS certificates needed by an application at runtime. | Handle large encryption workloads, such as encrypting rows in a database or encrypting binary data such as images and files. You can also use Cloud KMS to perform other cryptographic operations such as signing and verification.  
  
## Encryption of secrets

Secret Manager always encrypts your secret data before it is persisted to disk. To learn more about Google Cloud encryption options, refer to [Encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

Secret Manager manages server-side encryption keys on your behalf using the same hardened key management systems that we use for our own encrypted data, including strict key access controls and auditing. Secret Manager encrypts user data at rest using AES-256. There is no setup or configuration required, no need to modify the way you access the service, and no visible performance impact. Your secret data is automatically and transparently decrypted when accessed by an authorized user.

The Secret Manager API always communicates over a secure HTTP(S) connection.

Those who require an extra layer of protection can enable CMEK and use their own encryption keys stored in Cloud Key Management Service to protect the secrets stored in Secret Manager. See the [Add CMEK encryption to regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/create-secret-cmek-encryption) for details on how to use customer-managed encryption keys.

## What's next

  * Learn about [data residency and regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/data-residency).
  * Learn how to [create a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret).
  * Learn how to [add a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs).
  * Learn how to [edit a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/edit-regional-secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
