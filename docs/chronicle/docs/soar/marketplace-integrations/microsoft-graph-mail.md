---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail/
title: Integrate Microsoft Graph Mail with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:48.005833+00:00
---

# Integrate Microsoft Graph Mail with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Microsoft Graph Mail with Google SecOps

Microsoft Graph Mail | [Microsoft Graph Mail Delegated](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail-delegated "View this page for the Microsoft Graph Mail Delegated integration")

This document explains how to integrate Microsoft Graph Mail with Google Security Operations (Google SecOps). 

## Before you begin

Before you configure the Microsoft Graph Mail integration:

  1. Create the Microsoft Entra application.

  2. Configure the API permissions for your application.

  3. Create a client secret.




### Create the Microsoft Entra application

To create the Microsoft Entra app, complete the following steps:

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the application.

  5. Click **Register**.

This document provides an example that uses a single-tenant setup. As this integration uses the OAuth 2.0 client credentials flow, no interactive user sign-in occurs. Therefore, a `Redirect URI` is not required. 

  6. Save the **Application (client) ID** and **Directory (tenant) ID** values to configure the Integration Parameters.




### Configure API permissions

To configure the API permissions for the integration, complete the following steps:

  1. In Azure portal, go to **API Permissions > Add a permission**.

  2. Select **Microsoft Graph > Application permissions**. 

  3. In the **Select Permissions** section, select the following required permissions:

     * `Mail.Read`
     * `Mail.ReadWrite`
     * `Mail.Send`
     * `User.Read`
     * `Directory.Read.All`
