---
url: https://docs.cloud.google.com/architecture/identity/keycloak-single-sign-on/
title: Keycloak single sign-on \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:18.425712+00:00
---

# Keycloak single sign-on  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/keycloak-single-sign-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Keycloak single sign-on Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This guide shows how to set up single sign-on (SSO) between [Keycloak ](https://www.keycloak.org/)and your Cloud Identity or Google Workspace account by using [SAML federation](https://www.oasis-open.org/standards#samlv2.0). The document assumes you have installed and are using Keycloak.

**Note:** Keycloak does not provide built-in integration for automatically provisioning users and groups to Cloud Identity or Google Workspace. To automate user and group provisioning, you must combine Keycloak with a provisioning tool such as [Google Cloud Directory Sync](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts), which lets you provision users and groups from an LDAP server.

## Objectives

  * Configure your Keycloak server so that it can be used as an identity provider (IdP) by Cloud Identity or Google Workspace.
  * Configure your Cloud Identity or Google Workspace account so that it uses Keycloak for SSO.



## Before you begin

  1. If you don't have a Cloud Identity account, [sign up for an account](https://gsuite.google.com/signup/gcpidentity/welcome?&_ga=2.104797888.-157260409.1512652371).
  2. Make sure your Cloud Identity account has [super-admin](https://support.google.com/cloudidentity/answer/2405986?hl=en) privileges.
  3. If your Keycloak server is used to manage more than one realm, decide which realm you want to use for the federation.
  4. Ensure that you have admin access to the selected realm.



## Create a SAML profile

To configure single sign-on with Keycloak, you first create a SAML profile in your Cloud Identity or Google Workspace account. The SAML profile contains the settings related to your Keycloak server, including its URL and signing certificate.

You later assign the SAML profile to certain groups or organizational units.

To create a new SAML profile in your Cloud Identity or Google Workspace account, do the following:

  1. In the Admin Console, go to **Security > Authentication > SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Click **Third-party SSO profiles > Add SAML profile**.

  3. On the **SAML SSO profile** page, enter the following settings:

     * **Name** : `Keycloak`
     * **IDP entity ID** :

###  Keycloak 17 or later 
           
           https://KEYCLOAK/realms/REALM
           

###  Keycloak 16 or earlier 
           
           https://KEYCLOAK/auth/realms/REALM
           

     * **Sign-in page URL** :

###  Keycloak 17 or later 
           
           https://KEYCLOAK/realms/REALM/protocol/saml
           

###  Keycloak 16 or earlier 
           
           https://KEYCLOAK/auth/realms/REALM/protocol/saml
           

     * **Sign-out page URL** :

###  Keycloak 17 or later 
           
           https://KEYCLOAK/realms/REALM/protocol/openid-connect/logout
           

###  Keycloak 16 or earlier 
           
           https://KEYCLOAK/auth/realms/REALM/protocol/openid-connect/logout?redirect_uri=https://KEYCLOAK/auth/realms/REALM/account/
           

     * **Change password URL** :

###  Keycloak 17 or later 
           
           https://KEYCLOAK/realms/REALM/account
           

###  Keycloak 16 or earlier 
           
           https://KEYCLOAK/auth/realms/REALM/account
           

In all URLs, replace the following:

     * `KEYCLOAK`: the fully qualified domain name of your Keycloak server
     * `REALM`: the name of your selected realm

Don't upload a verification certificate yet.

  4. Click **Save**.

The **SAML SSO profile** page that appears contains two URLs:

     * Entity ID
     * ACS URL

You need these URLs in the next section when you configure Keycloak.




## Configure Keycloak

You configure your Keycloak server by creating a client.

### Create a client

Create a new SAML client in Keycloak:

  1. Sign in to Keycloak and open the administration console.
  2. Select the realm that you want to use for federation.
  3. In the menu, select **Clients**.
  4. Click **Create client**.
  5. Configure the following settings for the client:

###  Keycloak 19 or later 

     * **Client type** : **SAML**
     * **Client ID** : **Entity URL** from your SSO profile.
     * **Name** : `Google Cloud`

###  Keycloak 18 or earlier 

     * **Client ID** : **Entity URL** from your SSO profile.
     * **Client Protocol** : **saml**
     * **Client SAML Endpoint** : leave blank

  6. Click **Save**.

  7. Specify the details for the client by configuring the following settings:

###  Keycloak 19 or later 

On the **Settings** tab:

     * **Valid Redirect URIs** : **ACS URL** from your SSO profile
     * **Name ID Format** : **email**
     * **Force Name ID Format** : **on**
     * **Sign documents** : **off**
     * **Sign Assertions** : **on**

On the **Keys** tab:

     * **Client Signature Required** : **off**

###  Keycloak 18 or earlier 

     * **Name** : A name such as `Google Cloud`
     * **Sign Assertions** : **on**
     * **Client Signature Required** : **off**
     * **Force Name ID Format** : **on**
     * **Name ID Format** : **email**
     * **Valid Redirect URIs** : **ACS URL** from your SSO profile

Keep the default values for all other settings.

  8. Click **Save**.




### Export the signing certificate

After Keycloak authenticates a user, it passes a SAML assertion to Cloud Identity or Google Workspace. To enable Cloud Identity and Google Workspace to verify the integrity and authenticity of that assertion, Keycloak signs the assertion with a special token-signing key and provides a certificate that enables Cloud Identity or Google Workspace to check the signature.

You now export the signing certificate from Keycloak:

  1. In the menu, select **Realm settings**.
  2. Select the **Keys** tab.
  3. Find the row for **Algorithm: RS256**. If is more than one row, use the one with **Use: SIG**. Then select **Certificate**.

A dialog that contains a base64-encoded certificate appears.

  4. Copy the base64-encoded certificate value to the clipboard.




Before you can use the signing certificate, you must convert it into PEM format by adding a header and footer.

  1. Open a text editor such as Notepad or vim.
  2. Paste the following header, followed by a newline:
         
         -----BEGIN CERTIFICATE-----
         

  3. Paste the base64-encoded certificate from the clipboard.

  4. Add a newline and paste the following footer:
         
         -----END CERTIFICATE-----
         

After the change, the file looks similar to the following:
         
         -----BEGIN CERTIFICATE-----
         MIICmzCCAYMCBgF7v8/V1TANBgkq...
         -----END CERTIFICATE-----
         

  5. Save the file to a temporary location on your computer.




## Complete the SAML profile

You use the signing certificate to complete the configuration of your SAML profile:

  1. Return to the Admin Console and go to **Security > Authentication > SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Open the `Keycloak` SAML profile that you created earlier.

  3. Click the **IDP details** section to edit the settings.

  4. Click **Upload certificate** and pick the token signing certificate that you downloaded previously.

  5. Click **Save**.




Your SAML profile is complete, but you still need to assign it.

## Assign the SAML profile

Select the users for which the new SAML profile should apply:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Manage SSO profile assignments > Manage**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. In the left pane, select the group or organizational unit for which you want to apply the SSO profile. To apply the profile to all users, select the root organizational unit.

  3. In the right pane, select **Another SSO profile**.

  4. In the menu, select the `Keycloak - SAML` SSO profile that you created earlier.

  5. Click **Save**.




Repeat the steps to assign the SAML profile to another group or organizational unit.

## Test single sign-on

You've completed the single sign-on configuration. You can now check whether SSO works as intended.

  1. Choose a Keycloak user that satisfies the following criteria:

     * The user has an email address.
     * The email address corresponds to the primary email address of an existing user in your Cloud Identity or Google Workspace account.
     * The Cloud Identity user does not have super-admin privileges.

User accounts that have super-admin privileges must always sign in by using Google credentials, so they aren't suitable for testing single sign-on.

  2. Open a new browser window and go to the [Google Cloud console](https://console.cloud.google.com/).

  3. On the Google sign-in page, enter the email address of the user account, and then click **Next**.

![Google Sign in page.](https://docs.cloud.google.com/static/architecture/identity/images/sign-in-redirect-to-keycloak.png)

You are redirected to Keycloak.

  4. Enter your Keycloak credentials, and then click **Sign in**.

After successful authentication, Keycloak redirects you back to the Google Cloud console. Because this is the first login for this user, you're asked to accept the Google terms of service and privacy policy.

  5. If you agree to the terms, click **Accept**.

  6. You are redirected to the Google Cloud console, which asks you to confirm preferences and accept the Google Cloud terms of service. If you agree to the terms, click **Yes** , and then click **Agree and Continue**.

  7. Click the avatar icon, and then click **Sign out**.

You are redirected to Keycloak.




If you have trouble signing in, keep in mind that user accounts with super-admin privileges can bypass SSO, so you can still use the Admin console to verify or change settings.

## Optional: Configure redirects for domain-specific service URLs

When you link to the Google Cloud console from internal portals or documents, you can improve the user experience by using domain-specific service URLs.

Unlike regular service URLs such as `https://console.cloud.google.com/`, domain specific-service URLs include the name of your primary domain. Unauthenticated users that click a link to a domain specific-service URL are immediately redirected to Keycloak instead of being shown a Google sign-in page first.

Examples for domain-specific service URLs include the following:

Google service | URL | Logo  
---|---|---  
Gemini Enterprise | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://vertexaisearch.cloud.google.com/home/cid/ID` | ![Gemini](https://docs.cloud.google.com/static/architecture/identity/images/logo-gemini.png)  
Google Cloud console | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://console.cloud.google.com/` | ![Google Cloud logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-cloud.png)  
Google Docs | `https://docs.google.com/a/DOMAIN` | ![Google Docs logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-docs.png)  
Google Sheets | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://sheets.google.com/` | ![Google Sheets logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-sheets.png)  
Google Sites | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://slides.google.com/` | ![Google Sites logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-slides.png)  
Google Drive | `https://drive.google.com/a/DOMAIN` | ![Google Drive logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-drive.png)  
Gmail | `https://mail.google.com/a/DOMAIN` | ![Gmail logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-gmail.png)  
Google Groups | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://groups.google.com/` | ![Google Groups logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-groups.png)  
Google Keep | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://keep.google.com/` | ![Google Keep logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-keep.png)  
Data Studio | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://lookerstudio.google.com/` | ![Data Studio logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-looker.png)  
YouTube | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://www.youtube.com/` | ![YouTube logo](https://www.gstatic.com/images/branding/productlogos/youtube/v9/web-96dp/logo_youtube_color_1x_web_96dp.png)  
  
To configure domain-specific service URLs so that they redirect to Keycloak, do the following:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Domain-specific service URLs > Edit**.

[Go to domain-specific service URLs](https://admin.google.com/ac/security/sso/domain-specific-service-urls)

  2. Set **Automatically redirect users to the third-party IdP in the following SSO profile** to **enabled**.

  3. Set **SSO profile** to `Keycloak`.

  4. Click **Save**.




## Optional: Configure login challenges

Google sign-in might ask users for additional verification when they sign in from unknown devices or when their sign-in attempt looks suspicious for other reasons. These login challenges help improve security and we recommend to leave login challenges enabled.

If you find that login challenges cause too much friction, you can disable login challenges by doing the following:

  1. In the Admin Console, go to **Security > Authentication > Login challenges**.
  2. In the left pane, select an organizational unit for which you want to disable login challenges. To disable login challenges for all users, select the root organizational unit.
  3. Under **Settings for users signing in using other SSO profiles** , select **Don't ask users for additional verifications from Google**.
  4. Click **Save**.



## What's next

  * Learn more about [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview).
  * Read about [best practices for setting up an enterprise organization in Google Cloud](https://docs.cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
