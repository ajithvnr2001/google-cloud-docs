---
url: https://docs.cloud.google.com/resource-manager/docs/manage-baseline-constraints/
title: Manage Google Cloud security baseline constraints \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:14.057330+00:00
---

# Manage Google Cloud security baseline constraints  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-baseline-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Manage Google Cloud security baseline constraints Stay organized with collections  Save and categorize content based on your preferences. 

If you are a new customer, Google Cloud automatically provisions an organization resource for your domain in the following scenarios:

  * A user from your domain logs in for the first time.
  * A user creates a billing account that does not have an associated organization resource.



This organization resource's default configuration, characterized by unrestricted access, can make the infrastructure susceptible to security breaches. For example, default service account key creation is a critical vulnerability exposing systems to potential breaches.

Google Cloud security baseline addresses insecure security postures with a bundle of organization policies that are enforced when an organization resource is created. For more information, see [getting an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring). Examples of these organization policies include disabling service account key creation and disabling service account key upload.

When an existing user creates an organization, the security posture for the new organization resource might be different from the existing organization resources. Google Cloud security baseline constraints are enforced for all organizations created on or after May 3, 2024. Some organizations created between February 2024 and April 2024 might also have these default policy enforcements set. To view organization policies applied to your organization, see [Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies).

## Before you begin

For more information about what organization policies and constraints are and how they work, see the [introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage organization policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies:

  * `orgpolicy.constraints.list`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can delegate the administration of organization policies by adding [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the Organization policy administrator role binding. To control the resources where a principal can manage organization policies, you can make the role binding conditional on a particular [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For more information, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints/access-control-org#delegate-admin). 

## Organization policies enforced on organization resources

The following table lists the organization policy constraints that are automatically enforced when you create an organization resource.

Organization policy name | Organization policy constraint | Description | Impact of enforcement  
---|---|---|---  
[Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) | `constraints/iam.managed.disableServiceAccountKeyCreation` | Prevent users from creating persistent keys for service accounts. For information about managing service account keys, see [Provide alternatives to creating service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#alternatives). | Reduces the risk of exposed service account credentials.  
[Disable service account key upload](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload) | `constraints/iam.disableServiceAccountKeyUpload` | Prevent the upload of external public keys to service accounts. For information about accessing resources without service account keys, see these [best practices](https://docs.cloud.google.com/iam/docs/use-workload-identity-federation-to-let-customers-access-their-cloud-resources#best_practices). | Reduces the risk of exposed service account credentials.  
[Prevent the Editor role from being granted to default service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) | `constraints/iam.automaticIamGrantsForDefaultServiceAccounts` | Prevent default service accounts from receiving the overly permissive IAM Editor role at creation. | The Editor role lets the service account create and delete resources for most Google Cloud services, which creates a vulnerability if the service account gets compromised.  
[Restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#predefined-constraint) | `constraints/iam.allowedPolicyMemberDomains` | Limit resource sharing to identities that belong to a particular organization resource or Google Workspace customer ID. | Leaving the organization resource open to access by actors with domains other than the customer's own creates a vulnerability.  
[Restrict contacts by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services) | `constraints/essentialcontacts.managed.allowedContactDomains` | Limit Essential Contacts to only allow managed user identities in selected domains to receive platform notifications. | A bad actor with a different domain might get added as Essential Contacts, leading to a compromised security posture.  
[Restrict protocol forwarding based on type of IP address](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#restrict_protocol_forwarding_types) | `constraints/compute.managed.restrictProtocolForwardingCreationForTypes` | Restrict the configuration of protocol forwarding for internal IP addresses only. | Protects target instances from exposure to external traffic.  
[Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access) | `constraints/storage.uniformBucketLevelAccess` | Prevent Cloud Storage buckets from using per-object ACL (a separate system from allow and deny policies) to provide access. | Enforces consistency for access management and auditing.  
  
Note: For some organizations created after August 15, 2024, the `constraints/compute.restrictProtocolForwardingCreationForTypes` organization policy constraint might already be applied.

## Manage enforcement of organization policies

You can manage the enforcement of organization policies in the following ways:

### List organization policies

To check whether the Google Cloud security baseline constraints are enforced on your organization, use the following command:
    
    
    gcloud resource-manager org-policies list --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the unique identifier of your organization.

### Disable organization policies

To disable or delete an organization policy, run the following command:
    
    
    gcloud org-policies delete CONSTRAINT_NAME --organization=ORGANIZATION_ID

Replace the following:

  * `CONSTRAINT_NAME`: the name of the organization policy constraint that you want to delete—for example, `iam.allowedPolicyMemberDomains`
  * `ORGANIZATION_ID`: the unique identifier of your organization



## What's next

For more information about creating and managing organization policies, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