**Note:** This integration supports Shared Mailboxes. By default, granting Application permissions allows the integration to read mailboxes across your entire tenant. To restrict access to specific shared mailboxes only, configure a [Microsoft Application Access Policy](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail#limit_application_access_to_specific_mailboxes).

  4. Click **Add permissions**.

  5. Click **Grant admin consent for` ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




### Limit Application Access to Specific Mailboxes

By default, applications with `Mail.ReadWrite` or `Mail.Send` application permissions have access to all mailboxes in your organization. To restrict the application's access to only specific mailboxes, configure **Application Access Policies** in Microsoft Exchange Online.

To configure **Application Access Policies** , complete the following steps:

  1. Connect to Exchange Online PowerShell:

     1. Open PowerShell as an administrator.

     2. Install the Exchange Online Management module (if not already installed):
            
            Install-Module -Name ExchangeOnlineManagement
            

     3. Connect to Exchange Online:
            
            Connect-ExchangeOnline
            

  2. Identify application ID and target mailboxes:

     1. Get your Microsoft Graph Mail application's **Client ID (Application ID)** from Azure AD.

     2. Identify the email addresses of the mailboxes you want the application to access. For easier management, create a mail-enabled security group in Azure AD and add these mailboxes as members.

  3. Create an Application Access Policy:

     1. Use the `New-ApplicationAccessPolicy` cmdlet to create a policy that restricts access to selected mailboxes.

     2. Optional: Restrict access to a specific security group of mailboxes:

        1. Replace `<Your_Application_ID>` with your application's Client ID.

        2. Replace `<Security_Group_Email_Address>` with the email address of the security group containing the allowed mailboxes.
    
    New-ApplicationAccessPolicy -AppId "<Your_Application_ID>" -PolicyScopeGroupId "<Security_Group_Email_Address>" -AccessRight RestrictAccess -Description "SOAR Graph Mail Access Policy"
    

  4. Verify the policy's effectiveness using the `Test-ApplicationAccessPolicy` cmdlet:
         
         Test-ApplicationAccessPolicy -AppId "<Your_Application_ID>" -Identity "user_email_to_test@yourdomain.com"
         

This command indicates whether the application has access to the specified mailbox based on the applied policies.




**Note:**

  * `OrganizationManagement` or `Security Administrator` permissions in Exchange Online are required to create these policies.

  * Policy changes typically take effect within 30 minutes.

  * After applying the policy, the application can access only the permitted mailboxes. Attempts to access others will return an `Access Denied` error. 




### Create a client secret

To create a client secret, complete the following steps:

  1. Go to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the **Secret ID** parameter value when you configure the integration. The client secret value is only displayed once. 


**Important:** If you modify the Microsoft Graph **Application Permissions** after configuring this integration, regenerate the client secret if necessary and update the integration configuration. Existing credentials won't automatically receive newly granted permissions.

## Integration parameters

The Microsoft Graph Mail integration requires the following parameters: Parameter | Description  
---|---  
`Azure AD Endpoint` | Required.The Microsoft Entra ID endpoint to use in the integration.The value can be different for different tenant types. The default value is `https://login.microsoftonline.com`.  
`Microsoft Graph Endpoint` | Required.The Microsoft Graph endpoint to use in the integration.The value can be different for different tenant types. The default value is `https://graph.microsoft.com`.  
`Client ID` | Required.The client (application) ID of the Microsoft Entra application to use in the integration.  
`Secret ID` | Required.The client secret value of the Microsoft Entra application to use in the integration.  
`Tenant` | Required.The Microsoft Entra ID (tenant ID) value.  
`Default Mailbox` | Required.The mailbox to use in the integration.  
`Mail Field Source` | Optional.If selected, the integration retrieves the mailbox address from the user details `mail` attribute. If not selected, the integration retrieves the mailbox address from the `userPrincipalName` field.Not selected by default.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the Microsoft Graph server. Enabled by default.  
`Base64 Encoded Private Key` | Optional. The Base64-encoded private key used to decrypt S/MIME encrypted emails. If a value is provided, you must also provide the `Base64 Encoded Certificate`.  
`Base64 Encoded Certificate` | Optional. The Base64-encoded certificate used to decrypt S/MIME encrypted emails. If a value is provided, you must also provide the `Base64 Encoded Private Key`.  
`Base64 Encoded CA certificate` | Optional. The Base64-encoded trusted CA certificate for signature verification. If no value is provided, signature verification for incoming signed emails fails unless `Bypass S/MIME Signature Verification` is enabled.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Block Domain

Use the **Block Domain** action to block specific email domains by adding them to a message rule in the target mailbox. If the rule doesn't exist, it's created.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed. 

#### Action inputs

The **Block Domain** action requires the following parameters:

Parameter | Description  
---|---  
`Domains` | Optional.Comma-separated list of sender domains to block (for example, `example.com`). Domains manually input in this field and domains dynamically extracted from entities work together and will both be added to the rule conditions.  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes where the message rule will be added. Can be a comma-separated list of user principal names.  
`Rule Name` | Required. Default is `Google SecOps - Blocked Domains`.Name of the message rule to add these domains into. If the rule exists, it will be updated.  
`Action` | Required. Default is `Select One`.Action that should be taken for these domains. Possible values: `Select One`, `Move To Junk`, `Delete`. `Move To Junk` will move them to the Junk Email folder, and `Delete` will route them to Deleted Items. `Select One` preserves the existing action if the rule exists.  
`How many mailboxes to process in a single batch` | Optional. Default is `20`.Specify how many mailboxes the action should process in a single batch.  
  
#### Action outputs

The **Block Domain** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Block Domain** action:
    
    
    {
        "status": "Success",
        "mailbox": "user@domain.com",
        "blocked_domain": "malicious-domain.com"
    }
    

##### Output messages

The **Block Domain** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully blocked domain DOMAIN for mailbox MAILBOX.` | Action succeeded.  
`Failed to block domain DOMAIN for mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Block Domain** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Block Sender

Use the **Block Sender** action to block specified email senders by adding them to a message rule in the target mailbox. If the rule does not exist, it will be created.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed. 

#### Action inputs

The **Block Sender** action requires the following parameters:

Parameter | Description  
---|---  
`Senders` | Optional.Comma-separated list of sender email addresses to block. Senders manually input in this field and senders dynamically extracted from entities work together and will both be added to the rule conditions.  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes where the message rule will be added. Can be a comma-separated list of user principal names.  
`Rule Name` | Required. Default is `Google SecOps - Blocked Senders`.Name of the message rule to add these senders into. If the rule exists, it will be updated.  
`Action` | Required. Default is `Select One`.Action that should be taken for these senders. Possible values: `Select One`, `Move To Junk`, `Delete`. `Move To Junk` will move them to the Junk Email folder, and `Delete` will route them to Deleted Items. `Select One` preserves the existing action if the rule exists.  
`How many mailboxes to process in a single batch` | Optional. Default is `20`.Specify how many mailboxes the action should process in a single batch.  
  
#### Action outputs

The **Block Sender** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Block Sender** action:
    
    
    [
      {
        "Entity": "user@example.com",
        "EntityResult": {
          "successful_mailboxes": [
            "target@example.com"
          ],
          "failed_mailboxes": []
        }
      }
    ]
    

##### Output messages

The **Block Sender** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully blocked sender SENDER for mailbox MAILBOX.` | Action succeeded.  
`Failed to block sender SENDER for mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Block Sender** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Email

You can use the **Delete Email** action to delete one or more emails from a mailbox. This action deletes emails based on your search criteria. With the appropriate permissions, the **Delete Email** action can move emails into different mailboxes.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Delete Email** action requires the following parameters:

Parameter | Description  
---|---  
`Delete In Mailbox` | Required.The default mailbox where to run the delete operation. If permissions allow, the action can also search in other mailboxes. This parameter accepts multiple values as a comma-separated string.  
`Folder Name` | Required. A mailbox folder to search for email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Mail IDs` | Optional A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for. If this parameter is provided, the search ignores the `Subject Filter` and `Sender Filter` parameters.  
`Subject Filter` | Optional A filter condition that specifies the email subject to search.  
`Sender Filter` | Optional A filter condition that specifies the sender of requested emails.  
`Timeframe (Minutes)` | Optional A filter condition that specifies the timeframe in minutes to search for emails.  
`Only Unread` | Optional If selected, the action searches only for unread emails. Not selected by default.  
`How many mailboxes to process in a single batch` | OptionalThe number of mailboxes to process in a single batch (single connection to the mail server). The default value is `25`.  
  
#### Action outputs

The following table describes the output types associated with the **Delete Email** action:

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

The **Delete Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully deleted emails in the following mailboxes: MAILBOX_NAME: DELETED_EMAILS_NUMBER` `Mailbox MAILBOX was not found.` | Action succeeded.  
`Action was not able to find any emails based on the specified search criteria.` `Action failed to delete any emails because the provided mailbox folder name was not found in the mailbox(es): MAILBOX_NAME, MAILBOX_FOLDER` `Failed to find any of the provided mailboxes: MAILBOX_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Delete Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Inbox Rules

Use the **Delete Inbox Rules** action to delete a specified inbox message rule for the given Mailboxes. This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed. 

#### Action inputs

The **Delete Inbox Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes where the message rule will be deleted from. Can be a comma-separated list of user principal UPNs.  
`Rule Name` | Required.The exact name of the inbox message rule to delete.  
`How many mailboxes to process in a single batch` | Optional. Default is `25`.Specify how many mailboxes the action should process in a single batch. If nothing is provided, a default value of 25 will be used.  
  
#### Action outputs

The **Delete Inbox Rules** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Delete Inbox Rules** action:
    
    
    {
        "deleted_rule": [
            "New test cases"
        ],
        "successful_mailboxes": [
            "labops1@siemplifycyarx.onmicrosoft.com"
        ],
        "failed_mailboxes": [
            "user2@example.com",
            "user3@example.com"
        ]
    }
    

##### Output messages

The **Delete Inbox Rules** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully deleted inbox rule RULE_NAME from mailbox MAILBOX.` | Action succeeded.  
`Failed to delete inbox rule RULE_NAME from mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Delete Inbox Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Download Attachments From Email

Use the **Download Attachments From Email** action to download attachments from emails based on the criteria provided.

This action doesn't run on Google SecOps entities.

This action is asynchronous. If necessary, adjust the script timeout value in the Google SecOps IDE.

The action replaces the `\` forward slash or`/`backslash characters in the names of the downloaded attachments with the`_` underscore character.

#### Action inputs

The **Download Attachments From Email** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | Required.The default mailbox where the search operation runs. If permissions allow, the action can also search in other mailboxes. This parameter accepts multiple values as a comma-separated string.  
`Folder Name` | Required.A mailbox folder where to run the search. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Download Destination` | Required.A storage type to save the downloaded attachments. By default, the action attempts to save the attachment to the Cloud Storage bucket. Saving an attachment to the local file system is a fallback option.The possible values are `GCP Bucket` and `Local File System`. The default value is `GCP Bucket`.  
`Download Path` | Required.A path to download attachments.When saving attachments to the Cloud Storage bucket or a local file system, the action expects you to specify the download path in the Unix-like format, such as `/tmp/test`.  
`Mail IDs` | Optional A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for. If this parameter is provided, the search ignores the `Subject Filter` and `Sender Filter` parameters.  
`Subject Filter` | Optional A filter condition that specifies the email subject to search for. This filter uses the `contains` logic.  
`Sender Filter` | Optional A filter condition that specifies the sender of requested emails. This filter uses the `equals` logic.  
`Download Attachments From EML` | Optional If selected, the action downloads attachments from EML files. Not selected by default.  
`Download attachments to unique path?` | OptionalIf selected, the action downloads attachments to the unique path provided in the `Download Path` parameter field to avoid overwriting any previously downloaded attachments.Not selected by default.  
`How many mailboxes to process in a single batch` | OptionalThe number of mailboxes to process in a single batch (single connection to the mail server). The default value is `25`.  
  
#### Action outputs

The **Download Attachments From Email** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Download Attachments From Email** action:
    
    
    [
        {
            "attachment_name": "name1.png",
            "downloaded_path": "file_path/name1.png"
        },
        {
            "attachment_name": "name2.png",
            "downloaded_path": "file_path/name2.png"
        }
    ]
    

##### Output messages

The **Download Attachments From Email** action provides the following output messages:

Output message | Message description  
---|---  
`Downloaded  NUMBER_OF_ATTACHMENTS attachments. Files: PATHS.` `Failed to find emails in  MAILBOX with the following mail ids: EMAIL_IDS.` `In the mailboxes listed below, emails were found, but there were no attachments to download. Affected mailboxes: MAILBOXES. Mail IDs without attachments to download:  LIST_OF_EMAIL_IDS attachments.` | Action succeeded.  
`Failed to find any emails using the provided criteria!` `Failed to find any of the provided mailboxes: MAILBOXES` `Action failed to run because the provided mailbox folder name FOLDER_NAME was not found in the mailbox MAILBOX`. `Error executing action. Reason:  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Download Attachments From Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Extract Data From Attached EML

Use the **Extract Data From Attached EML** action to retrieve data from the email EML attachments and return it in the action results. This action supports the `.eml`, `.msg`, and `.ics` file formats.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Extract Data From Attached EML** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | Required.The default mailbox where the search operation runs. If permissions allow, the action can also search in other mailboxes. This parameter accepts multiple values as a comma-separated string.  
`Folder Name` | OptionalA mailbox folder where to run the search. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Mail IDs` | Required. A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for.  
`Regex Map JSON` | OptionalA JSON definition that contains regular expressions to apply to the attached email file and generate additional key values in the action JSON result. The example of this parameter value is as follows:
    
    
    {ips: \\b\\\\d{1,3}\\\\.\\\\d{1,3}\\\\.\\\\d{1,3}\\\\.\\\\d{1,3}\\b}
          
  
#### Action outputs

The **Extract Data From Attached EML** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Extract Data From Attached EML** action:
    
    
    [
        {
            "type": "EML",
            "subject": "examplesubject",
            "from": "sender@example.com",
            "to": "user1@example.com,user2@example.com",
            "date": "Thu,4Jul202412:11:29+0530",
            "text": "text",
            "html": "<p>example-html</p>",
            "regex": {},
            "regex_from_text_part": {},
            "id": "ID",
            "name": "example.eml"
        },
        {
            "type": "MSG",
            "subject": "examplesubject",
            "from": "user@example.com",
            "to": "user1@example.com,user2@example.com",
            "date": "Thu,4Jul202412:11:29+0530",
            "text": "text",
            "html": "<p>examplehtml</p>",
            "regex": {},
            "regex_from_text_part": {},
            "id": "ID",
            "name": "example.msg"
        },
        {
            "type": "ICS",
            "subject": "examplesubject",
            "from": "sender@example.com",
            "to": "user1@example.com,user2@example.com",
            "date": "Thu,4Jul202412:11:29+0530",
            "text": "text",
            "html": "<p>example-html</p>",
            "regex": {},
            "regex_from_text_part": {},
            "id": "ID",
            "name": "example.ics"
        }
    ]
    

##### Output messages

The **Extract Data From Attached EML** action provides the following output messages:

Output message | Message description  
---|---  
`Extracted data from  ATTACHMENT_NAMES attached email files. Files: PATHS` `Failed to find emails in  MAILBOX with the following mail ids:  MAIL_ID_LIST` | Action succeeded.  
`Failed to find any emails using the provided criteria!` `Failed to find any of the provided mailboxes: MAILBOX_LIST` `Action failed to run because the provided mailbox folder name MAILBOX_FOLDER was not found in the mailbox MAILBOX` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Extract Data From Attached EML** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Forward Email

Use the **Forward Email** action to forward emails that include previous threads. With the appropriate permissions, this action can send emails from a mailbox different than the one specified in the integration configuration.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Forward Email** action requires the following parameters:

Parameter | Description  
---|---  
`Send From` | Required.An optional email address from which to send an email, if permissions allow.By default, the email is sent from the default mailbox specified in the integration configuration.  
`Folder Name` | Optional A mailbox folder to search for emails. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Mail ID` | Required. The ID of the email to forward.  
`Subject` | Required. The email subject.  
`Send to` | Required. A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | Optional A comma-separated list of email addresses for the email CC field. The format is the same as for the `Send to` parameter.  
`BCC` | Optional A comma-separated list of email addresses for the email BCC field. The format is the same as for the `Send to` parameter.  
`Attachments Paths` | Optional A comma-separated list of paths for file attachments stored on the server, such as `/FILE_DIRECTORY/file.pdf`, `/FILE_DIRECTORY/image.jpg`.  
`Mail content` | Required. The email body.  
  
#### Action outputs

The following table describes the output types associated with the **Forward Email** action:

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

The **Forward Email** action provides the following output messages:

Output message | Message description  
---|---  
`Email with message ID  MAIL_ID was forwarded successfully.` | Action succeeded.  
`Error executing action "Forward Email" because the provided mail id EMAIL_ID was not found. ` `Action failed to delete any emails because the provided mailbox folder name was not found in the mailbox(es): MAILBOX: MAILBOX_FOLDER` `Action failed to run because specified attachments were not found: ATTACHMENTS_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Forward Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Mailbox Account Out Of Facility Settings

Use the **Get Mailbox Account Out Of Facility Settings** action to retrieve the mailbox account out of facility (OOF) settings for the Google SecOps `User` entity provided.

The **Get Mailbox Account Out Of Facility Settings** action uses the beta version of Microsoft Graph API.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Get Mailbox Account Out Of Facility Settings** action provides the following outputs:

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

The following example shows the JSON result output received when you use the **Get Mailbox Account Out Of Facility Settings** action:
    
    
    {
       "@odata.context": "https://graph.microsoft.com/beta/$metadata#communications/presences/$entity",
       "id": "ID",
       "availability": "Offline",
       "activity": "Offline",
       "statusMessage": null,
       "outOfOfficeSettings": {
           "message": "\n\nOut Of Facility111\n",
           "isOutOfOffice": true
       }
    }
    

##### Output messages

The **Get Mailbox Account Out Of Facility Settings** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned OOF settings for ENTITY_ID.` `Failed to find the following usernames in Office 365 service: USERNAME_LIST.` | The action succeeded.  
`Error executing action "Add Identity Protection Detection Comment". Reason:  ERROR_REASON` `Action wasn't able to find OOF settings for ENTITY_ID.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when you use the **Get Mailbox Account Out Of Facility Settings** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Rules

Use the **List Rules** action to list all message rules for a specific mailbox using the Microsoft Graph API.

#### Action inputs

The **List Rules** action requires the following parameters:

Parameter | Description  
---|---  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes to list rules for. Can be a comma-separated list of user principal names.  
`Rule Name` | Optional.Filter by the display name of the rule.  
`Limit` | Optional. Default is `20`.Limit the number of rules to return per mailbox.  
  
#### Action outputs

The **List Rules** action provides the following outputs:

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

The **List Rules** action provides execution details on the case wall table.

##### JSON result

The following example describes the JSON result output received when you use the **List Rules** action:
    
    
    [
      {
        "mailbox": "user@example.com",
        "rules": [
          {
            "id": "AAMkAD...",
            "displayName": "Google SecOps - Blocked Senders",
            "sequence": 1,
            "isEnabled": true
          }
        ]
      }
    ]
    

##### Output messages

The **List Rules** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched NUMBER_OF_RULES rules for mailbox MAILBOX.` | Action succeeded.  
`Failed to fetch rules for mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Rules** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Mark Email as Junk

Use the **Mark Email as Junk** action to mark emails as junk in a specified mailbox. This action adds the email sender to the list of blocked senders and moves the message to the **Junk Email** folder.

The **Mark Email as Junk** action uses the beta version of Microsoft Graph API.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Mark Email as Junk** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | Required.A mailbox where to search for email.By default, the action attempts to search for the email in the default mailbox that you specified in the integration configuration. To execute a search in other mailboxes, configure appropriate permissions for the action. This parameter accepts multiple values as a comma separated string.  
`Folder Name` | Required.A mailbox folder where to search for email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`. The default value is `Inbox`.  
`Mail IDs` | Required.The IDs or `internetMessageId` values of the mails to mark as junk.This parameter accepts multiple values as a comma-separated string.  
  
#### Action outputs

The **Mark Email as Junk** action provides the following outputs:

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

The **Mark Email as Junk** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully marked the email as junk.` `Failed to find email with ID ID in MAILBOX. ` `Mailbox MAILBOX was not found.` | The action succeeded.  
`Error executing action "Mark Email as Junk". Reason: ERROR_REASON` `Failed to find any emails based on provided parameters!` `Action failed to run because the provided mailbox folder name MAILBOX_FOLDER was not found in the mailbox MAILBOX.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when you use the **Mark Email as Junk** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Mark Email as Not Junk

Use the **Mark Email as Not Junk** action to mark emails as not junk in a specific mailbox. This action removes the sender from the list of blocked senders and moves the message to the **Inbox** folder.

The **Mark Email as Not Junk** action uses the beta version of Microsoft Graph API.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Mark Email as Not Junk** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | Required.A mailbox where to search for an email.By default, the action attempts to search for the email in the default mailbox that you specified in the integration configuration. To execute a search in other mailboxes, configure appropriate permissions for the action. This parameter accepts multiple values as a comma separated string.  
`Folder Name` | Required.A mailbox folder where to search for email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Mail IDs` | Required.The IDs or `internetMessageId` values of the mails to mark as junk.This parameter accepts multiple values as a comma separated string.  
  
#### Action outputs

The **Mark Email as Not Junk** action provides the following outputs:

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

The **Mark Email as Not Junk** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully marked the email as not junk.` `Failed to find email with ID ID in MAILBOX. ` `Mailbox MAILBOX was not found.` | The action succeeded.  
`Error executing action "Mark Email as Not Junk". Reason: ERROR_REASON` `Failed to find any emails based on provided parameters!` `Action failed to run because the provided mailbox folder name MAILBOX_FOLDER was not found in the mailbox MAILBOX.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when you use the **Mark Email as Not Junk** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Move Email To Folder

Use the **Move Email To Folder** action to move one or multiple emails from the source email folder to the other folder in the mailbox. With the appropriate permissions, this action can move emails to other mailboxes different from the one that is provided in the integration configuration.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

To configure the **Move Email To Folder** action, use the following parameters:

Parameter | Description  
---|---  
`Move In Mailbox` | Required.The default mailbox where the move operation runs. If permissions allow, the action can also search in other mailboxes. This parameter accepts multiple values as a comma-separated string.   
`Source Folder Name` | Required.A source folder from where to move the email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Destination Folder Name` | Required.A destination folder to move the email. Provide the parameter value in the following format: `Inbox/folder_name/subfolder_name`. This parameter is case-insensitive.  
`Mail IDs` | Optional A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for. If this parameter is provided, the search ignores the `Subject Filter` and `Sender Filter` parameters.  
`Subject Filter` | Optional A filter condition that specifies the email subject to search for. This filter uses the `contains` logic.  
`Sender Filter` | Optional A filter condition that specifies the sender of requested emails. This filter uses the `equals` logic.  
`Timeframe (Minutes)` | Optional A filter condition that specifies the timeframe, in minutes, to search for emails.  
`Only Unread` | Optional If selected, the action searches only for unread emails. Not selected by default.  
`How many mailboxes to process in a single batch` | OptionalThe number of mailboxes to process in a single batch (single connection to the mail server). The default value is `25`.  
  
#### Action outputs

The following table describes the output types associated with the **Move Email To Folder** action:

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

The **Move Email To Folder** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully moved emails in the following mailboxes: MAILBOX: MOVED_EMAILS_NUMBER` `Mailbox MAILBOX was not found.` | Action succeeded.  
`Action was not able to find any emails based on the specified search criteria.` `Action failed to move any emails because the provided source folder was not found in the mailbox(es): MAILBOX_NAME, MAILBOX_FOLDER` `Action failed to move any emails because the provided destination folder was not found in the mailbox(es): MAILBOX_NAME, MAILBOX_FOLDER` `Failed to find any of the provided mailboxes: MAILBOX_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Move Email To Folder** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to the Microsoft Graph mail service.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The following table describes the output types associated with the **Ping** action:

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Microsoft Graph mail service with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Microsoft Graph mail service! Error is ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Block Domain

Use the **Remove Block Domain** action to remove specified email domains from a message rule in the target mailbox. If the rule becomes empty, it will be deleted.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed. 

#### Action inputs

The **Remove Block Domain** action requires the following parameters:

Parameter | Description  
---|---  
`Domains` | Optional.Comma-separated list of sender domains to remove (for example, `example.com`). Domains manually input in this field and domains dynamically extracted from entities work together and will both be removed from the rule conditions.  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes where the message rule exists. Can be a comma-separated list of user principal names.  
`Rule Name` | Required. Default is `Google SecOps - Blocked Domains`.Name of the message rule to remove these domains from.  
`How many mailboxes to process in a single batch` | Optional. Default is `20`.Specify how many mailboxes the action should process in a single batch.  
  
#### Action outputs

The **Remove Block Domain** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Remove Block Domain** action:
    
    
    [
      {
        "Entity": "example.com",
        "EntityResult": {
          "successful_mailboxes": [
            "user@example.com"
          ],
          "failed_mailboxes": []
        }
      }
    ]
    

##### Output messages

The **Remove Block Domain** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully removed domain DOMAIN from the blocked senders list for mailbox MAILBOX.` | Action succeeded.  
`Failed to remove domain DOMAIN from the blocked senders list for mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Block Domain** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Block Sender

Use the **Remove Block Sender** action to remove specified email senders from a message rule in the target mailbox. If the rule becomes empty, it will be deleted.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) as needed. 

#### Action inputs

The **Remove Block Sender** action requires the following parameters:

Parameter | Description  
---|---  
`Senders` | Optional.Comma-separated list of sender email addresses to remove. Senders manually input in this field and senders dynamically extracted from entities work together and will both be removed from the rule conditions.  
`Mailboxes` | Required. Default is `Default Mailbox`.Mailboxes where the message rule exists. Can be a comma-separated list of user principal names.  
`Rule Name` | Required. Default is `Google SecOps - Blocked Senders`.Name of the message rule to remove these senders from.  
`How many mailboxes to process in a single batch` | Optional. Default is `20`.Specify how many mailboxes the action should process in a single batch.  
  
#### Action outputs

The **Remove Block Sender** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Remove Block Sender** action:
    
    
    [
      {
        "Entity": "user@example.com",
        "EntityResult": {
          "successful_mailboxes": [
            "target@example.com"
          ],
          "failed_mailboxes": []
        }
      }
    ]
    

##### Output messages

The **Remove Block Sender** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully removed sender SENDER from the blocked senders list for mailbox MAILBOX.` | Action succeeded.  
`Failed to remove sender SENDER from the blocked senders list for mailbox MAILBOX. Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Block Sender** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Save Email To The Case

Use the **Save Email To The Case** action to save emails or email attachments to the Google SecOps Case Wall. With the appropriate permissions, this action can save emails from mailboxes other than the one provided in the integration configuration.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Save Email To The Case** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | Required.The default mailbox where the search operation runs. If permissions allow, the action can also search in other mailboxes.  
`Folder Name` | OptionalA mailbox folder where to search for email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.  
`Mail ID` | Required. A comma-separated list of email IDs to search. If you used the **Send Email** action to send emails, set the parameter value to either the `{SendEmail.JSONResult|id}` or `{SendEmail.JSONResult|internetMessageId}` placeholder.  
`Save Only Email Attachments` | OptionalIf selected, the action saves only attachments from the specified email.Not selected by default.  
`Attachment To Save` | OptionalIf the `Save Only Email Attachments` parameter is selected, the action only saves attachments specified by this parameter. This parameter accepts multiple values as a comma-separated string.  
`Base64 Encode` | OptionalIf selected, the action encodes the email file into the base64 format.Not selected by default.  
  
#### Action outputs

The following table describes the output types associated with the **Save Email To The Case** action:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall attachment

The following attachments are associated with the **Save Email To The Case** action:

  * `EMAIL_SUBJECT.eml`, if the action saves the email.

  * If the action saves the attachment, the attachment name contains a file extension, if any.




##### JSON result

The following example describes the JSON result output received when you use the **Save Email To The Case** action:
    
    
    {
        "id": "ID",
        "createdDateTime": "2024-02-16T14:10:34Z",
        "eml_info": "example_info",
        "lastModifiedDateTime": "2024-02-16T14:10:41Z",
        "changeKey": "cxsdjjh",
        "categories": [],
        "receivedDateTime": "2024-02-16T14:10:35Z",
        "sentDateTime": "2024-02-16T14:09:36Z",
        "hasAttachments": true,
        "internetMessageId": "INTERNET_MESSAGE_ID",
        "subject": "all attachments",
        "bodyPreview": "all the attachments",
        "importance": "normal",
        "parentFolderId": "PARENT_FOLDER_ID",
        "conversationId": "CONVERSATION_ID",
        "conversationIndex": "example-index",
        "isDeliveryReceiptRequested": false,
        "isReadReceiptRequested": false,
        "isRead": true,
        "isDraft": false,
        "webLink": "https://example.com/",
        "inferenceClassification": "focused",
        "body": {
            "contentType": "html",
            "content": "<html><head>example-html</head></html>"
        },
        "sender": {
            "emailAddress": {
                "name": "NAME",
                "address": "sender@example.com"
            }
        },
        "from": {
            "emailAddress": {
                "name": "NAME",
                "address": "user@example.com"
            }
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "name": "NAME",
                    "address": "recipient@example.com"
                }
            }
        ],
        "ccRecipients": [],
        "bccRecipients": [],
        "replyTo": [],
        "flag": {
            "flagStatus": "notFlagged"
        }
    }
    

##### Output messages

On a Case Wall, the **Save Email To The Case** action provides the following output messages:

Output message | Message description  
---|---  
`Email successfully saved!` `Successfully saved the following attachments: ATTACHMENTS_LIST` `The following attachments were not found in email with mail id: EMAIL_ID: ATTACHMENTS_LIST` | Action succeeded.  
`Mailbox MAILBOX_NAME was not found.` `Action failed to run because the provided mailbox folder name MAILBOX_FOLDER was not found in the mailbox MAILBOX_NAME` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Save Email To The Case** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Emails

Use the **Search Emails** action to execute an email search in the default mailbox based on the provided search criteria. With appropriate permissions, this action can run a search in other mailboxes.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Search Emails** action requires the following parameters:

Parameter | Description  
---|---  
`Search In Mailbox` | _Mandatory_ The default mailbox where the search operation runs. If permissions allow, the action can also search in other mailboxes. This parameter accepts multiple values as a comma-separated string.For complex searches against a significant number of mailboxes, use the [Exchange Extension Pack integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchange-extension).  
`Folder Name` | _Optional_ A mailbox folder in which to search for emails. To specify a subfolder, use the `/` forward slash (such as `Inbox/Subfolder`). Default is `Inbox`.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for. This filter uses the `contains` logic.  
`Sender Filter` | _Optional_ A filter condition that specifies the sender of requested emails. This filter uses the `equals` logic.  
`Recipient Filter` | _Optional_ A filter condition that specifies the recipient of requested emails.  
`Timeframe (minutes)` | _Optional_ A filter condition that specifies the period in minutes to search for emails.  
`Start Time` | _Optional_ Specify the start time for the email search in ISO 8601 format. This parameter has priority over `Timeframe (minutes)`.  
`End Time` | _Optional_ Specify the end time for the email search in ISO 8601 format. If not provided and `Start Time` is valid, this parameter uses the current time.  
`Body Regex Filter` | _Optional_ Specify a regular expression pattern to search within the body of the email.  
`Message IDs` | _Optional_ A comma-separated list of message IDs to search for. Note: this filter has priority over other filters.  
`Max Emails To Return` | _Optional_ The number of emails for the action to return. If you don't set a value, the API default value is used. Default is `10`.  
`Only Unread` | _Optional_ If selected, the action searches only for unread emails. Not selected by default.  
`Select All Fields For Return` | _Optional_ If selected, the action returns all available fields for the obtained email. Not selected by default.  
`How many mailboxes to process in a single batch` | _Optional_ The number of mailboxes to process in a single batch (single connection to the mail server). Default is `25`.  
`Search in all mailboxes` | _Optional_ If selected, the action searches across all accessible mailboxes. Not selected by default.  
`Limit the Amount of Information Returned in the JSON Result` | _Optional_ If selected, the amount of information returned by the action is limited only to key email fields. Not selected by default.  
`Disable the Action JSON Result` | _Optional_ If selected, the action doesn't return a JSON result. Not selected by default.  
  
#### Action outputs

The **Search Emails** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### Case wall table

The **Search Emails** action can generate the following table:

Table title: **Matching Mails**

Columns:

  * **Mail ID**
  * **Subject**
  * **Sender**
  * **Receivers**
  * **Received Date**



##### Script result

The following table lists the value for the script result output when using the **Search Emails** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Search Emails** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found emails in the following mailboxes: MAILBOX: FOUND_EMAILS_NUMBER``Mailbox MAILBOX was not found.``Action was not able to find any emails based on the specified search criteria.` | Action succeeded.  
`Failed to find any of the provided mailboxes: MAILBOX_LIST``Failed to execute action, the error is: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Send Email

Use the **Send Email** action to send emails from a specific mailbox to an arbitrary list of recipients.

This action can send either plain text or HTML-formatted emails. With appropriate permissions, the action can send emails from a mailbox different than the one specified in the integration configuration.

This action doesn't run on Google SecOps entities.

#### S/MIME configuration quick reference

Use the following reference to determine which S/MIME parameters to configure based on the security level of the outgoing email:

Desired email type | `Base64 Encoded Certificate` | `Base64 Encoded Private Key` | `Base64 Encoded Recipient Certificate`  
---|---|---|---  
**Standard email (no S/MIME)** | Leave empty | Leave empty | Leave empty  
**Digitally signed** | Required | Required | Leave empty  
**Encrypted** | Leave empty | Leave empty | Required  
**Signed and encrypted** | Required | Required | Required  
  
#### Convert certificate files to Base64

To encode your certificate and private key files into single-line Base64 strings for the action parameters, run the following commands:

**Linux and macOS:**
    
    
    base64 -w 0 sender_cert.crt
    base64 -w 0 sender_key.key
    

**Windows PowerShell:**
    
    
    [Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\path\to\certificate.crt"))
    [Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\path\to\private_key.key"))
    

#### Action inputs

The **Send Email** action requires the following parameters:

Parameter | Description  
---|---  
`Send From` | Required.An optional email address from which to send emails, if permissions allow.By default, the action sends emails from the default mailbox specified in the integration configuration.  
`Subject` | Required. The email subject.  
`Send to` | Required. A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | Optional A comma-separated list of email addresses for the email CC field. The format is the same as for the `Send to` parameter.  
`BCC` | Optional A comma-separated list of email addresses for the email BCC field. The format is the same as for the `Send to` parameter.  
`Attachments Paths` | Optional A comma-separated list of paths for file attachments stored on the server, such as `/FILE_DIRECTORY/file.pdf`, `/FILE_DIRECTORY/image.jpg`.  
`Attachments Location` | Required. A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket.The possible values are `GCP Bucket` or `Local File System`. The default value is `GCP Bucket`.  
`Mail Content Type` | Optional The type of the email content. The possible values are as follows:

  * `Text`
  * `HTML`

The default value is `Text`.  
`Mail Content` | Required. The email body.  
`Reply-To Recipients` | OptionalA comma-separated list of recipients to use in the _Reply-To_ header.Use the _Reply-To_ header to redirect reply emails to the specified email address instead of the sender's address in the **From** field.  
`Base64 Encoded Certificate` | Optional The Base64-encoded X.509 public certificate (`.cer`, `.crt`, `.pem`) of the sender (single-line format). Used for S/MIME digital signing. If provided, you must also provide `Base64 Encoded Private Key`.  
`Base64 Encoded Private Key` | Optional The Base64-encoded private key (`.key`, `.pem`) of the sender (single-line format). Used for S/MIME digital signing. Mandatory if `Base64 Encoded Certificate` is provided.  
`Base64 Encoded Recipient Certificate` | Optional The Base64-encoded public certificate (`.cer`, `.crt`, `.pem`) of the recipient (single-line format). Used for email encryption.  
  
#### Action outputs

The following table describes the output types associated with the **Send Email** action:

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

The **Send Email** action provides the following output messages:

Output message | Message description  
---|---  
`Email was sent successfully.` | Action succeeded.  
`Action failed to run because specified attachments were not found: ATTACHMENTS_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Send Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Email HTML

Use the **Send Email HTML** action to send emails you use the Google SecOps HTML template from a specific mailbox to an arbitrary list of recipients. With appropriate permissions, the action can send emails from a mailbox other than the default one.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Email HTML** action requires the following parameters:

Parameter | Description  
---|---  
`Send From` | Required.An optional email address from which to send emails, if permissions allow.By default, the action sends emails from the default mailbox specified in the integration configuration.  
`Subject` | Required. The email subject.  
`Send to` | Required. A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | Optional A comma-separated list of email addresses for the email CC field. The format is the same as for the `Send to` parameter.  
`BCC` | Optional A comma-separated list of email addresses for the email BCC field. The format is the same as for the `Send to` parameter.  
`Attachments Paths` | Optional A full path for the attachment to provide, such as `/FILE_DIRECTORY/file.pdf`, `/FILE_DIRECTORY/image.jpg`.You can provide multiple values in a comma-separated string.  
`Email HTML Template` | Required. The type of the HTML template to use. The possible values are `Email HTML Template` and `Dynamically generated list of available templates`. The default value is `Email HTML Template`.  
`Mail Content` | Required. The email body.  
`Reply-To Recipients` | OptionalA comma-separated list of recipients to use in the _Reply-To_ header.Use the _Reply-To_ header to redirect reply emails to the specific email address instead of the sender's address stated in the _From_ field.  
`Attachment Location` | Required.A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket.The possible values are `GCP Bucket` or `Local File System`. The default value is `GCP Bucket`.  
  
#### Action outputs

The **Send Email HTML** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Send Email HTML** action:
    
    
    {
        "createdDateTime": "2024-01-30T16:50:27Z",
        "lastModifiedDateTime": "2024-01-30T16:50:27Z",
        "changeKey": "example-key",
        "categories": [],
        "receivedDateTime": "2024-01-30T16:50:27Z",
        "sentDateTime": "2024-01-30T16:50:27Z",
        "hasAttachments": false,
        "internetMessageId": "outlook.com",
        "subject": "Testing",
        "bodyPreview": "example",
        "importance": "normal",
        "parentFolderId": "ID",
        "conversationId": "ID",
        "conversationIndex": "INDEX",
        "isDeliveryReceiptRequested": false,
        "isReadReceiptRequested": false,
        "isRead": true,
        "isDraft": false,
        "webLink": "https://example.com",
        "inferenceClassification": "focused",
        "body": {
            "contentType": "html",
            "content": "content"
        },
        "sender": {
            "emailAddress": {
                "name": "NAME",
                "address": "sender@example.com"
            }
        },
        "from": {
            "emailAddress": {
                "name": "NAME",
                "address": "user@example.com"
            }
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "name": "NAME",
                    "address": "recipient@example.com"
                }
            }
        ],
        "ccRecipients": [],
        "bccRecipients": [],
        "replyTo": [],
        "uniqueBody": {
            "contentType": "html",
            "content": "content"
        },
        "flag": {
            "flagStatus": "notFlagged"
        },
        "id": "ID"
    }
    

