---
url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on/
title: Microsoft Entra ID (formerly Azure AD) user provisioning and single sign-on \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:22.149658+00:00
---

# Microsoft Entra ID (formerly Azure AD) user provisioning and single sign-on  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Microsoft Entra ID (formerly Azure AD) user provisioning and single sign-on Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-03-06 UTC

This document shows you how to set up user provisioning and single sign-on between a [Microsoft Entra ID (formerly Azure AD)](https://azure.microsoft.com/services/active-directory/) tenant and your Cloud Identity or Google Workspace account.

The document assumes that you already use Microsoft Office 365 or Microsoft Entra ID in your organization and want to use Microsoft Entra ID for allowing users to authenticate with Google Cloud. Microsoft Entra ID itself might be connected to an on-premises Active Directory and might use Entra ID federation, pass-through authentication, or password hash synchronization.

## Objectives

  * Set up Microsoft Entra ID to automatically provision users and, optionally, groups to Cloud Identity or Google Workspace.
  * Configure single sign-on to allow users to sign in to Google Cloud by using a Microsoft Entra ID user account or a user that has been provisioned from Active Directory to Microsoft Entra ID.



## Costs

If you are using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902), setting up federation with Microsoft Entra ID won't use any billable components of Google Cloud.

Check the [Microsoft Entra ID pricing page](https://azure.microsoft.com/pricing/details/active-directory/) for any fees that might apply to using Microsoft Entra ID.

## Before you begin

  * Make sure you understand the differences between [connecting Google Cloud to Microsoft Entra ID versus directly connecting Google Cloud to Active Directory](https://docs.cloud.google.com/solutions/federating-gcp-with-active-directory-introduction).
  * Decide how you want to map [identities](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_users), [groups](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_groups), and [domains](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_dns_domains) between Microsoft Entra ID and Cloud Identity or Google Workspace. Specifically, answer the following questions: 
    * Do you plan to use email addresses or User Principal Names (UPNs) as common identifiers for users?
    * Do you plan to provision groups? If so, do you plan to map groups by email address or by name?
    * Do you plan to provision all users to Google Cloud or only a select subset of users?
  * Before connecting your production Microsoft Entra ID tenant to Google Cloud, consider using a Microsoft Entra ID test tenant for setting up and testing user provisioning.
  * [Sign up for Cloud Identity](https://workspace.google.com/signup/gcpidentity/welcome?&_ga=2.104797888.-157260409.1512652371) if you don't have an account already.
  * If you're using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902) and intend to provision more than 50 users, [request an increase](https://support.google.com/cloudidentity/answer/7295541) of the total number of free Cloud Identity users through your support contact.
  * If you suspect that any of the domains you plan to use for Cloud Identity could have been used by employees to register consumer accounts, consider migrating these user accounts first. For more details, see [Assessing existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).

**Note:** This document refers to the [_Google Cloud/G Suite Connector by Microsoft_ gallery app from the Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/aad.googleapps). This app is a Microsoft product and is not maintained or supported by Google.

## Prepare your Cloud Identity or Google Workspace account

Create a dedicated user for Microsoft Entra ID, grant that user the necessary privileges, and register the necessary domains.

### Create a user for Microsoft Entra ID

To let Microsoft Entra ID access your Cloud Identity or Google Workspace account, you must create a user for Microsoft Entra ID in your Cloud Identity or Google Workspace account.

The Microsoft Entra ID user is only intended for automated provisioning. Therefore, it's best to keep it separate from other user accounts by placing it in a separate organizational unit (OU). Using a separate OU also ensures that you can later [disable single sign-on](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#disable_sso_for_super-admin_users) for the Microsoft Entra ID user.

  1. Create a new OU:

     1. Open the [Admin Console](https://admin.google.com) and log in using the super-admin user created when you signed up for Cloud Identity or Google Workspace.
     2. In the menu, go to **Directory > Organizational units**.
     3. Click **Create organizational unit** and provide a name and description for the OU: 
        * **Name** : `Automation`
        * **Description** : `Automation users`
     4. Click **Create**.
  2. Create a user account for Microsoft Entra ID and place it in the `Automation` OU. For detailed instructions, see [Add an account for a new user](https://support.google.com/a/answer/33310) or [Add an account for multiple users (Beta)](https://support.google.com/a/answer/16499021).

     1. When you create the account, provide an appropriate name and email address such as the following:

        * **First Name** : `Microsoft Entra ID`
        * **Last Name** : `Provisioning`
        * **Primary email** : `azuread-provisioning`

Keep the primary domain for the email address.

     2. For the user account, set the **Organizational unit** to the `Automation` OU that you created previously. For details, see [Move users to an organizational unit](https://support.google.com/a/answer/182449).

     3. Configure a password:

        * If the password option is available on the page, ensure that **Automatically generate a new password** isn't selected, and then enter a password. Make sure that **Ask for a password change at the next sign-in** isn't selected.
        * If the password option isn't available on the page, save the new user account, and then [reset the user's password](https://support.google.com/a/answer/33319).



### Assign privileges to Microsoft Entra ID

To let Microsoft Entra ID create, list, and suspend users and groups in your Cloud Identity or Google Workspace account, you must grant the `azuread-provisioning` user additional privileges as follows:

  * To allow Microsoft Entra ID to manage all users, including [delegated administrators](https://support.google.com/a/answer/9807615) and [super-admin users](https://support.google.com/a/answer/2405986), you must make the `azuread-provisioning` user a super-admin.

  * To allow Microsoft Entra ID to manage non-admin users only, it's sufficient to make the `azuread-provisioning` user a delegated administrator. As a delegated administrator, Microsoft Entra ID can't manage other delegated administrators or super-admin users.




###  Super-admin 

**Note:** The super-admin role grants the user full access to Cloud Identity, Google Workspace, and Google Cloud resources.

To make the `azuread-provisioning` user a super-admin, do the following:

  1. Locate the newly created user in the list and click the user's name to open their account page.
  2. Under **Admin roles and privileges** , click **Assign roles**.
  3. Enable the super-admin role.
  4. Click **Save**.



###  Delegated administrator 

To make the `azuread-provisioning` user a delegated administrator, create a new admin role and assign it to the user:

  1. In the menu, go to **Account > Admin roles**.
  2. Click **Create new role**.
  3. Provide a name and description for the role such as the following: 
     * **Name** : `Microsoft Entra ID`
     * **Description** : `Role for automated user and group provisioning`
  4. Click **Continue**.
  5. On the next screen, scroll down to the section named **Admin API privileges** and set the following privileges to **enabled** : 
     * **Organization Units > Read**
     * **Users**
     * **Groups**
  6. Click **Continue**.
  7. Click **Create role**.
  8. Click **Assign users**.
  9. Select the `azuread-provisioning` user and click **Assign role**.



**Warning:** To protect the user against credential theft and malicious use, we recommend that you enable [2-step verification](https://support.google.com/a/answer/175197) for the user. For more details on how to protect super-admin users, see [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373).

### Register domains

In Cloud Identity and Google Workspace, users and groups are identified by email address. The domains used by these email addresses must be registered and verified first.

Prepare a list of DNS domains that you need to register:

  * If you plan to map users by UPN, include all domains used by UPNs. If in doubt, include all custom domains of your Microsoft Entra ID tenant.
  * If you plan to map users by email address, include all domains used in email addresses. The list of domains might be different from the list of custom domains of your Microsoft Entra ID tenant.



If you plan to provision groups, amend the list of DNS domains:

  * If you plan to map groups by email address, include all domains used in group email addresses. If in doubt, include all custom domains of your Microsoft Entra ID tenant.
  * If you plan to map groups by name, include a dedicated subdomain like `groups.PRIMARY_DOMAIN`, where `PRIMARY_DOMAIN` is the primary domain name of your Cloud Identity or Google Workspace account.



Now that you've identified the list of DNS domains, you can register any missing domains. For each domain on the list not yet registered, perform the following steps:

  1. In the Admin Console, go to **Account > Domains > Manage domains**.
  2. Click **Add a domain**.
  3. Enter the domain name and select **Secondary domain**.
  4. Click **Add domain and start verification** and follow the instructions to verify ownership of the domain.



## Configure Microsoft Entra ID provisioning

### Create an enterprise application

You are ready to connect Microsoft Entra ID to your Cloud Identity or Google Workspace account by setting up the [_Google Cloud/G Suite Connector by Microsoft_ gallery app from the Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/aad.googleapps).

**Note:** This app is a Microsoft product and is not maintained or supported by Google.

The gallery app can be configured to handle both user provisioning and single sign-on. In this document, you use two instances of the gallery app—one for user provisioning and one for single sign-on.

First, create an instance of the gallery app to handle user provisioning:

  1. Open the [Azure portal](https://portal.azure.com/) and sign in as a user with _global administrator_ privileges.
  2. Select **Microsoft Entra ID > Enterprise applications**.
  3. Click **New application**.
  4. Search for **Google Cloud** , and then click the **Google Cloud/G Suite Connector by Microsoft** item in the result list.
  5. Set the name of the application to `Google Cloud (Provisioning)`.
  6. Click **Create**.
  7. Adding the application may take a few seconds, you should then be redirected to a page titled **Google Cloud (Provisioning) - Overview**.
  8. In the Azure Portal menu, click **Manage > Properties**: 
     1. Set **Enabled for users to sign-in** to **No**.
     2. Set **Assignment required** to **No**.
     3. Set **Visible to users** to **No**.
     4. Click **Save**.
  9. In the Azure Portal menu, click **Manage > Provisioning**:

     1. Click **Get started**.
     2. Change **Provisioning Mode** to **Automatic**.
     3. Click **Admin Credentials > Authorize**.
     4. Sign in using the `azuread-provisioning@DOMAIN` user you created earlier, where `DOMAIN` is the primary domain of your Cloud Identity or Google Workspace account.

**Note:** If you configured your Cloud Identity or Google Workspace account to [restrict access](https://support.google.com/a/answer/7281227#restrictaccess) for third-party apps, signing in might fail with the error message `Access blocked: Authorization Error` (error code `admin_policy_enforced`) or `Access blocked: Your institution’s admin needs to review Azure Active Directory` (error code `access_not_configured`). To resolve this error, grant the Google Cloud Connector app access by adding the client ID `283861851054-1n5jlu9rm93njt6kh3k5k7pqv73q7d8d.apps.googleusercontent.com` [to your list of trusted apps](https://support.google.com/a/answer/7281227#add_new_app).
     5. Because this is the first time you've signed on using this user, you are asked to accept the Google Terms of Service and privacy policy.

     6. If you agree to the terms, click **I understand**.

     7. Confirm access to the Cloud Identity API by clicking **Allow**.

     8. Click **Test Connection** to verify that Microsoft Entra ID can successfully authenticate with Cloud Identity or Google Workspace.

     9. Click **Save**.




### Configure user provisioning

The right way to configure user provisioning depends on whether you intend to map users by email address or by UPN.

### UPN

  1. Under **Mappings** , click **Provision Entra ID Users**.
  2. For the attributes **surname** and **givenName** , do the following: 
     1. Click **Edit**.
     2. Set **Default value if null** to `_`.
     3. Click **OK**.
  3. Click **Save**.
  4. Confirm that saving changes will result in users and groups being resynchronized by clicking **Yes**.
  5. Click **X** to close the **Attribute Mapping** dialog.



### UPN: domain substitution

  1. Under **Mappings** , click **Provision Entra ID Users**.
  2. For the attribute **userPrincipalName** , do the following:

     1. Click **Edit**.
     2. Configure the following mapping:

        * **Mapping type** : **Expression**
        * **Expression** :
              
              Replace([userPrincipalName], "@DOMAIN", , , "@SUBSTITUTE_DOMAIN", , )
              

Replace the following:

        * `DOMAIN`: domain name you want to replace
        * `SUBSTITUTE_DOMAIN` domain name to use instead
     3. Click **OK**.

  3. For the attributes **surname** and **givenName** , do the following:

     1. Click **Edit**.
     2. Set **Default value if null** to `_`.
     3. Click **OK**.
  4. Click **Save**.

  5. Confirm that saving changes will result in users and groups being resynchronized by clicking **Yes**.

  6. Click **X** to close the **Attribute Mapping** dialog.




### Email address

  1. Under **Mappings** , click **Provision Entra ID Users**.
  2. For the attribute **userPrincipalName** , do the following: 
     1. Click **Edit**.
     2. Set **Source attribute** to **mail**.
     3. Click **OK**.
  3. For the attributes **surname** and **givenName** , do the following: 
     1. Click **Edit**.
     2. Set **Default value if null** to `_`.
     3. Click **OK**.
  4. Click **Save**.
  5. Confirm that saving changes will result in users and groups being resynchronized by clicking **Yes**.
  6. Click **X** to close the **Attribute Mapping** dialog.



You must configure mappings for `primaryEmail`, `name.familyName`, `name.givenName`, and `suspended`. All other attribute mappings are optional.

When you configure additional attribute mappings, note the following:

  * The _Google Cloud/G Suite Connector by Microsoft_ gallery currently doesn't let you assign [email aliases](https://support.google.com/domains/answer/6304345).
  * The _Google Cloud/G Suite Connector by Microsoft_ gallery currently doesn't let you assign licenses to users. As a workaround, consider setting up [automatic licensing for organizational units](https://support.google.com/a/answer/6342682).
  * To assign a user to an organization unit, add a mapping for `OrgUnitPath`. The path must begin with a `/` character, must omit the root, and must refer to an organizational unit that already exists. For example, if the full path is example.com > employees > engineering, specify `/employees/engineering`.



### Configure group provisioning

The right way to configure group provisioning depends on whether your groups are mail-enabled. If groups aren't mail-enabled, or if groups use an email address ending with "onmicrosoft.com", you can derive an email address from the group's name.

### No group mapping

  1. Under **Mappings** , click **Provision Entra ID Groups**.
  2. Set **Enabled** to **No**.
  3. Click **Save**.
  4. Confirm that saving changes will result in users and groups being resynchronized by clicking **Yes**.
  5. Click **X** to close the **Attribute Mapping** dialog.



### Name

  1. Under **Mappings** section, click **Provision Entra ID Groups**.
  2. For the attribute **mail** , do the following: 
     1. Click **Edit**.
     2. Configure the following settings: 
        1. **Mapping type** : **Expression**.
        2. **Expression** : `Join("@", NormalizeDiacritics(StripSpaces([displayName])), "GROUPS_DOMAIN")`. Replace `GROUPS_DOMAIN` with the domain that all group email addresses are supposed to use—for example, `groups.example.com`.
        3. **Target attribute** : **email**.
     3. Click **OK**.
  3. Click **Save**.
  4. Confirm that saving changes will result in users and groups being resynchronized by clicking **Yes**.
  5. Click **X** to close the **Attribute Mapping** dialog.



### Email address

  * If you map groups by email address, keep the default settings.



### Configure user assignment

If you know that only a [certain subset of users need access to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#onboarding), you can optionally restrict the set of users to be provisioned by [assigning the enterprise app](https://docs.microsoft.com/azure/active-directory/manage-apps/assign-user-or-group-access-portal) to specific users or groups of users.

If you want all users to be provisioned, you can skip the following steps.

  1. In the Azure Portal menu, click **Manage > Users and groups**.
  2. Add the users or groups you want to provision. If you select a group, all members of this group are automatically provisioned.
  3. Click **Assign**.



### Enable automatic provisioning

The next step is to configure Microsoft Entra ID to automatically provision users to Cloud Identity or Google Workspace:

  1. In the Azure Portal menu, click **Manage > Provisioning**.
  2. Select **Edit provisioning**.
  3. Set **Provisioning Status** to **On**.
  4. Under **Settings** , set **Scope** to one of the following:

     1. **Sync only assigned users and groups** if you have configured user assignment.
     2. **Sync all users and groups** otherwise.

If this box to set the scope isn't displayed, click **Save** and refresh the page.

  5. Click **Save**.




Microsoft Entra ID starts an initial synchronization. Depending on the number of users and groups in the directory, this process can take several minutes or hours. You can refresh the browser page to see the status of the synchronization at the bottom of the page or select **Audit Logs** in the menu to see more details.

After the initial synchronization has completed, Microsoft Entra ID will periodically propagate updates from Microsoft Entra ID to your Cloud Identity or Google Workspace account. For further details on how Microsoft Entra ID handles user and group modifications, see [Mapping the user lifecycle](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_the_user_lifecycle) and [Mapping the group lifecycle](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#mapping_the_group_lifecycle).

### Troubleshooting

If the synchronization doesn't start within five minutes, you can force it to start by doing the following:

  1. Click **Edit provisioning**.
  2. Set **Provisioning Status** to **Off**.
  3. Click **Save**.
  4. Set **Provisioning Status** to **On**.
  5. Click **Save**.
  6. Close the provisioning dialog.
  7. Click **Restart provisioning**.



If synchronization still doesn't start, click **Test Connection** to verify that your credentials have been saved successfully.

## Configure Microsoft Entra ID for single sign-on

Although all relevant Microsoft Entra ID users are now automatically being provisioned to Cloud Identity or Google Workspace, you cannot use these users to sign in yet. To allow users to sign in, you still need to configure single sign-on.

### Create a SAML profile

To configure single sign-on with Microsoft Entra ID, you first create a SAML profile in your Cloud Identity or Google Workspace account. The SAML profile contains the settings related to your Microsoft Entra ID tenant, including its URL and signing certificate.

You later assign the SAML profile to certain groups or organizational units.

To create a new SAML profile in your Cloud Identity or Google Workspace account, do the following:

  1. In the Admin Console, go to **SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Click **Third-party SSO profiles > Add SAML profile**.

  3. On the **SAML SSO profile** page, enter the following settings:

     * **Name** : `Entra ID`
     * **IDP entity ID** : Leave blank
     * **Sign-in page URL** : Leave blank
     * **Sign-out page URL:** : Leave blank
     * **Change password URL:** : Leave blank

Don't upload a verification certificate yet.

  4. Click **Save**.

The **SAML SSO profile** page that appears contains two URLs:

     * Entity ID
     * ACS URL

You need these URLs in the next section when you configure Microsoft Entra ID.




### Create a Microsoft Entra ID application

Create a second enterprise application to handle single sign-on:

  1. In the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID > Enterprise applications**.
  2. Click **New application**.
  3. Search for **Google Cloud** , and then click **Google Cloud/G Suite Connector by Microsoft** in the result list.
  4. Set the name of the application to `Google Cloud`.
  5. Click **Create**.

Adding the application may take a few seconds. You are then redirected to a page titled **Google Cloud - Overview**.

  6. In the Azure Portal menu, click **Manage > Properties**.

  7. Set **Enabled for users to sign-in** to **Yes**.

  8. Set **Assignment required** to **Yes** unless you want to allow all users to use single sign-on.

  9. Click **Save**.




#### Configure user assignment

If you already know that only a [certain subset of users need access to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory#onboarding), you can optionally restrict the set of users to be allowed to sign in by [assigning the enterprise app](https://docs.microsoft.com/azure/active-directory/manage-apps/assign-user-or-group-access-portal) to specific users or groups of users.

If you set **User assignment required** to **No** before, then you can skip the following steps.

  1. In the Azure Portal menu, click **Manage > Users and groups**.
  2. Add the users or groups you want to allow single sign-on for.
  3. Click **Assign**.



#### Enable single sign-on

To enable Cloud Identity to use Microsoft Entra ID for authentication, you must adjust some settings:

  1. In the Azure Portal menu, click **Manage > Single sign-on**.
  2. On the ballot screen, click the **SAML** card.
  3. On the **Basic SAML Configuration** card, click _edit_ **Edit**.
  4. In the **Basic SAML Configuration** dialog, enter the following settings:

     1. **Identifier (Entity ID)** : 
        * Add the **Entity URL** from your SSO profile and set **Default** to **enabled**.
        * Remove all other entries.
     2. **Reply URL** : Add the **ACS URL** from your SSO profile.
     3. **Sign on URL** :
            
            https://www.google.com/a/PRIMARY_DOMAIN/ServiceLogin?continue=https://console.cloud.google.com/
            

Replace `PRIMARY_DOMAIN` with the primary domain name used by your Cloud Identity or Google Workspace account.

  5. Click **Save** , and then dismiss the dialog by clicking **X**.

  6. On the **SAML Certificates** card, find the entry labeled **Certificate (Base 64)** and click **Download** to download the certificate to your local computer.

  7. On the **Set up Google Cloud** card, you find two URLs:

     * Login URL
     * Microsoft Entra ID Identifier

You need these URLs in the next section when you complete the SAML profile.




The remaining steps differ depending on whether you map users by email address or by UPN.

### UPN

  1. On the **Attributes & Claims** card, click _edit_ **Edit**.
  2. Delete all claims listed under **Additional claims**. You can delete records by clicking the **…** button and selecting **Delete**.

The list of attributes and claims looks like the following:

![User Attributes & Claims dialog.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-ad-configuring-provisioning-and-sso-add-claim-upn.png)

  3. Dismiss the dialog by clicking **X**.




### UPN: domain substitution

  1. On the **User Attributes & Claims** card, click _edit_ **Edit**.
  2. Delete all claims listed under **Additional claims**. You can delete records by clicking the **…** button and selecting **Delete**.

The list of attributes and claims looks like the following:

![User Attributes & Claims dialog.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-ad-configuring-provisioning-and-sso-add-claim-upn.png)

  3. Click **Unique User Identifier (Name ID)** to change the claims mapping.

  4. Set **Source** to **Transformation** and configure the following transformation:

     * **Transformation** : **ExtractMailPrefix()**
     * **Parameter 1** : **user.userPrincipalName**
  5. Select **Add transformation** and configure the following transformation:

     * **Transformation** : **Join()**
     * **Separator** : `@`
     * **Parameter 2** : Enter the substitute domain name.

You must use the same substitute domain name for user provisioning and single sign-on. If the domain name isn't listed, you might need to [verify it first ](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/domains-manage#add-custom-domain-names-to-your-azure-ad-organization).

  6. Click **Add**.

  7. Click **Save**.

  8. Dismiss the dialog by clicking **X**.




### Email address

  1. On the **User Attributes & Claims** card, click _edit_ **Edit**.
  2. Select the row labeled **Unique User Identifier (Name ID)**.
  3. Change **Source attribute** to **user.mail**.
  4. Click **Save**.
  5. Delete all claims listed under **Additional claims**. To delete all records, click _more_horiz_ , and then click **Delete**.

![User Attributes & Claims dialog.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-ad-configuring-provisioning-and-sso-add-claim.png)

  6. Dismiss the dialog by clicking _close_.




### Complete the SAML profile

Complete the configuration of your SAML profile:

  1. Return to the Admin Console and go to **Security > Authentication > SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Open the `Entra ID` SAML profile that you created earlier.

  3. Click the **IDP details** section to edit the settings.

  4. Enter the following settings:

     * **IDP entity ID** : Enter the **Microsoft Entra Identifier** from the **Set up Google Cloud** card in the Azure Portal.
     * **Sign-in page URL** : Enter the **Login URL** from the **Set up Google Cloud** card in the Azure Portal.
     * **Sign-out page URL** : `https://login.microsoftonline.com/common/wsfederation?wa=wsignout1.0`
     * **Change password URL** : `https://account.activedirectory.windowsazure.com/changepassword.aspx`
  5. Under **Verification certificate** , click **Upload certificate** , and then pick the token signing certificate that you downloaded previously.

  6. Click **Save**.




The Microsoft Entra ID token signing certificate is valid for [a limited amount of time](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-manage-certificates-for-federated-single-sign-on) and you must rotate the certificate before it expires. For more information, see Rotate a single sign-on certificate later in this document.

Your SAML profile is complete, but you still need to assign it.

### Assign the SAML profile

Select the users for which the new SAML profile should apply:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Manage SSO profile assignments > Manage**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. On the left pane, select the group or organizational unit for which you want to apply the SSO profile. To apply the profile to all users, select the root organizational unit.

  3. On the right pane, select **Another SSO profile**.

  4. In the menu, select the `Entra ID - SAML` SSO profile that you created earlier.

**Warning:** Make sure you don't accidentally use the `Microsoft - OIDC` profile.
  5. Click **Save**.




To assign the SAML profile to another group or organizational unit, repeat the steps above.

Update the SSO settings for the `Automation` OU to [disable single sign-on](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#disable_sso_for_super-admin_users):

  1. On the left pane, select the `Automation` OU.
  2. On the right pane, select **None**.
  3. Click **Override**.



### Optional: Configure redirects for domain-specific service URLs

When you link to the Google Cloud console from internal portals or documents, you can improve the user experience by using domain-specific service URLs.

Unlike regular service URLs such as `https://console.cloud.google.com/`, domain specific-service URLs include the name of your primary domain. Unauthenticated users that click a link to a domain specific-service URL are immediately redirected to Entra ID instead of being shown a Google sign-in page first.

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
  
To configure domain-specific service URLs so that they redirect to Entra ID, do the following:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Domain-specific service URLs > Edit**.

[Go to domain-specific service URLs](https://admin.google.com/ac/security/sso/domain-specific-service-urls)

  2. Set **Automatically redirect users to the third-party IdP in the following SSO profile** to **enabled**.

  3. Set **SSO profile** to `Entra ID`.

  4. Click **Save**.




You can use domain-specific service URLs to add individual Google services to the Microsoft My Apps portal. For further details, see [Microsoft My Apps portal integration](https://docs.cloud.google.com/architecture/identity/integrating-google-services-and-apps-with-azure-ad-portal#adding_links).

### Optional: Configure login challenges

Google sign-in might ask users for additional verification when they sign in from unknown devices or when their sign-in attempt looks suspicious for other reasons. These login challenges help to improve security, and we recommend that you leave login challenges enabled.

If you find that login challenges cause too much inconvenience, you can disable login challenges by doing the following:

  1. In the Admin Console, go to **Security > Authentication > Login challenges**.
  2. In the left pane, select an organizational unit for which you want to disable login challenges. To disable login challenges for all users, select the root organizational unit.
  3. Under **Settings for users signing in using other SSO profiles** , select **Don't ask users for additional verifications from Google**.
  4. Click **Save**.



### Test single sign-on

Now that you've completed the single sign-on configuration in both Microsoft Entra ID and Cloud Identity or Google Workspace, you can access Google Cloud in two ways:

  * Through the list of apps in your [Microsoft Office portal](https://www.office.com/).
  * Directly by opening <https://console.cloud.google.com/>.



To check that the second option works as intended, run the following test:

  1. Pick a Microsoft Entra ID user that has been provisioned to Cloud Identity or Google Workspace and that doesn't have super-admin privileges assigned. Users with super-admin privileges always have to sign in using Google credentials and are therefore not suitable for testing single sign-on.
  2. Open a new browser window and go to <https://console.cloud.google.com/>.
  3. In the Google Sign-In page that appears, enter the email address of the user and click **Next**. If you use domain substitution, this address must be the email address with the substitution applied.

![Google Sign-In dialog.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-ad-configuring-provisioning-and-sso-google-dialog.png)

  4. You are redirected to Microsoft Entra ID and will see another sign-in prompt. Enter the email address of the user (without domain substitution) and click **Next**.

![Microsoft Entra ID sign-in dialog.](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-azure-ad-configuring-provisioning-and-sso-azure-ad-dialog.png)

  5. After entering your password, you are prompted whether to stay signed in or not. For now, choose **No**.

After successful authentication, Microsoft Entra ID should redirect you back to Google Sign-In. Because this is the first time you've signed in using this user, you are asked to accept the Google Terms of Service and privacy policy.

  6. If you agree to the terms, click **I understand**.

You are redirected to the Google Cloud console, which asks you to confirm preferences and accept the Google Cloud Terms of Service.

  7. If you agree to the terms, choose **Yes** and click **Agree and continue**.

  8. Click the avatar icon on the top left of the page, and then click **Sign out**.

You are redirected to a Microsoft Entra ID page confirming that you have been successfully signed out.




Keep in mind that users with super-admin privileges are exempted from single sign-on, so you can still use the Admin Console to verify or change settings.

## Rotate a single sign-on certificate

The Microsoft Entra ID token signing certificate is valid for only several months, and you must replace the certificate before it expires.

To rotate a signing certificate, add an additional certificate to the Microsoft Entra ID application:

  1. In the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID > Enterprise applications** and open the application that you created for single sign-on.
  2. In the Azure Portal menu, click **Manage > Single sign-on**.
  3. On the **SAML Certificates** card, click _edit_ **Edit**.

You see a list of one or more certificates. One certificate is marked as **Active**.

  4. Click **New certificate**.

  5. Keep the default signing settings and click **Save**.

The certificate is added to the list of certificates and is marked as **Inactive**.

  6. Select the new certificate and click **_more_horiz_ > Base64 certificate download**.

Keep the browser window open and don't close the dialog.




To use the new certificate, do the following:

  1. Open a new browser tab or window.

  2. Open the Admin Console and go to **SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  3. Open the `Entra ID` SAML profile.

  4. Click **IDP details**.

  5. Click **Upload another certificate** and select the new certificate that you downloaded previously.

  6. Click **Save**.

  7. Return to the Microsoft Entra ID portal and the **SAML Certificates** dialog.

  8. Select the new certificate and click **_more_horiz_ > Make certificate active**.

  9. Click **Yes** to activate the certificate.

Microsoft Entra ID now uses the new signing certificate.

  10. Test that SSO still works as expected. For more information, see Test single sign-on.




To remove the old certificate, do the following:

  1. Return to the Admin Console and the `Entra ID` SAML profile.
  2. Click **IDP details**.
  3. Under **Verification certificate** , compare the expiry dates of your certificates to find the old certificate and click _delete_.
  4. Click **Save**.



## Migrate from a legacy SSO profile to a SAML profile

If you set up single sign-on between Microsoft Entra ID and your Cloud Identity or Google Workspace account in 2023 or earlier, you might be using a legacy SSO profile. This section explains the differences between SAML profiles and legacy SSO profiles and shows you how to migrate from a legacy SSO profile to a SAML profile.

### SAML profiles and legacy SSO profiles compared

Legacy SSO profiles are deprecated. We recommend that you [replace them with SAML profiles](https://support.google.com/a/answer/15209818). SAML profiles differ from legacy profiles in several ways, including the following:

  * You can create multiple SAML profiles and assign them to one or more organizational units or groups. In contrast, you can only create a single legacy SSO profile for each Cloud Identity or Google Workspace account.
  * SAML profiles use a different format from legacy SSO profiles for [entity IDs and assertion consumer service (ACS) URLs](https://docs.cloud.google.com/architecture/identity/single-sign-on#configuration).
  * When you use SAML profiles, login challenges are [enabled by default](https://support.google.com/a/answer/6002699#ssochallenges). In contrast, when you use a legacy SSO profile, login challenges are disabled by default.



### Migrate from a legacy SSO profile to a SAML profile

To migrate from a legacy SSO profile to a SAML profile in a way that minimizes disruption, do the following:

  1. In the Azure portal, open the enterprise application that you use for single sign-on and do the following:

     1. In the Azure Portal menu, click **Manage > Single sign-on**.
     2. On the **SAML Certificates** card, find the entry that's labeled **Certificate (Base 64)** , and then click **Download** to download the certificate to your local computer.
     3. On the **Set up Google Cloud** card, take note of the following:

        * Login URL
        * Microsoft Entra ID Identifier

You need this information when you create a SAML profile.

  2. In the Admin Console, go to **Security > Authentication > Login challenges**.

[Go to Login challenges](https://admin.google.com/ac/managedsettings/352555445522/loginchallenge)

For each organization unit, do the following:

     1. Select an organization unit.
     2. Click **Post-SSO verification** and modify the **Settings for users signing in using other SSO profiles** so that they match the **Settings for users signing in using the SSO profile for your organization**.

In this dialog, _other SSO profiles_ refers to the SAML profiles and _SSO profile for your organization_ refers to your legacy SSO profile.

     3. Click **Save** or **Override**.

  3. In the Admin Console, go to **SSO with third-party IdP** and do the following:

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

     1. Click **Third-party SSO profiles > Add SAML profile**.

     2. On the **SAML SSO profile** page, enter the following information:

        * **Name** : `Entra ID`
        * **IDP entity ID** : Enter the **Microsoft Entra Identifier** from the **Set up Google Cloud** card in the Azure Portal.
        * **Sign-in page URL** : Enter the **Login URL** from the **Set up Google Cloud** card in the Azure Portal.
        * **Sign-out page URL** : `https://login.microsoftonline.com/common/wsfederation?wa=wsignout1.0`
        * **Change password URL** : `https://account.activedirectory.windowsazure.com/changepassword.aspx`
     3. For **Verification certificate** , click **Upload certificate** , and then select the token signing certificate that you downloaded previously.

     4. Click **Save**.

     5. On the **SAML SSO profile** page, take note of the following:

        * Entity ID
        * ACS URL

You need this information when you configure Microsoft Entra ID.

  4. Return to the Azure portal, open the enterprise application that you use for single sign-on and do the following:

     1. In the Azure Portal menu, click **Manage > Single sign-on**.
     2. On the **Basic SAML Configuration** card, click _edit_ **Edit**.
     3. For **Identifier (Entity ID)** , add the **Entity URL** from the SAML profile that you created.

**Important:** Don't remove any of the existing identifiers yet.
     4. For **Reply URL (Assertion Consumer Service URL)** , add the **ACS URL** from the SAML profile that you created.

**Important:** Don't remove the existing ACS URL yet.
     5. Click **Save** , and then dismiss the dialog by clicking **X**.

  5. Return to the Admin Console and go to **Security > Authentication > SSO with third party IdP**, and then click **Manage SSO profile assignments > Manage**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  6. For each existing SSO profile assignment that uses the **Legacy SSO profile** , do the following:

     1. Change the SSO profile from **Legacy SSO profile** to **Entra ID - SAML**.
     2. Select **Have Google prompt for their username, then redirect them to this profile's IDP sign-in page**.
     3. Click **Save**.
  7. Go back to the **SSO with third-party IDPs** page, and then click **Domain-specific service URLs > Edit**.

[Go to domain-specific service URLs](https://admin.google.com/ac/security/sso/domain-specific-service-urls)

     1. If **Automatically redirect users to the third-party IdP in the following SSO profile** is currently set to **enabled** , change the SSO profile to **Entra ID - SAML**.

If **Automatically redirect users to the third-party IdP in the following SSO profile** is set to **disabled** , you can skip this step.

     2. Click **Save**.

  8. Return to the Azure portal, open the enterprise application that you use for single sign-on and do the following:

     1. In the Azure Portal menu, click **Manage > Single sign-on**.
     2. On the **Basic SAML Configuration** card, click _edit_ **Edit**.
     3. For **Identifier (Entity ID)** , remove `google.com` and `http://google.com`.
     4. For **Reply URL (Assertion Consumer Service URL)** , remove `https://www.google.com/`.
     5. Click **Save** , and then dismiss the dialog by clicking **X**.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To disable single sign-on in your Cloud Identity or Google Workspace account, follow these steps:

  1. In the Admin Console and go to **Manage SSO profile assignments**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. For each profile assignment, do the following:

     1. Open the profile.
     2. If you see an **Inherit** button, click **Inherit**. If you don't see an **Inherit** button, select **None** and click **Save**.
  3. Return to the **SSO with third-party IDPs** page and open the **Microsoft Entra ID** SAML profile.

  4. Click **Delete**.




You can remove single sign-on and provisioning settings in Microsoft Entra ID as follows:

  1. In the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID > Enterprise applications**.
  2. From the list of applications, choose **Google Cloud**.
  3. In the Azure Portal menu, click **Manage > Single sign-on**.
  4. Click **Delete**.
  5. Confirm the deletion by clicking **Yes**.



## What's next

  * Learn more about [federating Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory)
  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Acquaint yourself with our [best practices for managing super-admin accounts.](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices)



## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
