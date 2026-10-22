---
url: https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices/
title: Super administrator account best practices \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:52.705283+00:00
---

# Super administrator account best practices  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Super administrator account best practices Stay organized with collections  Save and categorize content based on your preferences. 

To configure your Google Cloud organization resource, you need to use a Google Workspace or Cloud Identity super admin account. This page describes best practices for using your Google Workspace or Cloud Identity super admin accounts with your Google Cloud organization resource.

## Account types

A Google Workspace super admin account has a set of administrative capabilities that includes Cloud Identity. This provides a single set of identity management controls for use across all Google services, such as documents, sheets, Google Cloud, and so forth.

A Cloud Identity account only provides authentication and identity management functionality, independent of Google Workspace.

## Designate Organization Administrators

After you have acquired a new organization resource, you designate one or more [Organization Administrators](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#adding_an_organization_admin). This role has a smaller set of permissions that are designed to manage your day to day organization operations.

You should also create a private Google Cloud administrator group in your Google Workspace or Cloud Identity super admin account. Add your Organization Administrator users to this group, but not your super admin user. Grant this group the Organization Administrator Identity and Access Management (IAM) role or a limited subset of the role's permissions.

We recommend keeping your super admin account separate from your Organization Administrator group. As a super admin, you can grant the Organization Administrator role to the appropriate user best positioned to manage the organization resource and its contents.

For information about managing access control for your organization resource using allow policies, see [Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).

## Set appropriate roles

Google Workspace and Cloud Identity has administrative roles that are not as permissive as the super administrator role. We recommend following the principle of least privilege by granting users the minimum set of permissions they need to manage users and groups.

## Discourage super admin account usage

The Google Workspace and Cloud Identity super admin account has a powerful set of permissions that are not necessary for use in the daily administration of your organization. You should implement policies that will secure your super admin accounts and make users less likely to attempt to use them for day-to-day operations, such as:

  * Enforce [multi-factor authentication](https://docs.cloud.google.com/identity/solutions/enforce-mfa) on your super admin accounts as well as all accounts that have elevated privileges.

  * Use a security key or other physical authentication device to enforce two-step verification.

  * For the initial super admin account, ensure that the security key is kept in a safe place, preferably at your physical location.

  * Give super admins a separate account that requires a separate login. For example, user alice@example.com could have a super admin account alice-admin@example.com.

    * If you are synchronizing with a third-party identity protocol, ensure you apply the same suspension policy to Cloud Identity and the corresponding third-party identity.
  * If you have a Google Workspace enterprise or business account or a Cloud Identity premium account, you can enforce a [short sign-in](https://support.google.com/a/answer/7576830?hl=en) period for any super admin accounts.

  * Follow the guidance in the [security best practice patterns for administrator accounts](https://support.google.com/a/answer/9011373?hl=en).




## API call alerts

Use Google Cloud Observability to [set up alerts](https://www.youtube.com/watch?v=LdGqmnoowc8) that will notify you when a [`SetIamPolicy()`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) API call is made. This will send an alert when anyone modifies any allow policy.

## Account recovery process

Ensure that the Organization Administrators are familiar with the super admin [account recovery process](https://support.google.com/a/answer/33561?hl=en). This process will help you recover your account in the event that super admin credentials are lost or compromised.

**Note:** By default, self-recovery for super administrator accounts is disabled for new Cloud Identity and Google Workspace customers. We recommend keeping self-recovery disabled as a security best practice.

## Multiple organization resources

We recommend using [folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) to manage parts of your organization that you want to manage separately. If you want to use multiple organization resources instead, you will need multiple Google Workspace or Cloud Identity accounts. For information about the implications of using multiple Google Workspace and Cloud Identity, see [Manage multiple organization resources](https://docs.cloud.google.com/resource-manager/docs/managing-multiple-orgs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