##### Output messages

On a Case Wall, the **Send Email HTML** action provides the following output messages:

Output message | Message description  
---|---  
`Email was sent successfully.` | Action succeeded.  
`Action failed to run because the HTML template was not specified.` `Action failed to run because the following specified attachments were not found: ATTACHMENT_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Send Email HTML** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Thread Reply

Use the **Send Thread Reply** action to send a message as a reply to the email thread. With appropriate permissions, the action can send emails from a mailbox other than the one specified in the integration configuration.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Thread Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Send From` | Required.An optional email address from which to send emails, if permissions allow.By default, the action sends emails from the default mailbox specified in the integration configuration.  
`Mail ID` | Required. The email ID to search for.  
`Folder Name` | OptionalA mailbox folder where to search for email. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`. The default value is `Inbox`.  
`Attachments Paths` | Optional A comma-separated list of paths for file attachments stored on the server, such as `/FILE_DIRECTORY/file.pdf`, `/FILE_DIRECTORY/image.jpg`.  
`Mail Content` | Required. The email body.  
`Reply All` | OptionalIf selected, the action sends a reply to all recipients related to the original email. Not selected by default. This parameter has priority over the `Reply To` parameter.  
`Reply To` | OptionalA comma-separated list of emails to send the reply to.If you provide no value and the `Reply All` checkbox is clear, the action only sends a reply to the original email sender. If the `Reply All` checkbox is selected, the action ignores this parameter.  
`Attachments Location` | Required. A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket.The possible values are `GCP Bucket` or `Local File System`. The default value is `GCP Bucket`.  
`Message Timezone` | Optional. The timezone used for the original email sent date in the reply header (such as `UTC`, `America/New_York`, or `Europe/London`). If the provided value isn't valid, the default value is used. The default value is `UTC`.  
  
#### Action outputs

The following table describes the output types associated with the **Send Thread Reply** action:

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

The following example shows the JSON result output received when using the **Send Thread Reply** action:
    
    
      {
        "id": "yyyy",
        "createdDateTime": "2024-02-02T10:57:18Z",
        "lastModifiedDateTime": "2024-02-02T10:57:23Z",
        "changeKey": "dsf+oAAQLaPjk",
        "categories": [],
        "receivedDateTime": "2024-02-02T10:57:20Z",
        "sentDateTime": "2024-02-02T10:57:19Z",
        "hasAttachments": true,
        "internetMessageId": "sdfhsjdfhjsdjfd",
        "subject": "RE: reply checking",
        "bodyPreview": "Reply check kr",
        "importance": "normal",
        "parentFolderId": "id",
        "conversationId": "id",
        "conversationIndex": "sdghfjfke",
        "isDeliveryReceiptRequested": false,
        "isReadReceiptRequested": false,
        "isRead": true,
        "isDraft": false,
        "webLink": "https://www.example.com/about",
        "inferenceClassification": "focused",
        "body": {
          "contentType": "text",
          "content": "Reply check kr"
        },
        "sender": {
          "emailAddress": {
            "name": "aff",
            "address": "ddxsm@a.com"
          }
        },
        "from": {
          "emailAddress": {
            "name": "fasf",
            "address": "ddxsm@a.com"
          }
        },
        "toRecipients": [
          {
            "emailAddress": {
              "name": "wf",
              "address": "ddxsm@a.com"
            }
          }
        ],
        "ccRecipients": [],
        "bccRecipients": [],
        "replyTo": [],
        "uniqueBody": {
          "contentType": "html",
          "content": "Reply check"
        },
        "flag": {
          "flagStatus": "notFlagged"
        }
      }
    

##### Output messages

The **Send Thread Reply** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully sent reply to the mail with ID: EMAIL_ID` | Action succeeded.  
`Error executing action "Send Thread Reply". Reason: if you want to send a reply only to your own email address, you need to work with "Reply To" parameter.` | Action failed.Check the `Reply To` parameter value.  
`Error executing action "Send Thread Reply" because the provided mail id EMAIL_ID was not found.` `Action failed to run because specified attachments were not found: ATTACHMENTS_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Send Thread Reply** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Vote Email

Use the **Send Vote Email** action to send emails with the predefined answering options. This action uses Google SecOps HTML templates to format the email. With appropriate permissions, the **Send Vote Email** action can send emails from a mailbox other than the default one.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Send Vote Email** action requires the following parameters:

Parameter | Description  
---|---  
`Send From` | Required.An optional email address from which to send emails, if permissions allow.By default, the action sends emails from the default mailbox specified in the integration configuration.  
`Subject` | Required. The email subject.  
`Send to` | Required. A comma-separated list of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.  
`CC` | Optional A comma-separated list of email addresses for the email CC field. The format is the same as for the `Send to` parameter.  
`BCC` | Optional A comma-separated list of email addresses for the email BCC field. The format is the same as for the `Send to` parameter.  
`Attachments Paths` | Optional A full path for the attachment to provide, such as `/FILE_DIRECTORY/file.pdf`, `/FILE_DIRECTORY/image.jpg`.You can provide multiple values in a comma-separated string.  
`Email HTML Template` | Required. The type of the HTML template to use. The possible values are `Email HTML Template` and `Dynamically generated list of available templates`. The default value is `Email HTML Template`.  
`Reply-To Recipients` | OptionalA comma-separated list of recipients to use in the _Reply-To_ header.Use the _Reply-To_ header to redirect reply emails to the specified email address instead of the sender's address stated in the **From** field.  
`Structure of voting options` | Required.The structure of the vote to send to recipients. The possible values are `Yes/No` or `Approve/Reject`. The default value is `Yes/No`.   
`Attachment Location` | Required.A location where the attachments are stored. By default, the action attempts to upload the attachment from the Cloud Storage bucket.The possible values are `GCP Bucket` or `Local File System`. The default value is `GCP Bucket`.  
  
#### Action outputs

The **Send Vote Email** action provides the following outputs:

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

The following example describes the JSON result output received when you use the **Send Vote Email** action:
    
    
    {
        "createdDateTime": "2024-01-30T16:50:27Z",
        "lastModifiedDateTime": "2024-01-30T16:50:27Z",
        "changeKey": "KEY",
        "categories": [],
        "receivedDateTime": "2024-01-30T16:50:27Z",
        "sentDateTime": "2024-01-30T16:50:27Z",
        "hasAttachments": false,
        "internetMessageId": "<example-message-ID>",
        "subject": "Testing",
        "bodyPreview": "example",
        "importance": "normal",
        "parentFolderId": "FOLDER_ID",
        "conversationId": "CONVERSATION_ID",
        "conversationIndex": "CONVERSATION_INDEX",
        "isDeliveryReceiptRequested": false,
        "isReadReceiptRequested": false,
        "isRead": true,
        "isDraft": false,
        "webLink": "https://www.example.com/about",
        "inferenceClassification": "focused",
        "body": {
            "contentType": "html",
            "content": "content"
        },
        "sender": {
            "emailAddress": {
                "name": "NAME",
                "address": "sender@example.com"
            }
        },
        "from": {
            "emailAddress": {
                "name": "NAME",
                "address": "user@example.com"
            }
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "name": "NAME",
                    "address": "recipient@example.com"
                }
            }
        ],
        "ccRecipients": [],
        "bccRecipients": [],
        "replyTo": [],
        "uniqueBody": {
            "contentType": "html",
            "content": "content"
        },
        "flag": {
            "flagStatus": "notFlagged"
        },
        "id": "ID"
    }
    

##### Output messages

On a Case Wall, the **Send Vote Email** action provides the following output messages:

Output message | Message description  
---|---  
`Email was sent successfully.` | Action succeeded.  
`Action failed to run because the HTML template was not specified.` `Action failed to run because the following specified attachments were not found: ATTACHMENT_LIST` `Failed to execute action, the error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Send Vote Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Wait For Email From User

