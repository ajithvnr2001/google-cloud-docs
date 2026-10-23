---
url: https://docs.cloud.google.com/kms/docs/control-autokey-usage/
title: Control Autokey usage \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:14.892332+00:00
---

# Control Autokey usage  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/control-autokey-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Control Autokey usage Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use IAM deny policies and organization policy constraints to control how Autokey is used within an organization or folder. Both of these guardrails can only be modified with organization-level roles, so they can't be overridden by principals with Owner or Admin roles at the folder or project level.

The following use cases are supported:

  * Require keys to be created by Autokey. You can block principals from manually creating keys so that all keys are created by Autokey. In resources where Autokey isn't enabled, you won't be able to create keys.
  * Restrict Autokey to allow only dedicated-project key storage or to only same-project key storage.
  * Block Autokey entirely. This ensures that all keys are created manually.



## IAM versus organization policy

Both IAM and organization policies let you set guardrails to control how Cloud KMS Autokey can be used in your organization.

IAM controls who is authorized to perform which actions on which resources. You can use IAM to constrain _which principals_ can enable and use Autokey in your organization.

Organization policy controls what resources can be created and how they can be configured. You can use custom organization policies to constrain _where_ and _how_ Autokey can be enabled.

You can use IAM and organization policy together to create a robust system of guardrails to control who can enable and use Autokey and where and they can do so.

## Before you begin

