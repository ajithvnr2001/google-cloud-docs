---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-oauth-profiles-ms/
title: Email OAuth profiles and Microsoft 365 client credentials \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:19.256726+00:00
---

# Email OAuth profiles and Microsoft 365 client credentials  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-oauth-profiles-ms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Email OAuth profiles and Microsoft 365 client credentials Stay organized with collections  Save and categorize content based on your preferences. 

Email OAuth profiles let you manage OAuth settings for email accounts in Contact Center AI Platform (CCAI Platform). Instead of using a single global OAuth configuration for all OAuth IMAP accounts, you can create separate email OAuth profiles and link each email account to the profile it should use.

For Microsoft 365, email OAuth profiles support the client credentials grant type. This grant type authenticates at the application level instead of relying on an individual user sign-in. It is especially useful for shared mailboxes, such as `support@company.com`, because access doesn't depend on one admin user's password, consent session, or employment status.

This page shows you how to set up email OAuth profiles for Microsoft 365, using client credentials.

## Authorization code versus client credentials

CCAI Platform supports the authorization code and client credentials OAuth grant types for email accounts. The following table compares these grant types:

Grant type | Best for | How it works  
---|---|---  
Authorization code | User-specific mailboxes | An administrator or mailbox user signs in through the Microsoft OAuth consent flow.  
Client credentials | Shared or application-managed Microsoft 365 mailboxes | CCAI Platform uses an app registration, client secret, and instance-level permissions to request access without an interactive user sign-in.  
  
Each email OAuth profile uses one grant type. If your organization needs different grant types, providers, or mailbox configurations, create separate email OAuth profiles and link each email account to the appropriate profile.

**Note:** Gmail doesn't support the client credentials grant type. Gmail accounts must use the authorization code grant type.

## Before you begin

Make sure you have the following:

  * A Microsoft 365 instance.

  * Microsoft Entra administrator access.

  * A CCAI Platform administrator account with permission to manage email settings.

  * PowerShell installed locally.

  * The `ExchangeOnlineManagement` PowerShell module installed.

  * The Microsoft instance ID for your directory.




You also need to know which mailbox or mailboxes CCAI Platform should access.

## Create a Microsoft Entra app registration

CCAI Platform uses the Microsoft Entra app registration to request OAuth tokens for Microsoft 365 email access.

To create a Microsoft Entra app registration, follow these steps:

  1. In Microsoft Azure, go to **Microsoft Entra ID > App registrations**.

  2. Select **New registration**.

  3. Enter a clear name for the app, such as CCAI Platform Email OAuth.

  4. Complete the registration.

  5. Copy the **Application (client) ID**.

  6. Copy the **Directory (tenant) ID**.




Use these values when you create an email OAuth profile.

## Create a client secret

To create a client secret, follow these steps:

  1. In the app registration, go to **Certificates & secrets**.

  2. Create a new client secret.

  3. Copy the secret value immediately.


**Note:** Microsoft only shows the client secret value once. Store it securely before leaving the page.

## Add Microsoft API permissions

The app needs permission to access and send email through Exchange Online.

To add Microsoft API permissions, follow these steps:

  1. In the app registration, go to **API permissions**.

  2. Select **Add a permission**.

  3. Select **Office 365 Exchange Online**.

  4. Choose **Application permissions**.

  5. Add the required permissions:

     * `IMAP.AccessAsApp`

     * `SMTP.SendAsApp`

  6. If you want CCAI Platform to show available Microsoft 365 mailboxes in a drop-down, add the Microsoft Graph application permissions required to list users or mailboxes for your instance.

  7. Select **Grant admin consent for your organization**.




Confirm that the permissions show as granted before continuing.

**Note:** The exact Microsoft Graph permission required for mailbox discovery depends on your Microsoft instance configuration. If the mailbox drop-down doesn't load, confirm with your Microsoft administrator that the app can list the mailboxes CCAI Platform should display.

## Grant the app access to the mailbox

After the app has instance-level permissions, grant it access to the specific mailbox that CCAI Platform should connect to.

To grant the app access to the mailbox, follow these steps:

  1. Open PowerShell.

  2. Connect to Exchange Online:
         
         Connect-ExchangeOnline -Organization TENANT_ID
         

Replace `TENANT_ID` with your Microsoft 365 Directory (tenant) ID.

  3. Register the service principal in Exchange:
         
         New-ServicePrincipal `
             -AppId APPLICATION_CLIENT_ID `
             -ObjectId OBJECT_ID
         

Replace the following:

     * `APPLICATION_CLIENT_ID`: the Application (client) ID from your Microsoft Entra app registration

     * `OBJECT_ID`: the object ID from **Enterprise applications**

  4. Grant mailbox access:
         
         Add-MailboxPermission `
             -Identity EMAIL_ADDRESS `
             -User SERVICE_PRINCIPAL_ID `
             -AccessRights FullAccess
         

Replace the following:

     * `EMAIL_ADDRESS`: the email address of the mailbox that CCAI Platform should access

     * `SERVICE_PRINCIPAL_ID`: the service principal ID

**Note:** To get the service principal ID (or view registered service principals), run `Get-ServicePrincipal | fl` in PowerShell.



## Create an email OAuth profile in CCAI Platform

To create an email OAuth profile for the Microsoft 365 client credentials configuration, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Email Account Management** pane, and then click **Manage Email Account**. The **Email Account Management** page appears.

  3. Click the **Email OAuth** tab.

  4. Click **Add Profile**.

  5. In the **Name** field, enter a profile name.

  6. In the **Grant Type** list, select **Client Credentials**.

  7. In the **Token URL** field, enter the Microsoft OAuth token endpoint for your instance.

  8. In the **Client ID** field, enter the Application (client) ID from Microsoft Entra.

  9. In the **Client secret** field, enter the client secret value from Microsoft Entra.

  10. In the **Audience** field, enter the audience.

  11. In the **Scope** field, enter the scope.

  12. In the **State** field, enter the state.

  13. In the **Access Type** field, enter the access type.

  14. Click **Save**.




## Link an email account to the OAuth profile

To link an email account to the OAuth profile, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Email Account Management** pane, and then click **Manage Email Account**. The **Email Account Management** page appears.

  3. Click the **Email account list** tab.

  4. For the email account that you want to edit, click more_horiz, and then click **Edit email account**.

  5. In the **Email service** list, select **OAuth IMAP**.

  6. In the **OAuth Profile** list, select the OAuth profile that you created in the previous procedure.

  7. Click **Link**.

  8. In the **Email ID** list, select your mailbox.

  9. Click **Save**.




Linking confirms that CCAI Platform can authenticate with the selected OAuth profile. The mailbox selection tells CCAI Platform which mailbox the email account should use.

If CCAI Platform can't fetch the mailbox list from Microsoft, the form falls back to manual email address entry. Enter the mailbox address manually, then save the account.

## Troubleshooting

Issue | Resolution  
---|---  
The mailbox list doesn't load | Confirm that the Microsoft app has the required Microsoft Graph permissions and administrator consent. You can manually enter the mailbox if the drop-down is unavailable.  
Linking fails with an authentication error | Confirm the client ID, client secret, instance ID, and token URL are correct. Also confirm the client secret hasn't expired.  
The mailbox can't send or receive email | Confirm that the app has mailbox permissions in Exchange Online and that the email account is linked to the correct email OAuth profile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
