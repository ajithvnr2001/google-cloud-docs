---
url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-configuring-single-sign-on/
title: Active Directory single sign-on \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:21.223524+00:00
---

# Active Directory single sign-on  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-configuring-single-sign-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Active Directory single sign-on Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This article shows you how to set up [single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on) between your [Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services) environment and your Cloud Identity or Google Workspace account by using Microsoft [Active Directory Federation Services](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) (AD FS) and [SAML Federation](https://www.oasis-open.org/standards#samlv2.0).

The article assumes that you understand [how Active Directory identity management can be extended to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) and have already [configured user provisioning](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts). The article also assumes that you have a working AD FS 4.0 server that is running on Windows Server 2016 or a later version of Windows Server.

To follow this guide, knowledge of Active Directory Domain Services and AD FS is required. You also need a user in Cloud Identity or Google Workspace that has [super-admin](https://support.google.com/cloudidentity/answer/2405986?hl=en) privileges and a user in Active Directory that has administrative access to your AD FS server.

## Objectives

  * Configure your AD FS server so that Cloud Identity or Google Workspace can use it as an identity provider.
  * Create a claims issuance policy that matches identities between Active Directory and Cloud Identity or Google Workspace.
  * Configure your Cloud Identity or Google Workspace account so that it delegates authentication to AD FS.



## Costs

If you're using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902?hl=en), following this article will not use any billable components of Google Cloud.

## Before you begin

  1. Verify that your AD FS server runs Windows Server 2016 or later. While you can also configure single sign-on by using previous versions of Windows Server and AD FS, the necessary configuration steps might be different from what this article describes.
  2. Make sure you understand [how Active Directory identity management can be extended to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
  3. Configure [user provisioning between Active Directory and Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts).
  4. Consider setting up AD FS in a server farm configuration in order to avoid it becoming a single point of failure. After you've enabled single sign-on, the availability of AD FS determines whether users can log in to the Google Cloud console.



## Understanding single sign-on

By using [Google Cloud Directory Sync](https://tools.google.com/dlpage/dirsync/), you've already automated the creation and maintenance of users and tied their lifecycle to the users in Active Directory.

Although GCDS provisions user account details, it doesn't synchronize passwords. Whenever a user needs to authenticate in Google Cloud, the authentication must be delegated back to Active Directory, which is done by using AD FS and the Security Assertion Markup Language (SAML) protocol. This setup ensures that only Active Directory has access to user credentials and is enforcing any existing policies or multi-factor authentication (MFA) mechanisms. Moreover, it establishes a single sign-on experience between your on-premises environment and Google.

For more details on single sign-on, see [Single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on)

## Create a SAML profile

To configure single sign-on with AD FS, you first create a SAML profile in your Cloud Identity or Google Workspace account. The SAML profile contains the settings related to your AD FS instance, including its URL and signing certificate.

You later assign the SAML profile to certain groups or organizational units.

To create a new SAML profile in your Cloud Identity or Google Workspace account, do the following:

  1. In the Admin Console, go to **SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Click **Third-party SSO profiles > Add SAML profile**.

  3. On the **SAML SSO profile** page, enter the following settings:

     * **Name** : `AD FS`
     * **IDP entity ID** :
           
           https://ADFS/adfs/services/trust
           

     * **Sign-in page URL** :
           
           https://ADFS/adfs/ls/
           

     * **Sign-out page URL** :
           
           https://ADFS/adfs/ls/?wa=wsignout1.0
           

     * **Change password URL** :
           
           https://ADFS/adfs/portal/updatepassword/
           

In all URLs, replace `ADFS` with the fully qualified domain name of your AD FS server.

Don't upload a verification certificate yet.

  4. Click **Save**.

The **SAML SSO profile** page that appears contains two URLs:

     * Entity ID
     * ACS URL

You need these URLs in the next section when you configure AD FS.




## Configure AD FS

You configure your AD FS server by creating a relying party trust.

### Creating the relying party trust

Create a new relying party trust:

  1. Connect to your AD FS server and open the **AD FS Management** MMC snap-in.
  2. Select **AD FS > Relying Party Trusts**.
  3. On the **Actions** pane, click **Add relying party trust**.
  4. On the **Welcome** page of the wizard, select **Claims aware** , and click **Start**.
  5. On the **Select data source** page, select **Enter data about the relying party manually** , and click **Next**.
  6. On the **Specify display name** page, enter a name such as `Google Cloud` and click **Next**.
  7. On the **Configure certificate** page, click **Next**.
  8. On the **Configure URL** page, select **Enable support for the SAML 2.0 WebSSO protocol** , and enter the **ACS URL** from your SAML profile. Then click **Next**.

![Enable support for the SAML 2.0 WebSSO protocol.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-sso-service.png)

  9. On the **Configure identifiers** page, add the **Entity ID** from your SAML profile.

![Relying party trust identifiers.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-trust-ids.png)

Then click **Next**.

  10. On the **Choose access control policy** page, choose an appropriate access policy and click **Next**.

  11. On the **Ready to Add Trust** page, review your settings, and then click **Next**.

  12. On the final page, clear the **Configure claims issuance policy** checkbox and close the wizard.

In the list of relying party trusts, you see a new entry.




### Configuring the logout URL

When you're enabling users to use single sign-on across multiple applications, it's important to allow them to sign out across multiple applications:

  1. Open the relying party trust that you just created.
  2. Select the **Endpoints** tab.
  3. Click **Add SAML** and configure the following settings:

     1. **Endpoint type** : **SAML Logout**
     2. **Binding** : **POST**
     3. **Trusted URL** :
            
            https://ADFS/adfs/ls/?wa=wsignout1.0
            

Replace `ADFS` with the fully qualified domain name of your AD FS server.

![Add an endpoint.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-add-endpoint.png)

  4. Click **OK**.

  5. Click **OK** to close the dialog.




### Configuring the claims mapping

After AD FS has authenticated a user, it issues a SAML assertion. This assertion serves as proof that authentication has successfully taken place. The assertion must identify who has been authenticated, which is the purpose of the [`NameID` claim](https://support.google.com/a/answer/6330801?hl=en).

To enable Google Sign-In to associate the `NameID` with a user, the `NameID` must contain the primary email address of that user. Depending on how you are [mapping users](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_account_identities) between Active Directory and Cloud Identity or Google Workspace, the `NameID` must contain the UPN or the email address from the Active Directory user, with domain substitutions applied as necessary.

### UPN

  1. In the list of relying party trusts, select the trust that you just created and click **Edit claim issuance policy**.
  2. Click **Add rule**
  3. On the **Choose rule type** page of the **Add transform claim rule** wizard, select **Transform an incoming claim** , then click **Next**.
  4. On the **Configure claim rule** page, configure the following settings:

     * **Claim rule name** : `Name Identifier`
     * **Incoming claim type** : **UPN**
     * **Outgoing claim type** : **Name ID**
     * **Outgoing name ID format** : **Email**
  5. Select **Pass through all claim values** and click **Finish**.

  6. Click **OK** to close the claim issuance policy dialog.




### UPN: domain substitution

  1. In the list of relying party trusts, select the trust that you just created and click **Edit claim issuance policy**.
  2. Click **Add rule**
  3. On the **Choose rule type** page of the **Add transform claim rule** wizard, select **Transform an incoming claim** , then click **Next**.
  4. On the **Configure claim rule** page, configure the following settings:

     * **Claim rule name** : `Name Identifier`
     * **Incoming claim type** : **UPN**
     * **Outgoing claim type** : **Name ID**
     * **Outgoing name ID format** : **Email**
  5. Select **Replace incoming claim e-mail suffix with a new e-mail suffix** and configure the following setting:

     * **New e-mail suffix** : A domain name used by your Cloud Identity or Google Workspace account.
  6. Click **Finish** , and then click **OK**.




### Email

  1. In the list of relying party trusts, select the trust that you just created and click **Edit claim issuance policy**.
  2. Add a rule to lookup the email address: 
     1. In the dialog, click **Add Rule**.
     2. Select **Send LDAP Attributes as Claims** , and click **Next**.
     3. On the next page, apply the following settings: 
        1. **Claim rule name** : `Email address`
        2. **Attribute Store** : **Active Directory**
     4. Add a row to the list of LDAP attribute mappings: 
        1. **LDAP Attribute** : **E-Mail-Addresses**
        2. **Outgoing Claim Type** : **E-Mail-Address**
     5. Click **Finish**.
  3. Add another rule to set the `NameID`:

     1. Click **Add rule**
     2. On the **Choose rule type** page of the **Add transform claim rule** wizard, select **Transform an incoming claim** , then click **Next**.
     3. On the **Configure claim rule** page, configure the following settings:

        * **Claim rule name** : `Name Identifier`
        * **Incoming claim type** : **E-Mail-Address**
        * **Outgoing claim type** : **Name ID**
        * **Outgoing name ID format** : **Email**
     4. Select **Pass through all claim values** and click **Finish**.

     5. Click **OK** to close the claim issuance policy dialog.




### Email: domain substitution

  1. In the list of relying party trusts, select the trust that you just created and click **Edit claim issuance policy**.
  2. Add a rule to lookup the email address: 
     1. In the dialog, click **Add Rule**.
     2. Select **Send LDAP Attributes as Claims** , and click **Next**.
     3. On the next page, apply the following settings: 
        1. **Claim rule name** : `Email address`
        2. **Attribute Store** : **Active Directory**
     4. Add a row to the list of LDAP attribute mappings: 
        1. **LDAP Attribute** : **E-Mail-Addresses**
        2. **Outgoing Claim Type** : **E-Mail-Address**
     5. Click **Finish**.
  3. Add another rule to set the `NameID` value:

     1. Click **Add rule**
     2. On the **Choose rule type** page of the **Add transform claim rule** wizard, select **Transform an incoming claim** , then click **Next**.
     3. On the **Configure claim rule** page, configure the following settings:

        * **Claim rule name** : `Name Identifier`
        * **Incoming claim type** : **E-Mail-Address**
        * **Outgoing claim type** : **Name ID**
        * **Outgoing name ID format** : **Email**
  4. Select **Replace incoming claim e-mail suffix with a new e-mail suffix** and configure the following setting:

     * **New e-mail suffix** : A domain name used by your Cloud Identity or Google Workspace account.
  5. Click **Finish** , and then click **OK**.single-sign-on




### Exporting the AD FS token-signing certificate

After AD FS authenticates a user, it passes a SAML assertion to Cloud Identity or Google Workspace. To enable Cloud Identity and Google Workspace to verify the integrity and authenticity of that assertion, AD FS signs the assertion with a special token-signing key and provides a certificate that enables Cloud Identity or Google Workspace to check the signature.

Export the signing certificate from AD FS by doing the following:

  1. In the AD FS Management console, click **Service > Certificates**.
  2. Right-click the certificate that is listed under **Token-signing** , and click **View Certificate**.
  3. Select the **Details** tab.
  4. Click **Copy to File** to open the Certificate Export Wizard.
  5. On the **Welcome to the certificate export wizard** , click **Next**.
  6. On the **Export private key** page, select **No, do not export the private key**.
  7. On the **Export file format** page, select **Base-64 encoded X.509 (.CER)** and click **Next**.
  8. On the **File to export** page, provide a local filename, and click **Next**.
  9. Click **Finish** to close the dialog.
  10. Copy the exported certificate to your local computer.



## Complete the SAML profile

You use the signing certificate to complete the configuration of your SAML profile:

  1. Return to the Admin Console and go to **Security > Authentication > SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Open the `AD FS` SAML profile that you created earlier.

  3. Click the **IDP details** section to edit the settings.

  4. Click **Upload certificate** and pick the token signing certificate that you exported from AD FS.

  5. Click **Save**.


**Note:** The token-signing certificate is valid for a limited period of time. Depending on [your configuration](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ts-td-certs-ad-fs), AD FS either renews the certificate automatically before it expires, or it requires you to provide a new certificate before the current certificate expires. In both cases, you must update your configuration to use the new certificate.

Your SAML profile is complete, but you still need to assign it.

## Assign the SAML profile

Select the users for which the new SAML profile should apply:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Manage SSO profile assignments > Manage**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. In the left pane, select the group or organizational unit for which you want to apply the SSO profile. To apply the profile to all users, select the root organizational unit.

  3. In the right pane, select **Another SSO profile**.

  4. In the menu, select the `AD FS - SAML` SSO profile that you created earlier.

  5. Click **Save**.




Repeat the steps to assign the SAML profile to another group or organizational unit.

## Test single sign-on

You've completed the single sign-on configuration. You can check whether SSO works as intended.

  1. Choose an Active Directory user that satisfies the following criteria:

     * The user has been provisioned to Cloud Identity or Google Workspace.
     * The Cloud Identity user does not have super-admin privileges.

User accounts that have super-admin privileges must always sign in by using Google credentials, so they aren't suitable for testing single sign-on.

  2. Open a new browser window and go to <https://console.cloud.google.com/>.

  3. On the Google Sign-In page that appears, enter the email address of the user, and click **Next**. If you use domain substitution, you must apply the substitution to the email address.

![enter the email address of the user](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-email-address.png)

You are redirected to AD FS. If you configured AD FS to use forms-based authentication, you see the sign-in page.

  4. Enter your UPN and password for the Active Directory user, and click **Sign in**.

![Enter your UPN and password for the Active Directory user.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-account.png)

  5. After successful authentication, AD FS redirects you back to the Google Cloud console. Because this is the first login for this user, you're asked to accept the Google terms of service and privacy policy.

  6. If you agree to the terms, click **Accept**.

  7. You are redirected to the Google Cloud console, which asks you to confirm preferences and accept the Google Cloud terms of service. If you agree to the terms, click **Yes** , and then click **Agree and Continue**.

  8. At the upper left, click the avatar icon, and click **Sign out**.

You are redirected to an AD FS page confirming that you've been successfully signed out.




If you have trouble signing in, you might find additional information in the [AD FS admin log](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-logging).

Keep in mind that users that have super-admin privileges are exempted from single sign-on, so you can still use the Admin console to verify or change settings.

## Optional: Configure redirects for domain-specific service URLs

When you link to the Google Cloud console from internal portals or documents, you can improve the user experience by using domain-specific service URLs.

Unlike regular service URLs such as `https://console.cloud.google.com/`, domain specific-service URLs include the name of your primary domain. Unauthenticated users that click a link to a domain specific-service URL are immediately redirected to AD FS instead of being shown a Google sign-in page first.

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
  
To configure domain-specific service URLs so that they redirect to AD FS, do the following:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Domain-specific service URLs > Edit**.

[Go to domain-specific service URLs](https://admin.google.com/ac/security/sso/domain-specific-service-urls)

  2. Set **Automatically redirect users to the third-party IdP in the following SSO profile** to **enabled**.

  3. Set **SSO profile** to `AD FS`.

  4. Click **Save**.




## Optional: Configure login challenges

Google sign-in might ask users for additional verification when they sign in from unknown devices or when their sign-in attempt looks suspicious for other reasons. These login challenges help to improve security, and we recommend that you leave login challenges enabled.

If you find that login challenges cause too much inconvenience, you can disable login challenges by doing the following:

  1. In the Admin Console, go to **Security > Authentication > Login challenges**.
  2. In the left pane, select an organizational unit for which you want to disable login challenges. To disable login challenges for all users, select the root organizational unit.
  3. Under **Settings for users signing in using other SSO profiles** , select **Don't ask users for additional verifications from Google**.
  4. Click **Save**.



## Clean up

If you don't intend to keep single sign-on enabled for your organization, follow these steps to disable single sign-on in Cloud Identity or Google Workspace:

  1. In the Admin Console and go to **Manage SSO profile assignments**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. For each profile assignment, do the following:

     1. Open the profile.
     2. If you see an **Inherit** button, click **Inherit**. If you don't see an **Inherit** button, select **None** and click **Save**.
  3. Return to the **SSO with third-party IDPs** page and open the **AD FS** SAML profile.

  4. Click **Delete**.




To clean up configuration in AD FS, follow these steps:

  1. Connect to your AD FS server and open the **AD FS** MMC snap-in.
  2. In the menu at left, right-click the **Relying Party Trusts** folder.
  3. In the list of relying party trusts, right-click the relying party trust you created, and click **Delete**.
  4. Confirm the deletion by clicking **Yes**.



## What's next

  * Learn more about [federating Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
  * Learn about [Microsoft Entra ID (formerly Azure AD) B2B user provisioning and single sign-on](https://docs.cloud.google.com/architecture/identity/azure-ad-b2b-user-provisioning-and-sso).
  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Acquaint yourself with our [best practices for managing super-admin users.](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
