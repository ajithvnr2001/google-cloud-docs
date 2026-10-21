---
url: https://docs.cloud.google.com/organization-policy/domain-restricted-sharing/
title: Domain-restricted sharing \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:04.521667+00:00
---

# Domain-restricted sharing  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/domain-restricted-sharing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Domain-restricted sharing Stay organized with collections  Save and categorize content based on your preferences. 

Domain-restricted sharing lets you limit resource sharing based on a domain or organization resource. When domain-restricted sharing is active, only principals that belong to allowed domains or organizations can be granted IAM roles in your Google Cloud organization. [Service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) are not part of your organization, even if they are associated with resources in your organization, so they are blocked by domain-restricted sharing.

## Methods for restricting sharing by domain

There are several ways that you can use Organization Policy Service to limit resource sharing based on a domain or organization resource:

  * **The`iam.managed.allowedPolicyMembers` managed constraint**: You can enforce this managed constraint to allow roles to be granted to only the principals and principal sets that you list in the constraint.

With this managed constraint, you list the principals and principal sets that you want to allow roles to be granted to. To allow roles to be granted to all principals in your organization, include the organization's principal set in the constraint.

To learn how to set this constraint, see [Use the `iam.managed.allowedPolicyMembers` constraint to implement domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains#managed-constraint).

  * **A custom organization policy referencing the`iam.googleapis.com/AllowPolicy` resource**: You can use a custom organization policy to allow roles to be granted to only a specific set of principals.

In most cases, you should use the `iam.managed.allowedPolicyMembers` managed constraint instead of using a custom organization policy. However, the following configuration options are only available if you use custom organization policies:

    * Configuring allowed principals based on member type
    * Preventing specific principals from being granted roles
    * Allowing roles to be granted to special principals like `allUsers` and `allAuthenticatedUsers`

To set up domain-restricted sharing with custom organization policies, you use the following CEL functions to define who can be granted a role in your organization:

    * [`memberInPrincipalSet`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-in-principal-set)
    * [`memberTypeMatches`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-type-matches)
    * [`memberSubjectMatches`](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#member-subject-matches)

To allow roles to be granted to all principals in your organization, specify your organization's principal set in the `memberInPrincipalSet` function and include the organization's principal set in the constraint.

To learn more about how to create custom organization policies using these CEL functions, see [Use custom organization policies to implement domain restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains#custom-constraints).

  * **The`iam.allowedPolicyMemberDomains` legacy managed constraint**: You can enforce this legacy managed constraint to only allow roles to be granted to principals in your organization. You can limit access based on your organization principal set or your Google Workspace customer ID. To see differences between these identifiers, see Organization principal set versus Google Workspace customer ID on this page.

This constraint doesn't let you configure exceptions for specific principals. For example, imagine that you need to grant a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) in an organization that enforces the `iam.allowedPolicyMemberDomains` constraint. Service agents are created and managed by Google Cloud, and even if they are associated with resources in your organization, they aren't considered part of your organization, your Google Workspace account, or your Cloud Identity domain. As a result, to grant a role to the service agent, you need to disable the constraint, grant the role, and then re-enable the constraint.

You can override the organization policy at the folder or project level to change which users are allowed to be granted roles in which folders or projects. For more information, see [Override the organization policy for a project](https://docs.cloud.google.com/organization-policy/create-organization-policies#override_BOOLEAN_CONSTRAINT).

To learn how to set this constraint, see [Use the `iam.allowedPolicyMemberDomains` constraint to implement domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains#predefined-constraint).

**Note** : If your organization was created on or after May 3, 2024, then the `iam.allowedPolicyMemberDomains` legacy managed constraint is enforced by default, with your domain listed as the only allowed value. 




## How domain-restricted sharing works

When you use an organization policy to enforce domain-restricted sharing, no principals outside of the domains and individuals that you specify can be granted IAM roles in your organization.

The following sections outline some key details about how domain-restricted sharing constraints work in your organization.

### Constraints are not retroactive

Organization policy constraints are not retroactive. After a domain restriction is set, the limitation applies to allow policy changes made from that point forward, and not to any previous changes.

For example, consider two related organizations: `examplepetstore.com` and `altostrat.com`. You have granted an `examplepetstore.com` identity an IAM role in `altostrat.com`. Later, you decided to restrict identities by domain, and implemented an organization policy with the domain restriction constraint in `altostrat.com`. In this case, the existing `examplepetstore.com` identities wouldn't lose access in altostrat.com. From that point, you could only grant IAM roles to identities from the altostrat.com domain.

### Constraints apply whenever an IAM policy is set

Domain restriction constraints apply to all actions where an IAM policy is set. This includes automated actions. For example, the constraints apply to changes that a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) makes in response to another action. For example, if you have an automated service that imports BigQuery datasets, a BigQuery service agent will make IAM policy changes on the newly created dataset. This action would be restricted by the domain restriction constraint and blocked.

### Constraints don't automatically include your domain

Your organization's domain isn't automatically added to the allowed list of a policy when you set the domain restriction constraint. To let principals in your domain be granted IAM roles in your organization, you must add your domain explicitly. If you don't add your domain and the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) is removed from all users in your domain, then the organization policy becomes inaccessible.

### Google groups and domain-restricted sharing

If the domain restriction constraint is enforced in your organization, then you might not be able to grant roles to newly created Google groups, even if the groups belong to an allowed domain. This is because it can take up to 24 hours for a group to fully propagate through Google Cloud. If you can't grant a role to a newly created Google group, wait 24 hours and then try again.

Additionally, when evaluating whether a group belongs to an allowed domain, IAM only evaluates the group's domain. It doesn't evaluate the domains of any of the group's members. As a result, project administrators can bypass the domain restriction constraint by adding outside members to Google groups, and then granting roles to those Google groups.

To ensure that project administrators can't bypass the domain restriction constraint, the Google Workspace administrator should ensure that group owners cannot [allow members from outside of the domain](https://support.google.com/a/answer/167097) in the Google Workspace administrator panel.

## Organization principal set versus Google Workspace customer ID

If you use the `iam.allowedPolicyMemberDomains` legacy managed constraint to implement domain-restricted sharing, then you can limit access based on either your organization principal set or your Google Workspace customer ID.

Using your organization principal set allows the following principals to be granted roles in your organization:

  * All workforce identity pools in your organization
  * All service accounts associated with resources in your organization
  * All workload identity pools in any project in your organization
  * All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with resources in your organization



Using your Google Workspace customer ID allows the following principals to be granted roles in your organization:

  * All identities in all domains, including subdomains, associated with your Google Workspace customer ID
  * All workforce identity pools in your organization
  * All service accounts associated with resources in your organization
  * All workload identity pools in any project in your organization
  * All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with resources in your organization



If you want to implement domain-restricted sharing for specific subdomains, then you need to create a separate Google Workspace account for each subdomain. For more information about managing multiple Google Workspace accounts, see [Managing multiple organizations](https://docs.cloud.google.com/resource-manager/docs/managing-multiple-orgs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
