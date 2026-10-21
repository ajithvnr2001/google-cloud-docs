---
url: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google/
title: Admin settings - Google authentication \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:18:28.650560+00:00
---

# Admin settings - Google authentication  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Google authentication Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Setting up Google authentication in [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) is covered on the [Create an OAuth client and credentials for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) and the [Use Google OAuth for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) documentation pages.

The **Google Authentication** page in the **Authentication** section of the **Admin** menu lets you set up Google OAuth on the Looker side.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Feature overview

Looker can perform authentication using [Google OAuth](https://developers.google.com/identity/protocols/OAuth2) for users that have accounts registered with Google Google Workspace.

  * Organizations using Google Google Workspace can authenticate Looker users who have Google Accounts.
  * Users sign in to Looker by authenticating with their Google Account.
  * New Google Accounts automatically get access to Looker. No need to separately invite users to Looker. You set the default role for new users, which can limit their access to functionality and data.
  * When enabled, Looker authenticates users _only_ with Google OAuth _unless_ the "alternate login" option is selected (see the following section on Enabling email logins while Google Auth is enabled).
  * A user's Google avatar appears in the navigation bar instead of the standard user symbol.

**Warning:** The following behaviors might affect your decision to use Google OAuth:

  * When enabling Google OAuth, the Looker instance can merge existing user accounts with the Google-registered domain, but only for accounts whose email address matches the domain. All other non-admin accounts will lose the ability to sign in.
  * All users in the specified domain get access to the Looker instance.
  * Permissions for new Google users defaults to basic access for a specified list of models (which could, optionally, be access to zero models). Permissions can be updated by an admin after account creation.
  * New Looker accounts that authenticate using Google OAuth cannot switch to password authentication, even if OAuth is disabled for the Looker instance.



## Preliminary requirements

Using Google OAuth requires the following:

  * A [Google Workspace](https://workspace.google.com/) account for the organization.
  * A domain controlled by the organization and registered to the Google Google Workspace account.
  * Users with email addresses in the domain associated with the Google Account.
  * Each user must have a [managed user account](https://support.google.com/a/answer/11112794?ref_topic=7042002) in Google Google Workspace. To find and migrate any users with unmanaged user accounts, use the [Transfer tool for unmanaged users](https://support.google.com/a/answer/6178640).



## Enabling authentication with Google OAuth

Enabling authentication with Google OAuth requires an administrator to perform steps both on the Google side, and on the Looker side, as described in the following sections.

### Setup on the Google side

The steps for enabling Google OAuth on the Google side are described in this section. The generic description of these steps is on the Google support page on [setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849). You can also refer to [Google Cloud console Help](https://developers.google.com/console/help/) documentation.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. Click the down arrow in the **Select a project** drop-down. You may see the name of an existing project in the drop-down; click the down arrow regardless, and it will take you to the option to create a new project.

  3. In the **Select a project** page, click **New Project**.

The Google Cloud console displays the **New Project** page.

  4. Fill out the information on the **New Project** page and click **Create**.

When the Google Cloud console is done creating your new project, Google returns you to the Google Cloud console and shows your new project.

  5. In the left menu, select **APIs & Services > Credentials**.

  6. On the **Credentials** page, click the **Create credentials** button, and select **OAuth client ID** from the drop-down menu.

The Google Cloud console displays the **Create OAuth client ID** page.

  7. The Google Cloud console requires that you configure an [OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent), which lets your users choose how to grant access to their private data and provides a link to your organization's terms of service and privacy policy. Click **Configure consent screen**. (If you have configured OAuth consent for a previous project, you won't see this option, and you can skip to step 13.)

The Google Cloud console displays the **OAuth consent screen** page.

  8. Enter the domain of your Looker instance in the **Authorized domains** field. For example, if Looker hosts your instance at `https://mycompany.looker.com`, the domain is `looker.com`. For customer-hosted Looker deployments, enter the domain on which you host Looker.

  9. Configure your OAuth consent screen and click **Save and Continue**.

**Note:** For information about configuring the Google **OAuth consent screen** , see the [Configure OAuth](https://developers.google.com/workspace/guides/configure-oauth-consent) Google Workspace page.
  10. On the **Scopes** page, click **Save and Continue**. No additional scope configuration is required.

  11. On the **Summary** page, click **Back to Dashboard**.

The Google Cloud console returns you to the **Create OAuth client ID** page.

  12. Under **Application type** , select **Web application**.

  13. In the **Name** field, enter a name for your OAuth client ID.

  14. In the **Authorized JavaScript origins** field, enter the URL to your Looker instance, including the `https://`. For example:

     * If Looker hosts your instance: `https://mycompany.looker.com`
     * If you have a customer-hosted Looker instance: `https://looker.mycompany.com`
     * If your Looker instance requires a port number: `https://looker.mycompany.com:9999`
  15. In the **Authorized redirect URIs** field, enter the URL to your Looker instance, followed by `/oauth2callback`. For example: `https://mycompany.looker.com/oauth2callback` or `https://looker.mycompany.com:9999/oauth2callback`.

  16. Click **Create**.

  17. Copy your **client ID** and your **client secret** values — you will need them to configure Looker.




### Setup on the Looker side

**Note:** Google Group mirroring is only available when using OAuth with [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview)

To enable Google OAuth on the Looker side, follow these steps.

  1. From the Looker application, while logged in as an administrator, click the **Admin** drop-down to open the **Admin** menu.

  2. Under the **Authentication** group, click **Google**. Looker displays the **Google Authentication** page.

  3. Click **Enabled** to display and edit Google OAuth settings. (This does not immediately enable Google authentication; you must confirm your choice later).

  4. Enter your **Google Auth Settings**.

     * **Client ID and Client Secret** \- Copy and paste these values from the Google **OAuth client** page, as discussed in the previous Google setup instructions.
     * **Domains** \- Your organization's Google-managed domain name(s). Any Google user in the given domain can sign in to your Looker instance. If you control multiple Google domains you can enter them separated by commas.
**Warning:** Only enter Google domains controlled by your organization. Entering any other domain could open access to users of a domain you don't control.
  5. Enter **Migration Options** , which control behavior of the Looker instance during the transition to Google OAuth.

     * **Alternate login for admins** \- Lets administrators continue logging in with email and password. This setting enables a critical fallback method to prevent a complete lockout if the Google Cloud project that's hosting the Looker OAuth client is deleted or disabled (which can result in a **401`deleted_client`** error even after project restoration), or if Google OAuth fails for other reasons. This setting is highly recommended and is described further in Enabling email logins while Google Auth is enabled.
     * **Merge by email** \- Converts any existing users with email addresses in the given **Domains** to use Google OAuth, upon their next login. This setting is recommended.
     * **Roles for new users** \- Specifies the functionality and model access that new, non-admin users have. This list can be updated later. If left blank, new Google-authenticated users will have limited functionality inside the Looker platform until an admin adds a role to their account. Since all users within your Google domain will be able to sign in to Looker, consider specifying a default role for new users that limits access appropriately.
  6. Click **Test Google Authentication** to use the current settings and attempt to authenticate the current browser in a new window. This action **does not** save the current settings or apply them to the Looker instance.

If you are not logged into Google, you are prompted to sign in and asked for consent to use your Google Account information. This flow uses the custom **Consent screen** settings you used in the Google-side setup.

Upon success, a **User Info** section displays with your name, email, and domain. Presence of this **User Info** section shows that this user would be successfully authenticated by Looker.

Upon failure, error descriptions appear. Some common issues include the following:

     * Miscopied Client ID or Client Secret. These must be carefully copied and pasted in full.
     * User is out of domain. If you see a **Person Info** section, but no **User Info** , it is probably because the user is not in the domain you specified. This shows that the person has authenticated themselves to Google correctly, but they are not using a Google Account that you have chosen to allow into your Looker instance.
     * A Looker URL or redirect URL is not set up correctly in Google for your Looker instance.
  7. To save and apply changes, check **I have confirmed the configuration above and want to enable applying it globally.** Click **Update**.


**Note:** After you enable Google authentication, users can authenticate _only_ through Google OAuth. If you did not enable the **Merge by email** setting for existing accounts, every new Google-authenticated login creates a new Looker user. Existing email and password logins are not usable at the same time that Google authentication is enabled.

## Tips

  * To experiment with the full authentication cycle, you can log out of Google and see that Google prompts you to sign in again when you attempt to sign in to Looker.

  * In Google you can click **Account** in the personal drop-down (next to your email address on the top right of a Google Google Workspace page) to manage your personal account.

On that management page there is a **Security** tab with an **Account Permissions** section. Clicking on **Apps and websites _View all_** lets you (as a user) see and manage the services and apps to which you have granted permissions.

Clicking on the Looker permissions that you granted in order to log on shows the details that users see in the consent screen that you customized previously. You can also click **Revoke access** so that the next time you sign in to Looker (or test authorization) you will be re-prompted with the consent screen. You can use this workflow to help you customize your consent screen and view what users will see.




## Troubleshooting

To help troubleshoot authentication issues, check the [User Activity dashboard in System Activity](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#user_activity_dashboard). This dashboard has tiles that display recent login failures and includes the authentication method that was used, the error message that was returned, and the time of the attempt.

  * If a user's attempt to sign in fails, first make sure the user has both a first name and a last name in their Google Accounts. If the user has deleted either their first name or their last name from their Google Account, Looker may be unable to authenticate the user with Google OAuth.

  * If a user's attempt to sign in fails, and Looker displays an error such as `User not in the authorized domain`, check the `hd` field of the JSON response. If the `hd` field contains a domain, make sure that the domain is registered to your Google Google Workspace account. If the `hd` field is empty, use the [Transfer tool for unmanaged users](https://support.google.com/a/answer/6178640) to invite the user to convert their account to a managed account within your domain.

  * If a user's attempt to sign in fails, but Looker does not display an error message, the user may have edited their Google Google Workspace account name and deleted either their first or last name. In this situation, the Google Google Workspace account name may still look complete in the Admin console, which may not show the user's edits. To prevent this issue, Google Google Workspace admins can disable the **Allow users to customize this setting** option.

  * If Google authentication returns a **401`deleted_client`** error, this error indicates that the Google Cloud project that's hosting the Looker OAuth client has been deleted or disabled. Even if the Google Cloud project is subsequently restored, the OAuth client may continue to fail with the `deleted_client` error, resulting in a complete login lockout for all users. If Google authentication is the only enabled authentication method, this lockout prevents access even for administrators.

To prevent complete lockout in the event of an OAuth client deletion or failure, you must enable the **Alternate login for admins** setting. This setting ensures that administrators have a fallback login method to access the Looker instance and update authentication settings.




## Enabling email logins while Google Auth is enabled

New Google Accounts automatically get access to Looker, so there is no need to add users that are in your Google Domain.

To add a user with an email address that is not in your Google Domain:

  1. Enable the **Alternate login for admins and specified users** option on the Google Auth page
  2. Create or modify an existing user role to add the `login_special_email` permission
  3. Go to **Add Users** from the users panel (**/admin/users/new**)
  4. Add the email address(es) you would like to include, and the roles those users should have, which must include a role with the `login_special_email` permission
  5. Those users are now able to sign in using **https://mycompany.looker.com/login/email** (hidden URL)

**Note:** If a user has authenticated into the Looker instance using only Google, you can enable alternate login only by using the Looker API. To learn how to enable alternate login using the Looker API, see the [Enabling the alternate login option](https://docs.cloud.google.com/looker/docs/alternate-login) documentation page.

## Disabling Google Auth once it has been enabled

If you'd like to disable Google Authentication for your Looker instance after it has already been enabled, there are some things to think about:

  * Users who were created _before_ Google Authentication was added, and already setup a normal email login and password, will still function.
  * Users who were created _after_ Google Authentication was added will no longer be able to sign in. While their accounts still exist, they have no way to access them, and their accounts are effectively orphaned.



This is why we suggest avoiding this route. If you must go down this path there may be a method to fix the orphaned accounts by using the Looker API. Reach out to Looker Support for additional guidance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
