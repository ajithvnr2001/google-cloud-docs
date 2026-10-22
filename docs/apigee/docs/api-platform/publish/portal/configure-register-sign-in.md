---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in/
title: Configuring the user account creation and sign-in experience \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:53.599034+00:00
---

# Configuring the user account creation and sign-in experience  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring the user account creation and sign-in experience Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Configure the creation and sign-in experience for user accounts, as described in the following sections.

## Exploring the Account creation & sign in section

To configure the creation and sign-in experience for user accounts:

  1. Open the Portals page.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.  
  
[Go to Portals](https://console.cloud.google.com/apigee/portals)  


  2. Click the row of the portal that you want to configure.

  3. Click **Accounts**.

  4. Click the **Authentication** tab.




The Authentication details page displays. The Account creation & sign in section lets you:

  * Manage company information that appears on the registration and sign-in pages, including the company logo, name, and copyright information
  * Add custom registration fields to the account creation page for user credential authentication
  * Configure notifications for new user account registration and identify a portal administrator
  * Configure manual activation of user accounts



## Managing company information

Manage the company logo, name, and copyright information that appear on the portal registration and Sign In pages.

To manage company information:

  1. Access the Authentication page.
  2. Open the editor. Click edit **Edit**.
  3. Select a logo. 
     1. Click **Browse**.
     2. Navigate to the new logo, and then click **Open**.
  4. Edit the **Company name** and **Copyright** fields, as required.
  5. Click **Save**.



## Add custom registration fields to the account creation page

**Note:** This section applies to the [built-in identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#built-in).

By default, when registering with your portal, a portal user is prompted for their first and last name, an email, and a password. You can add up to three additional custom registration fields to the Create Account form to capture additional details. For example, you might want to capture the company name.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/custom-account-fields.png)

When a portal user provides data for a custom registration field, the content is displayed in the Users details. If you disable or remove a custom registration field, the custom information moves to the Legacy Data column in the Users list. See [Managing users](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users). 

> **Note** : The custom registration fields are accessible only from the [Users page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users) in the UI.

To add custom registration fields to the account creation page:

  1. Access the Authentication page.
  2. Open the editor. Click edit **Edit**.

  3. Edit one or more of the custom field labels. To remove a custom registration field, delete the field label.

  4. Select **Required** to require that the field be completed during registration.

  5. Click **Save**.




## Configuring notifications for new user account registration

> **Note** : This section applies to the [built-in identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#built-in).
> 
> See also [Configuring email notifications](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configuring_email_notifications).

To enable notifications for new user account registration:

  1. Access the Authentication page.
  2. Open the editor. Click edit **Edit**.

  3. Select **Notify portal administrator when a new portal user signs up**. The Portal administrator email field displays.

  4. Enter an email to receive a notification about the new user account registration in the **Portal administrator email** field.

**Note:** Specify an email distribution list if you want to notify multiple approvers.
  5. Click **Save**.




## Configuring manual activation of user accounts

**Note:** This section applies to the [built-in identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#built-in).

By default, when portal users register on the integrated portal, their user accounts are activated automatically.

Alternatively, you can configure your portal to require manual activation by an administrator for each new user account, as described in [Activating user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#activating_user_accounts). In this case, the status for the user account is listed as **Inactive** in the [user accounts list](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#explore-ui) and the portal user cannot sign in.

To configure manual activation of user accounts:

  1. Access the Authentication page.
  2. Open the editor. Click edit **Edit**.

  3. Select **Require approval for all new user accounts** to require manual activation of user accounts. To disable this feature, clear the option.

  4. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
