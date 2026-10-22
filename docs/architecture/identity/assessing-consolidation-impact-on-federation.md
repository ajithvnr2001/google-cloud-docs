---
url: https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation/
title: Assess the impact of user account consolidation on federation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:23.888187+00:00
---

# Assess the impact of user account consolidation on federation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Assess the impact of user account consolidation on federation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

If you plan to federate [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/) with an external identity provider (IdP) but still need to consolidate existing consumer accounts, this document helps you understand and assess the interplay between federation and consolidation. This document also shows you how to configure federation in a way that doesn't interfere with your ability to consolidate existing consumer accounts.

**Note:** This document applies only if you decided to follow [Plan 3: Federation with user account consolidation](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans#plan_3_federation_with_user_account_consolidation) (or a variation thereof).

## Interplay between federation and user account consolidation

In a federated setup, you connect Cloud Identity or Google Workspace to an external [authoritative source](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_authoritative_source) so that the authoritative source can automatically provision user accounts in Cloud Identity or Google Workspace.

These invariants typically hold for a federated setup:

  1. The authoritative source is the only source for identities.
  2. There are no user accounts in Cloud Identity or Google Workspace other than the ones provisioned by the authoritative source.
  3. The SAML identity provider does not allow Google single sign-on for any identities other than the ones for which the authoritative source has provisioned user accounts.



Although these invariants reflect the [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating), they cause problems when you want to migrate existing consumer accounts:

  1. Existing consumer accounts don't originate from the authoritative source. These accounts already exist, and they now need to be linked to an identity known by the authoritative source.
  2. Existing consumer accounts, once they are migrated to Cloud Identity or Google Workspace, are user accounts that have not been provisioned by the authoritative source. The authoritative source must recognize and "adopt" these migrated accounts.
  3. The identities of existing consumer accounts might be unknown to the SAML identity provider, yet they still need to be allowed to use single sign-on.



To allow existing consumer accounts to be consolidated, you have to temporarily set up federation in a way that is _safe for account consolidation_.

## Make federation safe for account consolidation

The following table lists the requirements to consider in order to make federation safe for account consolidation. If you plan to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp) but still need to consolidate existing consumer accounts, then you have to make sure that your setup initially meets these requirements. After you have completed the migration of existing consumer accounts, you are free to change the configuration because the requirements then no longer hold.

