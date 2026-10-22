---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact/
title: How portal users interact with your portal \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:20.063381+00:00
---

# How portal users interact with your portal  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  How portal users interact with your portal Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Out-of-the-box, the developer portal enables your portal users to create a user account, sign in, and manage the apps that will consume your APIs.

The following sections describe how portal users interact with your portal.

## Signing in to the portal

The following sections describe how portal users sign in to the integrated portal using their user credentials (built-in identity provider) or using SAML (Preview).

If you [enable both the built-in and SAML identity providers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider), then portal users will be able to choose their preferred method for signing in.

### Signing in to the portal using user credentials (built-in identity provider)

**Note:** The sign-in page cannot be edited other than to change the company logo as described in [ Configure the user account creation and sign-in experience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in).

When the [built-in identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configuring_the_built-in_identity_provider) is enabled, portal users can sign in to the integrated portal using their user credentials (username and password), as described in the following sections:

  * Create a user account on the integrated portal
  * Sign in to the integrated portal
  * Change the password



#### Creating a user account on the integrated portal

With the built-in identity provider, before portal users can use your APIs, they must create a user account on the integrated portal.

**Key point:** See also [Where app developer account information is stored](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#apidev-info-stored). 

Although it is possible to create user accounts on behalf of portal users manually using the Apigee UI, as described in [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product), this is not recommended to ensure that the user accounts on the integrated portal and the developer records on Apigee stay in sync. 

Portal users create an account on the integrated portal as follows:

  1. Navigate to the portal.
  2. Click **Sign In**.

The Sign in page displays.

  3. Click **Create account**.

The Create your account page displays.

![Create your account dialog](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/create-account.png)

**Note:** You can add custom registration fields to the account creation page, as described in [Adding custom registration fields to the account creation page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#custom-registration-fields).

  4. Complete the form.

You must enter values for all **required** fields. Passwords must be at least 8 characters and contain at least one of each of the following: number, lowercase letter, uppercase letter, and special character.

  5. Review and agree to the terms.

  6. Click **Create Account**. **Note:** If an attempt is made to create an account with an email ID that has already been registered, a message displays indicating that the account already exists, and the portal user will be encouraged to sign in instead. 

  7. Complete the CAPTCHA form and click **Verify** (if displayed).

The user account is created and a confirmation email is sent.

**Note:** You can configure the confirmation email, as described in [Configuring email notifications](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configuring_email_notifications). Apigee recommends that you configure the SMTP server used for the email notifications originating from the portal prior to launching, as described in [Configuring the SMTP server](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email#smtp).
  8. Within 10 minutes, click the link in the confirmation email to complete the registration process.

If you do not click the link within 10 minutes, you must repeat the steps in this procedure to create an account and be re-prompted.

  9. Sign in to the integrated portal (described below).




#### Signing in to the integrated portal

With the built-in identity provider, after portal users have registered on the integrated portal and are approved, they sign in using their credentials (username and password).

**Notes** : 

  * After 24 hours of inactivity, the session will expire, and the portal user will be signed out automatically and will need to sign in again.
  * If you [configured your integrated portal to require manual activation of user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#configuring_manual_activation_of_user_accounts), you need to [manually activate user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#activating_user_accounts) before portal users can sign in. At this time, portal users are given no indication that their registration must be manually activated before they can sign in. It is recommended that if you configure manual activation, you expedite the activation of new user accounts.
  * To navigate directly to the Sign in page, use the following URL:   
`https://_portal-url_ /login`



Portal users sign in as follows:

  1. Navigate to the portal.
  2. Click **Sign In**. The Sign in page displays:

![Sign in page](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/portal-signin.png)

  3. Enter the email address and password.

  4. Click **Sign In**.




#### Changing the password

With the built-in identity provider, portal users change the password as follows:

  1. Navigate to the portal.
  2. Click **Sign In**.
  3. Click **Reset Password**.
  4. Enter the email address for the account to be reset.
  5. Click **Send Reset Password Link**.

A reset password link is sent to the email.

> **Note** : To configure the SMTP server, see [Configuring the SMTP server](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email#smtp).

  6. Click the link in the confirmation email.

  7. Enter the new password and confirm it.

Passwords must be at least 8 characters and contain at least one of each of the following: number, lowercase letter, uppercase letter, and special character.

  8. Click **Create New Password**.




### Signing in to the portal using SAML authentication (Preview)

**Note:** This is the **Preview release of the SAML identity provider**. **Note:** The sign-in page cannot be edited other than to change the company logo as described in [ Configure the user account creation and sign-in experience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in).

When the [SAML identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configure_the_saml_identity_provider) is enabled, portal users sign in to the integrated portal using SAML authentication, as follows:

  1. Navigate to the portal.
  2. Click **Sign In**.
  3. Click **login with SAML**.

You are redirected to the SAML provider.

  4. If prompted, enter your credentials for your SAML identity provider.


**Note:** After 24 hours of inactivity, the session will expire, and the portal user will be signed out automatically and will need to sign in again.

## Viewing API reference documentation

Portal users can view the API reference documentation that you have published to your portal, as follows:

  1. Navigate to the portal.
  2. Click **APIs** in the top navigation bar. The APIs page is displayed. For example:  
  
![APIs page](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apis.png)

  3. Filter the list of APIs by category, title, or description, if desired, using the tools in the left pane.

  4. Click an API card to view the API reference documentation. The API reference documentation is displayed.




Portal users can learn about and try the APIs, or download the document used to render the API reference documentation. See [Publishing your APIs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis) for more information about how the API reference documentation is rendered.

## Sharing responsibility for an app using developer teams (Preview)

**Note:** You must have [ enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll).

Developer teams allow portal users to share responsibility for an app with other portal users. The following sections describe how to create and manage developer teams.

**Key point:** Developer teams are referred to simply as "teams" when browsing the developer portal.

### About the developer team roles

The following table summarizes the roles that can be assigned to developer team members:

**Note:** As a developer team member, you can remove yourself from any developer team regardless of your role unless you are a developer team owner. Role | Description  
---|---  
App Admin | 

  * Read-only privileges for developer team members and developer team details.
  * Read and write privileges for apps.

  
Owner | Full read and write privileges for developer team members, developer team details, and apps.  
Viewer | Read-only privileges for developer team members, developer team details, and apps.  
  
### Viewing the Teams page

The Teams page displays the developer teams for which you are a member.

To access the Teams page:

  1. Sign in to the portal.
  2. Select **Teams** from the user account drop-down in the portal.



The Teams page is displayed enabling you to:

  * View the developer teams for which you are a member, including the name, role, list of members, and date the team was created
  * Add a developer team 
  * Edit developer team membership and roles, remove yourself from a developer team, or delete a team by clicking the developer team row



### Adding developer teams

**Note:** Portal users can view the developer teams to which they are members on the Teams page. For the Preview release, no notifications are sent when a portal user is added to a developer team. 

To add a developer team:

  1. Sign in to the portal.
  2. Select **Teams** from the user account drop-down in the portal.
  3. Click **\+ New Team**.
  4. Enter a name and description.
  5. To add a member to the developer team, click **\+ Add another member** , enter the portal user's email address, and select a developer team role.

Repeat to add additional members.

**Note:**
     * You are added automatically as an owner of the developer team.
     * The maximum number of developer teams that a user can be a member of is **16**. 
  6. To delete a member from the developer team, click ![delete icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/delete-x-white.png) adjacent to the developer team member you wish to delete.

  7. Click **Create**.




### Editing developer team membership and roles

To edit developer team membership and roles:

  1. Sign in to the portal.
  2. Select **Teams** from the user account drop-down in the portal.
  3. Click in the row of the developer team that you want to edit and for which you are an owner.
  4. Perform one or more of the following steps:

     * Edit the name, description, and primary contact.
     * Add or remove developer team members.
     * Update developer team member roles. **Note:**
       * A developer team must have at least one owner.
       * The maximum number of developer teams that a user can be a member of is **16**.
  5. Click **Save**.




### Removing yourself from a developer team

**Note:** As a developer team member, you can remove yourself from any developer team regardless of your developer team role unless you are a developer team owner. 

To remove yourself from a developer team:

  1. Sign in to the portal.
  2. Select **Teams** from the user account drop-down in the portal.
  3. Click in the row of the developer team from which you want to remove yourself.
  4. Click **Leave Team**.



### Deleting a developer team

**Note:** When you delete a developer team, all apps owned by the developer team are deleted.

To delete a developer team:

  1. Sign in to the portal.
  2. Select **Teams** from the user account drop-down in the portal.
  3. Click in the row of the developer team that you want to delete.
  4. Click ![delete icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/delete-icon-black.png).
  5. Click **Confirm** to confirm the deletion.



## Registering apps

Register developer apps and developer team apps, as described in the following sections.

### Registering developer apps

**Key point** : After the portal user **registers a developer app** , the user account information is synced to and available on Apigee on the [Developers page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#ui). See [Where app developer account information is stored](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#apidev-info-stored). 

Portal users can register apps to use the APIs that you have [published](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis), as follows:

  1. From the portal, select **Apps** from the user account drop-down.
  2. Click **\+ New App** to create a new app.
  3. Enter a name and description for the app in the New App dialog.
  4. In the **APIs** section, **Enable** one or more APIs.

APIs in the catalog are categorized as Authenticated APIs, requiring a callback URL, or Public APIs. You must select at least one API in order to create an app.

  5. If you select an API in the Authenticated APIs section, enter a callback URL.

For more information, see [About callback URLs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#about-callback-url).

  6. Click **Save**.




### Registering developer team apps

**Note:** This step is applicable only if you have [enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll). In Preview, app ownership cannot be transferred after the app is created.

Developer team members can register apps for a developer team to use the APIs that you have published, as described below.

**Note** : A new developer team entity will be added to Apigee only **after a member registers an app for the team**. See [Where developer team information is stored (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#team-info-stored). 

To learn more about how:

  * Portal users add and manage teams, as described in Sharing responsibility for an app using developer teams (Preview).
  * API providers view and manage developer teams, as described in [Managing developer teams (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams).



To register developer team apps:

  1. Select **Teams** from the user account drop-down.
  2. Click the row of the developer team for which you want to register an app.
  3. Click **\+ New App** to create a new app.
  4. Enter a name and description for the app in the New App dialog.
  5. Select the owner of the App in the **Owner** drop-down list.

By default, the developer team is the owner of the app. If desired, select a different developer team or yourself as owner from the drop-down menu.

**Note:** In the Preview release, app ownership cannot be transferred after the app is created.
  6. In the API Catalog section, **Enable** one or more APIs.

APIs in the catalog are categorized as Authenticated APIs, requiring a callback URL, or Public APIs. You must select at least one API in order to create an app.

  7. If you select an API in the Authenticated APIs section, enter a callback URL.

For more information, see [About callback URLs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#callback-url).

  8. Click **Save**.




## Managing the APIs in an app

As an API producer, you [publish APIs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis) to enable portal users to consume your API products.

Portal users manage which APIs their apps use. The APIs are added to the app details page. For some APIs, approval is not automatic. A status of **Pending Approval** indicates an API for which access has been requested but not yet granted.

**Note:** APIs that are not published are not displayed currently; this issue will be fixed in a future release. 

If the portal user disables access to an API that is Private or Internal only, the API is removed from the app and must be re-added manually by the portal administrator, as described in [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api). 

Portal users can manage the APIs in an app from your portal, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the app in the list.
  3. In the APIs section, click **Enable** or **Disable** access, to add or remove an API from the app.
  4. For an Authenticated API, add or edit the callback URL, as required.
  5. Click **Save**.



## Viewing the API key and secret for an app

Portal users can manage the API key for an app from your portal, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the app in the list.
  3. View the API keys in the API Keys section.
  4. Confirm that the status of the API key is Active. If your API key requires approval and has not yet been approved, the status will show as **Pending Approval**.
  5. Click **Show secret** to view the secret.
  6. Position your cursor over the API key or secret and click ![delete-icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/copy-key.png) to copy it to the clipboard.

**Note:** If either the user account or app has been deactivated/revoked, the API key will not be valid until the user account or app is re-activated/re-approved. For more information, see [Activating and deactivating a developer](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#status) and [Approving or revoking an app](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api#approve-revoke-app).

## Rotating the API key for an app

A portal user can rotate an app's API key periodically or in response to a potential leak or compromise. When a portal user rotates an API key, a new API key is created with the same API entitlements as the original key. The original API key remains active while you transition it out of use. You must revoke the old API key to prevent its credentials from being accepted, as described in Revoking an API key for an app.

Portal users can rotate an API key for an app from your portal, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the app in the list.
  3. In the API Keys section, click **Add Key**.
  4. Click **Confirm** in the dialog box to confirm the operation.
  5. Optionally, revoke the old API key, as described below.



## Revoking an API key for an app

When a portal user rotates an API key, as described in the previous section, the API key remains active while you transition it out of use. You must revoke an API key to prevent its credentials from being accepted.

Portal users can revoke an API key for an app from your portal, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the name of the app.
  3. In the API Keys section, click **Revoke** in the **Actions** column associated with the API key that you want to revoke.
  4. Click **Confirm** to confirm the operation.

The Status of the key is updated to Revoked.




## Editing app details

Portal users can edit the app details, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the app in the list.
  3. Edit the Name or Description fields on the App Details tab.
  4. Managing the APIs in an app, as required.
  5. Click **Save**.



## Deleting an app

Portal users can delete an app from your portal, as follows:

  1. Select **Apps** from the user account drop-down.
  2. Click the app in the list.
  3. Click **DELETE**.
  4. Click **Confirm** to confirm the operation.



The app is deleted and removed from the Apps list.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
