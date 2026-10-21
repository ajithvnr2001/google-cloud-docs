---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk-installation-guide/
title: Zendesk CRM installation guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:49.974517+00:00
---

# Zendesk CRM installation guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk-installation-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Zendesk CRM installation guide Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) supports integration with Zendesk CRM. This guide covers the steps needed to perform this integration. The following Zendesk applications are supported:

  * **Call** : Latest version: v1.4.0

  * **Chat** : Latest version: v1.3.0




## Before you start

The following are prerequisites for the Zendesk CRM integration:

  * Sign in to CCAI Platform portal as an administrator.

  * Zendesk account on the Professional or Enterprise plan.

  * Download Zendesk app files.

  * Read through instructions before installing.




## Installation

Zendesk apps are private. They are not listed on the public Zendesk App Marketplace. You can contact your Zendesk representative to obtain and install them to your Zendesk account.

The Zendesk apps can be installed either by following these instructions or by clicking on the link in the Zendesk apps. To upload and install a private app in Zendesk support:

  1. Sign in to Zendesk and click the **Admin** icon settings in the sidebar.

  2. Select **Apps** > **Manage**.

  3. Click **Upload App**.

  4. Enter a name for the app. It is recommended that you use **Call** for the call app and **Chat** for the chat app.

  5. Click **Choose file** and select the zip file for your private app.

     * For call app, the filename is **zendesk-call-v1.4.zip**.

     * For chat app, the filename is **zendesk-chat-v1.3.zip**.

  6. Click **Upload**.

  7. In the window that appears, click **Agree and upload this App**.

  8. Enter your account subdomain.

  9. Enable role or group restrictions, enter role or group if needed.

  10. When prompted, click **Install**.




When the process is complete, your private app appears in the list of installed apps on the **Manage Apps** page.

Repeat steps if both the call and chat apps need to be installed.

![Zendesk app install](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e00bf1d20d8.png)

![Zendesk app install](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e00bf1d8829.png)

  1. For the app configuration, specify the following field values:

     * **Subdomain** : Enter the subdomain of your Zendesk account, which you should already know. (customer ie. **customer**.example.com)

\-- **Domain Name** : Leave it as the default value **example.com**.




## Managing apps

Once the chat and call applications have been installed they can be managed through Zendesk.

### Changing app settings

The application settings can be changed by following these instructions. You can change the settings for an app, including the title.

  1. Sign in to Zendesk and click the **Admin** icon settings in the sidebar.

  2. Select **Apps** > **Manage**.

  3. On the **My Apps** page, find the app you want to change.

  4. Click the app icon to open that app's settings page.

  5. Make the changes you want and click **Save Settings** at the bottom of the page. Your changes are saved.




### Updating apps

Periodically it might be necessary to update the installed apps. To update an app, follow these instructions:

You can find instructions to update a private app or click the following link from Zendesk, Private Apps.

  1. Sign in to Zendesk and click the **Admin** icon settings in the sidebar.

  2. Select **Apps** > **Manage**.

  3. On the **My Apps** page, find the app you want to update.

  4. On the app icon, click the settings icon to open the app settings menu. 

  5. Click **Update** to open the screen where you can upload an updated zip file.




## Setting up an OAuth client

Zendesk apps use OAuth2 to authenticate API requests to Zendesk. You should set up an OAuth Client for Zendesk Apps.

The following instructions guide you through the OAuth setup process including registering your application with Zendesk.

### Application registration

  1. In Zendesk Support, click **Manage** settings.

  2. Select **API** in the Channels category.

  3. Click the **OAuth Clients** tab on the Channels / API page.

  4. Click the add icon on the right side of the client list.

  5. Complete the following fields to create a client:

     * **Client Name** : Enter a name for your app. This is the name that users will see when asked to grant access to your application, and when they check the list of third-party apps that have access to their Zendesk.

     * **Description** : (Optional) This is a short description of your app that users will see when asked to grant access to it.

     * **Company** : (Optional) This is the company name that users will see when asked to grant access to your application. The information can help them understand who they're granting access to.

     * **Logo** : (Optional) This is the logo that users will see when asked to grant access to your application. The image can be a JPG, GIF, or PNG. For best results, upload a square image. It will be resized for the authorization page.

     * **Unique Identifier** : The field is auto-populated with a reformatted version of the name you entered for your app. You can change it if you want.

     * **Redirect URLs** : Enter the URL or URLs that Zendesk should use to send the user's decision to grant access to your application. The URLs must be absolute and not relative, https (unless localhost or 127.0.0.1), and newline-separated.

  6. Click **Save**.