To get the permissions that you need to control Autokey usage, ask your administrator to grant you the following IAM roles on the organization: 

  * Set organization policy: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) 
  * Set IAM deny policies: [Deny Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use IAM deny policies to control Autokey

IAM deny policies provide top-down control over which principals can perform which actions. Deny policies set on a resource can't be overridden by IAM role grants or deny policies set on a child resource. Principals can't complete actions that require denied permissions, even if the permission is included in a role that they have.

To learn how to create IAM deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

The following table shows some example use cases for IAM deny policies, including permissions that you can deny to control Autokey in your organization and the effect of denying each permission.

Use case | Denied permission | Principals | Effect  
---|---|---|---  
Prohibit enabling Autokey | `cloudkms.autokeyConfigs.update` | Any | Selected principals can't create new `AutokeyConfig` resources or update existing ones. Any existing `AutokeyConfig` resources remain in effect and can still be used.  
Prohibit using Autokey | `cloudkms.keyHandles.create` | Any | Selected principals can't create new `KeyHandle` resources, so they can't create new protected resources using Autokey, even where Autokey is enabled.  
Prohibit manual key creation | `cloudkms.cryptoKeys.create` | Any except Cloud KMS Service Agent | Selected principals can't create new keys. When you exempt only the Cloud KMS Service Agent, Autokey is the only way to create new keys.  
Only IaC can change Autokey configurations | `cloudkms.autokeyConfigs.update` | All except your Terraform execution agent | Selected principles can't create new `AutokeyConfig` resources or update existing ones. When you exempt your Terraform principal, your Autokey configurations are controlled by your Infrastructure as Code (IaC) pipeline.  
  
## Use custom organization policy constraints to control Autokey

Custom organization policy constraints provide bottom-up control of where and how Autokey can be configured. Constraints can be overridden by constraints enforced on a child resource. However, changing constraints requires organization-level permissions, so principals with folder- or project-level permissions can't override the constraints. While constraints are enforced, principals can't complete prohibited actions, even if they have the permissions required to do so.

To learn how to enforce custom constraints in your organization, see [Create custom organization policy constraints for Cloud KMS](https://docs.cloud.google.com/kms/docs/custom-org-policies).

You can combine the custom organization policy constraints described here with other [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

### Restrict Autokey mode

You can restrict Autokey functionality by conditionally blocking the creation of `AutokeyConfig` resources. The following sample constraint definition prohibits the creation or update of `AutokeyConfig` resources based on their `keyProjectResolutionMode`.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictAutokeyKeyStorage
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.keyProjectResolutionMode == 'KEY_PROJECT_RESOLUTION_MODE')"
        actionType: DENY
        displayName: Restrict Autokey key storage mode
        description: >
          Prevent creation or update of AutokeyConfig resources with
          `KEY_PROJECT_RESOLUTION_MODE` key resolution mode.
    

Replace `KEY_PROJECT_RESOLUTION_MODE` with the `keyProjectResolutionMode` that you want to block—for example, to prevent anyone in your organization from using same-project key storage in their projects, set this value to `RESOURCE_PROJECT`.

### Prohibit creating Autokey configuration on a folder

You can use custom organization policies to block Autokey from being enabled within a folder by blocking the creation of all `AutokeyConfig` resources.

The following sample constraint definition prohibits the creation of `AutokeyConfig` resources within a named folder. While this constraint is enforced, any existing configurations can still be modified.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.noNewAutokeyConfigFolder
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        condition: "resource.name == 'folders/FOLDER_ID/autokeyConfig'"
        actionType: DENY
        displayName: Prohibit Autokey within FOLDER_ID
        description: >
          Prevent creation of new AutokeyConfig resources within
          folders/FOLDER_ID.
    

Replace the following:

  * `ORGANIZATION_ID`: the identifier of your organization.
  * `FOLDER_ID` with the identifier of the folder where you want to block Autokey.



### Prohibit creating Autokey configuration within an organization

You can use custom organization policies to block Autokey from being enabled within your entire organization by blocking the creation of all `AutokeyConfig` resources.

The following sample constraint definition prohibits the creation of `AutokeyConfig` resources within your entire organization. While this constraint is enforced, any existing configurations can still be modified.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.noNewAutokeyConfigOrg
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        condition: "resource.name.endsWith('/autokeyConfig')"
        actionType: DENY
        displayName: Prohibit Autokey within ORGANIZATION_ID
        description: >
          Prevent creation of new AutokeyConfig resources within organization
          ORGANIZATION_ID.
    

Replace `ORGANIZATION_ID` with the identifier of your organization.

### Prohibit changing Autokey configuration on a folder

You can use custom organization policies to block Autokey configurations from being changed within a folder by blocking the creation or update of all `AutokeyConfig` resources.

The following sample constraint definition prohibits the creation or update of `AutokeyConfig` resources within a named folder.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.noChangeAutokeyConfigFolder
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.name == 'folders/FOLDER_ID/autokeyConfig'"
        actionType: DENY
        displayName: Prohibit Autokey within FOLDER_ID
        description: >
          Prevent creation or update of AutokeyConfig resources within
          folders/FOLDER_ID.
    

Replace the following:

  * `ORGANIZATION_ID`: the identifier of your organization.
  * `FOLDER_ID` with the identifier of the folder where you want to block Autokey.



### Prohibit changing Autokey configuration within an organization

You can use custom organization policies to block Autokey configurations from being changed anywhere in your organization by blocking the creation or update of all `AutokeyConfig` resources.

The following sample constraint definition prohibits the creation or update of `AutokeyConfig` resources within your entire organization.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.noChangeAutokeyConfigOrg
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        - UPDATE
        condition: condition: "resource.name.endsWith('/autokeyConfig')"
        actionType: DENY
        displayName: Prohibit Autokey within ORGANIZATION_ID
        description: >
          Prevent creation or update of AutokeyConfig resources within
          ORGANIZATION_ID.
    

Replace `ORGANIZATION_ID` with the identifier of your organization.

### Allow only `DISABLED` Autokey configuration

The following sample constraint definition prohibits anyone from creating or updating a `AutokeyConfig` resource within an entire organization, unless the `keyProjectResolutionMode` is explicitly set to `DISABLED`.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.onlyDisabledAutokeyConfig
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.keyProjectResolutionMode=='DISABLED'"
        actionType: ALLOW
        displayName: Prohibit Autokey within the organization
        description: >
          Prevent creation or update of `AutokeyConfig` resources within
          organization ORGANIZATION_ID unless the `keyProjectResolutionMode`
          is `DISABLED`.
    

### Prohibit project-level Autokey configuration

The following sample constraint definition prohibits anyone from creating or updating a `AutokeyConfig` resource on a project, without blocking folder-level configurations. While this constraint is enforced, any previously existing project-level `AutokeyConfig` resources remain in effect, but all other projects must continue to inherit the `AutokeyConfig` from their parent folder.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.noAutokeyConfigProject
        resourceTypes:
        - cloudkms.googleapis.com/AutokeyConfig
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.name.startsWith('projects/')"
        actionType: DENY
        displayName: Block project-level Autokey within the organization
        description: >
          Prevent creation or update of `AutokeyConfig` resources on projects within
          organization ORGANIZATION_ID. Existing project-level AutokeyConfig
          resources remain in effect, but all other projects must inherit the
          AutokeyConfig from their parent folder.
    

## Example use cases

The following sections provide examples that combine IAM deny policies, custom organization policies, and standard organization policies together.

### Require keys to be created by Autokey

If you want to require CMEK using Autokey within a folder, you can do so by combining IAM access controls with CMEK organization policies. This works by removing key creation permissions from principals other than the Cloud KMS service agent, and then requiring that all resources are protected by CMEK using the Autokey key project.

To enforce Autokey usage within a folder, complete the following steps:

  1. Block manual key creation in the key project by enforcing an IAM deny policy. In the deny policy, deny the `cloudkms.cryptoKeys.create` permission to all principals except the Cloud KMS Service Agent. If the folder uses dedicated-project key storage, apply the deny policy to the dedicated key project. If the folder uses same-project key storage, apply the deny policy to the resource projects.

When keys can't be manually created, then only keys created by Autokey can be created in these projects.

**Caution:** If you need to manually create keys to use with services that aren't compatible with Autokey, then you will need to create those keys in a project where the `cloudkms.cryptoKeys.create` permission isn't denied.
  2. Require that newly created resources within the folder must be protected using CMEK by enforcing the `constraints/gcp.restrictNonCmekServices` constraint.

For more information about this constraint, including the list of services that support the constraint, see [Require CMEK protection](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek).

  3. Require that keys used for CMEK must be from a dedicated key project or from projects where same-project key storage is enabled by enforcing the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint. For more information, about this constraint, including the list of services that support the constraint, see [Limit the use of Cloud KMS keys for CMEK](https://docs.cloud.google.com/kms/docs/cmek-org-policy#project-constraint).




### Prohibit Autokey entirely

If you want to block the use of Autokey entirely within an organization or folder, you can do so using either IAM deny policies or custom organization policy constraints. For multilayer assurances, you can use both together.

To block Autokey entirely within an organization or folder, complete the following steps:

  1. If Autokey is already enabled anywhere in the organization or folder, [disable Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey#disable-autokey) first.

  2. Block users from configuring Autokey by enforcing an IAM deny policy. In the deny policy, deny the `cloudkms.autokeyConfigs.update` permission to all principals. When Autokey is disabled everywhere and no principals are able to modify `AutokeyConfig` resources, Autokey remains fully disabled.

  3. Optional: The preceding steps are sufficient to prevent anyone from enabling Autokey. However, if you want another layer of assurance, then you can also enforce a custom organization policy constraint to only allow `AutokeyConfig` resources where Autokey is disabled.




If you enforce both the IAM deny policy and the custom organization policy constraint described here, no principal could enable Autokey in the resource without first cancelling or updating both of these guardrails.

## What's next

  * Learn more about [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).
  * Learn more about [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).
  * Learn more about the [Organization Policy Service service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about [custom organization policy constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
