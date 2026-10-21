---
url: https://docs.cloud.google.com/kms/docs/hsm-for-workspace-best-practices/
title: Best practices for Cloud HSM for Google Workspace \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:09:29.508342+00:00
---

# Best practices for Cloud HSM for Google Workspace  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/hsm-for-workspace-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)



Send feedback 

#  Best practices for Cloud HSM for Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines best practices for configuring Cloud HSM for Google Workspace to help protect your key material against accidental or unauthorized destruction and deletion, help ensure high availability and durability for critical cryptographic keys, and help meet regulatory and compliance requirements.

This document is intended for cloud architects, security teams, and Google Workspace administrators who are responsible for the security and operational resilience of the encryption keys used in [client-side encryption (CSE)](https://support.google.com/a/answer/10741897) for Google Workspace. It assumes that you're already familiar with [Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/hsm-for-workspace) and have completed the [onboarding process](https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace).

## Mitigate the loss of key material

Security risks can arise when a principal holds a role which grants permission to complete destructive actions, especially those outside the principal's usual scope of work. For example, a user with an overly broad Project Owner (`roles/owner`) role could destroy the key material used for Google Workspace CSE, leaving the encrypted data permanently inaccessible.

The following sections describe practices that help to mitigate the risk of both accidental and malicious key destruction and deletion by removing permissions to destroy or delete the Cloud KMS key material used by Google Workspace client-side encryption (CSE) and constraining key destruction.

### Enforce folder-level IAM deny policies

IAM deny policies let you deny permissions to principals, even if the permission is otherwise granted by a role that the principal holds. For example, even if a user has the Project Owner (`roles/owner`) role, a folder-level IAM deny policy can prevent them from destroying or deleting keys. By placing your Cloud HSM project inside a folder and applying a deny policy at the folder level, you create a guardrail that prevents key destruction and deletion while the policy is enforced. Enforced deny policies can't be canceled without a role such as Deny Admin (`roles/iam.denyAdmin`) on the folder.

Ensure that folder administration roles like Folder Admin (`roles/resourcemanager.folderAdmin`) and Deny Admin (`roles/iam.denyAdmin`) are only granted to principals that don't also have the Cloud KMS Admin (`roles/cloudkms.admin`) role on the project where your Cloud HSM keys reside. This separation of duties ensures that no single principal can both manage and destroy keys.

[Set a deny policy](https://docs.cloud.google.com/iam/docs/deny-access#create-deny-policy) based on the following example configuration:
    
    
    displayName: Deny KMS key destruction and deletion
    rules:
    - description: "Denies destroy and delete permissions on Cloud KMS keys for all principals."
      denyRule:
        deniedPrincipals:
        - "principalSet://goog/public:all"
        deniedPermissions:
        - "cloudkms.googleapis.com/cryptoKeyVersions.destroy"
        - "cloudkms.googleapis.com/cryptoKeys.delete"
    

For more information about IAM deny policies, see [IAM deny policy overview](https://docs.cloud.google.com/iam/docs/deny-overview).

### Enforce Organization Policy constraints for key destruction

Beyond IAM, you can enforce security guardrails at the organization or folder level using Organization Policy constraints. These constraints act as hard requirements that constrain what kinds of resources can be created and how they can be configured. Enforced Organization Policy constraints can't be bypassed, even by principals who have the required permissions to complete the prohibited action. Enforced Organization Policy constraints can't be canceled without a role such as Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) on the organization.

  * **Minimum destruction duration** (`constraints/cloudkms.minimumDestroyScheduledDuration`): Mandates a minimum _scheduled for destruction_ duration (for example, 90 or 120 days) across all keys in the organization or resource where the policy is enabled. This constraint prevents any user from shortening the recovery window below the configured minimum value.
  * **Disable before destroy** (`constraints/cloudkms.disableBeforeDestroy`): Requires that a key version be in the `DISABLED` state before it can be scheduled for destruction. This constraint adds a mandatory step to the destruction workflow, increasing the visibility of the action in audit logs.



For more information, see [Control key version destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction).

### Maximize the key destruction window

When a key version is scheduled for destruction, it enters a "soft delete" period. While a key version is in the _scheduled for destruction_ state, you can restore the key to cancel the key destruction. Setting this configurable period to the maximum length of 120 days helps to ensure that you have adequate time to restore a key version that was accidentally or maliciously scheduled for destruction. You can only set this value when you create the key.

When you restore a key version that was scheduled for destruction, the key version state is set to `DISABLED`. You must then re-enable the key version to restore access to your encrypted Google Workspace data.

The following gcloud CLI command creates an HSM-backed key with a 120-day scheduled destruction duration:
    
    
    gcloud kms keys create KEY_NAME \
        --location LOCATION \
        --keyring KEY_RING \
        --purpose encryption \
        --protection-level hsm \
        --destroy-scheduled-duration 120d
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.



To enforce this duration across all keys in your organization rather than setting it on each key, you can [define and enforce a custom Organization Policy constraint](https://docs.cloud.google.com/organization-policy/create-custom-constraints). The following example constraint only lets users create a key if the scheduled destruction duration is between 90 and 120 days:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.limitScheduledDestruction
    resourceTypes:
    - cloudkms.googleapis.com/CryptoKey
    methodTypes:
    - CREATE
    condition: "resource.destroyScheduledDuration >= duration('7776000s') && resource.destroyScheduledDuration <= duration('10368000s')"
    actionType: ALLOW
    displayName: Require scheduled destruction duration between 90 and 120 days
    description: Allows key creation only if the destroyScheduledDuration is between 90 and 120 days.
    

Replace `ORGANIZATION_ID` with your organization's numeric ID.

For more information about configuring the scheduled destruction duration, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore). For more information about using custom Organization Policy constraints with Cloud KMS, see [Create custom Organization Policy constraints for Cloud KMS](https://docs.cloud.google.com/kms/docs/custom-org-policies).

## Protect your infrastructure and project

The guardrails discussed earlier in this document focus on preventing key destruction and deletion. However, you also need guardrails to prevent deletion of the key project. Use the following guardrails to secure the project environment that houses your Google Workspace keys.

### Enforce project liens

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A project lien prevents a project from being deleted. Even a user with the Project Owner (`roles/owner`) role can't shut down the project while a lien is active. This is the most effective way to prevent the accidental or unauthorized deletion of the project where your Google Workspace keys reside.

For more information about project liens, see [Protect projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens#placing_a_lien_on_a_project).

### Understand the project recovery window

If a project is successfully deleted—for example, after a project lien ([Preview](https://cloud.google.com/products#product-launch-stages)) is removed—it enters the 30-day recovery window. During this time, a user with the Project Owner (`roles/owner`) or Organization Admin (`roles/resourcemanager.organizationAdmin`) role can restore the project. After 30 days, the project and all keys within it are permanently purged.

We recommend that you keep project liens in place and rely on the recovery window only as a last resort.

For more information about project recovery, see [Restore a deleted project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#restoring_a_project).

### Use VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you define a security perimeter around your Cloud HSM project. This helps ensure that the Cloud KMS API can only be accessed from trusted networks or specific identities, mitigating the risk of unauthorized administrative actions from outside your corporate environment.

## Ensure key material sovereignty with imported keys (BYOK)

For most organizations, we recommend that you let Cloud HSM generate and manage key material for you.

However, if you require "bring your own key (BYOK)" capabilities, then you can generate your key material on-premises and [import it](https://docs.cloud.google.com/kms/docs/key-import) into Cloud HSM. This BYOK approach lets you satisfy requirements such as maintaining an independent, on-premises copy of your key material—for example, to satisfy data sovereignty mandates or to recover from a catastrophic loss of key material. This approach gives you an independent copy of the key material that you can re-import if the key version in Cloud KMS is destroyed.

### Re-import to the same version

Cloud KMS lets you re-import identical key material into the destroyed key version, so that the resource identifier and URI are the same as the original imported key version. This lets you continue to use the same Google Workspace configurations. When you re-import a key version used in a Google Workspace configuration, data access is restored as soon as the key version finishes importing.

For more information about re-importing a destroyed key version, see [Re-importing a destroyed key version](https://docs.cloud.google.com/kms/docs/importing-a-key#re-importing_a_destroyed_key).

## Advanced protection with Single-tenant Cloud HSM

For customers requiring the highest level of isolation, Single-tenant Cloud HSM provides dedicated HSM partitions. Your Single-tenant Cloud HSM instance is created and managed by using quorum authentication, which requires approval from a configured minimum number of quorum members before critical operations, such as deleting the Single-tenant Cloud HSM instance. This helps prevent a single compromised account from destroying your Single-tenant Cloud HSM instance. The following practices apply when you use Single-tenant Cloud HSM. For more information, see [Quorum-based authentication](https://docs.cloud.google.com/kms/docs/single-tenant-hsm#quorum).

### Separate infrastructure and keys across projects

Create the Single-tenant Cloud HSM instance and your Google Workspace keys in separate projects. Separating the resource projects helps to ensure that a user with administrative roles on the key project has no authority over the underlying Single-tenant Cloud HSM instance. This separation of duties between infrastructure management and key management reduces the risk of unauthorized infrastructure-level actions.

For more information about Single-tenant Cloud HSM, see [Single-tenant Cloud HSM overview](https://docs.cloud.google.com/kms/docs/single-tenant-hsm).

## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
IAM deny policies | Enforce folder-level deny policies to block key destruction and deletion, even for highly privileged users.  
Organization policy constraints | Enforce constraints to mandate a minimum recovery period and require keys to be disabled before they can be destroyed.  
Scheduled for destruction period | 

  * Create your key with the _scheduled for destruction_ value set to the maximum of 120 days. Alternately, you can choose a shorter duration, but make sure that it's long enough to ensure that keys can be recovered if they are scheduled for destruction.
  * You can use a custom Organization Policy constraint to ensure that all keys are created with an appropriate duration for your needs.

  
Project liens | Enforce project liens to prevent the deletion of the project housing your encryption keys.  
VPC Service Controls perimeter | Define a VPC Service Controls perimeter to restrict Cloud KMS API access to trusted networks and identities.  
BYOK re-import | Generate key material on-premises and use re-import to recover destroyed key versions without changing resource names.  
Cross-project architecture | If you use Single-tenant Cloud HSM, separate the Single-tenant Cloud HSM instance and keys across different projects to enforce separation of duties.  
  
## What's next

  * [Onboard to Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace).
  * Learn more about [Cloud HSM](https://docs.cloud.google.com/docs/security/cloud-hsm-architecture#regulatory-compliance) and its regulatory compliance certifications.
  * Review [best practices for CMEK](https://docs.cloud.google.com/kms/docs/cmek-best-practices) for broader key management guidance.
  * Learn more about [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).
  * Learn more about [custom Organization Policy constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