Requirement | Justification  
---|---  
Allow single sign-on for identities with consumer accounts | Migrating a consumer account requires an account transfer. A Cloud Identity or Google Workspace administrator initiates the account transfer, but in order to complete the transfer, the owner of the consumer account must consent to the transfer. As an administrator, you have limited control over when the consent will be expressed and thus, when the transfer is conducted. Once the owner expresses consent and the transfer is complete, all subsequent sign-ons are subject to single sign-on using your external IdP. For single sign-on to succeed, regardless of when the transfer is complete, ensure that your external IdP [allows single sign-ons for the identities of all consumer accounts](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#limit_the_set_of_identities_that_you_provision_if_you_still_need_to_migrate_consumer_accounts) that you plan to migrate.  
Prevent automatic user provisioning for identities with consumer accounts | If you provision a user account for an identity that already has a consumer account, you [create a conflicting account](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite#migration_process_overview). A conflicting account blocks you from transferring ownership of the consumer account, its configuration, and any associated data to Cloud Identity or Google Workspace. The default behavior of many external IdPs is to proactively create user accounts in Cloud Identity or Google Workspace. This behavior can inadvertently cause conflicting accounts to be created. By preventing automatic user provisioning for identities with existing consumer accounts, you avoid inadvertently creating conflicting accounts and ensure that consumer accounts can be transferred correctly.  
  
If you have identified [consumer accounts without a matching identity in the external IdP](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts#consumer_accounts_without_a_matching_identity_in_the_external_idp) that you consider legitimate and that you want to migrate to Cloud Identity or Google Workspace, then you have to make sure that your federation configuration does not interfere with your ability to migrate these consumer accounts.

Requirement | Justification  
---|---  
Prevent deletion of migrated accounts without a matching identity in the external IdP | If you have a user account in Cloud Identity or Google Workspace that does not have a matching identity in your external IdP, then your IdP might consider this user account orphaned and might suspend or delete it. By preventing your external IdP from suspending or deleting migrated accounts without matching the identity in the external IdP, you avoid losing the configuration and data associated with affected accounts and ensure that you can manually [reconcile the accounts](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts) them.  
  
## Make Microsoft Entra ID (formerly Azure AD) federation safe for account consolidation

If you plan to [federate Cloud Identity or Google Workspace with Microsoft Entra ID (formerly Azure AD)](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory), you can use the [Google Workspace gallery app](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/aad.googleapps).

**Note:** The [Google Workspace gallery app from the Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/aad.googleapps) is a Microsoft product and is neither maintained nor supported by Google.

When you enable provisioning, Microsoft Entra ID ignores existing accounts in Cloud Identity or Google Workspace that don't have a counterpart in Microsoft Entra ID, so the requirement to prevent deletion of migrated accounts without a matching identity in the external IdP is always met.

Depending on how you configure the gallery app, you must still ensure that you do the following:

  * Allow single sign-on for identities with consumer accounts.
  * Prevent automatic user provisioning for identities with consumer accounts.



There are multiple ways to meet these requirements. Each approach has advantages and disadvantages.

### Approach 1: Don't configure provisioning

In this approach, you configure the gallery app to handle single sign-on, but you don't configure automatic user provisioning. By not configuring user provisioning, you prevent automatic user provisioning for identities with consumer accounts.

To allow single sign-on for identities with consumer accounts, assign the app to all identities that might eventually need access to Google services, even if their existing consumer accounts are still subject to being migrated.

For a user who has an existing consumer account, the corresponding Cloud Identity or Google Workspace user account is created automatically when the transfer request is accepted. That user can then immediately use single sign-on.

For users who don't have a user account in Cloud Identity or Google Workspace, you have to create one manually.

Although this approach meets the requirements and is the least complex to set up, it comes with the limitation that any attribute changes or user suspensions performed in Microsoft Entra ID won't be propagated to Cloud Identity or Google Workspace.

### Approach 2: Two apps with manual assignment

In this approach, you overcome the limitation of having to manually create user accounts in Google Workspace or Cloud Identity for users that don't have an existing account. The idea is to use two gallery apps, one for provisioning and one for single sign-on:

  * The first app is used exclusively for provisioning users and groups and has single sign-on disabled. By assigning users to this app, you control which accounts are being provisioned to Cloud Identity or Google Workspace.
  * The second app is used exclusively for single sign-on and is not authorized to provision users. By assigning users to this app, you control which users are allowed to sign on.



Using these two apps, assign users as follows:

  * Assign all identities that eventually need access to Google services to the single sign-on app. Include identities with existing consumer accounts so that you allow single sign-on for identities with consumer accounts.
  * When assigning identities to the provisioning app, include the identities that eventually need access to Google services, but exclude all identities that are known to have an existing consumer account. This way, you prevent automatic user provisioning for identities with consumer accounts.

**Important:** However, any mistake in assignment can lead immediately to a conflicting account being created, making this approach more risky than other approaches.

### Approach 3: Two apps with user creation disabled

When configuring provisioning, you need to authorize Microsoft Entra ID to access Cloud Identity or Google Workspace by using a Cloud Identity or Google Workspace account. Normally, it's best to use a dedicated super-admin account for this purpose, because super-admin accounts are exempted from single sign-on (that is, any SSO configuration doesn't apply to them; they will continue to use passwords for login).

However, for this scenario, you can have Microsoft Entra ID use a more restricted account for migration, one that doesn't allow Microsoft Entra ID to create users. That way, you effectively prevent Azure from automatically provisioning user accounts for identities with consumer accounts, regardless of which users are assigned to the provisioning app.

A restricted administrator user account in Cloud Identity or Google Workspace should have only the following privileges:

  * Organization Units > Read
  * Users > Read
  * Users > Update
  * Groups

**Note:** Disallowing Microsoft Entra ID from creating user accounts won't stop it from attempting to create them. Therefore, you're likely to find errors in the Microsoft Entra ID audit logs indicating that it failed to create user accounts in Cloud Identity or Google Workspace.

A downside of this approach is that for users without unmanaged accounts, you must manually create accounts in Cloud Identity or Google Workspace.

### Federate with Microsoft Entra ID: Comparison

The following table summarizes the approaches.

| Allow single sign-on for identities with consumer accounts | Prevent automatic user provisioning for identities with consumer accounts | Prevent deletion of migrated accounts without a matching identity in the external IdP | Auto-provision new accounts | Auto-update migrated accounts  
---|---|---|---|---|---  
Approach 1: No provisioning | ✅ | ✅ | ✅ | X | X  
Approach 2: Two apps with manual assignment | ✅ | Prone to manual error | ✅ | ✅ | ✅  
Approach 3: Two apps with user creation disabled | ✅ | ✅ | ✅ | X | ✅  
  
## Make Active Directory federation safe for account

If you plan to [federate Cloud Identity or Google Workspace with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction), you can use [Google Cloud Directory Sync (GCDS)](https://support.google.com/a/answer/106368) and Active Directory Federation Services (AD FS). When you configure GCDS and AD FS, you have to make sure to do the following:

  * Allow single sign-on for identities with consumer accounts.
  * Prevent automatic user provisioning for identities with consumer accounts.
  * Prevent the deletion of migrated accounts without a matching identity in the external IdP.



There are multiple ways to meet these requirements. Each approach has advantages and disadvantages.

### Approach 1: Disable GCDS

In this approach, you set up single sign-on with AD FS, but you don't enable GCDS until you've finished migrating unmanaged user accounts. By disabling GCDS, you prevent automatic user provisioning for identities with consumer accounts.

To allow single sign-on for identities with consumer accounts, create a custom [access control policy](https://docs.microsoft.com/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs) in AD FS and assign all identities that might eventually need access to Google services, even if their existing consumer accounts are still subject to being migrated.

For a user who has an existing consumer account, the corresponding Cloud Identity or Google Workspace user account is created automatically when the transfer request is accepted. By using the custom access control policy, you ensure that the user can immediately use single sign-on.

For users who don't have a user account in Cloud Identity or Google Workspace, you have to create one manually.

Although this approach meets the requirements and is the least complex to set up, it comes with the limitation that any attribute changes or user suspensions performed in Active Directory won't be propagated to Cloud Identity or Google Workspace.

### Approach 2: GCDS with manual assignment

In this approach, you overcome the limitation of having to manually create user accounts in Cloud Identity or Google Workspace for users that don't have an existing account:

  * Equivalent to Approach 1, you allow single sign-on for identities with consumer accounts by creating a custom [access control policy](https://docs.microsoft.com/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs) in AD FS and assigning all identities that might eventually need access to Google services, even if their existing consumer accounts are still subject to being migrated.

  * Create a group in Active Directory that reflects the user accounts that you want to automatically provision to GCDS. In the list of members, include the identities that eventually need access to Google services, but exclude all identities that are known to have an existing consumer account.

  * Configure GCDS to provision user accounts only for identities that are members of this group. This way, you prevent automatic user provisioning for identities with consumer accounts.




A key limitation of this approach is that you cannot prevent the deletion of migrated accounts without a matching identity in the external IdP. The approach is therefore applicable only if you don't have any [consumer accounts without a matching identity in the external IdP](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts#consumer_accounts_without_a_matching_identity_in_the_external_idp).

**Important:** Any mistake in assignment can lead to a conflicting account being created, making this approach more risky than other approaches.

### Approach 3: Disallow GCDS to create users

When configuring provisioning, you must authorize GCDS to access Cloud Identity or Google Workspace. Normally, it's best to use a dedicated super-admin account for this purpose, because such accounts are exempted from single sign-on (that is, any SSO configuration doesn't apply to them; they will continue to use passwords for login).

However, for this scenario, you can have GCDS use a more restricted account for migration, one that doesn't allow it to create users. That way, you effectively prevent GCDS from automatically provisioning user accounts for identities with consumer accounts and from deleting migrated accounts without a matching identity in the external IdP.

A restricted administrator user account in Cloud Identity or Google Workspace should only have the following privileges:

  * Organizational Units
  * Users > Read
  * Users > Update
  * Groups
  * Schema Management
  * Domain Management

**Note:** Disallowing GCDS from creating user accounts won't stop it from attempting to create them. Therefore, you're likely to find errors in the GCDS log indicating that it failed to create user accounts in Cloud Identity or Google Workspace.

A downside of this approach is that for users without unmanaged accounts, you must manually create accounts in Cloud Identity or Google Workspace.

### Federate with Active Directory: Comparison

The following table summarizes the approaches.

| Allow single sign-on for identities with consumer accounts | Prevent automatic user provisioning for identities with consumer accounts | Prevent deletion of migrated accounts without a matching identity in the external IdP | Auto-provision new accounts | Auto-update migrated accounts  
---|---|---|---|---|---  
Approach 1: Don't configure provisioning | ✅ | ✅ | ✅ | X | X  
Approach 2: GCDS with manual assignment | ✅ | Prone to manual error | X | ✅ | ✅  
Approach 3: Disallow GCDS to create users | ✅ | ✅ | ✅ | X | ✅  
  
## Make Okta federation safe for account consolidation

To federate Cloud Identity or Google Workspace with Okta, [you can use the Google Workspace app](https://docs.cloud.google.com/architecture/identity/okta-provisioning-and-single-sign-on) from the Okta app catalog. This app can handle [single sign-on](https://saml-doc.okta.com/SAML_Docs/How-to-Enable-SAML-2.0-in-Google-Apps.html) and [provision users and groups to Cloud Identity or Google Workspace](https://saml-doc.okta.com/Provisioning_Docs/G_Suite_Provisioning.html).

When you use the Google Workspace app for provisioning, Okta ignores any existing users in Cloud Identity or Google Workspace that don't have a counterpart in Okta, so the requirement to prevent deletion of migrated accounts without a matching identity in the external IdP is always met.

Depending on how you configure Okta, you must still do the following:

  * Allow single sign-on for identities with consumer accounts.
  * Prevent automatic user provisioning for identities with consumer accounts.



There are multiple ways to meet these requirements. Each approach has advantages and disadvantages.

### Approach 1: Don't configure provisioning

In this approach, you configure the Google Workspace app to handle single sign-on but don't configure provisioning at all. By not configuring user provisioning, you prevent automatic user provisioning for identities with consumer accounts.

To allow single sign-on for identities with consumer accounts, assign the app to all identities that might eventually need access to Google services, even if their existing consumer accounts are still subject to being migrated. The Google Workspace or Google Cloud icons appear on the Okta homepage of all identities that have been assigned to the app. However, signing in will fail unless a corresponding user account happens to exist on the Google side.

For a user who has an existing consumer account, the corresponding Cloud Identity or Google Workspace user account is created automatically when the transfer request is accepted. That user can then immediately use single sign-on.

Although this approach meets the requirements and is the least complex to set up, it comes with the limitation that any attribute changes or user suspensions performed in Okta won't be propagated to Cloud Identity or Google Workspace. Another downside of this approach is that you must manually create accounts in Cloud Identity or Google Workspace for all users who don't have an existing consumer account.

### Approach 2: Provision with manual assignment

In this approach, you configure the Google Workspace app to handle single sign-on and provisioning but only enable the following provisioning features:

  * Create users
  * Update user attributes
  * Deactivate users



When you assign identities to the app, include the identities that eventually need access to Google services, but exclude all identities that are known to have an existing consumer account. This way, you prevent automatic user provisioning for identities with consumer accounts.

As soon as a user accepts a transfer request, assign the user to the app so that they are enabled to use single sign-on and access Google Workspace or Google Cloud.

One downside of this approach is that any mistake that you make in assignment can immediately lead to a conflicting account being created, which makes this approach much riskier than some of the other approaches.

Another downside of this approach is that it causes temporary lockouts of migrated accounts. After accepting a transfer request, a user has to perform any subsequent sign-ons through Okta. These sign-on attempts will fail until you have assigned the user to the app in Okta.

### Approach 3: Provision with user creation disabled

In this approach, you configure Google Workspace to handle single sign-on and provisioning but only enable the following provisioning features:

  * Update user attributes
  * Deactivate users



Leave the **Create Users** option disabled and assign all identities that eventually need access to Google services to the app. Include identities with existing consumer accounts so that you allow single sign-on for identities with consumer accounts.

By disallowing Okta to create accounts, you prevent Okta from automatically provisioning user accounts for identities with consumer accounts. At the same time, this configuration still lets Okta propagate attribute changes and user suspensions to Cloud Identity or Google Workspace for those users that have a corresponding Google Account.

For identities that don't have a corresponding user account in Cloud Identity or Google Workspace, Okta might display an error message in the Okta Admin console:

![Okta error message.](https://docs.cloud.google.com/static/architecture/identity/images/okta-error-message.png)

For a user who has an existing consumer account, the corresponding Cloud Identity or Google Workspace user account is created automatically when the transfer request is accepted. That user can then immediately use single sign-on. Although the user account is functional at this point, Okta might not display an icon on the user's home page yet and might instead continue to display the error message in the Admin UI. To fix this, retry the assignment task in the Okta Administrator Dashboard.

This approach successfully prevents Okta from automatically provisioning user accounts for identities with consumer accounts, but still allows single sign-on for identities with consumer accounts. The approach is also less prone to accidental misconfiguration than the second approach. One downside is still that for users without existing consumer accounts, you must manually create user accounts in Cloud Identity or Google Workspace.

### Approach 4: Two apps with manual assignment

You can overcome some of the disadvantages of the previous approaches by using two apps, one for provisioning and one for single sign-on:

  * Configure one instance of the Google Workspace app to handle provisioning only. The single sign-on functionality of the app is not used. By assigning users to this app, you control which accounts are being provisioned to Cloud Identity or Google Workspace. You can ensure that this app is effectively hidden from your users by enabling the **Do not display application icon to users** option.
  * Configure another instance of the Google Workspace app for single sign-on purposes only. By assigning users to this app, you control who is allowed to sign on.



Using these two apps, assign users as follows:

  * Assign all identities that eventually need access to Google services to the single sign-on app. Include identities with existing consumer accounts so that you allow single sign-on for identities with consumer accounts.
  * When assigning identities to the provisioning app, include the identities that eventually need access to Google services, but exclude all identities that are known to have an existing consumer account. This way, you prevent automatic user provisioning for identities with consumer accounts.

Whenever a user accepts a transfer request, assign the user to the app as well.


**Important:** Similar to Approach 2, a downside of this approach is that any mistake that you make in assignment can immediately lead to a conflicting account being created, making this approach substantially more risky than other approaches.

### Federate with Okta: Comparison

The following table summarizes the approaches.

| Allow single sign-on for identities with consumer accounts | Prevent automatic user provisioning for identities with consumer accounts | Prevent deletion of migrated accounts without a matching identity in the external IdP | Auto-provision new accounts | Auto-update migrated accounts  
---|---|---|---|---|---  
Approach 1: No provisioning | ✅ | ✅ | ✅ | X | X  
Approach 2: Provision with manual assignment | X | Risky | ✅ | ✅ | ✅  
Approach 3: Provision with user creation disabled | ✅ | ✅ | ✅ | X | ✅  
Approach 4: Two apps with manual assignment | ✅ | Risky | ✅ | ✅ | ✅  
  
## What's next

  * Review how you can [set up federation with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) or [Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Start your onboarding process by [preparing Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
