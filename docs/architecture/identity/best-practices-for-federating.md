---
url: https://docs.cloud.google.com/architecture/identity/best-practices-for-federating/
title: Best practices for federating Google Cloud with an external identity provider \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:20.291356+00:00
---

# Best practices for federating Google Cloud with an external identity provider  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/best-practices-for-federating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for federating Google Cloud with an external identity provider Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document presents best practices and guidance that help you set up federation consistently and securely. The guidance builds on the [best practices for using Cloud Identity or Google Workspace with Google Cloud](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).

All Google services, including Google Cloud, Google Marketing Platform, and Google Ads, rely on [Google Sign-In](https://account.google.com/) to authenticate users. Instead of manually creating and maintaining [user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) in [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/) for each employee, you can [federate Cloud Identity or Google Workspace with your external identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp) such as Active Directory or Microsoft Entra ID (formerly Azure Active Directory). Setting up federation typically entails the following:

  * Automatically provisioning relevant user accounts from an [external authoritative source ](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_authoritative_source)to Cloud Identity or Google Workspace.
  * Enabling users to use an [external IdP](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_saml_identity_provider) to authenticate to Google services.

**Note:** A [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account) denotes a directory of users, not an individual user account. Individual user accounts are referred to as _users_ or _user accounts_.

## Map identities

The identity of a user account that's managed by Cloud Identity or Google Workspace [is defined by its primary email address](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account). The primary email address is listed as **Google Account email** on the [Google Account page](https://myaccount.google.com/email?utm_source=google-account&utm_medium=web). To be considered valid, the primary email address must use [one of the domains](https://support.google.com/a/answer/7502379) that you have added to your Cloud Identity or Google Workspace account.

The primary email address also serves these purposes:

  * The primary email address is the username that a user must provide when signing in. Although users can add [alternate email addresses or aliases](https://support.google.com/a/answer/33327) to their Google user account, these addresses are not considered identities and can't be used to sign in.
  * When an administrator needs to send out notifications to users (for example, to announce a potential security risk), those notifications are sent to the primary email address only.



To set up single sign-on and automatic user provisioning between Google and your external IdP, you must map identities in your external IdP to corresponding identities in Cloud Identity or Google Workspace. The following sections describe best practices for establishing this mapping.

### Use the same identity across all federated systems

All that's required to establish a mapping is to verify that the SAML assertion that the IdP supplies to Google contains a [`NameID` claim](https://support.google.com/a/answer/6330801) with a value that matches the primary email address of an existing Cloud Identity or Google Workspace user. The IdP is free to use whatever mapping or logic is applicable to derive a suitable `NameID` claim for its existing users.

Many IdPs rely on email addresses (or more generally, [RFC 822](https://tools.ietf.org/html/rfc822)–compliant names) to identify users. Examples include the following:

  * The `userPrincipalName` attribute in Active Directory is an RFC 822–compliant name that uniquely identifies a user and that can be used to sign in to Windows or Active Directory Federation Services (AD FS).
  * Entra ID uses the `UserPrincipalName` attribute [to identify users and let them sign in](https://docs.microsoft.com/azure/active-directory/hybrid/plan-connect-userprincipalname#what-is-userprincipalname).



If the users that your external IdP manages already rely on an email address as their identity, you can use the same identity as the primary email address in Cloud Identity or Google Workspace. Using the same user identity across federated systems has multiple advantages:

  * When users sign in to a Google tool such as the [Google Cloud console](https://console.cloud.google.com/), they are first prompted to provide the primary email address of their Cloud Identity or Google Workspace user before they are redirected to your external IdP. Depending on your IdP, the user might then be presented with another sign-on screen that prompts for their username and password.

If the email addresses differ for these steps, the sequence of sign-on screens can easily confuse end users. In contrast, if users can use a common identity across all steps, they aren't exposed to the technical differences between IdPs, which minimizes potential confusion.

  * If you don't have to map between user identities, it's easier for you to correlate audit logs from Google Cloud with logs from on-premises systems.

  * Similarly, if applications that are deployed on-premises and on Google Cloud need to exchange data containing user identities, you avoid the extra complexity of having to map user identifiers.




For more details on mapping Active Directory users or Entra ID users to Cloud Identity or Google Workspace, see the [Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_user_accounts) or [Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_user_accounts) guide.

### Ensure that identities use routable email addresses

Google Cloud uses the primary email address of a user to deliver notification emails. Examples of these notifications include the following:

  * Budget alerts: If you've configured a [budget alert](https://docs.cloud.google.com/billing/docs/how-to/budgets), Google Cloud sends a notification to Billing Admins and Billing Users when a budget threshold is crossed.

  * Payment notifications: Any payment-related notifications or alerts are sent to the email addresses of [payment users](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) that are configured for the affected billing account.

  * Project invitations: If you assign the Project Admin role to a user that is part of a different Cloud Identity or Google Workspace account than the one the project's organization is associated with, an invitation is sent to the user. Before the newly granted role can take effect, the user has to accept the invite by clicking a link in the email message.

  * Replies to support cases and other notifications from Support.




If you use Google Workspace and have properly configured the necessary DNS [MX records](https://support.google.com/a/answer/140034), all notification emails that are sent to the primary email address are delivered to the corresponding user's Gmail inbox.

For Cloud Identity users, Google Cloud also attempts to deliver notification emails, but the email must be handled by your existing email infrastructure. To make sure that your Cloud Identity users don't miss notifications, make sure that your existing email system accepts messages that are sent to the primary email addresses of Cloud Identity users, and that it routes this email to the correct mailboxes. Do the following:

  * Ensure that all domains [added to Cloud Identity](https://support.google.com/a/answer/7502379) have DNS MX records that point to your existing email system.

  * Ensure that the primary email address of a Cloud Identity user matches an existing mailbox in your email system. If there is a mismatch between the primary email address used by Cloud Identity and the user's email address, configure an alias in your existing email system so that email sent to each primary email address is routed to the right mailbox.




If these solutions aren't practical, consider [adding Google Workspace to your existing Cloud Identity account](https://admin.google.com/ac/billing/catalog) and assigning Google Workspace licenses to the key users that are in charge of billing or interacting with support, and who are therefore most likely to receive notifications.

### Assess migration options for existing consumer accounts

If your employees were using Google services such as [Google Ad Manager](https://admanager.google.com/home/), [Google AdSense](https://www.google.com/adsense/start/), or [Google Analytics](https://analytics.google.com/analytics/web/) before your organization signed up for Cloud Identity or Google Workspace, it's possible that your employees have been using consumer accounts to access these services.

Letting employees use consumer accounts for business purposes can be risky. For more details on what these risks are and how you can surface existing consumer accounts, see [Assessing your existing Google accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).

You can handle existing consumer accounts in the following ways:

  * Keep the consumer accounts as they are, accepting potential risks.
  * Migrate the accounts to Cloud Identity or Google Workspace by initiating a transfer.
  * Force the owners of the unmanaged user accounts to change their email address to use a different domain.



For more details on how to consolidate existing consumer accounts, see [Assessing identity consolidation options](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation).

How you decide to deal with consumer accounts influences [how and in what sequence](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite-best-practices-federation) you set up federation. Assess any existing consumer accounts that your users use before you begin creating user accounts or setting up single sign-on in Cloud Identity or Google Workspace.

## Map identity sets

When you've defined how individual identities are mapped between your external IdP and Cloud Identity or Google Workspace, you have to determine the _set of identities_ for which to enable access to Google services.

The effective set of identities that can authenticate to Google services is the intersection of two sets:

  1. External identities that map to an identity in Cloud Identity or Google Workspace.
  2. External identities that your external IdP allows for single sign-on to Cloud Identity or Google Workspace.

The process for controlling who is permitted to use single sign-on differs depending on which IdP you use. For example, Entra ID relies on [assignments](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/assign-user-or-group-access-portal), while AD FS uses [access control policies](https://docs.microsoft.com/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs).




### Limit the set of identities that can authenticate to Google services

Depending on how you plan to use Google Cloud, Google Workspace, and other Google tools, either all of your organization's employees or only a subset of them must be able to authenticate to Google services.

If you plan to grant only a subset of your organization's employees access to Google services, then it's best to restrict authentication to this set of users. By restricting the number of users that can authenticate, you establish an extra layer of defense that helps in case you accidentally configured any access control rule to be too lax.

You can limit the set of users that can authenticate to Google in the following ways:

  * Minimize the number of user accounts in Cloud Identity or Google Workspace. If there is no mapped user account, any attempt by a user to authenticate will fail, even if the IdP permits the user to sign in to Cloud Identity or Google Workspace by using single sign-on.
  * Configure single-sign on in your IdP to minimize the number of users that are allowed to sign in to Cloud Identity or Google Workspace.



The best approach for your situation depends on whether you have existing consumer accounts that you need to migrate.

### Limit the set of identities that you provision if you still need to migrate consumer accounts

You can migrate a consumer account to Cloud Identity or Google Workspace only if you haven't created a user account with the same identity in Cloud Identity or Google Workspace.

If you have existing consumer accounts that you still plan to migrate, you need to be careful not to [accidentally create conflicting user accounts](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite#avoiding_inadvertent_creation_of_conflicting_accounts). Follow these guidelines:

  * Limit authentication by creating new Cloud Identity or Google Workspace user accounts only for users that need them and are known to not have an existing consumer account.
  * Avoid inadvertently locking out migrated accounts by allowing single sign-on not only for the users for whom you create user accounts in Cloud Identity or Google Workspace, but also for all consumer accounts that are yet to be migrated.



The following diagram shows how different types of identities overlap and interrelate.

![How different types of identities overlap and interrelate.](https://docs.cloud.google.com/static/architecture/identity/images/overlapping-identities.svg)

In the diagram, identities with a user account in Cloud Identity or Google Workspace are in the smallest (yellow) ellipse. That ellipse is contained in the second (blue) ellipse, which contains identities that are able to authenticate. The third and largest ellipse (gray) contains the others and consists of the identities that have a user account in your IdP. For details on how to configure Active Directory, Entra ID, or Okta, see our [separate best practices guide](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite-best-practices-federation).

### Prevent new consumer account sign-ups

Adding a domain such as `example.com` to your Cloud Identity or Google Workspace account doesn't prevent employees from signing up for new consumer accounts using the same domain. These new consumer accounts are surfaced as unmanaged users in your Cloud Identity or Google Workspace account, but they aren't allowed to use single sign-on or any other configuration you applied in your Cloud Identity or Google Workspace account.

One way to block the creation of a new consumer account is to create a user account in Cloud Identity or Google Workspace with the same email address. For example, if you created a user `alice@example.com` in your Cloud Identity or Google Workspace account, then any attempts by an employee to sign up for a new consumer account with the same identity will fail. However, if no corresponding user exists in Cloud Identity or Google Workspace yet, then signing up for a new consumer account will succeed.

When there are no more consumer accounts to migrate to Cloud Identity, prevent new consumer account sign-ups by applying the following configuration:

  * Limit authentication by permitting only relevant users to use single sign-on to Cloud Identity or Google Workspace.

  * Provision Cloud Identity or Google Workspace users for all employees. Ensure that the user accounts use the employee's corporate email address as the primary email address or alias so that no new consumer accounts can be created using the same email address. If possible, keep user accounts that are not enabled for single sign-on in a suspended state.




The following diagram shows this configuration.

![Preventing new consumer account sign-ups.](https://docs.cloud.google.com/static/architecture/identity/images/limiting-access-by-sso.svg)

If you are still in the process of migrating consumer accounts, you can temporarily monitor new consumer account sign-ups by capturing the verification emails sent during the sign-up process. Verification emails use an envelope sender address that matches `*@idverification.bounces.google.com`. Set up a filter in your email system that identifies emails with this envelope sender address and holds them for internal review.

**Note:** The sender address used by verification emails might change in the future.

### Make Cloud Identity or Google Workspace identities a subset of the identities in your external IdP

Your Cloud Identity or Google Workspace account might contain user accounts with identities that don't map to any users in your external IdP. There are two typical scenarios that can result in these user accounts:

  * You create a new user account in Cloud Identity or Google Workspace and use a primary email address that doesn't map to any user in your external IdP.
  * You have a user account in Cloud Identity or Google Workspace that maps to an identity in your external IdP, but then you delete the identity in the external IdP. For example, you might delete the identity if the employee leaves the company.



When you enable single sign-on in Cloud Identity or Google Workspace, all users (with the exception of super admins) are forced to use single sign-on. For a Cloud Identity or Google Workspace user account that doesn't map to an identity in your external IdP, any attempt to use single sign-on will fail. A user account without such a counterpart is effectively defunct, but might still pose a risk, as in the following situations:

  * If at some point single sign-on is temporarily or permanently disabled, the user account can be used again. This might enable a former employee to sign in and access corporate resources.

  * The name of the deleted user account might be reused. For example, an employee joining the company might share the same name with a different employee who left the company months or years earlier. If the previous employee's user account has meanwhile been deleted, it's possible that you might assign the new employee the username that the former employee used to use.

The new employee's user account might have an internal ID that's different from that of the former employee. However, from a federation perspective, the two user accounts are considered the same if they both map to the same primary email address in Cloud Identity or Google Workspace. As a result, when the new employee signs in to Google, they might "inherit" existing data, settings, and permissions from the former employee.




Cloud Identity and Google Workspace super-admin users are exempt from the requirement to use single sign-on, but they are still allowed to use single sign-on when sign-on is initiated by the IdP. The ability to use IdP-initiated single sign-on makes super-admin users sensitive to name squatting if they lack a counterpart in your external IdP.

Consider the following example: Alice has a super-admin user `alice-admin@example.com` in Cloud Identity or Google Workspace and does not use two-step verification. Mallory, who does not know Alice's password, finds a way to create a new user in the external IdP that maps to `alice-admin@example.com`. Although this newly created user account might not have any special privileges and has no relation to Alice's user account, the fact that it shares a common identity with Alice's super-admin account now enables Mallory to use IdP-initiated single sign-on and authenticate as `alice-admin@example.com`.

To mitigate this name-squatting risk, make sure that your Cloud Identity or Google Workspace identities are a subset of the identities in your external IdP. The best way to accomplish this is to map the entire user account lifecycle as implemented by your external IdP to the user account lifecycle in Cloud Identity or Google Workspace.

### Use dedicated super-admin users

Google Workspace and Cloud Identity super-admin accounts have a powerful set of permissions that apply not only to the Cloud Identity or Google Workspace account, [but also to an associated Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up). Because only a small number of activities require super-admin privileges, whenever possible it's best to limit the number of administrators with super-admin access and to use less-privileged user accounts for the [daily administration of your account or Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices#discourage_super_admin_account_usage).

When you've identified the administrators who require super-admin access, create dedicated super-admin user accounts—for example:

  * Create a user account with the identity `alice@example.com` and assign regular permissions. This account should be used on an everyday basis for routine activities.
  * Create a second user account with identity `alice-admin@example.com` and assign it super-user privileges. It's a best practice for Alice to use this account only for occasions where super-admin privileges are required.

To ensure that notification emails sent to this email address are received in the user's mailbox, configure Google Workspace or your existing email system so that the email address `alice-admin@example.com` is an alias or is forwarded to `alice@example.com`.




Ensure that both identities are recognized by your external IdP so that the set of identities in Cloud Identity or Google Workspace continues to be a subset of the identities in your external IdP.

We recommend following a naming scheme for these dedicated super-admin accounts so that in audit logs you can track where and how they're being used. For example, add `-admin` to the username, as in the previous example.

### Limit the number of service users in Google Workspace and Cloud Identity

Your external IdP might contain not only user accounts for employees, but also user accounts intended for machine users such as applications, tools, or background jobs.

In contrast, the preferred way on Google Cloud to enable an application to authenticate and access Google APIs is to implement one of the following approaches:

  * A web application or tool that needs to access Google APIs or services on an end user's behalf should use either [OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2) or [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect). By using one of these protocols, the application first solicits the end user's consent to access the user's data and, on receiving consent, is then able to perform the access on behalf of the end user.

  * If access to APIs or services should not be on behalf of an end user but rather on behalf of the application itself, it's best to use [Google Cloud service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) for authentication and then [grant the service account access](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts) to the resources by using [IAM](https://docs.cloud.google.com/iam).




If Google Cloud service accounts are granted the appropriate roles in IAM, they can be used to authenticate and use any Cloud API. If you need to grant a service account access to APIs that are outside Google Cloud, for example, to the [Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/) or [Drive API](https://developers.google.com/drive/api/v3/reference/), you can use [Google Workspace domain-wide delegation](https://developers.google.com/admin-sdk/reports/v1/guides/delegation).

With Google Workspace domain-wide delegation, you enable a service account to act on behalf of a Cloud Identity or Google Workspace user. Because delegation is a powerful privilege, we recommend that you use Google Workspace domain-wide delegation only in cases where the OAuth approach is not practical.

Use a dedicated Cloud Identity or Google Workspace user for every Google Cloud service account that is enabled for Google Workspace domain-wide delegation. Create this user in your external IdP and then provision it to Cloud Identity or Google Workspace so that the set of users in Cloud Identity or Google Workspace continues to be a subset of the users in your external IdP.

Avoid creating service users in Cloud Identity and Google Workspace that you don't intend to use for Google Workspace domain-wide delegation.

## Map user account lifecycles

The user accounts in your external IdP follow a certain lifecycle. Typically, this lifecycle reflects the employment relationship between the employee and the company:

  1. A new user account is created for an employee joining the organization.
  2. The user account might temporarily be suspended and later reactivated—for example, when the employee goes on leave.
  3. When the user leaves the company, the user account is either deleted or kept in a suspended state for a certain retention period before ultimately being deleted.



The following diagram illustrates this lifecycle.

![Mapping user account lifecycles.](https://docs.cloud.google.com/static/architecture/identity/images/mapping-user-account-lifecycles.svg)

This section lists best practices for ensuring that the lifecycle of user accounts in Cloud Identity or Google Workspace follows the lifecycle of corresponding user accounts in your external IdP.

### Designate your external IdP as the source of truth

Many HR information systems (HRIS), IdPs, and adapters only support one-way user provisioning. This means that changes performed in the HRIS or IdP are propagated to Cloud Identity or Google Workspace, but changes performed in Cloud Identity or Google Workspace are not propagated back.

To prevent inconsistencies caused by one-way provisioning, designate your external IdP as the source of truth. Exclusively use your external IdP (or HRIS) to create, modify, or delete users, and rely on automated provisioning to have changes be propagated to Google Workspace and Cloud Identity. By designating your external IdP as the source of truth, you limit the risk of inconsistencies and of having manual modifications overridden by the IdP.

### Automate user provisioning to Cloud Identity or Google Workspace

To enable an employee to authenticate to Google by using single sign-on, you first have to create a user account for the employee in Cloud Identity or Google Workspace. To ensure consistency with your external IdP, it's best to automate the process of provisioning these user accounts in Cloud Identity or Google Workspace:

  * By automating provisioning, you can ensure that Cloud Identity or Google Workspace identities are always a subset of the identities in your external IdP.
  * You minimize the risk of inadvertently introducing a mismatch between an identity in Cloud Identity or Google Workspace and the corresponding identity in your external IdP. Mismatches such as an accidental misspelling of the email address can otherwise lead to employees experiencing problems signing in.
  * You minimize manual administration effort.



If you use an HRIS to manage the onboarding process, then one way to automate user provisioning is to configure the HRIS to provision user accounts to both your external IdP and to Cloud Identity or Google Workspace, as in the following diagram.

![Provision user accounts to both your external IdP and to Cloud Identity or Google Workspace.](https://docs.cloud.google.com/static/architecture/identity/images/provisioning-user-accounts.svg)

For this setup to work well, you have to ensure that your HRIS provisions user accounts so that they properly map to each other. Also, the HRIS must handle the decision of which user accounts to provision to Cloud Identity or Google Workspace.

Another way to automate user provisioning that works independently of an HRIS is to use your external IdP as the authoritative source for provisioning users in Cloud Identity or Google Workspace. In this setup, the configuration for mapping user accounts and user account sets is managed in the IdP or by the adapter, as the following diagram shows.

![Using your external IdP as the authoritative source for provisioning users in Cloud Identity or Google Workspace.](https://docs.cloud.google.com/static/architecture/identity/images/provisioning-user-accounts-with-external-idp.svg)

If you use Active Directory as your IdP, you can duplicate this setup [by using Google Cloud Directory Sync](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction). Other IdPs such as [Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) or Okta have built-in adapters for provisioning users to Google Workspace. Because Google Workspace and Cloud Identity [are based on the same platform and use the same APIs](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning#cloud_identity_and_g_suite_accounts), these adapters can also be used for Cloud Identity.

### Propagate suspension events to Cloud Identity or Google Workspace

When an employee leaves the organization, whether temporarily or permanently, we recommend that you revoke the employee's access to Google services. By suspending the employee's user account in your external IdP, you revoke their ability to use single sign-on to authenticate to Google, but that might not fully revoke access to all Google services. The following can still occur:

  * If the Cloud Identity or Google Workspace user has an active browser session, the session will continue to work. Any OAuth tokens that have already been obtained also continue to be valid.
  * If the user has super-admin privileges or if you have configured network masks, the employee might still be able to sign on using a password.
  * The user account might still receive notifications from Google Cloud, including [budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).
  * If the user has a Google Workspace license assigned, emails will continue to be delivered to the user's mailbox, the user still shows up in the address book, and the user might still be listed as available in Google Google Calendar.
  * If you [allow users to use less secure apps](https://support.google.com/a/answer/6260879), the user might still be able to access Gmail, Google Calendar, and other data by using [app passwords](https://support.google.com/accounts/answer/6010255).



To fully revoke access to Google services, propagate suspension events to Cloud Identity or Google Workspace in the following ways:

  * Ensure that whenever a user account is suspended in your external IdP, the corresponding user account in Cloud Identity or Google Workspace is suspended as well. Suspending a user in Cloud Identity or Google Workspace terminates active browser sessions, invalidates tokens, and revokes all other access.

  * Similarly, when you reactivate a user account in your external IdP, make sure that you also reactivate the corresponding user account in Cloud Identity or Google Workspace.




Suspending a user account in Cloud Identity or Google Workspace is a non-destructive operation. While the user account is suspended, the user's data is retained, Google Workspace licenses stay attached, and assigned roles in Google Cloud remain unchanged.

### Propagate deletion events to Cloud Identity or Google Workspace

When an employee permanently leaves the organization, you might decide to not only suspend the employee's user account in your external IdP, but also delete it.

If you delete a user account in your external IdP, but you don't delete the corresponding Cloud Identity or Google Workspace user, then the set of users in Cloud Identity and Google Workspace is not a subset of the users in your external IdP anymore. This can turn into a problem in the future if a new employee joins your organization who happens to have the same name as the employee who left the company. If you create a user account in your IdP for the new employee, you might reuse the old employee's username, causing the new user account to map to the old user account in Cloud Identity or Google Workspace. As a result, the new employee might gain access to the old employee's data and settings.

You can avoid the risks associated with orphaned Cloud Identity or Google Workspace user accounts by deleting a Cloud Identity or Google Workspace user as soon as the corresponding user account in your IdP is deleted.

Deleting a Cloud Identity or Google Workspace user is a destructive operation that can only be undone within a [certain time period](https://support.google.com/a/answer/1397578). Depending on the Google services consumed by the user, deleting the user might cause associated data to be permanently deleted and might therefore not meet your compliance requirements.

To preserve the user's settings and data for a certain retention period before permanently deleting them, implement one of the following approaches:

  * Delay the user account deletion in your external IdP by keeping the user in a suspended state for a certain retention period. Delete the user in both your IdP and Cloud Identity or Google Workspace after the retention period has elapsed.

  * When you delete a user account in your external IdP, suspend the corresponding Cloud Identity or Google Workspace user and change its primary email address to a name that is unlikely to ever cause a conflict. For example, rename `alice@example.com` to `obsolete-yyyymmdd-alice@example.com` where `yyyymmdd` reflects the date of the deletion in your external IdP. Keep the renamed user account in a suspended state for a retention period, and delete it after the retention period has elapsed.




To preserve Google Workspace data for suspended users, either keep the Google Workspace license assigned to the user or [switch it to an Archived User license](https://support.google.com/a/answer/9048836) to ensure that [Google Workspace Vault retention rules](https://support.google.com/vault/answer/2990828) continue to apply and that [the user's data is preserved](https://support.google.com/vault/answer/2736622).

## Single sign-on

All Google products, including services such as Google Cloud, Google Ads, and YouTube, use [Google Sign-In](https://developers.google.com/identity/) to authenticate users. A service initiates the authentication process by redirecting a user to `accounts.google.com` where the user sees the Google sign-in screen and is prompted for their email address. Depending on the domain of the provided email address, the user account is then looked up in Gmail, the consumer account directory, or if the domain matches its [primary, secondary, or alias domain](https://support.google.com/a/answer/7502379), in a Cloud Identity or Google Workspace account.

The following diagram illustrates this authentication process.

![Google authentication process.](https://docs.cloud.google.com/static/architecture/identity/images/google-authentication-process.svg)

If you [configure a Cloud Identity or Google Workspace account to use single sign-on](https://support.google.com/a/answer/60224), then users are redirected to an external IdP to authenticate. When the external IdP has completed the authentication, the result is relayed back to Google Sign-In by means of a SAML assertion. This SAML assertion serves as proof of a successful authentication. The assertion contains the email address of the user, and is signed by the external IdP's certificate so that Google Sign-In can verify its authenticity.

This process is referred to as _service provider–initiated single sign-on_ , and it applies to all users except for super admins. Super admins are never redirected to an external IdP and are prompted for a password instead.

Some IdPs also support _IdP-initiated single sign-on_. In this model, the user authenticates at the external IdP and then follows a link pointing to a Google service such as Google Cloud or Google Ads. If single sign-on has been enabled for a Cloud Identity or Google Workspace account, all users of that account are allowed to use IdP-initiated single sign-on, including super admins.

### Minimize the set of attributes passed in SAML assertions

After a user has authenticated at the external IdP, Cloud Identity or Google Workspace use the SAML assertion that is passed by the external IdP to establish a session. In addition to validating its authenticity, this process includes identifying the Cloud Identity or Google Workspace user account that corresponds to the `NameID` value in the SAML assertion.

The `NameID` value is expected to contain the primary email address of the user account to be authenticated. The email address is case sensitive. Aliases and alternate email addresses are not considered.

To avoid accidental spelling or casing mismatches, it's best to automatically provision user accounts.

SAML assertions are allowed to contain additional attributes, but they are not considered during authentication. Attributes containing information such as a user's forename, surname, or group memberships are ignored because the user's account in Cloud Identity or Google Workspace is considered the only source for this user information.

To minimize the size of SAML assertions, configure your IdP to not include any attributes that aren't [required by Google Sign-In](https://support.google.com/a/answer/6330801).

### Use google.com as the issuer

Google Sign-In sessions are not restricted to a single tool or domain. Instead, once a session has been established, the session is valid across all Google services that the user [has been granted access to](https://support.google.com/a/answer/182426). This list of services might include services like Google Cloud and Google Ads as well as services such as Google Search and YouTube.

The global nature of a session is reflected in the SAML protocol exchange: by default, Google uses `google.com` as the issuer (the `Issuer` element in the SAML request) in SAML requests, and it expects SAML assertions to specify `google.com` as the audience (the `Audience` element in the SAML response).

You can change this default by enabling the **Use a domain-specific issuer** option when you configure single sign-on in Cloud Identity or Google Workspace. Enable the domain-specific issuer option only if you have more than one Cloud Identity or Google Workspace account (and therefore multiple domains) and your IdP needs to be able to distinguish between sign-ons initiated by one Cloud Identity or Google Workspace account versus another account. When you enable the option, SAML requests use `google.com/a/DOMAIN` as the issuer and expect `google.com/a/DOMAIN` as the audience, where `DOMAIN` is the primary domain of the Cloud Identity or Google Workspace account.

In all other cases, keep the default setting to use `google.com` as the issuer and configure your external IdP to specify `google.com` as the audience in SAML assertions. Depending on your IdP, this setting might also be referred to as _issuer_ , _relying party trust identifier_ , or _entity ID_.

### Align the length of Google sessions and IdP sessions

When a user has completed the single sign-on process and a session has been established, the Google Sign-In session remains active for a certain period of time. When this time period elapses or if the user signs out, the user is requested to re-authenticate by repeating the single sign-on process.

By default, the session length for Google services is 14 days. For users with a Cloud Identity Premium or Google Workspace Business license, you can [change the default session length](https://support.google.com/a/answer/7576830) to a different period such as 8 hours.

You can [control the session length used by Google Cloud](https://support.google.com/a/answer/9368756). The Google Cloud session applies to the Google Cloud console as well as to the Google Cloud CLI and other API clients. You can set the Google Cloud session length in all Cloud Identity and Google Workspace account types.

Most external IdPs also maintain a session for authenticated users. If the length of the IdP session is longer than the Google session length, then re-authentication might occur silently. That is, the user is redirected to the IdP but might not have to enter credentials again. Silent re-authentication might undermine the intent of shortening the length of Google sessions.

To ensure that users have to enter their credentials again after a Google session has expired, configure the Google session length and the IdP session length so that the IdP session length is shorter than the Google session length.

**Note:** Google Admin console sessions have a fixed session length of 1 hour. This cannot be customized.

### Disable single sign-on for super-admin users

For super-admin users, SSO is optional: They can use SSO when the sign-on is initiated by the IdP, but they can also sign in by using username and password.

If you're not planning to use IdP-initiated single sign-on for super-admin users, you can decrease risk by using the following procedure:

  1. [Add a dedicated organizational unit](https://support.google.com/a/answer/182537) for super-admins.
  2. [Assign an SSO profile](https://support.google.com/a/answer/10723804) to the organizational unit that disables single sign-on.



Otherwise, if you're planning to use IdP-initiated single sign-on, make sure that you enforce post-SSO verification for super-admin users.

## Multi-factor authentication

Enabling single sign-on between Cloud Identity or Google Workspace and your external IdP improves the user experience for employees. Users have to authenticate less frequently and don't need to memorize separate credentials to access Google services.

But enabling users to seamlessly authenticate across services and environments also means that the potential impact of compromised user credentials increases. If a user's username and password are lost or stolen, an attacker might use these credentials to access resources not only in your existing environment, but also across one or more Google services.

To mitigate the risk of credential theft, it's best to use multi-factor authentication for all user accounts.

### Enforce multi-factor authentication for users

When you have configured single sign-on for your Cloud Identity or Google Workspace account, users without super-admin privilege have to use your external IdP to authenticate.

Configure your IdP to require the use of a second factor (such as a one-time code or a USB key) to enforce that multi-factor authentication is applied whenever single sign-on to Google is used.

If your external IdP doesn't support multi-factor authentication, consider [enabling post-SSO verification](https://support.google.com/a/answer/6002699) to have Google perform additional verification after the user returns from authenticating with your external IdP.

Avoid using network masks, because they could be abused as a way to sidestep multi-factor authentication for users.

### Enforce Google 2-step authentication for super-admin users

Super-admin users are not redirected to your external IdP when they try to sign in to the Google Cloud console or other Google sites. Instead, super-admin users are prompted to authenticate by username and password.

Because super-admin users can authenticate by username and password, they are not subject to any multi-factor authentication policies that your IdP might enforce. To protect super-admin users, [enforce Google 2-step authentication](https://support.google.com/a/answer/9176657) for all super-admin users.

Super-admin users typically fall into one of two categories:

  * **Personalized super-admin users:** These users are personalized and intended to be used by a single administrator. We recommend that you enforce 2-step verification for all personalized super-admin users.

  * **Machine super-admin users:** Although it's best to avoid these user accounts, they are sometimes necessary to enable tools such as Cloud Directory Sync or the Entra ID gallery app to manage users and groups in Cloud Identity or Google Workspace.

Limit the number of machine super-admin users and try to enable 2-step verification whenever possible.




For users that don't use single sign-on, you can enforce 2-step authentication on either account globally, by organizational unit, or by group:

  * If you don't have any machine super-admin users who cannot use 2-step verification, it's best to [turn on enforcement for all users](https://support.google.com/a/answer/9176657). By enforcing 2-step verification for all users, you avoid the risk of accidentally missing users.

  * If you have some machine super-admin users who cannot use 2-step verification, use a dedicated group to control 2-step verification. Create a new group, [turn on enforcement](https://support.google.com/a/answer/9176657) for the group, and add all relevant super-users to it.




For more details on using 2-step authentication to secure super-admin users, see our [security best practices for administrator accounts](https://support.google.com/a/answer/9011373).

### Enforce post-SSO verification for super-admin users

Although super-admin users are not required to use single sign-on, they are still allowed to use single sign-on when initiated by the IdP. To ensure that super-admin users are always subject to 2-step verification, even if they authenticate by IdP-initiated sign-in, turn on [additional SSO verifications and 2-Step verification](https://support.google.com/a/answer/6002699#ssochallenges&zippy=%2Cset-up-post-sso-verification) for all super-admin users.

The additional SSO verifications might seem redundant in cases where your IdP already enforce multi-factor authentication, but the setting can help protect super-admin users if your IdP becomes compromised.

### Don't restrict single sign-on by network mask

When you configure single sign-on in Cloud Identity or Google Workspace, you can optionally specify a [network mask](https://support.google.com/a/answer/6369487). If you specify a mask, only users that have IP addresses matching the mask are subject to single sign-on; other users are prompted for a password when they sign in.

If you use network masks, you might be undermining the multi-factor authentication that's enforced by your external IdP. For example, by changing locations or using a VPN, a user might be able to control whether the network mask applies or not. If you enforce multi-factor authentication at the external IdP, then this tactic might allow a user or attacker to circumvent the multi-factor authentication policies configured at your external IdP.

To ensure that multi-factor authentication applies consistently regardless of a user's location or IP address, avoid restricting single sign-on by network mask.

To restrict access to resources by IP address, either configure an appropriate IP allow list at your external IdP or use [context-aware access for Google Cloud](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) and [Google Workspace](https://support.google.com/a/answer/9261439).

## What's next

  * Learn about additional best practices: 
    * [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning)
    * [Best practices for securing super-admin accounts](https://support.google.com/a/answer/7587183)
    * [Security checklist for medium and large businesses](https://support.google.com/a/answer/9011373)
  * Compare [patterns for federating an external IdP with Google Cloud](https://docs.cloud.google.com/solutions/patterns-for-authenticating-corporate-users-in-a-hybrid-environment#patterns_for_federating_an_external_idp_with_gcp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
