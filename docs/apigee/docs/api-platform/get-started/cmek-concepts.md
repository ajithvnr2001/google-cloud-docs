---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts/
title: Introduction to CMEK \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:09.845161+00:00
---

# Introduction to CMEK  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Introduction to CMEK Stay organized with collections  Save and categorize content based on your preferences. 

This page describes using CMEK with Apigee. For best practices, see [ Best practices for Apigee CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices). 

## Overview

By default, Google Cloud automatically [ encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using encryption keys that are owned and managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK). 

You can read more about using CMEK for Apigee in Using CMEK with Apigee. For more information about CMEK in general, including when and why to enable it, see the [Cloud Key Management Service documentation](https://docs.cloud.google.com/kms/docs/cmek). 

Using [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) doesn't necessarily provide more security than Google's default encryption mechanisms; however, it gives you control over more aspects of the lifecycle and management of your keys in order to meet security and compliance requirements. 

If you need more control over key operations than what Google-owned and Google-managed encryption keys allow, you can use customer-managed encryption keys. These keys are created and managed using [Cloud Key Management Service](https://cloud.google.com/security/products/security-key-management) (Cloud KMS), and you store the keys as software keys, in an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally](https://docs.cloud.google.com/kms/docs/ekm). 

Key management features are provided by the Cloud KMS service.

## CMEK use cases

This section describes typical use cases for using CMEK with Apigee.

### Key rotation

Automatically or manually rotate the key. Note that when the key is rotated, data previously stored in Apigee is not automatically re-encrypted with the new key version, but will continue to be accessible as long as the previous key version used to encrypt the data is not disabled or destroyed.

The primary purpose of key rotation is to limit data exposure to one single key, not for replacing the old key version completely. Apigee does not currently support re-encryption upon key rotation. For Apigee specifically, when you rotate a key, only a limited number of new data (for example new proxy revision) will be encrypted with the new primary key version. Most data, like analytic data, runtime disk, and old proxy revision is still using the old key version. If you want to completely get rid of the previous key version, you need to recreate the `apigee` org. For runtime encryption keys, if you want to completely get rid of the previous key version, you need to recreate the runtime instances. See [ Best practices for Apigee CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices) for more details. 

See also: [Rotate a key](https://docs.cloud.google.com/kms/docs/rotating-keys)

### Key deletion and disablement

When a key version is disabled, Apigee data encrypted with that key version will not be accessible. To restore access to the data, the key can be re-enabled. 

When you delete or disable your CMEK key, even just for previous versions, your `apigee` org will start to malfunction depending on the key version being used for encryption. Certain APIs will stop functioning immediately as those APIs require a CMEK key to decrypt data, while certain functions will start malfunctioning only when some system action is triggered, such as [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) persistent disks to be remounted. See [ Key disablement](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices#key-disablement) for more information. 

When a key version is destroyed, any Apigee data encrypted with that key version will become unreadable and unrecoverable. **This is a permanent and irreversible operation**. 

See also: 

  * [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable)
  * [ Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore)



### Key restoration

If you accidentally delete or disable a key or a previous key version, you should try to restore them as soon as possible. Note that CMEK is a feature intended for data loss if the key is not available. After you restore the key, your `apigee` org is not guaranteed to recover, and you may experience data loss. See [ Re-enabling a key](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices#re-enabling-a-key) for more details. Contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) and see what is the best next step. 

See also: [ Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore)

### Revoke key access

If you revoke the Apigee service agent's access to the key using IAM, Apigee will be unable to access any control plane data encrypted by any key version. Apigee API operations that depend on decrypting the data will fail. Access to the data may be restored by re-granting access to the key and Apigee API operations that decrypt the data will be restored. 

See also: [ Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)

**Note:** The Apigee control plane and runtime are encrypted with separate keys. You must revoke both sets of keys to completely remove access to your data. 

### EKM

Apigee does not currently support [ Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm). If you use Cloud EKM, there is a known defect that Cloud EKM errors won't be properly propagated and surfaced to you. 

### Key tracking

Apigee supports [key usage tracking](https://docs.cloud.google.com/kms/docs/view-key-usage). The **Usage tracking** tab of a key in Cloud Key Management Service lists the Apigee resources that the key protects, for the following resource types: 

  * `apigee.googleapis.com/Organization`, which covers the control plane encryption key, the API consumer data encryption key, and the runtime database encryption key. 
  * `apigee.googleapis.com/Instance`, which covers the disk encryption key. 



For descriptions of these keys, see [About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys). 

**Note:** Key usage tracking is informational only, and the data can be delayed after you create or update a resource. Don't disable or destroy a key version based on key usage tracking alone. For the full set of caveats, see [Limitations](https://docs.cloud.google.com/kms/docs/view-key-usage#limitations). 

## Quotas

Using CMEK keys can generate usage against some Cloud KMS quotas. For the latest information about Cloud KMS quotas, see [Quotas](https://docs.cloud.google.com/kms/quotas). 

## Revoke encryption key

If you believe your data on Apigee in Google Cloud is compromised, you can revoke your encryption keys. Revoke the runtime CMEK to make your runtime instance malfunction and unable to access your gateway data. Revoke the control plane CMEK to make Apigee unable to perform analytics work or deploy new proxies. 

## Using CMEK with Apigee

Apigee encryption keys are used for runtime and control plane data and are created during the [ provisioning process](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). 

Apigee control plane data is encrypted using a different encryption key than runtime data, and it may be stored in different regions. As per the [CMEK](https://docs.cloud.google.com/kms/docs/cmek) documentation, this encryption applies only to data _at rest_ , that is, data that is ultimately stored on disk. 

Apigee control plane data includes proxy configurations (bundles), some environment configuration data, and analytics data. Apigee runtime data includes application data such as KVMs, cache, and client secrets, which is then stored in the runtime database. 

See [ About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys) for descriptions of the types of encryption keys. 

You can add encryption keys only at the time of Apigee organization creation; once a CMEK is assigned, you cannot change to a different CMEK after org creation. 

### Data residency control plane CMEK regions

In the regionalized Apigee control plane, you select two encryption keys for your control plane. This is because some of the components underlying the Apigee control plane are always in a single-region within the control plane location. See [ Data residency regions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) for more information. 

Details | Required keys  
---|---  
The control plane region is the where the control plane runs. Control plane in Apigee is an abstract concept where multiple underlying components together constitute the Apigee control plane. Control plane data is proxy configuration and analytics storage.  Other control plane data (e.g., analytics processing, portals) is in a sub-region of the control plane. All sub-region components will be in the same region as each other. |  One key for control plane data. One key for control plane sub-region data.  
  
### Organization policy constraints

If you have CMEK organization policy constraints on your Google Cloud project, Apigee will enforce compliance with those constraints. if you are using Apigee via the Google Cloud UI, CLI, or directly through Apigee APIs, enforcement of CMEK policies are guaranteed. when using the Google Cloud Apigee UI, CMEK organization policy constraints are pre-validated so that the UI can guide you into choosing valid, compliance configuration. 

CMEK organization policy constraints can be created to require that:

  * [ Customer-managed encryption keys are always used](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies#how-to-restrict-non-cmek-services)
  * [ Customer-managed encryption keys are allowed only from specific projects specified in an allowlist](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies#how-to-restrict-cmek-crypto-key-projects)



Not every feature in Apigee is currently CMEK compliant. To ensure that projects that require CMEK don't unknowingly use features that aren't CMEK protected, those features will be disabled for CMEK-constrained projects until they are compliant. Only new usages of the features will be disabled (creating new resources or enabling an add-on). Features and resources that are already in use will remain available and editable, but not CMEK-compliant. The following features will be disabled: 

  * **Apigee Shadow API Discovery** is not subject to CMEK organization policy and is not CMEK-compliant.

  * **Eval orgs creation** will be blocked by both the [ CreateOrganization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create) eval org API and the eval provisioning wizard. 
  * **Gemini Code Assist** is not available.

  * **Global orgs creation** will be blocked by the [ CreateOrganization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create) eval org API and the eval provisioning wizard. 
  * **Hybrid** instance creation is not available for enforcement. 
  * **Data Studio** button to open Data Studio with data from Apigee will be disabled when CMEK is required. 
  * **Retroactive enforcement** of compliance for existing resources is not available; you will need to delete and recreate resources if you need an existing resource to be compliant. 



See [ Using organization policy constraints in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies) for more information on using organization policy constraints with Apigee. 

### How to create encryption keys

By default, Google manages the creation of encryption keys during the provisioning process; however, you can create them yourself. For more information, see [ About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys). 

### Risks and mitigations

This section describes potential threats and actions you can take. 

  * Risks: 
    * **Key compromise:** Occurs when an attacker gains access to the encryption key, potentially through vulnerabilities in the KMS or attacks against key administrators. 
    * **Denial of service:** An attacker could disrupt access to encryption keys or data by attacking the KMS or storage system. 
    * **Loss of key:** Accidental key deletion or loss could lead to data loss or inaccessibility. 
  * Mitigations: 
    * Implement strong access control and key management policies.
    * Monitor KMS logs and activity for suspicious behavior.



### Troubleshooting

The following table describes some common error conditions that may arise with the CMEK- encrypted configstore data, the approximate error message returned by the Apigee API, and the recommended troubleshooting steps. 

Error message/symptom | Cause | Steps to take  
---|---|---  
`Constraint constraints/gcp.restrictNonCmekServices violated for projects/my-project attempting to create or enable trial org. CMEK is not supported for trial orgs. To use trial orgs, adjust the gcp.restrictNonCmekServices constraint for this project.` |  You attempted to provision a trial org where an organization policy constraint exists for the project.  |  CMEK is not supported for trial/eval orgs. You will have to update organization policy constraint `constraints/gcp.restrictNonCmekServices` to remove Apigee from the denied services list to be able to provision a trial org.   
`Constraint constraints/gcp.restrictCmekCryptoKeyProjects violated for projects/my-project attempting to use projects/my-project/locations/my-location/keyRings/kr-1/cryptoKeys/ck-1 key. Use a key from a project that is allowed by the gcp.restrictCmekCryptoKeyProjects constraint.` |  You attempted to provision an org where an organization policy constraint exists for the project and specified a KMS CryptoKey that is not allowlisted.  |  You have set `constraints/gcp.restrictCmekCryptoKeyProjects` in org policies which require you to provide a CMEK key from the allowed projects listed by you. You will have to provide the CMEK from an allowed project to be able to create an org or instances. Alternatively, you can update the organization policy constraint `constraints/gcp.restrictCmekCryptoKeyProjects` to allow keys from the specific Google Cloud project you want.   
`Apigee does not have permission to access key "..."` |  A user has revoked Apigee's access to the provided KMS key, i.e., by removing the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role.  | A user should check the configured roles on the KMS key and ensure that the Apigee service agent has the necessary permissions.   
`Unable to encrypt/decrypt data. Cloud KMS Error: "..." is not enabled, current state is: DESTROYED.` | A user has disabled or deleted the key version used to encrypt/decrypt the requested piece of data.  | A user should re-enable the key version if possible. If the key or key version has been destroyed, data is unrecoverable (by design).   
`No new Analytics data for US/EU users` |  One of the possible causes of this issue can be a user revoked/disabled/deleted single region key.  |  A user should re-enable/restore single region key access.   
`Control plane key "..." in region "..." is not valid for this control plane instance. Supported region(s) are "…".` |  A user has provided a single region control plane key in a region that is not valid or supported for the region or multi-region served by the instance of the control plane.  |  A user must either provide a key in one of the supported regions or choose to use a different control plane instance.   
`Multi-region control plane key is not valid for this control plane instance. Specify only the "apiConsumerDataEncryptionKeyName" field.` |  A user has provided a multi-region control plane key in a control plane that exists only in a single region (i.e. is not a multi-regional control plane).  |  A user must either omit the multi-regional key field or choose to use a multi-regional control plane instance.   
`Multi-region control plane key is not valid for this control plane instance. Specify a multi-region key with region "..."` |  A user has provided a multi-region control plane key to the wrong multi-regional control plane instance (e.g. a "us" key to the "eu" control plane instance)  |  A user must either use a multi-regional key in the correct multi-region or choose to use a different multi-regional control plane instance.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