After the page refreshes, a new pre-populated **Secret** field appears on the lower side. This is the `client_secret` value specified in the OAuth2 spec.

  7. Copy the **Secret** value to your clipboard and save it somewhere safe.

**Note:** The characters may extend past the width of the field, so make sure to select everything before copying.
  8. Set the OAuth redirect URL. 

`https://YOUR_SUBDOMAIN.example.com/v1/zendesk/oauth_callback`

You should replace YOUR_SUBDOMAIN with the actual subdomain of your Zendesk account.

  9. Set the **Unique Identifier** and **Secret** fields which are are auto-populated while adding a new OAuth client. You can edit the **Unique Identifier** if you want, but not the **Secret**. The **Secret** is displayed fully only once while adding a new client. Ensure this is kept safe. These are the **client_id** and **client_secret** values in the OAuth2 specifications.




### Configure OAuth application settings

  1. Sign in to the CCAI Platform portal.

  2. Go to **Settings** > **Developer Settings**.

  3. Select Agent Platform **Zendesk** in **CRM** section.

  4. Set **Zendesk Subdomain** to the subdomain of your Zendesk account.

  5. Set **OAuth Client ID** to the **Unique Identifier** of your Zendesk OAuth client.

  6. Set **OAuth Client Secret** to the **Secret** of your Zendesk OAuth client.

  7. Click **Save**.




## Generate an API token

The Zendesk API leverages tokens for security. To generate an API token in Zendesk, follow these steps:

  1. In Zendesk, click the **Admin** settings icon in the sidebar.

  2. Select **Channels** > **API**.

  3. Click the **Settings** tab, and make sure Token Access is **enabled**.

  4. Click the add icon to the right of **Active API Tokens**.

  5. Optionally, enter a description under **API Token Description**.

  6. The token is generated and displayed for you:

![Token display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e00bf207f40.png)

  7. Copy the token, and paste it somewhere secure. Once you close this window, the full token will never be displayed again.

  8. Click **Save** to return to the API page.

  9. A truncated version of the token is displayed:

![Truncated token display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e00bf20d67e.png)




## Configure API token

To assign the API token to the Zendesk CRM settings, follow these steps:

  1. Sign in to the CCAI Platform portal with an administrator account.

  2. Go to **Settings** > **Developer Settings**.

  3. Set **API Token** to the **API token** copied from your Zendesk client.




### Create customer and ticket fields

Optionally, the customer and ticket fields can be created. Follow these steps:

  1. Create a Zendesk account which has both administrator and agent role.

  2. In Zendesk, go to **Settings** > **Agent & Manager Team**.

  3. Select **Add an admin**.

  4. Check **This admin is also an agent**.

  5. Activate the account from invitation email.

  6. Sign out of the current administrator account and sign in with the new account.

  7. Sign in to Zendesk with administration role not agent.

  8. In Zendesk, sign in using the widget with credential which is an administrator with agent role.

  9. Click **Authorize**.

  10. Open the CCAI Platform portal, go to **Settings** > **Developer Settings**.

  11. Click the **Create** button from **CRM** > **Customer fields for Contact and Ticket** section.

  12. Check if the custom ticket fields were created from Zendesk **Admin** > **Manage** > **User Fields and Admin** > **Manage** > **Ticket Fields**.

These should include the fields:

     * **User fields** :

     * Identifier

     * **Ticket fields** :

     * Verification (Checkbox)

     * Customer Text Feedback (Multi-line text)

     * Customer Satisfaction Rating (Numeric): 1 to 5

     * Shared Customer Rating (Text): Twitter or Facebook




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