Use the **Wait For Email From User** action to wait for the user's response based on an email sent using the **Send Email** action.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE as needed. Setting the timeout to `0` or leaving it empty uses the default timeout configured in environment settings.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Wait For Email From User** action requires the following parameters:

Parameter | Description  
---|---  
`Mail ID` | _Mandatory_ The ID or `internetMessageId` of the email that the action will wait for. If you used the **Send Email** action to send emails, set the parameter value to either the `{SendEmail.JSONResult|id}` or `{SendEmail.JSONResult|internetMessageId}` placeholder.  
`Mail Date` | _Optional_ Send timestamp of the email that the action waits for. If the message was sent using the **Send Email** action, select the `{SendEmail.JSONResult|sentDateTime}` or `{SendEmail.JSONResult|createdDateTime}` field as a placeholder.  
`Mail Recipients` | _Optional_ Comma-separated list of recipient email addresses whose response the action waits for. If the message was sent using the **Send Email** action, select the `{SendEmail.JSONResult|toRecipients}` field as a placeholder.  
`How long to wait for recipient reply (minutes)` | _Optional_ How long in minutes to wait for the user's reply before marking it timed out. Default is `10080`.  
`Wait for All Recipients to Reply?` | _Optional_ If selected, the action waits for responses from all recipients until reaching timeout or proceeding with the first reply. Not selected by default.  
`Wait Stage Exclude pattern` | _Optional_ A regular expression to exclude specific replies from the wait stage. This parameter works both with the email subject and body. For example, if you configure the `Out of Office.*` regular expression, the action doesn't consider automatic out-of-office messages as recipient replies and waits for an actual user reply.  
`Folder to Check for Reply` | _Optional_ A mailbox email folder to search for incoming recipient replies. The search is run in the mailbox from which the email containing a question was sent. Supports nested subfolders using the `/` forward slash (for example, `Inbox/Subfolder`). This parameter is case-sensitive. Default is `Inbox`.  
`Fetch Response Attachments` | _Optional_ If selected and the recipient reply contains attachments, the action fetches the reply and adds it as an attachment to the action result. Not selected by default.  
`Limit the Amount of Information Returned in the JSON Result` | _Optional_ If selected, the amount of information returned by the action is limited only to key email fields. Selected by default.  
`Disable the Action JSON Result` | _Optional_ If selected, the action doesn't return a JSON result. Not selected by default.  
  
