---
url: https://docs.cloud.google.com/security-command-center/docs/cmek/
title: Enable CMEK for Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:31.501260+00:00
---

# Enable CMEK for Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable CMEK for Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

By default, Security Command Center encrypts customer content at rest. Security Command Center handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Security Command Center. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Security Command Center resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

For better separation of duties and control over key access, we recommend managing keys in a dedicated project without other Google Cloud resources. 

You can configure Security Command Center to use customer-managed encryption keys (CMEK) using Cloud Key Management Service keys when you activate Security Command Center for the organization. You can also change the configuration after Security Command Center is activated.

You can't enable CMEK with Security Command Center project-level activations.

To learn more about activating Security Command Center and changing the configuration, see the following:

  * [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)
  * [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)
  * [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption)



You can use organization policy constraints to enforce a required encryption configuration. For information about using CMEK organization policy constraints and Security Command Center, see CMEK organization policy constraints on this page.

Warning: If you disable, revoke access to, or destroy the CMEK after activation, Security Command Center stops working and you can lose your Security Command Center data. Destroying a key version is permanent and causes unrecoverable data loss. 

## Supported resource types

You can use CMEK to encrypt data for the following Security Command Center resource types:

  * Findings
  * Notification configurations
  * BigQuery exports
  * Mute configs



### Reconfiguring data encryption

After you activate Security Command Center, you can change the data encryption configuration between Cloud KMS keys and Google-owned and Google-managed encryption keys.

Warning: If you disable, revoke access to, or destroy the CMEK after activation, Security Command Center stops working and you can lose your Security Command Center data. Destroying a key version is permanent and causes unrecoverable data loss. 

You can [rotate the CMEK key](https://docs.cloud.google.com/kms/docs/key-rotation), which causes Security Command Center to use the new key version. However, some Security Command Center capabilities continue to use the old key for 30 days.

## Before you begin

The following section describes the steps to perform before you change the configuration.

### Determine the key location

When you create a Cloud KMS key and key ring for Security Command Center, you must use a location that corresponds to your Security Command Center location.

If you don't plan to enable [data residency for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/data-residency-support), then create your Cloud KMS key and key ring in the `us` location.

If you plan to enable data residency, then choose the Cloud KMS location that corresponds to your Security Command Center location:

Security Command Center location | Cloud KMS key location  
---|---  
`eu` | `europe`  
`sa` | `me-central2`  
`us` | `us`  
  
### Define organization policy constraints for CMEK

To enforce CMEK usage for Security Command Center, you can enforce the following organization policy constraints at the organization, folder, or project level:

  * `constraints/gcp.restrictNonCmekServices`: Requires you to use CMEK. If you enforce `constraints/gcp.restrictNonCmekServices` on an organization, and you've listed Security Command Center as a restricted service that's required to use CMEK, then you must enable CMEK when you activate Security Command Center.

**Important:** If you enforce this constraint, and you don't list Security Command Center as a restricted service, then some Security Command Center features won't work correctly.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: Requires that the Cloud KMS key for Security Command Center must come from a specific project or set of projects.




If you enforce both of these constraints on the organization where you activate Security Command Center, then Security Command Center requires you to enable CMEK and requires that the CMEK key is located in a specific project.

For information about how organization policies are evaluated across the Google Cloud resource hierarchy (organizations, folders, and projects), see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

For general information about using CMEK organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## Configure the Cloud Key Management Service keys

Before you configure Security Command Center to use CMEK, do the following:

  1. Install and initialize the Google Cloud CLI:

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Create a Google Cloud project with Cloud KMS enabled. This is your _key project_.

  3. Create a _key ring_ in the correct location. The key ring location must correspond to the location where you plan to activate Security Command Center.

To find the correct location, see Key location on this page. To learn how to create a key ring, see [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring).

  4. Create a Cloud KMS _key_ on the key ring. For instructions, see [Create a key](https://docs.cloud.google.com/kms/docs/create-key).




## Configure data encryption for Security Command Center

You can configure data encryption when you activate the Security Command Center [Standard service tier](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier) or [Premium service tier](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier) for an organization.

You can change the data encryption configuration on the Standard and Premium tiers after you activate Security Command Center. For more information, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

After you configure CMEK, Security Command Center encrypts data using your chosen Cloud KMS key.

## Troubleshooting CMEK

The following sections help you resolve issues that might occur with resource types that support CMEK.

### Restore service agent access to keys

With CMEK enabled, the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-security-command-center-service-agent) must have access to your Cloud KMS key. If this service agent doesn't have the required IAM role on your key, then some features of Security Command Center won't work correctly.

To determine whether you have this issue, view the list of [principals that have access to your key](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#view-access). If the service agent is configured correctly, then the list includes a principal with the identifier `service-org-ORGANIZATION_NUMBER@security-center-api.iam.gserviceaccount.com` and the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`).

If you don't see this principal and role, then grant the required role to the service agent on your key:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --member=serviceAccount:service-org-ORGANIZATION_NUMBER@security-center-api.iam.gserviceaccount.com \
        --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

  * `KEY_RING`: the key ring for your Cloud KMS key
  * `LOCATION`: the location of your Cloud KMS key
  * `KEY_NAME`: the name of your Cloud KMS key
  * `ORGANIZATION_NUMBER`: your organization number



### Restore keys that are disabled or scheduled for destruction

If a Cloud KMS key or key version is disabled, then you can [enable a key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable).

Similarly, if a Cloud KMS key is scheduled for destruction, then you can [restore a key version](https://docs.cloud.google.com/kms/docs/destroy-restore#restore). After a key is destroyed, you can't recover it, and you won't have access to Security Command Center resources that support CMEK.

### Resolve errors creating protected resources

If you choose Google-owned and Google-managed encryption keys when you activate Security Command Center, and then you enforce a CMEK organization policy constraint within that organization, you won't be able to create new resources that support CMEK.

If you can't create these resources, then check whether a CMEK organization policy constraint is enforced for your organization, or for any projects or folders in that organization. For more information, see CMEK organization policy constraints on this page.

## Quotas and pricing

When you use CMEK in Security Command Center, your projects can consume Cloud KMS cryptographic requests quotas. CMEK-encrypted instances consume quotas when reading or writing data in Security Command Center. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

In addition, Cloud KMS charges apply when Security Command Center uses your CMEK to encrypt or decrypt data. For more information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
