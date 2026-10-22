---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-oauth/
title: Configure your email channel for OAuth with Microsoft Office 365 \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:59.991701+00:00
---

# Configure your email channel for OAuth with Microsoft Office 365  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-oauth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure your email channel for OAuth with Microsoft Office 365 Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure a Contact Center AI Platform (CCAI Platform) email channel to support Microsoft OAuth.

**Note:** Email channel is only available for Salesforce, Zendesk, Kustomer, and Custom CRMs.

## Prerequisites

  1. An [Azure account](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F) with an active subscription. The account needs to have Microsoft Entra management access, so it must be configured as one of the following roles:

     * Application administrator
     * Application developer
     * Cloud application administrator
  2. A Microsoft Entra tenant. See the [Microsoft quickstart guide](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant) for instructions about how to create a tenant.




## Make sure the email account allows IMAP & SMTP

CCAI Platform uses IMAP and SMTP to send and receive email from Microsoft. Because a Microsoft account can be connected to different programs, it is important to ensure that IMAP or SMTP is not blocked by any other secondary programs. The following steps walk you through some common places to check in Microsoft.

  1. Go to **Users > Active** users in the left navigation panel.

  2. Select a user to verify.

  3. Click **Mail**. If you see "This user doesn't have an Exchange Online license", then you need to give the user a proper license to use Exchange. Without a proper license CCAI Platform won't be able to send or receive emails for this user account.

  4. After a proper license is added, select **Manage email apps** under the _Mail_ tab. Ensure that IMAP and Authenticated SMTP are checked.

  5. Click **Save**.

  6. Go to **Mailboxes** on the left navigation panel.

  7. Select the user account you want to check.

  8. Under the **General** tab, select **Manage email apps settings**. Ensure that the IMAP toggle is enabled.




## Register an application

  1. Sign in to the Microsoft Entra administrator center. If you have multiple tenants, use the _Directories + Subscriptions_ filter to switch to the correct tenant.

  2. Go to **Identity > Applications > App registrations > New registration**.

  3. Enter an identifiable display Name. Multiple app registrations can share the same name. The client ID is what the program uses to identify the app. However, because users of the program can see the name you've created, it might expedite registration to giving it a unique name.

  4. Specify the account type that can use the application, or sign-in audience. Several account types are supported:

     1. _Accounts in this organizational directory only_ : Select this option if you're building an application for use only by users (or guests) in a single tenant. This is sometimes referred to as a line of business (LOB) application.

     2. _Accounts in any organizational directory_ : Select this option if you want users in any tenant to be able to use this application. This option is preferable for multi-tenant configurations.

     3. _Accounts in any organizational directory and personal Microsoft accounts_ : Select this option if you want users in any tenant to be able to use this application, as well as users who have personal Microsoft accounts.

     4. _Personal Microsoft accounts_ : Select this option if you only want to create an application for users who have personal Microsoft accounts. Includes Microsoft, Skype, Xbox, Live, and Hotmail accounts.

  5. For **Redirect URI** , select **Web** and enter `https://{tenant}.ccaiplatform.com/v1/email_accounts/oauth_callback`. Replace `{tenant}`` with your CCAI Platform tenant name.

  6. Click **Register** to complete the initial app registration.

  7. After registration is complete, you will see the _Overview_ screen. Note the following information, which you will need when you complete the process in CCAI Platform:

     * Application (client) ID
     * Directory (tenant) ID



## Enable the application

  1. Sign in to the Microsoft Entra administrator center.

  2. Go to **Identity > Applications > Enterprise Applications** and select the app.

  3. Go to **Properties**.

  4. Toggle _Visible to users?_ to **Yes**.




## Add application credentials

Create a client secret for use on the CCAI Platform platform.

  1. Sign in to the Microsoft Entra administrator center.

  2. Go to **Identity > Applications > App registrations** and select the app.

  3. Go to **Certificates & secrets > Client secrets > New client secret**. This will open a panel for you to name the secret.

  4. Add a description for the client secret.

  5. Select an expiration date for the secret, or specify a custom lifetime. Client secret lifetime is limited to two years (24 months) or less, however Microsoft recommends setting an expiration value of less than 12 months.

  6. Click **Add**. Make a note of the secret's value. You will need it to complete the process in CCAI Platform.




## Add API permissions

The Graph API enables access tokens to work with IMAP, required for the CCAI Platform email channel's operation.

  1. Sign in to the Microsoft Entra administrator center.

  2. Go to **Identity > Applications > App registrations** and select the app.

  3. Select **API permissions > Add a permission**.

  4. Select **Microsoft Graph**.

  5. Select **Delegated permissions**. Use the **Select permissions** search bar to perform the following searches and check the boxes next to proper results:

     * IMAP: Check `IMAP.AccessAsUser.All`
     * `offline`: Check `offline_access`
     * `openid`: Check `openid`
     * `smtp`: `SMTP.Send`
  6. Click `Add permissions`.




## Add credentials to CCAI Platform

After the Microsoft setup is complete, use the information from the setup process to complete the connection between the two programs in CCAI Platform. Go to **Settings > Email Account Management > Email SO** and enter the following information:

_Access Type_ : leave empty.

_Authorization URL_ : `https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize`. `{tenant_id}` is the Directory (tenant) ID from the Microsoft app.

_Token URL_ : `https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token`. `{tenant_id}` is the Directory (tenant) ID from the Microsoft app.

_Client ID_ : The Application (client) ID from the Microsoft app.

_Client Secret_ : The Client Secret value from the Microsoft app.

_Scope_ : Enter the following values. They don't need to be comma-separated but they must all be present.

  * `openid email offline_access`
  * `https://outlook.office.com/IMAP.AccessAsUser.All`
  * `https://outlook.office.com/SMTP.Send`



_State_ : leave empty.

_Access Type_ : leave empty.

_Grant Type_ : Authorization Code

Clear "Include the Grant Type as part of the Authorization URL and Token URL."

Check "Include the Redirect URL as part of the Authorization URL and Token URL."

Click **Save**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