#### Action outputs

The **Wait For Email From User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### Case wall attachment

The following Case Wall attachment is associated with the **Wait For Email From User** action:

Type: Entity

Attachment content: Title, Filename (extensions included, if any), fileContent.

  * Title: `RECIPIENT_EMAIL` reply attachment.
  * Filename: `ATTACHMENT_FILENAME` \+ `FILE_EXTENSION`
  * fileContent: `CONTENT_OF_THE_ATTACHED_FILE`



##### Case wall table

The **Wait For Email From User** action can generate the following table:

Table title: **Matching Mails**

Columns:

  * **Mail ID**
  * **Received Date**
  * **Sender**
  * **Recipients**
  * **Subject**



##### Script result

The following table lists the value for the script result output when using the **Wait For Email From User** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Wait For Email From User** action provides the following output messages:

Output message | Message description  
---|---  
`Found the user EMAIL_RECIPIENT reply: USER_REPLY``Timeout getting reply from user: EMAIL_RECIPIENT.` | Action succeeded.  
`Action failed to receive any replies until timeout.``Failed to execute action, the error is: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Wait For Vote Email Results

Use the **Wait For Vote Email Results** action to wait for the user response based on the vote email sent using the **Send Vote Email** action.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Wait For Vote Email Results** action requires the following parameters:

Parameter | Description  
---|---  
`Vote Mail Sent From` | Required.The mailbox from which the **Send Vote Email** action sent an email. The default value is the mailbox that you specified in the integration configuration. Optionally, you can set a different value for this parameter if the vote mail is sent from a different mailbox.  
`Mail ID` | Required. The ID of the email.If the email is sent using the `Send Vote Email` action, set the parameter value to either the `SendVoteEmail.JSONResult|id` or `SendEmail.JSONResult|internetMessageId` placeholder. To return email IDs, you can use the **Search Emails** action.  
`Wait for All Recipients To Reply?` | Optional If selected, the action waits for responses from all recipients until reaching timeout or proceeding with the first reply. Enabled by default.  
`Wait Stage Exclude Pattern` | Optional A regular expression to exclude specific replies from the wait stage. This parameter works with the email body. Example: the action doesn't consider automatic out-of-office messages as recipient replies, instead waiting for an actual user reply.  
`Folder To Check For Reply` | Optional A mailbox email folder to search for the user's reply. The search is run in the mailbox from which the email containing a question was sent. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. This parameter is case-sensitive. The default value is `Inbox`.  
`Folder To Check For Sent Mail` | OptionalA mailbox folder to search for the sent mail in. It is a mailbox that you sent the email with a question from.This parameter accepts a comma-separated list of folders to check the user response in multiple folders.This parameter is case sensitive. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.The default value is `Sent Items`.  
`Fetch Response Attachments` | Optional If selected and the recipient reply contains attachments, the action fetches the reply and adds it as an attachment to the Case Wall. Not selected by default.  
  
#### Action outputs

The **Wait For Vote Email Results** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall attachment

The following Case Wall attachment is associated with the **Wait For Vote Email Results** action:

Type: Entity

Attachment content: Title, Filename (extensions included, if any), fileContent.

  * Title: `RECIPIENT_EMAIL` reply attachment.
  * Filename: `ATTACHMENT_FILENAME ` \+ `FILE_EXTENSION`
  * fileContent: ` CONTENT_OF_THE_ATTACHED_FILE`



##### Case wall table

On a Case Wall, the **Wait For Email Results** action generates the following table:

Table title: **Matching Mails**

Columns:

  * **Mail ID**
  * **Received Date**
  * **Sender**
  * **Recipients**
  * **Subject**



##### JSON result

The following example describes the JSON result output received when you use the **Wait For Vote Email Results** action:
    
    
    {
        "Responses": [
            {
                "recipient": "user@example.com",
                "vote": "Approve"
            }
        ]
    }
    

##### Output messages

The **Wait For Vote Email Results** action provides the following output messages:

Output message | Message description  
---|---  
`Found the user  EMAIL_RECIPIENT reply:  USER_REPLY.` `Exceeded timeout to get a reply from user: EMAIL_RECIPIENT.` | Action succeeded.  
`Action failed to receive any replies until timeout.` `Failed to execute action, the error is:  ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when you use the **Wait For Vote Email Results** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Microsoft Graph Mail Connector

