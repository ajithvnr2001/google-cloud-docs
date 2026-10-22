---
url: https://docs.cloud.google.com/iam/docs/temporary-elevated-access/
title: Temporary elevated access overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:02.483452+00:00
---

# Temporary elevated access overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/temporary-elevated-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Temporary elevated access overview Stay organized with collections  Save and categorize content based on your preferences. 

One way to protect sensitive resources is to limit access to them. However, limiting access to sensitive resources also creates friction for anyone who occasionally needs to access those resources. For example, a user might need break-glass, or emergency, access to sensitive resources to resolve an incident.

In these situations, we recommend giving the user permission to access the resource temporarily. We also recommend that, to improve auditing, you record the user's justification for accessing the resource.

In Google Cloud, there are several ways that you can manage this kind of temporary elevated access.

## Privileged Access Manager

You can use Privileged Access Manager (PAM) to manage just-in-time temporary privilege elevation for select principals, and to view audit logs afterwards to find out who had access to what and when.

You might want to provide temporary privilege elevation through Privileged Access Manager in the following situations:

  * **Grant emergency access** : Allow select emergency responders to perform critical tasks without having to wait for approval. You can require justifications for emergency access requests for additional context.

  * **Control access to sensitive resources** : Tightly control access to sensitive resources, requiring approvals and business justifications. Privileged Access Manager can also be used to audit how this access was used—for example, when granted roles were active for a user, which resources were accessible during that time, the justification for access, and who approved it.

For example, you can use Privileged Access Manager to do the following:

    * Give developers temporary access to production environments for troubleshooting or deployments.

    * Give support engineers access to sensitive customer data for specific tasks.

    * Give database administrators elevated privileges for maintenance or configuration changes.

  * **Implement granular least privilege** : Assigning administrative roles or broad access to all users can increase the attack surface. To prevent this, administrators can assign least privilege permanent roles and use Privileged Access Manager to provide temporary, time-bound elevated access for specific tasks when needed. Administrators can create entitlements with tag-based conditions and enforce requesters to create grant requests with customized scope and withdraw grants after the task is completed. This significantly reduces opportunities for misuse and reinforces the principle of "just-in-time" access.

  * **Automate privileged access approvals** : To enhance efficiency, you can configure service accounts or agent identities as approvers within your DevOps pipelines. These accounts can automate programmatic approvals by validating tickets directly from ITSM systems, thereby eliminating slow manual checks.

  * **Help secure service accounts and agent identities** : Instead of permanently granting roles to service accounts or agent identities, allow them to self-elevate and assume roles only when needed for automated tasks.

  * **Mitigate insider threats and accidental misuse** : With multi-party approvals, you can require a second approver for grant requests. This approach reduces the risk of a single administrator or a compromised account approving malicious access.

  * **Manage access for contractors and extended workforce** : Grant contractors or members of the extended workforce temporary, time-bound access to resources, with approvals and justifications required.

  * **Transition permanent roles to temporary access** : Remediate excessive permissions identified by [IAM recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Instead of permanently revoking a role, you can shift it to a temporary, on-demand entitlement. For more information, see [Remediate excessive permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).




For more information on setting up Privileged Access Manager, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview).

For more information on requesting temporary elevation, see [Request temporary elevated access](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access).

## Google groups

One way to manage temporary elevated access is to grant a Google group access to sensitive resources, then add and remove users from that group to control their access.

