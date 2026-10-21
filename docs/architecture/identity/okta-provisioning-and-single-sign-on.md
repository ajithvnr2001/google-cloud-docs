---
url: https://docs.cloud.google.com/architecture/identity/okta-provisioning-and-single-sign-on/
title: Okta user provisioning and single sign-on \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:34.101752+00:00
---

# Okta user provisioning and single sign-on  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/okta-provisioning-and-single-sign-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Okta user provisioning and single sign-on Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-30 UTC

This document shows you how to set up user provisioning and single sign-on between an [Okta organization](https://developer.okta.com/docs/concepts/okta-organizations/) and your Cloud Identity or Google Workspace account.

The document assumes that you already use Okta in your organization and want to use Okta for allowing users to authenticate with Google Cloud.

## Objectives

  * Configure Okta to automatically provision users and, optionally, groups to Cloud Identity or Google Workspace.
  * Configure single sign-on to allow users to sign in to Google Cloud by using an Okta user account.



## Costs

If you are using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902), setting up federation with Okta won't use any billable components of Google Cloud.

Check the [Okta pricing page](https://www.okta.com/pricing/) for any fees that might apply to using Okta.

## Before you begin

  * [Sign up for Cloud Identity](https://workspace.google.com/signup/gcpidentity/welcome?&_ga=2.104797888.-157260409.1512652371) if you don't have an account already.
  * If you're using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902) and intend to provision more than 50 users, [request an increase](https://support.google.com/cloudidentity/answer/7295541) of the total number of free Cloud Identity users through your support contact.
  * If you suspect that any of the domains you plan to use for Cloud Identity could have been used by employees to register consumer accounts, consider migrating these user accounts first. For more details, see [Assessing existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).



## Preparing your Cloud Identity or Google Workspace account

### Create a user for Okta

To let Okta access your Cloud Identity or Google Workspace account, you must create a user for Okta in your Cloud Identity or Google Workspace account.

The Okta user is only intended for automated provisioning. Therefore, it's best to keep it separate from other user accounts by placing it in a separate organizational unit (OU). Using a separate OU also ensures that you can later [disable single sign-on](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#disable_sso_for_super-admin_users) for the Okta user.

  1. Create a new OU:

     1. Open the [Admin Console](https://admin.google.com) and log in using the super-admin user created when you signed up for Cloud Identity or Google Workspace.
     2. In the menu, go to **Directory > Organizational units**.
     3. Click **Create organizational unit** and provide a name and description for the OU: 
        * **Name** : `Automation`
        * **Description** : `Automation users`
     4. Click **Create**..
  2. Create a user account for Okta and place it in the `Automation` OU. For detailed instructions, see [Add an account for a new user](https://support.google.com/a/answer/33310) or [Add an account for multiple users (Beta)](https://support.google.com/a/answer/16499021).

     1. When you create the account, provide an appropriate name and email address such as the following:

        * **First Name** : `Okta`
        * **Last Name** : `Provisioning`
        * **Primary email** : `okta-provisioning`

Keep the primary domain for the email address.

     2. For the user account, set the **Organizational unit** to the `Automation` OU that you created previously. For details, see [Move users to an organizational unit](https://support.google.com/a/answer/182449).

     3. Configure a password:

        * If the password option is available on the page, ensure that **Automatically generate a new password** isn't selected, and then enter a password. Make sure that **Ask for a password change at the next sign-in** isn't selected.
        * If the password option isn't available on the page, save the new user account, and then [reset the user's password](https://support.google.com/a/answer/33319).



### Assign privileges to Okta

To let Okta create, list, and suspend users and groups in your Cloud Identity or Google Workspace account, you must make the `okta-provisioning` user a super-admin:

  1. Locate the newly created user in the list and click the user's name to open their account page.
  2. Under **Admin roles and privileges** , click **Assign roles**.
  3. Enable the super-admin role.
  4. Click **Save**.

**Note:** The super-admin role grants the user full access to Cloud Identity, Google Workspace, and Google Cloud resources.**Warning:** To protect the user against credential theft and malicious use, we recommend that you enable [2-step verification](https://support.google.com/a/answer/175197) for the user. For more details on how to protect super-admin users, see [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373).

## Configuring Okta provisioning

You are now ready to connect Okta to your Cloud Identity or Google Workspace account by setting up the [Google Workspace application from the Okta catalog](https://www.okta.com/integrations/google-workspace/).

**Note:** This application is an Okta product and is not maintained or supported by Google.

The Google Workspace application can handle both user provisioning and single sign-on. Use this application even if you're using Cloud Identity and you're only planning to set up single sign-on for Google Cloud.

### Create an application

To set up the Google Workspace application, do the following:

  1. Open the Okta admin dashboard and sign in as a user with _Super Administrator_ privileges.
  2. In the menu, go to **Applications > Applications**.
  3. Click **Browse app catalog**.
  4. Search for `Google Workspace` and select the **Google Workspace** application.
  5. Click **Add integration**.
  6. On the **General settings** page, configure the following:

     * **Application label** : `Google Cloud`
     * **Your Google Apps company domain** : the primary domain name used by your Cloud Identity or Google Workspace account.
     * **Display the following links** :

       * Set **Account** to **enabled**.
       * Set other links to **enabled** if you're using Google Workspace, set other links to **disabled** otherwise.
     * **Application Visibility** : set to **enabled** if you're using Google Workspace, **disabled** otherwise

     * **Browser plugin auto-submit** : set to **disabled**

  7. Click **Next**.

  8. On the **Sign-on options** page, configure the following:

     * **Sign on methods** : select **SAML 2.0**
     * **Default Relay State** : leave empty
     * **Advanced Sign-on Settings > RPID**: leave empty
  9. Decide how you want to populate the primary email address for users in Cloud Identity or Google Workspace. A user's primary email address must use either the primary domain of your Cloud Identity or Google Workspace account or one of its secondary domains.

### Okta username

To use user's Okta username as primary email address, use the following settings:

     * **Application username format** : **Okta username**
     * **Update application username on** : **Create and update**.

### Email

To use user's Okta username as primary email address, use the following settings:

     * **Application username format** : **Email**
     * **Update application username on** : **Create and update**.

  10. Click **Done**.




### Configure user provisioning

In this section, you configure Okta to automatically provision users and groups to Google Cloud.

  1. On the settings page for the **Google Cloud** application, open the **Provisioning** tab.
  2. Click **Configure API Integration** and configure the following:

     * **Enable API integration** : set to to **enabled**
     * **Import Groups** : set to **disabled** unless you have existing groups in Cloud Identity or Google Workspace that you want to import to Okta
  3. Click **Authenticate with Google Workspace**.

  4. Sign in using the `okta-provisioning@DOMAIN` user you created earlier, where `DOMAIN` is the primary domain of your Cloud Identity or Google Workspace account.

  5. Review the Google Terms of Service and privacy policy. If you agree to the terms, click **I understand**.

  6. Confirm access to the Cloud Identity API by clicking **Allow**.

  7. Click **Save**.




Okta is connected to your Cloud Identity or Google Workspace account, but provisioning is still disabled. To enable provisioning, do the following:

  1. On the settings page for the **Google Cloud** application, open the **Provisioning** tab.
  2. Click **Edit** and configure the following:

     * **Create users** : set to **enabled**
     * **Update user attributes** : set to **enabled**
     * **Deactivate users** : set to **enabled**
     * **Sync password** : set to **disabled**
**Note:** You might need to adjust these settings if you're planning to consolidate existing consumer accounts. For more details, see [Making Okta federation safe for account consolidation](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation#making_okta_federation_safe_for_account_consolidation)
  3. Optionally, click **Go to profile editor** to customize attribute mappings.

If you use custom mappings, you must map `userName`, `nameGivenName`, and `nameFamilyName`. All other attribute mappings are optional.

  4. Click **Save**.




### Configure user assignment

In this section, you configure which Okta users to provision to Cloud Identity or Google Workspace:

  1. On the settings page for the **Google Cloud** application, open the **Assignments** tab.
  2. Click **Assign > Assign to people** or **Assign > Assign to groups**.
  3. Select a user or group and click **Assign**.
  4. On the assignment dialog that appears, keep the default settings and click **Save and go back**.
  5. Click **Done**.



Repeat the steps in this section for each user or group that you want to provision. To provision all users to Cloud Identity or Google Workspace, assign the **Everyone** group.

### Configure group assignment

Optionally, you can let Okta provision groups to Cloud Identity or Google Workspace. Instead of selecting groups individually, it's best to configure Okta to provision groups based on a naming convention.

For example, to let Okta provision all groups that begin with `google-cloud`, do the following:

  1. On the settings page for the **Google Cloud** application, open the **Push groups** tab.
  2. Click **Push groups > Find groups by role**.
  3. On the **Push groups by rule** page, configure the following rule:

     * **Rule name** : name for the role, for example `Google Cloud`.
     * **Group name** : **starts with** `google-cloud`
  4. Click **Create rule**.




### Troubleshooting

To troubleshoot user or group provisioning, click **View logs** on the settings page for the **Google Cloud** application.

To let Okta retry a failed attempt to provision users, do the following:

  1. Go to **Dashboard > Tasks**.
  2. Find the failed task and open the details.
  3. On the details page, click **Retry selected**.



## Configuring Okta for single sign-on

If you've followed the steps to configure Okta provisioning, all relevant Okta users are now automatically being provisioned to Cloud Identity or Google Workspace. To allow these users to sign in, configure single sign-on:

  1. On the settings page for the **Google Cloud** application, open the **Sign on** tab.
  2. Click **SAML 2.0 > More details**.
  3. Click **Download** to download the signing certificate.
  4. Note the **Sign-on URL** , **Sign-out URL** , and **Issuer** values, you need these in one of the following steps.



### Create a SAML profile

Create a SAML profile in your Cloud Identity or Google Workspace account:

  1. Return to the Admin Console and go to **SSO with third-party IdP**.

[Go to SSO with third-party IdP](https://admin.google.com/ac/security/sso)

  2. Click **Third-party SSO profiles > Add SAML profile**.

  3. On the **SAML SSO profile** page, enter the following settings:

     * **Name** : `Okta`
     * **IDP entity ID** : Enter the **Issuer** from the Okta admin dashboard.
     * **Sign-in page URL** : Enter the **Sign-on URL** from the Okta admin dashboard.
     * **Sign-out page URL:** : Enter the **Sign-out URL** from the Okta admin dashboard.
     * **Change password URL:** : `https://ORGANIZATION.okta.com/enduser/settings` where `ORGANIZATION` is the name of your Okta organization.
  4. Under **Verification certificate** , click **Upload certificate** , and then pick the token signing certificate that you downloaded previously.

  5. Click **Save**.

The **SAML SSO profile** page that appears contains an **Entity ID** in the format `https://accounts.google.com/samlrp/RPID` where `RPID` is a unique ID.

Note the **RPID** value. You need it in the next step.




### Assign the SAML profile

Select the users for which the new SAML profile should apply:

  1. In the Admin Console, on the **SSO with third-party IDPs** page, click **Manage SSO profile assignments > Manage**.

[Go to Manage SSO profile assignments](https://admin.google.com/ac/security/sso/sso-profile-assignments)

  2. On the left pane, select the group or organizational unit for which you want to apply the SSO profile. To apply the profile to all users, select the root organizational unit.

  3. On the right pane, in the menu, select the `Okta - SAML` SSO profile that you created earlier.

  4. Click **Save**.




To assign the SAML profile to another group or organizational unit, repeat the steps above.

Update the SSO settings for the `Automation` OU to [disable single sign-on](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#disable_sso_for_super-admin_users):

  1. On the left pane, select the `Automation` OU.
  2. Change the SSO profile assignment to **None**.
  3. Click **Override**.



### Complete the SSO configuration in Okta

Return to Okta and complete the SSO configuration:

  1. In the Okta admin dashboard, on the settings page for the **Google Cloud** application, open the **Sign on** tab.
  2. Click **Edit** and update the following settings:

     * **Advanced Sign-on Settings > RPID**: enter the **RPID** that you copied from the Admin Console.
**Note:** Make sure you only enter the **RPID** value, not the entire Entity ID. The **RPID** value must not contain any `/` character.
  3. Click **Save**.




### Optional: Configure login challenges

Google sign-in might ask users for additional verification when they sign in from unknown devices or when their sign-in attempt looks suspicious for other reasons. These login challenges help to improve security, and we recommend that you leave login challenges enabled.

If you find that login challenges cause too much inconvenience, you can disable login challenges by doing the following:

  1. In the Admin Console, go to **Security > Authentication > Login challenges**.
  2. In the left pane, select an organizational unit for which you want to disable login challenges. To disable login challenges for all users, select the root organizational unit.
  3. Under **Settings for users signing in using other SSO profiles** , select **Don't ask users for additional verifications from Google**.
  4. Click **Save**.



## Add the Google Cloud console and other Google services to the app dashboard

To add the Google Cloud console and, optionally, other Google services to your users' Okta app dashboard, do the following:

  1. In the Okta admin dashboard, select **Applications > Applications**.
  2. Click **Browse app catalog**.
  3. Search for `Bookmark app` and select the **Bookmark app** application.
  4. Click **Add integration**.
  5. On the **General settings** page, configure the following:

     * **Application label** : `Google Cloud console`
     * **URL** : `https://www.google.com/a/PRIMARY_DOMAIN/ServiceLogin?continue=https://console.cloud.google.com/`, replacing `PRIMARY_DOMAIN` with the primary domain name used by your Cloud Identity or Google Workspace account.
  6. Click **Done**.

  7. Change the application logo to the [Google Cloud logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-cloud.png).

  8. Open the **Sign on** tab.

  9. Click **User authentication > Edit** and configure the following:

     * **Authentication policy** : set to **Okta dashboard**
  10. Click **Save**.

  11. Open the **Assignment** tab and assign one or more users. Assigned users see the Google Cloud console link in their user dashboard.

**Important:** The assignment settings of the **Bookmark app** only control visibility. To grant a user permission to use single sign-on and access Google Cloud, you must also assign them to the Google Workspace app.



Optionally, repeat the steps above for any additional Google services you want to include in user dashboards. The table below contains the URLs and logos for commonly used Google services:

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
  
## Test single sign-on

After you've completed the single sign-on configuration in both Okta and Cloud Identity or Google Workspace, you can access Google Cloud in two ways:

  * Through the list in your Okta user dashboard.
  * Directly by opening <https://console.cloud.google.com/>.



To check that the second option works as intended, run the following test:

  1. Pick an Okta user that has been provisioned to Cloud Identity or Google Workspace and that doesn't have super-admin privileges assigned. Users with super-admin privileges always have to sign in using Google credentials and are therefore not suitable for testing single sign-on.
  2. Open a new browser window and go to <https://console.cloud.google.com/>.
  3. In the Google Sign-In page that appears, enter the email address of the user and click **Next**.
  4. You are redirected to Okta and will see another sign-in prompt. Enter your email address of the user and follow the steps to authenticate.

After successful authentication, Okta should redirect you back to Google Sign-In. Because this is the first time you've signed in using this user, you're asked to accept the Google Terms of Service and privacy policy.

  5. If you agree to the terms, click **I understand**.

You are redirected to the Google Cloud console, which asks you to confirm preferences and accept the Google Cloud Terms of Service.

  6. If you agree to the terms, choose **Yes** and click **Agree and continue**.

  7. Click the avatar icon on the top left of the page, and then click **Sign out**.

You are redirected to a Okta page confirming that you have been successfully signed out.




Keep in mind that users with super-admin privileges are exempted from single sign-on, so you can still use the Admin Console to verify or change settings.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

## What's next

  * Learn more about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Acquaint yourself with our [best practices for managing super-admin accounts.](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices)



## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
