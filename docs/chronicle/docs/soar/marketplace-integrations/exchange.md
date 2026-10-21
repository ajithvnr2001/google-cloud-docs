---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchange/
title: Exchange \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:05:03.764517+00:00
---

# Exchange  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Exchange

This document provides guidance on how to integrate Exchange with Google SecOps.

**Warning:** Starting in May of 2024, you will be unable to assign the `ApplicationImpersonation` role in Microsoft Exchange Online. In February of 2025, the `ApplicationImpersonation` role will be removed from Exchange Online. For details of the changes that Microsoft is making to the `ApplicationImpersonation` role, see [Retirement of RBAC Application Impersonation in Exchange Online](https://techcommunity.microsoft.com/t5/exchange-team-blog/retirement-of-rbac-application-impersonation-in-exchange-online/ba-p/4062671). If configured before May of 2024, the `ApplicationImperonation` role is functionable until February of 2025. The changes don't impact the on-premises versions of Exchange Server. We recommend that you use [Microsoft Graph Mail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail) to work with Exchange Online.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/Exchange.zip).

## Configure Exchange Online

The prerequisites and configuration steps differ depending on whether you configure the integration for the Exchange Online or Exchange Server.

  * To configure Exchange Online, proceed to the following section.

  * To configure Exchange Server, see Configure Exchange Server.




The integration for Exchange Online only supports OAuth delegated authentication with delegated tokens which requires additional configuration.

Changes made to permissions in the Azure environment can take up to 24 hours to take effect.

### Before you begin

Before you configure the Exchange Online integration, you must choose an authentication method and complete all of its configuration steps. Choose from one of the following methods:

  * Method 1: **Assign permissions to impersonate a user** : The integration acts as a single, designated user.
  * Method 2: **Delegate access** : The integration accesses multiple mailboxes directly.



### Assign permissions to impersonate a user

This method requires you to create an application in **Microsoft Entra ID** and assign it permissions to impersonate a single user.

#### Create a Microsoft Entra application

To begin the impersonation setup, you must register a new application in Microsoft Entra ID.

  1. Sign in to [Microsoft Azure](https://portal.azure.com) and go to **Microsoft Entra ID > App registrations > New registration**.
  2. Enter a name for the app and select a **Supported account type**.
  3. For the **Redirect URI** , provide the following values: 
     1. Platform: `Web`
     2. Redirect URL: `http://localhost`
  4. Click **Register**.
  5. Save the **Application (client) ID** and **Directory (tenant) ID** values.



#### Configure API permissions

You must grant your application the necessary permissions to access user data.

  1. Go to **API permissions > Add a permission**.
  2. Select **Microsoft Graph > Delegated permissions**.
  3. In the **Select permissions** section, select **EWS** and then the `Ews.AccessAsUser.All` permission.
  4. Click **Add permission > Grant admin consent**.



#### Create a client secret

You must create a client secret to use as a password for your application.

  1. Navigate to **Certificates and secrets > New client secret**.
  2. Provide a description, set an expiration, and click **Add**.
  3. Save the secret's value.



#### Assign permissions in Exchange Online:

To complete the setup, you must assign the `ApplicationImpersonation` role to the user you want to impersonate.

  1. In the [Exchange administrator center](https://admin.exchange.microsoft.com/), go to **Roles > Admin Roles** and find the role group that contains the `ApplicationImpersonation` role (such as **Discovery Management**).
  2. Add the user you're impersonating to that role group.



### Delegate Access

This method requires you to grant the service account direct permissions to a mailbox using Exchange Online PowerShell.

  1. Connect to [Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell).

  2. Use the `Add-MailboxPermission` cmdlet to assign permissions.

For example, to grant the service account full access to a specific mailbox:
         
         Add-MailboxPermission -Identity "user@contoso.com" -User "your_service_account" -AccessRights FullAccess
         

For more information, see [Role-based access control for applications in Exchange Online](https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac) for more information.




### Integrate Exchange Online with Google SecOps

For instructions about how to install and configure the integration on Google SecOps, see [Configure Integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

Integrating Exchange Online with the Google SecOps platform requires you to complete the following steps in Google SecOps:

  1. Configure the initial parameters and save them.

  2. Generate a refresh token:

     * Simulate a case in Google SecOps.

     * Run the **Get Authorization** action.

     * Run the **Generate Token** action.

  3. Input the obtained refresh token as the `Refresh Token` parameter value and save the configuration.




#### Configure initial parameters

The Exchange Online integration requires the following initial parameters:

Parameter | Description  
---|---  
`Mail Server Address` | _Required_ A mail server address (hostname or IP address) to connect to.  
`Mail address` | _Required_ A mail address to use in the integration to work with the sent and received emails in the mailbox.  
`Client ID` | _Required_ An application (client) ID of the Microsoft Entra application that is used for the integration.This is the Application (client) ID value that you saved when creating the Microsoft Entra application.  
`Client Secret` | _Required_ A client secret value of the Microsoft Entra application that is used for the integration.This is the client secret value that you saved when creating a client secret.  
`Tenant (Directory) ID` | _Required_ A directory (tenant) ID of the Microsoft Entra ID application that is used for the integration.This is the directory (tenant) ID value that you saved when creating the Microsoft Entra application.  
`Redirect URL` | _Required_ A redirect URI that is configured in the Microsoft Entra application.Keep the value default to `http://localhost`.  
  
After you have configured the parameters, click **Save**.

#### Generate a refresh token

Generating a refresh token requires you to run manual actions on an existing case. If your Google SecOps instance is new and has no existing cases, simulate one.

##### Simulate a case

To simulate a case in Google SecOps, follow these steps:

  1. In the left navigation, select **Cases**.

  2. On the Cases page, click **add > Simulate Cases**.

  3. Select any of the default cases and click **Create**. It doesn't matter what case you choose to simulate.

  4. Click **Simulate**.

If you have an environment other than default and would like to use it, select the correct environment and click **Simulate**.

  5. In the **Cases** tab, click **Refresh**. The case you have simulated appears in the case list.




##### Run the Get Authorization action

Use the Google SecOps case which you simulated to run the Get Authorization action manually.

  1. In the **Cases** tab, select your simulated case to open a Case View.

  2. Click **Manual Action**.

  3. In the Manual Action **Search** field, enter `Exchange`.

  4. In the results under the Exchange integration, select **Get Authorization**. This action returns an authorization link that is used to interactively sign in to the Microsoft Entra app.

  5. Click **Execute**.

  6. After the action is executed, navigate to the Case Wall of your simulated case. In the **Exchange_Get Authorization** action record, click **View More**. Copy the authorization link.

  7. Open a new browser window in incognito mode and paste the generated authorization URL. The Azure sign-in page opens.

  8. Sign in with the user credentials you selected for the integration. After signing in, your browser redirects you to an address with a code in the address bar.

It is expected for the browser to display an error as the app redirects you to `http://localhost`.

  9. Copy the whole URL with the access code from the address bar.




##### Run the Generate Token action

Use the Google SecOps case you've simulated to run the Generate Token action manually.

  1. In the **Cases** tab, select your simulated case to open a Case View.

  2. Click **Manual Action**.

  3. In the Manual Action **Search** field, enter `Exchange`.

  4. In the results under the Exchange integration, select **Generate Token**.

  5. In the `Authorization URL` field, paste the whole URL with the access code copied after running the **Get Authentication** action.

  6. Click **Execute**.

  7. After the action is executed, navigate to the Case Wall of your simulated case. In the **Exchange_Generate Token** action record, click **View More**.

  8. Copy the entire value of the generated refresh token.




#### Configure the Refresh Token parameter

  1. Navigate to the configuration dialog for the Exchange integration.

  2. Enter the refresh token value that you obtained when running the **Generate Token** action into the **Refresh Token** field.

  3. Click **Save**.

  4. Click **Test** to test if the configuration is correct and the integration works as expected.




You can make changes at a later stage if needed. Once configured, the instances can be used in playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Configure Exchange Server

Before integrating Exchange Server with Google SecOps, set up the basic authentication for Exchange Server.

To authenticate with the Exchange Server, use a username and a password.

### Set up basic authentication

To set up the basic authentication, complete the following steps:

  1. Verify that the Exchange Server (one of the servers in the cluster) is accessible from the Google SecOps server and meets the following requirements:

     * The Exchange Server DNS name is resolving.

     * The Exchange Server IP address is accessible.

     * Exchange Web Services (EWS) is enabled and hosted on a port accessible to the Google SecOps server.

If the Exchange Server is not accessible from the Google SecOps SOAR server, consider using a Google SecOps remote agent.

  2. Provide the integration with a username (user email account) and a password. Choose the user for the integration.

  3. For actions that use delegated or impersonated permissions, complete the following steps:

     1. Grant a delegated or impersonated access to the required mailboxes to an email account that you use in the integration.

We recommend you to configure access with impersonated permissions. For more information, see [Impersonation and EWS in Exchange](https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) in Microsoft product documentation.

     2. To access other mailboxes, assign the following Exchange roles to the user (mailbox) configured for the integration:

        * [`Discovery Management` role group](https://learn.microsoft.com/en-us/exchange/policy-and-compliance/ediscovery/assign-permissions?view=exchserver-2019) in Microsoft product documentation.

        * [`ApplicationImpersonation` role](https://learn.microsoft.com/en-us/exchange/applicationimpersonation-role-exchange-2013-help) in Microsoft product documentation.

        * [`Compliance Management` role](https://learn.microsoft.com/en-us/exchange/permissions/feature-permissions/policy-and-compliance-permissions?view=exchserver-2019) in Microsoft product documentation.

        * [`Organization Management` role](https://learn.microsoft.com/en-us/exchange/permissions/feature-permissions/policy-and-compliance-permissions?view=exchserver-2019) in Microsoft product documentation.




### Integrate Exchange Server with Google SecOps

For instructions about how to install and configure the integration on Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

#### Integration inputs

The Exchange Server integration requires the following parameters:

Parameter | Description  
---|---  
`Mail Server Address` | _Required_ A mail server address (hostname or IP address) to connect to.  
`Mail address` | _Required_ A mail address used in the integration to work with the sent and received emails in the mailbox.  
`Username` | _Required_ A username to authenticate with on the mail server, such as `exchange_onprem_test@exlab.local`.  
`Password` | _Required_ A password to authenticate with on the mail server.   
  
## Actions

The actions listed in this section fall under two categories:

  1. The common Exchange integration actions.

  2. Actions that are specific to the Exchange Block Sender and Domain functionality.




### Required permissions

For the minimal permissions that are required to run common actions, refer to the following table:

Action | Required permissions  
---|---  
Delete Mail | `ApplicationImpersonation` `Mailbox Search`  
Download Attachment | `ApplicationImpersonation`  
`Mailbox Search`  
Search Mails | `ApplicationImpersonation`  
`Mailbox Search` `MailboxSearchApplication`  
  
For the minimal permissions required to run actions from the Block Sender and Domain functionality, refer to the following table:

Action | Required permissions  
---|---  
Add Senders to Exchange-Siemplify Inbox Rule | `EDiscovery Group`  
`Author`  
Add Senders to Exchange-Siemplify Inbox Rule | `EDiscovery Group`  
`Author`  
Delete Exchange-Siemplify Inbox Rules | `EDiscovery Group`  
`Author`  
List Exchange-Siemplify Inbox Rules | `EDiscovery Group`  
`Author`  
Remove Domains from Exchange-Siemplify Inbox Rules | `EDiscovery Group`  
`Author`  
Remove Senders from Exchange-Siemplify Inbox Rules | `EDiscovery Group`  
`Author`  
  
### Delete Mail

Use the **Delete Mail** action to delete one or multiple emails that match the search criteria from a mailbox.

Deleting emails can apply to the first email that matches the search criteria or all matching emails.

For the permissions required to run this action, refer to the action permissions section of this document.

If the user is offline, the action may not delete the message from their Outlook client until the user reconnects and synchronizes their mailbox.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Delete Mail** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Optional_ A mailbox folder to search an email in.This parameter accepts a comma-separated list of folders.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Message IDs` | _Optional_ A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of message IDs to search for. If you provide the message ID, the action ignores the `Subject Filter`, `Sender Filter`, and `Recipient Filter` parameters.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition that specifies the sender of requested emails.  
`Recipient Filter` | _Optional_ A filter condition that specifies the recipient of requested emails.  
`Delete All Matching Emails` | _Optional_ If selected, the action deletes all emails that match the criteria. If not selected, the action deletes only the first matching email. Not selected by default.  
`Delete from all mailboxes` | _Optional_ If selected, the action deletes emails in all mailboxes that are accessible using the current impersonation settings.  
`How many mailboxes to process in a single batch` | _Required_ The number of mailboxes to process in a single batch (single connection to the mail server). If you selected the `Delete from all mailboxes` parameter, the action works in batches. The default value is 25.  
`Time Frame (minutes)` | _Optional_ The period in minutes to search for emails.  
  
#### Action outputs

The **Delete Mail** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Delete Mail** action can return the following output messages:

Output message | Message description  
---|---  
`NUMBER_OF_EMAILS email(s) were deleted successfully.` | Action succeeded.  
`Error deleting emails.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Mail** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Download Attachments

Use the **Download Attachments** action to download email attachments from an email to a specific path on the Google SecOps server. The action automatically replaces the backslash or space characters in the names of downloaded attachments with the underscore character.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Download Attachments** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Optional_ A mailbox folder to search an email in.This parameter accepts a comma-separated list of folders.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Download Path` | _Required_ A path on the Google SecOps server to download email attachments.  
`Message IDs` | _Optional_ A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of message IDs to search for. If you provide the message ID, the action ignores the `Subject Filter` parameter.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition that specifies the email sender to search for.  
`Only Unread` | _Optional_ If selected, the action downloads attachments only from unread emails. Not selected by default.  
`Download Attachments from EML` | _Optional_ If selected, the action downloads attachments from attached EML files. Not selected by default.  
`Download Attachments to unique path?` | _Optional_ If selected, the action downloads attachments to a unique path under the value provided in the `Download Path` parameter to avoid overwriting the previously downloaded attachments. Not selected by default.  
`Search in all mailboxes` | _Optional_ If selected, the action runs a search in all mailboxes accessible using the current impersonation settings.Not selected by default.  
`How many mailboxes to process in a single batch` | _Required_ The number of mailboxes to process in a single batch (single connection to the mail server). If you selected the `Search in all mailboxes` parameter, the action works in batches.The default value is 25.  
`Mailboxes` | _Optional_ A comma-separated list of mailboxes to run a search through.This parameter has a priority over the `Search in all mailboxes` parameter.  
  
#### Action outputs

The **Download Attachments** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Download Attachments** action:
    
    
    [
       {
           "attachment_name": "ATTACHMENT_NAME",
           "downloaded_path": "readonly" translate="no">FULL_PATH"
       },
       {
           "attachment_name": "ATTACHMENT_NAME",
           "downloaded_path": "readonly" translate="no">FULL_PATH"
       }
    ]
    

##### Output messages

The **Download Attachments** action can return the following output messages:

Output message | Message description  
---|---  
`Downloaded  NUMBER_OF_ATTACHMENTS attachments. Files: LIST_OF_LOCAL_PATHS_FOR_ATTACHMENTS ` | Action succeeded.  
`Failed to download email attachments, the error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Download Attachments** action:

Script result name | Value  
---|---  
`file_paths` | A string of comma-separated full paths to the saved attachments.  
  
### Extract EML Data

Use the **Extract EML Data** action to extract data from the email EML attachments.

This action runs on all Google SecOps entities.

#### Action inputs

The **Extract EML Data** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Optional_ Folder to fetch an email from.Default value is `Inbox`. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Message ID` | _Required_ Message ID, such as `1701cf01ba314032b2f1df43262a7723@example.com`.  
`Regex Map JSON` | _Optional_ Regular expression to select emails based on matching the email body part, for example, `{ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}`.  
  
#### Action outputs

The **Extract EML Data** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Extract EML Data** action:
    
    
    [
        {
            "count": 3,
            "files": {
                "mxtoolbox_test_case.case": "090a131a0726dea8f5b0c2205ffc9527"
            },
            "from": "Exam <user1@example.com>",
            "text": "hello eml test", "regex": {
    
            },
            "to": "Test Test <user2@example.com>",
            "html": "<html><div></div></html>",
            "date": "Wed, 12 Sep 2018 12:36:17 +0300",
            "subject": "eml test"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Extract EML Data** action:

Script result name | Value  
---|---  
`eml_data` | `EML_DATA`  
  
### Generate Token

Use the **Generate Token** action to get a refresh token for the integration configuration with OAuth authentication. Use the authorization URL that you received in the **Get Authorization** action.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Generate Token** action requires the following parameters:

Parameter | Description  
---|---  
`Authorization URL` | _Required_ Authorization URL received in the _Get Authorization_ action to request a refresh token.  
  
#### Action outputs

The **Generate Token** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Generate Token** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched the refresh token: REFRESH_TOKEN_VALUE. Copy this refresh token to the Integration Configuration. Note: This Token is valid for 90 days only.` | Action succeeded.  
`Failed to get the refresh token! The Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Generate Token** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Account Out Of Facility Settings

Use the **Get Account Out Of Facility Settings** action to get the account out of facility (OOF) settings for the provided Google SecOps `User` entity.

If the target user entity is a username and not an email, run the [Active Directory **Enrich Entities** action](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory) to retrieve an information about the user email that is stored in Active Directory.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Get Account Out Of Facility Settings** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Account Out Of Facility Settings** action returns the following table on a Case Wall in Google SecOps:

Table name: **Out of Facility Settings**

Table columns:

  * **Parameter**
  * **Value**



##### Entity enrichment

The **Get Account Out Of Facility Settings** action supports the following entity enrichment:

Enrichment field | Source (JSON key) | Logic  
---|---|---  
`Exchange.oof_settings` | `OofSettings` | The action returns the disabled or enabled state based on the API response.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Account Out Of Facility Settings** action:
    
    
    OofSettings(state='Disabled', external_audience='All', start=EWSDateTime(2020, 10, 1, 3, 0, tzinfo=<UTC>), end=EWSDateTime(2020, 10, 2, 3, 0, tzinfo=<UTC>))
    

##### Output messages

The **Get Account Out Of Facility Settings** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned OOF settings for ENTITY_ID` `Action wasn't able to find OOF settings for ENTITY_ID` | Action succeeded.  
`Error executing action "Get Account Out Of Facility Settings". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Get Authorization

Use the **Get Authorization** action to obtaining a link with the access code for the integration configuration with OAuth authentication. Copy the link and use it in the **Generate Token** action to get the refresh token.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Get Authorization** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

This **Get Authorization** action returns the following link:

Name: **Browse to this authorization link**

Link: `AUTHORIZATION_LINK`

##### Output messages

This **Get Authorization** action can return the following output messages:

Output message | Message description  
---|---  
`Authorization URL generated successfully. Please navigate to the link below as the user that you want to run integration with, to get a URL with access code. The URL with access code should be provided next in the Generate Token action.` | Action succeeded.  
`Failed to generate authorization URL! The Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Authorization** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Mail EML File

Use the **Get Mail EML File** action to retrieve a message EML file.

This action runs on all Google SecOps entities.

#### Action inputs

The **Get Mail EML File** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Optional_ A folder to fetch an email from.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Message ID` | _Required_ The message ID, such as `1701cf01ba314032b2f1df43262a7723@example.com`.  
`Base64 Encode` | _Optional_ If selected, the action encodes the mail file with in a base64 format. Not selected by default.  
  
#### Action outputs

The **Get Mail EML File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Mail EML File** action:

Script result name | Value  
---|---  
eml_info | `EML_INFORMATION`  
  
### Move Mail to Folder

Use the **Move Mail to Folder** action to move one or multiple emails from the source email folder to the other folder in a mailbox.

Depending on the use case, the action returns a different amount of information about processed emails in the JSON result.

If you select the **Limit the amount of information in the JSON result** parameter, the JSON result contains only the following email fields: `datetime_received`, `message_id`, `sender`, `subject`, `to_recipients`. Otherwise, the JSON result contains all available information about the processed email.

If you select the **Disable the Action JSON Result** parameter, the action doesn't return the JSON result at all.

The **Move Mail to Folder** action doesn't run on Google SecOps entities.

#### Action inputs

The **Move Mail to Folder** action requires the following parameters:

Parameter | Description  
---|---  
`Source Folder Name` | _Required_ A source folder to move emails from.  
`Destination Folder Name` | _Required_ A destination folder to move emails to.  
`Subject Filter` | _Optional_ A filter condition to search emails by specific subject.  
`Message IDs` | _Optional_ A filter condition to search for emails with specific email IDs. This parameter also accepts a comma-separated list of message IDs to search for. If you provide the message ID, the action ignores the `Subject Filter` parameter.  
`Only Unread` | _Optional_ A filter condition to search only for unread emails. Not selected by default.  
`Move In All Mailboxes` | _Optional_ If selected, the action searches and moves emails in all mailboxes accessible through current impersonalization settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Required_ The number of mailboxes to process in a single batch (single connection to the mail server).If you select the `Move In All Mailboxes` parameter, the action works in batches. The default value is 25.  
`Time Frame (minutes)` | _Optional_ A period in minutes to search for emails.  
`Limit the Amount of Information Returned in the JSON Result` | _Optional_ If selected, the action returns information only about the key email fields. If not selected, the action returns information about all email fields.Selected by default.  
`Disable the Action JSON Result` | _Optional_ If selected, the action doesn't return the JSON result. Not selected by default.  
  
#### Action outputs

The **Move Mail to Folder** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Move Mail to Folder** action can return the following output messages:

Output message | Message description  
---|---  
`NUMBER_OF_EMAILS mails were successfully moved from  SOURCE_FOLDER to  DESTINATION FOLDER` `No mails were found matching the search criteria!` | Action succeeded.  
`Error search emails:  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Move Mail to Folder** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test a connection to the Microsoft Exchange instance.

You can execute this action can be manually and not as a part of the playbook flow.

This action doesn't run on Google SecOps entities.

#### Action inputs

N/A

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Microsoft Exchange server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Microsoft Exchange server! Error is  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Save Mail Attachments To The Case

Use the **Save Mail Attachments To The Case** action to save email attachments from an email stored in the monitored mailbox to the Case Wall in Google SecOps.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Save Mail Attachments To The Case** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Required_ A mailbox folder to search an email in.This parameter also accepts a comma-separated list of folders.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Message IDs` | _Required_ The message ID to find a specific email and download attachments from it.  
`Attachment To Save` | _Optional_ If you don't configure this parameter, the action saves all email attachments to the Case Wall by default. Otherwise, the action saves only the attachment which you specified to the Case Wall.  
  
#### Action outputs

The **Save Mail Attachments To The Case** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Save Mail Attachments To The Case** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully saved the following attachments from the email MESSAGE_ID: ATTACHMENT_LIST` `No attachments found in email  MESSAGE_ID` | Action succeeded.  
`Failed to save the email attachments to the case, the error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Save Mail Attachments To The Case** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Mails

Use the **Search Mails** action to search for specific emails in a configured mailbox using multiple search criteria. This action returns information about emails that were found in a mailbox in the JSON format.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Search Mails** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | _Optional_ A mailbox folder to search an email in.This parameter accepts a comma-separated list of folders.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Subject Filter` | _Optional_ A filter condition which specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition to specify the sender of requested emails.  
`Recipient Filter` | _Optional_ A filter condition to specify the recipient of requested emails.  
`Time Frame (minutes)` | _Optional_ A period in minutes to search for emails.  
`Only Unread` | _Optional_ If selected, the action searches only for unread emails. Not selected by default.  
`Max Emails To Return` | _Optional_ The maximum number of emails to return in the action result.  
`Search in all mailboxes` | _Optional_ If selected, the action runs a search in all mailboxes that are accessible using current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Required_ The number of mailboxes to process in a single batch (single connection to the mail server).If you select the `Search in all mailboxes` parameter, the action works in batches. The default value is 25.  
`Start Time` | _Optional_ The start time for running the email search. The format to use is ISO 8601. This parameter has a priority over the `Time Frame (minutes)` parameter.  
`End Time` | _Optional_ The end time for running the email search. The format to use is ISO 8601. If you don't set a value and the `Start Time` parameter is valid, the action sets the `End Time` value to the current time.  
`Mailboxes` | _Optional_ A comma-separated list of mailboxes to run a search through.This parameter has priority over the `Search in all mailboxes` parameter.  
`Message IDs` | _Optional_ A comma-separated list of message IDs to search for. This filter has priority over other filter conditions.  
`Body Regex Filter` | _Optional_ A regular expression pattern to search for in the email body.  
  
#### Action outputs

The **Search Mails** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Search Mails** action returns the following table on a Case Wall in Google SecOps:

Table title: **Matching Mails**

Table columns:

  * **Message_id**
  * **Received Date**
  * **Sender**
  * **Recipients**
  * **Subject**
  * **Email body**
  * **Attachment names** (as a comma-separated list of attachment names)



If you select the `Search in all mailboxes` parameter, the action adds the **Found in mailbox** column to the table to indicate which mailbox the email was found in.

##### JSON result

The following example shows the JSON result output received when using the **Search Mails** action:
    
    
    [
        {
            "body": "Mail Body",
            "subject": "Mail Subject",
            "author": "user_1@example.com"
        }, {
            "body": " ",
            "subject": "Mail Subject",
            "author": "user_2@example.com"
        }
    ]
    

##### Output messages

The **Search Mails** action can return the following output messages:

Output message | Message description  
---|---  
`Search found  NUMBER_OF EMAILS emails based on the provided search criteria.` `Search didn't find any matching emails.` `The following mailboxes were not found in the Mail Server: MAILBOX_LIST` | Action succeeded.  
`Search didn't completed successfully due to error: ERROR_REASON` `Error executing action "Exchange - Search Mails". Reason: the following mailboxes were not found:  MAILBOX_LIST. Please check the spelling.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Mails** action:

Script result name | Value  
---|---  
mails_json | Not available  
  
### Send Email and Wait - Deprecated

**Deprecated:** This action is deprecated. It is recommended to use a combination of the Send Mail and Wait For Mail From.

Send email and wait action. Thr Send to field is comma-separated. Sender's display name can be configured in the client under the account settings.

#### Action inputs

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subject | String | N/A | Yes | The subject of the email.  
Send to | String | user@example.com | Yes | Recipient email address. Multiple addresses can be separated by commas.  
CC | String | user@example.com | No | CC email address. Multiple addresses can be separated by commas.  
BCC | String | N/A | No | BCC email address. Multiple addresses can be separated by commas.  
Mail content | String | N/A | Yes | Email body.  
Fetch Response Attachments | Checkbox | Unchecked | No | Allows attachment of files from response mail.  
Folder to Check for Reply | String | Inbox | No | Parameter can be used to specify the mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. The parameter also accepts a comma-separated list of folders to check the user response in multiple folders. Parameter is case-sensitive.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
Mail_body | N/A | N/A  
  
##### JSON Result
    
    
      [
          {
              "EntityResult": {
                  "attachments": [],
                  "sensitivity": "Normal",
                  "effective_rights": " test",
                  "has_attachments": "false",
                  "last_modified_name": "mail",
                  "is_submitted": "false"
              },
              "Entity": "example@example.com"
          }
      ]
      

### Send Mail

Use the **Send Mail** action to send an email from a specific mailbox to a list of recipients. You can use this action to inform users about the following:

  * Specific alerts created in Google SecOps.
  * Results of the specific alerts processing.



This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Mail** action requires the following parameters:

Parameter | Description  
---|---  
`Subject` | _Required_ The email subject.  
`Send to` | _Required_ A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | _Optional_ A comma-separated list of email addresses for the email CC field, such as `user1@example.com, user2@example.com`.  
`BCC` | _Optional_ A comma-separated list of email addresses for the email BCC field, such as `user1@example.com, user2@example.com`.  
`Attachments Paths` | _Optional_ A comma-separated list of paths for file attachments stored on the server, such as `C:\FILE_DIRECTORY\file.pdf, C:\FILE_DIRECTORY\image.jpg`.  
`Mail content` | _Required_ The email body.  
`Reply-To Recipients` | _Optional_ A comma-separated list of recipients used in the _Reply-To_ header. The action adds the _Reply-To_ header to send email replies to specific email addresses instead of the email sender address that is stated in the _From_ field.  
`Base64 Encoded Certificate` | _Optional_ A base64-encoded certificate used to encrypt an email.To encrypt the email, this parameter is enough. To sign the email, also provide the `Base64 Encoded Signature` parameter.  
`Base64 Encoded Signature` | _Optional_ A base64 encoded certificate used to sign an email.For the signature to work and contain a signing certificate, provide both `Base64 Encoded Signature` and `Base64 Encoded Certificate` parameters.  
  
#### Action outputs

The **Send Mail** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Send Mail** action:
    
    
    {
        "mime_content": "b'From: exchange_online_test\\r\\n\\t<test_user@example.com>\\r\\nTo: =?iso-8859-8-i?B?4ifp6e7xIOHl8OM=?=\\r\\n\\t<example@example.com>\\r\\nSubject: test email\\r\\nThread-Topic: test email\\r\\nThread-Index: AQHZI2sS6qOMRJL5hkWATMpRN9fv4Q==\\r\\nDate: Sun, 8 Jan 2023 14:11:15 +0000\\r\\nMessage-ID: <message_id@example>\\r\\nAccept-Language: en-US\\r\\nContent-Language: en-US\\r\\nX-MS-Has-Attach:\\r\\nContent-Type: multipart/alternative;\\r\\n\\tboundary=\"_000_1673187082551404817642532883270906446a69558cb5108_\"\\r\\nMIME-Version: 1.0\\r\\n\\r\\n--_000_1673187082551404817642532883270906446a69558cb5108_\\r\\nContent-Type: text/plain; charset=\"iso-8859-8-i\"\\r\\nContent-Transfer-Encoding: quoted-printable\\r\\n\\r\\ntest content\\r\\n\\r\\n--_000_1673187082551404817642532883270906446a69558cb5108_\\r\\nContent-Type: text/html; charset=\"iso-8859-8-i\"\\r\\nContent-Transfer-Encoding: quoted-printable\\r\\n\\r\\n<html>\\r\\n<head>\\r\\n<meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3Diso-8859-=\\r\\n8-i\">\\r\\n</head>\\r\\n<body>\\r\\n<p>test content </p>\\r\\n</body>\\r\\n</html>\\r\\n\\r\\n--_000_1673187082551404817642532883270906446a69558cb5108_--\\r\\n'",
        "_id": "ItemId(id='AAMkAGMwYTc3NmZmLTM4YjYtNGJmMC1hNTllLWJmNDdlZTE0YTg4ZQBGAAAAAABZKh7ro7RoSpjbI663J/SqBwDjM1k0xgBMR6sDaC+Azo7rAAAAAAEJAADjM1k0xgBMR6sDaC+Azo7rAAAAEth6AAA=', changekey='CQAAABYAAADjM1k0xgBMR6sDaC+Azo7rAAAAEm3h')",
        "parent_folder_id": "ParentFolderId(id='AAMkAGMwYTc3NmZmLTM4YjYtNGJmMC1hNTllLWJmNDdlZTE0YTg4ZQAuAAAAAABZKh7ro7RoSpjbI663J/SqAQDjM1k0xgBMR6sDaC+Azo7rAAAAAAEJAAA=', changekey='AQAAAA==')",
        "item_class": "IPM.Note",
        "subject": "test email",
        "sensitivity": "Normal",
        "text_body": "test content\r\n",
        "body": "<html><head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body><p>test content </p></body></html>",
        "attachments": [],
        "datetime_received": "2023-01-08 14:11:15+00:00",
        "size": 2928,
        "categories": null,
        "importance": "Normal",
        "in_reply_to": null,
        "is_submitted": true,
        "is_draft": true,
        "is_from_me": false,
        "is_resend": false,
        "is_unmodified": false,
        "headers": null,
        "datetime_sent": "2023-01-08 14:11:15+00:00",
        "datetime_created": "2023-01-08 14:11:15+00:00",
        "reminder_due_by": null,
        "reminder_is_set": false,
        "reminder_minutes_before_start": 0,
        "display_cc": null,
        "display_to": "\u05d2'\u05d9\u05d9\u05de\u05e1 \u05d1\u05d5\u05e0\u05d3",
        "has_attachments": false,
        "vote_request": null,
        "culture": "en-US",
        "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)",
        "last_modified_name": "exchange_online_test",
        "last_modified_time": "2023-01-08 14:11:15+00:00",
        "is_associated": false,
        "web_client_read_form_query_string": "https://example.com/&exvsurl=1&viewmodel=ReadMessageItem",
        "web_client_edit_form_query_string": null,
        "conversation_id": "ConversationId(id='AAQkAGMwYTc3NmZmLTM4YjYtNGJmMC1hNTllLWJmNDdlZTE0YTg4ZQAQAOqjjESS+YZFgEzKUTfX7+E=')",
        "unique_body": "<html><body><div>\r\n<div>\r\n<p>test content </p></div></div>\r\n</body></html>",
        "sender": "Mailbox(name='exchange_online_test', email_address='test_user@example.com', routing_type='SMTP', mailbox_type='Mailbox')",
        "to_recipients": [
            "Mailbox(name=\"\u05d2'\u05d9\u05d9\u05de\u05e1 \u05d1\u05d5\u05e0\u05d3\", email_address='example@example.com', routing_type='SMTP', mailbox_type='Mailbox')"
        ],
        "cc_recipients": null,
        "bcc_recipients": null,
        "is_read_receipt_requested": false,
        "is_delivery_receipt_requested": false,
        "conversation_index": "b'\\x01\\x01\\xd9#k\\x12\\xea\\xa3\\x8cD\\x92\\xf9\\x86E\\x80L\\xcaQ7\\xd7\\xef\\xe1'",
        "conversation_topic": "test email",
        "author": "Mailbox(name='exchange_online_test', email_address='test_user@example.com', routing_type='SMTP', mailbox_type='Mailbox')",
        "message_id": "<167318708255.14048.17642532883270906446@a69558cb5108>",
        "is_read": true,
        "is_response_requested": false,
        "references": null,
        "reply_to": null,
        "received_by": null,
        "received_representing": null,
        "vote_response": null,
        "email_date": 1673187075
    }
    

In addition to the mail object JSON technical result, the action also returns the message ID and the date when an email was sent. The additional data is used in the **Wait for Mail** action, if needed:
    
    
    {
    …
    "message_id": "<message_id@example.com>",
    "email_date": "1583916838"
    ...
    }
    

##### Output messages

The **Send Mail** action can return the following output messages:

Output message | Message description  
---|---  
`Mail sent successfully.` | Action succeeded.  
`Failed to send email! The Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Send Mail** action:

Script result name | Value  
---|---  
`Success_Inidicator` | Not available  
  
### Send Mail HTML

Use the **Send Mail HTML** action to send an email with the HTML template content. The `Send to` field is comma-separated.

You can configure the sender name in the email client under the account settings.

This action runs on all Google SecOps entities.

#### Action inputs

The **Send Mail HTML** action requires the following parameters:

Parameter | Description  
---|---  
`Subject` | _Required_ The email subject.  
`Send to` | _Required_ A comma-separated list of email addresses for the email recipients.  
`CC` | _Optional_ A comma-separated list of email addresses for the email CC field.  
`BCC` | _Optional_ A comma-separated list of email addresses for the email BCC field.  
`Attachments Paths` | _Optional_ A comma-separated list of paths for file attachments stored on the server, for example, `C:\FILE_DIRECTORY\file.pdf, C:\FILE_DIRECTORY\image.jpg`.  
`Mail content` | _Required_ The email body.  
  
#### Action outputs

The **Send Mail HTML** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Thread Reply

Use the **Send Thread Reply** action to send a message as a reply to the email thread.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Thread Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Message ID` | _Required_ The ID of the message to send a reply to.  
`Folder Name` | _Required_ A comma-separated list of mailbox folders in which to run a search for an email.You can set mail-specific folders, for example, _Gmail/All Mail_ to run a search in all of the Gmail mailbox folders. Additionally, the folder name must match the IMAP folder. If the folder name contains spaces, wrap spaces in double quotes. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.  
`Content` | _Required_ A content of the reply.  
`Attachment Paths` | _Optional_ A comma-separated list of paths to file attachments stored on the server.   
`Reply All` | _Optional_ If selected, the action sends a reply to all recipients related to the original email and the ignores the `Reply To` parameter.Selected by default.  
`Reply To` | _Required_ A comma-separated list of emails to send the reply to. If you don't set a value and don't select the `Reply All` parameter, the action only sends a reply to the sender of the email. If you select the `Reply All` parameter, the action ignores this parameter.  
  
#### Action output

The **Send Thread Reply** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Send Thread Reply** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully sent reply to the message with ID MESSAGE_ID in Exchange.` | Action succeeded.  
`Error executing action "Send Thread Reply". Reason: if you want to send a reply only to your own email address, you need to work with "Reply To" parameter.` | Action failed.Check the `Reply To` parameter to send replies only to your address.  
`Error executing action "Send Thread Reply". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Send Thread Reply** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Vote Mail

Use the **Send Vote Mail** action to send emails with preconfigured answer options to include users who don't have access to the Google SecOps UI in automated processes.

This action supports the vote feature only if the recipients use Exchange to properly view and select the vote options.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Vote Mail** action requires the following parameters:

Parameter | Description  
---|---  
`Subject` | _Required_ The email subject.  
`Send to` | _Required_ A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | _Optional_ A comma-separated list of email addresses for the email CC field, such as `user1@example.com, user2@example.com`.  
`BCC` | _Optional_ A comma-separated list of email addresses for the email BCC field, such as `user1@example.com, user2@example.com`.  
`Attachments Paths` | _Optional_ A comma-separated list of paths for file attachments stored on the server, for example, `C:\FILE_DIRECTORY\file.pdf, C:\FILE_DIRECTORY\image.jpg`.  
`Question or Decision Description` | _Required_ The question to ask recipients or the decision for the recipients to respond to.  
`Structure of voting options` | _Required_ A structure of the vote to sent to recipients. The possible values are as follows:

  * `Yes/No`
  * `Approve/Reject`

The default value is `Yes/No`.  
  
#### Action outputs

The **Send Vote Mail** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Send Vote Mail** action:
    
    
    {
    
    …
    
    "message_id": "example@example.com>",
    
    "email_date": "1583916838"
    
    ...
    
    }
    

##### Output messages

The **Send Vote Mail** action can return the following output messages:

Output message | Message description  
---|---  
`Vote Mail was sent successfully` `Could not send vote mail for the following mailboxes: MAILBOX_LIST` | Action succeeded.  
`Could not send vote mail to any of the provided mailboxes. Please check the action parameters and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Send Vote Mail** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Wait for Mail From User

Use the **Wait for Mail From User** action to wait for the user response based on an email sent with the **Send Mail** action.

This action works asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Wait for Mail From User** action requires the following parameters:

Parameter | Description  
---|---  
`Mail message_id` | _Required_ The message ID of the email.If the message is sent using the `Send Mail` action, select the `SendEmail.JSONResult|message_id` field as a placeholder.  
`Mail Date` | _Required_ A timestamp of the sent email which the current action awaits for. If a message is sent using the _Send Mail_ action, select the `SendEmail.JSONResult|email_date` field as a placeholder.  
`Mail Recipients` | _Required_ A comma-separated list of email recipients which the current action awaits the response from.If a message is sent using the _Send Mail_ action, select the `SendEmail.JSONResult|to_recipients` field as a placeholder.  
`How long to wait for recipient reply (minutes)` | _Required_ A period for the action to wait for the user reply before marking it timed out.The default value is 1440 minutes.  
`Wait for All Recipients to Reply?` | _Optional_ If selected, the action waits for responses from all recipients until either reaching a timeout or proceeding with the first reply. Selected by default.  
`Wait Stage Exclude pattern` | _Optional_ A regular expression to exclude specific replies from the wait stage. This parameter works with the email body. For example, you can configure the action to not consider automatic out-of-office messages as recipient replies and instead wait for an actual user reply.  
`Folder to Check for Reply` | _Optional_ A mailbox email folder to search for the user reply in. The action runs a search in the mailbox which the email containing a question was sent from. This parameter accepts a comma-separated list of folders. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. This parameter is case-sensitive. The default value is `Inbox`.  
`Fetch Response Attachments` | _Optional_ If selected and the recipient reply contains attachments, the action retrieves the reply and adds it as an attachment for the action result. Not selected by default.  
  
#### Action outputs

The **Wait for Mail From User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### Case wall attachment

The **Wait for Mail From User** action returns the following attachment on a Case wall in Google SecOps:

Attachment field | Description  
---|---  
`title` | Attachment from the recipient `RECIPIENT_EMAIL` reply  
`filename` | `ATTACHMENT_NAME`. `EXTENSION`  
`fileContent` | `ATTACHED_FILE_CONTENT `  
  
The attachment type is **Entity** is mapped to the recipient who replied to the `message_id` that the Google SecOps server tracks the responses for.

##### JSON result

As a JSON result, the action returns a combination of the two following outputs:

  1. A mail object JSON output for the email with a tracked response.

The action tracks the email response using `message_id`.

  2. A JSON output for the process of tracking responses from users.




The method to merge the output data is defined at the implementation stage.

The flow for the mail object JSON output is as follows:

  1. the action waits for at least one user response to proceed.

  2. After receiving the response from the first user, the action updates the JSON result and proceeds with action results.
         
         {
         "Responses":
         {[
             "user1@example.com": "Approved",
             "user2@example.com": "",
             "user3@example.com": ""
         ]}
         }
         




The flow for the tracking response process output is as follows:

  1. The action waits for all user responses to proceed.

  2. After receiving replies from users or reaching timeout, the action updates the JSON result.

In this case, if the action is waiting for responses from all recipients and the timeout is reached while waiting for user responses, the action returns the `handled_timeout` error.
         
         {
         "Responses":
         {[
             "user1@example.com": "Approved",
             "user2@example.com": "Approved",
             "user3@example.com": "Timeout"
         ]}
         }
         




##### Output messages

The **Wait for Mail From User** action can return the following output messages:

Output message | Message description  
---|---  
`Found the user  EMAIL_RECIPIENT reply:  USER_REPLY` `Timeout getting reply from user:  EMAIL_RECIPIENT` | Action succeeded.  
`Failed to execute action, the error is: ERROR_REASON` `Failed to get user  EMAIL_RECIPIENT reply, the error is:  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Wait for Vote Mail Results

Use the **Wait for Vote Mail Results** action to wait for and retrieve the responses of a vote mail that was sent using the **Send Vote Mail** action. The **Wait for Vote Mail Results** action forwards the retrieved responses to Google SecOps.

To properly track and retrieve the vote results, track the vote email. For more information, see the **Send Vote Mail** action.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Wait for Vote Mail Results** action requires the following parameters:

Parameter | Description  
---|---  
`Vote Mail message_id` | _Required_ The message ID of the vote email.If the message is sent using the `Send Vote Mail` action, select the `SendVoteMail.JSONResult|message_id` field as a placeholder.  
`Mail Recipients` | _Required_ A comma-separated list of recipient emails the current action awaits the response from.Select the `SendVoteMail.JSONResult|to_recipients ` field as a placeholder.  
`Folder to Check for Reply` | _Required_ A mailbox folder to search for the user reply in. The action runs a search in the mailbox which the email containing a question was sent from.This parameter also accepts a comma-separated list of folders. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. This parameter is case-sensitive. The default value is `Inbox`.  
`Folder to Check for Sent Mail` | _Required_ A mailbox folder to search for the sent mail in. The action runs a search in the mailbox which the email containing a question was sent from. This parameter also accepts a comma-separated list of folders. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.This parameter is case-sensitive. The default value is `Sent Items`.  
`How long to wait for recipient reply (minutes)` | _Required_ A period for the action to wait for the user reply before marking it as timed out.The default value is 1440 minutes.  
`Wait for All Recipients to Reply?` | _Optional_ If selected, the action waits for responses from all recipients until reaching a timeout or proceeding with the first reply. Selected by default.  
  
#### Action outputs

The **Wait for Vote Mail Results** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Wait for Vote Mail Results** action:
    
    
    {
        "Responses": [{
            "recipient": "user@example.com",
            "content": "Approve"
        }]
    }
    

##### Output messages

The **Wait for Vote Mail Results** action can return the following output messages:

Output message | Message description  
---|---  
`Found the user  EMAIL_RECIPIENT reply:  USER_REPLY` `Timeout getting reply from user:  EMAIL_RECIPIENT` | Action succeeded.  
`Could not perform action on the following mailboxes: MAILBOX_LIST` `Could not perform action on any of the provided mailboxes. Please check the action parameters and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Wait for Vote Mail Results** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## The Block Sender and Domain functionality

One of the most common use cases for email management and security is to contain existing threats, like phishing emails, that are already in the organization inbox, and then block a suspicious sender or a domain to protect your organization from future attacks and prevent possible security breaches.

In Google SecOps, the Exchange integration provides you with the **Block Sender and Domain** functionality comprising of the following sequential stages:

  1. Protection within the organization.

Use the **Block Sender by Message ID** action to add the sender to the blocklist using the _Mark as Junk_ EWS service.

  2. Protection outside of the organization with inbox rules.

Create inbox rules to add them on the client level and automatically prevent harmful emails from reaching your organization mailboxes.

  3. Protection outside of the organization with server inbox rules.

Create server inbox rules to prevent suspicious emails from even reaching the organization.




You can learn more about these stages in the following section.

### Use case

The following use case shows an example of a security breach that is a suspicious and potentially harmful email.

After discovering that a suspicious and harmful email has compromised several mailboxes of your organization, the routine for handling this kind of threat is as follows:

  1. Remediate the threat with the **Block Sender by Message ID** action.
  2. Handle compromised mailboxes.
  3. Add a protection against the received suspicious email in other mailboxes as well.



#### Remediate threat

To remediate the threat, run the **Block Sender by Message ID** action to obtain the parameters for investigation and more information about the suspicious email. The action also lets you examine only the compromised mailboxes and handle the threat contained in them.

The **Block Sender by Message ID** action triggers the Exchange EWS _Mark as Junk_ service to do the following:

  1. Move the suspicious email to the **Junk** folder.
  2. Add the email sender to the **Blocked Sender List** of the investigated mailbox.



For more information about using the _Mark as Junk_ service, see [Add and remove email addresses from the **Blocked Sender List** by using EWS in Exchange](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-add-and-remove-email-addresses-from-blocked-senders-list-by-using-ews) in Microsoft product documentation.

On one hand, remediating a threat with the **Block Sender by Message ID** action targets only compromised mailboxes and can be automatic. On the other hand, the action can neither block a sender in the uncompromised mailboxes nor add domains using API to the **Blocked Sender List**.

#### Handle compromised mailboxes

After remediating a threat, the next steps are to handle compromised mailboxes and protect every mailbox in the organization from any malicious senders, even the potential ones.

To handle compromised mailboxes, execute the inbox rules action set that consists of the following actions:

  1. **Add Domains to Exchange-Siemplify Inbox Rules**
  2. **Add Senders to Exchange-Siemplify Inbox Rule**
  3. **Delete Exchange-Siemplify Inbox Rules**
  4. **List Exchange-Siemplify Inbox Rules**
  5. **Remove Domains from Exchange-Siemplify Inbox Rules**
  6. **Remove Senders from Exchange-Siemplify Inbox Rules**



To learn more about the service used in the actions, see [Manage inbox rules in Exchange](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-manage-inbox-rules-by-using-ews-in-exchange) in Microsoft product documentation.

The Exchange integration lets you use a set of the following predefined rules for the most common operations:

  * **Siemplify – Senders List – Move To Junk**
  * **Siemplify – Senders List – Delete**
  * **Siemplify – Senders List – Permanently Delete**
  * **Siemplify – Domains List – Move To Junk**
  * **Siemplify – Domains List – Delete**
  * **Siemplify – Domains List – Permanently Delete**



#### Permanently delete the malicious sender emails

To maintain the same list of rules in all mailboxes, add the rules for the administrator user. To apply the administrator rules to other users, run the operation on all mailboxes.

To permanently delete the malicious sender emails, complete the following steps:

  1. In Google SecOps, from the administrator account, run the **Add Senders to Exchange-Siemplify Inbox Rule** action. Enter the malicious sender email.

  2. Choose the appropriate rule from the list to define how to manage a suspicious email. To permanently delete malicious emails, select the **Siemplify – Senders List – Permanently Delete** rule.

The action updates the inbox rule with the new malicious sender.

  3. Select the `Perform action in all mailboxes` parameter to apply the rule to all mailboxes.

If the rule doesn't exist in a mailbox, the action creates it. If the rule already exists in a mailbox, the action updates it with the new parameter values.

  4. To add a protection against the received suspicious email in other mailboxes and block the malicious sender domain, select the `Should add senders' domain to the corresponding Domains List rule as well?` parameter.

  5. Review other parameters in the action and adjust them if necessary.




The **Add Senders to Exchange-Siemplify Inbox Rule** action updates multiple rules at a time according to the `Mailboxes to process in one batch` parameter. The **Add Senders to Exchange-Siemplify Inbox Rule** action works on both senders and domains, applies to all mailboxes regardless of whether there's a suspicious email received, and can be automatic.

The end user can delete the applied rules for their mailbox. Applying administrator rules to other mailboxes automatically removes disabled private inbox rules.

### The Block Sender and Domain actions

Before running the actions for the Block Sender and Domain functionality, configure the minimal required permissions.

### Add Domains to Exchange-Siemplify Inbox Rules

Use the **Add Domains to Exchange-Siemplify Inbox Rules** action to get a list of domains as a parameter or work with the Google SecOps **Domain** entity if the parameters are empty. This action is available only for Google SecOps version 5.6 and later.

Before running this action, configure the required action permissions.

You can create or update a rule by filtering the domains from your mailboxes. You can modify this action using the `Rule to add Domains to` parameter.

The **Add Domains to Exchange-Siemplify Inbox Rules** action modifies the current inbox rules of your users with EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

If you don't set any parameters and your Google SecOps version is 5.6 and later, this action runs on the **Domain** entity.

#### Action inputs

The **Add Domains to Exchange-Siemplify Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Domains` | _Optional_ A comma-separated list of domains to add to the rule.  
`Rule to add Domains to` | _Required_ A rule to add domains to.If there is no rule, the action creates it.The possible values are as follows:

  * `Siemplify - Domains List - Move To Junk`
  * `Siemplify - Domains List - Delete`
  * `Siemplify - Domains List - Permanently Delete`

The default value is `Siemplify - Domains List - Move To Junk`.   
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 50.  
  
#### Action outputs

The **Add Domains to Exchange-Siemplify Inbox Rules** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Domains to Exchange-Siemplify Inbox Rules** action can return the following output messages:

Output message | Message description  
---|---  
`Added the following Domains to the corresponding rules: Domains: DOMAIN_LIST Rules updated: RULE_LIST` `Successfully updated  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` `NUMBER_OF_UPDATED_MAILBOXES mailboxes were updated out of  ALL_MAILBOXES mailboxes. Continuing.` | Action succeeded.  
`Error performing "Add Domains to Exchange-Siemplify Inbox Rules" action: ERROR_REASON` `No domains provided in "Domains" parameter, please check action parameters and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Domains to Exchange-Siemplify Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Senders to Exchange-Siemplify Inbox Rule

Use the **Add Senders to Exchange-Siemplify Inbox Rule** action to obtain a list of email addresses as a or work with the Google SecOps **User** entity if the parameters are empty. You can use regular expressions for this action.

You can create a new rule by filtering the senders from your mailboxes. You can modify this action using the `Rule to add senders to` parameter.

Before running this action, make sure to configure the required action permissions.

The **Add Senders to Exchange-Siemplify Inbox Rule** action modifies the current inbox rules of your users using EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

If the email regular expression is valid and you don't configure any parameters, this action runs on the **User** entity.

#### Action inputs

The **Add Senders to Exchange-Siemplify Inbox Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Senders` | _Optional_ A comma-separated list of email addresses to add to the rule. If you don't set a value, the action works with the **User** entity.  
`Rule to add senders to` | _Required_ A rule to add the sender to.If there is no rule, the action creates it.The possible values are as follows:

  * `Siemplify - Senders List - Move To Junk`
  * `Siemplify - Senders List - Delete`
  * `Siemplify - Senders List - Permanently Delete`

The default value is `Siemplify - Senders List - Move To Junk`.   
`Should add senders' domain to the corresponding Domains List rule as well?` | _Optional_ If selected, the action automatically adds the domains of the provided email addresses to the corresponding domain rules.Not selected by default.  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonalization settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 50.  
  
#### Action outputs

The **Add Senders to Exchange-Siemplify Inbox Rule** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Senders to Exchange-Siemplify Inbox Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Added the following inputs to the corresponding rules: Email Addresses:  EMAIL_ADDRESS_LIST Domains: DOMAIN_LIST Rules updated: RULE_LIST` `Successfully updated  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` `NUMBER_OF_UPDATED_MAILBOXES mailboxes were updated out of  ALL_MAILBOXES mailboxes. Continuing.` | Action succeeded.  
`Error performing "Add Senders to Siemplify Inbox Rule" action: ERROR_REASON` `No email addresses provided in "Senders" parameter and there are no email addresses in user entities, Please check action inputs and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Senders to Exchange-Siemplify Inbox Rule** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Block Sender by Message ID

Use the **Block Sender by Message ID** action to obtain a list of message IDs as a parameter and mark the list as junk.

In this action, marking an item as junk adds the email sender address to the **Blocked Senders List** and moves the item to the Junk folder.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

The **Block Sender by Message ID** action supports only Exchange Server version 2013 and later. If you use an earlier version, the action fails with the corresponding message.

A message from the suspicious email address must exist in the user mailbox before you add the email address to or remove it from the **Blocked Senders List**.

The **Block Sender by Message ID** action doesn't run on Google SecOps entities.

#### Action inputs

The **Block Sender by Message ID** action requires the following parameters:

Parameter | Description  
---|---  
`Move item to Junk folder?` | _Required_ If selected, the action moves the specified messages to the junk folder. Selected by default.  
`Message IDs` | _Optional_ A filter condition to find emails with specific email IDs. This parameter accepts a comma-separated list of message IDs to mark as junk. If you provide the message ID, the action ignores the `Subject Filter`, `Sender Filter`, and `Recipient Filter` parameters.  
`Mailboxes list to perform on` | _Optional_ A filter condition to execute the operation on a specific list of mailboxes for better timing.To mark messages from multiple email addresses as junk, provide a comma-separated list of email addresses. If you provide a mailbox list, the action ignores the `Perform Action in all Mailboxes` parameter.  
`Folder Name` | _Optional_ A mailbox folder to search for an email in.This parameter accepts a comma-separated list of folders.The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.The default value is `Inbox`.  
`Subject Filter` | _Optional_ A filter condition which specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition which specifies the sender of requested emails.  
`Recipient Filter` | _Optional_ A filter condition which specifies the recipient of requested emails.  
`Mark All Matching Emails` | _Optional_ If selected, the action marks all emails from the mailbox that match the criteria. If not selected, the action marks only the first matching email. Not selected by default.  
`Perform action in all mailboxes` | _Optional_ If selected, the action moves to junk and blocks sender emails in all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server). The default value is 25.  
`Time Frame (minutes)` | _Optional_ The period in minutes to search for emails.  
  
#### Action outputs

The **Block Sender by Message ID** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Block Sender by Message ID** action can return the following output messages:

Output message | Message description  
---|---  
` NUMBER_OF_EMAILS mails were successfully marked as junk.` `No mails were found matching the search criteria!` ` NUMBER_OF_EMAILS email(s) were marked as junk from  PROCESSED_MAILBOXES mailboxes (out of  ALL_MAILBOXES). Continuing.` | Action succeeded.  
`Failed to execute action - Action is fully supported only from Exchange Server version 2013 and above, Please make sure you have the appropriate version configured in Chronicle SOAR.` | Action failed.The Exchange Server version that you're using isn't supported.  
`Error performing "Mark as junk and Block Sender" action: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Block Sender by Message ID** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Exchange-Siemplify Inbox Rules

Use the **Delete Exchange-Siemplify Inbox Rules** action to get a rule name as a parameter and delete it from all specified mailboxes.

Before running this action, configure the required action permissions.

The **Delete Exchange-Siemplify Inbox Rules** action modifies the current inbox rules of your users with EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Delete Exchange-Siemplify Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Rule Name To Delete` | _Required_ A rule name to completely delete from the relevant mailboxes. The possible values are as follows:

  * `Siemplify – Senders List – Move To Junk`
  * `Siemplify – Senders List – Delete`
  * `Siemplify – Senders List – Permanently Delete`
  * `Siemplify – Domains List – Move To Junk`
  * `Siemplify – Domains List – Delete`
  * `Siemplify – Domains List – Permanently Delete`
  * `All available Exchange-Siemplify Senders Rules`
  * `All available Exchange-Siemplify Domains Rules`
  * `All available Exchange-Siemplify Rules`

  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server). The default value is 50.  
  
#### Action outputs

The **Delete Exchange-Siemplify Inbox Rules** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Delete Exchange-Siemplify Inbox Rules** action can return the following output messages:

Output message | Message description  
---|---  
`Deleted the following rules from the specified mailboxes: MAILBOX_LIST Rules updated: RULE_LIST` `Successfully updated  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` `NUMBER_OF_UPDATED_MAILBOXES mailboxes were updated out of  ALL_MAILBOXES mailboxes. Continuing.` | Action succeeded.  
`Error performing "Delete Siemplify Inbox Rules" action: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Exchange-Siemplify Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Exchange-Siemplify Inbox Rules

Use the **List Exchange-Siemplify Inbox Rules** action to get a rule name from the Exchange-Siemplify Inbox rules as a parameter and list it. If there are no mailboxes to list, the action lists the rules for the logged in user.

Before running this action, configure the required action permissions.

The **List Exchange-Siemplify Inbox Rules** action modifies the current inbox rules of your users with EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Exchange-Siemplify Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Rule Name To List` | _Required_ A rule name to list from the relevant mailboxes. The possible values are as follows:

  * `Siemplify – Senders List – Move To Junk`
  * `Siemplify – Senders List – Delete`
  * `Siemplify – Senders List – Permanently Delete`
  * `Siemplify – Domains List – Move To Junk`
  * `Siemplify – Domains List – Delete`
  * `Siemplify – Domains List – Permanently Delete`
  * `All available Exchange-Siemplify Senders Rules`
  * `All available Exchange-Siemplify Domains Rules`
  * `All available Exchange-Siemplify Rules`

  
`Mailboxes list to perform on` | _Optional_ A filter condition which specifies the list of mailboxes to execute the operation on, for better timing.This parameter accepts a comma-separated list of mail addresses to unmark the messages as junk. If a mailbox list is provided, the action ignores the `Perform action in all mailboxes` parameter.  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 50.  
  
#### Action outputs

The **List Exchange-Siemplify Inbox Rules** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **List Exchange-Siemplify Inbox Rules** action:
    
    
    {
      {
        "id": "example_id",
        "name": "Siemplify - Domains List - Delete",
        "priority": 1,
        "is_enabled": True,
        "conditions": {
            "domains": ["EXAMPLE.COM", "EXAMPLE.CO"],
            "addresses": []
        },
        "actions": "move_to_folder"
      }
    }
    

##### Output messages

The **List Exchange-Siemplify Inbox Rules** action can return the following output messages:

Output message | Message description  
---|---  
`Listed the following rules: LISTED_RULES for the specified mailboxes.` `Successfully listed  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` | Action succeeded.  
`Error performing "List Exchange-Siemplify Inbox Rules" action: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Exchange-Siemplify Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Domains from Exchange-Siemplify Inbox Rules

Use the **Remove Domains from Exchange-Siemplify Inbox Rules** to get a list of domains as a parameter or work on the **Domain** entity if the parameters are not provided. This action is available only for Google SecOps version 5.6 and later. You can remove the provided domains from the existing rules.

Before running this action, configure the required action permissions.

The **Remove Domains from Exchange-Siemplify Inbox Rules** action modifies the current inbox rules of your users with EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

If you don't configure any parameters, this action runs on the Google SecOps **Domain** entity.

#### Action inputs

The **Remove Domains from Exchange-Siemplify Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Domains` | _Optional_ A comma-separated list of domains to remove from the rule.If you don't set a value, the action works with entities.  
`Rule to remove Domains from` | _Required_ A rule to remove domains from.If you don't set a rule, the action fails.The possible values are as follows:

  * `Siemplify – Domains List – Move To Junk`
  * `Siemplify – Domains List – Delete`
  * `Siemplify – Domains List – Permanently Delete`

The default value is `Siemplify – Domains List – Move To Junk`.   
`Remove Domains from all available Rules` | _Optional_ If selected, the action searches for the provided domains in all Google SecOps inbox rules. Not selected by default.  
`Mailboxes list to perform on` | _Optional_ A filter condition which specifies the list of mailboxes to execute the operation on, for better timing.This parameter accepts a comma-separated list of mail addresses to unmark the messages as junk. If you provide a mailbox list, the action ignores the `Perform action in all mailboxes` parameter.  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 50.  
  
#### Action outputs

The **Remove Domains from Exchange-Siemplify Inbox Rules** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Remove Domains from Exchange-Siemplify Inbox Rules** action can return the following output messages:

Output message | Message description  
---|---  
`Removed the following inputs from the corresponding rules: Domains: DOMAIN_LIST Rules updated: RULE_LIST` `Successfully updated  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` `NUMBER_OF_UPDATED_MAILBOXES mailboxes were updated out of  ALL_MAILBOXES mailboxes. Continuing.` | Action succeeded.  
`Error performing "Remove Domains from Siemplify Inbox Rule" action: ERROR_REASON` `No domains provided in "Domains" parameter, please check action parameters and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Domains from Exchange-Siemplify Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Senders from Exchange-Siemplify Inbox Rules

Use the **Remove Senders from Exchange-Siemplify Inbox Rules** get a list of email senders as a parameter or work with the **User** entity if the parameters are not provided.

You can remove the provided senders from the existing rules.

Before running this action, configure the required action permissions.

The **Remove Senders from Exchange-Siemplify Inbox Rules** action modifies the current inbox rules of your users with EWS.

This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

If no parameters are provided, this action runs on the Google SecOps **User** entity.

#### Action inputs

The **Remove Senders from Exchange-Siemplify Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Senders` | _Optional_ A comma-separated list of email addresses to remove from the rule. If you don't set a value, the action works with the **User** entity.  
`Rule to remove senders from` | _Required_ A rule to remove the senders from.If you don't set a rule, the action fails.The possible values are as follows:

  * `Siemplify – Senders List – Move To Junk`
  * `Siemplify – Senders List – Delete`
  * `Siemplify – Senders List – Permanently Delete`

The default value is `Siemplify – Senders List – Move To Junk`.  
`Remove senders from all available rules` | _Optional_ If selected, the action searches for the provided senders in all Google SecOps inbox rules. Not selected by default.  
`Should remove senders' domain from the corresponding Domains List rule as well?` | _Optional_ If selected, the action automatically removes the domains of the provided email addresses from the corresponding domain rules.Not selected by default.  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonalization settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 50.  
  
#### Action outputs

The **Remove Senders from Exchange-Siemplify Inbox Rules** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Remove Senders from Exchange-Siemplify Inbox Rules** action can return the following output messages:

Output message | Message description  
---|---  
`Removed the following inputs from the corresponding rules: Senders: SENDERS_LIST Rules updated: RULE_LIST` `Successfully updated  NUMBER_OF_UPDATED_MAILBOXES out of  ALL_MAILBOXES.` `Failed to perform operation on the following mailboxes: MAILBOX_LIST.` `NUMBER_OF_UPDATED_MAILBOXES mailboxes were updated out of  ALL_MAILBOXES mailboxes. Continuing.` | Action succeeded.  
`Error performing "Remove Senders from Siemplify Inbox Rule" action: ERROR_REASON` `No email addresses provided in "Senders" parameter and there are no email addresses in user entities, Please check action inputs and try again.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Senders from Exchange-Siemplify Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Unblock Sender by Message ID

Use the **Unblock Sender by Message ID** action to obtain a list of message IDs as a parameter and unmark it as junk.

In this action, unmarking an item as junk removes the sender email address from the **Blocked Senders List**. To move an item back to the inbox folder, select the `Move items back to Inbox?` parameter in the action parameters.

The **Unblock Sender by Message ID** runs asynchronously. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

This action supports only Exchange Server version 2013 and later. If you use an earlier version, the action fails with the corresponding message.

A message from the suspicious email address must exist in the user mailbox before you add the email address to or remove it from the **Blocked Senders List**.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Unblock Sender by Message ID** action requires the following parameters:

Parameter | Description  
---|---  
`Move items back to Inbox?` | _Required_ If selected, the action moves the specified messages back to the inbox folder.Selected by default.  
`Message IDs` | _Optional_ A filter condition to unmark emails with specific email IDs. This parameter also accepts a comma-separated list of message IDs to unmark emails as junk. If you provide the message ID, the action ignores the `Subject Filter`, `Sender Filter`, and `Recipient Filter` parameters  
`Mailboxes list to perform on` | _Optional_ A filter condition to execute the operation on a specific list of mailboxes for better timing.To mark messages from multiple email addresses as junk, provide a comma-separated list of email addresses. If you provide a mailbox list, the action ignores the `Perform action in all mailboxes` parameter.  
`Folder Name` | _Optional_ A mailbox folder to search an email in.This parameter accepts a comma-separated list of folders to move the item from. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore.The default value is `Junk Email`.  
`Subject Filter` | _Optional_ A filter condition which specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition which specifies the sender of requested emails.  
`Recipient Filter` | _Optional_ A filter condition which specifies the recipient of requested emails.  
`Unmark All Matching Emails` | _Optional_ If selected, the action unmarks all emails from the mailbox that match the criteria. If not selected, the action unmarks only the first matching email. Not selected by default.  
`Perform action in all mailboxes` | _Optional_ If selected, the action applies to all mailboxes accessible through the current impersonation settings. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ If you select the `Perform action in all mailboxes` parameter, the action works in batches.This parameter defines the number of mailboxes to process in a single batch (single connection to the mail server).The default value is 25.  
`Time Frame (minutes)` | _Optional_ A period in minutes to search for emails.  
  
#### Action outputs

The **Unblock Sender by Message ID** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Unblock Sender by Message ID** action can return the following output messages:

Output message | Message description  
---|---  
` NUMBER_OF_EMAILS mails were successfully unmarked as junk.` `No mails were found matching the search criteria!` ` NUMBER_OF_EMAILS email(s) were unmarked as junk from  PROCESSED_MAILBOXES mailboxes (out of ALL_MAILBOXES). Continuing.` | Action succeeded.  
`Failed to execute action - Action is fully supported only from Exchange Server version 2013 and above, Please make sure you have the appropriate version configured in Chronicle SOAR.` | Action failed.The Exchange Server version that you're using isn't supported.  
`Error performing action: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Unblock Sender by Message ID** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

When configuring connectors and actions, pay attention to spaces and special symbols in your credentials. If the integration rejects your credentials, check the spelling.

To configure the selected connector use the connector-specific parameters listed in the following tables:

  * Exchange EML Connector configuration parameters
  * Exchange Mail Connector configuration parameters
  * Exchange Mail Connector V2 configuration parameters
  * Exchange Mail Connector v2 with OAuth Authentication configuration parameters



### Exchange EML Connector

**Warning:** This connector is outdated. We recommend that you use the **Exchange Mail Connector v2** and **Exchange Mail Connector v2 with OAuth** connectors instead.

The **Exchange EML Connector** retrieves emails from the Exchange server and parses them. If there are attached EML files, the connector attaches them to the case as events. If there are multiple EML attachments in the email, the connector creates multiple cases and ingests every attachment as one event for each case.

#### Known restrictions

  1. Microsoft 365 and basic authentication.

     * The **Exchange EML Connector** doesn't support basic authentication anymore and cannot be used with Microsoft 365. For Microsoft 365, use the **Exchange Mail Connector v2 with OAuth**.
  2. The **Exchange EML Connector** specifics are as follows:

     * The connector creates Google SecOps alerts only from emails that contain EML or MSG file attachments.

     * The connector ignores emails that don't contain mail attachments.




#### Connector inputs

The **Exchange EML Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `device_product`.  
`EventClassId` | _Required_ A field name that is used to determine the event name (subtype).The default value is `event_name`.  
`Server IP` | _Required_ An IP address of the server to connect to.  
`Domain` | _Required_ A domain value to use for authentication.  
`Username` | _Required_ A username for the mailbox to pull emails from, like `user@example.com`.  
`Password` | _Required_ A password for the email mailbox to pull emails from.   
`Mail Address` | _Required_ An email address for the mailbox to monitor. The default value is `Inbox`.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Exchange server is valid. Not selected by default.  
`Use Domain for Authentication` | _Optional_ If selected, the integration uses domain as a part of the authentication credentials, such as `user@domain`. Selected by default.  
`Unread Emails Only` | _Optional_ If selected, cases are created only from unread emails. Not selected by default.  
`Mark Emails as Read` | _Optional_ If selected, emails are marked as read after ingesting. Not selected by default.  
`Max Days Backwards` | _Optional_ The number of days before the first connector iteration to retrieve the emails from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process running current script.The default value is 30 seconds.  
`Folder Name` | _Optional_ A folder name to run a search through. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. The default value is `Inbox`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Encode Data as UTF-8` | _Optional_ If selected, the integration encodes the email data with UTF-8. It is recommended to select this parameter.Selected by default.  
`Attach EML or MSG File to the Case Wall` | _Optional_ If selected, the integration attaches the forwarded EML or MSG file to the Case wall in Google SecOps.Not selected by default.  
`Exclusion Body Regex` | _Optional_ A regular expression to exclude emails whose body matches the provided value. For example, the `'([N|n]ewsletter)|([O|o]ut of office)'` regular expression excludes all emails containing the _Newsletter_ or _Out of office_ keywords.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
`Extract urls from HTML email part?` | _Optional_ If selected, the connector attempts to extract URLs from the HTML part of the email. This parameter also allows connector to extract complex URLs, but not the URLs from the plain text part of email.Extracted URLs are available in the `urls_from_html_part` event field. Not selected by default.  
  
#### Connector rules

  * The **Exchange EML Connector** doesn't support blocklist and dynamic list rules.

  * The **Exchange EML Connector** supports proxies.




### Exchange Mail Connector

**Warning:** This connector is outdated. We recommend using **Exchange Mail Connector v2** and **Exchange Mail Connector v2 with OAuth** instead.

Use the **Exchange Mail Connector** to communicate with the Exchange server and search for emails in near real time and forward them for translating and contextualizing as alerts in Google SecOps cases.

This section refers to communicating with a Microsoft Exchange 2007-2019 Server or Microsoft 365 using Exchange Web Services (EWS) and explains how Google SecOps interacts with the Exchange Mail interface and the assisted workflows and activities within the application.

The **Exchange Mail Connector** enables retrieving emails from the configured Exchange server that scans each server and subsequently creates new cases. At least one initial email occurrence is included in each scenario. The main difference is that **Exchange Mail connector** removes emails and generates events that parse the EML or MSG data in the Exchange server's original emails. 

#### Known restrictions

  1. Microsoft 365 and basic authentication.

     * The **Exchange Mail Connector** doesn't support basic authentication anymore and cannot be used with Microsoft 365. For Microsoft 365, use the **Exchange Mail Connector v2 with OAuth**.
  2. The **Exchange Mail Connector** specifics are as follows:

     * The connector creates Google SecOps alerts only from original received emails that are contained in the mailbox.

     * The connector ignores attached EML and MSG files.




#### Connector inputs

The **Exchange Mail Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `device_product`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).the default value is `event_name`.  
`Server IP` | _Required_ An IP address of the server to connect to.  
`Domain` | _Required_ A domain value to use for authentication.  
`Username` | _Required_ A username for the mailbox to pull emails from, like `user@example.com`.  
`Password` | _Required_ A password for the email mailbox to pull emails from.   
`Mail Address` | _Required_ An email address for the mailbox to monitor. The default value is `Inbox`.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Exchange server is valid.Not selected by default.   
`Use Domain for Authentication` | _Optional_ If selected, the domain is used as a part of the authentication credentials, such as `user@domain`. Selected by default.  
`Unread Emails Only` | _Optional_ If selected, the integration creates cases only from unread emails. Selected by default.  
`Mark Emails as Read` | _Optional_ If selected, the integration marks all ingested emails as read. Not selected by default.  
`Max Days Backwards` | _Optional_ The number of days before the first connector iteration to retrieve the emails from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process running current script.the default value is 30 seconds.  
`Attach Original EML` | _Optional_ If selected, the original email is attached to the case as an EML file.Not selected by default.  
`Folder Name` | _Optional_ A folder name to run a search through. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. The default value is `Inbox`.  
`Environment Field Name` | _Optional_ A name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Exclusion Subject Regex` | _Optional_ A regular expression to exclude emails with a subject matching the provided value.For example, the `([N|n]ewsletter)|([O|o]ut of office)` regular expression excludes all emails containing the _Newsletter_ or _Out of office_ keywords in their email subject.  
`Exclusion Body Regex` | _Optional_ A regular expression to exclude emails with a body matching the provided value. For example, the `([N|n]ewsletter)|([O|o]ut of office)` regular expression excludes all emails containing the _Newsletter_ or _Out of office_ keywords in their email body.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Extract urls from HTML email part?` | _Optional_ If selected, the connector attempts to extract URLs from the HTML part of the email. This parameter lets the connector extract complex URLs, but not the URLs from the plain text part of email.Extracted URLs are available in the `urls_from_html_part` event field. Not selected by default.  
  
#### Configure dynamic list rules

In the dynamic list section, to extract specific values from emails using regular expressions, add a rule in the following format:
    
    
    '<var>FIELD_NAME</var>': '<var>REGULAR_EXPRESSION</var>'
    

For example, to extract the message ID from email, enter the following rule:

`message-id: (?<=Message-ID: ).*`

#### Connector rules

  * The **Exchange Mail Connector** supports proxies.

  * The **Exchange Mail Connector** doesn't support the blocklist rule.

  * The Exchange integration uses the dynamic list section to define regular expressions and enable the following:

    * Parse email content.
    * Add specific fields based on the regular expression that match the email event.



### Exchange Mail Connector v2

Use the **Exchange Mail Connector v2** to connect to the mail server and check for new emails in a specific mailbox.

If a new email appears, it triggers the connector to create and ingest in Google SecOps a new alert that contains information from the new email.

If there are no new emails, the **Exchange Mail Connector v2** completes the current iteration and stands by for a defined period before the upcoming iteration run.

#### Connector iteration flow

After each run, the **Exchange Mail Connector v2** updates the timestamp file with the date and time of the last run. The **Exchange Mail Connector v2** extracts actionable information for a case from the email as a mail object technical result, such as, but not limited to:

  * Email sender and recipient.
  * Email subject.
  * Email body.
  * URLs in the email.
  * Attachments, if any.



After the **Exchange Mail Connector v2** creates the alerts (cases) to ingest into Google SecOps, the connector iteration completes.

Based on the case data provided by the **Exchange Mail Connector v2** , the Google SecOps server runs ETL procedures to ingest new alerts and create or update cases. If there are related playbooks defined, Google SecOps executes playbooks to enrich the case, generate insights, and perform automatic actions.

#### Work with Alert Name Template and Case Name Template

The `Alert Name Template` and `Case Name Template` parameters let you overwrite the way alert and case name are created. Only the first alert sets the case or alert name, all other subsequent alerts don't affect the name.

The example of a Google SecOps event is as follows:
    
    
    {
        "event": {
            "type": "Phishing"
            "name": "Example Event",
            "id": "1"
        }
    }
    

To create a custom name for a Google SecOps alert, use the following template:
    
    
    [EVENT_TYPE] - [EVENT_NAME]
    

For example, to create a Google SecOps alert named **Phishing – Example Event** , the template is as follows:
    
    
    [Phishing] - [Example Event]
    

#### Connector inputs

In **Exchange Mail Connector v2** , the following parameters can affect email processing:

  * `Original Received Mail Prefix`
  * `Attached Mail File Prefixes`
  * `Create a Separate Siemplify Alert per Attached Mail File?`



To map the `to` and `from` fields of the processed emails, the connector creates the following sets of fields:

  1. Regular `to` and `from` fields that contain email addresses in the following format: `email@example`.

  2. `to_raw` and `from_raw` fields that contain only email address as a value in the following format: `email@example`.




The **Exchange Mail Connector v2** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ the name of the field where the product name is stored.The default value is `device_product`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).the default value is `event_name`.  
`Mail Server Address` | _Required_ A mail server IP address to connect to.When connecting to Microsoft 365, set the server address to `outlook.office365.com`.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Exchange server is valid. Not selected by default.  
`Mail Address` | _Required_ An email address for the mailbox to monitor. The default value is `Inbox`.  
`Use Domain for Authentication` | _Optional_ If selected, the domain is used as a part of the authentication credentials, such as `user@domain`.Selected by default.  
`Domain` | _Required_ A domain value to use for authentication.  
`Username` | _Required_ The username for the mailbox to pull emails from, like `user@example.com`.  
`Password` | _Required_ The password for the email mailbox to pull emails from.  
`Unread Emails Only` | _Optional_ If selected, cases are created only from unread emails. Selected by default.  
`Mark Emails as Read` | _Optional_ If selected, emails are marked as read after ingesting. Not selected by default.  
`Offset Time In Days` | _Required_ The number of days before the first connector iteration to retrieve the emails from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time. The default value is 5.  
`Max Emails Per Cycle` | _Required_ The number of emails to retrieve in a single connector iteration. the default value is 10.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Headers to add to events` | _Optional_ A comma-separated string that specifies which email headers to add to events.You can provided values as exact matches or set as a regular expression.  
`Email Exclude Pattern` | _Optional_ A regular expression to exclude specific emails from ingesting.This parameter works with both subject and body part of email. You can use this parameter to exclude mass broadcasted emails like news from ingesting.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process running current script.The default value is 60 seconds.  
`Folder to check for emails` | _Required_ An email folder to search for the emails. This parameter accepts a comma-separated list of folders. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. This parameter is case-sensitive. The default value is `Inbox`.  
`Attach Original EML` | _Optional_ If selected, the integration attaches the original email to the case as an EML file.Not selected by default.  
`Fetch Backwards Time Interval (minutes)` | _Optional_ An interval that the connector uses to retrieve events from the configured period in minutes before now. This parameter value is a timestamp of the last connector iteration.Adjust this value accordingly to the environment, for example, 60 minutes or less. The default value is 0.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Extract urls from HTML email part?` | _Optional_ If selected, the connector attempts to extract URLs from the HTML part of the email. This parameter lets connector extract complex URLs, but not the URLs from the plain text part of email.Extracted URLs are available in the `urls_from_html_part` event field. Not selected by default.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Original Received Mail Prefix` | _Optional_ A prefix to add to the extracted event keys, for example, _to_ , _from_ , or _subject_ from the original email received in the monitored mailbox.The default value is `orig`.  
`Attached Mail File Prefix` | _Optional_ A prefix to add to the extracted event keys, for example, _to_ , _from_ , or _subject_ from the attached email file received in the monitored mailbox.The default value is `attach`.  
`Create a Separate Siemplify Alert per Attached Mail File?` | _Optional_ If selected, the connector creates multiple alerts, with one alert for every attached email file.If you select this parameter, Google SecOps processes emails with multiple attached files and creates entities from attached files. Not selected by default.  
`Case Name Template` | _Optional_ A custom case name.When you configure this parameter, the connector adds a new key called _custom_case_name_ to the Google SecOps event. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. The connector processes only keys that contain the string value.  
`Alert Name Template` | _Optional_ A custom alert name. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. Only keys containing the string value are handled. If you provide no value or an invalid template, the connector uses the default alert name.  
`Email Padding Period (minutes)` | _Optional_ A period for the connector to retrieve emails before the latest timestamp.  
`URL Regex` | _Required_ The regular expression connector used to parse URLs from the processed emails.   
`Event Fields to Exclude` | _Optional_ A comma-separated list of fields to exclude from events.   
`Exclude Attachments` | _Optional_ If selected, the connector doesn't ingest email attachments or add them to cases.   
  
#### Connector rules

  * The **Exchange Mail Connector v2** supports proxy.

  * The **Exchange Mail Connector v2** doesn't support the blocklist rule.

  * The Exchange integration uses the dynamic list section for defining regular expressions to enable the following:

    * Parse email content.
    * Add specific fields based on the regular expression matches to the email event.



### Exchange Mail Connector v2 with OAuth Authentication

Use the **Exchange Mail Connector v2 with OAuth** to monitor specific mailboxes on Microsoft 365 mail servers that require OAuth authentication. You can use the **Get Authorization** and **Generate Token** actions to obtain refresh token required for the connector configuration.

To run the **Exchange Mail Connector v2 with OAuth** , configure the integration to support OAuth authentication.

#### Work with Alert Name Template and Case Name Template

The `Alert Name Template` and `Case Name Template` parameters enable you to overwrite the way alert and case name is created.

The example of a Google SecOps event is as follows:
    
    
    {
        "event": {
            "type": "Phishing"
            "name": "Example Event",
            "id": "1"
        }
    }
    

To create a custom name for a Google SecOps alert, use the following template:
    
    
    [EVENT_TYPE] - [EVENT_NAME]
    

For example, to create a Google SecOps alert named **Phishing – Example Event** , the template is as follows:
    
    
    [Phishing] - [Example Event]
    

#### Connector inputs

In **Exchange Mail Connector v2 with OAuth** , the following parameters can affect email processing:

  * `Original Received Mail Prefix`
  * `Attached Mail File Prefixes`
  * `Create a Separate Siemplify Alert per Attached Mail File?`



To map the `to` and `from` fields of the processed emails, the connector creates two following sets of fields:

  1. Regular `to` and `from` fields that contain email addresses, such as `email@example`.

  2. `to_raw` and `from_raw` fields that contain only email address as a value, such as `email@example`.




The **Exchange Mail Connector v2 with OAuth** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `device_product`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `event_name`.  
`Mail Server Address` | _Required_ A mail server IP address to connect to.When connecting to Microsoft 365, set the server address to `outlook.office365.com`.  
`Mail Address` | _Required_ A mail address to use for the connector.  
`Client ID` | _Required_ For Microsoft 365 OAuth authentication, an application (client) ID of the Microsoft Entra application that you used for the integration.  
`Client Secret` | _Required_ For Microsoft 365 OAuth authentication, the client secret that you provided for the authentication flow.  
`Tenant (Directory) ID` | _Required_ For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra application that you used for the integration.  
`Refresh Token` | _Required_ For Microsoft 365 OAuth authentication, the refresh token obtained after generating a token.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Exchange server is valid.Not selected by default.  
`Unread Emails Only` | _Optional_ If selected, the integration creates cases only from unread emails. Not selected by default.  
`Mark Emails as Read` | _Optional_ If selected, the connector marks ingested emails as read. Not selected by default.  
`Offset Time In Days` | _Required_ The number of days before the first connector iteration to retrieve the emails from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time. The default value is 5 days.  
`Max Emails Per Cycle` | _Required_ The number of emails to retrieve in a single connector iteration. The default value is 10 emails.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Headers to add to events` | _Optional_ A comma-separated string that specifies which email headers to add to events.You can provided values as exact matches or set as a regular expression.  
`Email Exclude Pattern` | _Optional_ A regular expression to exclude specific emails from ingesting.This parameter works with both subject and body part of email. You can use this parameter to exclude mass broadcasted emails like news from ingesting.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process running current script.The default value is 60.  
`Folder to check for emails` | _Required_ An email folder to search for the emails. This parameter accepts a comma-separated list of folders. The Exchange integration uses backslashes as separators to specify subfolders, such as `folder/subfolder1/subfolder2`. To avoid the timeout error or action failure, replace backslashes in folder or subfolder names with other characters like underscore. This parameter is case-sensitive. The default value is `Inbox`.  
`Attach Original EML` | _Optional_ If selected, the original email is attached to the case as an EML file.Not selected by default.  
`Fetch Backwards Time Interval (minutes)` | _Optional_ An interval that the connector uses to retrieve events from the configured period in minutes before now. This parameter value is a timestamp of the last connector iteration.Adjust this value accordingly to the environment, for example, 60 minutes or less. The default value is 0.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Extract urls from HTML email part?` | _Optional_ If selected, the connector attempts to extract URLs from the HTML part of the email. This parameter lets connector extract complex URLs, but not the URLs from the plain text part of email.Extracted URLs are available in the `urls_from_html_part` event field. Not selected by default.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Original Received Mail Prefix` | _Optional_ A prefix to add to the extracted event keys, for example, _to_ , _from_ , or _subject_ from the original email received in the monitored mailbox.The default value is `orig`.  
`Attached Mail File Prefix` | _Optional_ A prefix to add to the extracted event keys, for example, _to_ , _from_ , or _subject_ from the attached email file received in the monitored mailbox.The default value is `attach`.  
`Create a Separate Siemplify Alert per Attached Mail File?` | _Optional_ If selected, the connector creates multiple alerts, with one alert for every attached email file.If you select this parameter, Google SecOps processes emails with multiple attached files and creates entities from attached files. Not selected by default.  
`Case Name Template` | _Optional_ A custom case name.When you configure this parameter, the connector adds a new key called _custom_case_name_ to the Google SecOps event. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. The connector processes only keys that contain the string value.  
`Alert Name Template` | _Optional_ Parameter to set a custom alert name. A custom alert name. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. Only keys containing the string value are handled. If you provide no value or an invalid template, the connector uses the default alert name.  
`Email Padding Period (minutes)` | _Optional_ A period for the connector to retrieve emails before the latest timestamp.  
`Event Fields to Exclude` | _Optional_ A comma-separated list of fields to exclude from events.   
`Exclude Attachments` | _Optional_ If selected, the connector doesn't ingest email attachments or add them to cases.   
  
## Jobs

Before configuring jobs for the Exchange integration, make sure that your Google SecOps platform version supports them.

### Refresh Token Renewal Job

**Warning:** This job is supported only on Google SecOps platform version 6.2.35 and later. If you run this job on an earlier platform version, the job fails.

The goal of the **Refresh Token Renewal Job** is to periodically update the refresh token used in the integration.

By default, the refresh token expires every 90 days. It is recommended to run this job every 7 or 14 days to make sure that the refresh token is up to date.

#### Job inputs

The **Refresh Token Renewal Job** requires the following parameters:

Parameter | Description  
---|---  
`Integration Environments` | _Optional_ The integration environments which the job updates the refresh tokens for. This parameter accepts multiple values as a comma-separated string. Enclose individual values in quotation marks (`" "`).  
`Connector Names` | _Optional_ The connector names which the job updates the refresh tokens for. This parameter accepts multiple values as a comma-separated string. Enclose individual values in quotation marks (`" "`).  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