To set up a Google group for temporary elevated access, first [create a group](https://support.google.com/groups/answer/2464926), then grant it the roles that you want to temporarily give to users. If you use [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview), also consider making the group [exempt from any relevant deny rules](https://docs.cloud.google.com/iam/docs/deny-overview#deny-rules) to avoid unexpected denials.

After you set up your group, you can add and remove users to modify their access. If you use the Google Groups API, you can temporarily add users to a group by using [membership expiration](https://docs.cloud.google.com/identity/docs/how-to/manage-expirations).

If you want to record the user's justifications for accessing sensitive resources, you must define your own operational processes and tooling.

For example, to manage emergency access to Compute Engine resources, you could create a group, `emergency-compute-access@example.com`, and grant it the Compute Admin role (`roles/compute.admin`). If a user needs emergency administrative access to compute resources, you can add them to the `emergency-compute-access@example.com` group. After the emergency is resolved, you can remove them from the group.

## IAM Conditions

You can use IAM Conditions to grant users expiring access to Google Cloud resources. For more information, see [Configure temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access).

If you want to record the user's justifications for accessing sensitive resources, you must define your own operational processes and tooling.

Expired role bindings aren't automatically removed from your allow policies. To ensure that your allow policies don't exceed the maximum size for allow policies, we recommend periodically removing expired role bindings.

Deny policies don't support time-based conditions. As a result, you can't use conditions in deny policies to temporarily exempt a user from a deny rule.

## Just-in-time privileged access

Just-In-Time Access is an open source application that uses IAM Conditions to grant users just-in-time privileged access to Google Cloud resources. This application is designed to run on App Engine or Cloud Run.

This application has the following benefits over manually adding conditional role bindings:

  * Users can search for roles that they can activate with Just-In-Time Access.
  * Users are required to provide justifications before getting access.
  * The application replaces the existing conditional binding instead of creating new bindings, which helps maintain your IAM allow policy size.



For more information about Just-In-Time Access, see [Manage just-in-time privileged access to projects](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project).

**Note:** The Just-In-Time Access application can't give a user access if they've been [explicitly denied](https://docs.cloud.google.com/iam/docs/deny-overview).

## Service account impersonation

When an authenticated principal, such as a user or another service account, authenticates as a service account to gain the service account's permissions, it's called _impersonating_ the service account. Impersonating a service account lets an authenticated principal access whatever the service account can access. Only authenticated principals with the appropriate permissions can impersonate service accounts. 

To set up a service account for temporary elevated access, [create the service account](https://docs.cloud.google.com/iam/docs/service-accounts-create), then grant it the roles that you want to temporarily give to a user. If you use [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview), also consider adding the service account [exempt from any relevant deny rules](https://docs.cloud.google.com/iam/docs/deny-overview#deny-rules) to avoid unexpected denials.

After you set up the service account, you can give users temporary elevated access by letting them [impersonate the service account](https://docs.cloud.google.com/iam/docs/service-account-impersonation). There are several ways you can let users impersonate service accounts:

  * Grant users a role that lets them create short-lived credentials for the service account. Users can then use the short-lived credentials to impersonate the service account.

    * Grant the [Service Account OpenID Connect Identity Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#id-token-creator-role) (`roles/iam.serviceAccountOpenIdTokenCreator`) to let the user create short-lived OpenID Connect (OIDC) ID tokens for the service account.

    * Grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`) to let the user create the following types of service account credentials:

      * OAuth 2.0 access tokens, which you can use to authenticate with Google APIs
      * OIDC ID tokens
      * Signed JSON Web Tokens (JWTs) and binary blobs

If you grant a user one of these roles, they can impersonate the service account _at any time_ to elevate their own access. However, they're less likely to access or modify sensitive resources unintentionally.

To learn how to impersonate service accounts, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

  * Create a token broker service that gives users [short-lived credentials](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials) for the service account after they authenticate and provide a justification. Users can then use the short-lived credentials to impersonate the service account.

With this method, you can decide when to let users impersonate the service account.

To learn how to generate short-lived credentials, see [Create short-lived credentials for a service account](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).




To learn more about service account impersonation, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

## What's next

  * Set up Privileged Access Manager for [temporary elevated access](https://docs.cloud.google.com/iam/docs/pam-overview).
  * Use IAM Conditions to [grant temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access) to a principal. 
  * Deploy the [Just-In-Time Access application](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project). 
  * [Manually create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) to impersonate a service account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
