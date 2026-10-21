---
url: https://docs.cloud.google.com/looker/docs/2610/user-account/
title: Personalizing user account settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:33:34.638946+00:00
---

# Personalizing user account settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2610/user-account/

You are viewing documentation for Looker 26.10. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2610/intro)



Send feedback 

#  Personalizing user account settings Stay organized with collections  Save and categorize content based on your preferences. 

The **Account** page lets you configure some of your Looker user account settings. To access this page, select the **Profile** menu and then select **Account**.

This documentation page includes the following sections:

  * Changing standard account settings
  * Changing your email subscription settings
  * Managing your API keys
  * Configuring OAuth connection credentials
  * Configuring integrations with third-party services

  * Changing custom user settings

  * Saving changes




## Changing standard account settings

The top section of the **Account** page shows your Looker account's settings:

![](https://docs.cloud.google.com/static/looker/docs/images/browse-account-page-profile-514-v2.png)

  * **Profile Picture** : If your Looker admin has [enabled](https://docs.cloud.google.com/looker/docs/2610/admin-panel-general-settings#use_gravatar) it, you can use the [Gravatar](http://en.gravatar.com/) app to select or create an avatar for your account.
  * **First Name** : First name that is configured on the account.
  * **Last Name** : Last name that is configured on the account.
  * **Email** : Email address that is associated with the Looker account (this field is not editable).
  * **Password** : Password that is associated with the account. Select the **Change Password** button to set a new password. If your Looker instance has enabled password expiration after a set timeframe, 14 days before your password is set to expire a banner appears within the instance to alert you that you need to reset your password. If you are logged out of Looker and your password expires, you will be guided to reset your password before you log back in to the instance. When resetting your password, you can't reuse your most recent password.
  * **Time Zone** : Default time zone to be used for queries for this user.
  * **Development Mode** : The user's [Git branch](https://docs.cloud.google.com/looker/docs/2610/version-control-and-deploying-changes) for LookML development. This field defaults to the branch created when the user account was created, but you can select other branches.
  * **Text Editor Mode** : The style of text editor for the [LookML IDE](https://docs.cloud.google.com/looker/docs/2610/looker-ide). You can choose from Looker's default text editor style, a [Vim](http://www.vim.org/) text editor, or an [Emacs](https://www.gnu.org/software/emacs/) text editor.
  * **Subscription Settings:** The types of Looker emails that the user will receive, as described in the Changing your email subscription settings section.



## Changing your email subscription settings

You can manage your Looker email subscription settings. Choose whether you want to receive product and event announcements, tips and tricks, and other types of information.

You can view and update these settings in Looker's **Preference Center**. From the **Profile** section of your Looker **Account** page, select **Manage your email subscription settings** to open the preference center.

Follow these steps to update your preferences for Looker email subscriptions:

  1. In **Preferences for** , Looker fills in the email address from your account settings. If you would prefer a different email address, contact your Looker admin.
  2. In **Content** , select checkboxes for the types of emails you want to receive from Looker.
  3. If you want to suspend delivery of Looker emails for three months, or if you want to unsubscribe from all Looker emails, select the corresponding checkbox in **Settings**.
  4. Once you have selected your subscription settings, select **Update Preferences**.



When you select the **Update Preferences** button, Looker saves your email subscription preferences and sends you an email confirming your changes. You can return to this page to update your settings anytime by clicking the **Manage your email subscription settings** link on the **Account** page.

## Managing API keys

If your Looker admin has [enabled API keys for you](https://docs.cloud.google.com/looker/docs/2610/admin-panel-users-users#api_keys), you'll see the **Manage** button in the **API Keys** section. The **Manage** button opens the **API Keys** page, which lets you view, create, and delete your personal API keys. While Looker admins can see the client ID portion of your API keys, they cannot see the client secret portion, and they can't manage your API keys for you.

An API key is used to access the [Looker API](https://docs.cloud.google.com/looker/docs/2610/api-getting-started). API keys are created by Looker and consist of a client ID and a client secret. Looker requires an API key to execute commands with the Looker API.

Each row in the **API Keys** page represents one API key and shows the following attributes for that API key:

  * The client ID
  * The client secret, which you can view by clicking the **Show secret** icon
  * The date and time that the API key was created
  * An optional descriptive purpose for the API key, which you can edit by clicking in the **Purpose** field or by clicking the **Edit Purpose** icon
  * An option to delete the API key by clicking the **Delete** icon and then confirming the deletion



Click the **Create New API Key** button to add a new API key in a new row on the **API Keys** page.

Click the **Use API Explorer** button to open the [API Explorer](https://docs.cloud.google.com/looker/docs/2610/api-explorer), where you can view and run the [Looker API methods and types](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest).

## Configuring OAuth connection credentials

If your Looker instance has database connections that use OAuth, such as [Snowflake](https://docs.cloud.google.com/looker/docs/2610/db-config-snowflake#oauth) or [Google BigQuery](https://docs.cloud.google.com/looker/docs/2610/db-config-google-bigquery#oauth_for_bigquery_connections), Looker displays a section for **OAuth Connection Credentials**.

Select **Log In** to enter your OAuth credentials through an OAuth interface. If you have already logged in, Looker instead displays the options **Reauthorize** and **Log Out**.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-snowflake-loggedin-624.png)

Select **Reauthorize** to open the OAuth login page, or select **Log Out** to log your Looker user account out of the OAuth session.

See the [Snowflake](https://docs.cloud.google.com/looker/docs/2610/db-config-snowflake#oauth) and [Google BigQuery](https://docs.cloud.google.com/looker/docs/2610/db-config-google-bigquery#oauth_for_bigquery_connections) documentation pages for more information.

## Configuring integrations

If your Looker admin has integrated Slack into your instance by using the [Slack App](https://docs.cloud.google.com/looker/docs/2610/scheduling-slack) service, you must perform a one-time authentication for each Slack workspace before you can access it.

The Slack workspaces that require your authentication are listed in the **Integrations** section of your user **Account** page. Select **Sign in with Slack** to authenticate to a workspace.

If no Slack workspaces require your authentication, Looker displays a note in the **Integrations** section:
    
    
    There are no installed integrations. Contact your admin to install an integration.
    

Once you have successfully authenticated, Looker displays the name of the Slack workspace along with options to revoke authentication.

## Changing custom user settings

Your Looker admin can [set up additional user attributes](https://docs.cloud.google.com/looker/docs/2610/admin-panel-users-user-attributes) that help with customizing your experience in Looker. The **Additional Details** section displays the values of the user attributes that are configured for your Looker account. It shows a list of all user attributes, with each followed by its assigned value. If your Looker admin has set any of the user attributes to `hidden`, Looker won't display that value. Instead, the value will be indicated by a series of asterisks.

The **Custom Value** column indicates if the user attribute value is a custom value. A custom value is a value that is assigned to your user account individually, instead of a value that your account inherited from a [group](https://docs.cloud.google.com/looker/docs/2610/admin-panel-users-groups). If the **Custom Value** switch next to a user attribute is turned on, that user attribute has a custom value.

You may be able to edit some user attributes, depending on how your Looker admin has configured your account. To do so, turn on the **Custom Value** switch next to a user attribute, enter the value you want, and select **Save**.

## Saving changes

After making changes to any of the options on this page, select the **Save** button to save your changes.

**Note:** When you create an account or your organization's administrator creates an account to use the Platform on your behalf, additional information about your use is created, which may collect and use the following information:

  * License credentials to ensure that usage is in compliance with the customer's licensing terms. This information includes metadata about users, roles, database connections, server settings, features used, API usage, and Platform version. Information contained in your organization's Looker database used with the Platform, to which Looker have access when we automatically back it up and encrypt it.
  * Device information, which may include the hardware model, operating system and version, unique device identifiers, network information, IP address, and/or Platform version.
  * Logins that use external directory or single sign-on services share certain information with Google that we use to authenticate your identity and pre-populate certain forms (for example, user registration) on the Platform. Note that even if a user subsequently stops using the services, Google will retain the information that the user has shared with us.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