Use the **Microsoft Graph Mail Connector** to retrieve emails from the Microsoft Graph mail service. 

Use the dynamic list to filter the specified values from the email body and subject parts using regular expressions. By default, the connector uses a regular expression to filter out the URLs from the email.

#### Connector inputs

The **Microsoft Graph Mail Delegated Connector** requires the following parameters: Parameter | Description  
---|---  
`Product Field Name` | Required.The name of the field where the product name is stored.The default value is `device_product`.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `device_product` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.  
`Event Field Name` | Required.The field name used to determine the event name (subtype).The default value is `event_name`.  
`Environment Field Name` | Optional The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | Optional A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Email Exclude Pattern` | OptionalA regular expression to exclude specific emails from ingestion, such as spam or news. This parameter works with both the subject and body of the email.  
`PythonProcessTimeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script.The default value is `300`.  
`Azure AD Endpoint` | Required.The Microsoft Entra endpoint to use in the integration. The default value is `https://login.microsoftonline.com`.  
`Microsoft Graph Endpoint` | Required.The Microsoft Graph endpoint to use in the integration. The default value is `https://graph.microsoft.com`.  
`Mail Address` | Required.An email address for the connector to use.  
`Client ID` | Required.An application (client) ID of the Microsoft Entra application.  
`Secret ID` | Required.The client secret value of the Microsoft Entra application.  
`Tenant (Directory) ID` | Required.The Microsoft Entra ID (tenant ID) value.  
`Folder to check for emails` | Required.An email folder to search for the emails. This parameter accepts a comma-separated list of folders to search for the user response in multiple folders. To specify a subfolder, use the `/` forward slash, such as `Inbox/Subfolder`.This parameter is case-sensitive.The default value is `Inbox`.  
`Offset Time In Hours` | Required. The number of hours before the first connector iteration to retrieve emails. This parameter applies to the initial connector iteration after you enable the connector for the first time. The connector can use this parameter as a fallback value when the timestamp from the latest connector iteration expires.The default value is `24`.  
`Max Emails Per Cycle` | Required. The number of emails to fetch for every connector iteration. The default value is `10`.  
`Unread Emails Only` | Optional If selected, the connector creates cases only from unread emails. Not selected by default.  
`Mark Emails as Read` | Optional If selected, the connector marks emails as read after ingesting. Not selected by default.  
`Disable Overflow` | OptionalIf selected, the connector ignores the Google SecOps overflow mechanism.Not selected by default.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to Microsoft Graph. Enabled by default.  
`Original Received Mail Prefix` | OptionalA prefix to add to the extracted event keys (for example, `to`, `from`, or `subject`) from the original email received in the monitored mailbox. The default value is `orig`.  
`Attached Mail File Prefix` | OptionalA prefix to add to the extracted event keys (for example, `to`, `from`, or `subject`) from the attached email file received in the monitored mailbox. The default value is `attach`.  
`Create a Separate Google Secops Alert per Attached Mail File` | OptionalIf selected, the connector creates multiple alerts, with one alert for every attached email file.This behavior is useful when you process emails with multiple email files attached and set the Google SecOps event mapping to create entities from attached email files.Not selected by default.  
`Attach Original EML` | OptionalIf selected, the connector attaches the original email to the case info as an EML file.Not selected by default.  
`Headers to add to events` | OptionalA comma-separated string of email headers to add to Google SecOps events, such as `DKIM-Siganture`, `Received`, or `From`.You can configure an exact match for headers or set this parameter value as a regular expression. The connector filters the configured values from the `internetMessageHeaders` list and adds them to the Google SecOps event.To prevent the connector from adding headers to the event, set the parameter value as follows: `None`.By default, the connector adds all available headers.  
`Case Name Template` | OptionalA custom case name.When you configure this parameter, the connector adds a new key called `custom_case_name` to the Google SecOps SOAR event. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps SOAR event. The connector only handles keys containing the string value.  
`Alert Name Template` | OptionalA custom alert name. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps SOAR event. The connector only handles keys containing the string value. If you provide no value or an invalid template, the connector uses the default alert name.  
`Proxy Server Address` | OptionalThe address of the proxy server to use.  
`Proxy Username` | OptionalThe proxy username to authenticate with.  
`Proxy Password` | OptionalThe proxy password to authenticate with.  
`Mail Field Source` | OptionalIf selected, the integration retrieves the mailbox address from the user details `mail` attribute. If not selected, the integration retrieves the mailbox address from the `userPrincipalName` field. Not selected by default.  
`Extract URLs from HTML Email Part` | Optional If selected, the connector extracts URLs from the HTML body of the email. This allows the connector to extract complex URLs, but doesn't extract URLs from the plain-text part of the email. Extracted URLs are available in the `urls_from_html_part` event field. Enabled by default.  
`Event Fields to Exclude` | Optional A comma-separated list of event fields to exclude from event creation (such as `field1,field2`).  
`Exclude Attachments` | Optional If selected, the connector doesn't ingest email attachments or add them to cases.  
`Bypass S/MIME Signature Verification` | Optional If selected, the connector ingests S/MIME-signed emails without requiring a Base64-encoded CA certificate for signature verification. The message body, headers, and attachments are extracted directly.  
`Base64 Encoded Private Key` | Optional The Base64-encoded private key used to decrypt incoming S/MIME encrypted emails. If provided, you must also provide `Base64 Encoded Certificate`.  
`Base64 Encoded Certificate` | Optional The Base64-encoded certificate used to decrypt incoming S/MIME encrypted emails. If provided, you must also provide `Base64 Encoded Private Key`.  
`Base64 Encoded CA certificate` | Optional The Base64-encoded trusted CA certificate for verifying the digital signatures of incoming S/MIME emails. If no CA certificate is provided, signature verification for incoming signed emails fails unless `Bypass S/MIME Signature Verification` is enabled.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
