---
url: https://docs.cloud.google.com/architecture/identity/azure-ad-b2b-user-provisioning-and-sso/
title: Microsoft Entra ID (formerly Azure AD) B2B user provisioning and single sign-on \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:16.912461+00:00
---

# Microsoft Entra ID (formerly Azure AD) B2B user provisioning and single sign-on  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/azure-ad-b2b-user-provisioning-and-sso/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Microsoft Entra ID (formerly Azure AD) B2B user provisioning and single sign-on Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-30 UTC

This document shows you how you can extend [Microsoft Entra ID (formerly Azure AD) user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on) to enable single sign-on (SSO) for [Microsoft Entra ID B2B collaboration users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/add-users-administrator).

The document assumes that you use Microsoft Office 365 or Microsoft Entra ID in your organization and that you've already configured [Microsoft Entra ID user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on) as in the following diagram.

![Configuring Microsoft Entra ID user provisioning and single sign-on.](https://docs.cloud.google.com/static/architecture/identity/images/entra-user-provisioning-and-sso.svg)

In this diagram, users from external identity providers (IdPs) and from other Microsoft Entra ID tenants sign on to the Microsoft Entra ID tenant through B2B sign-on.

## Objectives

  * Extend the Microsoft Entra ID user provisioning configuration to cover Microsoft Entra B2B guest users.
  * Extend the Microsoft Entra ID SSO configuration to cover Microsoft Entra B2B guest users.
  * Configure Cloud Identity to limit session lengths for guest users.



## Before you begin

Make sure you've set up [Microsoft Entra ID user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on).

**Note:** This document refers to the [Google Cloud/Google Workspace Connector by Microsoft gallery app from the Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/aad.googleapps). This app is a Microsoft product and is not maintained or supported by Google.

## Microsoft Entra B2B guest users

Microsoft Entra ID lets you invite external users as guests to your Microsoft Entra ID tenant. When you invite an external user, Microsoft Entra ID creates a guest user account in your tenant. These guest user accounts differ from regular Microsoft Entra ID user accounts in multiple ways:

  * Guest users don't have a password. To sign on, guest users are automatically redirected to their home tenant or to the external identity provider (IdP) that they've been invited from.
  * The user principal name (UPN) of the guest user account uses a prefix derived from the invitee's email address, combined with the tenant's initial domain—for example: `prefix#EXT#@tenant.onmicrosoft.com`.
  * If you invite a user from a different Microsoft Entra ID tenant and the user is later deleted in its home tenant, then the guest user account remains active in your Microsoft Entra ID tenant.



These differences affect the way you configure user provisioning and single sign-on:

  * Because `onmicrosoft.com` is a Microsoft-owned DNS domain, you cannot add `tenant.onmicrosoft.com` as a secondary domain to your Cloud Identity or Google Workspace account. This caveat means that you cannot use the guest user's UPN as primary email address when provisioning the user to Cloud Identity or Google Workspace.

To provision guest users to Cloud Identity or Google Workspace, you must set up a mapping that transforms the guest user's UPN into a domain used by your Cloud Identity or Google Workspace account.

In this document, you set up a UPN mapping as indicated in the following table.

| Original UPN in Microsoft Entra ID | Primary email address in Cloud Identity or Google Workspace  
---|---|---  
**Regular user** | `alice@example.com` | `alice@example.com`  
**Microsoft Entra ID guest** | `charlie@altostrat.com` | `charlie_altostrat.com@example.com`  
**External guest** | `user@hotmail.com` | `user_hotmail.com@example.com`  
**Note:** The primary email address used for guest users must use the primary domain of your Cloud Identity or Google Workspace account.
  * When a user is deleted in its home tenant, Microsoft Entra ID won't suspend the corresponding user in Cloud Identity or Google Workspace. This poses a security risk: Although any attempts to use single sign-on will fail for such a user, existing browser sessions and refresh tokens (including those used by the Google Cloud CLI) might remain active for days or weeks, allowing the user to continue accessing resources.

Using the approach presented in this document, you can mitigate this risk by provisioning guest users to a dedicated organizational unit in Cloud Identity or Google Workspace, and by applying a policy that restricts the session length to 8 hours. The policy ensures that browser sessions and existing refresh tokens are invalidated at most 8 hours after the user has been deleted in its home tenant, effectively revoking all access. The user in Cloud Identity or Google Workspace stays active, however, until you delete the guest user from your Microsoft Entra ID account.




## Prepare your Cloud Identity or Google Workspace account

Create an organizational unit in your Cloud Identity or Google Workspace account that all guest users will be provisioned to.

  1. Open the [Admin Console](https://admin.google.com) and sign in using the super-admin user created when you signed up for Cloud Identity or Google Workspace.
  2. In the menu, go to **Directory > Organizational units**.
  3. Click **Create organizational unit** and provide a name and description for the OU: 
     1. **Name of organizational unit** : `guests`
     2. **Description** : `Microsoft Entra B2B guest users`
  4. Click **Create**.



Apply a policy to the organizational unit that limits the session length to 8 hours. The session length not only applies to browser sessions, but also restricts the lifetime of OAuth refresh tokens.

  1. In the Admin Console, go to **Security > Access and data control > Google Cloud session control**.
  2. Select the organizational unit **guests** and apply the following settings:

     * **Reauthentication policy** : **Require reauthentication**
     * **Reauthentication frequency** : **8 hours**.

This duration reflects the maximum amount of time a guest user might still be able to access Google Cloud resources after it has been suspended in Microsoft Entra ID.

     * **Reauthentication method** : **Password**.

This setting ensures that users have to re-authenticate by using Microsoft Entra ID after a session has expired.

  3. Click **Override**.


**Note:** The configuration change can take up to 24 hours to take effect.

## Configure Microsoft Entra ID provisioning

You are now ready to adjust your existing Microsoft Entra ID configuration to support provisioning of B2B guest users.

  1. In the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID > Enterprise applications**.
  2. Select the enterprise application **Google Cloud (Provisioning)** , which [you use for user provisioning](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#create_an_enterprise_application).
  3. Click **Manage > Provisioning**.
  4. Click **Edit provisioning**.
  5. Under **Mappings** , click **Provision Microsoft Entra ID Users**.
  6. Select the row **userPrincipalName**.
  7. In the **Edit Attribute** dialog, apply the following changes:

     1. **Mapping type** : Change from **Direct** to **Expression**.
     2. **Expression** :

`Replace([originalUserPrincipalName], "#EXT#@TENANT_DOMAIN", , , "@PRIMARY_DOMAIN", , )`

Replace the following:

        * `TENANT_DOMAIN`: the `.onmicrosoft.com` domain of your Microsoft Entra ID tenant, such as `tenant.onmicrosoft.com`.
        * `PRIMARY_DOMAIN`: the primary domain name used by your Cloud Identity or Google Workspace account, such as `example.org`.
  8. Click **OK**.

  9. Select **Add new mapping**.

  10. In the **Edit Attribute** dialog, configure the following settings:

     1. **Mapping type** : **Expression**.
     2. **Expression** :

`IIF(Instr([originalUserPrincipalName], "#EXT#", , )="0", "/", "/guests")`

     3. **Target attribute** : **OrgUnitPath**

  11. Click **OK**.

  12. Click **Save**.

  13. Click **Yes** to confirm that saving changes will result in users and groups being resynchronized.

  14. Close the **Attribute Mapping** dialog.




## Configure Microsoft Entra ID for single sign-on

To ensure that guest users can authenticate by using single sign-on, you now extend your existing Microsoft Entra ID configuration to enable single sign-on for guests:

  1. In the Azure portal, go to **Microsoft Entra ID > Enterprise applications**.
  2. Select the **Google Cloud** enterprise application, which [you use for single sign-on](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#enterprise-application-sso).
  3. Click **Manage > Single sign-on**.
  4. On the ballot screen, click the **SAML** card.
  5. On the **User Attributes & Claims** card, click **Edit**.
  6. Select the row labeled **Unique User Identifier (Name ID)**.
  7. Select **Claim conditions**.
  8. Add a conditional claim for external guests: 
     * **User type** : **External guests**
     * **Source** : **Transformation**
     * **Transformation** : **RegexReplace()**
     * **Parameter 1** : **Attribute**
     * **Attribute** : **user.userprincipalname**
     * **Regex pattern** : `(?'username'^.*?)#EXT#@(?i).*\.onmicrosoft\.com$`
     * **Replacement pattern** : `{username}@PRIMARY_DOMAIN`, replacing `PRIMARY_DOMAIN` with the primary domain name used by your Cloud Identity or Google Workspace account.
  9. Click **Add**.
  10. Add a conditional claim for Microsoft Entra ID guests from different tenants:

     * **User type** : **Microsoft Entra guests**
     * **Source** : **Transformation**
     * **Transformation** : **RegexReplace()**
     * **Parameter 1** : **Attribute**
     * **Attribute** : **user.localuserprincipalname**

**Note:** Make sure to select **user.localuserprincipalname** instead of **user.userprincipalname**
     * **Regex pattern** : `(?'username'^.*?)#EXT#@(?i).*\.onmicrosoft\.com$`

     * **Replacement pattern** : `{username}@PRIMARY_DOMAIN`, replacing `PRIMARY_DOMAIN` with the primary domain name used by your Cloud Identity or Google Workspace account.

  11. Click **Add**.

  12. Add a conditional claim for regular Microsoft Entra ID users:

     * **User type** : **Members**
     * **Source** : **Attribute**
     * **Value** : **user.userprincipalname**
  13. Click **Save**.




## Test single sign-on

To verify that the configuration works correctly, you need three test users in your Microsoft Entra ID tenant:

  * A regular Microsoft Entra ID user.
  * A Microsoft Entra ID guest user. This is a user that has been invited from a different Microsoft Entra ID tenant.
  * An external guest user. This is a user that has been invited using a non–Microsoft Entra ID email address such as a `@hotmail.com` address.



For each user, you perform the following test:

  1. Open a new incognito browser window and go to the <https://console.cloud.google.com/>.
  2. In the Google Sign-In page that appears, enter the email address of the user as it appears in the **Primary email address in Cloud Identity or Google Workspace** column of the earlier table. Refer to that table to see how the email address in Cloud Identity or Google Workspace derives from the user principal name.

You are redirected to Microsoft Entra ID where you see another sign-in prompt.

  3. At the sign-in prompt, enter the UPN of the user and follow the instructions to authenticate.

After successful authentication, Microsoft Entra ID redirects you back to Google Sign-In. Because this is the first time you've signed in using this user, you are asked to accept the Google Terms of Service and privacy policy.

  4. If you agree to the terms, click **Accept**.

You are redirected to the Google Cloud console, which asks you to confirm preferences and accept the Google Cloud Terms of Service.

  5. If you agree to the terms, choose **Yes** , and then click **Agree and continue**.

  6. Click the avatar icon, and then click **Sign out**.

You are redirected to a Microsoft Entra ID page confirming that you have been successfully signed out.




## What's next

  * Learn more about [federating Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external IdP](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).



## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
